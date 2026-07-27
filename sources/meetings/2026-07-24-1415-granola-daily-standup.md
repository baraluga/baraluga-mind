# Daily Standup

Source type: Granola meeting notes

Meeting ID: `38fae024-caa4-44f3-a977-5e8489a4febf`

Meeting date/time: Jul 24, 2026 2:15 PM GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This is not a verbatim transcript. It preserves the available Granola-generated meeting summary and next steps.

## Discussion Notes

### Jira Access and Sprint Admin

- Brian has access issues with the newly migrated Jira.
  - Old email may lack Okta integration.
  - Pierre contacted; worst case, a new account is created and associated manually.
- Ticket 1206 moved to In Review and pulled into current sprint.

### TSDB Validation Progress

- 2Y dashboard, ticket 1202, confirmed as done.
  - Francois confirmed via Japan group chat that the 2Y dashboard looks fine.
  - Any operational follow-ups are outside ticket scope.
- TSDB validation script in progress.
  - Correct metadata retrieved from UAT catalog.
  - Data access request submitted, likely routed to Carlos.
  - Brian uses SMP INTAC client ID credentials, not personal access.
  - Access requested for the whole team, ng apart, no prod, for future debugging.
- SMP Japan repository link issue.
  - Repository appears archived post-migration, not redirecting correctly.
  - Brian to post the correct URLs.
  - Plan: create a DAG in SMP Japan as a test, validating both TSDB values and DAG creation process.
- Production path: once UAT data is doubly confirmed, same process repeated for prod.
  - Approval chain for TSDB changes still unclear; need to identify the right person beyond current UAT manager.

### Ticket 1058 (Darwin / Mateo)

- Root cause identified: a commit by Jean-Christophe around March/April broke Darwin without detection.
- Fix agreed; Mateo committed to doing the backfill.
- Still in review, no update yet; expecting response end of day or Monday.

### Ticket 1206 (Operational Capacity / Grafana)

- Working version built and tested on dev.
  - Manually ran daily capacity to verify operational capacity output and CDH exposure in Grafana.
- Merged to QA; now testing full time frame: yearly, monthly, weekly, daily.
- Still ongoing on QA.

### Iberia Presentation and Upcoming Grooming

- Iberia presentation delivered; reception was cautiously positive.
  - Feedback: current solution may not be the final solution; further investigation needed.
  - Potential client interest noted around editing scrapers.
- Japan client requests currently sparse; backlog items identified for upcoming sprints.
- Grooming session deferred to Tuesday evening, after Brian's call with India.
  - Monday standup will be lighter; Tuesday more effective for full grooming.

## Next Steps

- Post correct SMP Japan repository URLs (Brian).
  - Repository is archived post-migration and not redirecting; needed to unblock DAG creation and TSDB validation.
- Identify approval owner for TSDB production changes (Brian).
  - Current contact only manages UAT; need to find the right person before prod rollout.
- Continue operational capacity testing on QA (Brian).
  - Validate full time frame: yearly, monthly, weekly, daily, and Grafana mapping for ticket 1206.
- Await TSDB validation feedback and Mateo's update on ticket 1058.
  - Expecting TSDB access confirmation via Carlos and Darwin backfill status from Mateo by end of day or Monday 27th July.
- Grooming session on Tuesday evening.
  - Scheduled after Brian's call with India; Monday standup skipped for grooming.

Last Updated: 2026-07-24
