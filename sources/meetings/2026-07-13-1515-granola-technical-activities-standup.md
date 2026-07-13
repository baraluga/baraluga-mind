# Technical Activities Standup

Source type: Granola meeting notes

Meeting ID: `e7283719-71c5-4ce6-843b-67b958168718`

Meeting date/time: Jul 13, 2026 3:15 PM GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves the available Granola notes and AI-generated summary. It is not a verbatim transcript.

## Discussion Notes / Summary

### GMR / Pyrin Deployments

- Pyrin: UAT environment already deployed.
- JMR: high worker removed, per request, because only default and low workers are needed.
  - Model runner Kubic web image updated to v3.8.5.
  - Repository configs and files for high worker cleaned up to prevent redeployment.
  - Alfred ran migration script to recreate all compute environments for production.
- Next for JMR: waiting on Alfred's task, Nikola's request from last week.
  - If no instruction comes, moving to deck leak deployment.

### AWS Role Cleanup

- Current pipeline uses an overly permissive AWS role with wide-open permissions.
- Plan: create a scoped replacement role for the model runner pipeline.
  - Script does not support this fully, but trust policy can be updated manually.
  - Tool to auto-generate roles already in progress.
- Approach: make dev work first, then replicate permissions to prod account.

### Pod Resource Allocation Issues

- Nikola sent updated resource requirements for high worker and Phoenix worker.
- Phoenix worker requirements are very high: 100 GB minimum, 220 GB memory.
- Dev and UAT both deployed, causing resource allocation conflicts.
- Open questions for Nikola:
  - Are dev and UAT requirements the same?
  - Should UAT be scaled down?
- Prod environment is available; Nikola can be asked to check it.
- Recommendation: confirm dev is fully working before configuring other environments.
  - Need to define exact machine counts and memory per environment before adding node groups.
  - 188 GB machines per environment flagged as potentially very expensive.

### Prosumer Remediation

- Items 6 and 87: security headers applied to public domain; still investigating project-specific headers for internal domain.
  - Plan to schedule a working session to proceed together.
- Item 5: user microservice endpoint update checked out but not yet tested; discussion with Nico planned.
- Item 4.2: sensitive content concern was about training videos on the Prosumer homepage, not the bull-proof page.
  - Agreed with Loic: training section protected by authentication, rest left open as a landing page for unauthenticated users.
  - If doubts remain, schedule a session to decide approach.
- Spike items: some partially done; remaining items still under discussion and investigation.
- Prosumer live schedule moved due to incomplete spike items.

### Walnut Migration and Brian's Update

- APM migration to Walnut: done, moving to validated/done status.
- SNS tasks for Grafana alerts: stack created, testing in progress; Sentry for APL is next.
- Brian added a composite action for certificate installation for gems/Artifactory.
  - Uses the public certificate found in Confluence.
  - Reusable across other pipelines to avoid code duplication.
  - SMP Japan migrated this morning and working.
  - SMP India: on hold, Francois still working on prerequisites.
- Blocker for SMP Japan: functional user `npm/nprm68` needs to be accepted into the `qrmvms` org.
  - Bong already sent the request; pending approval from any org owner.

## Next Steps / Action Items Present in Granola

- Coordinate with Nikola on pod resource requirements.
  - Clarify whether dev and UAT need the same specs, and whether UAT should be scaled down before adding node groups.
- Approve functional user `nprm68` into `qrmvms` org.
  - Bong has sent the request; an org owner needs to approve to unblock SMP Japan.
- Schedule working session on Prosumer security headers, items 6 and 87.
  - Investigate project-specific headers for the internal domain together.
- Test user microservice endpoint update.
  - Implementation PR exists but untested; discussion with Nico also planned.

Last Updated: 2026-07-13
