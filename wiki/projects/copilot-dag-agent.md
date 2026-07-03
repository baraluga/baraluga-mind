# Copilot DAG Agent

## Summary

The Copilot DAG agent is a helper for creating Airflow DAGs from the current codebase conventions rather than from a static template. In the June 23 walkthrough, it scaffolded a DAG, created a PR-style handover, and included conservative commented-out snippets for Grafana, email, and SharePoint.

The main durable value is reducing repeated DAG setup work while still keeping implementation aligned with the live repository. The main risk called out in the notes is branch and release workflow: agent-created changes must not accidentally pull unrelated `main` changes into `dev` or production.

## Details

- The agent uses a small input format and produces a new DAG plus README handover.
- It passed the output directory path from `prepare_output_directory` into `process_data`.
- A copy-paste script alternative was discussed, but the counterpoint was that templates require maintenance while an agent can adapt to current codebase conventions.
- Initial repo permission issues prevented a colleague from assigning the issue to Copilot until team access was added and the page was hard-refreshed.
- Windows users hit setup issues because README commands assumed Linux/macOS.
- Artifactory credentials for private dependencies and CDH upload steps were not documented clearly enough.
- Current branch state in the notes: agent branches from `main`, no branch protections yet, manual merge to `dev`.
- Discussed direction, not final decision: feature branch to PR to `main`, then merge to `dev` and `prod`.
- New dependency additions still require Docker image coordination in SMP Tool.

## Open Questions

- UNCERTAIN: Final branch and PR workflow was not decided in the captured meeting.

## Sources

- `sources/meetings/2026-06-22-1415-granola-daily-standup.md`
- `sources/meetings/2026-06-23-1430-granola-new-dag-agent.md`

Last Updated: 2026-07-04
