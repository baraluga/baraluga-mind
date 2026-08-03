# AM Standup

Source Type: Granola meeting notes

Meeting ID: `cf81c480-f1ee-456e-bd60-f9dc2da6c746`

Meeting Date/Time: Jul 31, 2026 9:45 AM GMT+8

Known Participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves the available Granola-generated meeting notes and summary. It is not a verbatim transcript.

## Discussion Notes / Summary

### Town Hall Follow-up

- Thanks given to team for joining yesterday's town hall
- SPH/ASPI announcement deferred; more pressing issues took priority
- Target window: September 1-15

### Data & Migration Work

- Peralta timeline: bug introduced around 2024, tracing back to fiscal year 2021 via Bloomberg
- Validation dates in focus: 12/16, 12/18, 12/19
- Airflow failures flagged as affected by validation spike (12/18)
- India migration: moving from old scraper org to QRMDMS (Michael)
- SMP migration scope:
  - Grafana and GitHub repositories in scope
  - SFF depositories/chapter out of scope
  - Pipeline conversion also out of scope
  - Migration value and depository work prioritized for 12/18

### Infrastructure and Storage

- Artifact subdomain: additional cost of 180 EUR/year per user
- Storage account consultation: disabling secure transfer under review
  - Secure transfer impacts NFS and API
  - Disabling enables workflow support for new stage scenario creation
  - Substacks to introduce stage stocks

### Sprint Tasks and Blockers

- No blocking issues currently; 403 resolved
- Tech task 35 identified as priority this sprint
- Task 358: not in scope for this sprint
- Task 355: spike/investigation underway
- Findings to be presented as PowerPoint/documentation next week

## Next Steps / Action Items From Granola

- Prepare spike investigation findings as a presentation.
  - Document and present Task 355 findings as PowerPoint; target next week.
- Confirm artifact subdomain email setup.
  - 180 EUR/year per user; clarify whether per-user email is acceptable before proceeding.

Last Updated: 2026-07-31
