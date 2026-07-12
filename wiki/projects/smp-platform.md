# SMP Platform

## Summary

SMP work in late June and early July 2026 centered on separating Japan and India environments, stabilizing production operations, improving deployment controls, and reducing manual dashboard/data-pipeline work.

The recurring operational theme was that India was still tied to Japan-era infrastructure or configuration in several places. Meeting notes mention India Airflow/Grafana access, CDH dataset ownership, GitHub/AWS OIDC setup, resource tagging, proxy errors, branch protection, Docker image separation, and documentation for secrets and dependencies.

## Details

- India environment separation work included scraper DAG detachment, Airflow Git sync, RDS setup, EFS production setup, IAM roles, Airflow/Grafana access, and CDH dataset migration from the Japan SMP project to the India project.
- CDH dataset disassociation was attributed in the notes to Japan dataset registration logic disassociating India datasets. The short-term fix was to reintroduce datasets to Japan prod config; the long-term direction was to migrate India datasets to the India project.
- Resource cleanup included application ID and environment tags for Japan and India. The same application ID was used for both environments.
- Proxy errors were reported as 403s in FMP Japan prod and FMP India prod while QA stayed consistently successful. Notes describe this as an incident symptom, not proven root cause.
- July 7 standup notes refine the proxy symptom: intermittent 403 Forbidden errors affected Japan and India prod since around 2026-06-26, about 6 out of 10 runs succeeded without changes, and QA appeared unaffected because it uses different proxy config. The working theory was a down or overloaded proxy in rotation, not a confirmed root cause.
- Branch protection direction discussed: core developers can push directly to dev and QA; prod requires PRs for all users.
- Current automated checks were described as linting, syntax checks, and import checks. Unit tests and coverage enforcement were not yet in place because of dependency issues.
- Future-proofing item: separate Docker images for Japan and India.
- July 8 standup notes make the Docker split more concrete: CSCR-119 needed separate images because Japan Airflow had pinned library dependencies while India used newer packaging.
- Kubernetes migration work was described as duplicating the VM setup into K8s, with documentation and codified execution setup still missing.
- S3-to-Airflow triggering was under review because 60-second polling was flagged as expensive; an event-driven path from S3 to EFS to the Airflow radio folder was proposed.
- July 7 Francois-help notes say GEMS Artifactory credentials were obsolete in SMP India/Japan README setup; only SMP Common through Walnut Artifactory was required in that walkthrough.
- July 7 Codex work committed and pushed README updates to `smp-india` and `smp-japan` under `SCR-1100`, simplifying Artifactory setup to `smp-core-prod`/Tools Artifactory credentials and treating GEM indexes as intranet/Zscaler reachable rather than separately credentialed.
- July 8 Codex work added README instructions to install local `pre-commit` and `pre-push` hooks in `smp-india` and `smp-japan`, including Windows PowerShell coverage. The durable policy point was that local hooks can be automated for convenience, but real enforcement is CI plus required branch protection.
- Pipeline tests were still skipped because of Zscaler proxy dependency and Walnut/GEMS Artifactory auth. The captured workaround was local reviewer testing until the GitHub migration team/Ilo sorts out the Walnut runner.
- July 8 AWS migration notes say the Walnut runner in the new GitHub org was still blocking automated Docker image builds because TLS trust for the GEMS artifact registry was not set up correctly.
- July 9 notes say `smp-common 0.4.3` introduced `send_debug_dag_email`, `smp-japan` wired it into the manual interconnector backfill DAG, and `smp-tool` was later bumped to `smp-common>=0.4.3`. The runtime still requires a QA Airflow image rebuild/redeploy before deployed DAGs can import the new callback.
- July 9 Copilot dependency audit removed dead `smp-tool` extras and flagged that `smp-india` uses `plotly` without declaring it directly, relying on `smp-tool` base dependencies.
- User account management was moving through `SCR-1172`, with a meeting planned with Jim to configure access rights. The next-sprint target was India user access plus detailed training, with Matteo to be invited.
- Synapse integration was not yet accepted; a demo was requested to evaluate fit before committing.
- PR review should stay in the loop initially, with rules preventing contributors from self-approving or self-merging.
- July 9 Copilot walkthrough summarized the SMP collection as separate region DAG repos (`smp-india`, `smp-japan`), runtime/deployment in `smp-tool`, and CDH/Grafana work in `smp-dashboard`. It reinforced the contract that DAG outputs intended for dashboards land as `dashboard_data/<dataset>/<stage>/<file>.parquet` before CDH/Athena/Grafana wiring.
- July 9 technical standup notes say CDK `6.5.1` was released to MS prod, NOP prod, Pyrene, and GMR, but compute-environment creation failed because some roles still expected the removed `dash-infra` project-name suffix.
- Pyrene migration status on July 9: compute environment migration was done, 13 TB EFS recovery was running via S3 sync, UAT setup was pending SSL certificate, and the rough target was Wednesday with worst case end of next week.
- Prosumer security remediation on July 9 centered on backend authorization for user lookup/sharing flows. The current frontend-controlled permission model was called out as insufficient, and the user microservice needed broader fix work across systems.
- [[smp-alerting-and-ops]] covers MS Teams email failures, fallback alerting, incident reporting, Grafana backup, and runbook automation.
- [[japan-interconnector-dashboard]] covers Japan interconnector data retrieval and dashboard work.
- [[copilot-dag-agent]] covers the DAG creation helper and branch workflow implications.
- July 12 Walnut diagnostics proved that `IS_INFRA_ROOT_CRT.crt` is the CA required for GEMS Artifactory: default trust failed with certificate verification code 19, while an explicit request using that CA returned HTTP 200 with verification code 0.
- Walnut can access the GEMS Python indexes anonymously. The initial India/Japan authorization failures came from sending usernames with empty passwords; removing those incomplete GEMS credentials allowed full dependency synchronization. Tools Artifactory still uses its separate credentials.
- India and Japan CI were consolidated into one workflow per repository with parallel docs, lint, and test jobs. Tests run on Walnut with frozen dependency sync, fork-PR isolation, timeouts, least-privilege permissions, and current action versions; both full pipelines were verified green.
- A private, narrowly scoped `qrm-dms/install-engie-ca` composite-action repository was created and released as `v1`. It installs and fingerprints the ENGIE CA without coupling certificate setup to Python or `uv`.
- The attempted native transfer of `smp-japan` to `qrm-dms` was pending owner acceptance at the end of the capture. The repository was changed to private before transfer, but neither old nor new remote was reachable while approval was pending; existing Airflow DAG checkouts could continue, while git-sync, restarts, or new pods were at risk.
- Durable migration preference after this incident: use a staged private mirror when only Git refs and history need preservation, keep the source operational through verification, and avoid approval-dependent organization operations unless explicitly authorized with the downtime boundary understood.

## Open Questions

- UNCERTAIN: Whether SMP prod database should be a cluster or a separate database still needed confirmation in the June 22 notes.
- UNCERTAIN: Exact root cause of the Japan/India production proxy 403s was not established in the captured notes.
- UNCERTAIN: Who owns approval and rotation of the ENGIE root certificate despite its technical validation for GEMS access.
- UNCERTAIN: Whether the pending `smp-japan` native transfer was accepted after the July 12 capture.
- UNCERTAIN: Whether Pyrene UAT should be always-on or on-demand remains unresolved in migration notes.
- UNCERTAIN: The exact final remediation shape for user lookup permissions belongs to a follow-up technical discussion.

## Sources

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

Last Updated: 2026-07-13
