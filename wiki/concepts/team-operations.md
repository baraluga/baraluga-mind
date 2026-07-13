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

## Open Questions

- UNCERTAIN: Extraordinary/additional bonus question was raised with no answer captured.
- UNCERTAIN: Whether GitHub/Walnut should reuse and rename the existing SMP organization or create a new one.
- UNCERTAIN: Whether a native transfer is still required for any repository whose GitHub metadata must be preserved; it is no longer the default for Git-only migrations.
- UNCERTAIN: Whether Artifactory is active, pending, or not applicable for every migrated artifact path.
- UNCERTAIN: Whether Pyrene UAT/pre-prod should be always-on or on-demand.
- UNCERTAIN: `Auto` in the July 9 Maintainer-access request may refer to an org, repo, or internal system; confirm before creating durable tooling around it.

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

Last Updated: 2026-07-13
