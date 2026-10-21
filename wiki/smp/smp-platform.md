# SMP Platform

## Current State

As of 2026-10-21.

- **Focus:** India delivery dominates. The 2026-09-23 sprint had no active Japan ticket. Japan next-period work is bug fixes and robustness; Common work is platform capabilities. India data products are on [[smp-india]].
- **Team:** [[brian-peralta]] runs delivery on India time-and-materials work from September. [[michael]] is back on SMP from 2026-10-01 at about 80%, owning infrastructure and deploys. Francois validates tickets and leads demos. Lou Dubuisson is taking over Mateo's India point-of-contact role and still needs a knowledge-transfer walkthrough of the India DAGs.
- **Process:** Japan is now in Kanban support mode with no active development; new requests enter a backlog for stakeholder prioritisation against available capacity. Bi-weekly meetings continue for delivery and budget visibility. India POC attempts remain capped at five before pivoting, and the team talks to India directly with no PO intermediary.
- **Budget:** the 2026-10-21 review reported 84% consumed for the current period, with most cost still supported by the India team. The source does not state the final budget or forecast.
- **Next-period priorities (2026-10-07/08):**
  - Darwin data fetch once access is fixed: [[darwin-collector]].
  - Jupyter DAG authoring: [[smp-jupyter-dag-authoring]].
  - `SCR-507` Docker image build/push automation. Michael is requesting the pipeline roles.
  - Observability: cluster resources under `SCR-1254`, Darwin monitoring under `SCR-1268`.
  - `SCR-1284` dashboard-delay analysis.
  - Lou onboarding. `SCR-1285` already added a CI-validated `data_catalog` of enabled DAGs.
- **Main blockers:** network and geo access for India sources. See [[smp-india-access]].

## Background

### Architecture

- **Environments:** one SMP codebase serves isolated Japan and India environments. DAGs are scrapers, transformations, and optional reconciliations, with outputs published to CDH or TSDB.
- **Repos (all in `qrm-dms`):**
  - `smp-india` and `smp-japan` hold the regional DAGs.
  - `smp-tool` holds the runtime and deployment.
  - `smp-dashboard` holds CDH registration and Grafana JSON.
  - `smp-common` is the shared library. `0.5.0` added the canonical TSDB publication runtime (validation, incremental writes, forecast-version protection, read-back verification); `0.6.0` is in production; `0.8.0` added the shared backfill runtime.
- **Runtime:** Airflow on AWS EKS via Helm, with web server, scheduler, Celery workers, triggerer, and Git-sync sidecar. DAGs load from GitHub on merge. Dev and QA are namespaces in a shared non-prod cluster, which was about 90% utilized in October; prod has its own cluster. Airflow metadata is on RDS. Custom images live in ECR and are still built and pushed manually.
- **Data flow:** DAG → parquet on EFS → S3/CDH via `smp-common` → Athena → Grafana. Dashboard outputs follow `dashboard_data/<dataset>/<stage>/<file>.parquet`.
  - TSDB is the governed source for reusable time series.
  - CDH holds durable evidence and analytics. It is also the bridge to Grafana, because Grafana cannot read TSDB directly.
  - Grafana is for presentation. Panels should nominate underlying data products rather than be published blindly.
- **CDH registration rules:**
  - The dataset must already exist in the CDH project.
  - The S3 key must match the dataset name.
  - At least one stage, such as `latest`, is needed before Grafana sees the dataset.
  - Schema-sample parquet must have zero rows, or Athena serves it as business data.
  - The `cdh-sdk` registration workflow can report success while the crawler failed, so it now fails loudly.
- **Orchestration direction:** Airflow Assets (`SCR-1239`) let consumers trigger on upstream data instead of on fixed offsets. Japan nuclear-dataset consumers are the first candidate, when budget allows.

### Governance and CI

- **Branch rules:** `dev`, `qa`, and `prod` need a PR, one `SMP-CODEOWNERS` approval after the latest push, and block deletion and force-push. Core approvers are Brian and Michael.
- **GitHub teams:** `SMP` (read, scrum team), `SMP-CODEOWNERS` (admin, core developers), `SMP-INDIA` (write, DAG contributors).
- **Tools Artifactory:** separate from GitHub and carries a licence cost. Contributors without it use `python scripts/sync_local.py`.
- **CI:** one workflow per repo with docs, lint (Ruff), pytest, and a coverage threshold, running on the Walnut runner. The ENGIE CA comes from `qrm-dms/install-engie-ca@v1`. Local git hooks are a convenience only; CI plus branch protection is the real enforcement.
- **Onboarding:** new DAGs start from the `New DAG` issue template, assigned to Copilot with the DAG Helper custom agent, which opens a draft PR. See [[copilot-dag-agent]]. It was still a pilot with no production DAGs as of August. Contributors also need Tools/Walnut Artifactory access through the `Modify Walnut Project` IT form, which the SMP team owns.
- **Known gaps (2026-08-19):** no CI image rebuild, no security-patch rebuild policy, and repos test on Python 3.13 while the Airflow image runs 3.12. Bitnami `kubectl:latest` is still used by the DAG processor sidecar, per checked-in config.

### Lessons Worth Keeping

- Repository moves: use a staged private mirror, keep the source live until verified, and avoid approval-dependent org transfers. The July `smp-japan` native transfer left both remotes unreachable while waiting for approval.
- Prove S3 access with exact-object reads rather than bucket listing, and suppress Botocore wire logging, which can print temporary credentials.
- Per-series sequential TSDB reads make publish-and-verify slow. A bulk reader cut an RTM run from about 5 minutes to about 27 seconds; see [[tsdb-bulk-read-probing]].
- Long TSDB backfills can outlive the token. Use parallel tasks with per-task token renewal, or split by year.

### Related Pages

- [[smp-india]]: India data products
- [[darwin-collector]]: the Darwin realtime collector
- [[smp-india-access]]: India network and access blockers
- [[smp-jupyter-dag-authoring]]: the Jupyter DAG-authoring work
- [[japan-interconnector-dashboard]] and [[smp-dashboards]]: Japan and dashboard work
- [[smp-alerting-and-ops]]: alerting, the File Browser monitor, and runbooks
- [[apac-tsdb-scraper]]: the older Lambda scrapers, including IEX RTM and Aurora
- [[sff-walnut-migration]]: the GitHub/Walnut migration
- [[technical-activities]]: non-SMP projects that previously lived on this page

## History

- 2026-07: India/Japan environment separation; SMP repos migrated into `qrm-dms`; CI consolidated onto Walnut; branch rulesets applied on 2026-07-28.
- 2026-07-15: remaining budget tightens; Michael drops to ceremonies-only.
- 2026-07-30: `smp-common` shared TSDB runtime reaches production (`0.6.0`).
- 2026-09: India time-and-materials work starts; POC cap and direct India access agreed at the 2026-09-09 retro.
- 2026-10-01: Michael returns to SMP.
- 2026-10-09: Kanban transition proposed.

## Open Questions

- UNCERTAIN: Who can update the AWS IAM OIDC trust for the `qrm-dms/smp-tool` India deployment subjects. It blocked `qa-india` and `prod-india` promotion in July; current status is not captured.
- UNCERTAIN: Whether the live clusters still run the Bitnami images seen in checked-in config.
- UNCERTAIN: Whether `Pathway`, in the `SCR-1284` delay flow, is an exact system name.
- UNCERTAIN: Whether the Kanban move was agreed with Fred and Bong.

## Sources

This page was split on 2026-10-11 into [[smp-india]], [[darwin-collector]], [[smp-india-access]], [[smp-jupyter-dag-authoring]], and [[technical-activities]]. The list below is the full evidence trail for the original page. The child pages cite their main sources and point back here. Open questions that were resolved, stale, or only about transcription were pruned; the prior version is in git history.

- `sources/meetings/2026-06-22-1415-granola-daily-standup.md`
- `sources/meetings/2026-06-23-1430-granola-new-dag-agent.md`
- `sources/meetings/2026-06-24-1552-granola-backlog-grooming.md`
- `sources/meetings/2026-06-29-1415-granola-standup.md`
- `sources/meetings/2026-07-01-0945-granola-am-standup.md`
- `sources/meetings/2026-07-02-1100-granola-sprint-planning.md`
- `sources/meetings/2026-07-02-1500-granola-sprint-planning.md`
- `sources/meetings/2026-07-07-1415-granola-standup.md`
- `sources/meetings/2026-07-07-1530-granola-francois-help.md`
- `sources/codex-conversations/2026-07-07-codex-conversations.md`
- `sources/meetings/2026-07-08-0945-granola-am-standup.md`
- `sources/meetings/2026-07-08-1514-granola-aws-migration-standup.md`
- `sources/codex-conversations/2026-07-08-codex-conversations.md`
- `sources/copilot-conversations/2026-07-09-copilot-conversations.md`
- `sources/codex-conversations/2026-07-09-codex-conversations.md`
- `sources/meetings/2026-07-09-0945-granola-am-standup.md`
- `sources/meetings/2026-07-09-1515-granola-technical-team-standup.md`
- `sources/codex-conversations/2026-07-12-codex-conversations.md`
- `sources/meetings/2026-07-13-1515-granola-technical-activities-standup.md`
- `sources/meetings/2026-07-14-0945-granola-team-meeting.md`
- `sources/meetings/2026-07-14-1515-granola-technical-standup.md`
- `sources/notes/2026-07-15-ingest-handover-clarifications.md`
- `sources/codex-conversations/2026-07-15-codex-conversations.md`
- `sources/notes/2026-07-15.md`
- `sources/codex-conversations/2026-07-16-codex-conversations.md`
- `sources/codex-conversations/2026-07-17-codex-conversations.md`
- `sources/meetings/2026-07-17-1600-granola-technical-activities.md`
- `sources/meetings/2026-07-20-1415-granola-standup.md`
- `sources/meetings/2026-07-20-1645-granola-ta-standup.md`
- `sources/codex-conversations/2026-07-20-codex-conversations.md`
- `sources/codex-conversations/2026-07-22-codex-conversations.md`
- `sources/meetings/2026-07-24-1415-granola-daily-standup.md`
- `sources/meetings/2026-07-24-1515-granola-technical-standup.md`
- `sources/notes/2026-07-27-ingest-handover-clarifications.md`
- `sources/meetings/2026-07-28-1430-granola-smp-backlog-grooming.md`
- `sources/codex-conversations/2026-07-28-codex-conversations.md`
- `sources/notes/2026-07-29-ingest-handover-clarifications.md`
- `sources/codex-conversations/2026-07-29-codex-conversations.md`
- `sources/meetings/2026-07-29-1500-granola-sprint-retro.md`
- `sources/meetings/2026-07-29-1630-granola-sprint-review.md`
- `sources/notes/2026-07-30-ingest-handover-clarifications.md`
- `sources/meetings/2026-07-30-1232-granola-generation-data-scraper.md`
- `sources/meetings/2026-07-30-1500-granola-sprint-planning.md`
- `sources/notes/2026-07-30.md`
- `sources/codex-conversations/2026-07-30-codex-conversations.md`
- `sources/codex-conversations/2026-07-31-codex-conversations.md`
- `sources/meetings/2026-07-31-1415-granola-daily-standup.md`
- `sources/notes/2026-07-31-ingest-handover-clarifications.md`
- `sources/meetings/2026-08-03-1415-granola-busy.md`
- `sources/notes/2026-08-04-ingest-handover-clarifications.md`
- `sources/codex-conversations/2026-08-03-codex-conversations.txt`
- `sources/meetings/2026-08-04-1415-granola-daily-standup.md`
- `sources/meetings/2026-08-06-1415-granola-daily-standup.md`
- `sources/codex-conversations/2026-08-06-codex-conversations.txt`
- `sources/codex-conversations/2026-08-07-codex-conversations.txt`
- `sources/meetings/2026-08-11-1415-granola-daily-standup.md`
- `sources/meetings/2026-08-11-1430-granola-backlog-grooming.md`
- `sources/meetings/2026-08-19-granola-busy.md`
- `sources/meetings/2026-08-19-granola-smp-overview-with-jeroen.md`
- `sources/meetings/2026-08-19-granola-backlog-grooming.md`
- `sources/codex-conversations/2026-08-20-codex-conversations.txt`
- `sources/codex-conversations/2026-08-24-codex-conversations.txt`
- `sources/codex-conversations/2026-08-26-codex-conversations.txt`
- `sources/meetings/2026-08-27-granola-mateo-call.md`
- `sources/codex-conversations/2026-08-27-codex-conversations.txt`
- `sources/meetings/2026-09-01-granola-busy.md`
- `sources/copilot-conversations/2026-09-01-copilot-conversations.md`
- `sources/codex-conversations/2026-09-01-codex-conversations.txt`
- `sources/meetings/2026-09-02-daily-standup.md`
- `sources/meetings/2026-09-02-standup.md`
- `sources/meetings/2026-09-02-backlog-grooming.md`
- `sources/codex-conversations/2026-09-02-codex-conversations.txt`
- `sources/codex-conversations/2026-09-03-codex-conversations.txt`
- `sources/meetings/2026-09-04-daily-standup.md`
- `sources/codex-conversations/2026-09-08-codex-conversations.txt`
- `sources/meetings/2026-09-09-1531-granola-smp-sprint-retro.md`
- `sources/meetings/2026-09-09-1630-granola-smp-sprint-review.md`
- `sources/codex-conversations/2026-09-09-codex-conversations.txt`
- `sources/codex-conversations/2026-09-10-codex-conversations.txt`
- `sources/codex-conversations/2026-09-14-codex-conversations.txt`
- `sources/meetings/2026-09-14-1415-granola-standup.md`
- `sources/meetings/2026-09-15-weekly-team-meeting.md`
- `sources/codex-conversations/2026-09-15-codex-conversations.txt`
- `sources/meetings/2026-09-17-1700-granola-tech-lead-roundtable.md`
- `sources/codex-conversations/2026-09-17-codex-conversations.txt`
- `sources/codex-conversations/2026-09-18-codex-conversations.txt`
- `sources/meetings/2026-09-18-0945-granola-daily-standup.md`
- `sources/meetings/2026-09-18-1230-granola-darwin-api.md`
- `sources/meetings/2026-09-18-1415-granola-smp-standup.md`
- `sources/meetings/2026-09-21-1415-granola-smp-standup.md`
- `sources/meetings/2026-09-21-1700-granola-smp-technical-consultation-on-darwin.md`
- `sources/codex-conversations/2026-09-21-codex-conversations.txt`
- `sources/meetings/2026-09-22-0945-granola-weekly-team-meeting.md`
- `sources/codex-conversations/2026-09-22-codex-conversations.txt`
- `sources/meetings/2026-09-23-1630-granola-smp-sprint-review.md`
- `sources/codex-conversations/2026-09-23-codex-conversations.txt`
- `sources/codex-conversations/2026-09-24-codex-conversations.txt`
- `sources/codex-conversations/2026-09-25-codex-conversations.txt`
- `sources/meetings/2026-09-25-1415-granola-smp-standup.md`
- `sources/codex-conversations/2026-09-28-codex-conversations.txt`
- `sources/meetings/2026-09-28-1415-granola-smp-standup.md`
- `sources/codex-conversations/2026-09-29-codex-conversations.txt`
- `sources/codex-conversations/2026-09-30-codex-conversations.txt`
- `sources/meetings/2026-09-30-0945-granola-morning-standup.md`
- `sources/meetings/2026-09-30-1415-granola-smp-standup.md`
- `sources/meetings/2026-09-30-1530-granola-sprint-backlog-grooming.md`
- `sources/meetings/2026-10-01-1415-granola-smp-standup.md`
- `sources/meetings/2026-10-01-1433-granola-backlog-grooming-again.md`
- `sources/codex-conversations/2026-10-01-codex-conversations.txt`
- `sources/codex-conversations/2026-10-02-codex-conversations.txt`
- `sources/meetings/2026-10-05-granola-smp-standup.md`
- `sources/meetings/2026-10-05-granola-trading-data-platform-presentation-and-jupyterlab-roadmap-with-bong.md`
- `sources/meetings/2026-10-06-1415-granola-smp-standup.md`
- `sources/meetings/2026-10-07-granola-integration-of-jupyterlab-to-airflow.md`
- `sources/meetings/2026-10-07-granola-morning-standup.md`
- `sources/meetings/2026-10-07-granola-sprint-review.md`
- `sources/meetings/2026-10-08-1131-granola-sprint-planning.md`
- `sources/meetings/2026-10-08-1431-granola-another-attempt-at-jupyter-discussion.md`
- `sources/meetings/2026-10-08-1533-granola-sprint-planning.md`
- `sources/codex-conversations/2026-10-08-codex-conversations.txt`
- `sources/meetings/2026-10-09-1415-granola-daily-standup.md`
- `sources/codex-conversations/2026-10-09-codex-conversations.txt`
- `sources/meetings/2026-10-21-1415-granola-smp-retro.md`
- `sources/meetings/2026-10-21-1630-granola-smp-review.md`

Last Updated: 2026-10-22
