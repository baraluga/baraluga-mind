# GitHub Copilot Custom Agents

## Summary

GitHub Copilot custom agents can be shared across the `qrm-dms` organization through the special repository `qrm-dms/.github`. The repository name is exact: GitHub discovers organization-level agents only from `.github` or `.github-private`, not from arbitrary names such as `sff-agents`.

The first organization-wide migration agent was an ADO Pipeline Modernizer. It helped establish executable migration contracts, but was decommissioned on July 25 after the reusable `sff-actions` contracts and human-facing recipe storefront became the more reliable operating model. Later agents are narrower: they assemble deployment-readiness evidence or dependency shopping lists without activating cloud changes.

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
- July 20 work tested the Modernizer on three real SFF migrations. The generated attempts for `sff-lib-user-ms-client` and `sff-lib-web-common` were insufficient without takeover: one made no change, while another missed pinned tools, artifact retention, the shared publisher, and non-mutating checks. The repaired workflows later passed CI and dry-run publishing.
- The `sff-ms-user` Modernizer attempt was stronger but still needed manual repair: source formatting failed, the Lambda image was mutable, corporate CA forwarding into Docker was incomplete, and version metadata generation could fail silently. After focused fixes, PR #1 became green with 72 tests, 85.54% coverage, Lambda parity, `dist` artifacts, and coverage artifacts.
- Those misses were converted into stronger `sff-actions` validation rather than only prompt changes. The live `validate-python-migration@v1` contract was advanced to `0f9cdc8` after `sff-actions`, the organization Modernizer fixture, and representative consumers were green.
- The hardened validator now enforces authenticated read-feed setup, ENGIE CA setup, `AZURE_ARTIFACTS_READ_PAT` read mode, Docker private-feed environment propagation, matching read-only `.netrc` and CA mount paths, `UV_SYSTEM_CERTS=true`, SHA-256-pinned Lambda images, and a clear boundary between structural validation and runtime CI evidence.
- The stronger validator exposed existing debt in repositories then named `sff-common-data-model` and `sff-microservice-meteomatics-client`: mutable Lambda images and pre-existing mutating tox environments. These were left untouched in the source conversation and are tracked in [[actions]].
- A July 21 Modernizer attempt on the freshly migrated `sff-infra-strategy` repository completed with no changes because the Copilot runner could not reach `mcp-registry.walnut.myengie.com`. Local reconstruction also found a repository-specific readiness issue: the ADO deploy step used `cd ./internal-web`, but the checked repository evidence pointed to `strategy-common/` as the CDK app directory. The repo was rolled back from GitHub before pipeline modernization proceeded.
- July 23-25 work converted the strongest repeated Python CI behavior into accepted reusable `sff-actions` contracts, a deterministic initializer, and a human-first recipe storefront. See [[sff-walnut-migration]].
- On July 25, the Pipeline Modernizer agent, its offline prompt, and its dedicated validation script were removed after the organization-wide CI closeout. The independently useful executable actions, reusable workflows, validators, profile contracts, templates, and structural recipe tests remain.
- The Deployment Runway Marshal creates inert, manual-only deployment readiness paths. A governance `403` must produce one handoff note and continued execution under its embedded contract; it is not itself a repository-readiness blocker.
- The Pipeline Customs Broker is intentionally analysis-oriented. It traces checked-in Azure dependencies and produces a concise owner/resource shopping list plus a reconciled evidence appendix; it does not design workflows, retrieve secrets, authenticate to cloud providers, deploy, publish, or delete Azure configuration.
- The strategy repo episode reinforces the current boundary: infrastructure/deployment modernization needs repo-local evidence for the real app directory, validated OIDC role naming such as `AWS_ROLE_ARN_NOPROD` / `AWS_ROLE_ARN_PROD`, and access to live shared-action contracts. If runner network access blocks registry lookup, the handoff must supply those contracts as evidence rather than letting the agent infer them.

## Open Questions

- UNCERTAIN: Whether prompt-only Modernizer guidance can consistently prevent misses such as omitted CA forwarding or mutable Lambda images; July 20 evidence suggests executable validation is the reliable control.
- UNCERTAIN: Which additional organization-level Copilot agents are worth contributing to `qrm-dms/.github`.
- UNCERTAIN: Whether `Validate migration contract` should become a required branch-protection check after the next real migration trial.
- UNCERTAIN: Whether GitHub-side Copilot runners will be granted access to `mcp-registry.walnut.myengie.com`, or whether registry-derived contracts must be supplied out-of-band in each infrastructure modernization handoff.
- UNCERTAIN: Whether `strategy-common/` is definitively the intended deployment directory for `strategy-common-infra`; it was the proven checked-in CDK path, but the ADO pipeline's `internal-web` path was stale or unexplained.
- UNCERTAIN: Whether the Deployment Runway Marshal and Pipeline Customs Broker will remain durable organization workflows after their current DeCliC proof-of-concept phase.

## Sources

- `sources/codex-conversations/2026-07-15-codex-conversations.md`
- `sources/codex-conversations/2026-07-17-codex-conversations.md`
- `sources/codex-conversations/2026-07-20-codex-conversations.md`
- `sources/codex-conversations/2026-07-21-codex-conversations.md`
- `sources/codex-conversations/2026-07-24-codex-conversations.md`
- `sources/codex-conversations/2026-07-25-codex-conversations.md`
- `sources/codex-conversations/2026-07-26-codex-conversations.md`

Last Updated: 2026-07-27
