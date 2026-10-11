# Japan Interconnector Dashboard

## Current State

As of 2026-10-05. Japan work is in maintenance mode: no active Japan sprint ticket since late September, with next-period work limited to bug fixes and robustness (see [[smp-platform]]).

- **Interconnector dashboard:** live in production since 2026-07-27, and Hiromi uses the production link. It covers all seven priority interconnectors:
  - available capacity and minimum capacity
  - operating capacity (`SCR-1206`)
  - actual flow
  - JEPX day-ahead price spread with `Last`/`WTD`/`MTD` boxes
  - an `As of` look-back selector (`SCR-1197`)

  Data goes back to FY2019, and FY27 data is reflected promptly. The aim was to end Hiromi's manual weekend data gathering. New additions still go through QA first.
- **TSDB:** production publishing is finalised for 35 interconnector series:
  - 14 directional available-capacity series
  - 14 directional minimum-capacity series
  - 7 signed actual-flow series

  Operating capacity and JEPX prices are also published. The provider is `interconnector`, owned by Carlos and Lona. History runs from 2021 for capacity and from FY2025 for actual flow, via the shared `smp-common` OCCTO publisher (`SCR-1171`/`1217`).
- **Other Japan look-back dashboards:** HJKS 2Y (`SCR-1202`) and nuclear by region (`SCR-1208`) are delivered and accepted. They snapshot one to three times a day through the snapshot-manifest pattern.
- **Open threads:**
  - Carlos's "adjustment reserve" question was answered on 2026-10-05. The closest OCCTO field is `広域調整枠` (with margin), which describes reserved interconnector capacity, not generation reserve. Planned flows, margins, and `広域調整枠` are in the source but not published to TSDB.
  - Aurora curves are the next proposed Japan data item, either via API if one exists or with the India Excel approach.

## Background

- **Sources:** OCCTO's public system-information service, over HTTP JSON/CSV endpoints with no credentials. JEPX price CSVs. Hiromi's Bloomberg workbook for FY2019–FY2024 actual flow, because OCCTO only has actual flow from 2025-04-01.
- **Meaning of "Available":** the dashboard's "Available" is OCCTO residual capacity (`空容量`), not operating capacity (`運用容量`). Actual flow can exceed residual capacity without any breach. That's why `SCR-1206` added operating capacity as grey dotted lines. A zero-capacity report on 2026-07-22 turned out to be OCCTO's own value.
- **Combining actual flow:** the dashboard joins OCCTO 30-minute averages with Bloomberg 30-minute snapshots under a neutral `Actual Flow` label. OCCTO wins where the two overlap, and Bloomberg fills older gaps. Bloomberg lives in a separate CDH dataset: see [[2026-07-13-use-separate-bloomberg-actual-flow-dataset]].
- **Reconciliation contract (`smp-japan`):**
  - Manual-backfill files are permanent inputs; live daily data is a bounded overlay.
  - Partial runs rebuild the affected years from the persisted baseline.
  - Publication fails closed if daily granularity would regress.
  - Processing streams 32,768-row batches one calendar year at a time, partitioned by the calendar year of `interval_start_jst`.
  - A completed-day capacity DAG at 00:30 JST persists the previous day's revised capacity.
  - Never scan the whole live prefix: in July, 44 stray backfill files there broke reconciliation.
- **OCCTO quirks:**
  - Weekly revised data is indexed by Thursday publication date (`SCR-1219` fixed a month-boundary bug).
  - Target year 2026 runs through March 2027.
  - Historical yearly, monthly, and weekly capacity lacks max values, so daily capacity is used for backfill.
  - Current OCCTO files revise past Available Capacity, so inside a repair range current values win.
- **Look-back pattern:** `latest` is a daily overwrite and `historical` holds cumulative snapshots. A manifest is published only when every region completes, and the `As of` dropdown resolves the newest snapshot on or before the chosen date. Legacy unversioned rows must be unioned in, or older history disappears.
- **Other Japan DAG notes:**
  - HJKS report emails were removed in `SCR-1216`, with processing kept.
  - An HJKS shadow DAG tested serialised retry windows after CSRF failures.
  - No SMP DAG scrapes the Tohoku `setsuden` site.
- **Process lessons:** Japan stakeholders accepted auto-scaled axes and Grafana's native CSV export in place of an Excel export (`SCR-1198`). Production CDH registration can go green without refreshing stages; see [[smp-dashboards]].

## History

- 2026-07-06: daily-average spread and stat boxes shipped to production.
- 2026-07-13: Bloomberg FY2019–FY2024 actual flow approved as a separate dataset.
- 2026-07-24: `SCR-1202` HJKS 2Y look-back accepted.
- 2026-07-27: interconnector dashboard fully released in production.
- 2026-07-29: three Japan look-back dashboards accepted; the project was projected to exceed its budget because of scope additions.
- 2026-09-09: interconnector TSDB production publishing finalised.

## Open Questions

- UNCERTAIN: Whether Carlos's "adjustment reserve" means reserved interconnector capacity or generation balancing reserve.
- UNCERTAIN: Whether the Singapore user's request for Tohoku historical demand actuals becomes SMP scope.
- UNCERTAIN: Whether `SCR-1208` passed its second scheduled-run check, proving that an older forecast is kept while `Latest` advances.

## Sources

- `sources/codex-conversations/2026-07-06-codex-conversations.md`
- `sources/codex-conversations/2026-07-12-codex-conversations.md`
- `sources/codex-conversations/2026-07-13-codex-conversations.md`
- `sources/codex-conversations/2026-07-16-codex-conversations.md`
- `sources/codex-conversations/2026-07-23-codex-conversations.md`
- `sources/meetings/2026-07-27-1415-granola-daily-standup.md`
- `sources/codex-conversations/2026-07-28-codex-conversations.md`
- `sources/meetings/2026-07-29-1630-granola-sprint-review.md`
- `sources/codex-conversations/2026-07-31-codex-conversations.md`
- `sources/codex-conversations/2026-08-03-codex-conversations.txt`
- `sources/codex-conversations/2026-08-04-codex-conversations.txt`
- `sources/codex-conversations/2026-08-11-codex-conversations.txt`
- `sources/meetings/2026-09-09-1630-granola-smp-sprint-review.md`
- `sources/codex-conversations/2026-10-05-codex-conversations.txt`
- Older sources are in this page's git history before 2026-10-11.

Last Updated: 2026-10-11
