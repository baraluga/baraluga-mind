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
- July 14 team notes reported EPM notification setup blocked because email notifications were not working due to SMTP configuration. The recommended resolution path was IAM or identity-provider based, with console checking as a workaround.
- July 14 technical standup said APM migration was complete and SNS infrastructure was done, but Grafana still needed AWS-admin help to create or confirm a role for CloudWatch/publish access.

## Open Questions

- UNCERTAIN: Exact permissions or routing cause of MS Teams channel email 403s was not confirmed in the notes.
- UNCERTAIN: Exact root cause of production proxy 403s was not confirmed in the notes.
- UNCERTAIN: Whether the Grafana alert destination should be one shared Teams channel or separate per system still needs confirmation.
- UNCERTAIN: Whether `EPM` is the exact system name from the July 14 team meeting capture.
- UNCERTAIN: Which AWS account owns the Grafana role needed for CloudWatch/publish access.

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

Last Updated: 2026-07-14
