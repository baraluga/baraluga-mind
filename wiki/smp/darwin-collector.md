# Darwin Collector

## Current State

As of 2026-10-07.

- **Blocked on network access, not code.** The collector was deployed to India dev on 2026-10-01 with [[michael]]'s help. Okta auth and the Darwin base API both return 403 because the proxy allowlist isn't configured. Michael raised the proxy request, and it was still waiting on IT on 2026-10-05.
- Local tests with the same credentials gave about 90% confidence that the flow works once the network path is open.
- On 2026-10-07 the IT ticket for Darwin API availability was marked done even though the API was flagged as legacy and not actually available. Mateo and another Darwin contact were out of office. Escalating to Gregory was planned if the path stayed blocked.
- **Tickets:**
  - `SCR-1261`: Tuticorin wind speed, wind direction, and generation.
  - `SCR-1273`: four more assets. All 15 requested measurements parse from saved responses.
  - `SCR-1268`: collector health and freshness monitoring, starting with Prometheus discovery.
- Next-period priority once access is fixed. See [[smp-platform]].

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

## Open Questions

- UNCERTAIN: Whether Darwin can replay previous-minute values, which would allow a simpler scheduled DAG.
- UNCERTAIN: How the collector avoids two active pollers during Kubernetes redeploys.
- UNCERTAIN: Whether 15-second polling is within Darwin's supported request rate.
- UNCERTAIN: Whether Khavda's sparse irradiance (6–7 values per 15 minutes) is expected Darwin behaviour. Asset spellings are settled in [[aliases]].
- UNCERTAIN: Whether Gregory is the right escalation owner.

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

Last Updated: 2026-10-11
