# Granola Capture: backlog grooming again

Source Type: meeting
Meeting Date: 2026-10-01 14:33 Asia/Manila
Granola Note: https://notes.granola.ai/d/33f3532e-95df-4fe9-a82b-bd5bcb70eecd
Captured: 2026-10-02

## Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### H. India Website Scraping (Ticket 1)

- Need to scrape DEM, GDEM, and RTM data directly from the H. India website because they are not available via API.
- Same approach as the regional-level implementation, now applied at national level.
- Build from scratch in Airflow; Matteo to provide ideas.
- Access issue: website returns 403 forbidden through Zscaler.
  - Was accessible in the office and outside Zscaler.
  - Previous HPX Scraper ticket was rejected for the same reason.
  - Plan: raise a ticket with James Snow from the security team to whitelist the provider.

### Bilateral Contract Scraper Refinement (Ticket 1078)

- Original scraper from two sprints ago only captured a subset of what the dashboard requires.
- Gap identified by comparing expected dashboard output against scraped data.
- Options: refine existing scraper or reimplement from scratch with full dashboard context.
  - Original work was done without knowing how data would be used.
  - Now have a clear dashboard spec to scrape against.
- Request originated from head of trading in DIA, hence higher priority.

### India Clearing Map Dashboard (Grafana)

- Recommendation: go straight to Plotly; quick win confirmed and head of trading is happy with it.
- Dashboard requires three maps; panels can be saved and reused across other Grafana dashboards.
- Color scheme: yellow-to-red gradient because there are no negative prices in India.
  - Price range: 0 to 10,000, mapped linearly.
  - Volume range: based on last year's historical data, with a +10% ceiling and 0 as floor.
- Freshness indicator needed near each map panel.
  - Show the oldest "latest date" across the time series in that panel as the worst-case freshness.
  - Similar to the "last collected / last push" indicator on the existing dashboard.
  - Use application date from System E and latest date from the TS graph.

### Matteo's KPI Dashboard (Airflow + CDH)

- Matteo has existing KPI-generating code on his laptop; data sources are now in TSDB or moving there soon.
- Plan: Airflow preprocessing DAG to collect time series, run calculations, push results to CDH, then build Grafana dashboard.
- Matteo wants ownership: pair with him so he can understand and replicate the process himself.
- Timing: not urgent; potentially deferred until after Jupyter integration is complete.
  - End-of-year timeline mentioned and accepted by Matteo.
  - Will contact Nilo for an update on Jupyter integration timeline.
- Technical decision open: route data TSDB to CDH, or split the flow and push to both TSDB and CDH directly from the same DAG.
- Schema approach: flat dump if dashboard shape is unknown; normalize if dashboard spec is confirmed.
  - Ask Matteo for more detail on desired dashboard structure before deciding.

### Ticket Housekeeping

- First three tickets should be converted from task to story type; last two can remain as tasks.
- Access issues with Zscaler blocking the H. India website affect both sides, not just one team member.
- Overall priority order agreed and considered sensible by all.

## Next Steps Mentioned

- Raise ticket with James Snow to unblock H. India website access.
- Convert first three backlog tickets from task to story type.
- Clarify Matteo's desired KPI dashboard structure before schema design.
- Contact Nilo for Jupyter integration timeline update.

## Value Gate

Passed: contains durable project context, prioritization, technical decisions, blockers, and follow-up actions.

