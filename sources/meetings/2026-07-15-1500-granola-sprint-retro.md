# Sprint Retro

Source type: Granola meeting notes

Meeting ID: `0069c9d4-a954-4492-9ef6-1b87e53dc8db`

Meeting date/time: Jul 15, 2026 3:00 PM GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves the available Granola notes and summary. It is not a verbatim transcript.

## Discussion Notes / Summary

### Check-In: AI Movie Poster Exercise

- Team used AI tools to generate sprint-themed movie posters as a check-in activity.
- Copilot image generation unavailable (service down), Gemini worked well.
- Brian connected Jira MCP to pull Sprint 24 tickets and generate a narrative poster.
  - 403 error cast as the main villain, Japan and India as key scenes.
  - Praised for data richness vs. manually prompted posters.

### Sprint 24 Retrospective

- Highlights:
  - Dependencies separated between Japan and India teams (changes to one no longer affect the other).
  - Intermittent 403 error resolved, unblocking multiple pending tasks.
  - Airflow upgraded to 3.3 for both teams, UI improvements.
  - ICD property merged at last.
- Plot twists / challenges:
  - GitHub org migrated from own org to QRM DMS shared org.
    - Each org running a pipeline costs $400/person, driving the consolidation.
    - Remaining migration items: India repo (Brian) and pipeline/artifact training.
  - Bastion regions opened discussion for potential Iberia (Spain + Portugal) and UK expansion.
    - Best case: two new namespaces, full deployment duplication.
    - Worst case: nothing if proposal not accepted.
- First sprint in a long time to close near the ideal burndown rate.

### Budget and Team Capacity

- 80% of project budget already consumed with ~4 sprints remaining.
- Remaining budget: 1.5 units across those sprints, requiring significant effort reduction.
- Core team going forward: Brian (full time), Francois, and the facilitator.
  - Michael joins ceremonies only; others consulted ad hoc.
  - Brian may contribute part-time to other projects (e.g., SMP) if capacity allows.
- Positive framing: ~90% of steering committee commitments already delivered.
  - Interconnector dashboard exceeds originally planned scope.
  - India team still fetching their own data; timeline for handoff work unclear.

### Sprint 25 Goals

- Goal 1: Mateo training.
  - Validate access provisioning and onboarding process end-to-end.
  - Refine before rolling out to broader audience.
- Goal 2: Push interconnector data to TSDB.
  - List of ~28 time series to be sent; IDs to be created via GSBK.
  - Octo provider owner (Carlos and team) to validate metadata changes.
  - Open question: send 5-minute or 30-minute average curves to TSDB.
  - Capacity and minimum capacity metrics are straightforward; actual flow data TBD.
- Automated multi-namespace deployment flagged as a future technical task (ticket exists).

### Sprint Review Prep

- Michael updated slides for Japan interconnector dashboard.
  - Shows latest/look-back mode, current date indicator.
  - Data backfilled to 2019 (Bloomberg only covers to 2025; remainder from Hiromi).
- SMP India section: Brian to show implemented state in GitHub, not a live creation demo.
  - Emphasis on clarified processes for new users and DAG developers.
- India next steps slide to be deleted.
- Remaining slides: budget/consumption, team split, scenarios.

## Next Steps / Action Items Present in Granola

- **Research Copilot agent token ownership** (Brian)

  Determine whether GitHub Copilot agent usage draws from the Walnut contract or individual tokens, to assess future cost implications.

- **Complete India repo migration away from SAP Walnut** (Brian)

  Last remaining item blocking decommission of the SAP-specific Walnut contract and associated $400/org pipeline cost.

- **Send TSDB time series list to the team**

  Facilitator to share the list of ~28 interconnector time series for Sprint 25 prioritization.

- **Confirm budget code for Iberia/UK expansion work**

  Check whether customer success or technical development codes can cover the two potential new country deployments.

- **Schedule support process refresher session**

  Carried over from last retro; not yet conducted. Facilitator to create a dedicated meeting.

Last Updated: 2026-07-15
