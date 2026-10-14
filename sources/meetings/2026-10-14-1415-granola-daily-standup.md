# Granola Capture: Daily Standup

Source Type: meeting
Source: Granola
Meeting Date: 2026-10-14 14:15 GMT+8
Meeting URL: https://notes.granola.ai/d/906102d6-ff9c-4e1f-bdd8-97f352ebd393
Granola ID: 906102d6-ff9c-4e1f-bdd8-97f352ebd393

## Known Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Darwin Connector Progress

- The Darwin API is accessible from the cluster and Brian created its CI/CD pipeline.
- Building and pushing the collector image remains blocked by an unassigned SMP India role ticket for AWS ECR permissions.
- Michael is helping test the Darwin tickets; he is also blocked from DashC and has raised a local IT ticket.

### HPX Scope Expansion

- Expected HPX time series increased from 24 to 32 after including an additional HPD market from the same source.
- The ticket was resized to two points and remains blocked until time-series IDs arrive.
- Markets run as separate parallel tasks, so a missing dataset does not stop the others.

### IEX Real-Time Prices DAG

- The QA DAG polls IEX every minute and skips downstream work when no data is new; the first observed delivery to CDH took 1 minute 2 seconds.
- Expected end-to-end delay is up to about five minutes including polling, processing, and Grafana refresh.
- A proposal is to use a five-to-ten-minute default interval and increase frequency during the critical trader window, such as 11 AM IST.

### Tickets, Backlog, and Access

- Tickets 1285, 1288, and 1292 await validation. Ticket 1288 requires a new KABA file for end-to-end testing; ticket 1292's DUX-list access was confirmed in dev chat and can move to done.
- The KABA S3 bucket is healthy but had no October 13 file; the latest data was October 12. This was not assessed as a pipeline defect.
- The RFC issue appears upstream in the Lambda scraper rather than the team's `reg_scraper`.
- Japan and India teams can see each other's dashboards because they share an Intact app instance; separation is desirable but not urgent.

## Next Steps Captured In Granola

- Follow up on the unassigned SMP India ECR role ticket.
- Propose the IEX schedule change to Mateo and Adrien.
- Validate tickets 1288 and 1292 when the KABA file is available.

Last Updated: 2026-10-15
