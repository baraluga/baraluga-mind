# SMP Alerting and Ops

## Summary

SMP operational discussions in late June and early July focused on production incident handling, failed MS Teams email alerting, proxy errors, Grafana backup, and repeatable runbooks. The most concrete alerting direction was to add direct-email fallback when Graph API or MS Teams alerting fails.

## Details

- MS Teams email still returned 403 after switching to the NPRM68 mailbox in one June 22 note.
- June 29 notes say NPRM68 without `.sem-em` worked for users but not the Teams channel.
- July 2 planning proposed catching Graph API email failures and sending SMTP/direct email fallback alerts.
- Proposed noise control: suppress repeated alerts for about 5 days and cap alerts around 3 per day.
- July 7 standup notes say ticket 1181 added an alert-on-alert mechanism: if MS Teams alerting fails, send fallback email. A dedicated forced-failure test was set up in Japan QA for Francois to verify.
- July 9 Codex/Copilot captures add a debug-only email callback, `send_debug_dag_email`, in `smp-common 0.4.3`, using `SMP_DEBUG_EMAIL_ENABLED` and `SMP_DEBUG_EMAIL_RECIPIENTS`. The callback is for manual/debug DAG runs, not production monitoring.
- July 9 captures say the Japan interconnector manual backfill DAG temporarily used the debug email callback for both success and failure, but runtime deployment needed the QA Airflow image to include `smp-common 0.4.3`.
- July 9 notes say `SCR-1181` email alert debugging showed the current DAG was not reaching the expected failure point, so lack of alert did not prove the alert path itself was broken.
- Francois wanted the MS Teams email issue resolved quickly or escalated through a vendor meeting.
- ServiceNow incident fields discussed: affected service, symptom, and dropdown incident link.
- Proxy errors were reported as 403s in FMP Japan prod and FMP India prod while QA was consistently successful.
- Application team meeting notes describe AI-assisted runbook automation for recurring APM issues, with diagnosis time reduced from about 10-20 minutes to about 2 minutes.
- Runbooks were stored in `docs/runbooks`; Confluence discoverability was discussed because of Microsoft 365 AI and searchability.
- July 9 technical standup says Grafana APM alerts were created and tested by lowering the threshold. SMTP was not configured; the proposed path was an encrypted common-stack SNS topic with a Teams channel subscriber.
- July 13 standup says the Grafana-alert SNS stack was created and testing was in progress; Sentry for APL was next.
- July 14 team notes reported APM notification setup blocked because email notifications were not working due to SMTP configuration. The recommended resolution path was IAM or identity-provider based, with console checking as a workaround. A July 15 clarification says this was APM, not EPM, and Huk is working on it.
- July 14 technical standup said APM migration was complete and SNS infrastructure was done, but Grafana still needed AWS-admin help to create or confirm a role for CloudWatch/publish access in the APM context.
- July 17 technical-activities notes say an SNS publisher role had been created and attached to the Grafana service account, but a web-identity/STSS error still persisted and Jeka was asked for namespace access. The SNS ticket was not expected to close that day because of a later demo.
- The same meeting introduced a broader alerting idea from the Prosumer simulation blockage: restore Prosumer-specific alarms if needed, but also consider account-level global alarms because the immediate root cause was shared AWS infrastructure capacity rather than a Prosumer application failure.
- August 11 backlog grooming proposed a short spike on out-of-the-box Airflow and Grafana features not yet used by the team. Airflow assets were called out as unexplored potential low-hanging fruit; Grafana alerting could replace daily manual dashboard checks for threshold-driven cases such as power prices; and Grafana monitoring views should be mapped for operational reuse.
- The intended spike output feeds the August 28 steering committee presentation, with findings expected by August 21 before the other speaker's August 24-30 holiday. The meeting expected two tickets: one for Grafana features and one for Airflow features.
- August 19 notes refined the spike output into a table of feature name, description, usefulness assessment, and applicable use cases. The same notes proposed Grafana threshold alerts that users can configure themselves, plus Prometheus and Loki monitoring for SMT health, pod usage, and processing load.
- The proposed resource-monitoring work is expected to fit Airflow and Grafana, take under five days, and provide earlier warning before failures or scaling issues.
- The August 20 SCR-1221 Airflow spike narrowed the recommendation to five practical improvements: Airflow Assets, deadline alerts, self-service runs with Params/backfills, exception-aware retry policies, and versioned Git DAG bundles. Assets were judged useful mainly for Japan's orchestration complexity and lower-value for India today; the recommended proof was Japan OCCTO daily capacity feeding a reconciliation consumer.
- The SCR-1221 and SCR-1222 work produced Confluence-ready tables plus private interactive demos: `https://smp-airflow-capabilities.baraluga.chatgpt.site` and `https://smp-grafana-top-five.baraluga.chatgpt.site`.

## Open Questions

- UNCERTAIN: Exact permissions or routing cause of MS Teams channel email 403s was not confirmed in the notes.
- UNCERTAIN: Exact root cause of production proxy 403s was not confirmed in the notes.
- UNCERTAIN: Whether the Grafana alert destination should be one shared Teams channel or separate per system still needs confirmation.
- UNCERTAIN: Which AWS admin can create the Grafana role needed for APM CloudWatch/publish access.
- UNCERTAIN: Whether `STSS` and `Jeka` are exact names from the July 17 technical-activities source.
- UNCERTAIN: Whether the Japan OCCTO daily capacity to reconciliation Asset proof was built or adopted after the August 20 demo.
- UNCERTAIN: Whether `SMT health` is the exact term from the August 19 backlog grooming note or a transcription artifact for SMP health.

## Sources

- `sources/meetings/2026-06-22-1415-granola-daily-standup.md`
- `sources/meetings/2026-06-29-1415-granola-standup.md`
- `sources/meetings/2026-07-02-1100-granola-sprint-planning.md`
- `sources/meetings/2026-07-02-1500-granola-sprint-planning.md`
- `sources/meetings/2026-07-02-1700-granola-application-team-meeting.md`
- `sources/meetings/2026-07-07-1415-granola-standup.md`
- `sources/notes/2026-07-09.md`
- `sources/codex-conversations/2026-07-09-codex-conversations.md`
- `sources/copilot-conversations/2026-07-09-copilot-conversations.md`
- `sources/meetings/2026-07-09-1515-granola-technical-team-standup.md`
- `sources/meetings/2026-07-13-1515-granola-technical-activities-standup.md`
- `sources/meetings/2026-07-14-0945-granola-team-meeting.md`
- `sources/meetings/2026-07-14-1515-granola-technical-standup.md`
- `sources/notes/2026-07-15-ingest-handover-clarifications.md`
- `sources/meetings/2026-07-17-1600-granola-technical-activities.md`
- `sources/meetings/2026-08-11-1430-granola-backlog-grooming.md`
- `sources/meetings/2026-08-19-granola-busy.md`
- `sources/meetings/2026-08-19-granola-backlog-grooming.md`
- `sources/codex-conversations/2026-08-20-codex-conversations.txt`

Last Updated: 2026-08-20
