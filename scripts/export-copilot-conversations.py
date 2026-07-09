#!/usr/bin/env python3
"""Export local GitHub Copilot conversations into the vault inbox."""

from __future__ import annotations

import argparse
import json
import sqlite3
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


LOCAL_TZ = ZoneInfo("Asia/Manila")


def parse_timestamp(value: str | None) -> datetime | None:
    if not value:
        return None
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        return datetime.fromisoformat(normalized)
    except ValueError:
        return None


def local_date(value: str | None) -> str | None:
    parsed = parse_timestamp(value)
    if parsed is None:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=LOCAL_TZ)
    return parsed.astimezone(LOCAL_TZ).date().isoformat()


def clean_message(text: str | None) -> str:
    return (text or "").strip()


def read_workspace_yaml(path: Path) -> dict[str, str]:
    metadata: dict[str, str] = {}
    if not path.exists():
        return metadata

    for line in path.read_text(errors="replace").splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata


def read_cli_session_store(copilot_home: Path) -> dict[str, dict[str, str]]:
    db_path = copilot_home / "session-store.db"
    if not db_path.exists():
        return {}

    sessions: dict[str, dict[str, str]] = {}
    uri = f"file:{db_path}?mode=ro"
    try:
        with sqlite3.connect(uri, uri=True) as conn:
            conn.row_factory = sqlite3.Row
            for row in conn.execute(
                """
                select id, cwd, repository, branch, summary, created_at, updated_at
                from sessions
                """
            ):
                sessions[row["id"]] = {key: row[key] or "" for key in row.keys()}
    except sqlite3.Error:
        return {}

    return sessions


def extract_cli_sessions(copilot_home: Path, capture_date: str) -> list[dict]:
    session_root = copilot_home / "session-state"
    store_metadata = read_cli_session_store(copilot_home)
    sessions: list[dict] = []

    for events_path in sorted(session_root.glob("*/events.jsonl")):
        session_id = events_path.parent.name
        workspace = read_workspace_yaml(events_path.parent / "workspace.yaml")
        store = store_metadata.get(session_id, {})
        metadata: dict[str, str] = {
            "session_id": session_id,
            "title": store.get("summary") or workspace.get("name") or "(untitled)",
            "cwd": store.get("cwd") or workspace.get("cwd") or "",
            "repository": store.get("repository") or workspace.get("repository") or "",
            "branch": store.get("branch") or workspace.get("branch") or "",
            "created": store.get("created_at") or workspace.get("created_at") or "",
            "updated": store.get("updated_at") or workspace.get("updated_at") or "",
            "model": "",
            "producer": "",
        }
        messages: list[dict[str, str]] = []
        seen_dates: set[str] = set()

        with events_path.open(errors="replace") as handle:
            for line in handle:
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue

                timestamp = event.get("timestamp")
                event_date = local_date(timestamp)
                if event_date:
                    seen_dates.add(event_date)

                data = event.get("data") or {}
                event_type = event.get("type")

                if event_type == "session.start":
                    metadata["created"] = data.get("startTime") or metadata["created"]
                    metadata["model"] = data.get("selectedModel") or metadata["model"]
                    metadata["producer"] = data.get("producer") or metadata["producer"]
                    context = data.get("context") or {}
                    metadata["cwd"] = metadata["cwd"] or context.get("cwd") or ""
                    metadata["repository"] = metadata["repository"] or context.get("repository") or ""
                    metadata["branch"] = metadata["branch"] or context.get("branch") or ""
                    continue

                if event_type not in {"user.message", "assistant.message"}:
                    continue

                if event_date != capture_date:
                    continue

                role = "user" if event_type == "user.message" else "assistant"
                text = clean_message(data.get("content"))
                if not text:
                    continue

                messages.append(
                    {
                        "timestamp": timestamp or "",
                        "role": role,
                        "text": text,
                    }
                )

        if capture_date in seen_dates or messages:
            sessions.append(
                {
                    "source": "Copilot CLI",
                    "path": events_path,
                    "session_id": session_id,
                    "title": metadata["title"],
                    "started": metadata["created"],
                    "updated": metadata["updated"],
                    "cwd": metadata["cwd"],
                    "repository": metadata["repository"],
                    "branch": metadata["branch"],
                    "model": metadata["model"],
                    "producer": metadata["producer"],
                    "messages": messages,
                }
            )

    return sessions


def read_vscode_workspace(path: Path) -> str:
    workspace_json = path / "workspace.json"
    if not workspace_json.exists():
        return ""

    try:
        data = json.loads(workspace_json.read_text(errors="replace"))
    except json.JSONDecodeError:
        return ""

    return data.get("folder") or data.get("workspace") or ""


def extract_vscode_sessions(code_support: Path, capture_date: str) -> list[dict]:
    workspace_root = code_support / "User" / "workspaceStorage"
    sessions: list[dict] = []

    for transcripts_dir in sorted(workspace_root.glob("*/GitHub.copilot-chat/transcripts")):
        workspace = read_vscode_workspace(transcripts_dir.parent.parent)
        for path in sorted(transcripts_dir.glob("*.jsonl")):
            session_id = path.stem
            metadata: dict[str, str] = {
                "session_id": session_id,
                "title": "(untitled)",
                "started": "",
                "updated": "",
                "cwd": workspace,
                "repository": "",
                "branch": "",
                "model": "",
                "producer": "",
            }
            messages: list[dict[str, str]] = []
            seen_dates: set[str] = set()

            with path.open(errors="replace") as handle:
                for line in handle:
                    try:
                        event = json.loads(line)
                    except json.JSONDecodeError:
                        continue

                    timestamp = event.get("timestamp")
                    event_date = local_date(timestamp)
                    if event_date:
                        seen_dates.add(event_date)

                    data = event.get("data") or {}
                    event_type = event.get("type")

                    if event_type == "session.start":
                        metadata["started"] = data.get("startTime") or timestamp or metadata["started"]
                        metadata["model"] = data.get("selectedModel") or metadata["model"]
                        metadata["producer"] = data.get("producer") or metadata["producer"]
                        continue

                    if event_type not in {"user.message", "assistant.message"}:
                        continue

                    if event_date != capture_date:
                        continue

                    role = "user" if event_type == "user.message" else "assistant"
                    text = clean_message(data.get("content"))
                    if not text:
                        continue

                    messages.append(
                        {
                            "timestamp": timestamp or "",
                            "role": role,
                            "text": text,
                        }
                    )
                    metadata["updated"] = timestamp or metadata["updated"]

            if capture_date in seen_dates or messages:
                sessions.append(
                    {
                        "source": "VS Code Copilot Chat",
                        "path": path,
                        "session_id": session_id,
                        "title": metadata["title"],
                        "started": metadata["started"],
                        "updated": metadata["updated"],
                        "cwd": metadata["cwd"],
                        "repository": metadata["repository"],
                        "branch": metadata["branch"],
                        "model": metadata["model"],
                        "producer": metadata["producer"],
                        "messages": messages,
                    }
                )

    return sessions


def count_messages(session: dict, role: str) -> int:
    return sum(1 for message in session["messages"] if message["role"] == role)


def render(capture_date: str, copilot_home: Path, code_support: Path, sessions: list[dict]) -> str:
    lines: list[str] = [
        f"# GitHub Copilot Conversations - {capture_date}",
        "",
        "## Capture Summary",
        "",
        "Source type: mixed capture / GitHub Copilot conversation export.",
        "",
        "This file is a daily inbox landing capture for GitHub Copilot conversations. It preserves filtered user/assistant transcript text from local Copilot state. Tool calls, tool outputs, system prompts, developer prompts, hidden reasoning records, and encrypted payloads are intentionally excluded from the transcript sections below.",
        "",
        "Facts:",
        f"- Capture date: `{capture_date}`",
        f"- Copilot CLI state directory: `{copilot_home / 'session-state'}`",
        f"- Copilot CLI session metadata DB: `{copilot_home / 'session-store.db'}`",
        f"- VS Code Copilot Chat workspace storage root: `{code_support / 'User' / 'workspaceStorage'}`",
        f"- Sessions found: {len(sessions)}",
        "",
        "Inferences:",
        "- These are the GitHub Copilot sessions stored locally on this machine. They may not include cloud-only conversations, browser conversations, conversations from other machines, or chats not persisted by the client.",
        "- `Copilot CLI` sessions come from `~/.copilot/session-state`; `VS Code Copilot Chat` sessions come from VS Code workspace transcript files.",
        "",
        "## Preliminary Ingest Notes",
        "",
        "- Review for actions, decisions, open questions, durable project context, and names/acronyms needing confirmation.",
        "- Do not treat this preliminary capture as canonical action tracking until an ingest pass updates `actions.md`.",
        f"- Suggested post-ingest destination for this evidence file: `sources/copilot-conversations/{capture_date}-copilot-conversations.md` or another appropriate source folder.",
        "",
        "## Session Index",
        "",
        "| Source | Title | Session | Started | Updated | Model | Messages | CWD | Repository | Branch | Raw File |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- |",
    ]

    for session in sessions:
        lines.append(
            "| {source} | {title} | `{session_id}` | `{started}` | `{updated}` | `{model}` | {messages} | `{cwd}` | `{repository}` | `{branch}` | `{path}` |".format(
                source=session["source"],
                title=session["title"],
                session_id=session["session_id"],
                started=session.get("started") or "",
                updated=session.get("updated") or "",
                model=session.get("model") or "",
                messages=f"{count_messages(session, 'user')} user / {count_messages(session, 'assistant')} assistant",
                cwd=session.get("cwd") or "",
                repository=session.get("repository") or "",
                branch=session.get("branch") or "",
                path=session["path"],
            )
        )

    lines.extend(["", "## Transcript", ""])

    for session in sessions:
        heading = session["title"] if session["title"] != "(untitled)" else session["session_id"]
        lines.extend(
            [
                f"## {heading}",
                "",
                f"- Source: {session['source']}",
                f"- Session: `{session['session_id']}`",
                f"- Started: `{session.get('started') or ''}`",
            ]
        )
        if session.get("updated"):
            lines.append(f"- Updated: `{session['updated']}`")
        if session.get("model"):
            lines.append(f"- Model: `{session['model']}`")
        if session.get("cwd"):
            lines.append(f"- CWD: `{session['cwd']}`")
        if session.get("repository"):
            lines.append(f"- Repository: `{session['repository']}`")
        if session.get("branch"):
            lines.append(f"- Branch: `{session['branch']}`")
        lines.extend([f"- Raw File: `{session['path']}`", ""])

        if not session["messages"]:
            lines.extend(["_No user/assistant transcript messages found for this date._", ""])
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
    parser.add_argument("--copilot-home", default=str(Path.home() / ".copilot"), help="Path to GitHub Copilot state.")
    parser.add_argument(
        "--code-support",
        default=str(Path.home() / "Library/Application Support/Code"),
        help="Path to VS Code application support.",
    )
    args = parser.parse_args()

    capture_date = args.date or datetime.now(LOCAL_TZ).date().isoformat()
    vault = Path(args.vault)
    copilot_home = Path(args.copilot_home)
    code_support = Path(args.code_support)

    sessions = [
        *extract_cli_sessions(copilot_home, capture_date),
        *extract_vscode_sessions(code_support, capture_date),
    ]
    sessions.sort(key=lambda session: (session.get("started") or "", str(session["path"])))

    inbox = vault / "inbox"
    inbox.mkdir(parents=True, exist_ok=True)
    output = inbox / f"{capture_date}-copilot-conversations.md"
    output.write_text(render(capture_date, copilot_home, code_support, sessions))
    print(output)
    print(f"sessions={len(sessions)}")


if __name__ == "__main__":
    main()
