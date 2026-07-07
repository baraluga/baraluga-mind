# SMP Alerting and Ops

## Summary

SMP operational discussions in late June and early July focused on production incident handling, failed MS Teams email alerting, proxy errors, Grafana backup, and repeatable runbooks. The most concrete alerting direction was to add direct-email fallback when Graph API or MS Teams alerting fails.

## Details

- MS Teams email still returned 403 after switching to the NPRM68 mailbox in one June 22 note.
- June 29 notes say NPRM68 without `.sem-em` worked for users but not the Teams channel.
- July 2 planning proposed catching Graph API email failures and sending SMTP/direct email fallback alerts.
- Proposed noise control: suppress repeated alerts for about 5 days and cap alerts around 3 per day.
- July 7 standup notes say ticket 1181 added an alert-on-alert mechanism: if MS Teams alerting fails, send fallback email. A dedicated forced-failure test was set up in Japan QA for Francois to verify.
- Francois wanted the MS Teams email issue resolved quickly or escalated through a vendor meeting.
- ServiceNow incident fields discussed: affected service, symptom, and dropdown incident link.
- Proxy errors were reported as 403s in FMP Japan prod and FMP India prod while QA was consistently successful.
- Application team meeting notes describe AI-assisted runbook automation for recurring APM issues, with diagnosis time reduced from about 10-20 minutes to about 2 minutes.
- Runbooks were stored in `docs/runbooks`; Confluence discoverability was discussed because of Microsoft 365 AI and searchability.

## Open Questions

- UNCERTAIN: Exact permissions or routing cause of MS Teams channel email 403s was not confirmed in the notes.
- UNCERTAIN: Exact root cause of production proxy 403s was not confirmed in the notes.

## Sources

- `sources/meetings/2026-06-22-1415-granola-daily-standup.md`
- `sources/meetings/2026-06-29-1415-granola-standup.md`
- `sources/meetings/2026-07-02-1100-granola-sprint-planning.md`
- `sources/meetings/2026-07-02-1500-granola-sprint-planning.md`
- `sources/meetings/2026-07-02-1700-granola-application-team-meeting.md`
- `sources/meetings/2026-07-07-1415-granola-standup.md`

Last Updated: 2026-07-08
