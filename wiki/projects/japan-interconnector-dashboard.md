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
- July 16 notes confirmed Grafana has a native CSV export path for displayed dashboard data. Brian drafted a short message to Hiromi asking whether that satisfies the current export need or whether a formatted Excel workbook is still required.
- July 16 HJKS investigation found intermittent `japan_get_hjks_final_dag` failures around CSRF refresh after Selenium search submission. A scheduled `japan_get_hjks_final_shadow_dag` was created and pushed to test 26 serialized retryable windows before retiring the current mega-orchestrator.
- July 16 actual-flow/capacity investigation clarified that the dashboard's blue/orange `Available` series is OCCTO residual available capacity, not the physical operating capacity. Actual flow can exceed residual available capacity without proving a physical capacity breach. The dashboard label should be clarified, and a true breach check requires comparing actual flow with directional operating capacity.
- July 16 QA investigation found `SCR-1197` capacity provenance was stale because the effective curve selected weekly capacity after the daily source fell out of the live window. A completed-day capacity DAG was added at 00:30 JST to persist yesterday's revised `D` capacity into the immutable prefix, trigger reconciliation, and prevent daily-to-weekly regression.
- July 16 production Bloomberg actual-flow registration exposed a CDH false positive: the workflow accepted schema detection but did not prove Athena table creation. The production Glue crawler `cdh_smpdatasourceprd_japan_bloomberg_interconnector_actual_flow_49` remained stuck in `RUNNING`, so `japan_bloomberg_interconnector_actual_flow_all` was still missing from Athena. A temporary OCCTO-only dashboard JSON was prepared but intentionally not imported because production users were still on QA.
- July 16 TSDB POC work for `SCR-1171` split the target into 35 series: 14 directional available-capacity series, 14 directional minimum-capacity series, and 7 signed actual-flow series. Capacity publication should use positive directional values at the TSDB boundary, while actual flow keeps signed five-minute values. The first UAT POC created five Hokkaido/Tohoku `TimeseriesChange` records and identified `zs5929` as the best single approver for both `smp_interconnector_recon` model metadata and the OCCTO time-series changes.
- July 17 standup notes say the production Bloomberg actual-flow backfill table was still missing from Grafana even though row-level preview was visible in CDH prod. A CDH support ticket had been raised and a support call was pending; the remaining work is to understand the CDH-to-Grafana/Athena gap and document findings for the team and future DAG users.
- `SCR-1202` added an opt-in HJKS 2Y dashboard look-back pattern. The implemented design records scheduled snapshots with explicit metadata, publishes a snapshot manifest only when all nine dashboard regions complete, and exposes complete scheduled snapshots in the `As of` selector as soon as their manifest is queryable. Manual and incomplete runs remain excluded, `Latest` remains default, and no pre-deployment backfill is required.
- `SCR-1202` was implemented across `smp-common`, `smp-tool`, `smp-japan`, and `smp-dashboard`: `smp-common 0.4.4` was published, `smp-tool` was pushed to `dev`, Japan changes were merged and promoted through QA, and dashboard changes were pushed directly to `dev` then promoted to QA. The remaining source-backed validation item is a real scheduled Airflow snapshot before production rollout.
- July 17 standup notes also say the TSDB catalog approval for `SCR-1171` was waiting on Carlos, with Laurent identified as fallback if Carlos did not respond by end of day. This appears related to the existing TSDB UAT approval wait rather than a separate design decision.
- July 20 standup says `SCR-1171` was still waiting on Carlos's approval of the spreadsheet listing expected TSDB catalog changes and time-series IDs. The proposed path was for Carlos to approve and contact Laurent to execute the TSDB changes; Brian planned email/DM follow-up if there was no response by end of day.
- July 20 standup says `SCR-1197` was set to validation, production was confirmed stable, all interconnector docs were enabled, and 2019-2025 fiscal-year data had been backfilled for capacity, JPX prices, and actual flow from Bloomberg and OCCTO.
- July 20 standup says `SCR-1202` HJKS 2Y look-back was in review. It was functionally done the prior Friday but needed enough weekend data to display. The same day's manual note marks the action to ask Japan to check the 2Y look-back feature as done.
- July 24 standup records `SCR-1202` as done after Francois confirmed in the Japan group chat that the 2Y dashboard looked correct. Operational follow-ups are outside that ticket's scope.
- A July 23 investigation proved that the reported zero Tohoku-to-Tokyo capacity at 2026-07-22 15:00 JST came directly from OCCTO's `空容量`, or remaining available capacity. OCCTO reported 5,250 MW operating capacity, 5,090 MW planned flow, 160 MW margin, and therefore zero remaining capacity while actual flow averaged 5,083 MW. The scraper JSON and OCCTO's downloadable revised same-day CSV matched on all 672 business rows.
- Hiromi's original epic deck exposed the product-level distinction: its delivered-period example treated `運用容量`, or operating capacity, as availability. The source pipeline was faithfully showing `空容量`, but the dashboard requirement also needed operating capacity.
- `SCR-1206` added operating capacity to the four live OCCTO parsers, reconciliation, CDH schemas, and all seven interconnector panels. The canonical dashboard shows two subtle neutral-grey dotted operating-capacity lines, one per direction, while retaining the existing available-capacity styling.
- The implementation was pushed to `smp-japan` dev and `smp-dashboard` main on July 23, then `smp-japan` was promoted to QA at `edb8f2d`. July 24 standup says dev validation passed and QA testing of yearly, monthly, weekly, daily, and Grafana mapping was still ongoing.
- `SCR-1207` is the separate two-point historical operating-capacity backfill. It must follow `SCR-1206`; historical records remain null for operating capacity until the backfill is run.
- July 24 Codex work implemented an event-driven TSDB capacity publisher and forecast-version conflict probe. Brian confirmed on July 27 that this work was subsequently landed and is operating correctly.
- July 27 standup confirms the `SCR-1197` interconnector dashboard was live in production and treated as fully released. Hiromi was redirected from the old QA link to the production dashboard; future additions should still pass through QA before production.
- `SCR-1206` operating capacity remained in QA. The feature worked, but historical persistence was wrong: the visible start date moved forward with time instead of carrying the last known capacity across missing days. Graph styling feedback also suggested making the non-price series more visible before stakeholder demos.
- `SCR-1207` added a guarded single-run QA workflow for historical operating-capacity backfill. The first run exposed a legitimate forward-year case because OCCTO target year 2026 extends through March 2027; the workflow was fixed to snapshot and compare that outside-range year, promoted to QA, and left ready for recovery by clearing only the commit task in the same run.
- `SCR-1208` applied the established snapshot-manifest pattern to the Japan nuclear dashboard. The producer and dashboard changes were merged and promoted to QA; CDH registration and one scheduled run proved the selector and snapshot plumbing.
- QA exposed a historical-horizon defect in `SCR-1208`: filtering only to the selected snapshot dropped pre-snapshot legacy data. The dashboard query was corrected to combine unversioned legacy rows with the selected snapshot and prefer selected rows on overlap. Selection and the full 2016-2028 horizon were then validated; a second scheduled run is still required to prove that the look-back preserves an older forecast while `Latest` advances.
- `SCR-1171` gained production-safe versions of the existing catalogue provisioning, approver discovery, and smoke-test commands. Production mutations remain dry-run by default and require both `--apply` and the exact `CONFIRM PROD` guard. The code was pushed to `dev` with green CI, but production catalogue approvals and VPN-side execution remain separate work.
- The July 27 standup described `SCR-1171` as waiting on `Franco`; Brian confirmed on July 29 that this means [[francois]].
- The July 29 sprint review records the three Japan look-back dashboards as delivered and accepted, with one to three historical snapshots per day depending on the dashboard.
- The interconnector dashboard now shows operating capacity alongside available capacity, actual flow, and EEX/JPX prices. Dashboard data was backfilled to 2019. Japan trading specialists are still providing feedback on the business interpretation.
- The project is expected to exceed its original budget because look-back work and other requests were added to scope. The July 29 retro chose to continue Brian at full capacity through August unless the client rejects the projected overshoot.
- The next proposed Japan data item is Aurora curves. Carlos said he would check whether the data exists in an API; otherwise the proposed fallback is the Excel-based approach already used for India.
- `SCR-1216` removed selected HJKS report-email tasks while preserving processing and upload paths. The change reached QA with green CI; a post-deployment nuclear DAG run proved the email tasks absent and the upload path successful. The two remaining HJKS DAGs and production mailbox behavior still need acceptance checks.
- `SCR-1219` traced the weekly-capacity failure to a month-boundary selector regression: OCCTO indexes weekly revised data by the Thursday publication date, while SMP calculated month/week from the Saturday target start. For the 2026-08-01 week, July/week 5 returned all 4,704 rows while August/week 1 returned `YA000010SW`. The boundary fix, including year-boundary coverage, was promoted to QA.
- The July 31 daily standup reported `SCR-1216` behaving as intended in repeated QA monitoring, with the selected HJKS report types no longer sending email while processing continued. Final clean-run and production acceptance were still pending.
- The same standup reported `SCR-1219` ready for validation once weekly-capacity runs were confirmed green in QA and production. Brian later confirmed that the source's `Ticket 417` historical-backfill discussion belongs to `SCR-1217`, and that its `Octo` references mean OCCTO. The source records a simplified scope using OCCTO through fiscal 2025, with Bloomberg needed for fiscal 2024 onward under a different TSDB setup.
- `SCR-1207` production backfill exposed that current OCCTO files revise existing Available Capacity as well as add Operating Capacity. The repair policy was changed so current OCCTO values are authoritative inside the selected repair range while outside-range history remains unchanged; the change was promoted through production and the failed run's prepared artifacts remained reusable.
- The shared `smp-common 0.6.0` OCCTO publisher and bounded historical TSDB campaign were combined in draft PR 21. The agreed default scope is capacity from 2021-01-01 and actual flow from 2025-04-01 through the latest completed JST day, with capacity serialized before actual flow and `write=false` by default.
- A UAT backfill write completed successfully, with per-chunk TSDB read-back and an independent Japan source-versus-TSDB audit. The preferred exhaustive confirmation is rerunning the exact resolved range with `write=false` and requiring zero would-write rows; a one-day all-series check should report 3,360 unchanged points.
- Rodrigue asked for validation of `interconnection, available capacity` and `interconnection, available capacity, minimum`; Alexandre Huynen subsequently confirmed that both variable groups should remain unchanged, including the `interconnection` qualifier. The remaining work is the ordinary production approval path for the 35 series, not a taxonomy redesign.
- On August 3, `SCR-1217` was moved to In Review after Carlos confirmed the bounded TSDB campaign shape: capacity starts from FY2021 while actual flow starts from FY2025.
- On August 4, the 2Y and nuclear dashboard production missing-table errors were traced to absent production `*_snapshot_manifest` Athena tables, not to missing DAG promotion. The producer code and a compatible Airflow image had reached production on July 30, while production CDH registration evidence was missing.
- The scoped nuclear history fix from QA, commit `3d205df`, was cherry-picked to `smp-dashboard/main` as `659995d`; the stale feature branch was then deleted. This fix prevents historical nuclear snapshot selection from dropping the older 2016-mid-2026 legacy horizon.
- Production CDH registrations for `hjks_2y_status` and `hjks_nuclear_by_region` later succeeded after the GitHub Tools credential used to install private `cdh-sdk` was renewed. The submitted crawler job IDs were `ca11da69-a242-4faa-96a9-34f93d5f623b` and `ccd17c6e-f297-4601-809a-44b032362c6e`.
- Brian later confirmed in CDH that successful production registration did not automatically refresh the affected stages; he had to refresh them manually. The likely difference from QA is the newer registration manager behavior that submits crawler work and exits green without waiting for every stage refresh to complete.
- August 11 standup notes framed the sprint-review message for Japan as TSDB push for spatial capacity and port activation, with operational-capacity metadata validation still waiting on Carlos and old Louis-dashboard metadata still pending.
- For the next engagement period, the source split Japan next steps by budget: support mode means no proactive next steps; full budget would push old operational-capacity data to TSDB. The team also wanted Japan stakeholders to surface future needs because next-period visibility was low.
- August 11 backlog grooming described the new interconnector metadata ticket as blocked, with old-dashboard time-series tickets waiting on Louis's team to push to TSDB. The practical unblock path is to check whether providers already exist, identify provider owners, and schedule injection so dashboards are not disrupted.

## Open Questions

- UNCERTAIN: Whether existing OCT time series can be reused for interconnector data.
- UNCERTAIN: Japan team's final Y-axis requirement still needed confirmation in the July 2 planning notes.
- UNCERTAIN: Whether capacity yearly/monthly/weekly historical rows with missing max values should ever be supported, or whether daily-only historical capacity is sufficient.
- UNCERTAIN: The parent Jira tickets `SCR-1126`, `SCR-1127`, `SCR-1128`, `SCR-1129`, `SCR-1168`, `SCR-1138`, and `SCR-1137` may still need workflow cleanup after an interrupted transition attempt.
- UNCERTAIN: Whether the existing dashboard export feature satisfies the requested accepted data export once the current dashboard is finalized.
- UNCERTAIN: Whether the remaining JEPX and shared-worker concurrency risks need proactive hardening before a large manual run.
- UNCERTAIN: Whether the Bloomberg manual backfill has completed successfully in QA after promotion and workbook upload.
- UNCERTAIN: Whether CDH support can reset the stuck production Bloomberg crawler before the July 17 EOD Manila timebox.
- UNCERTAIN: Whether the temporary OCCTO-only dashboard, manual Athena table, or recovery-dataset fallback will be needed if CDH support is silent.
- UNCERTAIN: Whether `zs5929` can approve both the `smp_interconnector_recon` model metadata and the five OCCTO UAT `TimeseriesChange` records without additional TSDB administrators.
- UNCERTAIN: Whether dashboard feedback after the early-week auction requires immediate Grafana changes.
- UNCERTAIN: Whether Carlos, Laurent, or `zs5929` is the current approval path for all `SCR-1171` TSDB catalog changes; the July 17 standup and July 16 Codex evidence name different approval routes.
- UNCERTAIN: Whether Carlos's July 20 spreadsheet approval covers the same TSDB objects as the earlier `zs5929` approval path or a broader catalog-change package.
- UNCERTAIN: Who approves production TSDB changes after UAT validation; the July 24 standup says the current contact manages only UAT.
- UNCERTAIN: Whether the completed UAT campaign has since received an exact-range `write=false` rerun proving zero would-write rows across all source-complete chunks.
- UNCERTAIN: Whether the production CDH registration workflow should block until each requested stage refresh has completed, or at least surface crawler-already-running outcomes as an explicit follow-up.
- UNCERTAIN: Whether `port activation` in the August 11 standup is the exact TSDB/Japan term.

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
- `sources/codex-conversations/2026-07-16-codex-conversations.md`
- `sources/notes/2026-07-16.md`
- `sources/codex-conversations/2026-07-17-codex-conversations.md`
- `sources/meetings/2026-07-17-1415-granola-daily-standup.md`
- `sources/notes/2026-07-17.md`
- `sources/meetings/2026-07-20-1415-granola-standup.md`
- `sources/notes/2026-07-20.md`
- `sources/codex-conversations/2026-07-23-codex-conversations.md`
- `sources/codex-conversations/2026-07-24-codex-conversations.md`
- `sources/meetings/2026-07-24-1415-granola-daily-standup.md`
- `sources/notes/2026-07-27-ingest-handover-clarifications.md`
- `sources/meetings/2026-07-27-1415-granola-daily-standup.md`
- `sources/codex-conversations/2026-07-27-codex-conversations.md`
- `sources/codex-conversations/2026-07-28-codex-conversations.md`
- `sources/notes/2026-07-29-ingest-handover-clarifications.md`
- `sources/codex-conversations/2026-07-29-codex-conversations.md`
- `sources/meetings/2026-07-29-1500-granola-sprint-retro.md`
- `sources/meetings/2026-07-29-1630-granola-sprint-review.md`
- `sources/notes/2026-07-30-ingest-handover-clarifications.md`
- `sources/meetings/2026-07-30-1500-granola-sprint-planning.md`
- `sources/notes/2026-07-30.md`
- `sources/codex-conversations/2026-07-30-codex-conversations.md`
- `sources/codex-conversations/2026-07-31-codex-conversations.md`
- `sources/meetings/2026-07-31-1415-granola-daily-standup.md`
- `sources/notes/2026-07-31-ingest-handover-clarifications.md`
- `sources/notes/2026-08-03-ingest-handover-clarifications.md`
- `sources/codex-conversations/2026-08-03-codex-conversations.txt`
- `sources/codex-conversations/2026-08-04-codex-conversations.txt`
- `sources/meetings/2026-08-11-1415-granola-daily-standup.md`
- `sources/meetings/2026-08-11-1430-granola-backlog-grooming.md`

Last Updated: 2026-08-11
