#!/usr/bin/env python3
"""Tests for the Codex conversation exporter."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("export-codex-conversations.py")
SPEC = importlib.util.spec_from_file_location("export_codex_conversations", SCRIPT_PATH)
assert SPEC and SPEC.loader
EXPORTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EXPORTER)


class ExportCodexConversationsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.capture_date = "2026-07-30"
        self.codex_home = Path("/tmp/codex-test")
        self.unique_transcript_text = "raw transcript content that must stay out of markdown"
        self.sessions = [
            {
                "path": Path("/tmp/session.jsonl"),
                "session_id": "session-1",
                "title": "Test conversation",
                "started": "2026-07-30T00:00:00Z",
                "updated": "2026-07-30T00:05:00Z",
                "cwd": "/tmp/project",
                "messages": [
                    {
                        "timestamp": "2026-07-30T00:01:00Z",
                        "role": "user",
                        "text": self.unique_transcript_text,
                    }
                ],
            }
        ]

    def test_index_references_raw_transcript_without_embedding_messages(self) -> None:
        index = EXPORTER.render_index(
            self.capture_date,
            self.codex_home,
            self.sessions,
            "2026-07-30-codex-conversations.txt",
        )

        self.assertIn("Test conversation", index)
        self.assertIn("2026-07-30-codex-conversations.txt", index)
        self.assertNotIn(self.unique_transcript_text, index)

    def test_write_capture_preserves_transcript_as_text(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            vault = Path(temporary_directory)
            index_path, transcript_path = EXPORTER.write_capture(
                vault,
                self.capture_date,
                self.codex_home,
                self.sessions,
            )

            self.assertEqual(index_path.suffix, ".md")
            self.assertEqual(transcript_path.suffix, ".txt")
            self.assertIn(transcript_path.name, index_path.read_text(encoding="utf-8"))
            self.assertIn(
                self.unique_transcript_text,
                transcript_path.read_text(encoding="utf-8"),
            )
            self.assertNotIn(
                self.unique_transcript_text,
                index_path.read_text(encoding="utf-8"),
            )

    def test_select_meaningful_sessions_excludes_scheduled_automations(self) -> None:
        automation_session = {
            **self.sessions[0],
            "session_id": "automation-session",
            "messages": [
                {
                    "role": "user",
                    "text": "Automation: Daily Capture\nAutomation ID: daily-capture\nAutomation memory: /tmp/memory.md",
                }
            ],
        }

        selected = EXPORTER.select_meaningful_sessions(
            [automation_session, self.sessions[0]]
        )

        self.assertEqual(selected, self.sessions)

    def test_select_meaningful_sessions_excludes_sessions_without_user_text(self) -> None:
        assistant_only = {
            **self.sessions[0],
            "session_id": "assistant-only",
            "messages": [{"role": "assistant", "text": "background result"}],
        }

        self.assertEqual(EXPORTER.select_meaningful_sessions([assistant_only]), [])


if __name__ == "__main__":
    unittest.main()
