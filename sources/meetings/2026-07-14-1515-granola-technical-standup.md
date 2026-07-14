# Technical Standup

Source type: Granola meeting notes

Meeting ID: `d6dd08a5-a68f-4dda-9010-5418fb3972d8`

Meeting date/time: Jul 14, 2026 3:15 PM GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves available Granola notes/summaries. It is not a verbatim transcript.

## Discussion Notes / Summary

### SAP / QRMS Data Migration

- Remaining tasks can be planned post-go-live.
- Final solution architecture still unclear; to be discussed with Nilo.
- Go-live date to be confirmed today after the discussion.
- Data migration feasibility confirmed to Luke; date to be fixed.
- One blocker: access token to QRMS not yet authorized.
  - Peer already contacted to resolve this.
  - Once authorized, SMP India to QRMS migration can proceed safely.

### Wallet Migration and APM

- APM migration already complete.
- SNS infrastructure for APM done.
- Blocker: Grafana needs an AWS admin to create a role for CloudWatch/publish access.
  - No one currently has admin access to the relevant AWS account or Kubernetes service account.
  - Need to confirm whether a role is being used.
  - Coordination needed: anyone with AWS admin access to assist.

### Open Blockers

- AWS admin access for Grafana role creation for APM/Grafana.
- QRMS access token authorization for SAP/SMP India migration.

### Process Improvement for Next Meeting

- Proposal: raise decision points and blockers upfront before project updates.
  - Allows Nilo, Guido, and others to address needs early.
- Shorten status updates to leave time for discussion.
- Discussions and follow-ups to happen after structured updates.

## Next Steps / Action Items Present in Granola

- Confirm go-live date after today's discussion.
  - Commitment made to Luke that migration feasibility would be confirmed by today.
- Follow up with Peer on QRMS access token authorization.
  - Required before SMP India to QRMS migration can proceed.
- Identify AWS admin to create Grafana role.
  - Needed to grant Grafana access to publish; no current admin identified on the team.

Last Updated: 2026-07-14
