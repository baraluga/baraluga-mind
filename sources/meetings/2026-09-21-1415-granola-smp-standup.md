# Granola Capture: SMP standup

- Date: 2026-09-21 14:15 GMT+8
- Source: Granola
- Meeting ID: `b7f380d8-d31a-4b28-a0c0-b9dfb3d21001`
- Title: SMP standup
- Known participants:
  - Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

# Grafana Alerting POC (Ticket 1260)

- Dev environment has a config issue; QA-only config suspected as root cause
- Francois to retest on QA after the call
- POC done in QA only, which is acceptable for now
  - If alerting is approved, will need to backpropagate config to dev

# Push Coverage Generation and TSDB UAT Alignment

- Production (TSDB) side done correctly; UAT has no data for the relevant time series
- Francois recommends deploying to TSDB UAT before validating, to respect staging practices
- Brian to double-check with Matteo whether UAT time series were created
  - Kavda's push generation prediction visible on UAT, so likely done, but needs confirmation
- No separate ticket for alignment; Brian to set current ticket to in progress

# Darwin API Integration (Ticket 1261)

- Brian has partial Okta access to Darwin; machine-to-machine auth still pending via Matteo
- Three integration options narrowed down, to be discussed later in the afternoon:
  1. Prometheus (concern: managing two TSDB systems, unclear ownership, no clear push path to TSDB)
  2. Airflow (previously discussed last Friday)
  3. Dedicated Python service within the cluster, polling Darwin API every minute, with a DAG pushing to TSDB via Airflow (Brian's preferred option)
- TSDB golden layer clarified as read-only; not viable for writing

# Sprint and Upcoming Events

- Kavda (1243): simple, data already available, just needs display work
- 1159: TSW80 to be enabled as soon as possible
- 507: low risk if not completed; not stakeholder-critical for sprint review
- Sprint review on Wednesday; sprint planning on Thursday
  - Review content to be discussed in tomorrow's daily to allow prep time
- Matteo likely unavailable today (visiting South India); Francois moved his sync with Matteo to tomorrow
- Steering committee to be scheduled before 21st October, with new stakeholder included
- Call with Neil later today: 5 PM Philippines time, ~11 AM Brian's time

# Next Steps

- **Confirm TSDB UAT time series creation with Matteo** (Brian)

  Verify Matteo deployed the same UAT setup for push coverage generation, not just production.
- **Finalize and send tickets 1259 and 1260 for validation** (Brian)

  Also enable TSW80 on 1159, then begin 1243 while awaiting Darwin API access.
- **Schedule steering committee before 21st October** (Francois)

  Include new stakeholder in the loop.

Last Updated: 2026-09-22
