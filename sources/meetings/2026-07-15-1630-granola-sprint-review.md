# Sprint Review

Source type: Granola meeting notes

Meeting ID: `1e8205b9-bb76-49d1-8580-64b7964a66e8`

Meeting date/time: Jul 15, 2026 4:30 PM GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves the available Granola notes and summary. It is not a verbatim transcript.

## Discussion Notes / Summary

### Sprint Overview

- Pew 2 Sprint 2 mid-period review, presented by Michael.
- Two goals for the sprint:
  - Improve the interconnector dashboard.
  - User empowerment: enable new users to create their own DAGs.

### Interconnector Dashboard (SMP Japan)

- Dashboard updated in Grafana with region-specific panels.
- New "As Of" feature with two modes:
  - Latest: uses current effective capacity.
  - Lookback: uses newest available historical snapshot for a selected date.
- Data backfilled to fiscal year 2019 (previously only from 2025), thanks to Moral Science.
- Dashboard elements:
  - Blue lines: available capacity.
  - Orange lines: minimum available capacity.
  - Green lines: actual power flow.
  - Purple lines: day-ahead price difference.
- Stakeholder noted the dashboard will be used in an upcoming auction early next week.
  - Feedback to follow after use.

### User Empowerment: DAG Creation (SAP Ingest)

- Presented by Francois.
- Process for users to create their own DAGs:
  1. Create an issue on the team's Git repository, assign to Copilot.
  2. Copilot generates basic scaffolding for the DAG.
  3. User writes the business logic.
  4. Submit pull request to dev branch to deploy.
  5. DAG becomes accessible on the platform.
  6. Data pushed to CDH dataset, accessible in Grafana via Antenna query and connector.
- Team remains available for support and questions.

### Budget Status

- 80% of budget consumed with ~one month remaining.
- ~90% of scope completed (interconnector + DAG empowerment).
- Only ~20% of effort remaining.
- Team size will be reduced for the final two sprints; Brian remains for support.
- New scope (e.g., new dashboards) will require additional budget discussion.
- Time spent this sprint: Common 77h, Japan 80h, Ingest ~60h (total: 219h).
- Next period scope being planned by colleagues in India; Carlos, Hiromi-san, and Usio-san may request additional dashboards.

## Next Steps / Action Items Present in Granola

- **Push interconnector dashboard data to TSDB**

- **Run beta tester training sessions for DAG creation**

  Extend to broader users after incorporating feedback on the process.

- **Begin planning for Jupiter integration**

  Target September implementation if use cases are validated at the steering committee.

Last Updated: 2026-07-15
