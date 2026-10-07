# Granola Capture: Sprint Review

Source Type: meeting
Meeting Date: 2026-10-07 16:30 Asia/Manila
Granola URL: https://notes.granola.ai/d/623a702c-7d05-44d8-83fe-8e9edd747873
Granola Meeting ID: 623a702c-7d05-44d8-83fe-8e9edd747873
Captured By: Brian Alexander Peralta

## Participants

- Brian Alexander Peralta

## Granola Summary

### Sprint 3 Summary

- Legacy scraper fixed; Bitstack data pushed to TSDB.
- India geomap dashboard built in Grafana by Brian.
  - Shows real-time market price and volume by region.
  - Supports max/min/average views, current slot, and data freshness indicator.
  - Initial Plotly prototype replaced by cleaner Grafana geomap.
- Bilateral contract dashboard built.
  - Table view of all bilateral contracts with region/code legend.
  - Freshness and anomaly indicators included.
  - Pending validation.
- Grafana alerting tested: Teams channel notifications work natively, no extra setup needed.
  - Brian wrote documentation on setup.
- Japan: small backfill and bug fix for interconnector data.

### Blockers

- Darwin connection: Airflow needs access to Darwin API at the right version.
  - IT tickets are in progress, slow but under control.
  - Once resolved, data push to TSDB is technically ready.
- Grid India: blocked on legal approval for VPN/scraping access.
  - Frédéric is chasing legal via Rashid for official green light.
  - Green India approval is needed first; WBS portal approval is a separate process.
  - If email is received today, it will be shared with François, Pong, Frédéric, Brian, Michael, and the full SMP team.

### Budget Status

- Total budget: approximately EUR 45,000 for this period, with an India-weighted split with Japan.
- Spent approximately 60% after 1.5 to 2 months; projected to close at approximately 80%.
- Approximately 20% surplus expected; 40% technically remaining.
- Last period went over budget; this period is being monitored to avoid repeat.
- Urgent scope can still be accommodated; otherwise normal development flow continues.

### Next Period Priorities

- Darwin data fetch once access is resolved: high-value, well-anticipated data.
- Jupyter integration: technical solution needs to be defined before implementation.
- Docker image push automation: to ease deployment pipeline.
- Observability stack: monitor computational resource usage.
- Support for Lou's onboarding and knowledge transfer.
- Matteo's dashboard support, currently on hold while he is on leave.
- Time series for HPX Scraper to be created in UAT and production, planned post-call.

### Steering Committee and Upcoming Events

- Demo on Friday: broader SMP future to be presented; full team attendance requested, especially Jayant.
- Steering committee next week Thursday: defines topics for the next 2-month period.
  - Tasks need enough detail to size effort and team, not full operational tickets.
  - Team to prepare topic list by Monday's meeting.
  - Monday meeting: review long-term plan and incorporate into steering committee slide.
  - Matteo to contribute if available; Jayant and Lou to be included in prep session tomorrow.
- Survey questions to be prepared and shared via Microsoft Forms before Friday.

### Next Steps

- Create HPX Scraper time series in UAT and production.
  - Matteo assigned this; planned for immediately after the call, with Lou.
- Share Grid India legal approval email when received.
  - Distribute to François, Pong, Frédéric, Brian, Michael, and full SMP team; then immediately request WBS portal approval.
- Prepare steering committee topic list by Monday.
  - Discuss with Jayant and Lou tomorrow; align with Matteo's input for the Thursday steering committee slide.

Last Updated: 2026-10-08
