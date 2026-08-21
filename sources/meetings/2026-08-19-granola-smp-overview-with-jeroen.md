# Granola Capture: SMP Overview with Jeroen

- Date: 2026-08-19 14:45 GMT+8
- Meeting ID: `e7823df1-bca9-4f45-9ecd-0c3bf763005d`
- Title: SMP Overview with Jeroen
- Participants: Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>
- Source: Granola

## Summary

# SMP Project Overview

- Scraper and Model Platform (SMP): originated from a Japan trading desk request to automate Python scripts running on a VM
  - Scripts scraped external sources and sent email reports; original developer left, triggering the rebuild
  - Team adopted open-source energy data ecosystem tools: Airflow for scheduling, Grafana for dashboards
- Two end clients: Japan team and India team, each isolated in their own environment
  - Single codebase deployed to two separate namespaces; teams are unaware of each other day-to-day
- Data flow: scraper DAGs collect data, transformation DAGs prep for Grafana, output published to CDH or TSDB
  - CDH (Common Data Hub): primary store; parquet files uploaded to S3, bound to CDH, accessed by Grafana via Athena
  - TSDB: time-series database; recently extended to receive parallel pushes from India pipelines
  - Grafana-to-TSDB direct connection not yet available; CDH remains the current bridge
- Governance: two-week sprints, formal stakeholder review every two months ("Peralta" cadence)

# Infrastructure Setup

- Airflow deployed on AWS EKS, managed via Helm; separate URLs per region (Japan/India)
  - Core pods: web server, scheduler, workers (Celery), triggerer, Git-sync sidecar
  - Git-sync auto-imports DAGs from GitHub on merge; no direct pushes to branches
  - Metadata DB migrated from local PostgreSQL to AWS RDS
- Custom Docker images stored in AWS ECR
  - Built and pushed manually; no CI/CD pipeline yet
  - No automated image rebuild policy for security patches; flagged as a gap during the meeting
  - No auditing tool implemented for image vulnerabilities
- External services in use:
  - SMTP via [infrasinfrasy.com](http://infrasinfrasy.com) for email alerts
  - Singapore proxy to bypass geo-blocks on certain data sources
  - MS SharePoint for some DAG output storage
  - MS Teams alerts via SMTP on DAG failure
- Environments: dev and QA per region in shared cluster; prod runs on a separate dedicated cluster

# DAG Development Workflow and AI Scaffolding

- Five repositories: SMP India, SMP Japan, SMP Common (shared), SMP Infra, SMP Dashboard (Grafana JSON exports)
- DAG lifecycle: scrape -> transform -> optional reconciliation -> publish (CDH or TSDB)
- AI DAG scaffolding agent (live ~1 month, first test July)
  - Triggered via GitHub issue using a structured template (name, description, schedule, tags)
  - Agent reads the current codebase to scaffold best-practice files and opens a PR automatically
  - Beta tester (Mateo/Matthew) currently blocked on local testing due to missing dependencies
  - No production DAGs created via this path yet; still in pilot phase
- Promotion path: PR -> dev (auto-synced via Git-sync) -> QA -> prod
  - Trunk-based development preferred; feature branches only for contributor onboarding
  - Branch protection on dev, QA, and prod: merge only, requires approval from a core member (Brian or Michael)
  - CI checks: linter (Ruff), pytest, test coverage threshold, documentation coherence check
  - Coverage threshold currently updated manually; idea raised to automate via a scheduled GitHub Copilot agent

# Next Steps

- **Define image rebuild and security patching policy**

  No current policy for updating Docker images on security grounds; flagged during infra review alongside known vulnerabilities.
- **Unblock Mateo on local DAG testing**

  Missing local dependencies are preventing him from validating AI-scaffolded DAGs before promoting to dev.
- **Automate test coverage threshold increases**

  Currently a manual process; idea to use a scheduled GitHub Copilot agent to raise the threshold based on current coverage.

Last Updated: 2026-08-19
