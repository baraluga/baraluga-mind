# Backlog Grooming

Source Type: Granola meeting notes
Meeting ID: `8475d145-a553-4051-99ed-8530f4346ae9`
Meeting Date/Time: Aug 11, 2026 2:30 PM GMT+8

## Known Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Capture Note

This capture preserves Granola-provided notes and summaries. It is not a verbatim transcript.

## Discussion Notes / Summary

### Sprint Context and Budget

- No confirmed budget and no formal sprint plan for the upcoming period
- Most tickets blocked, waiting on metadata or external inputs
- Sprint starts this week, two weeks duration

### Blocked Tickets

- New metadata ticket: blocked, relates to interconnector metadata
- Time series tickets (old dashboard): waiting on Louis's team to push to TSDB
  - Can pre-check whether providers already exist in TSDB
  - Identify provider owners and sync to enable proper data injection
  - Data injection itself needs careful scheduling to avoid disrupting dashboards
- Japan user access rights: blocked pending proof of concept from Material
- Reporting ticket: also waiting on metadata

### Technical Tasks Available

- Automated Docker image push and deployment pipeline trigger
  - Low priority, budget-dependent, but would improve Brian's workflow
- Graphene and other board backup: nice to have, not urgent
- Backlog cleanup planned for next period: remove obsolete tickets, start fresh

### Spike: Unexplored Airflow and Grafana Features

- Proposal to spike on out-of-the-box Airflow and Grafana features not currently used
  - Airflow "assets" feature: completely unexplored, potential low-hanging fruit
  - Grafana alerting: stakeholders currently check dashboards manually every day
    - Threshold-based alerts (e.g. power price triggers) could replace manual checks
  - Grafana monitoring views: worth mapping exactly what's available
- Output of spike feeds directly into the upcoming steering committee presentation
- Brian to share findings internally, possibly via the front-end/back-end chapter
  - No current channel for sharing project accomplishments since Advanced Analytics era

### Timeline and Next Steps

- Spike should be completed by next week (before the week of 24th-30th Aug, when the other speaker is on holiday)
- Friday morning catch-up: slide deck to be ready by then
- Steering committee meeting: 28th Aug, spike output used as a talking point
- Two tickets to be created: one for Grafana features, one for Airflow features

## Next Steps / Action Items Present In Granola

- **Complete Airflow and Grafana feature spike** (Brian)

  Cover unexplored assets, alerting, and monitoring features; output feeds the steering committee slide deck.
- **Have spike findings ready by Friday 21st August** (Brian)

  Needed before the other speaker's holiday (24th-30th Aug) so slides can be prepared for the 28th August steering committee.
- **Share spike discoveries in the relevant chapter (front-end/back-end or equivalent)** (Brian)

  Promote findings to a wider project audience, similar to recent AI accomplishment sharing in Applications.

Last Updated: 2026-08-11
