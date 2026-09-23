# Granola: SMP Sprint Review

Date: 2026-09-23 16:30 GMT+8
Source: Granola
Granola URL: https://notes.granola.ai/d/9169e1ae-270e-4da5-8ea9-e08ccf98a401
Meeting ID: 9169e1ae-270e-4da5-8ea9-e08ccf98a401

## Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Sprint Review: SMB India Progress

- Market coverage broadened in asset monitoring.
- Bilateral contracts data collection has started and is currently in CDH.
- Decision on CSDB push and visualization is still pending.
- IEX RTM data collection gaps were identified and resolved; refinement is ongoing.
- Bitstack curves data collection is live, with dashboard tweaking in progress.
- Kavda was added as a monitored RNF asset alongside Kaba in Grafana.

### Grafana Email Alerts

- A proof-of-concept alert was built for IEX and triggers when RTM price crosses 10,000.
- Francois confirmed the alerting feature works by creating his own alert.
- The feature is live in QA and expected to roll out to production in the coming days.
- Documentation has been prepared and will be shared once production rollout is complete.
- Teams notification through email-to-mailbox is feasible.
- Frederic confirmed Airflow already uses email-to-mailbox for DAG errors.
- Mateo wants to explore email-to-mailbox notifications for traders, not just internal use.
- The team plans to explore this as a simple addition in the next sprint.

### Budget Status

- Period 3 budget is 38% consumed at the 50% mark, which is 12% under budget.
- The prior period ran 18% over budget, so this period partially compensates.
- Main risk: India index access for S&P.
- Fred will escalate the India index access infrastructure issue to the IS team in Europe.
- Darwin every-minute solution is already in place.
- Remaining activities are considered low risk.

### Next Sprint Priorities

- Japan: small bug fixes and robustification to prevent recurring incidents.
- India: publish EOX Bitstack to TSDB, pending time series ID.
- India: prioritize Tutikarin live data and other sites.
- India: align UAT vs. production dashboard and TSDB after access rights are fixed.
- India: assess sizing and workload for the legacy scraper fix.
- Common team: continue exploring native Grafana and Airflow capabilities.
- Common team: automate Docker image build and push to improve deployment.
- Common team: work on an observability stack to monitor cluster resource usage.
- Common team: plan Jupyter integration, including specification and architecture definition.
- Goal: enable Mateo's team to create DAGs with minimal developer input.

### Upcoming and Team Updates

- Steering committee is scheduled for mid-October, just before the end of the last sprint of the period.
- New stakeholders will be involved: one for Japan and one for India.
- An SMB India demo is planned.
- A new French VAE is joining the India team in about two weeks.
- Mateo plans to hand off SMB work to the new VAE.

## Next Steps

- Roll out Grafana email alerts to production and share documentation.
- Explore Teams notifications through email-to-mailbox for Grafana alerts.
- Mateo will discuss with traders to confirm the need before implementation.
- Fred will escalate the India index access issue to the IS team in Europe.

Last Updated: 2026-09-24
