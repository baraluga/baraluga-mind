# Standup

Source: Granola
Meeting ID: `0c3dbb0f-2dd6-4de3-bdbb-5dafa13cfe43`
Date: 2026-09-14 14:15 GMT+8
Captured by: Brian Alexander Peralta
Participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Grafana Alerting Setup

- Alerting working via manual testing
- Contact point configured in Grafana using terminal email address
- Corporate email used for initial test; SMS also triggered via same setup
- Same namespace as Airflow, reusing Airflow's configuration
- POC chart built: triggers email alert at 10K threshold
- Needs redeploy after reconfiguring in Grafana; Michael involved via Git on Friday
- Alerts set to be consistent with interview/staging environment for now
- User-side configuration: users should be able to set their own alerts (per "them")

### Scraper and Proxy Solution

- VPN raised as access method if scraper is used
- Proxy solution needed, especially for India (no scraper yet)
- Singapore has a tagging solution; Adrian should be looped in
- Singapore IT or Indian IT to handle within SMP
- Scraper can be run locally for testing
- Benjamin script mentioned as one of the acceptance criteria
- Proxy solution must work for India as well as Singapore

### Cobweb Sweeper / Freshness Check

- Freshness monitoring via cobweb sweeper, running every 15 minutes
- Straightforward brute-force option: check every 5 minutes
- More graceful, real-time approach also considered
- Ticket raised at 12:59, 1 point, timing acceptable
- Gaps bug previously observed; Grafana monitoring shows no gaps now
- Continuing to monitor

### Next Steps

- Coordinate with Michael on Grafana redeploy
  - Reconfiguration requires a redeploy; Michael flagged via Git, targeting Friday.
- Loop in Adrian on proxy solution for Singapore/India
  - Adrian's involvement needed to unblock IS proxy setup so both regions are covered.
- Continue monitoring Grafana for gaps bug
  - No gaps currently showing; keep under observation to confirm fix holds.

Last Updated: 2026-09-15
