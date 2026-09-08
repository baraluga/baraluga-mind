# Atlas Dashboard

## Summary

Atlas is a Dash Framework front-end application for graphs, tables, and maps. Francois Caffont built the first version with AI assistance and wants enough engineering confidence for continued internal development without turning the consulting engineer into the primary maintainer.

The recommended operating model is tier zero: one lightweight Dash developer agent and Dash-specific standards generated through the governance curator, plus a bounded baseline audit. A standing PO/dev/QA/architect agent fleet was considered overkill unless repeated failures prove a narrower specialized role is needed.

## Details

- The target is a safe path for Francois to keep building while an engineer consults on foundations and higher-risk changes.
- The first engineering pass should check reproducible setup, secrets/configuration handling, access controls, data-to-UI correctness, dependencies, deployment, rollback, error handling, and whether another engineer can understand and change the code.
- Repo setup should include a short `README.md`, project-specific `AGENTS.md`, a focused test suite for critical calculations and empty/invalid data, CI checks, a PR template, and protected review boundaries.
- Francois remains the product owner and primary builder. Engineer review should be required for authentication, permissions, secrets, new data sources, write operations, deployment changes, shared state/caching/background work, or consequential calculations.
- Acceptance for the MVP: Dash standards and agent exist, the agent communicates with the architect agent, and the existing Atlas codebase receives a full audit.
- Timeline from the September 8 meeting: no hard deadline, but sooner is better because Francois is actively adding features; target before year-end, with Brian available from Thursday and a Friday progress touch point.

## Open Questions

- UNCERTAIN: Whether Atlas is the final repository/application name and where the canonical repo will live.
- UNCERTAIN: Whether S3 via Digital Acceleration tooling is already the production deployment path or only the current draft deployment path.
- UNCERTAIN: Which users, data sensitivity level, and operational decisions define the exact approval bar for Atlas.

## Sources

- `sources/meetings/2026-09-08-1630-granola-atlas-discussion.md`
- `sources/codex-conversations/2026-09-08-codex-conversations.txt`

Last Updated: 2026-09-09
