# Copilot DAG Agent

## Summary

The Copilot DAG agent is a helper for creating Airflow DAGs from the current codebase conventions rather than from a static template. In the June 23 walkthrough, it scaffolded a DAG, created a PR-style handover, and included conservative commented-out snippets for Grafana, email, and SharePoint.

The main durable value is reducing repeated DAG setup work while still keeping implementation aligned with the live repository. The main risk called out in the notes is branch and release workflow: agent-created changes must not accidentally pull unrelated `main` changes into `dev` or production.

## Details

- The agent uses a small input format and produces a new DAG plus README handover.
- The current GitHub Copilot flow is issue-driven: a contributor creates a `New DAG` issue, assigns it to Copilot, selects the DAG Helper custom agent profile, and the Copilot coding agent runs under the repository's DAG Helper instructions.
- The agent instructions tell Copilot to read the issue inputs and current repository, create a feature branch, scaffold files and tests, commit the result, and open a PR. In `smp-india`, the instruction explicitly says to open a draft PR targeting `dev`; the matching `smp-japan` instruction only says to open a PR even though the issue template promises a draft PR.
- It passed the output directory path from `prepare_output_directory` into `process_data`.
- A copy-paste script alternative was discussed, but the counterpoint was that templates require maintenance while an agent can adapt to current codebase conventions.
- Initial repo permission issues prevented a colleague from assigning the issue to Copilot until team access was added and the page was hard-refreshed.
- Windows users hit setup issues because README commands assumed Linux/macOS.
- Artifactory credentials for private dependencies and CDH upload steps were not documented clearly enough.
- Current branch state in the notes: agent branches from `main`, no branch protections yet, manual merge to `dev`.
- Discussed direction, not final decision: feature branch to PR to `main`, then merge to `dev` and `prod`.
- New dependency additions still require Docker image coordination in SMP Tool.
- The August 4 AI Corner material framed the durable need as onboarding contributors through repo-specific DAG conventions without maintaining a maze of stale Confluence pages. The solution proof was a short DAG request becoming a repository-grounded, reviewable scaffold PR.
- Matéo's beta test remains the strongest evidence: the flow reached draft-PR generation, and the failure was an external Tools/Walnut Artifactory entitlement gap rather than the agent being unable to scaffold.
- The August 19 SMP overview said the agent has been live for about one month, with its first test in July. It is still a pilot: no production DAGs have been created through this path yet, and Mateo/Matthew remains blocked on local validation because of missing dependencies.

## Open Questions

- UNCERTAIN: Final branch and PR workflow was not decided in the captured meeting.
- UNCERTAIN: Whether `smp-japan` should align its DAG Helper instruction with `smp-india` by explicitly requiring a draft PR targeting `dev`.
- UNCERTAIN: Whether Mateo and Matthew refer to the same beta tester in the August 19 overview note.

## Sources

- `sources/meetings/2026-06-22-1415-granola-daily-standup.md`
- `sources/meetings/2026-06-23-1430-granola-new-dag-agent.md`
- `sources/codex-conversations/2026-08-04-codex-conversations.txt`
- `sources/meetings/2026-08-04-1700-granola-application-team-meeting.md`
- `sources/meetings/2026-08-19-granola-smp-overview-with-jeroen.md`

Last Updated: 2026-08-20
