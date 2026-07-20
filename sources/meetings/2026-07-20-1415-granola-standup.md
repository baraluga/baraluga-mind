# Standup

Source type: Granola meeting notes

Meeting ID: `7b508710-a13c-49ab-9684-8c3c545892d2`

Meeting date/time: 2026-07-20 14:15 GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves the available Granola notes/summary. It is not a verbatim transcript.

## Discussion Notes

### Ticket Status Overview

- 1171: awaiting Carlos's approval on the spreadsheet sent, with both copied.
  - Spreadsheet lists all expected TSDB catalog changes and time series IDs.
  - Carlos to review, approve, then contact Laurent to execute TSDB changes.
  - Follow-up email and DM to Carlos planned if no response by end of day.
- 1197: set to validation; production confirmed stable.
  - All interconnector docs enabled.
  - 2019-2025 fiscal year data backfilled: capacity, JPX prices, actual flow from Bloomberg and Octo.
- Job 01: marked done last Friday.
- 1202, lookback for 2Y dashboard: set to in review.
  - Was functionally done Friday but lacked sufficient data to display.
  - Let run over the weekend; validation-ready by end of today.

### Mateo Onboarding to SMP India

- Plan: minimal handholding, let documentation gaps surface naturally.
  - Give Mateo access to QRMDMS org first, then assign to SMP India.
  - Point him to README and CONTRIBUTING markdown files.
- Mateo is technically capable and actively maintains PSDB scraper.
- Confirm whether Mateo has a GitHub corporate license; PSDB scraper is under ADO.
  - If no license, explore exposing repo to specific org without making it private.

### Mateo Onboarding Process (Environment Flow)

- Follow dev to QA to prod sequence to avoid breakage.
- Give Mateo dashboard creation rights in dev.
- Treat him as a beta tester: note any permission, access, or process friction.
  - Feedback will improve onboarding before wider rollout.

### SMP Presentation to Chantal Lee (UK)

- Chantal leads a UK data governance project: "Empowering Users with Data".
- Positive reception, especially on the user interaction layer.
- Identified potential overlap with a TSDB team initiative, Dexter or similar, akin to Airflow.
- Key open question: level of support SMP team wants to provide.
  - Build and maintain platform only, or do development for other teams?
  - To be aligned with Fred.
- No immediate action; wait-and-see; may get referrals to other teams.
- Iberia meeting later this week: end-user team like Japan/India, more activity expected.

### Logistics

- Tomorrow's daily stand-up cancelled: Belgian public holiday.
- Next sync: Wednesday.

## Next Steps

- Send follow-up email and DM to Carlos on ticket 1171 (Brian Alexander Peralta).
  - If no response by end of day today, 2026-07-20.
- Send 1202 lookback dashboard for validation (Brian Alexander Peralta).
  - Data should be sufficient by end of today.
- Onboard Mateo: grant QRMDMS org access, then SMP India, then dashboard rights (Brian Alexander Peralta).
  - Confirm GitHub corporate license first; check if PSDB scraper ADO project covers it.
- Align with Fred on SMP support model.
  - Decide: platform-only maintenance vs. active development support for other teams.

Last Updated: 2026-07-20
