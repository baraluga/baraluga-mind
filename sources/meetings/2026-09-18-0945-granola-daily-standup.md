# Granola Capture: Daily Standup

- Date: 2026-09-18 09:45 GMT+8
- Source: Granola
- Meeting ID: `806be39c-fc5a-42c3-846e-15b8892faadf`
- Title: Daily Standup
- Known participants:
  - Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

# Deployment Blockers and Timelines

- Urgent deployment request to production targeting tomorrow (Sat 19th Sep) or Monday/Tuesday 21st-22nd Sep
  - If quick ticket: can check and proceed sooner
  - If complex: may need to wait until next week
- New target date: October 9th for main progress milestone
  - Signups flagged as critical path item
  - Two sprints (current + next) allocated to make it production-ready
- UAT missing file in production (August 24th issue)
  - No NSH associated with it
  - Request to add missing file to repository (UAT.shan)

# Signup and Long-Term Fix

- Signups stubbing flagged as urgent for the Dolphy product
- Long-term fix needed to resolve domain error
  - Runbook to be created on how to fix the net/apartment error
  - Preference to consolidate into one long-term fix rather than multiple patches
- Sign-up order flow checked; pending confirmation if correct and allowed
- No migration preferred; if migration needed, key vault instance is readable from within cluster
  - Programmatic access to key-value secrets makes it a straightforward tech task

# Brian's Updates (SMP and Handover)

- Confirmation received from Mateo (yesterday, 17th Sep) on 2 tickets, now unblocked
  - Both tickets ready for validation; sending to validation team
  - Tickets open since August 5th
- Dashboard and pipeline for automated SMP image deployment: in progress
- Official handover: final feedback stage
  - If all goes well, targeting finalization by today (Friday 19th Sep)

# Monitoring and Access Requests

- New APM alerts learned and being implemented
  - Alert implementation started but not yet tested
  - Priority today: ticket 544, black box exporter implementation
- Abram's request: monitoring stock deployment to prod for Piri
  - Will inform and support regarding deployment
  - Access request for Rancher to be raised
- File manager ticket: investigation underway; services confirmed under the same umbrella

# Next Steps

- Add missing UAT file to repository
  - UAT.shan file missing from production since August 24th; no NSH associated.
- Send 2 unblocked SMP tickets for validation (Brian Alexander Peralta)
  - Confirmed by Mateo on 17th Sep; both tickets ready.
- Finalize SMP handover by today, 18th Sep (Brian Alexander Peralta)
  - Last feedback stage; targeting completion by end of Friday.
- Investigate and implement ticket 544 (black box exporter)
  - Priority for today; alert implementation started but untested.
- Raise Rancher access request for Abram's prod monitoring
  - Needed to support deployment monitoring for Piri in production.

Last Updated: 2026-09-19
