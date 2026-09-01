# 2026-09-01 Busy

Source type: Granola meeting notes
Meeting ID: `5535fce1-6d62-481d-b23e-22ae41fea4c1`
Date: 2026-09-01 14:15 GMT+8
Captured by: Brian Alexander Peralta
Participants known to source:
- Brian Alexander Peralta from Icloud <ba.peralta@icloud.com>

Note: This is from meeting notes or transcript-derived material and may contain transcription errors.

## Summary

### Sprint Setup and Ticket Priorities

- New sprint created, approximately 6 story points allocated.
- Tickets reorganized per Mateo's email priority order.
- Kaaba-related tickets, Child 37 and Child 38, placed at top of sprint.
- Bilateral contract scraping vs. bid stack priority is unclear.
  - Mateo's email says bilateral is lower priority; Francois heard the opposite from Matthew.
  - Francois to double-confirm with Adrian while Mateo is away.

### India IEX Bid Stack Ticket

- Split into three tickets for clearer tracking and dependency management:
  1. Scraping.
  2. Dashboard.
  3. TSDB publishing.
- 60 time series IDs required: 3 metrics times 2 directions, buy/sell, times 10 price bands.
- Adrian to confirm whether new or existing TS IDs will be used.
- Split allows scraper and dashboard work to proceed while TS IDs are pending.

### Proxy/Regional Access Blocker

- Blocked indefinitely due to India regional proxy access requirement.
- Japan precedent exists: proxy workaround was done for a Singapore-only site.
- Same approach likely applicable for India.
- Management approval still pending; Francois sent mail, no reply yet, and expects an answer within two weeks.
- Brian to check with Michael first before looping in Nilo or others.
- Not targeted for current sprint; may begin investigation toward sprint's end.

### Current Sprint: Tickets in Review

- Backfill for TSTV production started after Laurent confirmed access approval.
  - Expected to complete in 36 hours; set to "In Review," no points assigned.
- Ticket 12:37, POA metric for CABA generation, is ready for Francois's validation.
  - No dashboard for all 5 CABA series; logging added to DAG to compare CSV values vs. TSDB pushes.
  - Francois to validate post-meeting; noted as high priority for Mateo.
- Ticket 12:38, Active power panel for India IEX, is ready for Francois's validation.
  - Panel added below MCP chart on India IEX volume trends dashboard.
  - Dashboard exported from production, imported to QA for safe testing.
  - JSON committed to Git repository.

### Sprint Review and POC for Steering Committee

- Sprint review is on 2026-09-09 for a shortened sprint.
- Francois is on holiday Monday through Wednesday the following week.
- Steering committee expects 2-3 presentations; given shortened sprint, aim for at least 1 mini POC.
- POC to showcase a Grafana or Airflow out-of-the-box feature.
  - Options: asset management, dataset scheduling, or another promising feature.
  - Brian to pick the most feasible/enticing one.
  - Can be slotted before or after India tickets; Mateo is okay with some delay on India work.

## Next Steps Captured

- Validate tickets 12:37 and 12:38. Owner: Francois.
- Confirm bid stack vs. bilateral contract priority with Adrian. Owner: Francois.
- Check with Michael on India proxy access approach. Owner: Brian.
- Prepare one mini POC for the steering committee. Owner: Brian.

Last Updated: 2026-09-01
