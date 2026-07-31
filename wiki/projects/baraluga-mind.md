# Baraluga Mind

## Summary

Baraluga Mind is the local markdown second brain used to turn raw captures into durable wiki pages, source evidence, and one canonical action register.

The current ingest convention is that captured material lands in `inbox/` first. After an ingest pass, useful evidence moves to `sources/`, durable synthesis goes under `wiki/`, and active follow-up work goes into [[actions]].

## Details

- `actions.md` is the canonical register for active and completed follow-up work.
- Daily Codex conversation captures can be generated from local session JSONL files under `/Users/qn5792/.codex/sessions/YYYY/MM/DD/`.
- The preferred flow for Codex conversation capture is:
  - write a small dated index to `inbox/YYYY-MM-DD-codex-conversations.md`;
  - preserve the complete filtered transcript in the paired `inbox/YYYY-MM-DD-codex-conversations.txt`;
  - ingest the pair like any other inbox source;
  - move both processed files to `sources/codex-conversations/`.
- The capture should preserve user/assistant transcript evidence while filtering out tool calls, tool outputs, system prompts, developer prompts, and reasoning records.
- Raw transcripts must remain `.txt` because oversized Markdown transcripts can crash Obsidian 1.12.7 during indexing.
- The July 6 capture showed that full daily transcripts can be large, so the durable wiki should summarize only decisions, implementation outcomes, risks, and follow-ups.
- The corrected July 7 capture found five local Codex sessions and was ingested as source evidence. The July 8 capture found zero sessions and is preserved separately.
- The daily Codex conversation capture automation was confirmed active on July 9. It writes the paired `.md` index and `.txt` transcript to `inbox/` and explicitly stays export-only until a separate ingest pass.
- On July 30, the Codex exporter was changed to scan continuing sessions across the local session tree and include only messages whose timestamps fall on the capture date in `Asia/Manila`. This allows one long-lived pinned Daily Dump task to be captured correctly across multiple days instead of relying on the task's creation-date folder. The automation now runs at 00:10 and explicitly exports the previous Asia/Manila calendar day so messages sent between 23:00 and midnight are included.
- On July 31, the Codex exporter was changed to skip writing inbox capture files when no sessions have user/assistant messages for the target local date. Empty days should be visible in automation logs as `sessions=0` and `skipped=no-sessions`, not preserved as empty source evidence.
- A global `dump` skill now provides a chat-first, note-visible capture path without requiring a pinned task. Explicit `$dump` invocation or clear capture signals such as `dump:` create or update `inbox/YYYY-MM-DD.md` immediately. The note maintains provisional task state, completion annotations, notes, and an immutable raw timeline; ingestion later reconciles it with `actions.md` and preserves it under `sources/notes/`.
- GitHub Copilot conversations can also be exported from local Copilot CLI state under `/Users/qn5792/.copilot/session-state` and VS Code Copilot Chat workspace storage. The July 9 capture found ten local Copilot sessions and followed the same inbox-first ingest path.
- By July 12, Codex, GitHub Copilot, and Granola capture automations were all operating as inbox-only exporters. The July 12 captures contained six Codex sessions, two Copilot sessions, and a Granola status recording that the connector returned no meetings.
- The July 13 captures contained twelve Codex sessions, zero Copilot sessions, and one Granola standup. A trial morning brief grouped the previous day's evidence into `DONE`, `TODO`, and `BLOCKERS` and stayed in chat while the format is evaluated.
- The July 14 capture set contained four Codex sessions, zero Copilot sessions, three Granola meeting notes, and an empty manual daily note file. The Codex sessions included SMP Japan promotion and manual interconnector backfill follow-up work plus the export-only capture automations.
- The July 15 capture set contained thirteen Codex sessions, zero Copilot sessions, two Granola meeting notes, and a manual migration checklist. The Codex sessions were heavy on QRM/SFF migration coordination, Copilot custom agents, Aurora XLSX parser hardening, and a File Browser health monitor.
- The July 17 capture set contained eleven Codex sessions, zero Copilot sessions, two Granola meeting notes, and a manual daily checklist. The Codex sessions were heavy on `SCR-1202` HJKS 2Y look-back implementation, SMP ruleset cleanup, SFF pipeline migration guardrails, Meteomatics/TDB CI publishing, and Zscaler/Codex private-site access diagnostics.
- The July 18 capture set contained one Codex session, zero Copilot sessions, and a Granola status note saying no meetings dated 2026-07-18 Asia/Manila were returned by the connector. The Codex session only captured the export-only daily Codex conversation capture run.
- The July 19 capture set contained three Codex sessions, zero Copilot sessions, and a Granola status note saying no meetings matched the 2026-07-19 Asia/Manila date filter. The Codex sessions only captured the export-only daily Copilot, Granola, and Codex capture runs.
- The July 20 capture set contained ten Codex sessions, one Copilot session with no transcript messages, two Granola meeting notes, and a short manual daily checklist. The durable work centered on SFF/Walnut migration, Modernizer and `sff-actions` hardening, Confluence migration playbooks, Japan interconnector follow-up, and SMP technical-activities work.
- The July 21 capture set contained six Codex sessions, zero Copilot sessions, and a Granola status note saying no meetings dated 2026-07-21 Asia/Manila were returned by the connector. Durable work included creating the global `consult-mind-palace` skill, producing an evidence-based unmigrated-repository age audit, migrating `wss_client` to GitHub, and rolling back `strategy-common-infra` after pipeline modernization readiness issues surfaced.
- The July 23 capture set contained thirteen Codex sessions, zero Copilot sessions, and a Granola status note saying no matching local-date meetings were returned. Durable work included `SCR-1206` operating-capacity implementation, Darwin diagnosis and correction, the first SFF Artifactory publication waves, and a DAG Helper show-and-tell deck.
- The July 24 capture set contained fifty-nine Codex session records, three Granola meetings, and one Copilot session. Many Codex records were delegated or repeated views of the same SFF migration work. Durable outcomes included the recovered `data-common` library, accepted Python CI contracts, further Artifactory publication, and the Walnut/SMP standup state.
- The July 25 capture set contained fourteen Codex sessions, zero Copilot sessions, and a no-meetings Granola status. Durable outcomes included organization-wide SFF CI closeout, GAMS readiness documentation, Pipeline Modernizer decommissioning, DeCliC migration work, and the installed Buddy v2 Codex pet.
- The July 26 capture set contained six Codex sessions, zero Copilot sessions, and a no-meetings Granola status. Durable outcomes included DeCliC deployment-runway validation and the Pipeline Customs Broker proof of concept.
- `consult-mind-palace` is a global Codex skill under `/Users/qn5792/.codex/skills/consult-mind-palace/`. It treats this repository as a read-only "mind palace" from any working directory, searches durable wiki pages before action/source evidence, and returns source-backed synthesis for tasks such as Confluence drafting.

## Open Questions

- UNCERTAIN: The July 7 automation initially produced an empty capture before the corrected export was created.

## Sources

- `scripts/export-codex-conversations.py`
- `inbox/AGENTS.md`
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
- `sources/codex-conversations/2026-07-21-codex-conversations.md`
- `sources/copilot-conversations/2026-07-21-copilot-conversations.md`
- `sources/meetings/2026-07-21-granola-meeting-notes-status.md`
- `sources/codex-conversations/2026-07-23-codex-conversations.md`
- `sources/copilot-conversations/2026-07-23-copilot-conversations.md`
- `sources/meetings/2026-07-23-granola-meeting-notes-status.md`
- `sources/codex-conversations/2026-07-24-codex-conversations.md`
- `sources/copilot-conversations/2026-07-24-copilot-conversations.md`
- `sources/meetings/2026-07-24-1045-granola-walnut-migration-caucus.md`
- `sources/meetings/2026-07-24-1415-granola-daily-standup.md`
- `sources/meetings/2026-07-24-1515-granola-technical-standup.md`
- `sources/codex-conversations/2026-07-25-codex-conversations.md`
- `sources/copilot-conversations/2026-07-25-copilot-conversations.md`
- `sources/meetings/2026-07-25-granola-meeting-notes-status.md`
- `sources/codex-conversations/2026-07-26-codex-conversations.md`
- `sources/copilot-conversations/2026-07-26-copilot-conversations.md`
- `sources/meetings/2026-07-26-granola-meeting-notes-status.md`

Last Updated: 2026-07-31
