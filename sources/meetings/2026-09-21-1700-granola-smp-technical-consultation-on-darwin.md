# Granola Capture: SMP Technical Consultation on Darwin

- Date: 2026-09-21 17:00 GMT+8
- Source: Granola
- Meeting ID: `ddbcf1be-0a26-4578-88d0-0b7afffc30ba`
- Title: SMP Technical Consultation on Darwin
- Known participants:
  - Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

# India Geo-Restriction: SMP Cluster Access

- Target website is geo-locked to India; SMP cluster exits via Singapore, blocking access
- Zscaler fix works on personal machines but not at cluster level
- France/Belgium IT confirmed no India infrastructure and no clear budget path
  - Legal blockers too, not just technical ones
- India VPCs reportedly blocked in the current AWS account
- External proxy not viable without NG approval (logging and data protection requirements)
- Japan scraping worked previously because Singapore IP wasn't blocked there

# Escalation Path

- Consensus to escalate to Frederik
  - Nilo has already spoken with Olivier and the network team; both confirmed no solution available
  - Nilo will explain the technical context; Frederik to engage Alexander if needed
- Michael to set up the call with Frederik directly (faster given existing meeting cadence)

# Real-Time Data Scraping: Darwin API

- India team (Mateo) has a Darwin endpoint returning a new value every minute
- Airflow not ideal for guaranteed per-minute execution
  - Batch/DAG scheduling is best-effort, not deterministic at 1-minute intervals
  - Error handling every minute (stop vs. retry) also unresolved
- Recommended approach: independent Python service deployed as a Kubernetes pod
  - Runs in a loop, writes to TSDB; Airflow DAGs access collected data via standard reads
  - Pod designed to fail fast so Kubernetes auto-restarts on another node
  - Resilient to Airflow downtime
- Open question: whether historical/previous-minute values can be recovered from the API
- Kubernetes redeploy risk: two instances may run simultaneously; needs cooperative design

# Monitoring and Prometheus Integration

- Prometheus already running in the cluster; Grafana dashboards active for namespace metrics
- Synapse team building full Prometheus/alerting integration, targeting production release in 1-2 weeks
- Recommendation: wait 1-2 weeks before developing monitoring for the new pod
  - SMP (AWS cluster) should be covered; Nilo to double-check deployment across clusters
- Jeka (Philippines) currently owns monitoring responsibilities for SMP
- Airflow version: team recently updated; Nilo noted they're on a newer version than 3.1.7, should be compatible

# JupyterLab Integration (Next Session)

- Planned for end of October; will be discussed in a future session
- Likely simpler than Synapse integration (no change control overhead)
- Nilo to receive a user story outlining desired functionality before the session
- Eric to be invited: most up-to-date on Jupyter integration

# Next Steps

- **Set up call with Frederik to escalate India proxy issue** (Michael)

  Nilo has full technical context and can answer questions; Frederik to engage Alexander if needed.
- **Build and test independent Python scraping service for Darwin API**

  Deploy as a Kubernetes pod; defer monitoring integration until Synapse tooling is ready in 1-2 weeks.
- **Prepare JupyterLab user story for Nilo ahead of next session**

  Session targeting end of October; invite Eric as he leads Jupyter integration.

Last Updated: 2026-09-22
