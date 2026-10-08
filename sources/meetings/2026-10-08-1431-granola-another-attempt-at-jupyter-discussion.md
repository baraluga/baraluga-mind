# Granola Capture: Another Attempt at Jupyter Discussion

Source Type: meeting
Meeting Date: 2026-10-08 14:31 Asia/Manila
Granola URL: https://notes.granola.ai/d/af95dd3a-a595-4cc1-bf92-9d189c7ac8e8
Granola Meeting ID: af95dd3a-a595-4cc1-bf92-9d189c7ac8e8
Captured By: Brian Alexander Peralta

## Participants

- Brian Alexander Peralta

## Granola Summary

### Background and Problem Statement

- SMP users currently develop DAGs locally, then submit a pull request.
  - It is hard to replicate the Airflow Python environment locally.
  - Users cannot test DAGs end-to-end with decorators before submitting.
- Goal: provide a sandbox where users can iterate on DAGs in the correct environment before pushing a PR.
  - Sandbox needs the same Python environment as Airflow.
  - Sandbox needs access to team secrets and CDH / third-party APIs.
  - PR gate remains to catch hardcoded credentials and bad practices.

### Proposed Architecture

- A DevX branch is created per development session, forked from dev.
- Each session gets a paired Jupyter + Airflow instance in a new namespace, isolated from official environments.
- A shared volume is mounted to both Jupyter and Airflow for real-time DAG reflection without committing.
- When finished, the user commits changed files, opens a PR, and the DevX branch is deleted.
- Two safety gates were discussed:
  - Save hook in Jupyter for validation, dry run, and sensitive-data filtering.
  - PR merge with full pipeline checks before merging to dev.
- Spin-up/teardown versus persistent namespace tradeoff:
  - Teardown keeps current with latest dev branch but adds lag.
  - Persistent namespace with a sync-to-latest-dev mechanism is viable.
  - Consensus: persistent namespace preferred; spin-up/teardown is unnecessary given the small user base.

### Jupyter Demo and Value Proposition

- JupyterHub provisions per-user single-user pods; multiple users share the same namespace.
- DAG files and notebook files are distinct formats.
  - DAGs must be Python files following Airflow conventions.
  - Notebooks cannot run directly in Airflow.
  - Notebooks are useful for iterating on logic such as CDH calls and data transforms before copying into a DAG file.
- Proposed SMP user workflow:
  - Open Jupyter and debug logic interactively in a notebook.
  - Copy function calls and decorators into the DAG Python file.
  - Save the file, which reflects in the shared-volume Airflow instance within about 30-45 seconds.
  - Confirm the DAG runs correctly, then commit and open a PR.
- Key SMP value: removes local environment setup friction around Artifactory dependencies, credentials, and environment parity.
- Multi-user file conflict risk was acknowledged and considered acceptable given small team size and coordination norms.

### Resource Constraints and Next Steps

- SMP runs on a shared EKS cluster currently at about 90% utilization across 10 nodes / 78.2 cores.
- Adding Airflow deployments per DevX namespace is expensive and needs coordination with cluster admin Milo.
- Mitigation: set strict CPU/memory resource limits on DevX pods via Helm charts.
- Active SMP DAG developers are estimated at 1-2, likely the India team; low namespace count expected.
- Francois to sync with Bon and Fred on budget limits and acceptable resource spend.

### Next Steps

- Confirm cluster resource budget with Bon and Fred. Owner: Francois.
- Coordinate with Milo on shared cluster capacity.
- Align with Nilo on final architecture decisions.

Last Updated: 2026-10-09
