#!/usr/bin/env python3
"""Incrementally capture a Claude Code conversation into Baraluga Mind's inbox.

Runs as a Claude Code `Stop` / `SessionEnd` hook: reads the hook JSON from stdin,
appends user/assistant text added to the session transcript since the last run,
and writes one file per Asia/Manila day per session:

    inbox/YYYY-MM-DD-claude-<project>-<session8>.txt

Tool calls, tool results, thinking, and system reminders are dropped. Obvious
secrets are redacted before anything is written. The script never fails the hook:
errors go to stderr and it exits 0.
"""

from __future__ import annotations

import fcntl
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

INBOX = Path(os.environ.get("BARALUGA_INBOX", Path.home() / "baraluga-mind" / "inbox"))
STATE_DIR = Path(os.environ.get("BARALUGA_CAPTURE_STATE", Path.home() / ".cache" / "baraluga-mind" / "claude-capture"))
TZ = ZoneInfo("Asia/Manila")

REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
# ponytail: pattern-based redaction only catches obvious secrets; ingest must still watch for others.
REDACTIONS = [
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----", re.S), "[REDACTED: private key]"),
    (re.compile(r"(?i)\b(bearer)\s+[A-Za-z0-9._~+/=-]{16,}"), r"\1 [REDACTED]"),
    (re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"), "[REDACTED: aws key]"),
    (re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9_-]{20,}|xox[abpr]-[A-Za-z0-9-]{10,})"), "[REDACTED: token]"),
    (re.compile(r"(?i)\b(password|passwd|pwd|secret|api[_-]?key|access[_-]?token|token)(\s*[:=]\s*)[\"']?[^\s\"']{4,}"), r"\1\2[REDACTED]"),
]


def redact(text: str) -> str:
    for pattern, replacement in REDACTIONS:
        text = pattern.sub(replacement, text)
    return text


def project_label(root: str) -> str:
    if "/scratch-workspaces/" in root:
        return "scratch"
    return re.sub(r"[^a-z0-9]+", "-", Path(root).name.lower()).strip("-") or "unknown"


def message_text(entry: dict) -> str | None:
    """Return the human-readable text of a user or assistant entry, else None."""
    if entry.get("type") not in ("user", "assistant") or entry.get("isMeta") or entry.get("isSidechain"):
        return None
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, str):
        parts = [content]
    elif isinstance(content, list):
        parts = [b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text"]
    else:
        return None
    text = REMINDER.sub("", "\n\n".join(parts)).strip()
    return text or None


def read_new_entries(transcript: Path, offset: int) -> tuple[list[dict], int]:
    """Parse complete JSONL lines after `offset`; a trailing partial line waits for the next run."""
    with transcript.open("rb") as f:
        f.seek(offset)
        data = f.read()
    end = data.rfind(b"\n") + 1
    entries = []
    for line in data[:end].splitlines():
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return entries, offset + end


def capture(hook: dict) -> list[Path]:
    if hook.get("agent_id"):
        return []
    session_id = hook["session_id"]
    transcript = Path(hook["transcript_path"])
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with (STATE_DIR / f"{session_id}.json").open("a+") as state_file:
        fcntl.flock(state_file, fcntl.LOCK_EX)
        state_file.seek(0)
        state = json.loads(state_file.read() or "{}")
        entries, state["offset"] = read_new_entries(transcript, state.get("offset", 0))
        written: dict[Path, list[str]] = {}
        for entry in entries:
            if "root" not in state and entry.get("cwd"):
                state["root"] = entry["cwd"]
            text = message_text(entry)
            if not text or not entry.get("timestamp"):
                continue
            root = state.get("root") or hook.get("cwd", "")
            local = datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00")).astimezone(TZ)
            out = INBOX / f"{local:%Y-%m-%d}-claude-{project_label(root)}-{session_id[:8]}.txt"
            if out not in written and not out.exists():
                written[out] = [
                    f"# Claude Conversation - {local:%Y-%m-%d}\n\n"
                    f"Project: {project_label(root)} ({root})\n"
                    f"Session: `{session_id}`\nTranscript: `{transcript}`\n"
                    f"Resume: `claude --resume {session_id}`\n"
                ]
            cwd = entry.get("cwd") or root
            where = "" if cwd == root or not cwd.startswith(root) else f" ({os.path.relpath(cwd, root)})"
            written.setdefault(out, []).append(f"\n## {local:%H:%M} {entry['type']}{where}\n\n{redact(text)}\n")
        INBOX.mkdir(parents=True, exist_ok=True)
        for out, chunks in written.items():
            with out.open("a") as f:
                f.write("".join(chunks))
        state_file.seek(0)
        state_file.truncate()
        state_file.write(json.dumps(state))
    return list(written)


def main() -> None:
    try:
        capture(json.load(sys.stdin))
    except Exception as exc:  # never break the user's session over a capture failure
        print(f"baraluga capture skipped: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
