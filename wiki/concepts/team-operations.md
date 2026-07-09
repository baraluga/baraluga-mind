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
- Artifact migration was still unsettled. SFF components may need dedicated repos for common artifacts, SMP Common may become a shared artifact source, and ADO artifacts remain in use until cutover.
- July 8 AWS migration notes introduced a centralized technical-activities board with separate epics for AWS migration, Walnut migration, and security remediation, charged per project instead of one blanket bucket.
- Pyrine/GMR migration notes mention default EFS backup in the new DMS account, 35-day warm backup, daily incremental backup, and Pyrine storage cost estimated around USD 600-700/month for about 13 TB.
- Pyrine environment scope was unresolved because a resource-heavy always-on machine was estimated around USD 2,000/month.
- Atlassian migration was virtually moved around July 1, with actual migration still coming.
- Sentry will be recreated from scratch in Europe, with previous logs accepted as lost.
- Portfolio topics mentioned: JMR v2, AVST index builder, Onset, Platform, Sign Ups, SMP, carbon emissions platform, Delphi CLI, APM, and Click.
- Sign Ups AKS migration covered Azure resource groups, naming conventions, storage accounts, Key Vault, workload identity, Bicep, and IT dependencies.

## Open Questions

- UNCERTAIN: Extraordinary/additional bonus question was raised with no answer captured.
- UNCERTAIN: Whether GitHub/Walnut should reuse and rename the existing SMP organization or create a new one.
- UNCERTAIN: Whether GitHub CLI transfer is officially preferred for all existing repos or only the observed repo migration case.
- UNCERTAIN: Whether Artifactory is active, pending, or not applicable for every migrated artifact path.
- UNCERTAIN: Whether Pyrine UAT/pre-prod should be always-on or on-demand.

## Sources

- `sources/meetings/2026-06-23-0945-granola-team-meeting.md`
- `sources/meetings/2026-07-02-1700-granola-application-team-meeting.md`
- `sources/meetings/2026-07-07-0945-granola-weekly-team-meeting.md`
- `sources/meetings/2026-07-07-1415-granola-standup.md`
- `sources/meetings/2026-07-08-0945-granola-am-standup.md`
- `sources/meetings/2026-07-08-1330-granola-walnut-migration-planning.md`
- `sources/meetings/2026-07-08-1514-granola-aws-migration-standup.md`
- `sources/copilot-conversations/2026-07-09-copilot-conversations.md`

Last Updated: 2026-07-09
