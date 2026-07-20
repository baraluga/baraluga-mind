# ADO iOS

## Summary

`ado-ios` is a Python CLI for migrating one Azure DevOps repository to GitHub at a time. The July 9 Copilot capture describes it as a deliberately small wrapper around `gh ado2gh migrate-repo` with safe defaults: private visibility, dry-run by default, no token prompts/storage, and command preview before execution.

The v1 cleanup work added Ruff and pytest, characterized existing behavior first, split the monolithic CLI into focused modules, and merged the resulting PR.

On July 13, the repository itself was moved from `qrm-dms` to Brian's enterprise account at `QN5792_engieco/ado-ios`. The transfer stayed private, preserved both branches and PR #1, removed inherited collaborators, and repointed the local clone.

On July 15, `ado-ios` became the working helper for the broader SFF/QRM repository migration wave. The current operating convention is to migrate Git refs and reachable history first, validate the GitHub target, then run `lock-source` to make the ADO source branches read-only unless Brian explicitly opts out.

## Details

- The tool defaults to ADO org `AA-SSO-EMEAI` and GitHub org `qrm-dms`.
- Main commands are migration, `pipeline-inventory`, and `lock-source`.
- By July 15, `migrate` skipped pipeline inventory by default; pipeline analysis is a separate explicit command and migration prompt step.
- Azure CLI metadata lookup can resolve repos case-insensitively and pre-fill the default branch when `az` and `ADO_PAT` are available.
- Commands are built as argument lists rather than shell strings, with rendered command previews for review.
- The refactor split a roughly 939-line `cli.py` into focused modules: `models`, `formatting`, `commands`, `az_client`, `process`, `prompts`, `args`, `reporting`, and `migration`, leaving `cli.py` as a thin dispatcher.
- Validation captured in the Copilot source: 115 tests, 93% coverage, Ruff clean, and a dry-run CLI smoke test.
- The PR was created, approved, and merged on July 9.
- An initial misunderstanding created an accidental private mirror at `baraluga/ado-ios`. It remains pending deletion because the `baraluga` CLI authorization did not yet include `delete_repo`; the correct enterprise repository is already verified and intact.
- The migration prompts now require a meaningful GitHub repository description based on source README/project metadata rather than carrying over generic workbook text.
- July 15 migrations and delegations used `ado-ios` for SFF repositories including `sff-ado-aws-iam-federation`, `cubicweb-infrastructure`, `pydanticai_tools`, `file-manager`, `common_data_model`, and `tdb_client`. Several repo-only migrations finished, but `common_data_model` and `tdb_client` pipeline transfers were still active.
- `tdb_client` was migrated to the workbook-provided destination `qrm-dms/sff-tool-tdb-cliennt`; validation found matching refs/history but source locking was left outstanding because GitHub automatically activated an inherited Dependency Graph workflow/run.
- July 20 repo-only SFF migrations used the current staged mirror flow for `user_ms_client`, `web_common`, and `user_microservice`. `user_ms_client` became `qrm-dms/sff-lib-user-ms-client` with 9 branches and 3 tags; `web_common` became `qrm-dms/sff-lib-web-common` with 8 branches and 1 tag; `user_microservice` became `qrm-dms/sff-ms-user` with 44 branches and 17 tags.
- After the July 20 migrations, the corresponding ADO source branches were locked read-only: 9/9 for `user_ms_client`, 8/8 for `web_common`, and 44/44 for `user_microservice`. Pipeline definitions were intentionally left for separate migration work.

## Open Questions

- UNCERTAIN: Whether v2 should add CI wiring for Ruff/pytest, more migration commands, or deeper pipeline inventory behavior.
- UNCERTAIN: Whether the accidental `baraluga/ado-ios` mirror has been deleted after the required GitHub device authorization.
- UNCERTAIN: Whether every successful July 15 SFF migration has already had all ADO source branches locked read-only; the July 20 SFF migrations listed above were source-locked.

## Sources

- `sources/copilot-conversations/2026-07-09-copilot-conversations.md`
- `sources/codex-conversations/2026-07-13-codex-conversations.md`
- `sources/codex-conversations/2026-07-15-codex-conversations.md`
- `sources/notes/2026-07-15.md`
- `sources/codex-conversations/2026-07-20-codex-conversations.md`

Last Updated: 2026-07-20
