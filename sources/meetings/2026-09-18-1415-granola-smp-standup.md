# Granola Capture: SMP Standup

- Date: 2026-09-18 14:15 GMT+8
- Source: Granola
- Meeting ID: `816398d7-71ee-4c89-a516-2737045896d8`
- Title: SMP Standup
- Known participants:
  - Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

# Sprint Status

- Ticket 1229: in production but validation is tricky
  - No dashboard or TSDB publishing expected by S&P India
  - Validation approach: check data format and spot-check data points in CDH
- Grafana native alerts: working in QA, safe to push to production this sprint
  - Alerts fire twice: once on threshold breach, once on recovery
  - Programmatically created alerts are read-only in UI; end-user UI-created alerts work normally
  - Confluence page drafted on how to set up alerts as an end user
- Ticket J59: sent for validation; Mateo approved but requested Kava 1-minute backfill
  - New common backfill implementation published to SMP Common
  - Michael asked to deploy to all environments across both regions
- Kava DAGs (India): 300+ failed runs in prod due to missing file, DAG retrying every 5 minutes
  - Exponential backoff implemented, capping at 15 minutes
  - Concern raised: a single missed file immediately triggers the 15-minute delay, losing ~10 minutes of availability
  - Preferred approach: switch to 15-minute interval only after 5 consecutive failures, then trigger reconciliation and revert to 5-minute schedule once file returns
  - Known data gap issue: delayed CSV files don't recover gracefully; 2-hour delay = 2-hour hole in data
  - CSV file size variance (1.3-1.7 MB) confirms missing data in some files
  - Mateo to be informed of the backoff strategy and its implications
- Ticket 1260: in review, pending one QA validation test in progress
- Ticket 1243 (Bidstack India dashboard): data shape already validated in CDH last sprint; dashboard creation remaining
  - Bidstack data goes to both CDH and TSDB; TSDB time series not yet ready (lower priority)
- Ticket 507: automate Airflow Docker image build and push; currently manual, only Joyce or Michael can do it
  - Brian to sort out next week

# Kava Near-Real-Time Data and Airflow Fit

- Darwin request: data upload to TSDB every minute
- Airflow minimum interval is 5 minutes, raising a question about whether it's the right tool
- Mateo clarified: 1-minute granularity is not a hard requirement
  - What matters is capturing every minute of data within each 5-minute run window
  - No need for data to appear in Grafana/TSDB in real time
- Airflow remains viable for now, but worth exploring TSDB golden layer or alternative solutions
- If Airflow genuinely can't meet the need, the team's responsibility is to redirect to a better-fit tool or team

# Org, Access, and Upcoming Milestones

- Francois-Xavier departing for FlexHub; replacement and team reshuffling not yet finalized
- Brian flagged as a potential dedicated product owner for SMP (covering India, Singapore, Japan)
  - Needs to be discussed with Brian directly; salary adjustment would need to be negotiated separately
- Steering committee: Francois to schedule for the week of 12-18 October (before period end on 21st October)
  - Goal: avoid the budget accountability lag that occurred last time
- Michael not yet fully on SMP; expected full onboarding by first week of October (still finishing migration work)
- Grid India access via Zscaler VPN not working in Paris or ETB; Airflow also lacks access
  - Two actions needed: enable proxy in SMP (done before for Singapore), and enable local PC access
  - Michael asked to set up a call with Nilo, who implemented the Singapore proxy
  - Call to be scheduled Monday or Tuesday next week
- Long-running scripts: consider running in the cluster or as a microservice called by Airflow, rather than inside Airflow directly

# Next Steps

- Validate ticket 1229 via CDH data check
  - Confirm format and spot-check a few data points manually; no dashboard or TSDB output expected.
- Align with Mateo on Kava backoff strategy
  - Discuss failure threshold, for example 5 consecutive failures, before switching to 15-minute interval, and confirm reconciliation behavior on file recovery.
- Automate Airflow Docker image build and push (Brian)
  - Currently manual and restricted to Joyce or Michael; address first thing next week.
- Schedule call with Nilo on Grid India proxy access
  - Target Monday or Tuesday; cover both SMP proxy enablement and local PC access setup.
- Schedule steering committee for week of 12th-18th October (Francois)
  - Before period end on 21st October to avoid budget accountability lag.

Last Updated: 2026-09-19
