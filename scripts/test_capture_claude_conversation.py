#!/usr/bin/env python3
"""Tests for the Claude conversation capture hook."""

from __future__ import annotations

import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).with_name("capture-claude-conversation.py")


def load(inbox: Path, state: Path):
    os.environ["BARALUGA_INBOX"] = str(inbox)
    os.environ["BARALUGA_CAPTURE_STATE"] = str(state)
    spec = importlib.util.spec_from_file_location("capture_claude_conversation", SCRIPT_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def entry(kind, content, ts, cwd="/Users/x/repos/smp", **extra):
    return {"type": kind, "timestamp": ts, "cwd": cwd, "message": {"role": kind, "content": content}, **extra}


class CaptureClaudeConversationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.cap = load(self.tmp / "inbox", self.tmp / "state")
        self.transcript = self.tmp / "s.jsonl"
        self.hook = {"session_id": "abcdef12-3456", "transcript_path": str(self.transcript), "cwd": "/Users/x/repos/smp"}

    def write(self, entries, partial=""):
        with self.transcript.open("a") as f:
            f.writelines(json.dumps(e) + "\n" for e in entries)
            f.write(partial)

    def test_keeps_only_conversation_text_split_by_manila_day(self) -> None:
        self.write([
            entry("user", "hello <system-reminder>noise</system-reminder>", "2026-10-11T15:50:00Z"),
            entry("assistant", [{"type": "thinking", "thinking": "hidden"}, {"type": "text", "text": "hi"}], "2026-10-11T15:51:00Z"),
            entry("assistant", [{"type": "tool_use", "name": "Bash"}], "2026-10-11T15:52:00Z"),
            entry("user", [{"type": "tool_result", "content": "output"}], "2026-10-11T15:53:00Z"),
            entry("user", "meta", "2026-10-11T15:54:00Z", isMeta=True),
            entry("user", "after midnight", "2026-10-11T16:05:00Z", cwd="/Users/x/repos/smp/smp-india"),
        ])
        files = sorted(p.name for p in self.cap.capture(self.hook))
        self.assertEqual(files, ["2026-10-11-claude-smp-abcdef12.txt", "2026-10-12-claude-smp-abcdef12.txt"])
        day1 = (self.tmp / "inbox" / files[0]).read_text()
        self.assertIn("Project: smp (/Users/x/repos/smp)", day1)
        self.assertIn("hello", day1)
        self.assertIn("hi", day1)
        for dropped in ("noise", "hidden", "Bash", "output", "meta"):
            self.assertNotIn(dropped, day1)
        self.assertIn("## 00:05 user (smp-india)", (self.tmp / "inbox" / files[1]).read_text())

    def test_incremental_runs_append_without_duplicates_and_wait_for_partial_lines(self) -> None:
        self.write([entry("user", "first", "2026-10-11T01:00:00Z")], partial='{"type": "user"')
        self.cap.capture(self.hook)
        self.transcript.write_text(self.transcript.read_text()[: -len('{"type": "user"')])
        self.write([entry("assistant", [{"type": "text", "text": "second"}], "2026-10-11T01:01:00Z")])
        self.cap.capture(self.hook)
        self.cap.capture(self.hook)
        text = (self.tmp / "inbox" / "2026-10-11-claude-smp-abcdef12.txt").read_text()
        self.assertEqual((text.count("first"), text.count("second"), text.count("# Claude Conversation")), (1, 1, 1))

    def test_redacts_obvious_secrets_and_labels_scratch_and_skips_subagents(self) -> None:
        scratch = "/Users/x/Library/Application Support/Claude/scratch-workspaces/a/b/scratch-1"
        self.write([entry("user", "password: hunter22 and ghp_" + "a" * 36, "2026-10-11T01:00:00Z", cwd=scratch)])
        self.assertEqual(self.cap.capture({**self.hook, "agent_id": "sub"}), [])
        (out,) = self.cap.capture(self.hook)
        text = out.read_text()
        self.assertTrue(out.name.startswith("2026-10-11-claude-scratch-"))
        self.assertNotIn("hunter22", text)
        self.assertNotIn("ghp_aaaa", text)


if __name__ == "__main__":
    unittest.main()
