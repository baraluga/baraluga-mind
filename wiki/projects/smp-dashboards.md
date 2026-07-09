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

## Open Questions

- UNCERTAIN: Grafana backup implementation path remains blocked by network/VPN access in the captured notes.
- UNCERTAIN: CDH crawler delay duration and operator-facing status behavior are not fully characterized.
- UNCERTAIN: Grafana database engine and RDS backup path still need confirmation.

## Sources

- `sources/meetings/2026-06-24-1552-granola-backlog-grooming.md`
- `sources/meetings/2026-07-01-1630-granola-smp-revie.md`
- `sources/meetings/2026-07-02-1100-granola-sprint-planning.md`
- `sources/codex-conversations/2026-07-06-codex-conversations.md`
- `sources/meetings/2026-07-07-1530-granola-francois-help.md`
- `sources/codex-conversations/2026-07-07-codex-conversations.md`
- `sources/meetings/2026-07-08-1514-granola-aws-migration-standup.md`

Last Updated: 2026-07-09
