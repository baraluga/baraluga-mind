# Inbox Instructions

`inbox/` is the landing zone for automated captures: the daily Codex, GitHub Copilot, and Granola exports. Anything dropped here by hand follows the same ingest path.

- There is no live daily note. The `dump` skill was retired on 2026-10-11, and ingest runs autonomously on a schedule.
- Codex exports arrive as a `.md` index plus `.txt` transcript pair. Treat the pair as one source and move both together.
- Leave a file here only when it still needs clarification; say why in the ingest report.
- Older `inbox/YYYY-MM-DD.md` notes, if any remain, are ordinary sources. Ingest them, then move them to `sources/notes/`.
