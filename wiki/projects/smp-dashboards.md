# SMP Dashboards

## Summary

Several dashboard efforts were active in late June and early July 2026: Japan interconnector, Yoko day-ahead price and volume, India IEX REC, Carlos's TV/dashboard setup, Grafana backup, and possible TSDB integration.

Dashboard delivery was moving quickly, while infrastructure work was slower and often blocked by access, proxy, VPN, or dependency issues.

## Details

- Yoko day-ahead price and volume dashboard was complete and live in Japan production by July 1.
- Yoko dashboard shows price and volume percentile curves for Tohoku and Chugoku.
- Yoko percentiles are fixed at p5, p25, p50, p75, and p95.
- Yoko date range is +1 day for day-ahead view.
- India IEX REC dashboard is live in India production and pulls from the IEX API.
- India REC dashboard shows cleared volume, total sell, total buy, and clearing price.
- India REC data window was extended from 1 year to 4 years, starting from 2023.
- Grafana dashboard backup was considered desirable. One discussed approach was API export of JSON config to SharePoint or an auto-PR, but access was blocked by VPN/Zscaler constraints.
- Carlos requested interconnector data also be pushed to TSDB.
- Japan interconnector production dashboard updates on July 6 added daily-average JEPX spread, interconnector-specific spread labels, and compact `Last`, `WTD avg`, and `MTD avg` spread stat boxes.
- The final Japan interconnector stat layout uses three right-aligned metric boxes per interconnector, with WTD/MTD based on the latest available spread date in the selected range.
- July 7 Francois-help notes describe the expected self-service dashboard flow: register dataset/schema in CDH, assign the dataset to the CDH project for dev/QA/prod, add the data source to the CDH project in Grafana, then edit the visible dashboard.
- The same notes say the contributor had edit rights in QA but not dev, and that the SMP Dashboard README has the full guide.
- Carlos previously handled CDH setup himself; Brian only added the data source to the CDH project.
- July 7 Codex work added a targeted CDH dataset-manager path for Japan interconnector effective-capacity historical stage registration and improved schema/crawler refresh behavior for existing datasets and stages.
- CDH crawler lag made the historical stage appear broken at first; once it caught up, the cleaner same-dataset/two-stage model was restored.
- July 8 AWS migration standup favored backing up the full Grafana database instead of only dashboard JSON exports. Grafana was thought to use MySQL or Postgres, with an option to connect to existing RDS using the same pattern as Airflow.
- July 17 Codex notes requested hardening the manual `cdh-register.yml` workflow so the target environment is inferred from the branch and the one-hour CDH token can be pasted as an explicit workflow input. The motivation was to avoid a dev branch run accidentally targeting production.
- July 17 `SCR-1202` dashboard work added an opt-in HJKS 2Y `As of` selector pattern with immediate visibility for complete scheduled snapshots, exact snapshot filtering across all 12 panels, and a reusable look-back playbook for future dashboards.
- August 3 SMP India notes reaffirm the dashboard publication path for new DAG outputs: create the CDH dataset in the project, write parquet under a matching S3 dataset key and stage, then query it from Grafana through Athena once CDH registration exposes the table.
- Mateo identified generation dashboarding as a straightforward first India DAG-to-Grafana use case, with forecaster benchmarking as a more complex follow-up because it compares three external forecasters against actual generation curves and may require several data sources. Brian could not yet confirm the forecaster benchmarking ownership or source breakdown on 2026-08-04.
- August 4 production Japan dashboard troubleshooting showed a practical CDH registration hazard: the manual workflow can finish green after submitting crawler jobs even when Athena tables are not yet visible or stage refreshes were skipped/rejected because another crawler was already running.
- `smp-dashboard` depends on private `cdh-sdk` directly from GitHub Tools, not only on Artifactory packages. The manual CDH registration workflow therefore needs `ENGIE_GITHUB_TOOLS_NETRC` for dependency installation and `CDH_TOKEN_ONESHOT` for CDH itself.
- The August 4 production registration failure was caused by an expired or revoked GitHub Tools credential while installing `cdh-sdk`; it did not reach CDH and caused no partial registration. A fresh GitHub Tools PAT with access to `GBSEngieDigitalDPAAS/cdh-sdk` fixed the dependency step.
- The long-term cleanup preference is to publish `cdh-sdk` to Artifactory or use an organization-managed machine account, rather than keeping a personal GitHub Tools PAT in `smp-dashboard`.
- August 11 standup and grooming notes kept old Louis-dashboard metadata as a blocker. The team can pre-check whether providers already exist in TSDB, identify provider owners, and coordinate injection scheduling so dashboard continuity is not disrupted.
- The August 11 feature spike makes Grafana alerting a possible alternative to stakeholders manually checking dashboards every day, especially for threshold-based monitoring such as power-price triggers. Grafana monitoring views also need an inventory before the team claims a reusable operations pattern.
- August 19 India planning added a bid-stack dashboard request: publish 15-minute buy/sell volume and price across three markets, group contracts by price category, push the result as TSDB time series, and build one Grafana dashboard per market. Japan bid-stack reports were named as the reference shape.
- The August 20 SCR-1222 Grafana spike recommended five native or official workflow improvements: data freshness and alerts, dynamic dashboards, guided drill-downs, Git Sync, and the Foundation SDK. No community plugin made the top five because native Grafana capabilities carried broader value with less maintenance and governance overhead.
- The SCR-1222 output was a brief Confluence-ready table plus a private interactive demo at `https://smp-grafana-top-five.baraluga.chatgpt.site`.
- The August 27 FEDV chapter meeting shifted monitoring standardization toward Splunk for 24/7 production support because the IS team recommends Splunk, has Splunk expertise, and lacks internal Grafana expertise for round-the-clock support. Existing or planned Grafana deployments may be converted to Splunk where needed.
- Dashboard standardization was flagged as a chapter-level need after initial business stakeholder presentations showed inconsistent visual design, including random colors and unclear representations.
- The same FEDV meeting marked Power BI MCP work as not relevant for now because usage was declining while Grafana and Synapse took over. Argos and one other Power BI project were expected to be decommissioned by year-end, although Microsoft Copilot licensing could make future Power BI agent integration possible if demand returns.
- August 27 `SCR-1238` work exposed a dashboard source-control convention: portable Grafana dashboard sources belong under `dashboards/india/`, while `dashboards/backups/india/` is for snapshots captured after live promotion. The portable India IEX dashboard source should retain the dashboard UID when it is meant to overwrite the existing dashboard, but datasource UIDs must be parameterized, for example with `${DS_SMP_CDH}`, so dev, QA, and production imports can bind the correct Athena datasource.
- The same work clarified that the existing India IEX DAM/GDAM/RTM MCP and volume dashboard cannot display a raw TSDB UUID directly because it queries Athena/CDH. Khaba active generation therefore needs a CDH/Athena table sourced from the validated Khaba pipeline before the Grafana panel can be imported and tested cleanly.
- During the `SCR-1238` migration, the dashboard query was made tolerant of overlap between a temporary rolling Khaba snapshot and the new date-based Parquet files by deduplicating rows and preferring the daily files.
- September 1 sprint planning aimed for at least one mini POC for the 2026-09-09 sprint review or steering committee. Candidate themes came from the SCR-1235 epic and included Grafana or Airflow out-of-the-box features.
- A September 1 Copilot reconnaissance ranked `SCR-1248` Grafana Drill-downs as a low-risk POC because it stays inside `smp-dashboard` JSON and can link an overview dashboard to the existing `outages_report.json` detail view without new infrastructure, plugins, credentials, DAG work, or Helm changes. Brian then chose to stay in Jira-management mode and set `SCR-1248` Story Points to 3.
- The `SCR-1248` estimate was calibrated against actual SCR story-point anchors: 2-point tickets for bounded panel/spike work such as `SCR-1238` and `SCR-1222`, 3-point tickets for new patterns or new dashboards such as `SCR-1202` and `SCR-1243`, and 5-point tickets for new data-source or infrastructure integrations such as `SCR-1229`, `SCR-1230`, and `SCR-1171`.
- Later September 1 Codex work corrected the `SCR-1248` interpretation: ordinary Grafana dashboard data links were the wrong product shape for the ticket, so both dashboard-link attempts were reverted from `smp-dashboard` `main`. The useful direction is Grafana's dedicated Drilldown apps/queryless exploration, which fit observability backends such as Prometheus/Mimir, Loki, Tempo, or Pyroscope rather than Athena/CDH market dashboards.
- A fresh isolated `SCR-1248` Metrics Drilldown POC was then committed to branch `scr-1248-grafana-metrics-drilldown` at `9b1e7bf`. It uses Grafana 12.2.5, Metrics Drilldown 2.5.1, Prometheus 3.5.0, and synthetic SMP-style scraper metrics labelled by region, DAG, scraper, and status. It is intentionally not a production SMP integration.
- September 2 backlog grooming narrowed Grafana usage monitoring to dashboard access by user and frequency, excluding internal team usage. Loki was identified as the likely first tool because it is Grafana-native and Signups already has Loki running; Okta logs may provide basic connection metadata but need a quick check.
- The same grooming discussion noted that the shared Grafana/Airflow stack is used beyond SMP by Synapse and Delphi, so monitoring cost attribution should be clarified before SMP absorbs the whole cost.

## Open Questions

- UNCERTAIN: Grafana backup implementation path remains blocked by network/VPN access in the captured notes.
- UNCERTAIN: CDH crawler delay duration and operator-facing status behavior are not fully characterized.
- UNCERTAIN: Grafana database engine and RDS backup path still need confirmation.
- UNCERTAIN: Whether the `cdh-register.yml` input-token redesign has been implemented after the July 17 request.
- UNCERTAIN: Whether the forecaster benchmarking sources and ownership will be handled by Brian's team, Mateo, Adrian, or a broader India workflow.
- UNCERTAIN: Whether `cdh-register.yml` should fail, wait, or emit a separate required follow-up when requested production stage refreshes are skipped because a crawler is already running.
- UNCERTAIN: Whether `cdh-sdk` will be packaged into Artifactory or remain a direct GitHub Tools dependency.
- UNCERTAIN: Which old Louis-dashboard providers and metadata owners are needed before TSDB injection can proceed.
- UNCERTAIN: Which three India bid-stack markets are in scope and whether the Japan bid-stack reference has exact reusable panel semantics.
- UNCERTAIN: Whether the SCR-1222 Git Sync and Foundation SDK recommendations were later piloted against committed SMP dashboard JSON.
- UNCERTAIN: Which Grafana deployments are actually being converted to Splunk, and whether SMP dashboards are in that conversion scope.
- UNCERTAIN: Which Power BI project besides Argos is expected to be decommissioned by year-end.
- UNCERTAIN: Whether the `SCR-1238` portable India IEX dashboard JSON has been imported into live QA Grafana and verified against the exact Khaba TSDB series.
- UNCERTAIN: Whether the September 9 mini POC should stay as a spike-only artifact or be promoted into production dashboard JSON.
- UNCERTAIN: Whether the isolated `SCR-1248` Metrics Drilldown branch should become a PR, remain a demo artifact, or be superseded by a different SCR-1235 POC.
- UNCERTAIN: Whether Loki's default logs expose enough dashboard-access detail for the intended Grafana usage-monitoring scope.
- UNCERTAIN: Whether Okta logs are accessible and useful enough for dashboard usage metadata.
- UNCERTAIN: Whether Bastian or another owner decides cost attribution for shared Grafana/Airflow monitoring across SMP, Synapse, and Delphi.

## Sources

- `sources/meetings/2026-06-24-1552-granola-backlog-grooming.md`
- `sources/meetings/2026-07-01-1630-granola-smp-revie.md`
- `sources/meetings/2026-07-02-1100-granola-sprint-planning.md`
- `sources/codex-conversations/2026-07-06-codex-conversations.md`
- `sources/meetings/2026-07-07-1530-granola-francois-help.md`
- `sources/codex-conversations/2026-07-07-codex-conversations.md`
- `sources/meetings/2026-07-08-1514-granola-aws-migration-standup.md`
- `sources/codex-conversations/2026-07-17-codex-conversations.md`
- `sources/meetings/2026-08-03-1415-granola-busy.md`
- `sources/notes/2026-08-04-ingest-handover-clarifications.md`
- `sources/codex-conversations/2026-08-04-codex-conversations.txt`
- `sources/meetings/2026-08-11-1415-granola-daily-standup.md`
- `sources/meetings/2026-08-11-1430-granola-backlog-grooming.md`
- `sources/meetings/2026-08-19-granola-backlog-grooming.md`
- `sources/codex-conversations/2026-08-20-codex-conversations.txt`
- `sources/meetings/2026-08-27-granola-fedv-chapter-meeting.md`
- `sources/codex-conversations/2026-08-27-codex-conversations.txt`
- `sources/meetings/2026-09-01-granola-busy.md`
- `sources/copilot-conversations/2026-09-01-copilot-conversations.md`
- `sources/codex-conversations/2026-09-01-codex-conversations.txt`
- `sources/meetings/2026-09-02-backlog-grooming.md`
- `sources/meetings/2026-09-02-standup.md`

Last Updated: 2026-09-02
