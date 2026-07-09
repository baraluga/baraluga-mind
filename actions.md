# Actions

Centralized action list migrated from wiki page `TODO:` items on 2026-07-04.

## Today

## Open

### Team Operations

- [ ] Complete the 40-minute training video.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-07-0945-granola-weekly-team-meeting.md`

- [ ] Submit the engagement meter survey and midyear GitHub feedback.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-07-0945-granola-weekly-team-meeting.md`; `sources/meetings/2026-07-08-0945-granola-am-standup.md`

- [ ] Finalize GitHub organization members, targets, and git rules before end of July.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-07-0945-granola-weekly-team-meeting.md`; `sources/meetings/2026-07-08-1330-granola-walnut-migration-planning.md`

- [ ] Post a short team-chat note documenting the GitHub CLI remote-transfer approach for existing repos.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-07-1415-granola-standup.md`

- [ ] Update PR rules to prevent contributors from self-merging.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-07-1530-granola-francois-help.md`

- [ ] Adjust and share AWS migration allocation so Brian is reviewer/consultant rather than primary owner.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-08-0945-granola-am-standup.md`

- [ ] Confirm Artifactory status and artifact publishing plan for the GitHub/Walnut migration.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-08-1330-granola-walnut-migration-planning.md`

- [ ] Sync Pyrine and GMR tickets to Dale's board.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-08-1514-granola-aws-migration-standup.md`

- [ ] Request Maintainer access in Auto for Brian.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-09-0945-granola-am-standup.md`

- [ ] Document the manual ADO-to-GitHub migrator UI process before automating it.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-09-0945-granola-am-standup.md`

- [ ] Coordinate Click migration with JB after security remediation is complete.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-09-1515-granola-technical-team-standup.md`

### Job Search

- [ ] Enable Chrome local file access for Codex, then submit the queued LinkedIn/manual applications.
  - Context: [[job-search-2026]]
  - Source: `sources/codex-conversations/2026-07-07-codex-conversations.md`; `sources/codex-conversations/2026-07-08-codex-conversations.md`; `sources/codex-conversations/2026-07-09-codex-conversations.md`

### Japan Interconnector

- [ ] Try the interconnector historical backfill as a month-by-month run.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/notes/2026-07-07.md`

- [ ] Reimport the updated `SCR-1197` look-back dashboard JSON after the date-only `as_of` fix.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/codex-conversations/2026-07-07-codex-conversations.md`

- [ ] Capture successful reconciliation input manifests and latest daily capacity output keys before implementing reconciliation source-selection hardening.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/codex-conversations/2026-07-07-codex-conversations.md`

- [ ] Clarify look-back dashboard point-in-time requirements with Hermine.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/meetings/2026-07-07-1415-granola-standup.md`

- [ ] Confirm whether the existing dashboard data export feature is sufficient once the current interconnector dashboard is finalized.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/meetings/2026-07-08-1514-granola-aws-migration-standup.md`; `sources/meetings/2026-07-09-1415-granola-smp-standup.md`

- [ ] Send Japan group chat message on dashboard review, historical look-back feedback, and `SCR-1198` export confirmation.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/meetings/2026-07-09-1415-granola-smp-standup.md`

- [ ] Raise PR for `SCR-11102`.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/meetings/2026-07-09-1415-granola-smp-standup.md`

- [ ] Check Prometheus for Japan QA cluster memory pressure and namespace memory reservation after parallel backfill failures.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/meetings/2026-07-09-1415-granola-smp-standup.md`

- [ ] Confirm actual-flow source path for FY2019-FY2024 with Hiromi.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/meetings/2026-07-09-1415-granola-smp-standup.md`

### SMP Dashboards

- [ ] Complete a Grafana dashboard end-to-end as a solo exercise.
  - Context: [[smp-dashboards]]
  - Source: `sources/meetings/2026-07-07-1530-granola-francois-help.md`

- [ ] Use the solo Grafana exercise to demonstrate self-service capability to Material and Adrian, then replicate with Carlos.
  - Context: [[smp-dashboards]]
  - Source: `sources/meetings/2026-07-07-1530-granola-francois-help.md`

- [ ] Investigate Grafana database type and backup strategy.
  - Context: [[smp-dashboards]]
  - Source: `sources/meetings/2026-07-08-1514-granola-aws-migration-standup.md`

### SMP Platform

- [ ] Finalize CSCR-119 Docker image separation for Japan and India Airflow version conflicts.
  - Context: [[smp-platform]]
  - Source: `sources/meetings/2026-07-08-0945-granola-am-standup.md`

- [ ] Document and codify Kubernetes environment setup for the VM-to-K8s migration.
  - Context: [[smp-platform]]
  - Source: `sources/meetings/2026-07-08-0945-granola-am-standup.md`

- [ ] Evaluate the event-driven S3-to-Airflow trigger proposal as an alternative to 60-second polling.
  - Context: [[smp-platform]]
  - Source: `sources/meetings/2026-07-08-0945-granola-am-standup.md`

- [ ] Check whether the GEMS artifact registry TLS certificate issue is in team scope.
  - Context: [[smp-platform]]
  - Source: `sources/meetings/2026-07-08-1514-granola-aws-migration-standup.md`

- [ ] Evaluate Synapse integration fit after the requested demo.
  - Context: [[smp-platform]]
  - Source: `sources/meetings/2026-07-08-1514-granola-aws-migration-standup.md`

- [ ] Rebuild and redeploy the QA Airflow image so `smp-common 0.4.3` is available at runtime.
  - Context: [[smp-platform]]
  - Source: `sources/codex-conversations/2026-07-09-codex-conversations.md`; `sources/copilot-conversations/2026-07-09-copilot-conversations.md`

- [ ] Fix the CDK compute-environment role bug caused by the removed `dash-infra` suffix and redeploy.
  - Context: [[smp-platform]]
  - Source: `sources/meetings/2026-07-09-1515-granola-technical-team-standup.md`

- [ ] Publish an unofficial artifact to test the `dash-infra` suffix correction before creating a PR.
  - Context: [[smp-platform]]
  - Source: `sources/meetings/2026-07-09-1515-granola-technical-team-standup.md`

- [ ] Resume Pyrene EFS S3 sync with a detachable session or Kubernetes job, considering 16-20 threads.
  - Context: [[smp-platform]]
  - Source: `sources/meetings/2026-07-09-1515-granola-technical-team-standup.md`

- [ ] Handle the Pyrene UAT SSL certificate request.
  - Context: [[smp-platform]]
  - Source: `sources/meetings/2026-07-09-1515-granola-technical-team-standup.md`

- [ ] Schedule a focused user-microservice security discussion with a subset of the team.
  - Context: [[smp-platform]]
  - Source: `sources/meetings/2026-07-09-1515-granola-technical-team-standup.md`

- [ ] Message Lloyd about AWS ADO access.
  - Context: [[smp-platform]]
  - Source: `sources/meetings/2026-07-09-1515-granola-technical-team-standup.md`

### AI Assisted Engineering

- [ ] Confirm Copilot token billing model with Irun.
  - Context: [[ai-assisted-engineering]]
  - Source: `sources/meetings/2026-07-07-1530-granola-francois-help.md`

- [ ] Set up an encrypted common-stack SNS topic for Grafana APM alerts and coordinate the Teams channel subscriber with Nilo.
  - Context: [[smp-alerting-and-ops]]
  - Source: `sources/meetings/2026-07-09-1515-granola-technical-team-standup.md`

## Waiting

### Recruitment

- [ ] Wait for Alfred's further assessment of Matt Mendez.
  - Context: [[recruitment-2026]]
  - Source: `sources/meetings/2026-07-08-1100-granola-matt-mendez.md`

### Team Operations

- [ ] Wait for Alexander to define GitHub governance pipeline and master branch protection rules.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-08-1330-granola-walnut-migration-planning.md`

- [ ] Wait for Michael to set up the GitHub repo structure and migrate the first repo.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-08-1330-granola-walnut-migration-planning.md`

- [ ] Clarify Pyrine UAT environment scope with Nicola.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-08-1514-granola-aws-migration-standup.md`

## Done

### Baraluga Mind

- [x] Decide whether to automate the daily Codex conversation dump into `inbox/`.
  - Context: [[baraluga-mind]]
  - Source: `sources/codex-conversations/2026-07-06-codex-conversations.md`

### SMP Platform

- [x] Document user secrets and Python dependency addition process.
  - Context: [[smp-platform]]
  - Source: `sources/meetings/2026-06-24-1552-granola-backlog-grooming.md`

- [x] Define and document Airflow/dashboard user roles and permissions.
  - Context: [[smp-platform]]
  - Source: `sources/meetings/2026-07-02-1100-granola-sprint-planning.md`

- [x] Confirm whether Helm upgrade needs an image digest or latest tag.
  - Context: [[smp-platform]]
  - Source: `sources/meetings/2026-06-24-1552-granola-backlog-grooming.md`



### Alerting and Ops

- [x] Implement email fallback on 403 or any request error in the MS Teams alert script.
  - Context: [[smp-alerting-and-ops]]
  - Source: `sources/meetings/2026-07-02-1100-granola-sprint-planning.md`

- [x] Write the GEMS service desk report for the proxy incident.
  - Context: [[smp-alerting-and-ops]]
  - Source: `sources/meetings/2026-07-02-1500-granola-sprint-planning.md`



### Japan Interconnector

- [x] Share the proxy address needed for ticket 1186.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/meetings/2026-07-07-1415-granola-standup.md`; `sources/meetings/2026-07-09-1415-granola-smp-standup.md`

- [x] Pair with Francois on ticket 1100 dependency setup.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/meetings/2026-07-07-1415-granola-standup.md`; `sources/notes/2026-07-09.md`

- [x] Investigate why `reconcile_capacity_task` started failing after the 13:00 successful run.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/codex-conversations/2026-07-07-codex-conversations.md`

- [x] Verify and finish the parent-ticket transition for `SCR-1126`, `SCR-1127`, `SCR-1128`, `SCR-1129`, `SCR-1168`, `SCR-1138`, and `SCR-1137`.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/codex-conversations/2026-07-06-codex-conversations.md`

- [x] Confirm TSDB time series IDs with Francois/Japan team.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/meetings/2026-07-02-1500-granola-sprint-planning.md`

- [x] Continue coordinating dashboard feedback with the Japan team.
  - Context: [[japan-interconnector-dashboard]]
  - Source: `sources/meetings/2026-07-01-1630-granola-smp-revie.md`



### SMP Dashboards

- [x] Export Grafana dashboard JSON versions 1-9 once access is available.
  - Context: [[smp-dashboards]]
  - Source: `sources/meetings/2026-07-02-1100-granola-sprint-planning.md`



### Copilot DAG Agent

- [x] Update SMP India and SMP Japan READMEs with Windows commands and Artifactory credential setup.
  - Context: [[copilot-dag-agent]]
  - Source: `sources/meetings/2026-06-23-1430-granola-new-dag-agent.md`

- [x] Refine the agent prompt so it stops looking for a non-existent DAG helper skill.
  - Context: [[copilot-dag-agent]]
  - Source: `sources/meetings/2026-06-23-1430-granola-new-dag-agent.md`

- [x] Have a colleague implement a small DAG and raise a PR to `main`.
  - Context: [[copilot-dag-agent]]
  - Source: `sources/meetings/2026-06-23-1430-granola-new-dag-agent.md`



### Recruitment

- [x] Prioritize Azure experience in remaining CV screening.
  - Context: [[recruitment-2026]]
  - Source: `sources/meetings/2026-06-30-1600-granola-recruitment-alignment.md`



### AI Assisted Engineering

- [x] Fred to bring team-level AI implementation planning to the tech meeting.
  - Context: [[ai-assisted-engineering]]
  - Source: `sources/meetings/2026-07-02-1700-granola-application-team-meeting.md`



### Team Operations

- [x] Send anniversary date survey.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-06-23-0945-granola-team-meeting.md`

- [x] Fix Tempo reporting/configuration issues.
  - Context: [[team-operations]]
  - Source: `sources/meetings/2026-07-02-1700-granola-application-team-meeting.md`

- [x] Refactor `ado-ios` v1 with Ruff, pytest, TDD module split, and merged PR.
  - Context: [[ado-ios]]
  - Source: `sources/copilot-conversations/2026-07-09-copilot-conversations.md`



### People

- [x] Improve loop-in process for ticket updates and stakeholder messages.
  - Context: [[brian-peralta]]
  - Source: `sources/meetings/2026-06-30-1504-granola-feedback-from-francois.md`

- [x] Francois to add explicit validation checkpoints to the ticket workflow.
  - Context: [[francois]]
  - Source: `sources/meetings/2026-06-30-1504-granola-feedback-from-francois.md`

- [x] Francois to provide TSDB time series IDs.
  - Context: [[francois]]
  - Source: `sources/meetings/2026-07-02-1500-granola-sprint-planning.md`

- [x] Francois to submit the resource planning form by end of week from the June 30 note.
  - Context: [[francois]]
  - Source: `sources/meetings/2026-06-30-1504-granola-feedback-from-francois.md`
