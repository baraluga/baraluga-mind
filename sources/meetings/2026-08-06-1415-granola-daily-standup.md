# daily standup

Source type: Granola meeting notes
Meeting ID: `7fd674aa-d6bc-4f48-be04-783ad2e7f6f7`
Meeting date/time: Aug 6, 2026 2:15 PM GMT+8

## Known Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Note

This capture preserves available Granola notes and summaries. It is not a verbatim transcript.

## Granola Summary

# Ticket 25 (Generation Kaaba)

- Set to done; explicit confirmations requested
- Francois's comment addressed: Mateo won't hit the described issue due to separate GitHub groups
- Artifactory workaround already communicated to Mateo on the 2/9 call

# Ticket 9 (TSDB Publishing)

- QA confirmed; same time series visible in prod TSDB via UI
- Two DAGs merged to production:
  - Real-time: every 10 minutes
  - Reconciliation: ~2:30 IST
- Access issue still pending: can't personally verify data reads
- Pending Mateo's confirmation on his TSDB prod side before closing

# Ticket 12-17 (Actual Flow Backfill)

- Backfill for full FY2025 took 15 hours
  - 366 days x ~2 min/Octo request = ~700 requests, roughly matching elapsed time
- Ongoing run covers May 3 to June 8 (data exists from June 8 onward)
- Can't set to validation yet; backfill still running
- Question raised: can QA data be copied directly to prod to avoid re-scraping Octo?
  - Previously attempted but not completed; reason unclear
  - Risk: Octo may detect duplicate scraping (web scraping occupational hazard)
  - Worst case: wait for DAGs to finish, same seamless process used for available capacity
- Mateo to be reminded: alternative process available, data pushing to prod, and good time to build a DAG for generation data in the dashboard

# Ticket 12-15 (Operational Capacity to TSDB)

- Pulled in alongside 12-17; same process as before
- Story point estimate: 3 (torn between 3 and 5, settled on 3 given effort level)
- Process: SDK request, spreadsheet creation, email to Carlos, then activate Airflow and wait for backfill
- Metadata collection work noted: inventory existing data, check for duplicates, create remaining TS and inject; Louis may handle portions

# Next Steps

- **Confirm with Mateo that TSDB prod is healthy (Brian)**

  Once positive feedback received, ticket 9 can be closed.
- **Check feasibility of copying QA backfill data directly to prod**

  Avoids re-scraping Octo; investigate why this was previously abandoned.
- **Send budget extension follow-up email**

  No response yet; escalate at next sprint review if needed.

Last Updated: 2026-08-06
