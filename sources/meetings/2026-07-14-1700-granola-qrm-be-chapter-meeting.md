# QRM BE Chapter Meeting

Source type: Granola meeting notes

Meeting ID: `915b15a3-77bb-4502-8a5f-438c08be2705`

Meeting date/time: Jul 14, 2026 5:00 PM GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves available Granola notes/summaries. It is not a verbatim transcript.

## Discussion Notes / Summary

### GitHub Cloud Organization Structure

- Single GitHub organization chosen for all QRM/DMS repositories.
  - Multiple orgs rejected due to fixed cost per org for Walnut Runners, at EUR 600/year each.
  - GitHub-hosted runners: pay per consumption, no fixed cost.
  - Walnut runners: fixed cost per org, includes 10,000 min/month bundle, then pay-per-use.
- Repository visibility set to private by default.
  - "Internal" repos would be visible across all of NG; not used.
  - Default access to all repos disabled at org level.
- Teams feature used to manage access.
  - Teams linked to repos with read or write permissions.
  - Global QRM-all team being created by David for department-wide sharing.
  - Sub-teams per QRM team also in progress.
- Governance doc in Confluence covers naming conventions and team creation.
- Goal: migrate all QRM repos from ADO into this single org; exceptions possible for teams needing full separation.

### Two Runner Types

- GitHub-hosted runners, such as `ubuntu-latest`: public internet access, no NG network access.
- Walnut runners, self-hosted and managed by the Walnut team: run inside NG network and can reach private Artifactory, internal endpoints, etc.
- Rule of thumb: use GitHub runner when no NG dependencies; use Walnut runner otherwise.
  - Cost benefit: GitHub runners are cheaper for jobs that do not need internal access.

### ADO to GitHub Migration Approaches

- Three options identified by Brian, based on SMP project experience:
  1. GitHub UI import: specify ADO URL and PAT; simple but limited.
  2. `ado2gh` CLI extension: uses GitHub Enterprise Import API; brings PRs, issues, and wiki; requires admin, owner, or migrator role.
  3. Git mirror push: clone from ADO, push with `--mirror` flag to GitHub, redirects clones automatically.
- SMP used the mirror approach: simplest, CLI-scriptable, good for bulk migration.
  - 3 of 4 SMP repos already migrated.
  - Downside: no ADO metadata, such as PRs or issues, carried over; team agreed this is acceptable.
- Pipelines are never migrated automatically regardless of method.
  - Pipeline recreation is the main migration effort.
  - Copilot can help convert Azure Pipelines YAML to GitHub Actions.

### Friction Points and Solutions

- Private Artifactory access, such as tsdb or cdh, requires Walnut runner.
  - Request form available in Walnut Confluence, routes to service desk.
- Missing certificates on Walnut runners.
  - Company laptops handle certs via Zscaler; Walnut runners do not inherit this.
  - Solution: install NG certificate explicitly in the pipeline.
  - Brian built a reusable `install-ngca` GitHub Action in a centralized `sff-actions` repo.
  - Any consuming pipeline can call this action; avoids repeating the setup.
  - Open question: whether Walnut team should pre-bake certs into runner images, to be raised with Walnut team via service desk or Yammer/Viva Engage community.
- AWS permissions: IAM users no longer allowed; OIDC with federated credentials now required for GitHub Actions deploying to AWS, as a one-time setup per org.
- Shared libraries: ADO used npm/PyPI feeds; GitHub equivalent is Walnut Artifactory.
  - Harbor raised as an alternative for Python packages.
  - JFrog/Artifactory has per-developer, per-component access complexity; Harbor offers project-level and robot user flexibility.
  - To be discussed further in VE chapter: pros/cons of Artifactory vs. Harbor.

## Next Steps / Action Items Present in Granola

- Raise certificate pre-installation request with Walnut team.
  - Ask whether Walnut runners can ship with NG certs pre-installed; use service desk ticket or Viva Engage Walnut community channel.
- Discuss Artifactory vs. Harbor governance in VE chapter.
  - Evaluate pros/cons for publishing shared Python/npm packages across QRM teams.
- Share Viva Engage Walnut community link with the group.
  - For teams with migration questions to reach the Walnut team directly.

Last Updated: 2026-07-14
