# SMP Jupyter DAG Authoring

## Current State

As of 2026-10-23.

- **Delivery shape:** `SCR-1210` is now the epic for an India-first browser development environment. `SCR-1297` is the outcome ticket, *SMP-ready browser dev environment (India pilot)*; it preserves [[francois-delcourt]]'s original scope. Its acceptance target is a no-local-setup environment where a key user can develop a DAG, push it, and have another user see it in India dev Airflow.
- **Current planning:** `SCR-1298` is the spike that must settle per-region versus per-branch isolation with [[francois-delcourt]] and [[nilo-menezes]], JupyterHub versus Codespaces, and the `dev` versus `sandbox` branch. `SCR-1299` (JupyterHub on India dev with Okta) and `SCR-1300` (Codespaces for `smp-india`) are mutually exclusive implementation paths; delete the losing path after the spike. Per-branch is a materially different on-demand platform (branch, namespace, Airflow/database, JupyterLab, storage, cost cap, and teardown), not simply a scaled per-region deployment.
- **Direction, not yet a final architecture:** Brian prefers one sandbox per region over an Airflow/Jupyter instance per user branch, because the estimate is only one to two active authors and per-user instances add lifecycle and capacity cost. The spike remains the decision gate; it must account for the isolation and clean-PR benefits of per-branch work.
- **Operational constraints:** JupyterHub needs EKS capacity, an Okta callback/ingress configuration, and an SMP-ready image. A 2026-10-23 local OrbStack spike installed the stock `jupyterhub/jupyterhub` 4.3.4 chart and opened JupyterLab for a test user; it was then fully removed and OrbStack Kubernetes was disabled. This proves only the baseline chart, not Okta, Git, SMP-image, ingress, or India deployment readiness. Codespaces remains practically doubtful: searches found no Walnut onboarding/support process, it runs only on GitHub-hosted infrastructure, and its private-network/Artifactory fit is unresolved. Brian asked Pierre about license availability; no response is captured.
- **Airflow behaviour:** a comment was posted to `SCR-1297` that new DAGs default paused and existing active/inactive state lives in each Airflow database, so merging to `dev` does not switch already-running DAGs. This is implementation guidance, not a production verification.
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
- UNCERTAIN: Whether Codespaces is available to the organisation, how it is billed, and whether GitHub Enterprise private networking can satisfy SMP's Artifactory and service-access needs.
- UNCERTAIN: Whether EKS has capacity for JupyterHub, who owns the Okta callback configuration, and who will deploy `SCR-1299` if Brian does not use DashC/AWS infrastructure access.

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
- `sources/claude-conversations/2026-10-23-claude-smp-d2cd8178.txt`
- `sources/codex-conversations/2026-10-23-codex-conversations.txt`

Last Updated: 2026-10-24
