# Granola Capture: Integration of Jupyterlab to Airflow

Source Type: meeting
Meeting Date: 2026-10-07 14:31 Asia/Manila
Granola URL: https://notes.granola.ai/d/30e8adc0-8d25-4984-8cca-7dd4369daf4e
Granola Meeting ID: 30e8adc0-8d25-4984-8cca-7dd4369daf4e
Captured By: Brian Alexander Peralta

## Participants

- Brian Alexander Peralta

## Granola Summary

### JupyterLab Integration Approach for SMP

- Goal: give SMP developers a proper dev environment to write, test, and commit DAG code without going through the infra team's sprint cycle.
- Current blocker: no way for SMP developers to test DAG behavior in an Airflow-like environment before submitting PRs.
- Synapse model reviewed but explicitly not recommended for SMP.
  - Too complex: multiple pipelines, repositories, and libraries; took days to understand.
  - Compliance machinery, including save-to-DB audit trail, was built for trading; SMP does not need it.
  - Every Jupyter save triggers a commit, which is slow and convoluted.

### Proposed Architecture

- Deploy JupyterHub in SMP dev environment, not production at least initially.
  - Grant access only to developers, not all users.
  - Take a snapshot of the DAG Git repository on login.
  - Give each user a local volume so work persists if the kernel dies; clean periodically.
- Execution environment should mirror Airflow.
  - Same image, same network access, same credentials for CDH, TSDB, and proxy.
  - CDH credentials are the SMP team's own; no concern sharing them.
- Commit flow via Git, not direct DAG manipulation.
  - Developers work in Jupyter, then commit to a secondary branch.
  - Secondary branch is PR'd into the branch Airflow reads.
  - Airflow never picks up changes until PR is approved.
- Avoid direct DAG code edits inside Jupyter that write back to the live DAG path.
  - Risk: same DAG ID would trigger execution on real external services immediately.

### Security Concerns and Simplification Guidance

- Key risk: once developers can commit code, they effectively become infra developers.
  - Past issues: hardcoded credentials, passwords in environment files, secrets in spreadsheets.
  - Vibe-coding trend means developers may not be aware of what they are committing.
  - PR review process is the main safeguard; keep it mandatory.
- VS Code remote session into a cluster container was floated as a lighter alternative to Jupyter.
  - Skips JupyterHub entirely; useful if developers do not need visual output such as charts.
  - Jupyter is preferred if visual inspection of outputs is needed.
- Per-developer Airflow environments, as in the Synapse model, are possible but expensive; not recommended unless needed.
- Strong advice: keep it simple; do not replicate Synapse's full machinery.

### Next Steps

- Enable Jupyter access in SMP dev for François to test.
  - Owner: Eric.
  - François will validate what works, what does not, and invite an SMP-side developer to iterate.
- Send Eric an email requesting SMP dev Jupyter notebook access.
  - Owner: François.
  - First step before looping in Ardu to define requirements and move forward.

Last Updated: 2026-10-08
