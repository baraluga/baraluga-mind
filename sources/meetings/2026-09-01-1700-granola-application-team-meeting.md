# 2026-09-01 Application Team Meeting

Source type: Granola meeting notes
Meeting ID: `d40c501e-c7e5-4cf3-9323-dce11ff64451`
Date: 2026-09-01 17:00 GMT+8
Captured by: Brian Alexander Peralta
Participants known to source:
- Brian Alexander Peralta from Icloud <ba.peralta@icloud.com>

Note: This is from meeting notes or transcript-derived material and may contain transcription errors.

## Summary

### Management Updates

- Three key challenges flagged for end of year:
  - Synapse: new production support model, which is new for the team.
  - AI onboarding: learning from the Kiva project how to use AI in development.
  - MCP for collection support, connecting to Synapse, reusable across projects.
- DNS and Br1JMS discussions are ongoing between Dmitry and the head of market analyst.
  - Possible impact on project scope; no confirmed changes yet, flagged for transparency.
- Jerome Blanc is leaving the company by end of month.
  - He is involved in key projects; follow-up handover is being arranged with UK contacts.
- Philippines trip planned for November for three weeks, including training sessions.
- Training priorities:
  - Kubernetes upskilling still needed.
  - AI training under review: Microsoft Copilot Studio course, approximately EUR 1,300 for 3-4 days, flagged but cost/value is unclear.
  - Explorer sessions on Friday mornings suggested for some team members.
- Development and learning review deadline is 2026-09-15 in Sesame.
  - Dedicated 1:1s or offline completion available in the coming two weeks.
- Time tracking: Philippines team moves from Tempo to a new application starting 2026-09-01.

### AI Corner: Atlassian MCP Tool (Alfred)

- MCP for Atlassian connects IDE through Copilot to Confluence and Jira.
- Install via VS Code by searching for the MCP extension; configure with username and API token.
- Key use cases demonstrated on the Kiva project:
  - Syncing repo documentation to Confluence pages, such as a dev runbook synced live.
  - Creating stories and subtasks by passing meeting transcripts or summaries to the agent.
- Skills/workflow rules limit scope, such as only creating under the Kiva page and no modifications outside QRM without verification.
- Cost: approximately 160 credits for story/subtask creation using Opus; page sync approximately 15 credits each.
- If a GitHub Action already handles syncing, MCP sync is redundant because GitHub Action is free.
- Skill for product owner / planner role to keep tickets short and concise is still in progress.
- Next step: Alfred to create a PR to commit the skill to the shared GitHub repo.

### Kiva Platform: Industrialization Update (Jeka)

- Current Kiva: ABSD-specific "talk to my data" chatbot using a ReAct agent, calling 5 MCP servers.
- Problem: desk-specific design causes code duplication if other desks onboard.
- Solution: industrialize into a platform service with clear ownership split:
  - DMS owns infrastructure, MCP servers, authentication, deployment, and scaling.
  - Desk teams own agent skills, context, query logic, and desk-specific reasoning.
- Sprint 1 completed:
  - Positron MCP server live on Kubernetes, moved from ABSD VMs.
  - Domain live: `dms-kiva-dev.ms.myng.com`.
  - Registered with NG MCP registry; VS Code extension visible.
  - Basic user management in place; authentication via Okta.
  - Okta's new "Cos App" feature in use; team is first to use it in production.
  - 13 Positron tools discovered by Copilot; list market query returned 77 markets.
- Next steps:
  - Deploy MCP servers for other data sources: GitHub, Grafana, Quiver.
  - Add desk-specific context/skills to agent.
  - Request NG registration for additional MCP servers, involving wait times and SNOW requests.
  - Whitelist VS Code URL in proxy, currently blocked.
  - Coordinate with each data source team for credentials and change management.

## Next Steps Captured

- Complete development and learning review in Sesame by 2026-09-15. Owner: Brian.
- Alfred to raise PR for Atlassian MCP skill to shared GitHub repo. Owner: Alfred.
- Raise anything relevant in old accounts before deletion. Owner: unspecified.
- Finalize GMR migration to remove legacy resources from old account. Owner: unspecified.

Last Updated: 2026-09-01
