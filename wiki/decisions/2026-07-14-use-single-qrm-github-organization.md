# Decision: Use Single QRM GitHub Organization

## Decision

QRM/DMS repositories should migrate into a single GitHub Cloud organization by default.

## Context

The July 14 QRM BE chapter meeting compared organization structure, repository visibility, runner costs, access management, and ADO-to-GitHub migration approaches. The source says multiple organizations were rejected because Walnut runners carry a fixed cost per organization, while GitHub-hosted runners are consumption-based.

## Rationale

One organization keeps the Walnut runner fixed cost to one org, allows department-wide and sub-team access through GitHub teams, and supports private-by-default repository visibility with default org-wide repository access disabled.

The operating rule captured in the meeting is to use GitHub-hosted runners when a workflow has no NG network dependency, and Walnut runners when a workflow needs private Artifactory, internal endpoints, or other NG network access.

## Tradeoffs

The single-org model reduces fixed runner cost and centralizes governance, but it requires careful team and repository permission design. Exceptions may still be needed for teams that need full separation.

## Sources

- `sources/meetings/2026-07-14-1700-granola-qrm-be-chapter-meeting.md`

Last Updated: 2026-07-14
