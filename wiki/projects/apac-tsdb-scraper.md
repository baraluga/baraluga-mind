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
- July 24 standup says the Darwin root cause was accepted and Mateo committed to perform the backfill. Brian confirmed on July 27 that Mateo fixed the issue and completed the follow-up.
- September 23 IEX incident probing found that all 12 national IEX series had metadata updates on September 22 around 14:33:52-14:34:15 IST and now resolve under `iex_api`; the unchanged Lambda scraper still searched `iex`, so its catalog lookup returned no national series and stopped publishing. Mateo confirmed the catalog change was intended, so Brian changed the national lookup to `iex_api`, added validation for missing/duplicate/invalid destination IDs, added bounded DAM/GDAM replay support, and pushed commits `60588d2` and `c0bf1f9` to `apac-tsdb-scraper` `main`. Local evidence reports 232 passing tests and a live-source check mapping 2,136 observations; production deployment and backfill were still pending because deployment credentials needed VPN refresh.
- The same September 23 investigation separated upstream TSDB publication failure from downstream `smp-india` Airflow failures: the Lambda fix can restore source-backed TSDB prices/bid/cleared-volume publication, but separate scheduled-volume TSDB IDs were returning catalog-object 404s in Airflow and require a separate SMP India reader-side repair.

## Open Questions

- UNCERTAIN: Whether Mateo's future Aurora templates will stay structurally compatible enough for the new discovery checks.
- UNCERTAIN: Whether the payload extraction slice was completed and committed after the July 15 capture ended.
- UNCERTAIN: Whether a read-only UAT catalog lookup was later run for the catalog refactor; dry run does not exercise TSDB catalog resolution.
- UNCERTAIN: Whether the September 22 IEX scheduled-volume catalog-object 404s share the same root cause as the intended `iex_api` catalog reclassification.
- UNCERTAIN: Whether `apac-tsdb-scraper` production deployment/backfill completed after the September 23 commits.

## Sources

- `sources/codex-conversations/2026-07-15-codex-conversations.md`
- `sources/codex-conversations/2026-07-23-codex-conversations.md`
- `sources/meetings/2026-07-24-1415-granola-daily-standup.md`
- `sources/notes/2026-07-27-ingest-handover-clarifications.md`
- `sources/codex-conversations/2026-09-23-codex-conversations.txt`

Last Updated: 2026-09-24
