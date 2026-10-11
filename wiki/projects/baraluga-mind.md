# Baraluga Mind

## Current State

As of 2026-10-11.

- **Purpose:** a reference memory and second brain for anything Brian might forget. It is not a task tracker. The operating rules live in `AGENTS.md`; this page records how the system runs and why it is shaped this way.
- **Capture:** daily exports at 00:10 Asia/Manila, each covering the full previous local day, land in `inbox/`. There are three:
  - Codex sessions, from `~/.codex/sessions/`.
  - GitHub Copilot sessions, from Copilot CLI state and VS Code chat storage.
  - Granola meetings.
- **Manual capture:** the `dump` skill writes a live daily note to `inbox/YYYY-MM-DD.md`.
- **Ingest:** a scheduled pass at 00:30 applies the value gate, moves evidence to `sources/`, and updates `wiki/`. Since 2026-10-11, pages follow the Current-State Rule: `Current State` is rewritten, never appended to.
- **Retrieval:** the global Codex skill `consult-mind-palace` searches the repo read-only from any directory.
- **Not captured:** Claude conversations, and Teams. Teams needs corporate access.
- **Planned:**
  - Share the skills between Codex and Claude via symlinks from this repo.
  - Add a Claude Code plugin/mod for capture and `/palace` lookups.
  - Add an `index.md` so no page is orphaned.
  - Convert the remaining large pages to the current-state shape.

## Background

- **Markdown in git** is the canonical store. It stays readable, diffable, and agent-neutral. Any search index should be a cache rebuilt from these files, never the source of truth.
- **Conversation exports** keep only user and assistant messages, dropping tool calls, system and developer prompts, and reasoning. Each export is a pair: a small `.md` index plus the full `.txt` transcript, moved together. Large Markdown transcripts crashed Obsidian 1.12.7 during indexing.
- **The Codex exporter** scans continuing sessions across the whole tree and filters messages by Asia/Manila date. That way a long-lived session is captured on every day it is used. Days with no messages write nothing.
- **Scheduled-automation sessions** are excluded from export. Ingest also requires a durable knowledge delta before moving or committing anything (see History, 2026-08-19).

## History

- 2026-07-04: repo started as a markdown wiki. Wiki `TODO:` items moved into a central `actions.md`.
- 2026-07-09 to 07-12: Codex, Copilot, and Granola capture automations running as inbox-only exporters.
- 2026-07-21: `consult-mind-palace` skill created.
- 2026-07-30: transcripts split into `.md` index plus `.txt` pairs after Obsidian crashes; the exporter switched to date-filtered scanning.
- 2026-08-19: capture and ingest formed a feedback loop during Brian's vacation, exporting and committing their own automation sessions. Fixed by excluding automation sessions and gating ingest on durable deltas.
- 2026-09-04: all captures aligned to 00:10 with ingest at 00:30.
- 2026-10-06: Notion pilot started, with the repo staying canonical during the trial.
- 2026-10-11: Notion pilot dropped; the repo stays the home.
- 2026-10-11: revamp after an audit found pages had become append-only logs, people pages were stale, and `actions.md` had 258 open items nobody read.
  - `actions.md` frozen as an archive.
  - Current-State Rule adopted.
  - `smp-platform` split into [[smp-india]], [[darwin-collector]], [[smp-india-access]], [[smp-jupyter-dag-authoring]], and [[technical-activities]].

## Sources

- `scripts/export-codex-conversations.py`
- `inbox/AGENTS.md`
- `process-notes.md`
- `sources/codex-conversations/2026-07-06-codex-conversations.md`
- `sources/codex-conversations/2026-07-09-codex-conversations.md`
- `sources/copilot-conversations/2026-07-09-copilot-conversations.md`
- `sources/codex-conversations/2026-07-12-codex-conversations.md`
- `sources/codex-conversations/2026-07-21-codex-conversations.md`
- `sources/codex-conversations/2026-09-04-codex-conversations.txt`
- `sources/codex-conversations/2026-10-06-codex-conversations.txt`
- User clarification on 2026-10-11 (Claude Code session): Notion pilot dropped; revamp scope.

Last Updated: 2026-10-11
