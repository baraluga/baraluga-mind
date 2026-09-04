# Daily Standup

Source: Granola
Meeting ID: `877b5fe3-2758-4cb4-bf36-cdacc9962a2a`
Date: 2026-09-04 14:15 GMT+8
Captured By: Brian Alexander Peralta
Participants:
- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### KAVA Scraper Failure (Dev/QA)

- Dev and QA AWS account lost cross-account access to the KAVA S3 bucket.
- Production is unaffected; the bucket lives on the fraud account and was provisioned by Mateo and Adrian.
- Brian is in contact with Lua Amar from the city about this.
- Root cause is still unknown; Lua is also unclear.
- Plan: disable both KAVA DAGs in QA until resolved.
- Create an OpEx India ticket for this under the maintenance category.

### Ticket Validations Needed

- Chelsea 5-6 (1257) was already pushed to production after a bug was found.
- Adrian is off until next week, so his sign-off was not available.
- Another party agreed to validate this morning.
- Mini POC 1239 (Airflow Assets) is to be validated by Bong, not Brian.
- A Confluence page was created with a high-level guide on standardizing and industrializing across applicable DAGs.
- Brian will ping Bong this week to confirm next steps by next week.

### Airflow Asset-Based Orchestration POC

- Assets offer a more robust orchestration approach than schedule-based orchestrator DAGs.
- Producers define their own schedules; consumers run on asset updates instead of a fixed clock.
- The UI clearly visualizes producer DAGs, assets produced, and consumer DAGs.
- Confirmed: an operator exists to wait for multiple assets before triggering downstream tasks.
- Current Japan/AJKS orchestration runs on a fixed schedule at 9 AM, 1 PM, and 5 PM; assets would eliminate this dependency.
- Feature may have been introduced in a recent Airflow version, coinciding with the UI refresh.
- The meeting agreed this approach should replace the large orchestrator DAG when budget allows.
- Brian will discuss the migration path with Bong next week.

### Bilateral Contracts (India) Scraper

- Working resolution is in Dev and currently being tested.
- Schedule is set to 6 PM India time, but data arrives later in bulk at the end of the market day.
- Plan: push the schedule 1-2 hours later.
- Open question: there is no agreed plan for what to do with the data beyond storing it in CDH.
- There is no TSDB plan because this is not a time series, and no dashboard spec is confirmed.
- Additional request: split the name column into sub-columns to represent trade nature for easier filtering.
- Mateo and Adrian are both off this week, so column structure cannot be confirmed until they return.
- Mateo is expected back around 2026-09-11; Adrian's return is unclear.

### India Grid Data Permissions

- A request to access India grid data through proxy unexpectedly escalated to the head of Singapore infrastructure and power infrastructure.
- Nilo was looped in so Brian is not alone in the discussion.
- No new information yet; this will unblock once permissions are clarified.

## Next Steps Captured

- Disable KAVA DAGs in QA and open an OpEx India maintenance ticket. Owner: Brian.
- Ping Bong on 1239 mini POC validation and next steps. Owner: Brian.
- Confirm bilateral contracts schedule and column split with Mateo and Adrian. Owner: Brian.

Last Updated: 2026-09-05
