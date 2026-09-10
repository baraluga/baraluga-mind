# Atlas Dashboard

## Summary

Atlas is a Dash Framework front-end application for graphs, tables, and maps. Francois Caffont built the first version with AI assistance and wants enough engineering confidence for continued internal development without turning the consulting engineer into the primary maintainer. By September 10, 2026, the active repo was being worked under `qrm-dms/atlas-dash-frontend` on branch `dm-898`.

The recommended operating model is tier zero: one lightweight Dash developer agent and Dash-specific standards generated through the governance curator, plus a bounded baseline audit. The first guardrail layer is now underway: focused business-behavior tests, a startup smoke test, Ruff lint/format checks, GitHub Actions validation, and contributor/agent setup guidance. A standing PO/dev/QA/architect agent fleet was considered overkill unless repeated failures prove a narrower specialized role is needed.

## Details

- The target is a safe path for Francois to keep building while an engineer consults on foundations and higher-risk changes.
- The first engineering pass should check reproducible setup, secrets/configuration handling, access controls, data-to-UI correctness, dependencies, deployment, rollback, error handling, and whether another engineer can understand and change the code.
- Repo setup should include a short `README.md`, project-specific `AGENTS.md`, a focused test suite for critical calculations and empty/invalid data, CI checks, a PR template, and protected review boundaries.
- Francois remains the product owner and primary builder. Engineer review should be required for authentication, permissions, secrets, new data sources, write operations, deployment changes, shared state/caching/background work, or consequential calculations.
- Acceptance for the MVP: Dash standards and agent exist, the agent communicates with the architect agent, and the existing Atlas codebase receives a full audit.
- Timeline from the September 8 meeting: no hard deadline, but sooner is better because Francois is actively adding features; target before year-end, with Brian available from Thursday and a Friday progress touch point.
- September 9 Codex work established the first engineering baseline: `pytest` and `pytest-cov` for ownership/filtering and per-country balance calculations, a Flask/Dash startup smoke test, a provisional 20% coverage floor, Ruff formatting/linting in CI, and a documented local setup workflow. The coverage threshold is a starting gate, not proof of broad behavior coverage.
- The same baseline deliberately used small DataFrame fixtures instead of Francois's local workbooks so tests can run without environment-owned production files. This tests filtering/calculation behavior, but does not yet validate workbook loading or transformation.
- Deployment automation shifted from vague DAC/CDH uncertainty to a concrete sequence: prove runner connectivity, configure DEV DAC/INTACT credentials, make the deployment package reproducible, prove a manual DEV deployment, then consider automatic DEV delivery and deliberate production promotion.
- GitHub Actions `workflow_dispatch` could not run from `dm-898` until the workflow exists on the default branch, so a narrowly scoped push trigger was added to test the diagnostic without merging to `main`.
- The `ubuntu` runner can run Atlas diagnostics and reach internal resources. DAC package index access, DAC-Tools installation, and DEV dashboard health eventually passed from the runner.
- The DEV dashboard initially failed TLS verification because the server did not supply two intermediate certificates. The existing `install-engie-ca` action installed the ENGIE root correctly, but the runner also needed a bundle containing `GSES Intermediate CA 1` and `GEM HQ Issuing CA1`.
- The temporary Atlas-specific certificate bundle was replaced by a shared `qrm-dms/sff-actions` action, `configure-engie-ca-bundle`, pinned from Atlas to exact commit `7c4c73c` through Atlas commit `9d236e9`. Shared CI and Atlas diagnostic/CI all passed. The shared action had not been released through protected `v1` at the end of the capture.
- Deployment remains blocked on authorized DEV DAC/INTACT credentials, CDH project URI, and role ARN being configured directly in GitHub, plus a reproducible deployment package/data path. No deployment occurred in the captured work.

## Open Questions

- UNCERTAIN: Whether S3 via Digital Acceleration tooling is the final production deployment path or only the current draft deployment path.
- UNCERTAIN: Which users, data sensitivity level, and operational decisions define the exact approval bar for Atlas.
- UNCERTAIN: Which DEV DAC/INTACT client, CDH project URI, and role ARN should be used for the first non-production Atlas deployment proof.
- UNCERTAIN: Whether `configure-engie-ca-bundle` should be promoted into the protected `sff-actions@v1` contract or remain pinned by SHA while it matures.

## Sources

- `sources/meetings/2026-09-08-1630-granola-atlas-discussion.md`
- `sources/codex-conversations/2026-09-08-codex-conversations.txt`
- `sources/codex-conversations/2026-09-09-codex-conversations.txt`
- `sources/codex-conversations/2026-09-10-codex-conversations.txt`

Last Updated: 2026-09-11
