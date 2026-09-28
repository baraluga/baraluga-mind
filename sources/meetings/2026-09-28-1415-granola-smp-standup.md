# Granola Capture: SMP Standup

- Date: 2026-09-28
- Time: 14:15 Asia/Manila
- Source: Granola
- Meeting ID: `954ecc95-b668-4552-a5e0-02edb3e3dbb7`
- URL: https://notes.granola.ai/d/954ecc95-b668-4552-a5e0-02edb3e3dbb7
- Captured by: Brian Alexander Peralta
- Known participants:
  - Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Ticket Updates

- Backfilling for ticket 1253 (bid stacks): confirmed fine to skip for now
  - Mateo already validated; Francois to cross-check TSDV values against Grafana
- Bug fix for duplicates (ticket 1265): no error on Teams; Kaba real-time check today counts as validation
  - Francois to validate both tickets before meeting with Matteo

### Darwin API Access and Legacy Scraper

- Darwin API access still blocked: escalated to a French contact, no concrete action yet
- Brian focusing on legacy scraper in the meantime
- No risk of running out of work if Darwin stays blocked
  - Fallback options: POCs, map work

### Grafana Map Dashboard

- Francois explored two mapping approaches over Friday:
  - Plotly-based map (file hosted in Runfra Grafana folder): works, but uses a non-standard format; Claude can convert Python Plotly scripts
  - Grafana geomap: cleaner integration, but currently limited to static JSON (colors must be hardcoded, no dynamic variable mapping)
- Ticket created to explore dynamic JSON activation and connect correct time series for material requests
- Grafana + JupyterLab integration: Eric meeting held; Signups' setup is essentially what the team wants
  - Tweaks needed: PR review layer, and environment escalation path (can be request-based initially)
  - Nilo to be looped in; ready for next period

### Upcoming Meetings and Sprint

- Sprint planning/grooming session this week
- Demo planned for Indian counterparts: first week of October
  - Francois to gather info on what to demo; Japan team member also to be introduced
- Brian has a meeting with Matteo (and possibly Adrien) today

### Next Steps

- **Validate TSDV values against Grafana for ticket 1253** (Francois)

  Cross-check that values match what's visible in Grafana, as a second validation after Mateo's.
- **Validate duplicate bug fix and ticket 1265 before Matteo meeting** (Francois)

  No Teams error received; Kaba real-time check today serves as validation signal.
- **Gather demo requirements for Indian counterparts** (Francois)

  Demo targeted for first week of October; confirm scope before planning session.
- **Update on Matteo meeting outcome** (Brian)

  Francois asked to be kept in the loop on what comes out of today's session.

Last Updated: 2026-09-29
