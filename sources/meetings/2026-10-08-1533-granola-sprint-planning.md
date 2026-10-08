# Granola Capture: Sprint Planning

Source Type: meeting
Meeting Date: 2026-10-08 15:33 Asia/Manila
Granola URL: https://notes.granola.ai/d/c62e0721-37e4-4d93-95ff-28965b50984d
Granola Meeting ID: c62e0721-37e4-4d93-95ff-28965b50984d
Captured By: Brian Alexander Peralta

## Participants

- Brian Alexander Peralta

## Granola Summary

### Sprint Status and Ticket Points

- Sprint completed earlier that morning.
- Minor nitpicks are expected from Adrian; logic and CDH are in place.
- Tickets pointed at 1 point each due to uncertainty:
  - Original Darwin API ticket: 1 point.
  - Darwin API extension: 1 point.
  - HPX scraping: 1 point, blocked on time series IDs from Adrien.
- Ticket 507 was raised to 3 points because it was underestimated.
  - Artifactory gem unavailability was an issue.
  - Permission fix was resolved by enabling a checkbox in repo settings alongside the correct role ARN.
  - Remaining work: new Docker image commit, Helm upgrade, and pipeline permission checks.
- Ticket 1268 for Darwin collector monitoring is 3 points in the worst case.
  - Best case: existing observability stack covers it, making it 1 point.
  - Jeka, who owns the observability stack, should be consulted later today or Monday.
  - Worst case: build a small web app to monitor Darwin health and error logs.
  - Ticket 1279, monitor script outside Airflow, was confirmed as duplicate of 1268 and deleted.
- Sprint total is 12 points currently and could reach 14-15 if 1284 requires a solution.

### Dashboard Delay Analysis and New Tickets

- New ticket 1284 was added: analyze and reduce dashboard data delay.
  - Traders are unhappy with about 20-minute lag between API and Grafana visibility.
  - Goal: map the full data flow across Airflow, TSDB, CDH, Grafana, and Pathway, and identify where time is lost.
  - Two possible outcomes: optimize what exists, or confirm the architecture cannot go faster.
  - Real-time data was not in original scope; if it is not achievable, that needs to be relayed to end users.
- Ticket 1285 covers process and channel documentation for onboarding Lou.
  - Lou needs to understand which time series come from where.
  - Decision: keep docs close to the code in the repo rather than Confluence.
  - Read-only repo access is expected via Jupyter integration anyway.
  - Starting point is India process documentation; tagged as OPEX.

### Jupyter Integration and Cluster Resources

- Jupyter requirement confirmed: traders need to iterate on DAGs quickly and test functions outside Airflow, including CDH access and mail/OTT functions.
- Nilo should be invited to a follow-up meeting on Monday or Tuesday to align on Jupyter/local volume setup.
  - Nilo was absent from this meeting.
  - His input is needed on non-prod resource allocation.
- Shared cluster constraints were flagged:
  - Resources are shared across all QRM projects.
  - New namespaces should provision tightly.
  - Airflow instances will be smaller and have fewer DAGs.
  - Observability stack will help determine if current resource usage is efficient.
  - A dedicated cluster is possible but expensive; preference is to right-size within the shared cluster.
- Sprint start was agreed.
- Darwin and Grid India tickets are prioritized once unblocked.
- New mid-sprint tasks should be deferred to the next sprint to maintain visibility and avoid rushing.

### Next Steps

- Ping Adrien to unblock HPX scraping ticket.
- Consult Jeka on observability stack coverage for Darwin monitoring.
- Schedule Jupyter/cluster alignment meeting with Nilo.

Last Updated: 2026-10-09
