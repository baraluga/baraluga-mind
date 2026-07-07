#!/usr/bin/env python3
"""Export local Codex user/assistant conversations into the vault inbox."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def read_titles(codex_home: Path) -> tuple[dict[str, str], dict[str, str]]:
    titles: dict[str, str] = {}
    updated: dict[str, str] = {}
    index_path = codex_home / "session_index.jsonl"
    if not index_path.exists():
        return titles, updated

    with index_path.open() as handle:
        for line in handle:
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue

            session_id = item.get("id")
            if not session_id:
                continue
            if item.get("thread_name"):
                titles[session_id] = item["thread_name"]
            if item.get("updated_at"):
                updated[session_id] = item["updated_at"]

    return titles, updated


def extract_sessions(codex_home: Path, capture_date: str) -> list[dict]:
    year, month, day = capture_date.split("-")
    session_dir = codex_home / "sessions" / year / month / day
    titles, updated = read_titles(codex_home)
    sessions: list[dict] = []

    for path in sorted(session_dir.glob("*.jsonl")):
        session_id = None
        cwd = None
        started = None
        messages: list[dict[str, str | None]] = []

        with path.open() as handle:
            for line in handle:
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue

                if event.get("type") == "session_meta":
                    payload = event.get("payload") or {}
                    session_id = payload.get("id") or payload.get("session_id") or session_id
                    cwd = payload.get("cwd") or cwd
                    started = payload.get("timestamp") or started
                    continue

                if event.get("type") != "response_item":
                    continue

                payload = event.get("payload") or {}
                if payload.get("type") != "message":
                    continue

                role = payload.get("role")
                if role not in {"user", "assistant"}:
                    continue

                parts = [
                    content["text"].strip()
                    for content in payload.get("content") or []
                    if content.get("type") in {"input_text", "output_text"} and content.get("text")
                ]
                text = "\n".join(part for part in parts if part).strip()
                if text:
                    messages.append(
                        {
                            "timestamp": event.get("timestamp"),
                            "role": role,
                            "text": text,
                        }
                    )

        if session_id or messages:
            sessions.append(
                {
                    "path": path,
                    "session_id": session_id or path.stem,
                    "title": titles.get(session_id or "", "(untitled)"),
                    "started": started,
                    "updated": updated.get(session_id or ""),
                    "cwd": cwd,
                    "messages": messages,
                }
            )

    return sessions


def render(capture_date: str, codex_home: Path, sessions: list[dict]) -> str:
    year, month, day = capture_date.split("-")
    session_dir = codex_home / "sessions" / year / month / day
    lines: list[str] = [
        f"# Codex Conversations - {capture_date}",
        "",
        "## Capture Summary",
        "",
        "Source type: mixed capture / Codex conversation export.",
        "",
        "This file is a daily inbox landing capture for Codex conversations. It preserves filtered user/assistant transcript text from local Codex session JSONL files. Tool calls, tool outputs, system prompts, developer prompts, and reasoning records are intentionally excluded from the transcript sections below.",
        "",
        "Facts:",
        f"- Capture date: `{capture_date}`",
        f"- Generated from local session directory: `{session_dir}`",
        f"- Sessions found: {len(sessions)}",
        "",
        "Inferences:",
        "- These are the Codex sessions stored locally under the date directory. They may not include conversations that were not synced or not present on this machine.",
        "",
        "## Preliminary Ingest Notes",
        "",
        "- Review for actions, decisions, open questions, durable project context, and names/acronyms needing confirmation.",
        "- Do not treat this preliminary capture as canonical action tracking until an ingest pass updates `actions.md`.",
        f"- Suggested post-ingest destination for this evidence file: `sources/codex-conversations/{capture_date}-codex-conversations.md` or another appropriate source folder.",
        "",
        "## Thread Index",
        "",
        "| Thread | Session | Started | Updated | Messages | CWD | Raw File |",
        "| --- | --- | --- | --- | ---: | --- | --- |",
    ]

    for session in sessions:
        user_count = sum(1 for message in session["messages"] if message["role"] == "user")
        assistant_count = sum(1 for message in session["messages"] if message["role"] == "assistant")
        lines.append(
            "| {title} | `{session_id}` | `{started}` | `{updated}` | {messages} | `{cwd}` | `{path}` |".format(
                title=session["title"],
                session_id=session["session_id"],
                started=session.get("started") or "",
                updated=session.get("updated") or "",
                messages=f"{user_count} user / {assistant_count} assistant",
                cwd=session.get("cwd") or "",
                path=session["path"],
            )
        )

    lines.extend(["", "## Transcript", ""])

    for session in sessions:
        lines.extend(
            [
                f"## {session['title']}",
                "",
                f"- Session: `{session['session_id']}`",
                f"- Started: `{session.get('started') or ''}`",
            ]
        )
        if session.get("updated"):
            lines.append(f"- Updated: `{session['updated']}`")
        if session.get("cwd"):
            lines.append(f"- CWD: `{session['cwd']}`")
        lines.extend([f"- Raw File: `{session['path']}`", ""])

        if not session["messages"]:
            lines.extend(["_No user/assistant transcript messages found._", ""])
            continue

        for message in session["messages"]:
            role = "User" if message["role"] == "user" else "Assistant"
            lines.extend(
                [
                    f"### {role} - {message.get('timestamp') or 'unknown time'}",
                    "",
                    message["text"],
                    "",
                ]
            )

    lines.extend([f"Last Updated: {capture_date}", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", help="Date to export in YYYY-MM-DD format. Defaults to local today.")
    parser.add_argument("--vault", default="/Users/qn5792/baraluga-mind", help="Path to the markdown vault.")
    parser.add_argument("--codex-home", default=str(Path.home() / ".codex"), help="Path to Codex state.")
    args = parser.parse_args()

    capture_date = args.date or __import__("datetime").date.today().isoformat()
    vault = Path(args.vault)
    codex_home = Path(args.codex_home)
    sessions = extract_sessions(codex_home, capture_date)

    inbox = vault / "inbox"
    inbox.mkdir(parents=True, exist_ok=True)
    output = inbox / f"{capture_date}-codex-conversations.md"
    output.write_text(render(capture_date, codex_home, sessions))
    print(output)
    print(f"sessions={len(sessions)}")


if __name__ == "__main__":
    main()
