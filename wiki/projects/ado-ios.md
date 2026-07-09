# ADO iOS

## Summary

`ado-ios` is a Python CLI for migrating one Azure DevOps repository to GitHub at a time. The July 9 Copilot capture describes it as a deliberately small wrapper around `gh ado2gh migrate-repo` with safe defaults: private visibility, dry-run by default, no token prompts/storage, and command preview before execution.

The v1 cleanup work added Ruff and pytest, characterized existing behavior first, split the monolithic CLI into focused modules, and merged the resulting PR.

## Details

- The tool defaults to ADO org `AA-SSO-EMEAI` and GitHub org `qrm-dms`.
- Main commands are migration, `pipeline-inventory`, and `lock-source`.
- Azure CLI metadata lookup can resolve repos case-insensitively and pre-fill the default branch when `az` and `ADO_PAT` are available.
- Commands are built as argument lists rather than shell strings, with rendered command previews for review.
- The refactor split a roughly 939-line `cli.py` into focused modules: `models`, `formatting`, `commands`, `az_client`, `process`, `prompts`, `args`, `reporting`, and `migration`, leaving `cli.py` as a thin dispatcher.
- Validation captured in the Copilot source: 115 tests, 93% coverage, Ruff clean, and a dry-run CLI smoke test.
- The PR was created, approved, and merged on July 9.

## Open Questions

- UNCERTAIN: Whether v2 should add CI wiring for Ruff/pytest, more migration commands, or deeper pipeline inventory behavior.

## Sources

- `sources/copilot-conversations/2026-07-09-copilot-conversations.md`

Last Updated: 2026-07-09
