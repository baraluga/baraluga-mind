# Morning Standup

- Source: Granola
- Meeting ID: `512eacf3-ba6e-4f63-88ee-00e5a8499361`
- Date: 2026-09-30 09:45 Asia/Manila
- URL: https://notes.granola.ai/d/512eacf3-ba6e-4f63-88ee-00e5a8499361
- Captured by: Brian Alexander Peralta

## Summary

### Team Updates and Reminders

- Jelena/Dale absent today
- End-of-month reminder: Q3 closes today (30th September 2026)
  - Projected inputs were entered on the 19th; actuals now due
- NGME survey sent out: annual, ~10-15 minutes
- Michael: SMB work starts tomorrow
  - At least 80% SMB focus, 20% walnut migration

### Brian's Updates

- 3 backlog points completed; sending for validation
  - Checking with Mateo to set tickets to "done" on his end
- C1265 bug: failure occurred Monday in Sakaba, self-resolved
  - Double-checking stability in prod; upstream reliability is inconsistent, causing occasional delays
- Darwin unblocked
  - Client ID and client secret ready
  - Needs Michael's help for a short deploy to Airflow dev cluster

### Michael's Updates

- SMB: creating a reusable role for pipeline automation and mapping
- Prosumer pipeline blocked by permission error
  - Messaged Alfred; Alfred is clarifying workflow agreement
  - Alfred to update the role; may improve the pipeline push/backend flow
- Iteration migration plan in progress; some Prosumer pipelines already converted
- IT admin ticket note: communication on roles and permissions needs clear ownership
  - If an agreement issue can't be handled, escalate to other IT admins rather than letting it stall
  - Other Prosumer pipelines can still be attempted while the blocked one is resolved

### General and Infrastructure

- General cleanup and organization ongoing
- Deployment planned for 5/6
- Screen documentation in progress; shared resources to be updated
- Grafana credentials setup underway
- Documentation being maintained synchronously with infra files
- Script conversion in progress (without natural language support due to bugs)

### Next Steps

- **Validate completed backlog points and confirm done status with Mateo** (Brian)

  Send for validation and check Mateo's end to mark tickets done.
- **Double-check Sakaba stability in prod** (Brian)

  Bug self-resolved but upstream reliability is inconsistent.
- **Coordinate Darwin deployment to Airflow dev cluster** (Brian, Michael)

  Client ID and secret are ready; needs a short deploy with Michael's help.
- **Update Grafana credentials and push documentation**

  Credentials setup in progress; sync with infra files once complete.

Last Updated: 2026-10-01
