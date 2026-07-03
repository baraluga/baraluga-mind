# Sprint Planning

Source type: Granola meeting notes
Meeting ID: `e0d3be9b-e99f-4895-84f2-3742074d5b66`
Date: 2026-07-02 11:00 GMT+8
Participants known to Granola: Brian Alexander Peralta

Note: This is from Granola notes/summaries, not a verbatim transcript.

## Discussed

- Ticket 10-87 was in progress, with cleanup remaining for grid credentials and Kubernetes commit.
- Proxy error was treated as an incident symptom, not root cause.
- Actual fix was tied to network/time changes starting June 26, tracked under a separate monitoring ticket.
- ServiceNow incident ticket fields discussed: affected service, symptom, and dropdown incident link.
- MS Teams alerting currently sends email alerts through an API; 403s cause alert failures.
- Proposed alerting fix: on any request error, send email directly.
- Proposed retry/noise control: suppress repeat alerts for about 5 days and cap alerts around 3 per day.
- User access and permission scope needed clarification for Airflow/dashboard roles.
- Roles discussed: admin, developer, viewer/editor, producer.
- Secrets handling options included Airflow variables, Kubernetes secrets, and AWS Secrets Manager.
- Branch protection and CI pipeline setup were discussed, with basic automated tests required before merging to prod.
- Grafana dashboard backup would export JSON config to SharePoint; versions 1-9 still need export.
- JupyterLab multi-environment spike discussed proxy/domain issues in India.

## Next Steps

- Create ServiceNow incident ticket with correct affected service and symptom fields.
- Brian to implement email fallback on 403 or any request error in the MS Teams alert script.
- Define and document Airflow user roles and permissions.
- Draft Confluence page on secrets management decision flow.
- Set up automated daily dashboard JSON export to SharePoint.

Last Updated: 2026-07-04
