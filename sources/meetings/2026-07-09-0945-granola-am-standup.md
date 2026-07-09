# Granola Meeting Notes: AM Standup

- Meeting ID: `b470e224-f0eb-4d99-9c88-e8d44f69ccf2`
- Date: 2026-07-09 09:45 GMT+8
- Source type: meeting
- Source: Granola meeting notes
- Participants known to Granola: Brian Alexander Peralta

## Summary

### Team Announcements

- Feedback reminder: review the Excel file and provide feedback to those who opted in.
- Cupcake ceremony is tomorrow after lunch, around 1:00 or 1:30 PM.
- Budget covers cakes and sweets; attendees should bring coffee or use office vending machines.

### SMP and Airflow Updates

- SMP separation and upper image per region are in progress.
- Airflow version update is needed; FastAPI navigation is pending.
- OTV and flip image builds/pushes are in progress.
- There are issues around proxy behavior, target URLs, access, and error messages/logs.
- Phoenix was mentioned around 5 PM onward.
- Ticket cleanup:
  - 1087: unblocked, cleanup in progress.
  - 1181/1100: email list update.
  - 1102: same status, so far so good.
  - 1169: QA readiness, Peralta emergency production, deep synchronization SMP Japan prod.
  - 1197: working version from 2019, lookback dashboard.
  - 1198: data export.
  - 1186: set to be validated by Myel.

### S3 Design and SF Access

- S3 model design is underway; implementation is continuing.
- SF/Salesforce environment usage was encouraged for visibility.
- Access is not required per repository ID.
- Brian requested Maintainer access in Auto.

### Migration and Repository Access

- Migrator role discussion covered migrating PRs from ADO to GitHub.
- Extensive migration includes history, the repository, and pipeline.
- Migrator role does not cover repository migration by default.
- Bulk migration of pipelines was suggested as an option.
- Team principle: understand the manual UI process before automating.
- Peralta was noted as owner with org-level access; personal vs. org repo distinction was clarified.

## Next Steps Captured

- Validate ticket 1186. Owner: Myel.
- Request Maintainer access in Auto for Brian.
- Document the manual migrator process via UI before automating.

Last Updated: 2026-07-09
