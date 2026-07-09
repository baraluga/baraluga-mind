# AWS Migration Standup?

Source type: Granola meeting notes

Meeting ID: `a46157a7-a35f-4eda-b1fb-8492caef1e5b`

Meeting date/time: 2026-07-08 15:14 GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This is not a verbatim transcript. It preserves the available Granola meeting notes/summaries.

## Discussion Notes / Summary

### Board and Ticket Visibility

- New board structure introduced to centralize all technical activities.
- AWS migration, walnut migration, security remediation each get their own epic.
- Subtasks added per project: APM, walnut, security for Click/Prosumer.
- Charging will be per project, not a blanket "technical activities" bucket.
- Walnut migration: Bong still finalizing requirements; overall status tracked in a separate Excel because 35 repos are too many for individual tickets.

### AWS Migration: Pyrine and GMR

- EFS backup confirmed: new DMS account has default backup in place.
- 35-day warm backup, daily incremental.
- Estimated cost for Pyrine, about 13 TB, is $600-700/month, well under threshold.
- S3 sync started to copy Pyrine prod bucket and seed EFS volume in new account.
- UAT vs. pre-prod environment naming dispute involving Nicola vs. team standard.
- Concern: Pyrine is resource-heavy; a single machine runs about $2,000/month.
- Need to clarify scope and whether environment needs to be always-on or on-demand.
- To be clarified with Nicola separately.
- Stage tag cleanup: consensus to remove the stage tag rather than just fix capitalization.
- Environment tag already used by ING; stage appears unused in Lambda functions.
- Environment variables for Lambdas are separate and unaffected.
- Walnut runner in new GitHub org still blocking automated Docker image build.
- TLS certificate trust for GEMS artifact registry not set up correctly.
- Need to check with Nilo or Guido on whether cert is in scope for the team.

### SMP Platform and Next Sprint Priorities

- Interconnector dashboard nearly complete; a few detail tickets remain, including ticket 97 for time series view and accepted data exports.
- Brian to confirm with her whether existing export feature is sufficient once current dashboard is finalized.
- Adaptable Y axis ticket closed: user accepted auto-adjusted scale as-is.
- User account management, ticket 1172: meeting tomorrow with Jim to configure access rights.
- Goal: end user can create a DAG, connect to data sources, use SMP command library, and build a dashboard end-to-end.
- Target: India user access and detailed training ready next sprint; Matteo to be invited.
- Grafana backup: consensus to back up the full database, not just dashboard JSON exports.
- Grafana likely uses MySQL or Postgres; option to connect to existing RDS using same approach as Airflow.
- Brian to investigate Grafana's database type and backup approach.
- Airflow version alignment, India and Japan: remove dependencies tied to DAGs no longer in production; update remaining DAGs to latest where possible.
- Synapse integration: demo requested to evaluate fit before committing.
- Next sprint focus: finish interconnector dashboard, advance user empowerment, TSDB tickets and user account management to be refined after tomorrow's meeting.

## Next Steps / Action Items From Granola

- Confirm with her whether existing data export feature is sufficient (Brian). Do this once the current dashboard is finalized.
- Check with Nilo or Guido on TLS certificate for GEMS artifact registry. Determine if the cert is in the team's scope or needs to be handled externally.
- Investigate Grafana database type and backup strategy (Brian). Confirm if MySQL/Postgres is used; evaluate connecting to RDS for automated backup.
- Clarify Pyrine UAT environment scope with Nicola. Determine if always-on is needed or if on-demand is sufficient given about $2,000/month per machine.
- Sync Pyrine and GMR tickets to Dale's board. Planned for tomorrow; use Robo to transfer quickly.

Last Updated: 2026-07-09
