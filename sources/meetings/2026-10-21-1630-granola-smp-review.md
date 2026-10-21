# Granola Capture: SMP Review

Source Type: meeting
Source: Granola
Meeting Date: 2026-10-21 16:30 GMT+8
Meeting URL: https://notes.granola.ai/d/631cff47-98a9-41c5-8edc-234be6b94842
Granola ID: 631cff47-98a9-41c5-8edc-234be6b94842

## Known Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Development Workflow and Data Platform

- The Gitata catalogue is available as a documentation reference. Jupyter integration with the Synapse team is planned to enable more self-service development and reduce ticket-driven back-and-forth.
- The Kafka reference file was updated and the dependency between forecast and realised-data processes was resolved, leaving the two processes independent and more resilient to upstream issues.
- The bilateral-contract table and Bitstack report were promoted from QA to production and are now available to end users.
- Darwin ingestion was under final validation: the service polls Darwin every 15 seconds, stores the data, and pushes it to production TSDB. Supporting DAGs check freshness and handle the TSDB push.
- A CDH push for Grafana visualisation was planned for the next sprint.

### Budget, Operating Model, and Cadence

- Budget consumption was reported at 84% for the current period, with most costs still supported by the India team. The reporting cadence will remain in place to keep costs visible and controlled.
- Japan is switching to Kanban support mode with no active development; new requests enter the backlog for stakeholder prioritisation against available team capacity.
- Bi-weekly meetings will continue to track delivery progress and budget consumption.

### Near-Term Priorities

- The common priority is to continue current work and begin Jupyter integration with Synapse. A first iteration is expected in the coming weeks, followed by rollout and end-user training.
- An India geography task with Matteo was identified as a practical Jupyter-integration example.
- India priorities are to complete Darwin validation, push collected Darwin data to CDH for dashboarding, and create a dedicated Teams channel for DAG-failure notifications.

## Next Steps Captured In Granola

- Continue Darwin ingestion validation and prepare the CDH push for dashboarding.
- Begin Jupyter integration with the Synapse team, using the India geography task with Matteo as a possible first example.
- Create a dedicated Teams channel for DAG failure notifications.

Last Updated: 2026-10-22
