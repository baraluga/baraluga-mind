# Francois Delcourt

## Current State

As of 2026-10-19. SMP product owner (ENGIE Belgium) and Brian's main SMP counterpart for validation, planning, sprint scope, and stakeholder safety. Not the same person as [[francois-caffont]], who owns [[atlas-dashboard]].

- Validates India tickets before they close, often cross-checking TSDB values against Grafana. Validation queues on him: tickets waited on his sign-off on 2026-07-27 (1171), 2026-09-01 (1237, 1238), and 2026-09-28 (1253, 1265).
- 2026-10-13: asked about Khaba QA failures and the minute feed's ~6h "weird state". The QA pause was intentional; the 6h bar was the file sensor timing out while blocking later runs.
- 2026-10-08: keen on Jupyter as the "frontend" for DAG contributors such as Mateo; Brian is skeptical it differs from normal DAG development unless it abstracts Airflow away. Recurring, undecided topic.
- 2026-10-08: relayed Gauthier de Maere's request for help loading Aurora data into TSDB, framed as a discussion phase: share the Mateo Aurora script, but do not start work without a framework. The script lives in [[apac-tsdb-scraper]].
- 2026-10-09: his "big no" about working for free on Aurora was read seriously by Fred; Brian read it as a joke.

## Background

- Gave Brian strong feedback on 2026-06-30: technical delivery, proposals, client relationship management, autonomy with users. Main improvement area: tickets and stakeholder messages moving too fast without looping him in. He acknowledged he could follow progress more proactively.
- Agreed working model: he adds explicit validation checkpoints before certain client-facing actions and is the safety net for production pushes and major deliverables; Brian keeps freedom for user interactions.
- Allocation was 40% on 2026-06-30; he wanted 20% or lower.
- Provides TSDB time series IDs (interconnector data, broken IEX series in September) and gathers demo requirements for Indian counterparts.
- Presented the product/business overview and demo in the 2026-08-19 SMP overview for Jeroen.
- Brian once read conflicting priority signals through him: on 2026-09-01 Mateo's email said bilateral was lower priority, while Francois heard the opposite from Matthew.

## History

- 2026-06-30: feedback session; validation-checkpoint working model agreed.
- 2026-10-19: split from a page that had merged him with [[francois-caffont]].

## Sources

- `sources/meetings/2026-06-29-1415-granola-standup.md`
- `sources/meetings/2026-06-30-1504-granola-feedback-from-francois.md`
- `sources/meetings/2026-07-02-1500-granola-sprint-planning.md`
- `sources/meetings/2026-07-27-1415-granola-daily-standup.md`
- `sources/meetings/2026-08-19-granola-smp-overview-with-jeroen.md`
- `sources/meetings/2026-09-01-granola-busy.md`
- `sources/meetings/2026-09-28-1415-granola-smp-standup.md`
- `sources/codex-conversations/2026-07-17-codex-conversations.md`
- `sources/codex-conversations/2026-08-19-codex-conversations.txt`
- `sources/codex-conversations/2026-10-08-codex-conversations.txt`
- `sources/codex-conversations/2026-10-09-codex-conversations.txt`
- `sources/claude-conversations/2026-10-13-claude-smp-31a97f39.txt`
- `sources/claude-conversations/2026-10-13-claude-smp-5c0b0e8d.txt`

Last Updated: 2026-10-19
