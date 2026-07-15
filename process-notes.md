# Process Notes

### 2026-07-15

- Observation: Repository migration selection initially ranked a workbook row as easy without checking the workbook `Action` column, so an `Archive` candidate entered the migration queue.
- Suggested rule: Migration audits should always include `Action`, current repo status, owner, and pipeline complexity before recommending next repositories.
- Example: `quality_tools` looked technically easy from its Renovate pipeline, but the workbook action was `Archive`, so it should have been excluded from migration candidates.
