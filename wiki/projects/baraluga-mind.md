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

## Open Questions

- UNCERTAIN: Whether the daily Codex conversation dump should be automated on a schedule or kept as an explicit manual capture step.
- UNCERTAIN: The July 7 automation initially produced an empty capture before the corrected export was created.

## Sources

- `sources/codex-conversations/2026-07-06-codex-conversations.md`
- `sources/codex-conversations/2026-07-07-codex-conversations.md`
- `sources/codex-conversations/2026-07-08-codex-conversations.md`

Last Updated: 2026-07-08
