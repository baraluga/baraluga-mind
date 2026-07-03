# SMP Revie

Source type: Granola meeting notes
Meeting ID: `cb270179-9b38-4e02-8eac-07a43d413c2c`
Date: 2026-07-01 16:30 GMT+8
Participants known to Granola: Brian Alexander Peralta

Note: This is from Granola notes/summaries, not a verbatim transcript.

## Discussed

- Sprint goals were separating Japan and India environments and starting Japan interconnector data retrieval/display.
- Japan interconnector dashboard is an early Grafana dashboard for daily average spread across interconnector lines.
- Japan team process and data management flow were mapped; 7 priority interconnector lines were identified.
- Current Japan process uses Excel updated monthly; goal is automated collection and timely Grafana visualization.
- Metrics shown: actual available capacity, actual power flow, and day-ahead price difference.
- Display order follows north-to-south flow as specified by Japan team.
- Backfill completed from March/April, the fiscal year start.
- Airflow DAGs were implemented for yearly, monthly, weekly, and daily granularities.
- Yoko day-ahead price and volume dashboard is complete and live in Japan production.
- Yoko dashboard shows price and volume percentile curves for Tohoku and Chugoku.
- Percentiles are fixed at p5, p25, p50, p75, and p95.
- Date range is +1 day for day-ahead view.
- India IEX REC dashboard is live in India production and pulls from IEX API.
- India REC dashboard shows cleared volume, total sell, total buy, and clearing price.
- India data window was extended from 1 year to 4 years, from 2023.
- Upcoming generation data ingestion into TSDB was flagged.

## Next Steps

- Test TSDB injection using interconnector data as a pilot.
- Francois to share generation data task details with the SMP team.
- Continue coordinating interconnector dashboard feedback with Japan team.

Last Updated: 2026-07-04
