# Granola Capture: SMP Standup

Source Type: meeting
Source: Granola
Meeting Date: 2026-10-06 14:15 GMT+8
Meeting URL: https://notes.granola.ai/d/92556b75-7ae1-401b-8106-efcd1adccba0
Granola ID: 92556b75-7ae1-401b-8106-efcd1adccba0

## Known Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Demo Rescheduled to Friday

- Demo moved to Friday; Brian confirmed available.
- Slot borrowed from Catherine McGregor's team weekly meeting.
  - Adrien confirmed they are willing to offer the time.
  - Catherine's team will be very busy otherwise, hence the move.

### Lou Dubuisson: New Point of Contact

- Lou Dubuisson is taking over Matteo's role, becoming the primary close colleague.
- Lou is not yet fully onboarded on the project; onboarding is expected in coming weeks.
- Lou was invited to Friday's demo.
- Knowledge transfer is needed: Brian and Michael to walk Lou through all DAGs created for India.
  - Goal: Lou can diagnose issues independently.
  - DAGs should be well documented with a clear data-flow overview.

### Ticket Updates

- No changes to tickets already marked done.
- Ticket 1078/1075, bilateral contract: Adrien to validate after discussing with the trader; follow-up needed because he may have forgotten.
- Tickets 1267 and 1269, Grafana Teams alert for S&P Japan:
  - Proven working.
  - Setting up channels is out of scope.
  - Confluence page written covering the Teams side, referencing the existing Grafana Confluence page.
  - To be validated after review.

### Geomap Dashboard, Tickets 1267/1269

- Geomap dashboard built in QA, binding to live IEX data.
- Color configuration is done in dashboard settings, not in the GeoJSON file.
  - This was confirmed by successfully importing the same dashboard JSON into production.
- Matteo expects three maps; all are feasible.
- Reusable panel is not prioritized yet; copy-pasting the query is sufficient for now.
- Open question: whether uploading a new GeoJSON file to the public Grafana folder requires special rights in production.
  - Brian to triple-check; behavior in production versus QA may differ.

### Upcoming Actions and Sprint Close

- Demo prep: Francois to lead the demo tomorrow.
- Sprint ritual scheduled for tomorrow.
- S&P integration point with Eric Martin added: technical discussion on Synapse integration.
  - Goal: rough order-of-magnitude estimate of sprints needed for steering committee communication.
- Sprint period: September 24 to October 7.
  - Brian and Michael to log man-hours via Promethe or DM to Francois.

## Next Steps Captured In Granola

- Follow up with Adrien on bilateral contract validation: Adrien said he would discuss with the trader but may have forgotten; needs a nudge.
- Validate Confluence page for Grafana Teams alert: review the page; if clear, mark tickets 1267 and 1269 as validated.
- Triple-check GeoJSON file upload rights in production Grafana: unclear whether special permissions are needed to add new country map files in production.
- Organize knowledge transfer session with Lou Dubuisson: walk Lou through all DAGs built for India; ensure documentation and data flow are clear.
- Log man-hours for sprint period September 24 to October 7: send number of days spent to Francois via Promethe or DM.

Last Updated: 2026-10-07
