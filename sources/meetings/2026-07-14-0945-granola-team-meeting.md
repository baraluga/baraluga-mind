# Team Meeting

Source type: Granola meeting notes

Meeting ID: `5eacc973-3f34-4d00-8f20-acc080e8baad`

Meeting date/time: Jul 14, 2026 9:45 AM GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves available Granola notes/summaries. It is not a verbatim transcript.

## Discussion Notes / Summary

### Sprint Review Reminder

- Sprint review scheduled for tomorrow.
- Roundtable on project issues and concerns held before main agenda.

### Technical Updates and Blockers

- File browser plugin: authentication issue after upgrade to new non-Airflow version.
  - Version context: 3.3.0 vs. 3.2.2.
- EPM notification setup blocked.
  - Email notifications not working due to SMTP configuration issue.
  - Workaround: check console later.
  - IAM/identity provider approach recommended as resolution path.
- Walnut migration ongoing; support available until Friday.
- Clickstart migration: pre-migration work continuing.
  - Custom node group labels needed for deploying resources to specific node groups.
  - Node memory variance: 11 GB vs. 256 GB nodes require specified targeting.
  - Cleanup task needed: update roles for deploying resources per node group.
- Extruder remediation: assessing whether to postpone remaining tasks.
  - Critical issues to investigate first; remaining remediation to follow go-live.

### Announcements and Team Updates

- New project starting with Joy, a consultant, hopefully next week.
- Two tickets assigned: technically alerts and young century setup.
- Restructuring update: company separating into cleaner energy and renewables, including solar, heating, and cooling.
  - Two gigawatts to be set up in the Philippines; current capacity unclear, with approximately 1.5 MW mentioned.
  - Job security confirmed for the team.
- Possible next team event: bonus distribution or contract signing celebration.
- One-day workshop on stakeholder management and requirements elicitation planned.
  - Waiting on consultant to conduct the training.
  - Rationale: team needs skills to extract information from stakeholders more effectively.
- Training reminder: overdue "5 Keys to Sustainable Performance" module, deadline was end of June.
  - Can be completed while waiting for Jira tickets to reopen.

### Calendar and Logistics

- July 14: National Day of Belgium, no afternoon stand-up.
- Christina off: July 22 to August 14.
- August 2-22: CPL period noted.
- Jira still being troubleshot; workaround: use incognito mode or Chrome authenticator.
- Next check-in: Tuesday, July 21, with Michael.

## Next Steps / Action Items Present in Granola

- Address the file browser plugin authentication issue after the upgrade.
- Resolve EPM email notification setup; IAM/identity provider approach was recommended.
- Continue Walnut migration while support is available until Friday.
- Continue Clickstart pre-migration work, including custom node group labels and role cleanup.
- Investigate critical Extruder remediation issues before deciding whether to postpone remaining tasks.
- Complete overdue "5 Keys to Sustainable Performance" training.

Last Updated: 2026-07-14
