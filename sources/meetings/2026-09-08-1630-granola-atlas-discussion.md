# Atlas Discussion

## Metadata

- Source: Granola
- Meeting ID: `54c6440d-a552-4f0d-b3ac-6a6c3f57f18b`
- Date: 2026-09-08 16:30 GMT+8
- Captured by: Brian Alexander Peralta
- Known participants:
  - Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Atlas Application: Context and Goal

- Atlas is a front-end app (graphs, tables, maps) built by Francois using Dash Framework and Copilot.
- Goal: bring Atlas codebase in line with development standards and best practices.
- Approach: build a QA agent to automatically check code against standards, rather than Brian doing manual reviews.

### Agent Architecture and Approach

- Existing agents in `.github`: Angular dev (front end), FastAPI dev (back end), CDK Python dev (infra).
- Plan: create a new senior Dash developer agent via the governance curator.
  - Governance curator generates Dash-specific standards folder and a compliant agent.
  - Architect agent works with curator to propose and validate best practices.
  - Can also feed existing Atlas repo as context and pull latest Dash best practices via web search.
- Tiers of agent usage:
  - Tier 3: full hands-off pipeline (PO specs, tech specs, work packages, dev, review); most expensive.
  - Tier 2: spec-driven with targeted changes.
  - Tier 1: direct bug fixes to a specific agent, no full pipeline.
  - Tier 0: cheapest, no specs needed, developer agent builds directly against standards with optional reviewer.
- Recommendation: use tier zero for Atlas, given it is a small project and budget should be kept lean.
- Credit cost is driven by context size, not prompt length; indexed standards help keep costs down.
- Copilot's prompt coach is available for prompt optimization.
- Atlas is deployed on S3 via Digital Acceleration team tooling; Kubernetes is not yet in standards.

### Timeline, Ownership, and Next Steps

- MVP scope: generate the Dash agent and standards, then run a full audit of the existing Atlas codebase.
- Acceptance criteria: agent in place, respects Dash standards, communicates with architect agent.
- Timeline: no hard deadline, but sooner is better as Francois is actively adding features; target before end of year.
- Brian available starting Thursday; tail end of current sprint ends Wednesday.
- Francois off Thursday and will share repo link by end of day today.
- Touch point scheduled for Friday to check progress; demo if agent is already done.

### Next Steps

- Share Atlas repository link with Brian. Owner: Francois.
  - Commit and push pending changes first; Brian needs this to start.
- Set up governance curator, generate Dash standards and agent, and audit Atlas codebase. Owner: Brian.
  - Start Thursday; use tier zero. Flag any standard violations or refactoring suggestions.
- Friday touch point to review progress.
  - Demo the agent if ready; otherwise status check.

Last Updated: 2026-09-09
