# Team Operations

## Summary

Team operations notes from late June and early July 2026 covered recruitment, office routines, anniversaries, AI tooling, portfolio demand, migrations, and cross-team planning. Most items are coordination context rather than durable decisions.

## Details

- First anniversary celebration was planned before July 15, with a survey to decide the celebration date.
- Office credits were expected to be auto-applied by July, and some members still needed to complete June office visits.
- Tempo project target completion was June 30; the later application meeting said the Tempo timesheet parallel run was complete with remaining configuration issues.
- Demand management topics included AWS migration, prosumer penetration testing, Lean/GMR migration, and Transvect database feedback.
- GitHub/Walnut migration direction was one shared organization instead of one org per project because of runner cost.
- Open GitHub/Walnut question: reuse and rename the existing SMP organization or create a new one.
- July 7 weekly team notes say one-organization consolidation was underway, members and targets should be set before the end of July, cleanup/migration was planned after summer while Europeans are on vacation, and git rules/policies still needed definition.
- July 7 standup notes say Brian used GitHub CLI to transfer an existing repo/update its remote, rather than Guido's import process. The transfer path appeared better for existing repos because local remotes can be updated in place.
- July 8 Walnut migration planning split repo migration into ADO-direct and non-GitHub-source paths. The proposed sequence was read-only repo migration, recreate GitHub pipelines, add users after pipelines stabilize, then turn off ADO access after a few days.
- July 8 notes say most migration effort is pipeline recreation rather than repo transfer. Michael was execution lead, Brian handled support/automation/governance oversight, and Alexander owned governance pipeline and master branch protection settings.
- [[ado-ios]] is a small Python CLI for one-repo-at-a-time Azure DevOps to GitHub migration through `gh ado2gh migrate-repo`, with dry-run defaults and source-lock support.
- July 9 AM standup clarified that the migrator role does not cover repository migration by default, bulk pipeline migration may be an option, and the team principle is to understand the manual UI process before automating.
- July 9 technical standup decided not to pursue migrator role for PR history. See [[2026-07-09-skip-pr-history-for-walnut-migration]].
- July 9 technical standup said ABT dashboard was migrated as a test case using GitHub CLI and Azure CLI without migrator role. Click migration should wait until JB's security remediation work is complete because commits during migration can leave leftovers.
- Artifact migration was still unsettled. SFF components may need dedicated repos for common artifacts, SMP Common may become a shared artifact source, and ADO artifacts remain in use until cutover.
- July 8 AWS migration notes introduced a centralized technical-activities board with separate epics for AWS migration, Walnut migration, and security remediation, charged per project instead of one blanket bucket.
- Pyrene/GMR migration notes mention default EFS backup in the new DMS account, 35-day warm backup, daily incremental backup, and Pyrene storage cost estimated around USD 600-700/month for about 13 TB.
- Pyrene environment scope was unresolved because a resource-heavy always-on machine was estimated around USD 2,000/month.
- Atlassian migration was virtually moved around July 1, with actual migration still coming.
- Sentry will be recreated from scratch in Europe, with previous logs accepted as lost.
- Portfolio topics mentioned: GMR / Model Runner v2, AVST index builder, Onset, Platform, Sign Ups, SMP, carbon emissions platform, Delphi CLI, APM, and Click.
- Sign Ups AKS migration covered Azure resource groups, naming conventions, storage accounts, Key Vault, workload identity, Bicep, and IT dependencies.
- A July 12 `smp-japan` migration attempt showed that native GitHub transfers can create an approval window where neither organization URL is accessible. For migrations that only need branches, tags, and commit history, the preferred operational method is now a staged private mirror with the source left available until the target is verified.
- The July 13 migration presentation settled the current comparison: plain mirror push and GitHub Importer preserve Git source/history without a Migrator role; `ado2gh` uses GitHub Enterprise Importer and requires an organization owner or Migrator role. GitHub Importer does not preserve ADO PRs, while `ado2gh` can preserve PRs and branch policies.
- The current package path is transitional: migrated repositories may publish to and install from Walnut Artifactory, GitHub Packages remains a secondary option to assess by package type, and some consumers still use ADO Artifacts through a technical-account PAT. The final standard is not yet fixed.
- Migration is considered done when the repository is usable in Walnut and every existing ADO pipeline, including deployment, has been recreated and proven. PRs, Issues, and other ADO metadata are explicitly out of scope for the current program.
- The July 14 QRM BE chapter meeting chose one QRM/DMS GitHub Cloud organization by default. See [[2026-07-14-use-single-qrm-github-organization]].
- Repositories in the QRM org should be private by default, with org-wide default repository access disabled. GitHub teams provide read/write access, including a planned department-wide QRM-all team and sub-teams per QRM group.
- The migration approach remains pragmatic: Git mirror push is the simplest scriptable path when Git history is enough; GitHub UI import is simpler but limited; `ado2gh` can preserve richer ADO metadata but needs elevated roles. Pipelines must be recreated regardless of migration method.
- Runner selection guidance from the July 14 chapter: use GitHub-hosted runners when no NG network access is needed; use Walnut runners for workflows that need private Artifactory or internal endpoints.
- The package-hosting discussion expanded to include Harbor as an alternative to JFrog/Artifactory for shared Python/npm packages, especially where project-level access or robot users may be easier than per-developer/per-component access.
- A July 15 clarification says Walnut runner certificate pre-installation and Harbor package governance are real topics, but not current confirmation priorities.
- July 15 SFF migration work moved from ad hoc repo selection toward a tracker-driven process. A local tracker was created from the SharePoint workbook, grouped by workbook priority, owner, owner confirmation, commit activity, and pipeline complexity.
- The first high-priority trivial migrations were grouped by low red tape and owner coordination. The completed local set included IAM federation, Cubicweb infrastructure, Pydantic tools, Certificate, Kubestat, Cmdutil, and File Manager. `common_data_model` and `tdb_client` became the capped active pipeline-transfer pair.
- The workbook `Action` column became a required gate after `quality_tools` was initially treated as an easy migration candidate even though the workbook action was `Archive`. Later audit separated `Migrate` rows from archive/done rows.
- A full workbook pipeline audit found 172 rows marked `Migrate`: 50 `TRIVIAL`, 2 `EASY`, and 120 `HARD` under the strict rule that no pipeline is trivial, a pipeline with no variables/secrets is easy, and anything credentialed, variable-driven, broken, unreadable, or unproven is hard.
- For migrated GitHub pipelines that need the shared Azure Artifacts feed, the preferred model is organization-level variables for non-secret coordinates and organization-level secrets for Azure Artifacts PATs. `qrm-dms/.github` remains the organization-facing configuration/profile/agent repository, while `qrm-dms/sff-actions` remains the versioned executable automation library.
- A July 16 note says the `tdb_client` pipeline migration was completed. The same note says the ADO backwards-compatibility action was set up in `sff-actions`.
- July 17 SFF migration work hardened the standard migrated Python package shape. Meteomatics was fixed to mount Azure Artifacts `.netrc` into its Lambda Docker compatibility test, split CI from manual publishing, remove duplicate push/PR runs, use the shared tested-artifact publisher, and pass a dry-run publish. TDB kept the split release model, removed duplicate CI triggers, pinned public bootstrap tools, and passed CI plus dry-run publishing.
- The organization-level modernizer and `sff-actions` now treat migration correctness as an executable contract: generated repositories should run `validate-python-migration@v1` locally and in CI, rather than relying only on Copilot prompt adherence.
- Repository ruleset cleanup on July 17 found automatic Copilot review only on active `smp-japan`, plus a stranded ruleset on archived legacy `DMS-Scraper-and-Models-Platform/smp-india`. The legacy ruleset was removed after temporary unarchive, and `smp-japan` kept its branch protections while removing the `copilot_code_review` rule.
- July 20 SFF work migrated `user_ms_client` to `qrm-dms/sff-lib-user-ms-client`, `web_common` to `qrm-dms/sff-lib-web-common`, and `user_microservice` to `qrm-dms/sff-ms-user`. Git refs matched source branches/tags, ADO source branches were locked, migrated GitHub CI went green, and manual publisher dry-runs passed without package upload.
- The SFF naming convention was clarified with Bong's rule: deployed microservices use `sff-ms-*`, while importable clients use `sff-lib-*-client`. The SharePoint workbook's red-font repository names appear to indicate naming corrections, not visibility issues.
- A temporary org-wide `All-repository admin` role enabled a confirmed batch rename of 20 SFF repositories. `sff-actions` and stale/no-op `sff-tool-tdb-client` were intentionally left unchanged. Brian clarified on 2026-07-21 that all repo admin will be revoked at the end of July.
- Public-facing Confluence migration guidance was published as three child pages: repository migration, pipeline migration, and `Artifact migration (WIP)`. The artifact page is explicitly WIP/TBD because package hosting, historical artifact migration, retention, permissions, and consumer cutover are not final.
- A July 20 standup said Chantal Lee leads a UK data-governance project, "Empowering Users with Data", with possible SMP overlap. The key unresolved operating question is whether SMP provides platform-only support or active delivery support for teams such as UK data governance and Iberia.
- July 21 migration planning created a separate Markdown audit and polished spreadsheet from the master workbook's unmigrated rows. The audit found 126 unmigrated records, with 124 verified latest commits, one empty repository (`NEMO / NEMO`), and one Azure DevOps URL that returned missing or inaccessible (`Prosumer / prosumer-shared-tools`). A later scope cut removed 16 PLEXOS and pegase repositories from the workbook, leaving 110 in-scope records sorted oldest activity first.
- The migration-age workbook was kept as a companion artifact rather than merged into the live shared SharePoint master workbook. The rationale was to avoid disrupting an actively edited master while preserving a timestamped, replaceable audit snapshot. A future integration could add namespaced audit sheets directly to the SharePoint workbook if stakeholders prefer one file.
- July 21 Git-only migration moved `wss_client` to private `qrm-dms/sff-lib-wss-client`, preserved 9 branches and 12 tags, set default branch `master`, and locked all 9 ADO source branches. `strategy-common-infra` was briefly migrated to `qrm-dms/sff-infra-strategy`, but the migration was rolled back the same day: the GitHub repository was deleted, and the ADO `main` branch was unlocked after pipeline modernization evidence showed the repo was not ready.

## Open Questions

- UNCERTAIN: Extraordinary/additional bonus question was raised with no answer captured.
- UNCERTAIN: Whether GitHub/Walnut should reuse and rename the existing SMP organization or create a new one.
- UNCERTAIN: Whether a native transfer is still required for any repository whose GitHub metadata must be preserved; it is no longer the default for Git-only migrations.
- UNCERTAIN: Whether Artifactory is active, pending, or not applicable for every migrated artifact path.
- UNCERTAIN: Whether Pyrene UAT/pre-prod should be always-on or on-demand.
- UNCERTAIN: `Auto` in the July 9 Maintainer-access request may refer to an org, repo, or internal system; confirm before creating durable tooling around it.
- UNCERTAIN: Whether `sff-tool-tdb-cliennt`, `sff-tool-federatioam-federation`, and `sff-tool-certificatte` are intentionally misspelled destination names or workbook artifacts that should be corrected later.
- UNCERTAIN: Whether the newly migrated SFF `master` branches should receive branch protection immediately or wait for the broader GitHub governance rules.
- UNCERTAIN: `Dexter` remains unidentified; Brian did not recognize what this referred to in the July 20 standup.
- UNCERTAIN: Whether `Chantal Lee` is the exact spelling from the July 20 standup.
- UNCERTAIN: Whether the July 21 migration-age audit should stay as a companion workbook, be uploaded beside the SharePoint master, or be integrated as namespaced sheets in the master workbook.
- UNCERTAIN: Whether `strategy-common-infra` should be migrated only after its stale ADO deploy path and GitHub OIDC deployment model are fixed, or whether it should remain out of the current batch.

## Sources

- `sources/meetings/2026-06-23-0945-granola-team-meeting.md`
- `sources/meetings/2026-07-02-1700-granola-application-team-meeting.md`
- `sources/meetings/2026-07-07-0945-granola-weekly-team-meeting.md`
- `sources/meetings/2026-07-07-1415-granola-standup.md`
- `sources/meetings/2026-07-08-0945-granola-am-standup.md`
- `sources/meetings/2026-07-08-1330-granola-walnut-migration-planning.md`
- `sources/meetings/2026-07-08-1514-granola-aws-migration-standup.md`
- `sources/copilot-conversations/2026-07-09-copilot-conversations.md`
- `sources/meetings/2026-07-09-0945-granola-am-standup.md`
- `sources/meetings/2026-07-09-1515-granola-technical-team-standup.md`
- `sources/codex-conversations/2026-07-12-codex-conversations.md`
- `sources/codex-conversations/2026-07-13-codex-conversations.md`
- `sources/meetings/2026-07-14-0945-granola-team-meeting.md`
- `sources/meetings/2026-07-14-1700-granola-qrm-be-chapter-meeting.md`
- `sources/notes/2026-07-15-ingest-handover-clarifications.md`
- `sources/codex-conversations/2026-07-15-codex-conversations.md`
- `sources/notes/2026-07-15.md`
- `sources/notes/2026-07-16.md`
- `sources/codex-conversations/2026-07-17-codex-conversations.md`
- `sources/meetings/2026-07-20-1415-granola-standup.md`
- `sources/meetings/2026-07-20-1645-granola-ta-standup.md`
- `sources/codex-conversations/2026-07-20-codex-conversations.md`
- `sources/notes/2026-07-20.md`
- `sources/codex-conversations/2026-07-21-codex-conversations.md`

Last Updated: 2026-07-21
