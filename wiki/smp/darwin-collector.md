# Darwin Collector

## Current State

As of 2026-10-15.

- The network blocker appears to have cleared enough to resume rollout work. Earlier, the collector was deployed to India dev on 2026-10-01 with [[michael]]'s help but Okta auth and the Darwin base API returned proxy 403s; by October 13 Brian treated Darwin as unblocked and moved to deployment/config questions.
- There is no automatic collector deployment. Code changes need a new amd64 image; config-only changes need rendering the complete enabled-site config, server-side dry-run, apply, and rollout status. Omitting a site from render silently stops collecting it.
- For `SCR-1273`, Mateo clarified ModuleTemperature is not needed. The rollout removed ModuleTemperature from collection instead of collecting and dropping it later.
- TSDB probing found 12 Gujarat IDs in UAT and all 16 in prod. The four Tithwa series existed in prod but initially 404ed in UAT; Mateo said he would create them in UAT too. Generation destinations are MW, so Darwin kW values still need the existing 0.001 conversion.
- Local live-Darwin validation after the mapping changes collected all six entities and 18 streams, with no ModuleTemperature and no quarantine, then published live batches through the real publisher into a fake TSDB. Real TSDB writes and cluster rollout remained unproven in the source.
- **Tickets:**
  - `SCR-1261`: Tuticorin wind speed, wind direction, and generation.
  - `SCR-1273`: four more assets. All 15 requested measurements parse from saved responses.
  - `SCR-1268`: collector health and freshness monitoring, starting with Prometheus discovery.
- As of 2026-10-14, the cluster can reach the Darwin API and CI/CD exists, but building and pushing the collector image is blocked on an unassigned SMP India AWS ECR/data-source-role ticket. [[michael]] is helping with deployment.
- Mateo asked to add four Khaba series using Darwin request type `ENS7`; the entity code and whether this is a parallel or replacement source for the existing Khaba CSV feed need confirmation. See [[smp-india]].

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

## Open Questions

- UNCERTAIN: Whether Darwin can replay previous-minute values, which would allow a simpler scheduled DAG.
- UNCERTAIN: How the collector avoids two active pollers during Kubernetes redeploys.
- UNCERTAIN: Whether 15-second polling is within Darwin's supported request rate.
- UNCERTAIN: Whether Khavda's sparse irradiance (6–7 values per 15 minutes) is expected Darwin behaviour. Asset spellings are settled in [[aliases]].
- UNCERTAIN: Whether Gregory is still relevant now that Brian treated Darwin as unblocked.
- UNCERTAIN: Whether the four Tithwa UAT series were created after Mateo's October 13 reply.
- UNCERTAIN: Whether first real UAT writes and the cluster rollout succeeded after the local live-Darwin/fake-TSDB check.
- UNCERTAIN: Which Darwin entity represents Khaba, and whether its Darwin series should run alongside or replace the CSV feed.

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

Last Updated: 2026-10-15
