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
- July 13 standup reported Pyrene UAT deployed and the high-worker configuration for GMR / Model Runner removed because only default and low workers were needed. Alfred recreated production compute environments. The source also says a model-runner web image called `Kubic` was updated to `v3.8.5`; that name remains unconfirmed.
- A scoped replacement is planned for an overly permissive AWS role used by the model-runner pipeline. The intended rollout is to validate trust and permissions in dev, then reproduce the working policy in production.
- Updated high-worker and Phoenix-worker requirements created dev/UAT allocation conflicts. The notes cite Phoenix at 100 GB minimum and 220 GB memory, and call for exact machine counts plus per-environment memory before adding node groups.
- Prosumer remediation remains incomplete. Public-domain security headers were applied, internal project-specific headers need a working session, and the user-microservice endpoint change exists but still needs testing and discussion with Nico. The training section will remain authenticated while the rest of the homepage stays available as an unauthenticated landing page.
- APM migration to Walnut was reported done. The shared certificate action was reused successfully by SMP Japan; SMP India remains on hold for Francois's prerequisites. SMP Japan is blocked on approval of confirmed SMP functional user `nprm68` into an organization transcribed as `qrmvms`.
- July 14 team notes reported an SMP file browser plugin authentication issue after an upgrade to a new non-Airflow version, with `3.3.0` and `3.2.2` mentioned as version context.
- SAP / `qrm-dms` migration planning was still waiting on final solution architecture with Nilo and a go-live date confirmation. The notes say feasibility was confirmed to Luke, but `qrm-dms` access-token authorization was still blocking safe SMP India to qrm-dms migration.
- APM migration itself was reported complete on July 14, but Grafana still needed an AWS admin to create or confirm a role for CloudWatch or publish access in the APM context.
- Clickstart pre-migration work was mentioned with custom node-group labels and deployment-role cleanup, but a July 15 clarification says the term still needs more context before treating the details as settled.
- Extruder remediation had remaining critical issues to investigate before deciding whether other remediation tasks can wait until after go-live.
- July 15 Codex work migrated `smp-india` into `qrm-dms/smp-india` as a private Git mirror with only `dev`, `qa`, and `prod`; the three branch SHAs matched the source and no tags existed. The old source repository was later archived read-only rather than deleted.
- `smp-tool` India git-sync references were updated to `qrm-dms/smp-india` and promoted to `dev-india`, but runtime promotion stopped there because AWS rejected GitHub OIDC for the new `qrm-dms/smp-tool` repository subjects. `qa-india` and `prod-india` were intentionally not advanced.
- The current AWS trust update needed for India runtime promotion is to allow `repo:qrm-dms/smp-tool:ref:refs/heads/dev-india` and `repo:qrm-dms/smp-tool:ref:refs/heads/qa-india` on the noprod role, and `repo:qrm-dms/smp-tool:ref:refs/heads/prod-india` on the prod role.
- A bare-minimum File Browser monitor was added to `smp-tool`: a scheduled/manual GitHub Actions workflow probes the Japan dev, QA, and prod `/filebrowser/` URLs on the internal `ubuntu` runner and checks for the unauthenticated `Login with Okta` page. It was first proven green, then reduced to a daily 09:00 Manila schedule.
- The File Browser monitor proves DNS, TLS, ingress, Airflow API-server reachability, and plugin login-page availability. It does not prove Okta login, authenticated browsing, mount readability, or downloads.
- July 16 `smp-dashboard` work added and promoted a manual CDH registration GitHub Actions workflow. It uses branch-to-environment mapping, explicit Japan/India region selection, environment approval for short-lived `CDH_TOKEN_ONESHOT`, and long-lived GitHub Tools credentials for installing `cdh-sdk`.
- The same CDH registration work later exposed a false-positive risk: `cdh-sdk 1.1.81` could submit schema detection while crawler-status refresh failed, so the workflow reported success even though Athena did not have the expected table. The local hardening made schema upload and crawler status terminal checks fail loudly, but production crawler reset still required CDH/platform support.
- July 17 notes requested a follow-up to improve `smp-dashboard` CDH registration: infer the target environment from the workflow branch instead of accepting a user-supplied branch, and pass the one-hour CDH token directly as a workflow input instead of storing it as an environment secret.
- July 17 technical-activities notes described a Grafana/Loki signups deployment blocked on IP registration before DNS and certificate requests. The notes also mention service-account work for SNS publishing, but a web-identity/STSS error persisted after the role was attached.
- The same meeting identified a runaway AWS Batch configuration: GMR compute environments had minimum CPU set to 1,200, causing more than 1,200 M3 medium EC2 instances to run continuously without CrowdStrike coverage. The minimum was reduced to zero during the meeting, and maximum vCPU limits still needed review across compute environments.
- The Prosumer simulation blockage was attributed to saturated shared AWS infrastructure capacity rather than an application-specific Prosumer failure. Reducing the AWS Batch minimum CPU was expected to relieve the capacity issue, but simulation recovery still needed verification.
- July 20 standup introduced Mateo as a beta tester for SMP India onboarding. The plan is to confirm his GitHub corporate license, grant `qrm-dms` and SMP India access, grant dashboard creation rights in dev, and use his friction to improve README/CONTRIBUTING and onboarding permissions.
- July 20 TA standup says the billing-ticket issue was not a billing-system defect: the customer's unexpected cost came from an accidental run of 1,000 instances for six days. The follow-up should clarify the manual-error explanation while the customer switches from hourly to fixed monthly/yearly billing display.
- The same TA standup says Pyrene work resumed after Nicola's issues from the prior week. Most issues were tied to File Manager, which was deployed separately from Pyrene and still needed integration. Abraham provided integration information, but end-to-end run status still needed confirmation.
- Model Runner migration status on July 20: Alfred had migrated EFS and images; database and file migration should occur when users cut over to production. The cutover plan is to scale up cluster instances rather than redeploy, and a new ADO pipeline pushes images to MS accounts with a separate promotion pipeline across accounts.
- Prosumer data migration was planned for 2026-07-21. Preparation required adding old Prosumer prod and DMS prod S3 buckets to an Azure admin role with `s3:GetObject` and `s3:ListBucket`, plus enabling cost-center tags for ABAC. A reset/delete-then-restore script using `s3 sync --delete` was created for the prod account.
- July 20 "Wallet Migration" notes say three SFF repositories had been migrated. Brian clarified on 2026-07-21 that the source phrase transcribed as `web-colon` means `web_common`, matching the broader Codex evidence for `user_ms_client`, `web_common`, and `user_microservice`.

## Open Questions

- UNCERTAIN: Whether SMP prod database should be a cluster or a separate database still needed confirmation in the June 22 notes.
- UNCERTAIN: Exact root cause of the Japan/India production proxy 403s was not established in the captured notes.
- UNCERTAIN: Who owns approval and rotation of the ENGIE root certificate despite its technical validation for GEMS access.
- UNCERTAIN: Whether the pending `smp-japan` native transfer was accepted after the July 12 capture.
- UNCERTAIN: Whether Pyrene UAT should be always-on or on-demand remains unresolved in migration notes.
- UNCERTAIN: The exact final remediation shape for user lookup permissions belongs to a follow-up technical discussion.
- UNCERTAIN: Whether `Kubic`, `Phoenix Worker`, and `qrmvms` are the exact names; the meeting source may contain transcription artifacts.
- UNCERTAIN: `Clickstart` still needs more context before the migration work can be interpreted confidently.
- UNCERTAIN: `Peer` may be a mistranscribed person name and needs more context.
- UNCERTAIN: Whether `Extruder` is the exact project/system name from the July 14 meeting capture.
- UNCERTAIN: Whether an unauthenticated `/filebrowser/health` endpoint or authenticated synthetic browse check is needed after the daily monitor has run for a while.
- UNCERTAIN: Who can update the AWS IAM trust policy for the new `qrm-dms/smp-tool` India deployment subjects.
- UNCERTAIN: Whether `smp-dashboard` should upgrade from `cdh-sdk 1.1.81` to `1.1.91` after the crawler-status workflow hardening.
- UNCERTAIN: Whether `STSS` is the exact service-account/web-identity error name from the July 17 technical-activities source.
- UNCERTAIN: Whether `ngloud` is the exact AMI/image family name behind the GMR CrowdStrike coverage issue.
- UNCERTAIN: Whether `Abstract`, `Bong`, `Milo`, and `Jeka` are exact names from the July 17 technical-activities source or transcript artifacts.
- UNCERTAIN: Whether `Nicola`, `Abraham`, `David`, `Pankaj`, and `Nick` are exact names from the July 20 TA standup.

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

Last Updated: 2026-07-21
