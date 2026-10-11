# SMP India Access

## Current State

As of 2026-10-07. Network and access blockers are the main drag on [[smp-india]] delivery.

- **Grid India (`SCR-1230`):** geo-blocked. It needs legal approval for VPN or scraping access first, then a separate WBS portal approval. Zscaler enablement may not be legally permitted. One or two static IPs routing to India was proposed on 2026-10-05. The approval email will go to Francois, "Pong" (source spelling, likely Bong), Frederic, Brian, Michael, and the SMP team.
- **Darwin:** the proxy allowlist is missing, so the dev cluster gets 403s. The request is with IT. See [[darwin-collector]].
- **H. India national website:** Zscaler returns 403, but the site works from the office and off-Zscaler. The fix is a security whitelist ticket with James Snow. The same blocker got an earlier HPX scraper ticket rejected.
- **Cross-account CDH/S3:** Khaba QA could not read the production-owned source bucket because of an explicit AWS Organizations SCP deny. CDH support changed an SCP on 2026-09-30 to allow cross-region access; Airflow QA validation is still pending. See [[smp-india]].
- **Escalation path:** [[michael]] is the point person. The India geo-restriction for cluster access went to Frederik on 2026-09-21, because France/Belgium IT had no India infrastructure or budget path and India VPCs were reportedly blocked in the current AWS account.

## Background

- **Evidence of geo-blocking:** on 2026-09-10, probes from Mumbai, Bengaluru, and Hyderabad got HTTP 200 from Grid India, while Singapore, Los Angeles, and Manila got connection resets. That does not prove report downloads work from India.
- **Two separate needs:** deployed scrapers need a proxy exit in India, and developers need to build and debug from machines behind Zscaler/VPN. Solving one does not solve the other.
- **Singapore precedent:** a Japan-side Singapore-only proxy workaround exists, built by Nilo. In September, though, Singapore proxy traffic was seen leaving via Ireland/US instead of Asia. IT/IS owns proxy routing, not the dev team.
- **Escalation lesson:** a proxy request on 2026-09-04 unexpectedly went up to the head of Singapore infrastructure. Nilo was looped in so Brian would not carry that alone.

## History

- 2026-06/07: intermittent proxy 403s in Japan and India prod (about 6 in 10 runs succeeded). Root cause never established.
- 2026-09-03: Khaba QA SCP denial found. On 2026-09-21 the denial named a different SCP ID.
- 2026-09-10: Grid India geo-blocking confirmed.
- 2026-09-30: CDH support changed an SCP for cross-region access.

## Open Questions

- UNCERTAIN: Whether the legal and WBS approvals are both mandatory for production scraping, or only for the current workaround.
- UNCERTAIN: Whether the H. India whitelist should cover only Brian's path or a reusable SMP execution path.
- UNCERTAIN: Whether the SCP change also fixes the KAVA Dev/QA cross-account loss.

## Sources

Main sources are below. The full trail from before the 2026-10-11 split is on [[smp-platform]].

- `sources/meetings/2026-09-01-granola-busy.md`
- `sources/meetings/2026-09-04-daily-standup.md`
- `sources/meetings/2026-09-14-1415-granola-standup.md`
- `sources/meetings/2026-09-15-weekly-team-meeting.md`
- `sources/meetings/2026-09-21-1700-granola-smp-technical-consultation-on-darwin.md`
- `sources/meetings/2026-10-01-1433-granola-backlog-grooming-again.md`
- `sources/meetings/2026-10-05-granola-smp-standup.md`
- `sources/meetings/2026-10-07-granola-sprint-review.md`
- `sources/codex-conversations/2026-09-03-codex-conversations.txt`
- `sources/codex-conversations/2026-09-10-codex-conversations.txt`
- `sources/codex-conversations/2026-09-21-codex-conversations.txt`

Last Updated: 2026-10-11
