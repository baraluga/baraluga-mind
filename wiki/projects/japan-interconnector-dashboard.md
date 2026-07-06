# Japan Interconnector Dashboard

## Summary

Japan interconnector work aims to automate data collection and visualization that was previously handled through monthly Excel updates. The dashboard work focuses on seven priority interconnector lines and shows actual available capacity, actual power flow, and day-ahead price difference.

The notes describe an early Grafana dashboard for daily average spread across interconnector lines, with display order following north-to-south flow as specified by the Japan team.

## Details

- Backfill was completed from March or April 2026, aligned to the fiscal year start.
- Airflow DAGs were implemented for yearly, monthly, weekly, and daily granularities.
- Validation approach discussed in grooming: recover data from two weeks prior, run the equivalent process, and compare against IROMI's Excel output.
- Two dashboard variants were prepared: one with separate JEPX prices and one combined.
- JEPX prices matched the spreadsheet with minor rounding differences; daily values did not align because of timing differences.
- TSDB push for interconnector data can start once Francois provides time series IDs.
- Japan team should own TSDB catalog/provider creation; the dev team only needs time series IDs.
- Existing OCT time series may be reusable, but this needed checking.
- July 6 source probes found OCCTO actual-flow data available only from `2025-04-01` through the checked public paths. FY2019 actual-flow backfill was not feasible from OCCTO.
- July 6 source probes found JEPX FY2019 prices available through the existing yearly CSV path.
- July 6 source probes found OCCTO FY2019 capacity available. Daily capacity worked cleanly; historical yearly/monthly/weekly capacity had `akyuryMax1 = "-"`, so daily capacity was preferred for historical backfill unless the team decides how to model missing max values.
- A local `smp-japan` operator CLI was implemented and pushed to support JEPX, daily capacity, and actual-flow historical backfill with dry-run defaults and explicit execute mode.
- Production dashboard work in `smp-dashboard` switched JEPX spread to daily-average spread, added interconnector-specific spread labels, and added `Last`, `WTD avg`, and `MTD avg` stat boxes.
- The final stat behavior anchors WTD/MTD to the latest available daily spread date inside the selected dashboard range, not to the selected range end, to avoid misleading blanks when the range extends beyond available JEPX data.
- Two follow-up Jira stories were created for Hiromi's enhancement requests: `SCR-1197` look-back dashboard and `SCR-1198` Excel/data export.

## Open Questions

- UNCERTAIN: Whether existing OCT time series can be reused for interconnector data.
- UNCERTAIN: Japan team's final Y-axis requirement still needed confirmation in the July 2 planning notes.
- UNCERTAIN: Whether capacity yearly/monthly/weekly historical rows with missing max values should ever be supported, or whether daily-only historical capacity is sufficient.
- UNCERTAIN: The parent Jira tickets `SCR-1126`, `SCR-1127`, `SCR-1128`, `SCR-1129`, `SCR-1168`, `SCR-1138`, and `SCR-1137` may still need workflow cleanup after an interrupted transition attempt.

## Sources

- `sources/meetings/2026-06-24-1552-granola-backlog-grooming.md`
- `sources/meetings/2026-06-29-1415-granola-standup.md`
- `sources/meetings/2026-07-01-1630-granola-smp-revie.md`
- `sources/meetings/2026-07-02-1500-granola-sprint-planning.md`
- `sources/codex-conversations/2026-07-06-codex-conversations.md`

Last Updated: 2026-07-06
