# Darwin Collector

## Current State

As of 2026-10-21.

- The network blocker appears to have cleared enough to resume rollout work. Earlier, the collector was deployed to India dev on 2026-10-01 with [[michael]]'s help but Okta auth and the Darwin base API returned proxy 403s; by October 13 Brian treated Darwin as unblocked and moved to deployment/config questions.
- The collector catalogue is now the single source of truth in `smp-india`: it supplies collector entity/tag selection, publisher destinations, and freshness expectations. It has 18 expected streams in dev/QA and 21 in prod; Tithwa is prod-only. The duplicate `smp-tool` site configuration and publisher `mappings.json` were removed.
- Collector deployments now require an explicit image tag. The new catalogue is bundled into the image, so enabling a site is an `smp-india` change and deployment of that image; the old-image/new-manifest pairing is refused before it can replace a running pod. CI currently publishes an image artifact rather than directly to ECR, so the manual image-transfer/deploy path remains until the CI ECR setting and AWS OIDC trust are resolved.
- On 2026-10-21, a documentation-only change under the collector `src/` directory was committed to `dev` as `b89c82d` to force a fresh content-derived image tag (`darwin-collector-b89c82dddddb`). The captured CI run was only queued; image build and ECR publication are not yet evidenced. The run still depends on an environment-level `DARWIN_COLLECTOR_ECR_PUSH=true` setting because it is absent from repository-level variables.
- For `SCR-1273`, Mateo clarified ModuleTemperature is not needed. The rollout removed ModuleTemperature from collection instead of collecting and dropping it later.
- TSDB probing found 12 Gujarat IDs in UAT and all 16 in prod. The four Tithwa series existed in prod but initially 404ed in UAT; Mateo said he would create them in UAT too. Generation destinations are MW, so Darwin kW values still need the existing 0.001 conversion.
- India dev is now proven end to end: a read-back returned `OK` for all 24 mapped series over three hours, including Khaba after its redeploy. Its 39–45 files per five-minute run indicate a drained, steady-state backlog. Darwin-source gaps are deliberately not filled.
- Khaba is confirmed as Darwin entity `SOF_INNS7`; its Darwin series remain parallel backup to the CSV/SFTP feed. Khavda horizontal irradiance appeared frozen at 131.99 W/m² across several snapshots, so it is published as received but should not be used until Darwin corrects it.
- Darwin is live in QA and prod as of 2026-10-20. QA published before the go-live hand-off retired dev; Brian separately confirmed the dev publisher was paused and its freshness DAG then failed because the collector was intentionally off. The QA and prod freshness checks show all configured sites except the known upstream outages receiving current source data, which proves production egress to Darwin; a completed TSDB read-back was reported but its output was not captured here.
- The operating pattern is documented in `smp-india/docs/realtime-collector-pattern.md`; it describes the collector-to-EFS-to-Airflow publisher flow, write-only TSDB publishing, freshness triage, and deployment. Related Jira tickets `SCR-1261`, `SCR-1268`, `SCR-1273`, `SCR-1283`, and `SCR-1294` received links to that documentation.
- As of 2026-10-20, Raganesda (`SOF_INRAG`) and production-only Tithwa (`WIF_INGUV`) are stale because their source data stopped upstream, not because of the pipeline. A direct 24-hour Darwin-history probe found all sampled Raganesda devices stopped together at 19 Oct 14:20 UTC; Tithwa series dropped between 02:40 and 04:40 UTC on 20 Oct. This suggests site communications/SCADA failures, but historical recurrence cannot be checked from Darwin's 24-hour history window. The freshness DAG correctly remains failed while either site is stale.
- **Tickets:**
  - `SCR-1261`: Tuticorin wind speed, wind direction, and generation.
  - `SCR-1273`: four more assets. All 15 requested measurements parse from saved responses.
  - `SCR-1268`: collector health and freshness monitoring, starting with Prometheus discovery.
- Freshness monitoring (`SCR-1268`) now compares EFS collector state with the catalogue's expected streams, so a site that has never produced data is stale rather than invisible. Khaba's three dev streams will remain correctly stale until the new collector image is deployed and begins polling them.
- The publisher no longer performs Athena read-before-write or read-back on live runs: TSDB storage-confirmation sockets cannot connect from EKS. It writes each series and moves fully written raw files to `published/` for seven days; a bulk validator design is pending before that retention can become verified cleanup. The manual aggregation Airflow test and its CI coverage were repaired after the catalogue migration.
- A 2026-10-21 probe reconfirmed that the machine account can only access `/production/data/lastday`: 24 hours at 10-minute or hourly resolution. Network failure then prevented more probing. Mateo must supply the exact historical endpoint and access path before a longer or exact one-minute backfill can be designed.

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
- 2026-10-19: dev read-back proved all mapped series through collector, EFS, publisher, and UAT TSDB; QA/prod go-live script was pushed to `smp-tool` dev.
- 2026-10-20: QA and prod went live; the dev collector was retired after QA's first publication.

## Open Questions

- UNCERTAIN: Whether Darwin can replay previous-minute values, which would allow a simpler scheduled DAG.
- UNCERTAIN: How the collector avoids two active pollers during Kubernetes redeploys.
- UNCERTAIN: Whether 15-second polling is within Darwin's supported request rate.
- UNCERTAIN: Whether Khavda's sparse irradiance (6–7 values per 15 minutes) is expected Darwin behaviour. Asset spellings are settled in [[aliases]].
- UNCERTAIN: Whether Gregory is still relevant now that Brian treated Darwin as unblocked.
- UNCERTAIN: Whether the four Tithwa UAT series were created after Mateo's October 13 reply.
- UNCERTAIN: The captured evidence proves production egress to Darwin but does not retain the result of the reported QA/prod TSDB read-backs.
- UNCERTAIN: Whether CI can be authorized to push Darwin images directly to ECR through GitHub OIDC.
- UNCERTAIN: Whether the planned bulk validator will prove published files in TSDB before their seven-day retention ends.
- UNCERTAIN: Whether Mateo's historical API is a distinct Darwin endpoint, UI access, or a permission unavailable to the machine account; `/lastday` cannot provide exact one-minute backfill.

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
- `sources/claude-conversations/2026-10-19-claude-smp-36b94912.txt`
- `sources/claude-conversations/2026-10-19-claude-smp-68dedda3.txt`
- `sources/claude-conversations/2026-10-20-claude-smp-1aff4345.txt`
- `sources/claude-conversations/2026-10-20-claude-smp-68dedda3.txt`
- `sources/claude-conversations/2026-10-21-claude-smp-45346bf9.txt`
- `sources/claude-conversations/2026-10-21-claude-smp-68dedda3.txt`

Last Updated: 2026-10-22
