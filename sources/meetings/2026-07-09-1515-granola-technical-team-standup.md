# Granola Meeting Notes: Technical Team Standup

- Meeting ID: `48b4f1a2-557b-49f7-9249-1f9a5f10698c`
- Date: 2026-07-09 15:15 GMT+8
- Source type: meeting
- Source: Granola meeting notes
- Participants known to Granola: Brian Alexander Peralta

## Summary

### Walnut: ADO to GitHub Migration

- Decision: PR history is not required for migration; commit messages are sufficient.
- GitHub import UI includes commits and messages, but not PRs.
- ADO-to-GitHub extension supports PRs but requires migrator role.
- Consensus: not worth pursuing migrator role for PR history.
- ABT dashboard was migrated as a test case using GH CLI and AZ CLI without migrator role.
- Click migration should be coordinated with JB before migrating because security remediation is ongoing on the same repo.
- Risk: committing to a repo mid-migration creates leftovers.
- Plan: complete security remediation first, then migrate with Nika.

### AWS Migration: Pyrene and GMR

- CDK v6.5.1 was released and deployed to all environments: MS prod, NOP prod, Pyrene, and GMR.
- Bug found after deploy: project name suffix `dash-infra` was removed, but some roles still expect it.
- Root cause: compute environment creation fails without the correct project tag.
- Fix in progress: publish an unofficial artifact to test the correction.
- Alfred migrated the compute environment in Pyrene.
- EFS data recovery of 13 TB is in progress via S3 sync.
- Session was lost overnight after being kicked from pod shell; a detach/keep-alive mechanism is needed.
- Suggested speedup: increase S3 sync thread count to 16-20.
- UAT environment setup is underway and pending SSL certificate, to be handled today.
- Remaining work estimate: worst case end of next week, rough target Wednesday.
- GMR still needs EFS migration, expected to be lighter than Pyrene.
- Pyrene artifact publishing to Carver still needs confirmation; Confluence page exists.
- Post-migration: schedule half-day session with Abraham and Nico covering new software deployments and node group management.

### Security Remediation: Prosumer

- Two tickets are ready to close: vulnerable components and token in browser storage.
- CSP headers: public domain ticket is done; separate ticket was created for MS domain.
- Internal A/B: CSP cannot be a single policy across multiple domains and needs a solution.
- Remediation 5: user filter email endpoint was flagged.
- Endpoint currently returns full user info and allows pagination across all users.
- Current frontend logic stores and controls user permissions client-side; backend must enforce permissions.
- Proposal: restrict endpoint to self-query only and require minimum search query of 4-5 characters before listing users.
- For project sharing, use GuyID only; backend confirms the user exists.
- Broader fix is needed in the user microservice and affects all systems, not only Prosumer.
- Dedicated discussion should be scheduled with a subset of the team.
- July 13 go-live target is likely to move because items remain open.
- Security team will validate all items together, not ticket by ticket.

### Business Test Pipeline and Grafana Alerts

- Business test pipeline issue is resolved by correcting PyPI feed ordering: PyPI first, then SFF backend.
- Pipeline now runs via ADO on a separate branch; PR was shared in DevOps Prosumer chat.
- Teams notifications on test results are already firing.
- Unused S3 bucket in the business test stack should be removed.
- Deployment model clarified: Lloyd's team is autonomous for triggering business tests and promoting per environment; no automation will be added.
- Grafana APM alerts were created and tested by lowering the threshold.
- SMTP is not configured; plan is to use SNS topic instead, encrypted via common stack.
- One shared Teams channel was proposed for all alert notifications.
- Sentry setup is expected to begin after the meeting.

## Next Steps Captured

- Fix CDK compute environment role bug and redeploy. Owner: Brian.
- Publish unofficial artifact to test the `dash-infra` suffix correction before creating a PR.
- Resolve EFS S3 sync session drop and resume transfer using detach/keep-alive or Kubernetes job; consider 16-20 threads.
- Handle UAT SSL certificate request today.
- Schedule dedicated user microservice discussion with subset of team.
- Set up SNS topic for Grafana APM alerts using encrypted common stack and Teams channel subscriber; coordinate with Nilo.
- Message Lloyd about AWS ADO access. Owner: Brian.

Last Updated: 2026-07-09
