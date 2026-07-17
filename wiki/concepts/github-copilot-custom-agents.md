# GitHub Copilot Custom Agents

## Summary

GitHub Copilot custom agents can be shared across the `qrm-dms` organization through the special repository `qrm-dms/.github`. The repository name is exact: GitHub discovers organization-level agents only from `.github` or `.github-private`, not from arbitrary names such as `sff-agents`.

The first durable agent direction is an ADO Pipeline Modernizer. Its job is to help rebuild Azure DevOps YAML pipelines as idiomatic GitHub Actions workflows while preserving the pipeline's externally observable contract and documenting every intentional behavior change.

## Details

- Organization-wide agents live under `qrm-dms/.github/agents/*.agent.md`.
- `qrm-dms/.github` should remain the organization-facing configuration repository: Copilot agents, organization profile files, issue/PR templates, workflow templates, and governance documentation.
- `qrm-dms/sff-actions` should remain the executable automation library: composite actions, reusable workflows, CI for those actions/workflows, and stable tags such as `v1`.
- The ADO Pipeline Modernizer replaced the initial smoke-test agent on July 15 and was pushed with the no-scope conventional commit `feat: add ADO pipeline modernizer agent`.
- The agent is intentionally standalone. It should work from the migrated repository's checked-in ADO YAML, templates, docs, manifests, and existing GitHub workflow conventions; it should not depend on `ado-ios`.
- The modernization principle is to preserve the source pipeline's contract, not mechanically reproduce Azure DevOps structure. Deployment, publishing, or infrastructure workflows should default to `workflow_dispatch` until credentials, environments, approvals, runners, and validation are confirmed.
- A July 15 follow-up added an instruction that external GitHub Actions versions must be verified against current release/tag metadata rather than chosen from model memory or copied examples.
- July 17 Meteomatics/TDB work showed that prompt instructions alone were not enough: the modernizer already had the container credential-boundary rule, but the generated workflow still failed to mount `.netrc` into the Lambda Docker container. The resulting direction is to move correctness into executable guardrails.
- `qrm-dms/sff-actions` now exposes `validate-python-migration@v1`, a Ruby-based dependency-free validator with a machine-readable Python migration contract. It checks split CI/publish workflows, non-overlapping triggers, tested artifact publishing, dry-run defaults, Docker credential and CA mounts, non-mutating checks, pinned bootstrap tools, approved action versions, job timeouts, and least-privilege permissions.
- The modernizer now requires a local validator pass and a dedicated migration-contract CI job before handoff. Common Data Model, Meteomatics, and TDB enforce the released validator action in CI and passed with zero warnings in the July 17 evidence.
- Ruby was chosen for the validator because GitHub-hosted runners include Ruby and its standard library provides YAML parsing without installing packages. The portability risk is explicit: if Ruby availability becomes a real problem for local or Copilot environments, a bundled Node action may be justified.

## Open Questions

- UNCERTAIN: Whether the ADO Pipeline Modernizer plus validator can one-shot a genuinely untouched Python repository migration; the July 17 work proved the guardrail on known repositories, not a fresh migration.
- UNCERTAIN: Which additional organization-level Copilot agents are worth contributing to `qrm-dms/.github`.
- UNCERTAIN: Whether `Validate migration contract` should become a required branch-protection check after the next real migration trial.

## Sources

- `sources/codex-conversations/2026-07-15-codex-conversations.md`
- `sources/codex-conversations/2026-07-17-codex-conversations.md`

Last Updated: 2026-07-17
