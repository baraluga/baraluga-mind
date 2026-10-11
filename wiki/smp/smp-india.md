# SMP India

## Current State

As of 2026-10-09. These are the India data products built on [[smp-platform]]. Stakeholders are Mateo (on leave in early October), Adrien/Adrian (escalation while Mateo is away), and Lou Dubuisson (incoming point of contact). Validation runs through Francois.

**Delivered by the 2026-10-07 sprint review:**
- Legacy Green DAM scraper fix (`SCR-1264`)
- IEX bid-stack data in TSDB (`SCR-1253`)
- India geomap in Grafana
- Bilateral-contract dashboard (`SCR-1275`)
- Grafana alerting docs

**In flight or pending:**
- `SCR-1286`: October IEX Green DAM/GDAM gap fix, pushed to [[apac-tsdb-scraper]]. Lou confirmed it works; closure still pending.
- `SCR-1284`: about 20 minutes of IEX RTM delay to Grafana. The cause is two independent schedules: `apac-tsdb-scraper` publishes to TSDB, then an India DAG copies TSDB to CDH. If Adrian accepts a 2–3 minute target, the proposal is for Airflow to write RTM to TSDB and CDH in parallel. True realtime would follow the [[darwin-collector]] pattern.
- The GDAM Grafana panel queries the empty `india_iex_tsdb_dashboard_latest` table, while the data sits in `india_iex_tsdb_expanded_latest` (2026-10-09). This looks like a stale panel reference.
- `SCR-1274`: HPX national DAM/GDAM/RTM scraper. Implemented locally, blocked on TSDB IDs from Adrien. The request is three series with a two-day forward view.
- Darwin assets for Tuticorin and four new sites: blocked on proxy and IT. See [[darwin-collector]].
- Grid India (`SCR-1230`) and the national H. India site: blocked on access. See [[smp-india-access]].
- Khaba QA: CDH support changed an SCP on 2026-09-30 to allow cross-region access. Re-enabling the QA DAGs and backfilling TSDB UAT is still open.
- Not urgent: a KPI dashboard Mateo wants to pair on (TSDB → calculations → CDH → Grafana), and adapting the Aurora XLSX loader, which needs dataset, format, and ownership answers first.

## Background

### Khaba Generation

- Source: a CDH-managed FTP CSV in S3 (`KHABA/FTP_DATA<dd-mm-yyyy>.csv`, `ap-south-1`) with one-minute readings, overwritten through the day.
- **15-minute path:** a realtime DAG and a previous-day reconciliation DAG share one parser. They publish only complete 15-minute averages of Active Power, GHI, Module Surface Temperature, and Ambient Temperature to TSDB (Mateo later renamed the irradiance series to POA without changing its ID), under provider `R&F India` (code alias `rf_india`; series IDs versioned in code). They verify by read-back, then write date-based CDH parquet for Athena/Grafana (`SCR-1238`). Publication is gated by `KHABA_GENERATION_TSDB_PUBLISH_ENABLED`.
- **One-minute path (`SCR-1259`):** runs in parallel for operational needs, with five more series IDs. The 15-minute path stays unchanged. Promoted to QA on 2026-09-17; backfill runs through `smp-common 0.8.0`.
- **Missing source files:** an Airflow rescheduling sensor with exponential backoff, capped at 15 minutes, with a failure horizon of about six hours. Mateo was to be asked whether to back off only after about five consecutive misses.
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

## Open Questions

- UNCERTAIN: Root cause of the 2026-09-04 Khaba Dev/QA cross-account S3 loss (recorded as "KAVA"), and whether the 2026-09-30 SCP change fixed it. Khaba and Khavda are two distinct sites; see [[aliases]] for variants.
- UNCERTAIN: Whether bilateral-contract data should stay CDH-only or also feed TSDB.
- UNCERTAIN: Whether the live GDAM panel already diverged from the checked-in query.
- UNCERTAIN: Whether the one-minute Khaba path passed stakeholder validation after QA.

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

Last Updated: 2026-10-11
