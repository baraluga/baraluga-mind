# Technical Activities

## Current State

Non-SMP projects that came up in technical-activities standups, the tech-lead roundtable, and weekly team meetings. These are captured only in passing, so each line is the last known state with its date, not a tracked status. Moved out of [[smp-platform]] on 2026-10-11. See also [[team-operations]] and [[sff-walnut-migration]].

- **Pyrene** (2026-07-24): UAT deployed on 2026-07-13. File Manager still needed integration. An EKS update Snow ticket for weekday cluster scheduling and pod labels had stalled.
- **GMR / Model Runner** (2026-07-24): EFS and images migrated by [[alfred-villalva]]; the final migration was tentatively the following week. Cutover means scaling up cluster instances, not redeploying. On 2026-07-17 a GMR compute environment with minimum CPU 1,200 was running more than 1,200 EC2 instances without CrowdStrike; it was reduced to zero. Maximum vCPU limits still needed review.
- **Prosumer** (2026-07-20): backend authorization fixes for user lookup/sharing were incomplete; the frontend-controlled permission model was called insufficient. Data migration was planned for 2026-07-21.
- **CrowdStrike** (2026-09-17/22): ephemeral machines (ARM, Prosumer, GMR) lacked port 8080 to the proxy; Nilo was to add it. A separate issue traced to the customer ID pointing to the US tenant instead of Europe, still to be reconfirmed.
- **Lambda VPC binding** (2026-09-17): several no-prod Lambdas, including Extruder and The Click, are deployed without VPC binding. Not urgent; a report is wanted.
- **DayClick** (2026-09-17): production domain `declick.myengi.com`, pending NGIT DNS and DigiCert. UNCERTAIN: exact names.
- **Omniland** (2026-09-17): moving to ECR publication via an ADO-to-GitHub pipeline, EventBridge, and Step Functions. Moving to a backend-for-frontend auth pattern after a pentest.
- **Onset Energy** (2026-09-17): green-lit. Angular, FastAPI, CDK, serverless, with a DNV integration.
- **Kiba MCP and MCP servers** (2026-09-17/22): Kiba MCP stores no data; users supply keys at runtime. 2 of 5 MCP servers were deployed by 2026-09-15, with governance unsettled.
- **Consumer backend** (2026-09-22): migrated to GitHub; integration testing blocked on front-end/back-end integration. [[michael]] was waiting on Artifactory and the Sabina team.
- **ABS-CBS TSDB** (2026-09-22): production approval blocked until TSDB metadata is pre-created.
- **DB instance / GMR pipelines** (2026-09-22): pipeline deploys blocked by an Artifactory dependency. A Bastion Prod workaround was in use.

## Open Questions

- UNCERTAIN: Many names here (`Extruder`, `The Click`, `Clickstart`, `Kubic`, `Sabina`, `coins`, `ABS-CBS`, `ATAS`) come from meeting transcription and are unconfirmed.

## Sources

Main sources are below. The full trail from before the 2026-10-11 split is on [[smp-platform]].

- `sources/meetings/2026-07-09-1515-granola-technical-team-standup.md`
- `sources/meetings/2026-07-13-1515-granola-technical-activities-standup.md`
- `sources/meetings/2026-07-14-1515-granola-technical-standup.md`
- `sources/meetings/2026-07-17-1600-granola-technical-activities.md`
- `sources/meetings/2026-07-20-1645-granola-ta-standup.md`
- `sources/meetings/2026-07-24-1515-granola-technical-standup.md`
- `sources/meetings/2026-09-15-weekly-team-meeting.md`
- `sources/meetings/2026-09-17-1700-granola-tech-lead-roundtable.md`
- `sources/meetings/2026-09-22-0945-granola-weekly-team-meeting.md`

Last Updated: 2026-10-11
