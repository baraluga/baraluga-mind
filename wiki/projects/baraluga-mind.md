# Baraluga Mind

## Summary

Baraluga Mind is the local markdown second brain used to turn raw captures into durable wiki pages, source evidence, and one canonical action register.

The current ingest convention is that captured material lands in `inbox/` first. After an ingest pass, useful evidence moves to `sources/`, durable synthesis goes under `wiki/`, and active follow-up work goes into [[actions]].

## Details

- `actions.md` is the canonical register for active and completed follow-up work.
- Daily Codex conversation captures can be generated from local session JSONL files under `/Users/qn5792/.codex/sessions/YYYY/MM/DD/`.
- The preferred flow for Codex conversation capture is:
  - write a dated capture to `inbox/YYYY-MM-DD-codex-conversations.md`;
  - ingest it like any other inbox source;
  - move the processed capture to `sources/codex-conversations/`.
- The capture should preserve user/assistant transcript evidence while filtering out tool calls, tool outputs, system prompts, developer prompts, and reasoning records.
- The July 6 capture showed that full daily transcripts can be large, so the durable wiki should summarize only decisions, implementation outcomes, risks, and follow-ups.
- The corrected July 7 capture found five local Codex sessions and was ingested as source evidence. The July 8 capture found zero sessions and is preserved separately.
- The daily Codex conversation capture automation was confirmed active on July 9. It runs daily at 23:00, writes to `inbox/YYYY-MM-DD-codex-conversations.md`, and explicitly stays export-only until a separate ingest pass.
- GitHub Copilot conversations can also be exported from local Copilot CLI state under `/Users/qn5792/.copilot/session-state` and VS Code Copilot Chat workspace storage. The July 9 capture found ten local Copilot sessions and followed the same inbox-first ingest path.
- By July 12, Codex, GitHub Copilot, and Granola capture automations were all operating as inbox-only exporters. The July 12 captures contained six Codex sessions, two Copilot sessions, and a Granola status recording that the connector returned no meetings.
- The July 13 captures contained twelve Codex sessions, zero Copilot sessions, and one Granola standup. A trial morning brief grouped the previous day's evidence into `DONE`, `TODO`, and `BLOCKERS` and stayed in chat while the format is evaluated.
- The July 14 capture set contained four Codex sessions, zero Copilot sessions, three Granola meeting notes, and an empty manual daily note file. The Codex sessions included SMP Japan promotion and manual interconnector backfill follow-up work plus the export-only capture automations.
- The July 15 capture set contained thirteen Codex sessions, zero Copilot sessions, two Granola meeting notes, and a manual migration checklist. The Codex sessions were heavy on QRM/SFF migration coordination, Copilot custom agents, Aurora XLSX parser hardening, and a File Browser health monitor.
- The July 17 capture set contained eleven Codex sessions, zero Copilot sessions, two Granola meeting notes, and a manual daily checklist. The Codex sessions were heavy on `SCR-1202` HJKS 2Y look-back implementation, SMP ruleset cleanup, SFF pipeline migration guardrails, Meteomatics/TDB CI publishing, and Zscaler/Codex private-site access diagnostics.
- The July 18 capture set contained one Codex session, zero Copilot sessions, and a Granola status note saying no meetings dated 2026-07-18 Asia/Manila were returned by the connector. The Codex session only captured the export-only daily Codex conversation capture run.
- The July 19 capture set contained three Codex sessions, zero Copilot sessions, and a Granola status note saying no meetings matched the 2026-07-19 Asia/Manila date filter. The Codex sessions only captured the export-only daily Copilot, Granola, and Codex capture runs.
- The July 20 capture set contained ten Codex sessions, one Copilot session with no transcript messages, two Granola meeting notes, and a short manual daily checklist. The durable work centered on SFF/Walnut migration, Modernizer and `sff-actions` hardening, Confluence migration playbooks, Japan interconnector follow-up, and SMP technical-activities work.

## Open Questions

- UNCERTAIN: The July 7 automation initially produced an empty capture before the corrected export was created.

## Sources

- `sources/codex-conversations/2026-07-06-codex-conversations.md`
- `sources/codex-conversations/2026-07-07-codex-conversations.md`
- `sources/codex-conversations/2026-07-08-codex-conversations.md`
- `sources/codex-conversations/2026-07-09-codex-conversations.md`
- `sources/copilot-conversations/2026-07-09-copilot-conversations.md`
- `sources/codex-conversations/2026-07-12-codex-conversations.md`
- `sources/copilot-conversations/2026-07-12-copilot-conversations.md`
- `sources/meetings/2026-07-12-granola-meeting-notes-status.md`
- `sources/codex-conversations/2026-07-13-codex-conversations.md`
- `sources/copilot-conversations/2026-07-13-copilot-conversations.md`
- `sources/meetings/2026-07-13-1515-granola-technical-activities-standup.md`
- `sources/codex-conversations/2026-07-14-codex-conversations.md`
- `sources/copilot-conversations/2026-07-14-copilot-conversations.md`
- `sources/meetings/2026-07-14-0945-granola-team-meeting.md`
- `sources/meetings/2026-07-14-1515-granola-technical-standup.md`
- `sources/meetings/2026-07-14-1700-granola-qrm-be-chapter-meeting.md`
- `sources/notes/2026-07-14.md`
- `sources/codex-conversations/2026-07-15-codex-conversations.md`
- `sources/copilot-conversations/2026-07-15-copilot-conversations.md`
- `sources/meetings/2026-07-15-1500-granola-sprint-retro.md`
- `sources/meetings/2026-07-15-1630-granola-sprint-review.md`
- `sources/notes/2026-07-15.md`
- `sources/codex-conversations/2026-07-17-codex-conversations.md`
- `sources/copilot-conversations/2026-07-17-copilot-conversations.md`
- `sources/meetings/2026-07-17-1415-granola-daily-standup.md`
- `sources/meetings/2026-07-17-1600-granola-technical-activities.md`
- `sources/notes/2026-07-17.md`
- `sources/codex-conversations/2026-07-18-codex-conversations.md`
- `sources/copilot-conversations/2026-07-18-copilot-conversations.md`
- `sources/meetings/2026-07-18-granola-meeting-notes-status.md`
- `sources/codex-conversations/2026-07-19-codex-conversations.md`
- `sources/copilot-conversations/2026-07-19-copilot-conversations.md`
- `sources/meetings/2026-07-19-granola-meeting-notes-status.md`
- `sources/codex-conversations/2026-07-20-codex-conversations.md`
- `sources/copilot-conversations/2026-07-20-copilot-conversations.md`
- `sources/meetings/2026-07-20-1415-granola-standup.md`
- `sources/meetings/2026-07-20-1645-granola-ta-standup.md`
- `sources/notes/2026-07-20.md`

Last Updated: 2026-07-20
