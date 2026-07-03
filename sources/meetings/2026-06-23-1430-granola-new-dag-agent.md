# New DAG Agent

Source type: Granola meeting notes
Meeting ID: `43f19f76-3374-4b02-a6e3-1f5f26899cdf`
Date: 2026-06-23 14:30 GMT+8
Participants known to Granola: Brian Alexander Peralta

Note: This is from Granola notes/summaries, not a verbatim transcript.

## Discussed

- First walkthrough of the Copilot DAG-creation helper.
- A colleague could not find where to assign the issue to Copilot because of missing repo permissions.
- After adding them to the team and hard-refreshing, the assignment button appeared.
- Agent scaffolded a new DAG from the current codebase rather than a static template.
- Conservative commented-out snippets were included for Grafana, email, and SharePoint.
- Output directory path was passed from `prepare_output_directory` into `process_data`.
- A copy-paste script alternative was discussed; counterpoint was that templates require maintenance while the agent adapts to codebase conventions.
- Windows users hit setup issues because README commands assume Linux/macOS.
- Artifactory credentials for private dependencies were not documented clearly enough.
- CDH upload process was unclear to the colleague.
- Current branch state: agent branches from `main`, no branch protections yet, manual merge to `dev`.
- Agreed direction, not final decision: feature branch to PR to `main`, then merge to `dev` and `prod`.
- Automatic tests should gate PRs; if green, human review may not be needed.
- Direct feature branch merge to `dev` risks pulling unrelated `main` changes into `dev`/`prod`.
- Airflow syncs the repo automatically, so merged code becomes live immediately.
- New dependency additions still require Docker image coordination in SMP Tool.
- Missing docs: Windows commands, Artifactory setup, and `smp-common` docstrings.

## Next Steps

- Brian to update SMP India and SMP Japan READMEs with Windows commands and Artifactory credential setup.
- Brian to refine Copilot agent prompt so it stops looking for a non-existent DAG helper skill.
- Colleague to implement a small DAG and raise a PR to `main`.
- Schedule a team meeting to finalize branch and PR workflow.
- Brian to create/estimate a ticket for Carlos's Grafana/TSDB dashboard request.

Last Updated: 2026-07-04
