# Michael

## Current State

As of 2026-10-07.

- Back on SMP from 2026-10-01, split roughly 80% SMP and 20% Walnut migration. UNCERTAIN: the source says "SMB"; read as SMP from context.
- Owns SMP infrastructure and deployment. As of 2026-09-18 only he or [[joyce]] could build and push Airflow Docker images, and it was still manual. He is requesting the roles needed for a GitHub pipeline that automates Airflow and Grafana image deployment; ticket 507 was waiting on his role requirements as of 2026-10-05.
- Deployed the Darwin collector to India dev on 2026-10-01. It is blocked by proxy 403s, and he raised the proxy request with IT. Still waiting as of 2026-10-05.
- Point person for India proxy escalation, first with Nilo and then directly with Frederik.
- Core reviewer: SMP dev, QA, and prod merges require approval from [[brian-peralta]] or Michael.
- Pending: a knowledge-transfer walkthrough of the India DAGs for Lou with Brian, a JupyterLab demo with Eric, and a Loki demo with Jeka.

## Background

- One of the active SMP developers with [[joyce]] and [[brian-peralta]] (user-provided, 2026-07-04). Infrastructure-leaning: he presented the Kubernetes, pods, Airflow, and India/Japan coexistence part of the SMP overview for Jeroen.
- Brian's go-to for Docker/AWS ECR, cross-account S3 access, Grafana pod changes such as GeoJSON uploads, and redeploys.
- Led execution of the GitHub one-organization consolidation and Walnut migration from July: migrated SFF/common components to Walnut GitHub, was named for the India move from the old scraper org to `qrm-dms`, handled Artifactory dependencies, and aligned with Stefan and Nicole on hosting the GAMS installer in Artifactory. See [[sff-walnut-migration]].
- Earlier SMP work: fixed Graph API email sending and presented the mid-July sprint review with interconnector dashboard slides. See [[smp-alerting-and-ops]] and [[japan-interconnector-dashboard]].

## History

Role changes only. Detail stays in the sources.

- 2026-07-07: named lead for GitHub reorganization; 2026-07-08 execution lead for the Walnut migration, with 0.5 allocation to the AWS migration.
- 2026-07-15: dropped to ceremonies-only on SMP as the remaining budget tightened.
- 2026-09-30: announced the return to SMP starting 2026-10-01.

## Open Questions

- UNCERTAIN: surname and role title are not captured.

## Sources

- `sources/meetings/2026-06-22-1415-granola-daily-standup.md`
- `sources/meetings/2026-07-01-0945-granola-am-standup.md`
- `sources/meetings/2026-07-07-0945-granola-weekly-team-meeting.md`
- `sources/meetings/2026-07-08-0945-granola-am-standup.md`
- `sources/meetings/2026-07-08-1330-granola-walnut-migration-planning.md`
- `sources/meetings/2026-07-15-1500-granola-sprint-retro.md`
- `sources/meetings/2026-07-15-1630-granola-sprint-review.md`
- `sources/meetings/2026-07-28-1430-granola-smp-backlog-grooming.md`
- `sources/meetings/2026-07-30-1500-granola-sprint-planning.md`
- `sources/meetings/2026-07-31-0945-granola-am-standup.md`
- `sources/meetings/2026-08-04-1700-granola-application-team-meeting.md`
- `sources/meetings/2026-08-19-granola-smp-overview-with-jeroen.md`
- `sources/meetings/2026-09-02-backlog-grooming.md`
- `sources/meetings/2026-09-09-1600-granola-supporting-gams-in-our-walnut-artifactory.md`
- `sources/meetings/2026-09-18-1415-granola-smp-standup.md`
- `sources/meetings/2026-09-21-1700-granola-smp-technical-consultation-on-darwin.md`
- `sources/meetings/2026-09-25-1415-granola-smp-standup.md`
- `sources/meetings/2026-09-30-0945-granola-morning-standup.md`
- `sources/meetings/2026-09-30-1415-granola-smp-standup.md`
- `sources/meetings/2026-10-01-1415-granola-smp-standup.md`
- `sources/meetings/2026-10-05-granola-smp-standup.md`
- `sources/meetings/2026-10-05-granola-trading-data-platform-presentation-and-jupyterlab-roadmap-with-bong.md`
- `sources/meetings/2026-10-06-1415-granola-smp-standup.md`
- User clarification on 2026-07-04.

Last Updated: 2026-10-11
