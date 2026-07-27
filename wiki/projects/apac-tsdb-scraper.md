# APAC TSDB Scraper

## Summary

`apac-tsdb-scraper` contains older Lambda/tag-flow TSDB scrapers. July 15 work focused on the Aurora XLSX CLI used for Indian power-market forecast uploads, especially workbook compatibility, release selection, dry-run safety, and refactoring the CLI into smaller tested boundaries.

Mateo reported that the new Aurora release renamed the price worksheet from market-specific names such as `Half hourly DAM prices` to the generic `Half hourly power prices`. The fix hardened sheet discovery by structure rather than relying only on tab names.

## Details

- The repository was fast-forwarded on July 15 from `c99c0af` to `1782ab9`, with latest commit `patch error today->tomorrow for DAM and GDAM`.
- Real Q2 and Q3 Aurora workbooks showed the data layout stayed stable while the Q3 tab name changed. Q2 used market-specific tabs; Q3 used the generic tab.
- The hardened loader supports old names, new generic names, and structural fallback discovery. It validates market markers, expected scenarios, expected regions, 52 series per market, continuous 30-minute timestamps, and non-empty numeric values.
- Discovery was also fixed to select one coherent latest quarterly release instead of accidentally mixing markets from different releases when Q2 and Q3 files share a folder.
- Validation against the six real downloaded workbooks parsed all markets successfully: Q2 had 604,944 rows and 52 series per market; Q3 had 600,528 rows and 52 series per market; inflation had 36 annual rows covering 2025-2060.
- The parser hardening was committed and pushed as `fix(scr-1014): support renamed Aurora power price sheets`.
- A follow-up refactor began after the hotfix. The agreed cadence became TDD, full validation, then an immediate isolated commit for every refactor point.
- Refactor commits captured in the July 15 source:
  - `07bd398 refactor(scr-1014): isolate Aurora TSDB session state`
  - `c57d790 refactor(scr-1014): isolate Aurora workbook discovery`
  - `9fa1826 refactor(scr-1014): isolate Aurora workbook parsing`
  - `b195edd refactor(scr-1014): isolate Aurora TSDB catalog resolution`
  - `2fd54d3 refactor(scr-1014): isolate Aurora TSDB configuration`
- By the end of the capture, the payload extraction slice had started but was not shown as committed before the source ended.
- July 23 Darwin investigation found a real prod configuration defect: the active config pointed Darwin at UAT Athena workgroup `cdh_solarisapac_22047` rather than prod workgroup `cdh_solarisapac_48380`. The defect was introduced in commit `bace005` on 2026-03-03; the original Lambda prod config used the correct workgroup.
- Mateo's report that all scrapers stopped on April 26 initially suggested a shared RestKafka/topic failure, but he later clarified that the other scrapers recovered while Darwin remained broken. The task-creation screenshot proved discovery and task creation only, leaving execution, Athena, and TSDB write stages as the relevant failure boundary.
- The Darwin workgroup correction and local-test documentation were committed and pushed to `origin/main` as `5258e66 fix: use prod Athena workgroup for Darwin` and `5c3c081 docs: document local test commands`. The captured validation reports 119 passing tests.
- July 24 standup says the Darwin root cause was accepted and Mateo committed to perform the backfill, but the backfill had not yet been reported complete.

## Open Questions

- UNCERTAIN: Whether Mateo's future Aurora templates will stay structurally compatible enough for the new discovery checks.
- UNCERTAIN: Whether the payload extraction slice was completed and committed after the July 15 capture ended.
- UNCERTAIN: Whether a read-only UAT catalog lookup was later run for the catalog refactor; dry run does not exercise TSDB catalog resolution.
- UNCERTAIN: The exact Darwin missing-data interval and whether Mateo completed the promised backfill.

## Sources

- `sources/codex-conversations/2026-07-15-codex-conversations.md`
- `sources/codex-conversations/2026-07-23-codex-conversations.md`
- `sources/meetings/2026-07-24-1415-granola-daily-standup.md`

Last Updated: 2026-07-27
