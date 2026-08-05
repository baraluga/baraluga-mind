# DAILY STANDUP

Source type: Granola meeting notes
Meeting ID: `147a1b94-442a-4217-a7f7-489ab208285c`
Meeting date/time: 2026-08-04 14:15 GMT+8
Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves available Granola notes and summaries. It is not a verbatim transcript.

## Discussion Notes / Summary

### Mateo Onboarding Follow-up

- Mateo's questions were mostly on S&P, CDH, Grana, SDB, and Airflow, not the onboarding process itself.
- Busy early in the week but will have more time in the next few days.
- Goal: get his feedback as proof that someone outside the project can understand the flow.

### Gold Layer Discussion

- Francois raised testing the gold layer for generation use case (operational need flagged).
- Brian's view: no meaningful code change on the S&P side, only the read function differs:
  - Standard: `timeseries.read()`
  - Gold layer: `timeseries.readest_version()`
- Writing to TSDB is the same across all layers; gold layer only affects reads.
- Decision: not worth pursuing until there's a real need; Mateo/Adrian's call if generation data needs gold layer access.
- Francois to gather brief documentation on how teams can use the gold layer read function.

### TSDB Backfill Issues (Ticket 4-12-17)

- Last DAG run took 11 hours and failed due to an expired TSDB token.
- Root cause: large data volume (from 2021, per day, every 15-30 minutes) plus sequential API writes.
- Fix in progress: breaking writes into multiple parallel tasks, renewing the token per task.
- Francois suggested splitting backfill by year (2021, 2022, etc.) as separate executions.
- Data is being pushed successfully per logs, but DAG has not yet completed in a successful state.

### Other Updates

- Tickets 10:58 and 2:09: Mateo clarified ideal tag schedule; change already made, follow-up pending.
  - Mateo working from France for the next three weeks.
- Nuclear data validation: functionally working, no visible data change yet (published ~every 6 weeks).
  - Agreed to mark as validated and revisit if issues arise.
- Francois to ping the Iberia team (Bong and Bastion) for updates.
- Francois to follow up with Carlos on metadata (message sent 3-4 days ago, no response).
- Upcoming real use case: predictive models running on S&P comparing TSDB data against actual generation.

## Next Steps / Action Items From Granola

- Follow up with Mateo on tickets 10:58 and 2:09 (Brian Alexander Peralta).
  - Mateo is in France for three weeks; confirm tag schedule changes are acknowledged.
- Rerun the TSDB backfill DAG with parallelized tasks and per-task token renewal (Brian Alexander Peralta).
  - Consider splitting by year (2021, 2022, etc.) to reduce failure risk from token expiry.
- Write gold layer documentation for read access (Francois).
  - Clarify how teams can switch from `timeseries.read()` to `timeseries.readest_version()` for gold layer data.

Last Updated: 2026-08-04
