# Decision: Use a Separate Bloomberg Actual-Flow Dataset

## Decision

Import Hiromi's FY2019-FY2024 Bloomberg workbook through a controlled manual Airflow DAG into a separate CDH dataset. The main Japan interconnector dashboard combines Bloomberg and OCCTO in SQL, uses neutral `Actual Flow` labeling, and gives OCCTO row-level precedence wherever both sources contain the same interconnector timestamp.

Missing Bloomberg timestamps remain blank. The workbook stays in private S3 rather than Git.

## Context

The Bloomberg workbook contains seven interconnectors and 729,078 populated observations from `2019-04-01 00:00` through `2025-03-31 23:30`. Its values are 30-minute snapshots, while the existing OCCTO dataset contains 5-minute observations that the dashboard averages into 30-minute values. The workbook's `Missing Data` sheet also conflicts with some populated historical rows, so the historical value table is authoritative and contradictions are reported for audit.

## Rationale

A separate dataset preserves source and measurement semantics without inventing OCCTO provenance fields or blending snapshots into OCCTO averages. Private S3 avoids committing licensed Bloomberg data into permanent Git history. SQL precedence lets Bloomberg fill older gaps while protecting any overlapping OCCTO values.

## Tradeoffs

The design requires a second CDH registration and dashboard union logic. Operators must upload the unchanged workbook to each environment's approved S3 key and verify its SHA-256 before running the DAG.

## Sources

- `sources/codex-conversations/2026-07-13-codex-conversations.md`

Last Updated: 2026-07-13
