# Standup

Source type: Granola meeting notes
Meeting ID: `3bcdff8f-add0-4f30-8bce-e4893556fdfe`
Date: 2026-07-07 14:15 GMT+8
Participants known to Granola: Brian Alexander Peralta

Note: This is from Granola notes/summaries, not a verbatim transcript.

## Discussed

### Interconnector Production Readiness

- Dashboard adjustments are ongoing before prod merge.
- QA is stable; no out-of-memory issues were seen this sprint.
- Historical backfill is confirmed to run directly in production.
- Backfill estimate: 11-12 hours of non-stop backfilling.
- Backfill will cover fiscal year 2019 to present.
- Agreement with Hermine: skip QA backfill and go straight to prod.
- Remaining prod blocker: ticket 1186, intermittent 403 Forbidden proxy error.

### Proxy 403 Forbidden Issue

- Intermittent Forbidden errors have affected Japan and India prod environments since around 2026-06-26.
- Around 6 out of 10 runs succeed without changes.
- Issue is prod-only; QA is not affected because it has different proxy config.
- Likely cause: one proxy in the rotation is down or overloaded.
- Francois is escalating to Olivier/Nilo.
- Francois needs the proxy address from the repository.
- Start date confirmed as 2026-06-26 per Michael.

### MS Teams Alert Failover

- Ticket 1181 adds an alert-on-alert mechanism: if MS Teams alerting fails, send fallback email.
- A dedicated "failure dog" forces an error to test the chain.
- Failure dog lives in Japan QA.
- Francois will verify the QA test.

### GitHub Repo Migration Process

- Brian used GitHub CLI to change the remote, not Guido's import process.
- Francois received a transfer notification rather than an import notification.
- Transfer appears more effective for repos already in use because local remote can be updated in place.
- Brian should post a short note in the relevant chat explaining the CLI approach.
- Team should document this as the preferred process for existing projects.

### Lookback Snapshot Dashboard

- Ticket 1197 plan: add a second CDH stage called `historical` alongside existing `latest`.
- `latest` is daily overwrite.
- `historical` is cumulative daily snapshots stored as Parquet.
- Data should be accessible in Grafana.
- Open question: backfill data may reflect current forecast date rather than the original as-of date.
- If Hermine wants true point-in-time views, a staircase lookup approach may be needed.
- First step is archive version with progressive build-out, then confirm exact requirements with Hermine.

## Next Steps

- Brian to post GitHub CLI migration note in team chat.
- Brian to share proxy address for ticket 1186.
- Brian to pair with Francois on ticket 1100 dependency setup.
- Clarify lookback dashboard requirements with Hermine.
- Brian to attend repo migration meeting later on 2026-07-07.

Last Updated: 2026-07-08
