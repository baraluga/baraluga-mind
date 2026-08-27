# Granola Capture: FEDV Chapter Meeting

Date: 2026-08-27 17:00 GMT+8
Source: Granola
Meeting ID: 596241fa-9158-422c-9dd1-fd3976a2cdee
Title: FEDV Chapter Meeting
Captured by: Brian Alexander Peralta <ba.peralta@icloud.com>

## Summary

# Year-End Deliverables Status

- Documentation, standards, and final members list: complete
- Initiatives section: still outstanding, needs to be filled in
- Knowledge sharing session (UX/UI): not yet scheduled, date to be set soon

# Standards Management and GitHub Migration

- Current standards in org-level .github repo, but not yet organized by chapter
- Plan to reorganize by chapter (Angular, UX, Python frameworks with frontend, etc.)
- Moving away from direct Confluence edits toward GitHub as the source of truth
  - Easier for AI agents to consume standards from GitHub
  - Two options to sync back to Confluence:
    1. MCP server
    2. Deterministic pipeline (preferred)
- Angular standards being updated for Angular 22
  - PrimeNG no longer recommended (paid in newer versions)
- React initiative deprioritized: one project using it is stalled, no news on revival

# Monitoring and Dashboards (Grafana / Splunk)

- Grafana pages updated; fewer custom dashboards being built going forward
- Splunk is the IS team's recommended monitoring tool (Frederic's preference)
  - Team has Splunk experts; no internal Grafana expertise for 24/7 production support
  - Grafana deployments being converted to Splunk where needed
- Placeholder Splunk page to be added to the chapter documentation
- Dashboard standardization flagged as a need
  - Initial business stakeholder presentations showed inconsistent, low-quality dashboard designs (random colors, no clear representation)
- Power BI MCP server initiative marked as not relevant for now
  - Usage declining as Grafana and Synapse take over
  - Some Power BI projects (Argos, one other) being decommissioned by year-end
  - Microsoft Copilot license now available, which may enable Power BI agent integration if a future need arises

# SDD Agents and Credit Consumption

- SDD (spec-driven development) pipeline uses orchestrator + sub-agents (developer, reviewer roles)
- Demo built in days using SDD; estimated ~40K tokens consumed
- Credit consumption breakdown (based on recorded metrics):
  - Grounding artifacts (standards + SDD artifacts): ~58% (30% artifacts, 28% standards)
  - Generated/implemented source files: ~30%
  - Model choice: minor contributor (~third lever)
- Context size, not model choice, is the primary cost driver
- Python script built (AI-assisted) to measure consumption per machine
  - Figures are a lower bound: cancelled calls and cleared sessions not captured
  - Orchestrator-level consumption not yet tracked (admins only); actual cost likely higher
- Slides prepared to share with Frederic addressing his credit consumption concerns

# Next Steps

- **Add Splunk placeholder page to chapter documentation**

  Acknowledged during the meeting as a gap to fill.
- **Reorganize GitHub standards repo by chapter**

  Segregate existing frontend standards into Angular, UX, Python/frontend, etc. sections.
- **Fill in initiative details for GitHub-to-Confluence standards pipeline**

  Owner confirmed as spoke for this initiative.
- **Schedule UX/UI knowledge sharing session**

  Has been delayed due to SDD agent workload; date to be set soon.

Last Updated: 2026-08-27
