# Process Notes

### 2026-07-15

- Observation: Repository migration selection initially ranked a workbook row as easy without checking the workbook `Action` column, so an `Archive` candidate entered the migration queue.
- Suggested rule: Migration audits should always include `Action`, current repo status, owner, and pipeline complexity before recommending next repositories.
- Example: `quality_tools` looked technically easy from its Renovate pipeline, but the workbook action was `Archive`, so it should have been excluded from migration candidates.

### 2026-07-27

- Observation: Daily Codex captures can contain many delegated or repeated records for one canonical task, making session counts much larger than the number of distinct durable conversations.
- Suggested rule: During ingest, group Codex records by canonical task/session and reconcile the final parent outcome before treating delegated records as separate evidence.
- Example: The 2026-07-24 capture contained 59 session records, including repeated Wave 4, `data-common`, and SFF standardization workers that belonged to a much smaller set of durable workstreams.

### 2026-07-30

- Observation: Obsidian 1.12.7 crashed its renderer while indexing daily Codex Markdown transcripts of 3.3 MB and 2.2 MB.
- Suggested rule: Export Codex captures as a small Markdown index paired with a complete raw `.txt` transcript, and keep the pair together during ingest.
- Example: The 2026-07-24 and 2026-07-25 raw transcripts remain intact as `.txt` while their original `.md` paths now contain lightweight indexes.
