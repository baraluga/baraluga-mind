# SMP Standup

- Source: Granola
- Meeting ID: `57547ecf-18b0-4274-90a6-f9627df203a6`
- Date: 2026-09-30 14:15 Asia/Manila
- URL: https://notes.granola.ai/d/57547ecf-18b0-4274-90a6-f9627df203a6
- Captured by: Brian Alexander Peralta

## Summary

### Darwin Integration Progress

- Darwin ticket unblocked: machine-to-machine credentials obtained and tested locally
- Michael asked to deploy to dev cluster (India); expected within the day
- Once deployed, DAG will be enabled on dev to pull values from EFS and publish to TSDB
- Architecture decision: publishing to TSDB kept strictly in Airflow
  - Rejected direct collector-service-to-Grafana path
  - Avoids maintaining two sets of credentials across Airflow and cluster level
  - Microservices are less monitored, so keeping it in Airflow is safer
- Grafana data is 5 minutes behind real time (DAG frequency: 5 min), confirmed acceptable

### Darwin Validation (Production Bug Fix)

- Fix submitted for validation; Matteo confirmed everything looks good on his end
- Validation criteria: TSDB values from July 8th to present
- Fix pushed directly to production (production bug)
- 403 error on TSDB UAT when writing data
  - Catalog access works fine; data access returns 403
  - Using APAC TSDB scraper credentials from AWS Secrets, no config changes made
  - Confirming with Matteo whether fix also needs to be pushed to UAT
- Validation for ticket 1264 (Kaba real-time) to be done on prod, not UAT

### Kaba / CDH Cross-Region Access

- CDH support made a change on their end (SCP security config) to allow cross-region access
- Verified access via console; yet to confirm in Airflow QA
- Plan: re-enable Kaba DAGs in QA, confirm no errors, then backfill from point of lost contact
- Goal: re-establish TSDB UAT data for Kaba

### GitHub Pipeline and Automated Deployment

- Michael started requesting roles needed for GitHub pipeline
  - Will enable automated image deployment for Airflow and Grafana
  - Currently deploying manually (same approach used for Darwin API)
- Once roles are granted, pipeline setup expected to be straightforward
- Update expected from Michael tomorrow (1st October)

### Backlog and Upcoming

- Backlog grooming at 09:30 (03:30 local)
  - No new items following discussion with Matthew; nothing changed since last week
  - May not need the full session; plan to refine top-of-backlog items
- Darwin sites: contact Matthew and Andrea to define remaining Darwin-linked tickets for the backlog
  - 6-7 additional sites to onboard beyond current work
- Japan contact: follow up with new Japan contact who hasn't responded yet

### Next Steps

- **Re-enable Kaba DAGs in Airflow QA and verify cross-region access** (Brian)

  CDH confirmed the SCP fix on their end; backfill TSDB UAT from point of lost contact once confirmed.
- **Confirm with Matteo whether Darwin fix needs to be pushed to UAT** (Brian)

  403 errors on TSDB UAT are blocking; production fix is already in place.
- **Contact Matthew and Andrea to define Darwin site tickets**

  6-7 additional sites need to be scoped and added to the backlog in a defined way for the next sprint.
- **Follow up with new Japan contact to schedule a meeting**

  No response received yet.

Last Updated: 2026-10-01
