# Granola Capture: Mateo Call

Source Type: meeting
Source: Granola
Meeting Date: 2026-10-14 14:41 GMT+8
Meeting URL: https://notes.granola.ai/d/f893962c-14a8-4ac7-9c7d-77625a9ed0bd
Granola ID: f893962c-14a8-4ac7-9c7d-77625a9ed0bd

## Known Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Darwin API Scraper

- Proxy and authentication work was blocked for about a week while IT whitelisted Okta and the Darwin base URI.
- IT had flagged the URI as legacy, then opened a group chat with Darwin contacts to verify the correct URL.
- The work was unblocked on 2026-10-13; testing is ongoing.

### Kaba Time Series Addition

- Mateo will add about four Kaba time series to the Darwin scraper, using the Darwin API request type ENS7 rather than Kafka's ENKHA.
- The data already has backups; Mateo will provide the time-series details in chat.
- Louie is also involved on HPX.

### Grafana Dashboard Issues

- Map panels copied into Mateo's new dashboard show region, band, and threshold errors. The suspected cause is a dollar-sign mismatch in copied JSON or query configuration.
- Some panels ignore the top-level dashboard time selector and appear fixed to their own time range, producing inconsistent ranges across the dashboard.

## Next Steps Captured In Granola

- Brian to investigate the Grafana map-panel errors in Mateo's dashboard.
- Brian to add the Kaba time series to the Darwin scraper once Mateo shares the details.

Last Updated: 2026-10-15
