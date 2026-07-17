# Daily Standup

Source type: Granola meeting notes
Meeting ID: `e0d1c88d-b2f2-4ce3-8869-df60f683983a`
Meeting date/time: Jul 17, 2026 2:15 PM GMT+8
Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This is not a verbatim transcript. It preserves the available Granola-generated meeting notes and summary.

## Discussion Notes / Summary

### SCR-101: Aurora CLI Backwards Compatibility Fix

- Ticket added to address CLI backwards compatibility issue reported by Mateo.
- Root cause: latest Aurora files changed a specific tab name the CLI relied on.
- Fix: updated logic to interpret file structure instead of hardcoding tab names.
- Also included refactoring to make the CLI more resilient.
- UAT confirmed by Mateo; currently running in prod.
  - No explicit prod confirmation yet, but UAT considered sufficient for acceptance criteria.
- Ticket closed at 2 points.

### Ticket 1202: Look-Back Function for Japan 2i Dashboard

- Adding look-back functionality (previously built for Interconnector dashboard) to Japan 2i.
- Rated 3 points due to scope of files touched, not complexity.
- Strategy: set up underlying schema, parquet, and dashboard infrastructure now.
  - Look-back data will be ready by default, but hidden (opt-in per dashboard).
  - Future dashboards (e.g. Bid Stack) will only need dashboard updates, not DAG/CDH changes.
- Performance concern raised: no expected impact on load times.
  - Based on IC dashboard experience, load time depends on time period selected, not look-back itself.

### Ticket 1197: Bloomberg Backfill Data Missing in Prod

- Bloomberg actual flow backfill table still missing in production.
- Data visible in CDH prod (row-level preview confirmed), but lost somewhere between CDH and Grafana.
- CDH support ticket raised; call pending.
- Action: document findings for the team and end users once resolved (they'll likely hit the same issue with new DAGs).

### TSDB / Ticket 1171 and Weekend Plans

- TSDB changes pushed for catalog approval; awaiting sign-off from Carlos (reached out ~4-5 hours ago, no reply).
- Identified Laurent (octo provider owner) as fallback contact if Carlos doesn't respond by end of day.
- Once catalog approved, time series will be created and data push can proceed.
- Focus for remainder of sprint: 1197 (prod stabilization) and continuing work on ticket 1202.
- Team update: Iberia SMP meeting postponed to next week; UK meeting scheduled for today (first contact, no decisions expected).

## Next Steps / Action Items Present in Granola

- Document Bloomberg backfill investigation findings (Brian).
  - CDH support call pending; document outcome for team and end users before new DAGs go live.
- Escalate TSDB approval to Laurent if no reply from Carlos by EOD (Brian).
  - TSDB data push is blocked until catalog changes are approved.
- Verify Interconnector dashboard fix environment.
  - Confirm which environment the recent fix was deployed to so it can be reviewed.

Last Updated: 2026-07-17
