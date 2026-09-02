# Granola Capture: Daily Standup

Date: 2026-09-02 09:45 GMT+8
Source: Granola
Meeting ID: `a731f410-6189-4bb3-b12d-d8a63758159e`

## Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Notes

# AI Ventures Training Announcement

- New registration open until 15th September
- 12 sessions, every other Friday starting October
- Covers beginner and advanced levels
- AI being actively pushed by the company

# Brian's Updates (SMP)

- JIRA 1215: in review, waiting on execution, DAG/Airflow running under 12 hours
- JIRA 1237: pending validation, checked 1238, status good
- JIRA 31: ongoing testing, summer goal to have at least one POC completed
- Phoenix item: peer reviewed and approved months ago, pending merge signal to fraud and map deploy
  - Two options presented: skip security audit and deploy to all environments, or wait for security graduation
  - Fix is mainly a matter of syncing across all environments

# Michael/Florence: Migration and Pipeline

- DMX and GitHub pipeline clarification done, no backend scene changes
- Habanero migration pipeline reviewed
- Artifactory decision: adding genetic/generic repository
- Azure installation clarification for later; pipeline conversion for today
- Feeder market pipeline dependency noted as low priority
- Priority triage in progress: low, medium, high items being sorted

# Kubernetes and Signups

- Current production version: 1.34, Kubernetes 1.35 confirmed to proceed
- Local get-mirror task and PowerPoint for later presentation in progress
- Test signup screen deployed yesterday; some deployments still pending
- Node/availability zone mismatch issue flagged, fix in progress
- Pirate monitoring: manual dashboard planned for future
- ICA confirmation with Alfred needed for prod deployment of signups
- Onboarding discussion for signups: confirming who can take on the work

# Next Steps

- **Register for AI Ventures training before 15th September**

  Open to beginner and advanced attendees; company is actively pushing AI adoption.
- **Decide on security audit path for Phoenix deploy**

  Either skip audit and deploy to all environments now, or wait for security graduation.
- **Confirm prod deployment of signups with Alfred**

  ICA confirmation needed before proceeding to production.
- **Resolve node/availability zone mismatch**

  Part of a broader cluster monitoring report; waiting on resolution.

Last Updated: 2026-09-02
