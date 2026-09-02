# Granola Capture: Backlog Grooming

Date: 2026-09-02 15:30 GMT+8
Source: Granola
Meeting ID: `312e4c52-9cde-4690-88cf-3e4686fe907c`

## Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Notes

# Backlog Priorities

- Bilateral contract scrapping: next priority ticket
  - Name parsing can be deferred; store raw data now, map later
- India grid data ticket: proxy issue noted but not yet actionable
- Two Bitstack tickets: sized and clear, ready to pick up
- User account / permission scope ticket: goal is to document how to add a new DAG developer to the platform
- Deployment pipeline (Docker image push via GitLab runner): blocker likely resolved since dependencies can now be installed on test; flag removed
- Grafana backup: still very low priority

# Grafana Usage Monitoring

- Scope narrowed to Grafana only (Airflow excluded as less relevant)
- Goal: see which dashboards are accessed, by whom, and how often
  - Exclude internal team from counts
  - Optional stretch: zoom/graph interaction tracking (feasibility unknown)
- Not exclusive to SMP: Synapse and Delphi also use the shared Grafana/Airflow stack
  - Raises question of whether SMP should bear the cost alone; to be raised with Bastian
- Loki likely the right tool: has a usage/stack log by default, integrates natively with Grafana
  - Prometheus + Loki also a Grafana-native option
  - Amplitude not needed
- Okta logs: could provide basic connection metadata; worth a quick check
- Action: spike on Loki usage logs; check Okta log availability

# Observability Stack (Epic 1254) and Jupyter Integration (Epic 1210)

- Epic 1254: resource monitoring (CPU/memory) per SMP deployment, visualized in Grafana
  - Signups team already implemented Loki on their cluster; Michael to coordinate with Jeka on a demo when back from holiday
  - Agreed: set a baseline first before implementing anything; SMP and Synapse use the same stack differently
  - Near-term goal: simple alerting at ~95% resource usage, manual response before any autoscaling
- Epic 1210: Jupyter-based DAG authoring experience
  - Vision: browser-based notebook connected to a dev environment clone, with all dependencies installed
    - Author DAG cells, define parameters, press a button to convert to a DAG and open a PR to dev
    - Support for business tests defined inline, mapped to a test folder
  - Technically very ambitious: requires web-deployed notebook, sandboxed Airflow instance, and a Git client built behind the scenes
  - Signups doing something similar for notebook training; need to sync with them and Nilo on reusability
  - Context: Iberia team frustrated by slow IT handoffs and lack of hands-on access to business logic; current process still too cumbersome per Matteo's feedback
  - Next step: revisit scope with Fred and Milo, identify must-haves vs. drops, then break into smaller tasks

# Next Steps

- **Spike on Loki usage logs for Grafana monitoring**

  Check if default Loki stack logs provide dashboard access data; also verify whether Okta logs expose connection metadata.
- **Raise SMP cost attribution question with Bastian**

  Grafana/Airflow monitoring benefits Synapse and Delphi too; clarify who should own the work.
- **Attend scrapping task clarification call with Matthew and Adrian** (Brian)

  Francois will forward the invite; use it to refine tickets and capture any new requests.
- **Sync with Nilo and Fred on Epic 1210 scope**

  Identify go/no-go features for the Jupyter DAG authoring experience before splitting into tasks.
- **Coordinate Loki demo with Jeka via Michael**

  Michael to set this up when back from holiday; Signups already deployed Loki on their cluster.

Last Updated: 2026-09-02
