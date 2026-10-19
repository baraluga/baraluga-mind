# SMP India

## Current State

As of 2026-10-20. These are the India data products built on [[smp-platform]]. Stakeholders are Mateo, Adrien/Adrian, and Lou Dubuisson. Validation runs through [[francois-delcourt]].

**Delivered by the 2026-10-07 sprint review:**
- Legacy Green DAM scraper fix (`SCR-1264`)
- IEX bid-stack data in TSDB (`SCR-1253`)
- India geomap in Grafana
- Bilateral-contract dashboard (`SCR-1275`)
- Grafana alerting docs

**In flight or pending:**
- `SCR-1286`: October IEX Green DAM/GDAM gap fix, pushed to [[apac-tsdb-scraper]]. Lou confirmed it works; closure still pending.
- `SCR-1284`: production evidence showed most RTM delay comes from two independent 30-minute schedules: `apac-tsdb-scraper` publishes IEX RTM into TSDB, then an India DAG copies TSDB to CDH. Adrien said near-real-time is mandatory but they are not bidding on RTM yet. The favoured design is RTM-only: move the scraper into `smp-india`, poll the API frequently, and write TSDB and CDH in parallel. Open design choice is a simple one-minute Airflow DAG versus a continuous [[darwin-collector]] style service, depending on the accepted API-to-Grafana delay target.
- The QA IEX RTM DAG polls once a minute and skips downstream work when nothing is new. First observed CDH delivery was 1 minute 2 seconds; the expected API-to-Grafana delay is up to about five minutes. The team will propose a five-to-ten-minute default interval with increased frequency during the critical trading window.
- The GDAM Grafana panel queries the empty `india_iex_tsdb_dashboard_latest` table, while the data sits in `india_iex_tsdb_expanded_latest` (2026-10-09). This looks like a stale panel reference unless the live panel has already changed.
- `SCR-1274`: HPX national scope is 29 PT15M series: five each for DAM, RTM, and HPDAM, plus 14 GDAM series. GDAM includes price, total purchase bid, sell bids, and cleared/scheduled volume by total, solar, non-solar, and hydro; it has no MCV series. Lou's IDs were mapped and catalog-checked in UAT and prod before promotion through dev, QA, and prod; publication enablement remains a separate rollout choice.
- `SCR-1274` publication performance fix is now on dev, QA, and prod. It uses bulk TSDB reads, in-task verification only after writes, shorter retry budgets, and visible timing logs; the initial RTM/manual runs were fast, but the first scheduled write-path run still needs timing evidence.
- Khaba `SCR-1288`: Michael's `index_col=False` fix handles the October 9 inverter expansion and trailing-delimiter parse shift from October 10 onward. Follow-up hardening added a regression test, clearer field-count errors, and a "last row wins" rule for rare conflicting duplicate minute readings after preserving the existing all-zero safeguard. Brian confirmed the October 9-12 backfills succeeded; October 8 remained a possible follow-up.
- Khaba scheduling: deployed realtime and minute DAGs now explicitly skip a missing same-day CSV (with clear logs), while daily reconciliation stays fail-fast. This prevents hundreds of routine missing-file failures from obscuring real faults; an upstream outage can take until the next daily reconciliation to alert. The temporary `KHABA_GENERATION_SOURCE_TRANSITION_WINDOW_MINUTES=1440` stopgap should be removed once the deployed code is confirmed active.
- `SCR-1289`: the REC scraper remains a Lambda; it was re-enabled in its prod run list, backfilled, and monitored rather than moved to Airflow. The scheduled runs of 16–18 October completed autonomously and configuration-drift checking was clean. The remaining handover is validation by [[francois-delcourt]].
- Darwin assets for Tuticorin and four Gujarat sites are moving from access-blocked design to rollout. See [[darwin-collector]].
- Grid India (`SCR-1230`) and the national H. India site: blocked on access. See [[smp-india-access]].
- Khaba QA pauses in early October were intentional operational choices, not a DAG pause-logic defect: QA was kept runnable for testing while avoiding unnecessary side-by-side production cost.
- Khaba forecasts are now a separate CDH dataset/DAG (`india_khaba_forecasts`) rather than fields embedded in the actual-generation export. Its dashboards were imported in QA and prod and the associated export change was promoted. The remaining 12–15 October actual-generation gaps derive from incomplete upstream CSVs; reconciliation should run again only after complete files are re-sent.
- Khavda forecast reads now bulk-read consecutive delivery dates in nine-day chunks, then split locally: three TSDB reads per run rather than 27. This was promoted alongside the Khaba change; live timing evidence remains useful.
- Not urgent: a KPI dashboard Mateo wants to pair on (TSDB → calculations → CDH → Grafana), and adapting the Aurora XLSX loader, which needs dataset, format, and ownership answers first.

## Background

### Khaba Generation

- Source: a CDH-managed FTP CSV in S3 (`KHABA/FTP_DATA<dd-mm-yyyy>.csv`, `ap-south-1`) with one-minute readings, overwritten through the day.
- **15-minute path:** a realtime DAG and a previous-day reconciliation DAG share one parser. They publish only complete 15-minute averages of Active Power, GHI, Module Surface Temperature, and Ambient Temperature to TSDB (Mateo later renamed the irradiance series to POA without changing its ID), under provider `R&F India` (code alias `rf_india`; series IDs versioned in code). They verify by read-back, then write date-based CDH parquet for Athena/Grafana (`SCR-1238`). Publication is gated by `KHABA_GENERATION_TSDB_PUBLISH_ENABLED`.
- **One-minute path (`SCR-1259`):** runs in parallel for operational needs, with five more series IDs. The 15-minute path stays unchanged. Promoted to QA on 2026-09-17; backfill runs through `smp-common 0.8.0`.
- **Missing source files:** both realtime and minute paths skip missing same-day source files during the first four hours after IST midnight, then fail fast. The old minute DAG six-hour sensor was removed in October 2026 after it made normal missing-file periods look like stuck tasks.
- **Timestamp semantics:** a 15-minute block is labelled by its start (09:15 means 09:15–09:29). UNCERTAIN: Mateo has not confirmed start versus end labelling.
- **Partial intervals** are skipped. Reprocessing them needs Mateo's agreement.
- **Related sites:** Khavda was added as an R&F monitored asset beside Khaba in Grafana (2026-09-23 review). `SCR-1255` added Manikaran day-ahead and intraday forecasts beside actual generation.

### IEX

- **Bid stack:** collection (`SCR-1231`) and a QA/prod dashboard (`SCR-1243`), with separate buy and sell panels. TSDB publication (`SCR-1253`) uses 60 IDs: DAM/GDAM/RTM × buy/sell × 10 price bands, MW at 15-minute frequency. It verifies with a faster bulk reader. Backfill was skipped after Mateo's validation.
- **History and cleanup:** `SCR-1257` added a national-price history dataset from the previous year onward (stored in UTC, shown in IST). `SCR-1256` cleans stale DAM rows.
- **RTM:** published by [[apac-tsdb-scraper]]. September rollover gaps were replayed and verified against IEX. `SCR-1258` prepared a trailing six-hour sliding reconciliation.
- **Green DAM:** IEX changed its categories on 2026-07-08 (Circular 2713). The old Solar/Non-Solar series stay historical; the new Wind/Hydro/DRE/Other RE breakdown uses 12 new series plus a total.

### Bilateral Contracts

- `SCR-1229` scrapes IEX and HPX contract data into production CDH, with no TSDB publication. The schedule runs 1–2 hours after 18:00 IST because the source arrives in bulk later. The `SCR-1275` dashboard caveats:
  - GTAM has average/lowest/highest prices while TAM and HPX give a discovered price.
  - GTAM volume is labelled MWh but stored as MU.
  - Some contracts have split delivery windows.
  - Two HPX TAM rows for 2026-09-19 were missing from CDH.

### Working Rules

- SMP does not provision TSDB IDs. Missing IDs are a stakeholder dependency to raise early.
- Default to forward-only ingestion unless a stakeholder asks for a backfill start date.
- India Athena shares the GEM Production account with other workloads. A `GetWorkGroup` throttling burst on 2026-09-29 hit SMP dashboards; the caller was never identified.

## History

- 2026-07-30: Khaba generation scoped; the first India TSDB publication follows in August.
- 2026-08-27: Mateo sets priorities: POA/Khaba dashboard first, then bilateral contracts, with Grid India parked pending access.
- 2026-09: IEX bid stack, price history, Manikaran forecasts, and bilateral contracts delivered.
- 2026-10-07: Sprint 3 closes with bid-stack TSDB, the geomap, and the bilateral dashboard.
- 2026-10-13: Khaba source parsing and missing-file handling hardened after the October 9 inverter expansion, and HPX `SCR-1274` scope expanded to include HPDAM plus 32 total TSDB series.
- 2026-10-15: HPX scope corrected from 33 to 29 series when Lou supplied the final IDs and confirmed GDAM excludes MCV; mappings were validated in UAT and prod.
- 2026-10-15: Khaba missing-current-source handling promoted through QA and prod; REC TSDB/CDH recovery confirmed through 30 September.
- 2026-10-17: Khaba forecast CDH dataset promoted through prod; dashboard/export separation is awaiting Grafana import and the associated India promotion.
- 2026-10-19: Khaba dashboards and export separation reached QA/prod; HPX performance changes were promoted; REC ran autonomously over the weekend.

## Open Questions

- UNCERTAIN: Root cause of the 2026-09-04 Khaba Dev/QA cross-account S3 loss (recorded as "KAVA"), and whether the 2026-09-30 SCP change fixed it. Khaba and Khavda are two distinct sites; see [[aliases]] for variants.
- UNCERTAIN: Whether bilateral-contract data should stay CDH-only or also feed TSDB.
- UNCERTAIN: Whether the live GDAM panel already diverged from the checked-in query.
- UNCERTAIN: Whether the one-minute Khaba path passed stakeholder validation after QA.
- UNCERTAIN: Whether October 8 Khaba needed the same backfill as October 9-12.
- UNCERTAIN: What exact delay target Adrien will accept for `SCR-1284` RTM.
- UNCERTAIN: Whether the deployed Khaba DAGs have been observed skipping a missing source in the live Airflow environments, and whether the temporary 1440-minute Variable has been removed.
- UNCERTAIN: Whether [[francois-delcourt]] has validated SCR-1289 and whether the 19 October REC run completed once its window opened.
- UNCERTAIN: Whether the first scheduled HPX write-path run has the expected timing/verification behaviour.
- UNCERTAIN: Whether Khavda's bulk-read change behaves correctly against live TSDB under shared Athena-slot contention.

## Sources

Main sources are below. The full trail from before the 2026-10-11 split is on [[smp-platform]].

- `sources/meetings/2026-07-30-1232-granola-generation-data-scraper.md`
- `sources/meetings/2026-08-27-granola-mateo-call.md`
- `sources/meetings/2026-09-23-1630-granola-smp-sprint-review.md`
- `sources/meetings/2026-10-07-granola-sprint-review.md`
- `sources/meetings/2026-10-09-1415-granola-daily-standup.md`
- `sources/codex-conversations/2026-09-17-codex-conversations.txt`
- `sources/codex-conversations/2026-09-21-codex-conversations.txt`
- `sources/codex-conversations/2026-09-28-codex-conversations.txt`
- `sources/codex-conversations/2026-09-30-codex-conversations.txt`
- `sources/codex-conversations/2026-10-09-codex-conversations.txt`
- `sources/claude-conversations/2026-10-01-claude-smp-8ce08f10.txt`
- `sources/claude-conversations/2026-10-13-claude-smp-31a97f39.txt`
- `sources/claude-conversations/2026-10-13-claude-smp-32cc547a.txt`
- `sources/claude-conversations/2026-10-13-claude-smp-5c0b0e8d.txt`
- `sources/claude-conversations/2026-10-13-claude-smp-8ce08f10.txt`
- `sources/claude-conversations/2026-10-13-claude-smp-e3dc30e8.txt`
- `sources/codex-conversations/2026-10-13-codex-conversations.txt`
- `sources/meetings/2026-10-14-0945-granola-daily-standup.md`
- `sources/meetings/2026-10-14-1415-granola-daily-standup.md`
- `sources/claude-conversations/2026-10-14-claude-smp-8ce08f10.txt`
- `sources/claude-conversations/2026-10-14-claude-smp-bb0d20e1.txt`
- `sources/claude-conversations/2026-10-15-claude-smp-8ce08f10.txt`
- `sources/claude-conversations/2026-10-15-claude-smp-822de913.txt`
- `sources/claude-conversations/2026-10-15-claude-smp-cbea7fa4.txt`
- `sources/claude-conversations/2026-10-16-claude-smp-4e922cd7.txt`
- `sources/claude-conversations/2026-10-17-claude-smp-4e922cd7.txt`
- `sources/claude-conversations/2026-10-17-claude-smp-e4dded4d.txt`
- `sources/claude-conversations/2026-10-19-claude-smp-4e922cd7.txt`
- `sources/claude-conversations/2026-10-19-claude-smp-822de913.txt`
- `sources/claude-conversations/2026-10-19-claude-smp-8ce08f10.txt`

Last Updated: 2026-10-20
