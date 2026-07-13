# Decision: Skip PR History for Walnut Migration

## Decision

For Walnut ADO-to-GitHub migration, commit history and commit messages are sufficient. Migrating PR history is not worth pursuing through the ADO-to-GitHub extension and migrator-role path.

## Context

The July 9 technical team standup compared GitHub import UI behavior with the ADO-to-GitHub extension. The GitHub import UI includes commits and commit messages but not PRs. The extension can support PRs but requires migrator role.

## Rationale

The team agreed the extra role and process overhead did not justify preserving PR history for this migration.

The July 13 presentation work made the acceptance boundary explicit: migration is complete when the repository is usable in Walnut and all existing ADO pipelines, including deployment, are recreated and working. PRs, Issues, and other ADO metadata remain out of scope.

## Tradeoffs

This keeps migration simpler and avoids a migrator-role dependency. The cost is that old ADO PR discussions will not be preserved in GitHub as native PR history.

## Sources

- `sources/meetings/2026-07-09-1515-granola-technical-team-standup.md`
- `sources/codex-conversations/2026-07-13-codex-conversations.md`

Last Updated: 2026-07-13
