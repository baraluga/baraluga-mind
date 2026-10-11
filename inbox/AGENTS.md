# Inbox Instructions

`inbox/` is the landing zone for automated captures: the daily Codex, GitHub Copilot, and Granola exports, plus Claude Code conversations. Anything dropped here by hand follows the same ingest path.

- Claude conversations arrive as `YYYY-MM-DD-claude-<project>-<session8>.txt`, written by the `Stop` hook running `scripts/capture-claude-conversation.py`. The header gives the Claude project (a project such as `smp` can span several repos), and `## HH:MM user (subdir)` headings show where in the project the session was working.
- Each file grows all day. Ingest only files dated before the current Asia/Manila day; leave today's files for the next run. Move processed ones to `sources/claude-conversations/`.
- Capture redacts obvious secrets only. If a password, token, or key still appears, redact it in the source copy before committing.

- There is no live daily note. The `dump` skill was retired on 2026-10-11, and ingest runs autonomously on a schedule.
- Codex exports arrive as a `.md` index plus `.txt` transcript pair. Treat the pair as one source and move both together.
- Leave a file here only when it still needs clarification; say why in the ingest report.
- Older `inbox/YYYY-MM-DD.md` notes, if any remain, are ordinary sources. Ingest them, then move them to `sources/notes/`.
