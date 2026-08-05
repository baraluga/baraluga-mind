# SFF Walnut Migration

## Summary

The SFF migration moves Azure DevOps repositories and pipelines into the `qrm-dms` GitHub organization while replacing Azure Artifacts dependencies with tested Walnut Artifactory DEV flows where the package evidence supports that change. Repository transfer alone is not cutover: required CI, publication, deployment, downstream consumption, credentials, and rollback paths must be proven before Azure is retired.

By July 25, 2026, the active SFF estate audit counted 47 repositories: 23 GitHub-only, 1 GitHub-plus-Azure, 7 Azure-only, and 16 with neither pipeline. `sff-ms-service-desk` was the sole remaining dual-pipeline repository because its Azure deployment identity and environment contract were not yet reproducible safely in GitHub.

## Repository Naming Convention

Repositories within the SFF project use a purpose-based `sff-*` prefix:

| Prefix | Repository purpose |
|---|---|
| `sff-lib-` | Shared libraries |
| `sff-ms-` | Shared microservices |
| `sff-fw-` | Frameworks |
| `sff-tool-` | Utilities and tooling |
| `sff-infra-` | Infrastructure components |
| `sff-action-` | GitHub Actions |
| `sff-template-` | Repository templates |
| `sff-ai-` | AI assets and agents |
| `sff-data-` | Data components |
| `sff-doc-` | Documentation and standards |

## Python Artifact Migration

- The proven Python flow installs the ENGIE CA, configures Artifactory reads through organization variables and secrets, runs non-mutating host and Lambda-parity tests, builds `dist` once, retains it as a CI artifact, and publishes through a protected reusable workflow with authenticated no-cache readback.
- July 23-24 waves published or migrated the proven package chain, including `aws-clients==2.1.2`, `common-data-model==3.5.1`, Address `2.0.3`, Billing `4.2.2`, Notification `4.3.2`, and `data-common==2.1.2`. Service Desk was treated as a consumer/application rather than inventing a package-publication contract.
- `data_common` was recovered from active Azure repository `SFF/_git/data_common`, migrated to private `qrm-dms/sff-lib-data-common`, and published after preserving its Python 3.11/3.13 tests and fixing an sdist fixture omission.
- `sff-ms-computing-kernel` later published `computing_kernel==6.5.2` after its dependency readiness and release workflow were corrected.
- GAMS-dependent `sff-data-types` and `sff-tool-or-common` remain blocked on approved installer and licence custody. `sff-fw-limma` remains downstream-blocked until `python-datatypes` is available from Artifactory.

## Shared CI Contracts

- `qrm-dms/sff-actions` became the executable contract layer for CA installation, Artifactory configuration, tox tooling, Lambda parity, validation, distribution handling, and publication.
- The `python-package` reusable CI profile was piloted against `sff-lib-user-ms-client` and `sff-lib-web-common`, accepted after both passed authenticated reads, host tox, Lambda Python 3.13 parity, package build, and retained `dist`, then released behind protected `@v1`.
- A deterministic initializer can generate or check only the owned `ci.yml`, `publish.yml`, and `release.yml` callers for repositories that satisfy the accepted profile. It refuses ambiguous or ineligible repositories and does not edit source, tox, dependencies, metadata, or tests.
- A shared `install-python-tox-ci-tools` action standardized pinned public installation of `build`, `tox`, and `tox-uv`. The bounded rollout reached all ten documented eligible existing-CI consumers without changing their repository-specific test or artifact behavior.
- The organization-wide closeout found no honest reason for further whole-job centralization. Repositories with different coverage, sdist, deployment, or publication behavior keep composed shared actions rather than being forced into one reusable workflow.

## Agent Lifecycle

- The ADO Pipeline Modernizer initially accelerated pipeline reconstruction but repeatedly required manual takeover or executable validation to catch missing CA/NETRC boundaries, unsafe mutable images, incorrect action inputs, and dependency-readiness problems.
- On July 25, the migration agent, its offline prompt, and its dedicated validation script were deleted. The durable replacement is a human-first `sff-actions` storefront with tested copy-paste recipe families and narrower reusable contracts.
- Specialized governance agents continued for bounded work. The Deployment Runway Marshal builds inert, manual-only deployment readiness paths without activating cloud changes. The Pipeline Customs Broker produces source-led dependency and owner shopping lists without designing or deploying workflows.

## Deployment Readiness

- `sff-ms-service-desk` has GitHub-owned tests, builds, Lambda packaging, artifacts, and infrastructure imports, but Azure still uniquely owns environment mapping, AWS authentication, and CDK deployment. Missing AWS role metadata, protected GitHub environments, synth-safe account resolution, and runtime proof block cutover.
- `declic-backend` was mirrored into `qrm-dms`. Draft PR 1 has green CI and an intentionally failing deployment-readiness check that preserves the remaining branch/stage, infrastructure, image-provenance, dependency, security, smoke-test, environment, OIDC, and recovery gates.
- The SFF functional account cannot be requested until an SFF project exists in CMDB. The July 24 technical standup proposed finding someone with Snow/CMDB catalog access, creating the project, and then submitting the linked functional-account request.
- July 27 work published the missing historical `common-stacks==8.4.6` dependency from exact source and proved independent and combined resolution with `user==7.1.3`. It also added a tested `sff-actions` historical-package-backfill recipe and organization policy pointer.
- DeCliC application readiness advanced: `declic-backend` PR 4 merged with green CI, `declic-app` gained green credential-free CI, and `declic-infra` gained green credential-free CI after the historical dependency backfill. Deployment remains parked because environment ownership, secret custody, AWS OIDC, approvals, smoke tests, and rollback are not complete.
- July 28 environment cleanup consolidated active DeCliC GitHub environments into shared non-production and production boundaries. The cleanup did not create a deployable CD contract or authorize cloud changes.
- On August 4, Steffen's Azure DevOps repository `SFF/_git/mcp_proto` was migrated as a private Git-only mirror to `qrm-dms/sff-ai-halo`. The chosen name follows the SFF naming convention and the repository's own Halo product identity rather than using the generic source prototype name.
- The `mcp_proto` migration preserved all 29 commits, one `main` branch, and zero tags; the GitHub branch SHA matched Azure at `96f9578e...`, and Azure `main` was locked after verification. There were no Azure pipelines, classic releases, repository pipeline YAML, GitHub Actions workflows, tags, LFS, submodules, or active PRs to migrate.
- The remaining `sff-ai-halo` follow-up is operational, not migration parity: Steffen still needs access to the new private GitHub repository, and the repository's fresh install has an MCP 2.x dependency incompatibility because `mcp>=1.2.0` resolves to an incompatible major version.

## Open Questions

- UNCERTAIN: Who owns approval and custody for the GAMS installers and licence needed by Data Types and OR Common.
- UNCERTAIN: Which AWS roles, protected GitHub environments, smoke tests, and recovery procedure should authorize the Service Desk deployment cutover.
- UNCERTAIN: Whether all seven Azure-only pipelines should migrate in the current program or remain until their owners establish readiness.
- UNCERTAIN: Whether `sff-ai-halo` should pin its MCP dependency before adding CI, or keep the Git-only mirror unchanged until Steffen has access.

## Sources

- `sources/codex-conversations/2026-07-23-codex-conversations.md`
- `sources/codex-conversations/2026-07-24-codex-conversations.md`
- `sources/codex-conversations/2026-07-25-codex-conversations.md`
- `sources/codex-conversations/2026-07-26-codex-conversations.md`
- `sources/meetings/2026-07-24-1045-granola-walnut-migration-caucus.md`
- `sources/meetings/2026-07-24-1515-granola-technical-standup.md`
- `sources/notes/2026-07-27-ingest-handover-clarifications.md`
- `sources/codex-conversations/2026-07-27-codex-conversations.md`
- `sources/meetings/2026-07-28-1050-granola-declic-sharing.md`
- `sources/codex-conversations/2026-07-28-codex-conversations.md`
- `sources/codex-conversations/2026-08-04-codex-conversations.txt`

Last Updated: 2026-08-05
