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

## Open Questions

- UNCERTAIN: The captured notes do not define a single team-wide AI governance policy.
- UNCERTAIN: Copilot token usage for GitHub-side PR fixes was believed to be org-budgeted rather than personal-tokened, but this needed confirmation with IT/Irun.

## Sources

- `sources/meetings/2026-06-23-0945-granola-team-meeting.md`
- `sources/meetings/2026-06-23-1430-granola-new-dag-agent.md`
- `sources/meetings/2026-06-30-1600-granola-recruitment-alignment.md`
- `sources/meetings/2026-07-02-1700-granola-application-team-meeting.md`
- `sources/meetings/2026-07-07-0945-granola-weekly-team-meeting.md`
- `sources/meetings/2026-07-07-1530-granola-francois-help.md`

Last Updated: 2026-07-08
