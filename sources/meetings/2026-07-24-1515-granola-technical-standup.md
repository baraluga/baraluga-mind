# Technical Standup

Source type: Granola meeting notes

Meeting ID: `72386a51-22b2-4c7e-8629-a6608af2438e`

Meeting date/time: Jul 24, 2026 3:15 PM GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This is not a verbatim transcript. It preserves the available Granola-generated meeting summary and next steps.

## Discussion Notes

### Artifactory Migration Status

- Overall migration: 39% complete across all repositories.
  - Pipeline: 22% migrated.
  - Artifactory: 19% migrated.
- Packages uploaded first because they have no internal dependencies; microservices now the focus.
  - Mathematics microservice next, depends on common stocks, already uploaded.
- SFF packages with the most dependencies are being prioritized to unblock downstream work.
- Secrets and variables for Artifactory connection already set at org level.
  - Currently using personal accounts for recent publications.
  - Will swap to functional account seamlessly once available.

### Functional Account Setup

- Functional account cannot be tied to a single project, so SFF project must be created first.
- Step 1: Create SFF project in CMDB using Snow ticketing system.
- Step 2: Submit ticket to create functional account, linked to SFF project.
- Action: drop a message in the DMS One Team global chat to find who has CMDB catalog access.

### Pyrine (EKS Cluster Update)

- Snow ticket assigned but no updates yet; will ping the assignee.
- Ticket goals:
  - Schedule cluster uptime Monday to Friday.
  - Set labels to improve pod deployment.
- Ticket created earlier this week, Monday, so follow-up is appropriate now.
- Abraham requesting pod update support; meeting continuing after this standup.

### Demand / Azure Cost Monitoring

- AWS tagging and cost center monitoring already confirmed workable.
- Azure Cost Management being investigated; tagging resources looks feasible.
- ABSD index builder ticket: SSO role created, policy update remaining.
  - Reassigned so team is not blocked waiting; others can handle the back-and-forth.
- Checking with Jeka on one open question before processing further.
- ADM v2-to-v3 consumer migration: commented on ticket to verify if still needed, awaiting reply.

### Meeting Cadence and Next Steps

- Meeting reduced from 30 to 15 minutes; further reduction discussed.
- One attendee proposing to stop attending as their work is no longer technical.
- Preference to replace daily standup with a daily message in One Team chat, meeting only on blockers.
- Plan: cancel next week's sessions if migration continues smoothly.
- JMR final migration: Abraham confirmed next week; will align with Nicola on schedule.
- After JMR, remaining work is the Artifactory migration and associated technical activities.

## Next Steps

- Create SFF project in CMDB via Snow ticket.
  - Required before the functional account ticket can be submitted; post in DMS One Team chat to find who has catalog access.
- Submit functional account ticket once SFF project exists.
  - Link the account to the new SFF project in the drop-down.
- Ping Snow ticket assignee for EKS cluster update.
  - Ticket has been assigned since Monday with no updates; follow-up is due.
- Confirm JMR migration schedule with Nicola.
  - Abraham confirmed next week as the target window.
- Decide on daily standup continuation next week.
  - Cancel sessions if migration is on track; replace with daily One Team chat updates.

Last Updated: 2026-07-24
