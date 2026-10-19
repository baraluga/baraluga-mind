# Francois Caffont

## Current State

As of 2026-10-19. Product owner who built [[atlas-dashboard]], a Dash app, with Copilot, and remains its primary builder. Brian consults on engineering foundations and deployment, not feature ownership. Not the same person as [[francois-delcourt]], the SMP product owner.

- 2026-10-13: reported Atlas DEV redirecting to the dashboards homepage; evidence pointed to a missing DEV ECS service outside Brian's control, with PROD healthy.

## Background

- Sole committer on the Atlas repo as of 2026-09-09.
- Project administrator of `portfolio-atlas` in Intact Beta; PROD dashboard application admins are him and Raphael Lasry (2026-09-15).
- Deployed Atlas manually with his personal login before the GitHub Actions pipeline; he set the deployment credentials in GitHub, and plans to upload data Excel files to S3 for the pipeline to pick up.
- Agreed with Brian that Atlas deploys only from `dev` and `prod` branches.

## Feedback Notes

Observed behaviour for feedback season, as a third-party observer. Rendered by the Feedback Ledger artifact.

- **Strength** (2026-09-08): Built Atlas himself with Copilot and kept shipping features; strong product initiative for a PO. `sources/meetings/2026-09-08-1630-granola-atlas-discussion.md`
- **Strength** (2026-09-24): Unblocked quickly when asked: set the deployment credentials in GitHub so PROD could be configured. `sources/codex-conversations/2026-09-24-codex-conversations.txt`
- **Strength** (2026-10-13): Reported the Atlas DEV redirect clearly enough to trace it to a missing DEV service. `sources/claude-conversations/2026-10-13-claude-atlas-dash-frontend-b943dd75.txt`
- UNCERTAIN: no growth area captured; evidence is limited to Atlas.

## Sources

- `sources/meetings/2026-09-08-1630-granola-atlas-discussion.md`
- `sources/codex-conversations/2026-09-08-codex-conversations.txt`
- `sources/codex-conversations/2026-09-09-codex-conversations.txt`
- `sources/codex-conversations/2026-09-15-codex-conversations.txt`
- `sources/codex-conversations/2026-09-17-codex-conversations.txt`
- `sources/codex-conversations/2026-09-24-codex-conversations.txt`
- `sources/claude-conversations/2026-10-13-claude-atlas-dash-frontend-b943dd75.txt`

Last Updated: 2026-10-19
