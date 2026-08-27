# Granola Capture: Mateo Call

Date: 2026-08-27 16:46 GMT+8
Source: Granola
Meeting ID: 622d8748-7fc6-401c-b70b-9bed69ae5864
Title: Mateo Call
Captured by: Brian Alexander Peralta <ba.peralta@icloud.com>

## Summary

# Ticket Priorities

- POA time series and kappa generation dashboard update for IX: top priority
- Bilateral contract scraping (ticket 1229): start next, no blockers
- Grid India data scraping: blocked due to access restrictions
  - VPN may be a solution; Mateo suggested checking with Francois or others who may have done it before
  - Singapore market analysts may request this data at any time, so unblocking it matters

# Grid India Access

- Brian cannot currently access Grid India for data mining
- Mateo suggested a VPN workaround; unclear if Francois or someone else has resolved this before
- If access cannot be resolved, Mateo confirmed it's fine to deprioritize and explain the blocker

# POA Time Series Update

- Mateo needs to modify a time series previously injected into TSDB
  - Old name: "Irradiance" (was incorrect, referred to horizontal irradiance)
  - New name: terrain/POA irradiance
  - ID will not change; Mateo will send the new column ID once updated
- Brian confirmed the scraper uses the ID, not the name, so no impact on Brian's side
- Mateo will action this by end of day (27th August)

# Handover and Availability

- Mateo leaving 1st-11th September (10 days, fully offline)
- Adrian covering in his absence, also aligned on the Singapore timeline
- Brian should raise any TSDB access or permissions requests before Mateo leaves

# Next Steps

- **Start on bilateral contract scraping (ticket 1229)**

  No blockers; prioritize this while Grid India access is unresolved.
- **Clarify Grid India VPN access with the team**

  Check with Francois or others on whether a VPN or alternative solution has been used before.
- **Raise any TSDB permissions needed before 1st September**

  Mateo is offline 1st-11th September; Adrian covers in his absence.

Last Updated: 2026-08-27
