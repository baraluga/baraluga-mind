# SMP Dashboards

## Current State

As of 2026-10-22. Grafana dashboard work across SMP Japan and India. India data behind the dashboards is on [[smp-india]]; Japan interconnector dashboards are on [[japan-interconnector-dashboard]]; alerting is on [[smp-alerting-and-ops]].

- **India geomap:** delivered. It shows realtime market price and volume by region, with max/min/average and current-slot views and a freshness indicator. The Plotly prototype was replaced by native Grafana geomap, and colour settings live in the dashboard JSON, so the same JSON imports into production. Mateo expects three maps (price/volume sets joined by region codes such as `N1`–`N3`), using fixed scales: yellow to red, price 0–10,000, volume up to last year's maximum plus 10%.
- **Bilateral contracts (`SCR-1275`):** a table of all contracts with a region legend, freshness, and anomaly indicators. Still needs validation. It consumes `SCR-1278`'s validated tables rather than fixing scraper behaviour in dashboard code, and it must show source differences explicitly (see [[smp-india]]).
- **IEX `DAM/GDAM/RTM MCP & Volume Trends`:** the main India market dashboard. Its six Khaba panels and the R&F Assets & Forecasts dashboard now query the separate `india_khaba_forecasts_latest` dataset instead of forecasts embedded in actual-generation output. QA and prod imports plus the matching `smp-india` promotion were completed; the remaining actual-generation gaps for 12–15 October trace to incomplete upstream CSVs, not the forecast path. It also includes the `SCR-1257` historical MCP heatmap and `SCR-1243` bid-stack curves; the bid-stack curves use separate buy/sell axes because the values are already cumulative, plus an estimated crossing marker.
- **India dashboard releases (`SCR-1296`):** official repo dashboards are released manually from `smp-dashboard` `main` to the read-only-in-practice `(⭐) Golden Copies` folder in QA and prod. The release workflow completed its first run (nine dashboards, no deletions) on 2026-10-19. Users may copy dashboards or panels to their personal Views folders; direct edits in Golden Copies are overwritten by the next release. The workflow should block a release on live-version drift rather than overwrite it blindly.
- **Portable map panels:** Mateo's copied map panels failed because panel-only copies omit dashboard-level Grafana variables and shared-query panel references. The POC now makes map, freshness, zone-table, and price-stat panels self-contained with direct Athena queries and safe defaults. Treat independent panel pasting as the preferred pattern where it does not remove needed controls.
- **Grafana usage (`SCR-1252`):** SMP runs Grafana OSS, so Enterprise Usage Insights isn't available. The cheapest first answer is active-user counts from the org-users API (`lastSeenAt`) or Okta logs, going deeper only if usage justifies it.
- **QA datasource cleanup (`SCR-1296`):** a stray Athena datasource should only be removed after checking whether it is the default and whether dashboards or alert rules reference it. A QA-only, unexecuted script was prepared to perform that inventory and require typed confirmation before deletion; deletion itself needs a Grafana Admin token, not the Editor-scoped release token.
- **Not urgent:** Matteo's KPI dashboard (end of year; flat CDH output if its shape is unknown) and the Grafana + JupyterLab integration, waiting on Nilo (see [[smp-jupyter-dag-authoring]]).

## Background

### Publishing a dashboard

- **Data path:** DAG writes parquet → CDH dataset with a matching S3 key and stage → Athena → Grafana. Rules are on [[smp-platform]]. Grafana cannot show a raw TSDB series, so TSDB data needs a CDH table first.
- **Registration workflow:** `cdh-register.yml` in `smp-dashboard`.
  - It needs `ENGIE_GITHUB_TOOLS_NETRC` (private `cdh-sdk` installs from GitHub Tools) and a one-hour `CDH_TOKEN_ONESHOT`.
  - A green run can still leave Athena without the table if the crawler was busy. Production now waits for the crawler and refreshes the CDH project role before reporting green: India prod got this in `154cec1`.
  - The preference is to move `cdh-sdk` to Artifactory or a machine account instead of a personal PAT.
- **Schema samples must have zero rows,** or Athena serves them as data. Dashboard queries should prefer real pipeline files when a table can scan both.
- **Source control:**
  - Portable dashboard sources live under `dashboards/<region>/`, and post-promotion snapshots under `dashboards/backups/<region>/`.
  - Keep the dashboard UID when the source is meant to overwrite a live dashboard, but parameterise datasource UIDs (e.g. `${DS_SMP_CDH}`) so dev, QA, and prod bind correctly.
  - Git as the single source of truth, with no drift from live Grafana, remains the goal.
- **Permissions:** group-based edit rights (e.g. Intact `editor`) can show as `Viewer` until the user logs out and back in. On 2026-10-22, Lou remained `Viewer` in QA after a forced logout/re-login despite being in `smp-dashboard-editor`, while other group members showed `Admin`; the general mapping therefore works, but Lou's group/token sync remains unresolved.

### Patterns and Preferences

- **Multi-endpoint data:** if scheduled refresh is acceptable, put a backend aggregator in front that writes to CDH, and keep Grafana on Athena. Interactive, filter-triggered API calls would need a custom datasource or plugin, which is a much heavier ask.
- **Grafana spike (`SCR-1222`):** the best native wins are freshness and alerts, dynamic dashboards, guided drill-downs, Git Sync, and the Foundation SDK. No community plugin made the cut.
- **Drilldown apps** (`SCR-1248`) suit Prometheus/Loki-style observability data, not Athena market dashboards. Ordinary data links were reverted. An isolated Metrics Drilldown demo branch exists (`scr-1248-grafana-metrics-drilldown`).
- **Demos:** go deep on one or two production dashboards with different visual types, and treat screenshots as evidence.
- **Chapter context:** dashboard visual standardisation was flagged as a need. The IS team prefers Splunk for 24/7 production monitoring. Power BI is declining in favour of Grafana and Synapse.
- **Story-point anchors:** 2 for a bounded panel or spike, 3 for a new pattern or dashboard, 5 for a new data source or infrastructure integration.

## History

- 2026-07-01: Japan "Yoko" day-ahead price/volume percentile dashboard and India IEX REC dashboard (4 years from 2023) live in production.
- 2026-07-17: reusable HJKS 2Y `As of` look-back selector pattern (`SCR-1202`).
- 2026-09-03: India IEX heatmap added; India prod CDH role-refresh fix.
- 2026-10-07: India geomap and bilateral-contract dashboard delivered.
- 2026-10-14: the IEX map POC was revised so every panel works when copied independently; the corrected import was tested in Mateo's dashboard.
- 2026-10-17: Khaba forecast panels switched to the separate forecast dataset; Grafana import is pending.
- 2026-10-19: Khaba forecast dashboards were imported and the export change promoted; the first managed release created `(⭐) Golden Copies` in India QA and prod.

## Open Questions

- UNCERTAIN: Whether production Grafana has the latest India IEX dashboard JSON (heatmap, schema-artifact filters, bid-stack crossing marker).
- UNCERTAIN: Who validates the bilateral-contract dashboard before it counts as done.
- UNCERTAIN: Whether Grafana backup should be the full database (the July preference) or JSON in Git. No backup path was confirmed.
- UNCERTAIN: Which Grafana deployments, if any, are being converted to Splunk.
- UNCERTAIN: Whether anyone still needs the National/Regional Expanded dashboards, whether `adhj947` replaces `ad6txb2`, and whether `corsica` should remain personal or become official.
- UNCERTAIN: Whether copying a dashboard or a single panel from Golden Copies works as documented in this Grafana version.

## Sources

- `sources/meetings/2026-07-01-1630-granola-smp-revie.md`
- `sources/meetings/2026-07-07-1530-granola-francois-help.md`
- `sources/codex-conversations/2026-07-17-codex-conversations.md`
- `sources/codex-conversations/2026-08-04-codex-conversations.txt`
- `sources/codex-conversations/2026-08-20-codex-conversations.txt`
- `sources/meetings/2026-08-27-granola-fedv-chapter-meeting.md`
- `sources/codex-conversations/2026-08-27-codex-conversations.txt`
- `sources/copilot-conversations/2026-09-01-copilot-conversations.md`
- `sources/codex-conversations/2026-09-01-codex-conversations.txt`
- `sources/codex-conversations/2026-09-02-codex-conversations.txt`
- `sources/codex-conversations/2026-09-03-codex-conversations.txt`
- `sources/codex-conversations/2026-09-22-codex-conversations.txt`
- `sources/codex-conversations/2026-09-30-codex-conversations.txt`
- `sources/meetings/2026-09-30-1530-granola-sprint-backlog-grooming.md`
- `sources/meetings/2026-10-01-1433-granola-backlog-grooming-again.md`
- `sources/codex-conversations/2026-10-01-codex-conversations.txt`
- `sources/meetings/2026-10-05-granola-trading-data-platform-presentation-and-jupyterlab-roadmap-with-bong.md`
- `sources/meetings/2026-10-06-1415-granola-smp-standup.md`
- `sources/meetings/2026-10-07-granola-sprint-review.md`
- `sources/meetings/2026-10-14-1441-granola-mateo-call.md`
- `sources/claude-conversations/2026-10-14-claude-smp-bde564a1.txt`
- `sources/claude-conversations/2026-10-16-claude-smp-4e922cd7.txt`
- `sources/claude-conversations/2026-10-17-claude-smp-4e922cd7.txt`
- `sources/claude-conversations/2026-10-19-claude-smp-4e922cd7.txt`
- `sources/claude-conversations/2026-10-19-claude-smp-7de67109.txt`
- `sources/claude-conversations/2026-10-20-claude-smp-7de67109.txt`
- `sources/claude-conversations/2026-10-22-claude-smp-1439c39e.txt`
- Older sources are in this page's git history before 2026-10-11.

Last Updated: 2026-10-23
