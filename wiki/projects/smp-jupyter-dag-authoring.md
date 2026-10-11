# SMP Jupyter DAG Authoring

## Current State

As of 2026-10-08.

- **Timeline:** planned for next period, roughly late October to late November or early December. The goal is for India stakeholders (Mateo, Adrien, Lou) to create DAGs with minimal developer help.
- **Preferred architecture (2026-10-08):**
  - A persistent DevX namespace with paired Jupyter and Airflow instances.
  - A shared volume, so DAG changes show up in about 30–45 seconds.
  - Strict pod CPU and memory limits.
  - Git/PR review stays the merge gate. No per-session spin-up or teardown unless evidence demands it.
- **Main risk:** capacity. The shared non-prod EKS cluster was about 90% utilized (10 nodes, 78.2 cores).
- **Before the period starts:** Brian needs a JupyterLab demo, likely from Eric, with [[michael]]. Bong and Fred need an explicit tradeoff between this and regular delivery. An S&P/Synapse integration estimate with Eric Martin feeds the steering committee.

## Background

- **The real need** (reframed 2026-09-02): contributors want a fast, trustworthy feedback loop before deployment, with platform dependencies, network reachability, Airflow variables and connections, and safe dev service access. Notebooks are one way to deliver that.
- **Notebooks versus DAGs:** notebooks are for debugging CDH, API, and transform logic. Airflow still needs Python DAG files. The intended path is to iterate in Jupyter, copy the validated logic into the DAG file, commit, and open a PR.
- **Rejected:**
  - Writing directly from Jupyter into the live DAG path, because a duplicate DAG ID could trigger real external calls.
  - Copying Synapse's save-to-DB audit trail, per-save commits, or per-developer Airflow, unless later evidence needs them.
- **Alternative:** a VS Code remote session into a cluster container, if notebook visuals aren't needed.
- **Scope:** `SCR-1210` stays an epic, to be split into hosting/security, authoring/export, Git/CI, and test-support stories. Python versions must line up: repos use 3.13, the Airflow image uses 3.12.

## History

- 2026-08-24: `SCR-1210` rated conditionally feasible but too broad for one story.
- 2026-10-07: simplified to JupyterHub in SMP dev only, without the Synapse machinery.
- 2026-10-08: DevX namespace with paired Jupyter and Airflow preferred.

## Open Questions

- UNCERTAIN: Whether `DevX` is the chosen name.
- UNCERTAIN: Whether Eric is confirmed as demo owner.
- UNCERTAIN: Why `SCR-992` was rejected and what `SCR-1011` concluded.

## Sources

Main sources are below. The full trail from before the 2026-10-11 split is on [[smp-platform]].

- `sources/codex-conversations/2026-08-24-codex-conversations.txt`
- `sources/codex-conversations/2026-09-02-codex-conversations.txt`
- `sources/meetings/2026-09-02-backlog-grooming.md`
- `sources/meetings/2026-10-05-granola-trading-data-platform-presentation-and-jupyterlab-roadmap-with-bong.md`
- `sources/meetings/2026-10-07-granola-integration-of-jupyterlab-to-airflow.md`
- `sources/meetings/2026-10-08-1431-granola-another-attempt-at-jupyter-discussion.md`

Last Updated: 2026-10-11
