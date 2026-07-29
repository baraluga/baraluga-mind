# Sprint Review

Source type: Granola meeting notes

Meeting ID: `de8abf24-39b3-493e-a8e2-9893f7b81af1`

Meeting date/time: Jul 29, 2026 4:30 PM GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves Granola-provided meeting notes and summaries. It is not a verbatim transcript.

## Discussion Notes / Summary

### Sprint Accomplishments (SMP Japan)

- Lookback functionality added to Grafana dashboards.
  - Covers: 2Y, nuclear by region, most recent interconnector views.
  - Provides historical snapshots, 1-3 per day depending on dashboard.
- Interconnector dashboard enhanced with operational capacity.
  - Previously showed: available capacity, actual flow, EEX/JPX prices.
  - Now also plots operational capacity alongside existing metrics.
  - Data backfilled to 2019 for consistency.
  - Brian flagged: no trading expertise to validate interpretation; Japan colleagues asked to QA.

### Sprint Accomplishments (SMP India)

- Aurora CLI hardened against minor Excel template changes.
  - Regression traced to template inconsistency; fix applied.
  - Will still break on drastic structural changes, such as workbook consolidation.
- Darwin scraper debugging resolved.
- India DAG contributor onboarding started.
  - Ongoing: ironing out access issues and IT requests for future contributors.

### Budget and Capacity

- Projecting around 15% budget overshoot (time and material contract).
  - Driven by additional requests not in original scope.
  - Remaining capacity reduced to Brian only for the final sprint.
  - Estimated overshoot: around 5,800 EUR, split 60/40.
  - Could land at 7% or lower depending on final sprint scope.
- Final sprint planning tomorrow to confirm Brian's capacity and task list.

### Data Access Strategy and Next Steps

- Louis needs programmatic access to dashboard underlying data.
  - Three options discussed:
    1. SharePoint upload (cheapest, least robust).
    2. Parquet files from dashboards (moderate effort).
    3. Push time series to TSDB (preferred).
  - Carlos strongly prefers TSDB: single client works locally and in cloud (AWS), avoids data source fragmentation.
  - Team to identify required time series and build metadata/providers; may carry into backlog due to provider red tape.
- India generation data push to TSDB in scope.
  - 15-minute interval data; potential delay risk through workflow.
  - May require moving to TSDB first layer for smoother access.
  - Call to be scheduled with Brian to clarify data access and sharing on CDH.
- OR curves for Japan, similar to India solution, raised.
  - Current access is manual via Excel workbook, not API.
  - Team to confirm whether data exists in the API; if not, reuse India Excel-based approach.
  - Prioritization needed: dashboard time series vs. file-based uploads, given sprint capacity.

### Deprioritized Items

- Deployment automation and DAG developer experience improvements pushed down.
  - Lower priority given budget constraints and TSDB injection work.
  - Feedback from Material and feature/DAG developer still to be incorporated when capacity allows.

## Next Steps / Action Items Present in Granola

- Add operational capacity to TSDB with backfill: Carlos requested backfill from at least 2025, ideally 2019, to match Grafana dashboard data.
- Schedule call with Brian on India generation data access: clarify CDH data location, sharing method, and any access pain points before starting TSDB push.
- Confirm whether Japan OR curve data exists in the API: if not in API, proceed with Excel-based solution matching the India approach; then prioritize against dashboard time series work.
- Final sprint planning tomorrow: confirm Brian's capacity and scope to determine whether overshoot lands at 15% or closer to 7%.

Last Updated: 2026-07-29
