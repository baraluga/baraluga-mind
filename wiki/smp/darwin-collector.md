# Darwin Collector

## Current State

As of 2026-10-17.

- The network blocker appears to have cleared enough to resume rollout work. Earlier, the collector was deployed to India dev on 2026-10-01 with [[michael]]'s help but Okta auth and the Darwin base API returned proxy 403s; by October 13 Brian treated Darwin as unblocked and moved to deployment/config questions.
- The collector catalogue is now the single source of truth in `smp-india`: it supplies collector entity/tag selection, publisher destinations, and freshness expectations. It has 18 expected streams in dev/QA and 21 in prod; Tithwa is prod-only. The duplicate `smp-tool` site configuration and publisher `mappings.json` were removed.
- Collector deployments now require an explicit image tag. The new catalogue is bundled into the image, so enabling a site is an `smp-india` change and deployment of that image; the old-image/new-manifest pairing is refused before it can replace a running pod. CI currently publishes an image artifact rather than directly to ECR, so the manual image-transfer/deploy path remains until the CI ECR setting and AWS OIDC trust are resolved.
- For `SCR-1273`, Mateo clarified ModuleTemperature is not needed. The rollout removed ModuleTemperature from collection instead of collecting and dropping it later.
- TSDB probing found 12 Gujarat IDs in UAT and all 16 in prod. The four Tithwa series existed in prod but initially 404ed in UAT; Mateo said he would create them in UAT too. Generation destinations are MW, so Darwin kW values still need the existing 0.001 conversion.
- The collector is running in India dev and has gathered a publish backlog, but the first real UAT TSDB write was rejected with HTTP 403 on the `tsdb-uat-live-darwin` topic. The UAT service account can read catalogue/data but lacks Darwin-source write permission; the publisher should remain paused until that grant is made. The backlog remains on EFS because deletion follows verified writes.
- Khaba is confirmed as Darwin entity `SOF_INNS7`. Its Darwin series are intended to run in parallel with, not replace, the CSV/SFTP feed, which remains the backup. The capture verified the three source tags were fresh; four associated TSDB IDs existed in both UAT and prod, but end-to-end publishing is blocked by the UAT permission failure.
- **Tickets:**
  - `SCR-1261`: Tuticorin wind speed, wind direction, and generation.
  - `SCR-1273`: four more assets. All 15 requested measurements parse from saved responses.
  - `SCR-1268`: collector health and freshness monitoring, starting with Prometheus discovery.
- Freshness monitoring (`SCR-1268`) now compares EFS collector state with the catalogue's expected streams, so a site that has never produced data is stale rather than invisible. Khaba's three dev streams will remain correctly stale until the new collector image is deployed and begins polling them.
- The publisher no longer performs Athena read-before-write or read-back on live runs: TSDB storage-confirmation sockets cannot connect from EKS. It writes each series and moves fully written raw files to `published/` for seven days; a bulk validator design is pending before that retention can become verified cleanup. The manual aggregation Airflow test and its CI coverage were repaired after the catalogue migration.

## Background

- **Why a collector:** Airflow is a poor fit for guaranteed per-minute polling, and Darwin may expose only the latest readings. So a standalone Python service runs as a Kubernetes pod, writes observations to a durable JSON handoff on EFS, and a five-minute Airflow DAG publishes them to TSDB.
- **Why TSDB stays in Airflow:** publication stays in Airflow to avoid maintaining TSDB credentials in two places. A five-minute delay is accepted.
- **Sampling:** adaptive polling keeps the first valid sample per source minute with its exact source timestamp. A one-minute poll missed a source minute; a 15-second trial captured every minute. The Airflow publisher averages whatever minutes exist in each 15-minute window and does not fill gaps (`smp-india` `357c8fb`).
- **Auth:** production uses a Darwin application account with OAuth client credentials, not a personal login. Machine-to-machine credentials were obtained on 2026-09-30.
- **Code:** collector, handoff, publisher, conflict quarantine, and restart-safe publication live in `smp-india`, with a mock Darwin API for dev POCs in `smp-tool`. All TSDB evidence so far is fake-TSDB or local.

## History

- 2026-09-18: Darwin access blocked on provisioning; continuous-collector fallback designed.
- 2026-09-21: first collector milestone pushed to `smp-india` `dev`.
- 2026-09-30: M2M credentials obtained.
- 2026-10-01: deployed to India dev; blocked by proxy 403s.
- 2026-10-13: Gujarat mappings and ModuleTemperature removal completed and pushed to `dev`; rollout still needed registry/image or config apply work and first UAT writes.
- 2026-10-15: first UAT Darwin publication attempt reached TSDB but failed with a 403 write-permission error; no data was lost.
- 2026-10-16: catalogue ownership moved into `smp-india`; live publisher reads were removed after EKS could not use TSDB storage-confirmation sockets.

## Open Questions

- UNCERTAIN: Whether Darwin can replay previous-minute values, which would allow a simpler scheduled DAG.
- UNCERTAIN: How the collector avoids two active pollers during Kubernetes redeploys.
- UNCERTAIN: Whether 15-second polling is within Darwin's supported request rate.
- UNCERTAIN: Whether Khavda's sparse irradiance (6–7 values per 15 minutes) is expected Darwin behaviour. Asset spellings are settled in [[aliases]].
- UNCERTAIN: Whether Gregory is still relevant now that Brian treated Darwin as unblocked.
- UNCERTAIN: Whether the four Tithwa UAT series were created after Mateo's October 13 reply.
- UNCERTAIN: Whether TSDB will grant the UAT Darwin-source write permission, and whether the prod service account needs the same grant.
- UNCERTAIN: Whether the first production write probe was run; it would make an irreversible but genuine point.
- UNCERTAIN: Whether the newly tagged collector image has been deployed in dev and Khaba has appeared in the collector state.
- UNCERTAIN: Whether CI can be authorized to push Darwin images directly to ECR through GitHub OIDC.
- UNCERTAIN: Whether the planned bulk validator will prove published files in TSDB before their seven-day retention ends.

## Sources

Main sources are below. The full trail from before the 2026-10-11 split is on [[smp-platform]].

- `sources/meetings/2026-09-18-1230-granola-darwin-api.md`
- `sources/meetings/2026-09-21-1700-granola-smp-technical-consultation-on-darwin.md`
- `sources/meetings/2026-09-30-1415-granola-smp-standup.md`
- `sources/meetings/2026-10-01-1415-granola-smp-standup.md`
- `sources/meetings/2026-10-05-granola-smp-standup.md`
- `sources/meetings/2026-10-07-granola-morning-standup.md`
- `sources/codex-conversations/2026-09-18-codex-conversations.txt`
- `sources/codex-conversations/2026-09-21-codex-conversations.txt`
- `sources/codex-conversations/2026-09-28-codex-conversations.txt`
- `sources/codex-conversations/2026-10-01-codex-conversations.txt`
- `sources/claude-conversations/2026-10-02-claude-smp-68dedda3.txt`
- `sources/claude-conversations/2026-10-13-claude-smp-68dedda3.txt`
- `sources/claude-conversations/2026-10-13-claude-smp-8ce08f10.txt`
- `sources/meetings/2026-10-14-1415-granola-daily-standup.md`
- `sources/meetings/2026-10-14-1441-granola-mateo-call.md`
- `sources/claude-conversations/2026-10-14-claude-smp-68dedda3.txt`
- `sources/claude-conversations/2026-10-15-claude-smp-36b94912.txt`
- `sources/claude-conversations/2026-10-15-claude-smp-68dedda3.txt`
- `sources/claude-conversations/2026-10-16-claude-smp-36b94912.txt`
- `sources/claude-conversations/2026-10-16-claude-smp-68dedda3.txt`
- `sources/claude-conversations/2026-10-16-claude-smp-c410edb9.txt`

Last Updated: 2026-10-18
