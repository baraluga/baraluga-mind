# SMP Alerting and Ops

## Current State

As of 2026-10-21.

- **Grafana alerts to email and Teams.**
  - Native Grafana alerts work in India QA (`SCR-1244`); the POC was an IEX RTM 10,000 threshold, and [[francois-delcourt]] created his own alert to confirm.
  - Teams delivery (`SCR-1267`/`1269`) was proven working by 2026-10-06. Users create a Teams channel, allow external senders, and add its email address as a Grafana Email contact point, with no IT request.
  - The Confluence guide is published under SMP India next to the `SCR-1244` email guide. Validation after review is the remaining step.
  - Business/data alert channels are user-owned and kept separate from SMP's operational alerting.
- **Observability is next-period work.**
  - `SCR-1254` covers resource monitoring, starting from real pain points: Airflow CPU pressure, Airflow memory pressure, and Grafana dashboard access errors. Grafana usage tracking starts from cheap Okta or user-activity evidence.
  - `SCR-1268` covers Darwin collector monitoring: about 1 point if Jeka's existing observability stack covers it, about 3 if SMP must build a small health monitor. See [[darwin-collector]].
- **`SCR-1284` dashboard delay:** before proposing the Airflow dual-write bypass described in [[smp-india]], the team needs timing evidence across scrape → TSDB → CDH, with mean and standard deviation for one IEX series and one non-IEX source.
- **Next India operational change:** create a dedicated Teams channel for DAG-failure notifications. This is separate from user-owned business/data alert channels; the captured review does not state its owner, routing, or implementation date.

## Background

- **Airflow alerting:** DAG failures go to Teams by emailing a channel through Microsoft Graph, with an SMTP fallback (`mailhost.infrasys16.com:25`) to support recipients when Graph fails. This "alert-on-alert" fallback came from `SCR-1181` in July. Proposed noise control was roughly a 5-day repeat suppression and about 3 alerts per day.
- **Grafana alerting mechanics:**
  - Alert rules are not imported through dashboard JSON; use the HTTP API.
  - Alerts fire on both breach and recovery.
  - Alerts created programmatically are read-only in the UI, while ones created by end users behave normally.
  - SMP Grafana is VPN-only, so live checks need a VPN session.
  - Grafana and Airflow are separate Helm releases in the same namespace, according to the checked-in design.
- **Debug email:** `send_debug_dag_email` in `smp-common` (`SMP_DEBUG_EMAIL_ENABLED`, `SMP_DEBUG_EMAIL_RECIPIENTS`) is for manual and debug DAG runs only, not production monitoring.
- **Monitoring stack:** Prometheus already runs in the SMP cluster with namespace dashboards. Synapse was building fuller Prometheus/alerting integration as of September, and Jeka is the current SMP monitoring owner. Signups runs Loki on its cluster, which is a possible reference.
- **Splunk versus Grafana:** the IS team prefers Splunk for 24/7-supported production monitoring because it has in-house expertise. Grafana stays the SMP tool.
- **Recurring patterns:**
  - Athena `GetWorkGroup` throttling in shared accounts can clear before anyone investigates. Collect the dashboard, time, request ID, and account/role/region when it recurs.
  - Paused DAGs that still receive queued runs point to a stale trigger configuration. Stop the triggers first, then decide per DAG to unpause or retire it.
- **Product framing (2026-08-24):** the Airflow/Grafana capability spikes (`SCR-1221`/`1222`) are product-discovery demos. Start from a named persona and pain point; "interesting, but no demonstrated demand" is a valid outcome.
  - The recommended Airflow features were Assets, deadline alerts, self-service Params/backfills, exception-aware retries, and versioned DAG bundles.

## History

- 2026-07: MS Teams email 403s led to the Graph-then-SMTP fallback (`SCR-1181`).
- 2026-08-20: Airflow and Grafana capability spikes delivered with demos.
- 2026-09-14: first working Grafana email alert in QA.
- 2026-10-05/06: Grafana-to-Teams path proven and documented.

## Open Questions

- UNCERTAIN: Whether Grafana email alerts reached production after the 2026-09-23 "coming days" plan.
- UNCERTAIN: Whether traders want alerts beyond internal use. Mateo was to confirm.
- UNCERTAIN: Whether Synapse's Prometheus integration covers the SMP cluster and the Darwin pod.
- UNCERTAIN: Whether `Pathway`, in the delay path, is an exact system name.

## Sources

- `sources/meetings/2026-07-07-1415-granola-standup.md`
- `sources/codex-conversations/2026-07-09-codex-conversations.md`
- `sources/codex-conversations/2026-08-20-codex-conversations.txt`
- `sources/codex-conversations/2026-08-24-codex-conversations.txt`
- `sources/meetings/2026-08-27-granola-fedv-chapter-meeting.md`
- `sources/codex-conversations/2026-09-02-codex-conversations.txt`
- `sources/codex-conversations/2026-09-10-codex-conversations.txt`
- `sources/meetings/2026-09-14-1415-granola-standup.md`
- `sources/meetings/2026-09-18-1415-granola-smp-standup.md`
- `sources/meetings/2026-09-21-1700-granola-smp-technical-consultation-on-darwin.md`
- `sources/meetings/2026-09-23-1630-granola-smp-sprint-review.md`
- `sources/codex-conversations/2026-09-25-codex-conversations.txt`
- `sources/codex-conversations/2026-09-29-codex-conversations.txt`
- `sources/meetings/2026-09-30-1530-granola-sprint-backlog-grooming.md`
- `sources/meetings/2026-10-05-granola-smp-standup.md`
- `sources/codex-conversations/2026-10-05-codex-conversations.txt`
- `sources/meetings/2026-10-06-1415-granola-smp-standup.md`
- `sources/meetings/2026-10-08-1131-granola-sprint-planning.md`
- `sources/meetings/2026-10-09-1415-granola-daily-standup.md`
- `sources/meetings/2026-10-21-1630-granola-smp-review.md`
- Older sources (June–July Teams/APM threads) are in this page's git history before 2026-10-11.

Last Updated: 2026-10-22
