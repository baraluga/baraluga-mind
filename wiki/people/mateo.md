# Mateo

## Current State

As of 2026-10-23. India stakeholder on the trading side and SMP's main India user: owns TSDB metadata and time series creation for India data, validates India tickets, and is the planned first pilot for browser-based DAG authoring. `SCR-1297` expects him to push a DAG from the chosen environment and a second user to see it in India dev Airflow. Wants to own more himself (KPI dashboard pairing, 2026-10-01). A later forecast-versus-actual exercise would move his local error calculation into a DAG and train him on the tooling, but it is deferred until Jupyter/Dolphin integration. Adrien covers when he is away. He needs to identify the exact Darwin historical API endpoint/access path that showed Tithwa data, because the machine account only confirms a 24-hour `/lastday` route.

## Feedback Notes

Observed behaviour for feedback season, as a third-party observer. Rendered by the Feedback Ledger artifact.

- **Headline**: Fixes things himself; the IDs are the bottleneck.
- **Strength** (2026-07-23): Fixed the April RestKafka outage himself and explained it plainly when asked. `sources/codex-conversations/2026-07-23-codex-conversations.md`
- **Strength** (2026-08-03): Granted all TSDB rights for the client IDs before leaving for France, and on 2026-08-27 announced his 10-day offline period in advance with Adrien as cover. `sources/meetings/2026-08-03-1415-granola-busy.md`
- **Strength** (2026-07-22): Agreed to beta-test the DAG helper onboarding; his feedback surfaced the Artifactory access gap in the docs. `sources/codex-conversations/2026-07-29-codex-conversations.md`
- **Strength** (2026-09-22): Useful dashboard feedback (the BUY/SELL axis scale problem). `sources/codex-conversations/2026-09-22-codex-conversations.txt`
- **Strength** (2026-10-01): Asked to pair on his KPI dashboard so he can replicate the process himself; accepted an end-of-year timeline. `sources/meetings/2026-10-01-1433-granola-backlog-grooming-again.md`
- **Growth** (2026-09-25): Time series creation he owns is a recurring blocker: IDs promised "today or tomorrow at the latest" (2026-07-30), 1264 waiting on him (2026-09-25), 1058 with no response (2026-07-27). Ask: batch TSDB ID requests at grooming, or name Adrien as backup creator. `sources/meetings/2026-09-25-1415-granola-smp-standup.md`
- **Growth** (2026-09-01): His email priority order conflicted with what Matthew told Francois. Ask: send priorities through one channel (the PO). `sources/meetings/2026-09-01-granola-busy.md`
## Sources

- `sources/meetings/2026-07-20-1415-granola-standup.md`
- `sources/meetings/2026-07-27-1415-granola-daily-standup.md`
- `sources/meetings/2026-07-30-1232-granola-generation-data-scraper.md`
- `sources/meetings/2026-08-27-granola-mateo-call.md`
- `sources/claude-conversations/2026-10-21-claude-smp-68dedda3.txt`
- `sources/claude-conversations/2026-10-22-claude-smp-d2cd8178.txt`
- `sources/meetings/2026-10-22-0930-granola-busy.md`

Last Updated: 2026-10-24
