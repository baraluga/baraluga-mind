# Team Operations

## Current State

As of 2026-10-21. Team-wide context for the QRM Philippines team: how work is run, logged, and coordinated. SMP specifics are on [[smp-platform]], non-SMP projects on [[technical-activities]], and the GitHub migration on [[sff-walnut-migration]].

- **SMP process:** moving off strict sprints. On 2026-09-02, Brian recommended Scrumban: continuous pull, WIP limits, a visible `Waiting` state, and cycle-time metrics instead of velocity, while keeping a two-week demo and budget cadence. On 2026-10-09 the team favoured Kanban because mid-sprint pulls distort burn-down and India users already validate in near real time. This still needs discussion with Fred and Bong.
- **Time tracking:** the Philippines team left Tempo on 2026-09-01. Prométhée (also spelled Promethe) is filled every Friday. UNCERTAIN: the name of the new tracker.
- **AI credits:** to request more, email Fred and the requester with the business need, current usage, and planned use, then submit the ticket (2026-10-07).
- **Coming up:**
  - Fred and Christina's Philippines visit on 2026-11-16 to 11-20, with full attendance requested and no leave that week.
  - A three-week November Philippines trip with training: Kubernetes, possibly Copilot Studio, and Explorer sessions.
  - Dinner and Dance, tentatively 2026-11-12.
- **Recent changes:** Jerome Blanc was expected to leave at the end of September, with handover to UK contacts. Development reviews were due in Sesame by 2026-09-15.
- **QRM All (2026-10-20):** the leadership roadmap is due for validation by 2026-11-09 and manager performance scores are due in Sesame by 2026-11-13. Chronio migration/dashboard rollout was reported on track for leadership rollout in November, but the source does not establish its wider rollout status. Commercial reporting was EUR 1.45M billed against a EUR 9.17M objective, with EUR 2.85M pipeline.

## Background

- **Rules worth remembering:**
  - Never share private keys in Jira, repos, or email; use Vault (Tech Lead Roundtable, 2026-09-17).
  - Raise IT requests in the dedicated IT channel by tagging IT admin.
  - The architecture committee validates security design, not just alert hygiene.
  - Leave carry-over is capped at 5 days and must be used by June of the following year.
- **Timesheet workflow (from 2026-08-10):**
  - Pre-fill scheduled Teams meetings first, then split the rest by the active sprint's story points per project.
  - Logging tickets: `SCR-1203` Japan, `SCR-1204` India, `SCR-1205` Common.
  - Steps: 15-minute increments in Tempo, 0.125-day increments in Prométhée.
  - Prométhée must be explicitly saved and re-checked after reload; submission is a separate step.
- **Chapters:**
  - FEDV keeps standards in the org `.github` repo, synced to Confluence by a deterministic pipeline.
  - Angular standards are moving to Angular 22; PrimeNG is no longer recommended.
  - Dashboard visual standardisation was flagged.
  - The IS team prefers Splunk for 24/7 production monitoring.
- **QRM business snapshot (2026-09-15):** EUR 7.65M commercial pipeline, EUR 1.52M short of objective. The hackathon had 40+ participants and 90%+ ROTI. Lesson for next time: sponsor pitches and flat-file data up front.
- **Stakeholder framing (2026-08-28 workshop):** SMP's purpose is timely data shown in dashboards for end users. Four stakeholder groups: the dev team, the PO, Japan stakeholders, and everyone else. Narrative order: Why → Who → Success → Risk → Collaboration → Commitment.
- **Platform incidents:** the 2026-09-22 Walnut Artifactory remediation briefly affected GitHub Actions and Claude Code. A queued workflow can be a platform problem even when validation has passed.

## History

- 2026-07-08: a central technical-activities board was created, with AWS migration, Walnut migration, and security remediation epics charged per project.
- 2026-07-14: one QRM GitHub organization chosen.
- 2026-07-29: SMP projected about 15% over budget (about EUR 5,900) from added scope. Brian stayed full time through August.
- 2026-09-01: Tempo replaced for the Philippines team.
- 2026-10-09: Kanban transition proposed for SMP.

## Open Questions

- UNCERTAIN: What the new time-tracking app is called.
- UNCERTAIN: Whether SMP formally adopts Kanban or Scrumban.
- UNCERTAIN: Whether `Chronio`, `Carrier Pass`, and `Communication Plan Strategy` are the exact names and what scope they cover.

## Sources

- `sources/meetings/2026-07-08-1514-granola-aws-migration-standup.md`
- `sources/meetings/2026-07-14-1700-granola-qrm-be-chapter-meeting.md`
- `sources/meetings/2026-07-29-1500-granola-sprint-retro.md`
- `sources/codex-conversations/2026-08-10-codex-conversations.txt`
- `sources/meetings/2026-08-11-0945-granola-weekly-team-meeting.md`
- `sources/meetings/2026-08-27-granola-fedv-chapter-meeting.md`
- `sources/codex-conversations/2026-08-28-codex-conversations.txt`
- `sources/meetings/2026-09-01-1700-granola-application-team-meeting.md`
- `sources/codex-conversations/2026-09-02-codex-conversations.txt`
- `sources/meetings/2026-09-15-weekly-team-meeting.md`
- `sources/meetings/2026-09-15-qrm-all.md`
- `sources/meetings/2026-09-17-1700-granola-tech-lead-roundtable.md`
- `sources/meetings/2026-09-22-0945-granola-weekly-team-meeting.md`
- `sources/meetings/2026-10-07-granola-morning-standup.md`
- `sources/meetings/2026-10-09-1415-granola-daily-standup.md`
- `sources/meetings/2026-10-20-1500-granola-qrm-all.md`
- Migration evidence moved with the playbook to [[sff-walnut-migration]]. Older sources are in this page's git history before 2026-10-11.

Last Updated: 2026-10-21
