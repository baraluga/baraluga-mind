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
- September 15 Codex work established the Intact/CDH binding model for Atlas deployment: create an Intact service application, subscribe it to `api.cdh`, then add the service application's client ID to the CDH project tag `gem_okta_client_id`. Atlas DEV initially had no such tag, while the working SMP comparison project did.
- Atlas DEV end-to-end deployment was proven through GitHub Actions after the CDH client binding and GitHub secrets/variables were configured. The captured evidence says service credentials were verified, 68 tests passed, live workbooks were preserved and smoke-tested, ECS rollout and ALB targets were healthy, and the dashboard loaded after authenticated Okta login. The recorded green run was `https://github.com/qrm-dms/atlas-dash-frontend/actions/runs/34951067529`.
- PROD remains incomplete because its real Intact service-client ID/secret and runtime target values were not available. The CDH trust and policies were observed as ready, but the GitHub PROD service-client ID still used a placeholder in the capture.
- Brian and Francois agreed that Atlas continuous deployment should run only from `dev` and `prod` branches. `main` is the development branch, while pushes to `dev` or `prod` are release requests for the matching environment; pull requests and other branches validate without deployment.
- A September 15 handover audit found that the repository foundation was sufficient for ordinary fixes and feature work, but the contributor documentation still needed simplification around current deployment behavior and platform-specific setup commands before handoff.
- On September 17, the Atlas release design shifted from branch-triggered deployment to a manual GitHub Actions workflow. The workflow asks for target environment and release type, with data refreshes using the code already deployed in that environment. This keeps code release and data refresh explicit while avoiding dummy commits for workbook-only changes.
- Atlas data refresh now expects monthly paired CDH stages from `masterupstream` and `masterdownstream`; the app needs upstream for generation/capacity and downstream for sales/PPA figures. Francois confirmed he uploads downstream separately for the same month.
- The initial GitHub runner access probe for the Atlas service credentials passed, and the release preflight correctly stopped before deployment while old daily stages still existed. Later work added a default dry-run mode through a `Deploy after validation` checkbox and a GitHub run summary that reports collected stages, row counts, validation, smoke checks, and outcome without exposing raw business data.
- `dm-898` was merged and pushed to `main` on September 17 with CI passing, making **Deploy Atlas -> Run workflow** visible. No deployment was triggered during the merge; Francois still needed to clean CDH stages before trying `DEV -> data-only`.
- The September 17 Tech Lead Roundtable framed Brian's Atlas role as consultation rather than feature ownership. DMS is not taking on Dash skills or ongoing deployment accountability; the near-term objective is to make Francois more autonomous through CI/CD enablement and repository guardrails.

## Open Questions

- UNCERTAIN: Whether S3 via Digital Acceleration tooling is the final production deployment path or only the current draft deployment path.
- UNCERTAIN: Which users, data sensitivity level, and operational decisions define the exact approval bar for Atlas.
- UNCERTAIN: Whether `configure-engie-ca-bundle` should be promoted into the protected `sff-actions@v1` contract or remain pinned by SHA while it matures.
- UNCERTAIN: Which real Intact PROD service-client ID/secret and runtime target values Francois will provide for the first production Atlas deployment.
- UNCERTAIN: Whether Francois has completed CDH cleanup so only monthly paired upstream/downstream stages remain for DEV data-only validation.
- UNCERTAIN: Whether the Dash Expert agent has been tested after the September 17 merge; Brian's API credits were exhausted at the Atlas checkpoint.

## Sources

- `sources/meetings/2026-09-08-1630-granola-atlas-discussion.md`
- `sources/codex-conversations/2026-09-08-codex-conversations.txt`
- `sources/codex-conversations/2026-09-09-codex-conversations.txt`
- `sources/codex-conversations/2026-09-10-codex-conversations.txt`
- `sources/meetings/2026-09-15-1-1-bong.md`
- `sources/codex-conversations/2026-09-15-codex-conversations.txt`
- `sources/meetings/2026-09-17-1630-granola-atlas-checkpoint.md`
- `sources/meetings/2026-09-17-1700-granola-tech-lead-roundtable.md`
- `sources/codex-conversations/2026-09-17-codex-conversations.txt`

Last Updated: 2026-09-18
