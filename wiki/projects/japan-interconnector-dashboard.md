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
- July 7 standup notes say QA was stable, with no out-of-memory issues seen that sprint, and that the historical backfill would run directly in production instead of QA.
- July 7 standup notes estimated the production backfill at 11-12 hours of continuous work from fiscal year 2019 to present.
- The remaining production blocker in the July 7 standup was ticket 1186, an intermittent production-only 403 Forbidden proxy error affecting Japan and India since around 2026-06-26.
- `SCR-1197` look-back dashboard direction: keep `latest` as daily overwrite and add `historical` as cumulative daily Parquet snapshots. A true point-in-time view may require a staircase lookup if Hermine needs original as-of behavior rather than archived current forecasts.
- A July 7 pasted note says interconnector backfill remained difficult, month-by-month execution was being considered, `reconcile_capacity_task` was failing after a 13:00 success, and the `SCR-1197` look-back mode showed only actual flow.
- July 7 Codex work added and pushed the `SCR-1197` look-back dashboard prototype and the CDH historical stage registration on `smp-dashboard` `dev`.
- CDH/Athena visibility for the new historical stage was delayed by crawler behavior. A temporary separate-dataset workaround was implemented, then reverted once the original `japan_interconnector_effective_capacity/historical` stage became visible; the stage model remained the chosen clean approach.
- The look-back dashboard was later adjusted locally so `as_of` lists date-only `YYYY-MM-DD` values and capacity lookup selects the latest `reconciled_at_utc` snapshot on or before that date. That JSON needed simple Grafana reimport.
- July 7 reconciliation outage root cause was confirmed in QA: 44 manual backfill daily files landed in the live source prefix `japan_occto_interconnector_capacity/all` around `2026-07-07T05:*Z` and `2026-07-07T06:*Z`, causing current reconciliation to process too much historical daily input.
- Two temporary operational DAGs were added and promoted to QA: `z_japan_occto_capacity_reconciliation_probe_dag` for read-only inventory/metadata diagnostics and `z_japan_occto_capacity_source_quarantine_dag` for dry-run-first copy-verify-delete quarantine.
- Quarantining the 44 suspect daily files reduced daily source files from 482 to 438 and restored `japan_occto_capacity_reconciliation_dag` in QA.
- Durable design direction after recovery: capacity source storage may be append-only/history-bearing, but current effective reconciliation must use a bounded or manifest-based source selection instead of scanning every object in `japan_occto_interconnector_capacity/all`.
- July 8 AWS migration standup said the interconnector dashboard was nearly complete, with remaining detail tickets including ticket 97 for time series view and accepted data exports.
- The same note says the adaptable Y-axis ticket was closed because the user accepted auto-adjusted scale as-is.
- July 9 SMP standup says historical backfill was complete for JPX and capacity from 2019, while actual flow was available only for 2025. Hiromi was investigating the actual-flow download path for FY2019-FY2024.
- July 9 notes say the historical look-back path takes the latest snapshot at 23:30 JST and copies reconciled capacity to a new CDH dataset. It was working in Grafana and waiting for Japan team feedback.
- `SCR-1198` export remained open on July 9. The best case was using existing Grafana export; Excel template complexity was still TBD.
- July 9 proxy notes say Oliver deployed a proxy handler fix around 17:00, no proxy errors appeared after the fix, root cause was an access-control filter using the wrong network mask and destination IP filtering, and the ticket was validated and moved done.
- Some Japan QA DAGs still failed with clean-looking logs. The working theory was memory pressure from parallel backfill runs, requiring Prometheus and namespace memory reservation checks.
- Interconnector TSDB direction on July 9: send reconciled interconnector capacity view to TSDB, four time-series inserts per interconnector, with Carlos consolidating the catalog and IDs expected next sprint.
- July 12 investigation confirmed that scheduled reconciliation could overwrite granular manual-backfill results: the manual raw files were isolated under `backfill/manual`, but the scheduled rebuild omitted that prefix and replaced the stable yearly effective-capacity files.
- The reconciliation contract was hardened in `smp-japan`: manual-backfill files are permanent inputs, live daily data is a bounded overlay, partial runs rebuild affected years from the persisted baseline, and completed-year publication fails closed if daily granularity would regress.
- A full-history QA run exposed memory pressure across reconciliation, validation, and publication. All three paths were changed test-first to stream Parquet data in 32,768-row batches and process one calendar year at a time; the fresh QA reconciliation then completed successfully.
- Effective output is partitioned by the calendar year of `interval_start_jst`, not the source `target_year`, because fiscal-year source files can contain January-March intervals from the following calendar year.
- A July 12 read-only audit found no comparable urgent memory defect in normal scheduled interconnector DAGs. Remaining medium risks were unbounded multi-year JEPX extraction, concurrent branches in the unified history backfill, and four Celery task subprocesses sharing a 4 GiB QA worker pod.
- Hiromi supplied a Bloomberg workbook covering FY2019-FY2024 actual flow for all seven interconnectors. Validation found 729,078 populated half-hour observations, no duplicate timestamps, and missing periods represented by omitted timestamps rather than blank values.
- The approved historical-source design is captured in [[2026-07-13-use-separate-bloomberg-actual-flow-dataset]]: a manual Airflow import reads the unchanged workbook from private S3, publishes a separate Bloomberg CDH dataset, and leaves missing periods blank.
- The main dashboard now combines OCCTO 30-minute averages with Bloomberg 30-minute snapshots under neutral `Actual Flow` labeling. OCCTO wins at overlapping interconnector timestamps; Bloomberg fills older gaps.
- CDH registration for `japan_bloomberg_interconnector_actual_flow/all` succeeded in dev, QA, and production. The `smp-dashboard` changes were pushed to `dev`, and the `smp-japan` importer/DAG was committed, pushed to `dev`, and promoted to QA as `japan_bloomberg_actual_flow_backfill_manual_dag` after Michael uploaded the workbook to all three environment buckets.
- `SCR-1197` was simplified to one visible `As of` dropdown. `Latest` selects the current `_all` table; a date selects `_historical` and resolves the newest snapshot on or before that date. The tested change was committed and pushed to `smp-dashboard` `dev`.
- July 14 Codex work normalized the manual interconnector backfill DAG date parameters: `start_date` and `end_date` now use date-formatted schema values, `end_date` is nullable, and `null` preserves runtime "today in Asia/Tokyo" behavior. The change was committed to `smp-japan` `dev` and promoted through `qa` and `prod`.
- A July 15 clarification says the normalized manual DAG parameter behavior is already up and running.
- Sprint 24 review notes say the dashboard now shows region-specific panels, `Latest` and look-back `As Of` behavior, data backfilled to fiscal year 2019, actual power flow, capacity, minimum capacity, and day-ahead price-difference lines. A stakeholder expected to use the dashboard in an auction early the following week and provide feedback afterward.
- Sprint 25 goals include pushing interconnector data to TSDB. The sprint retro notes say roughly 28 time series are expected, IDs need to be created through GSBK, Carlos and the OCCTO provider owner team should validate metadata changes, and the open design question is whether to submit 5-minute or 30-minute average curves.

## Open Questions

- UNCERTAIN: Whether existing OCT time series can be reused for interconnector data.
- UNCERTAIN: Japan team's final Y-axis requirement still needed confirmation in the July 2 planning notes.
- UNCERTAIN: Whether capacity yearly/monthly/weekly historical rows with missing max values should ever be supported, or whether daily-only historical capacity is sufficient.
- UNCERTAIN: The parent Jira tickets `SCR-1126`, `SCR-1127`, `SCR-1128`, `SCR-1129`, `SCR-1168`, `SCR-1138`, and `SCR-1137` may still need workflow cleanup after an interrupted transition attempt.
- UNCERTAIN: Whether the existing dashboard export feature satisfies the requested accepted data export once the current dashboard is finalized.
- UNCERTAIN: Whether the remaining JEPX and shared-worker concurrency risks need proactive hardening before a large manual run.
- UNCERTAIN: Whether the Bloomberg manual backfill has completed successfully in QA after promotion and workbook upload.
- UNCERTAIN: Whether TSDB should receive 5-minute or 30-minute average interconnector curves.
- UNCERTAIN: Whether dashboard feedback after the early-week auction requires immediate Grafana changes.

## Sources

- `sources/meetings/2026-06-24-1552-granola-backlog-grooming.md`
- `sources/meetings/2026-06-29-1415-granola-standup.md`
- `sources/meetings/2026-07-01-1630-granola-smp-revie.md`
- `sources/meetings/2026-07-02-1500-granola-sprint-planning.md`
- `sources/codex-conversations/2026-07-06-codex-conversations.md`
- `sources/meetings/2026-07-07-1415-granola-standup.md`
- `sources/notes/2026-07-07.md`
- `sources/codex-conversations/2026-07-07-codex-conversations.md`
- `sources/meetings/2026-07-08-1514-granola-aws-migration-standup.md`
- `sources/meetings/2026-07-09-1415-granola-smp-standup.md`
- `sources/notes/2026-07-09.md`
- `sources/codex-conversations/2026-07-09-codex-conversations.md`
- `sources/copilot-conversations/2026-07-09-copilot-conversations.md`
- `sources/codex-conversations/2026-07-12-codex-conversations.md`
- `sources/codex-conversations/2026-07-13-codex-conversations.md`
- `sources/codex-conversations/2026-07-14-codex-conversations.md`
- `sources/notes/2026-07-15-ingest-handover-clarifications.md`
- `sources/meetings/2026-07-15-1500-granola-sprint-retro.md`
- `sources/meetings/2026-07-15-1630-granola-sprint-review.md`

Last Updated: 2026-07-15
