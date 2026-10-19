# SMP Local Workspace

## Current State

As of 2026-10-20. `/Users/qn5792/repos/smp` is a parent workspace, not a git repository. Its retained repositories are `apac-tsdb-scraper`, `smp-common`, `smp-dashboard`, `smp-india`, `smp-japan`, and `smp-tool`; `sff-actions` moved to `~/repos/sff-actions` because it belongs to the SFF team. Root-level config includes `AGENTS.md`, `CLAUDE.md`, `Makefile`, `.envrc`, `.claude`, `.vscode`, and `.cursor`.

`CLAUDE.md` now imports `AGENTS.md` in the five tracked SMP repositories so Claude Code loads the actual instructions. Root `.ignore` excludes archives, dependencies, caches, generated decks, and data from agent search. Loose evidence moved under `notes/<topic>/`; archival material and retired project sources are in `_archive/`. Copilot worktrees were moved to `~/repos/copilot-worktrees/` to retain their four unpushed commits.

The Artifactory credential is now outside the workspace in a mode-600 config file loaded by `.envrc`; it should not return to the parent workspace. The remaining uncommitted repo-local work includes OCCTO probes in `smp-japan`, IEX probes in `apac-tsdb-scraper`, and `smp-tool/docs/spikes/`; it was intentionally not reorganized.

## History

- 2026-10-19: workspace cleaned and normalised for agent use; five `CLAUDE.md` import commits were pushed to their current branches.

## Sources

- `sources/claude-conversations/2026-10-11-claude-smp-b6f4d55c.txt`
- `sources/claude-conversations/2026-10-19-claude-smp-f61c600d.txt`

Last Updated: 2026-10-20
