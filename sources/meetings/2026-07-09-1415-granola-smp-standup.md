# Granola Meeting Notes: SMP Standup

- Meeting ID: `a51b5ec9-76fd-4850-8f33-970682ed12df`
- Date: 2026-07-09 14:15 GMT+8
- Source type: meeting
- Source: Granola meeting notes
- Participants known to Granola: Brian Alexander Peralta

## Summary

### Airflow Upgrade: SCR 1191

- Docker image build is still in progress.
- It is uncertain whether the slow build is caused by local internet.

### SMP Japan Validation

- Production merge is blocked because Git repo sync is not yet updated and SCR 1087 cleanup is pending.
- Data backfill is complete for JPX and capacity from 2019; actual flow is available for 2025 only.
- Hiromi is investigating the download path for actual flow FY2019-2024.
- Historical lookback is implemented: it takes the latest snapshot at 11:30 PM JST and copies reconciled capacity to a new CDH dataset.
- Historical lookback is working in Grafana and awaiting Japan team feedback.
- SCR 1198 export best case is an existing Grafana export; Excel template complexity is still TBD.
- Message to the Japan group chat is pending for Hiromi and two others, covering dashboard review and export confirmation.

### Proxy Fix and QA DAG Failures

- Proxy handler fix was deployed by Oliver around 5 PM.
- No proxy errors have appeared since the fix.
- Root cause: access control filter used the wrong network mask and filtered by destination IP.
- Ticket was validated and moved to done.
- Some DAGs are still failing in QA Japan, but logs appear clean with no visible error.
- Suspected cause is memory pressure from parallel backfill runs.
- Plan: check Prometheus for cluster state and assess memory reservation for the namespace.
- No-product cluster is in use with three stages; both memory limit and reservation may need increasing.
- Feedback is expected tomorrow.

### SCR 1181 Email List Fix

- Francois is not receiving emails because he is missing from the email list.
- Brian needs to add Francois to both dev and QA email lists immediately after standup.

### SCR 11102 and Jupiter Integration

- No progress yesterday.
- PR should be raised after the call for review.
- Jupiter integration demo is scheduled tomorrow; integration plan will follow.
- A separate technical discussion is needed after the demo.

### TSDB Data Plan

- Agreement with Carlos: send reconciled interconnector capacity view to TSDB.
- Four time-series inserts per interconnector.
- Catalog is being built in Excel for Carlos to consolidate.
- Carlos is co-owner of the provider; time-series IDs are expected to be created next sprint.

### Incident Ticket Process Reminder

- Do not assign incidents to the SMP team.
- Leave category and subcategory fields blank when creating tickets.
- Filling category causes the proxy to disappear from the ticket view.

## Next Steps Captured

- Add Francois to dev and QA email lists for SCR 1181. Owner: Brian.
- Send Japan group chat message on dashboard review, historical lookback feedback, and SCR 1198 export confirmation. Owner: Brian.
- Raise PR for SCR 11102.
- Check Prometheus and report on cluster memory; feedback due tomorrow.

Last Updated: 2026-07-09
