# AM Standup

Source type: Granola meeting notes

Meeting ID: `7973f3af-742b-4128-8655-0f83dce5c84a`

Meeting date/time: 2026-07-08 09:45 GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This is not a verbatim transcript. It preserves the available Granola meeting notes/summaries.

## Discussion Notes / Summary

### Announcements

- Feedback deadline: July 8th, share with anyone interacted with in the past 6 months.
- AWS migration update: 0.5 allocation to Michael; Brian as reviewer/consultant until sustainable.
- Allocations need to be adjusted and shared accordingly.

### SMP Validation (CSCR-119)

- Separate Docker image needed for both regions due to Airflow version conflict.
- Japan Airflow version has library dependencies pinned to specific versions.
- India Airflow version uses latest packaging, causing conflict.
- Proxy/Peloton incident tickets raised in ILO.

### Brian's Updates

- Policy 1181: no receiving email required as recipient; select few in scope for QA, adds 1100.
- Credentials for Walnut Artifactory needed for anyone contributing to Japan/India.
- Connected via Scaler; pull request pending.
- QRMDMS contribution workflow: organization -> teams -> sub-teams.
- Migration target: fewer MDMS, with connector backfill planned for near future.
- Historical snapshot challenge: dates from 2019, about 2 snapshots/day, compounding volume.
- Memory pressure increasing despite stable major version.
- Merge not yet in production; historical snapshot technically working but growing daily.

### Infrastructure and S3-to-Airflow Pipeline

- Kubernetes migration: duplicating VM setup to K8s environment is in progress.
- Missing steps: documentation and codified execution setup.
- S3-to-Airflow duck generation: current poll every 60 seconds flagged as expensive.
- Proposed alternative: event-driven trigger directly to EFS, then to Airflow radio folder.
- Proposal open for feedback.

## Next Steps / Action Items From Granola

- Submit feedback by July 8th (Brian Alexander Peralta). Share with anyone interacted with over the past 6 months.
- Adjust and share AWS migration allocation. Brian's role is reviewer/consultant; allocations need to be redistributed accordingly.
- Finalize CSCR-119 Docker image separation. Resolve Airflow version and packaging conflict between Japan and India regions.
- Document and codify Kubernetes environment setup. Missing steps are a potential blocker for the VM-to-K8s migration.
- Evaluate event-driven S3-to-Airflow trigger proposal. Replace 60-second polling with direct EFS event trigger; open for team feedback.

Last Updated: 2026-07-09
