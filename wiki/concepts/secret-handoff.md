# Secret Handoff

## Summary

Secret values should not be stored in durable collaboration tools. Requests can be tracked in Jira, Confluence, Teams, GitHub, or PR comments, but the value itself needs an ephemeral handoff path.

## Details

- July 8 Codex work on the SMP user-secrets Confluence page found an internal ENGIE `One time secrets` tool in the Confluence linked-applications menu.
- The page was updated so the default handoff is ENGIE `One time secrets`.
- A live unrecorded call is the fallback when a one-time secret link is not practical.
- Teams text chat can coordinate a handoff, but should not contain the secret value itself.

## Open Questions

- UNCERTAIN: Whether the ENGIE `One time secrets` tool has formal team-wide guidance beyond its availability in the Confluence app switcher.

## Sources

- `sources/codex-conversations/2026-07-08-codex-conversations.md`

Last Updated: 2026-07-09
