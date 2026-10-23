# SMP Jupyter DAG Authoring

## Current State

As of 2026-10-22.

- **Delivery shape:** `SCR-1210` is now the epic for an India-first browser development environment. `SCR-1297` is the outcome ticket, *SMP-ready browser dev environment (India pilot)*; it preserves [[francois-delcourt]]'s original scope. Its acceptance target is a no-local-setup environment where a key user can develop a DAG, push it, and have another user see it in India dev Airflow.
- **Current planning:** `SCR-1298` is the spike that must settle per-region versus per-branch isolation with [[francois-delcourt]] and [[nilo-menezes]], JupyterHub versus Codespaces, and the `dev` versus `sandbox` branch. `SCR-1299` (JupyterHub on India dev with Okta) and `SCR-1300` (Codespaces for `smp-india`) are mutually exclusive implementation paths; delete the losing path after the spike.
- **Direction, not yet a final architecture:** Brian prefers one sandbox per region over an Airflow/Jupyter instance per user branch, because the estimate is only one to two active authors and per-user instances add lifecycle and capacity cost. The spike remains the decision gate; it must account for the isolation and clean-PR benefits of per-branch work.
- **Operational constraints:** JupyterHub needs EKS capacity, an Okta callback/ingress configuration, and an SMP-ready image. Codespaces needs organisation availability/billing and a way to use private Artifactory dependencies without public-network access. The shared non-prod EKS cluster was reported at about 90% utilized on 2026-10-08 (10 nodes, 78.2 cores), but that is not a current capacity measurement.
- **Workflow preference:** retain Git/PR review as the merge gate and avoid Synapse-style automatic commits on every Jupyter save/autosave. The desired user flow is intentional commit/push from the browser environment; notebooks remain optional to the core setup-friction problem.

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
- 2026-10-21: Synapse Jupyter integration made the primary committed deliverable, with a dev-environment-first rollout.
- 2026-10-22: `SCR-1210` received an outcome ticket, a decision spike, and mutually exclusive JupyterHub/Codespaces implementation tickets.

## Open Questions

- UNCERTAIN: Which environment model wins: per-region or per-branch.
- UNCERTAIN: Whether Codespaces is available to the organisation, how it is billed, and how it can safely consume private Artifactory dependencies.
- UNCERTAIN: Whether EKS has capacity for JupyterHub and who owns the Okta callback configuration.

## Sources

Main sources are below. The full trail from before the 2026-10-11 split is on [[smp-platform]].

- `sources/codex-conversations/2026-08-24-codex-conversations.txt`
- `sources/codex-conversations/2026-09-02-codex-conversations.txt`
- `sources/meetings/2026-09-02-backlog-grooming.md`
- `sources/meetings/2026-10-05-granola-trading-data-platform-presentation-and-jupyterlab-roadmap-with-bong.md`
- `sources/meetings/2026-10-07-granola-integration-of-jupyterlab-to-airflow.md`
- `sources/meetings/2026-10-08-1431-granola-another-attempt-at-jupyter-discussion.md`
- `sources/meetings/2026-10-21-1415-granola-smp-retro.md`
- `sources/meetings/2026-10-21-1630-granola-smp-review.md`
- `sources/claude-conversations/2026-10-22-claude-smp-d2cd8178.txt`

Last Updated: 2026-10-23
