# SMP Backlog Grooming

Source type: Granola meeting notes
Meeting ID: `4530973f-d09b-47e5-9542-bfc1aacd6c30`
Meeting date/time: Jul 28, 2026 2:30 PM GMT+8

## Known Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Capture Note

These are Granola meeting notes/summaries, not a verbatim transcript.

## Discussion Notes / Summary

### TSDB Data Ingestion: Gen-A Data Pipeline

- File delivered via SFTP to "Go Anywhere" service, updated every 15 minutes.
  - File grows from 0 to 96 lines across the day, then resets at midnight.
  - 5AM scraper run to sync any late/missing data from prior day.
- Push to TSDB must happen every 15 minutes, overwriting the current day's window.
- Key open questions pending Matthew and Adrian:
  - URL and access method for Go Anywhere.
  - Machine-to-machine connectivity versus user login only.
  - Geo-blocking risk. Precedent: India scraping was blocked.
- Fast-access layer in TSDB flagged as a consideration if insertion lag is an issue.
  - Try standard insertion first; escalate to fast-access layer if lag observed.

### Backlog and Sprint Priorities

- Docker image build/push to GCR: good time to tackle given low user activity.
  - Brian flagged knowledge gap on Docker/AWS ECR; needs Joyce or Michael involved.
- Grafana dashboard sync to Git: long-standing ticket, good time to action.
  - Goal: single source of truth, rollback capability, no JSON/Grafana drift.
- Interconnector Excel export: deprioritized; immediate Japan requests for OP capacity and lookback take precedence.
- User account management ticket: likely already documented in Confluence.
  - Process: request access to QRMDMS org, assign to team, add to Grafana via email.
  - Action: create one concise Confluence page consolidating the steps.
- Jupyter Lab / DAG integration, new epic, early stage:
  - Papermill operator is the official Airflow tool for running notebooks.
  - Limitation: entire notebook runs as a single task, not per-cell tasks.
  - No granular monitoring; business logic is opaque versus multi-task DAGs.
  - Mismatch between Airflow's design intent and Jupyter-style interactivity.
  - To discuss further next week; may involve Eric, who worked on this previously.
- Copilot PR auto-review agent: set up dry run, Brian double-checks output.
  - Cost concern: unclear who gets charged when auto-triggered on a PR.
  - Working theory: credit charged to whoever creates the PR.
  - Need to confirm with Pierre; quick test first to validate the theory.

### Steering Committee Presentation (August)

- Japan items to include:
  - Interconnector dashboard update: backfilling, OP capacity.
  - Snapshot feedback: one dashboard done, one pending.
  - Lookback function.
  - TSDB data update: flag as in-progress, confirm with Carlos.
- India items: data collection and training.
- Demo scope: S&P Japan dashboards and interconnector only.
  - Hardened XLSEC (12.01) is CLI-only, run by Mateo; mention but nothing to show.
- Budget slide: submit hours to Gong before end of morning.
- Git push / user empowerment feature: Matthew to test, then extend to users; prepare proposal for August steering committee.

## Next Steps / Action Items Present in Granola

- Confirm Go Anywhere access details with Matthew and Adrian.
  - Need URL, machine-to-machine credentials, and access rights before TSDB ingestion work can start.
- Create Confluence page for new DAG developer onboarding.
  - Consolidate fragmented docs: QRMDMS org access, team assignment, Grafana email invite.
- Test Copilot PR auto-review cost attribution.
  - Validate theory that credit is charged to the PR creator; check with Pierre if confirmed.
- Submit hours to Gong before end of morning.
- Schedule technical feasibility call on Jupyter Lab integration for next week.
  - May need to involve Eric given his prior work on the Airflow/notebook side.

Last Updated: 2026-07-28
