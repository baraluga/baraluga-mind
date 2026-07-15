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

## Open Questions

- UNCERTAIN: Whether Mateo's future Aurora templates will stay structurally compatible enough for the new discovery checks.
- UNCERTAIN: Whether the payload extraction slice was completed and committed after the July 15 capture ended.
- UNCERTAIN: Whether a read-only UAT catalog lookup was later run for the catalog refactor; dry run does not exercise TSDB catalog resolution.

## Sources

- `sources/codex-conversations/2026-07-15-codex-conversations.md`

Last Updated: 2026-07-15
