# Granola: Weekly Team Meeting

Date: 2026-09-22 09:45 GMT+8
Source: Granola
Granola URL: https://notes.granola.ai/d/76f4c495-55f7-477c-a3bc-cb47104fb2cd
Meeting ID: 76f4c495-55f7-477c-a3bc-cb47104fb2cd

## Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Project Updates

- Consumer backend migrated to GitHub.
- Integration testing is in progress and blocked on front-end/back-end integration for deployment.
- Michael is depending on Artifactory and the Sabina team for migration; web hosting service is expected.
- Michael is double-checking project dependencies flagged by Nikola, including unfamiliar projects such as "coins".
- Effort is ongoing for Model Runner and Payvin (JMR).

### CrowdStrike / CloudStack Issue

- IT team update: URL is US tenant, currently blocked; Europe tenant affected.
- Root cause: customer ID configuration pointing to US instead of Europe Connect.
- Needs reconfirmation with the relevant team, Prosumer and GMR.

### TSDB Blocker (ABS-CBS)

- Problem: time series metadata creation blocks approval if metadata was not pre-created.
- Production is fully blocked; approval cannot proceed without TSDB team input.
- Placeholder meeting created for the TSDB team and internal team this Friday.
- Topics for the meeting: new provider discussion and business rules for ABS-CBS.
- UAT environment has two possible approval paths: anyone can approve, or a user with metadata admin rights can approve.
- Action noted in meeting: confirm business rules with Francesco/Jorge before Friday.

### DB Instance / GMR Tickets

- Team cannot deploy via pipeline; Yanik's ticket is also blocked by the Artifactory dependency.
- Workaround: provisioned a new DB instance for user and placed it on Bastion Prod.
- DB Manager is not working because of an RDS client security issue on Bastion Prod.
- Fix: a new network interface was created, limited to 5 security groups.
- Temporary solution: using the original IP to create the DB instance.

### Announcements and Team Activities

- APE (Annual Physical Exam) is within October; team should fill up the clinic preference form by end of day.
- Form should indicate preferred clinic and planned dates; top choice is prioritized.
- Alfred is exempted; all others should complete the form.
- Visit from Fred/Sebastian (Chris's boss) is expected Monday, Wednesday, and Saturday.
- Team encouraged to showcase skills and contributions during the visit.
- Possible office lunch and activities are planned.
- RTO (Return to Office): September is ending soon and the last capture is approaching.
- Credits/leave questions were raised for the week of the visit.
- Support week exemption: if on 24/7 support duty that week, the RTO form can reflect it.
- Standby allowance is available for those on support.
- Team check-in closed with an online word-guessing imposter game, possibly "Palanetto" or similar.

Last Updated: 2026-09-23
