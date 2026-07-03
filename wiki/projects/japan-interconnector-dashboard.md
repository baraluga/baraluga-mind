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

## Open Questions

- UNCERTAIN: Whether existing OCT time series can be reused for interconnector data.
- UNCERTAIN: Japan team's final Y-axis requirement still needed confirmation in the July 2 planning notes.

## Sources

- `sources/meetings/2026-06-24-1552-granola-backlog-grooming.md`
- `sources/meetings/2026-06-29-1415-granola-standup.md`
- `sources/meetings/2026-07-01-1630-granola-smp-revie.md`
- `sources/meetings/2026-07-02-1500-granola-sprint-planning.md`

Last Updated: 2026-07-04
