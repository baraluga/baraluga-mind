# Granola Capture: SMP Standup

Source Type: meeting
Source: Granola
Meeting Date: 2026-10-05 14:15 GMT+8
Meeting URL: https://notes.granola.ai/d/997a87ef-1572-4b5d-b375-abb8f8fe7816
Granola ID: 997a87ef-1572-4b5d-b375-abb8f8fe7816

## Known Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Blocked Tickets Overview

- Legacy scraper validated: 3 points done.
- 3 tickets currently blocked:
  - 2 tickets blocked by Darwin proxy issue, awaiting IT response requested by Michael.
  - Ticket 41274 blocked on missing TSDB IDs.
    - Expected 5 TSIDs: day-ahead market today and next day, GTAM today and next day, RTM.
    - Clarified as 3 time series, not 5, with a 2-day forward view per series.
    - Escalated to Adrien since Matteo is off; expected to unblock quickly.

### Bilateral Contracts Tickets

- Comment spotted on dashboard, noted and updated.
- Screenshot attached to ticket.
- To be validated and shown to Adrien in the upcoming session.

### Grafana Alerts: Teams Integration

- Confirmed feasible with no IT requests needed.
- Setup flow:
  1. Create a Teams channel.
  2. Get the channel's assigned email address.
  3. Configure channel to accept external senders.
  4. Add as a contact point in Grafana.
- Agreed: channel creation is the user's responsibility, not the team's.
  - Use case: traders setting price-threshold alerts for their own buckets, such as GTAM.
- Deliverable for ticket 1267: Confluence page covering Teams channel setup, email config, and Grafana contact point linking.

### IT Call and Grid India Access

- Scheduled IT call related to Grid India.
  - Proposed solution: 1-2 static IPs for routing traffic to India.
  - Zscaler enablement for Grid India may not be legally permitted.
- HDX access confirmed working on local machines and is low priority.
- Ticket 507: awaiting Michael's input on pipeline role requirements.

### Sprint Status and Demo

- Sprint mostly in waiting mode; backlog item Grafana alerts picked up proactively.
- Next sprint already has tasks lined up.
- Demo on Wednesday: François to present, since Brian has done 2-3 consecutive demos.
  - Michael or François preferred; Brian stepping back from demoing.
- Presentation review to follow this call, with Adrien joining after to adjust content.
  - Some items Adrien will not escalate to his boss; he knows the internal dynamics.

## Next Steps Captured In Granola

- Create Confluence page for Grafana Teams integration (Brian): document Teams channel setup, email address retrieval, and Grafana contact point config for ticket 1267.
- Confirm TSDB ID count and structure with Adrien: clarify whether it is 3 or 5 time series to unblock ticket 41274.
- Present Wednesday sprint review demo (François): Brian stepping back after 2-3 consecutive demos.

Last Updated: 2026-10-06
