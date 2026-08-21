# Granola Capture: backlog grooming

- Date: 2026-08-19 15:30 GMT+8
- Meeting ID: `bdc647bd-5216-43aa-bc3a-c914f2a2352b`
- Title: backlog grooming
- Participants: Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>
- Source: Granola

## Summary

# India Workload Overview

- Meeting called to review upcoming India demands ahead of the steering committee on 28th August
- Work expected to start 1st September or first week of September
- Proposal: time and material, two people (Brian + one other), covering 60-80% India demand

# Four Incoming Tickets

- **India scraper (bilateral contracts):** fetch from UX and/or data source, not TSDB-compatible
  - Contract names encode technical info (baseload, peak hours, month, etc.)
  - Need to parse name into structured dataframe, then publish to CDH
  - Main unknown: what is the website/data source?
- **Bid-stack dashboards:** table published every 15 minutes with volume and price (buy/sell) across three markets
  - Three Grafana dashboards needed, one per market
  - Group contracts by price category, push resulting time series to TSDB
  - Japan bid-stack reports as reference/inspiration
- **Generation data benchmarking:** provide infrastructure for model benchmarking against generation data
  - Similar to work done previously for generation
  - Piggybacking on existing Git work; light support expected
- **Data Grid scraper (geolocation-blocked):** fetch generation data by technology (gas, solar, etc.) and push to TSDB
  - Data used downstream by Orchestrate and IDEN (PPA contract pricing tool), so accuracy matters
  - TSDB time series already created; metadata in place
  - Current setup: a local laptop running in India, broken since May, no monitoring
  - Main blocker: VPN/proxy solution to bypass geolocation restriction
  - No Grafana dashboard required; data feeds other processes

# Effort and Capacity Assessment

- Brian's view: four tickets are not epics; two to three sprints for two FTEs feels borderline too much on the happy path
  - Scrapers can go very smoothly or be extremely difficult depending on access/credentials/geolocation
  - Geolocation blocker requires expert escalation (Milo-level), not solved by adding developers
  - Two people is right; three would be wasteful
- Agreed: two people provides enough bandwidth to absorb additional Japan requests or structural work (e.g. Jupiter integration)
- New or large tickets will be negotiated separately if they arise

# Platform Improvements to Propose

- **Grafana alerting:** allow users to set threshold alerts on time series (e.g. price spike, volume anomaly)
  - Infrastructure (email/notification layer) to be set up by the team
  - Users self-configure alert thresholds via Grafana UI
  - Possible India use cases shared in chat (interchange, interconnector spikes)
- **Resource monitoring (Prometheus + Loki):** visualize SMT health, pod usage, and processing load
  - Compatible with Airflow and Grafana; estimated under five days to implement
  - Early warning system before failures; useful for support team and scaling decisions

# Next Steps

- **Attend Monday morning call with Mateo to discuss India ticket details** (Brian)

  Replacing the daily standup slot at 8:15; invite to be forwarded.
- **Start spike on Grafana/Airflow features** (Brian)

  Investigate dataset-based triggering and other features; present findings at Monday standup.
- **Surface geolocation and access blockers early in Sprint 1**

  Milo or Nilo to engage the right people while low-hanging tasks are in progress.

Last Updated: 2026-08-19
