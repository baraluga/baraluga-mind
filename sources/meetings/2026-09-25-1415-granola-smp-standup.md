# Granola Capture: SMP Standup

Date: 2026-09-25 14:15 GMT+8
Source: Granola
Meeting ID: `a5a84559-dcc9-4dcc-8c6f-87aff8c00c87`
URL: https://notes.granola.ai/d/a5a84559-dcc9-4dcc-8c6f-87aff8c00c87

## Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Sprint Status

- Sprint officially started at the top of the call.
- Active tickets summarized:
  - 1261: still waiting for access.
  - 1264: waiting on Mateo for time series creation.
  - 1265, Kaba real-time: monitor over the weekend and mark done Monday if stable.
  - 1253, Bitstack to TSDB publish: working solution in QA, with cleanup in progress across SMP India and SMP Common.
- 1266 was confirmed fixed by Louis and marked done.

### Job 61 and Ticket 1264 Coordination

- Brian and Mateo are coordinating closely with the Darwin team.
- The work is still in back-and-forth, waiting on concrete details.
- Adrien confirmed that new time series creation is needed for 1264.
- Mateo owns the metadata, so he is the owner for creating the time series.
- Mateo needs a follow-up to confirm and unblock 1264.

### Kaba Cross-Region CDH Issue, Ticket 1265

- Root cause hypothesis: CDH resources and AWS credentials are in Ireland (`eu-west-1`), while Kaba is in Mumbai.
- Cross-region access works in production but appears blocked for no-prod outside Mumbai.
- Brian tested by creating a dataset in `eu-west-1`; it was accessible from QA, no-prod, and prod without issues.
- Kaba production behaves differently because it is in a different region.
- The team is discussing with CDH support whether this is intended design or a misconfiguration.
- No CDH configuration changes have been made since project creation.
- François suggested looping in Nilor if CDH support needs additional push.

### New Technical Tasks

- Spike: assess feasibility of Grafana alerts via Teams notifications.
  - Sending email to a Teams channel is feasible.
  - Grafana-native Teams notification approach is still unclear.
  - Goal is to confirm feasibility and propose the ideal setup.
  - Separate Teams channels are planned for S&P Japan and S&P India, not shared with the existing Airflow health channel.
- Technical task: monitoring solution for the Darwin Python service.
  - Brian is drafting the ticket and laying out implementation options for whoever picks it up.

### Grafana Map Feature

- François noted that Grafana supports map panels via uploaded GeoJSON files.
- The GeoJSON file must be placed in the public directory of the Grafana installation, likely on the pod or cluster.
- François cannot do this alone and will need Michael's help to upload the file.

## Next Steps Captured

- Follow up with Mateo on time series creation for ticket 1264; Mateo owns it and it unblocks progress.
- Brian to monitor Kaba stability over the weekend and mark 1265 done if stable after production runs through Monday, 2026-09-28.
- Brian to add a spike ticket for Grafana alerts via Teams and a Darwin monitoring task.
- François to loop in Michael to upload the GeoJSON file to the Grafana pod.

Last Updated: 2026-09-26
