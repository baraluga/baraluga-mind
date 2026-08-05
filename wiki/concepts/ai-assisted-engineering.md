# AI Assisted Engineering

## Summary

AI-assisted engineering appeared in several captures as a practical workflow theme: Copilot DAG generation, agentic pull requests, reusable AI-generated scripts, MCP/browser validation, dependency and vulnerability remediation, AI-assisted runbook automation, and AI-permitted candidate assessments.

The notes frame AI as a way to reduce repeated implementation or diagnosis work, while still requiring human review, explanation, and workflow controls.

## Details

- [[copilot-dag-agent]] uses current repository conventions to scaffold Airflow DAGs.
- Application team AI workflow ideas included MCP-based browser rendering for frontend validation, reusable AI-generated scripts, and agent workflows for dependency and vulnerability remediation.
- AI-assisted runbook automation for recurring APM issues reportedly reduced repeat diagnosis from about 10-20 minutes to about 2 minutes.
- Management direction relayed in the July 2 application team meeting: move toward supervising AI agents instead of doing all implementation manually.
- Recruitment assessments allow candidates to use AI tools, but candidates must explain and defend their results.
- Technical constraints appeared too: Anthropic access from the Philippines was blocked due to Hong Kong/China network routing, with workarounds including disabling ZScaler or using another network.
- One team meeting noted Scalar defaulting to a Hong Kong IP, causing Claude/Anthropic access issues; GPT/Gemini alternatives were mentioned.
- July 7 weekly team notes say one hour of IT troubleshooting restored Claude/Anthropic access through web or IDE, though Hong Kong routing remained a concern and IT would report the network tool block.
- July 7 Francois-help notes say GitHub Copilot can fix PR pipeline errors directly in GitHub and commit to the existing PR, making simple PR fixes more accessible to non-Python contributors.
- July 9 Copilot CLI sessions show the same repo-grounded workflow being used outside Codex: project walkthroughs for the SMP collection and `ado-ios`, then a TDD refactor with Ruff, pytest, coverage, smoke validation, commit, PR creation, approval, and merge.
- July 15 work created [[github-copilot-custom-agents]] for `qrm-dms`, replacing an initial smoke-test agent with an ADO Pipeline Modernizer agent intended to help convert and redesign Azure DevOps YAML pipelines as GitHub Actions workflows.
- July 17 diagnostics for [[zscaler-codex-access]] showed that Codex can sometimes keep an existing response stream alive during Zscaler handoff, but fresh Codex/OpenAI requests can fail with 403 through the Zscaler path. Private-site browser testing may still work once Zscaler settles, but durable agentic access needs an approved networking policy rather than local protocol workarounds.
- July 21 work created a global `consult-mind-palace` Codex skill that can use this repository as a source-backed memory layer from any working directory. A forward test produced a Japan Interconnector briefing with facts, decisions, actions, uncertainty, and stale-status caveats separated.
- July 21 also showed a practical limit of GitHub-side custom agents: a Modernizer run may finish without changes when the runner cannot reach internal registry evidence. In that case, Codex can reconstruct and supply a grounded handoff, but authentication and repo readiness still control whether relaunching is appropriate.
- July 28 grooming proposed a dry run of Copilot automatic PR review. The working theory was that the PR creator's credits would be charged, but the team wanted a small test and confirmation with Pierre before adopting the automation.
- The August 4 Application Team AI Corner used [[copilot-dag-agent]] as a concrete example: the team chose a GitHub Copilot custom agent as a POC for DAG contributor onboarding because SMP India and Japan had recently moved to GitHub, and because repo-grounded scaffolding can evolve with code changes better than long Confluence instructions.
- The same meeting framed model quality as a real constraint: the DAG Helper result remains under the mercy of the selected model's capability, so a capable thinking model and human review are still part of the operating model.
- The Omniron spec-driven-development pilot used an orchestrator plus specialized agents for PO, architect, tech lead, front end, back end, and sub-agent roles. It ran end-to-end and produced a deployable web app candidate, but the team explicitly said not to adopt the approach elsewhere yet because inter-agent communication, standards size, completion checks, compliance, and token burn still need tuning.

## Open Questions

- UNCERTAIN: The captured notes do not define a single team-wide AI governance policy.
- UNCERTAIN: Copilot token usage for GitHub-side PR fixes was believed to be org-budgeted rather than personal-tokened, but this needed confirmation with IT/Irun.
- UNCERTAIN: The ADO Pipeline Modernizer agent had only been lightly tried by July 15; it still needs real-pipeline pilots before being treated as a proven migration path.
- UNCERTAIN: Whether IT will approve a ChatGPT/Codex Zscaler bypass or split-routing policy for private-site agentic testing.
- UNCERTAIN: Whether internal registry access for GitHub-side agent runners will be solved centrally or handled with per-run evidence handoffs.
- UNCERTAIN: Whether automatic Copilot PR review is charged to the PR creator or another organization billing pool.
- UNCERTAIN: Whether Omniron's spec-driven-development agent workflow will become a reusable team pattern after the planned workshop and compliance review.

## Sources

- `sources/meetings/2026-06-23-0945-granola-team-meeting.md`
- `sources/meetings/2026-06-23-1430-granola-new-dag-agent.md`
- `sources/meetings/2026-06-30-1600-granola-recruitment-alignment.md`
- `sources/meetings/2026-07-02-1700-granola-application-team-meeting.md`
- `sources/meetings/2026-07-07-0945-granola-weekly-team-meeting.md`
- `sources/meetings/2026-07-07-1530-granola-francois-help.md`
- `sources/copilot-conversations/2026-07-09-copilot-conversations.md`
- `sources/codex-conversations/2026-07-15-codex-conversations.md`
- `sources/meetings/2026-07-15-1500-granola-sprint-retro.md`
- `sources/codex-conversations/2026-07-17-codex-conversations.md`
- `sources/codex-conversations/2026-07-21-codex-conversations.md`
- `sources/meetings/2026-07-28-1430-granola-smp-backlog-grooming.md`
- `sources/meetings/2026-08-04-1700-granola-application-team-meeting.md`
- `sources/codex-conversations/2026-08-04-codex-conversations.txt`

Last Updated: 2026-08-05
