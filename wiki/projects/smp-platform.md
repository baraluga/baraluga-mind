# SMP Platform

## Summary

SMP work in late June and early July 2026 centered on separating Japan and India environments, stabilizing production operations, improving deployment controls, and reducing manual dashboard/data-pipeline work.

The recurring operational theme was that India was still tied to Japan-era infrastructure or configuration in several places. Meeting notes mention India Airflow/Grafana access, CDH dataset ownership, GitHub/AWS OIDC setup, resource tagging, proxy errors, branch protection, Docker image separation, and documentation for secrets and dependencies.

## Details

- India environment separation work included scraper DAG detachment, Airflow Git sync, RDS setup, EFS production setup, IAM roles, Airflow/Grafana access, and CDH dataset migration from the Japan SMP project to the India project.
- CDH dataset disassociation was attributed in the notes to Japan dataset registration logic disassociating India datasets. The short-term fix was to reintroduce datasets to Japan prod config; the long-term direction was to migrate India datasets to the India project.
- Resource cleanup included application ID and environment tags for Japan and India. The same application ID was used for both environments.
- Proxy errors were reported as 403s in FMP Japan prod and FMP India prod while QA stayed consistently successful. Notes describe this as an incident symptom, not proven root cause.
- Branch protection direction discussed: core developers can push directly to dev and QA; prod requires PRs for all users.
- Current automated checks were described as linting, syntax checks, and import checks. Unit tests and coverage enforcement were not yet in place because of dependency issues.
- Future-proofing item: separate Docker images for Japan and India.
- [[smp-alerting-and-ops]] covers MS Teams email failures, fallback alerting, incident reporting, Grafana backup, and runbook automation.
- [[japan-interconnector-dashboard]] covers Japan interconnector data retrieval and dashboard work.
- [[copilot-dag-agent]] covers the DAG creation helper and branch workflow implications.

## Open Questions

- UNCERTAIN: Whether SMP prod database should be a cluster or a separate database still needed confirmation in the June 22 notes.
- UNCERTAIN: Exact root cause of the Japan/India production proxy 403s was not established in the captured notes.

## Sources

- `sources/meetings/2026-06-22-1415-granola-daily-standup.md`
- `sources/meetings/2026-06-23-1430-granola-new-dag-agent.md`
- `sources/meetings/2026-06-24-1552-granola-backlog-grooming.md`
- `sources/meetings/2026-06-29-1415-granola-standup.md`
- `sources/meetings/2026-07-01-0945-granola-am-standup.md`
- `sources/meetings/2026-07-02-1100-granola-sprint-planning.md`
- `sources/meetings/2026-07-02-1500-granola-sprint-planning.md`

Last Updated: 2026-07-04
