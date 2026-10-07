# Granola Capture: Morning Standup

Source Type: meeting
Meeting Date: 2026-10-07 09:45 Asia/Manila
Granola URL: https://notes.granola.ai/d/85382101-ce2a-4dce-8e0c-4952d7b0e24f
Granola Meeting ID: 85382101-ce2a-4dce-8e0c-4952d7b0e24f
Captured By: Brian Alexander Peralta

## Participants

- Brian Alexander Peralta

## Granola Summary

### AI Credits Request Process

- Email Fred and the speaker first, explaining:
  - New business need.
  - Current AI usage in workflow, to assess overuse, underuse, or misuse.
  - Planned use of additional credits.
- After email, submit a ticket to increase credits.
- Angie and one other person already completed this; one unresolved case may be a system error.

### Sprint Review

- No changes to sprint backlog; 1-4 point tickets not yet validated.
- Grafana alerts via Teams channel spike: marked done.
  - François had a pending question about Jira versus Microsoft Teams integration option.
  - Clarified: posting to Microsoft Teams via email is the goal and already proven; unrelated to ticket scope.
- Backlog grooming needed for:
  - Observability stack tickets.
  - Ungroomed tickets.
  - Blocked tickets, such as India grid data.
- Jack consulted on observability stack: advising on resolution and setup order.

### Darwin API / IT Issue

- Darwin API provided by IT is reportedly not available.
- IT ticket marked done despite issue being unresolved and flagged as "legacy".
- Mateo and another Darwin contact are both out of office; no reply to clarification message.
- Root cause unclear: possible Swagger misconfiguration or IT/Darwin miscommunication.
- Escalating to Gregory for follow-up.

### Documentation and Infrastructure Updates

- Documentation reorganized; DAG bundle details still insufficient in infra docs.
- Eric's file has 90+ differences and needs cross-checking.
- Intac access: planning read-only group access, applied to all environments.
- Subfile configuration updated but not deployed to production; database not yet updated.
  - Will confirm whether to push changes to 6-7 before proceeding.
- Dev 3 duplicate number bug fixed; not in original image but communicated.
- Shared config docs updated for dev 4-6; pre-prod value for active runs per DAG should be 1, not 16.
- Grafana GitHub access request submitted for Ashum Narul; no update yet, follow-up planned.
- Airflow upgrade deployment check noted.
- Alert Manager: Pharma Library in signups flagged for review.

### Next Steps

- Follow up with Darwin team on API availability.
  - Mateo and Darwin contact are out of office; escalate to Gregory if no response.
- Confirm and push subfile config changes to production.
  - Confirm with team before pushing changes to 6-7; database not yet updated in production.
- Follow up on Grafana GitHub access for Ashum Narul.
  - No update yet; check in if access is not created soon.
- Cross-check Eric's infra documentation file.
  - 90+ differences noted; verify what is current versus what is missing for DAG bundles.

Last Updated: 2026-10-08
