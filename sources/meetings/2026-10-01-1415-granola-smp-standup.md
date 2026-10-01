# Granola Capture: SMP Standup

Source Type: meeting
Meeting Date: 2026-10-01 14:15 Asia/Manila
Granola Note: https://notes.granola.ai/d/8b449326-5390-4297-9fb4-51f2990f40ce
Captured: 2026-10-02

## Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Upcoming Events and Alignment

- Demo scheduled Tuesday: introduction of Skype for Google platform with India.
  - End of day for the India team.
  - Alignment meeting follows immediately after, which is a good moment for first feedback.
- Fred to be pinged to attend the alignment meeting.
  - Useful to preview steering committee content so there are no surprises.
- Michael and Frank forwarded the demo invite.

### Ticket Validation Status

- Ticket 1265 validated yesterday.
- Tickets 1263 and December tickets pending validation.
  - 1263: re-enabling of Kava drugs in UETI, QA, and UAT; publishes to TSDB UAT.
  - Ready for validation and flagged for review.
- Decision on TSDB backfill: skip backfill for now.
  - Goal is to confirm things work and maintain the two-stage process.
  - If resource consumption becomes an issue, it can be disabled later.

### Darwin Connector: Proxy Blocker

- Collector deployed on dev with Michael's help.
- Blocker: 403 errors on both Okta auth and the base API URL.
  - Root cause: proxy not configured to allow these requests.
  - Ticket set to blocked; Michael already raised the proxy request.
- Approximately 90% confidence that the end-to-end flow will work once network/access issues are resolved.
  - Tested extensively on Mac locally with the same credentials, where it works.

### Darwin Collector Expansion

- Expanding collector to capture four additional asset values: Cavda, Sharpar, Raganesta, and Kitty.
  - All confirmed available via the API.
- Minor observation on Cavda global or tilted irradiance:
  - Only 6-7 values collected per 15 minutes, versus every minute for other assets.
  - To confirm with Mateo or Darwin team whether this is expected behavior.
- Ticket pulled to sprint; work in progress and described as straightforward, following the same pattern as Tuticorin expansion.
- One sentence in the ticket is in French and should be corrected.

### Docker Image Automation (Michael)

- Focused on SMP today.
- Darwin connector finalized for deployment in SAP India dev environment.
- Docker image also to be pushed to QA.
- Credentials/secrets applied across all SMB India stages.
- Working on automating Docker image builds using existing YAML from GitHub workflows in SMP tool.
  - Plan: use build output to update Helm values and run Helm upgrade.

## Next Steps Mentioned

- Validate December tickets, including 1263 and others flagged.
- Confirm Cavda irradiance data frequency with Mateo or the Darwin team.
- Paste Darwin proxy API URL into the ticket. Owner mentioned: Michael.

## Value Gate

Passed: contains durable project context, validation status, a technical decision, blockers, and follow-up actions.

