# Granola Capture: Darwin API

- Date: 2026-09-18 12:30 GMT+8
- Source: Granola
- Meeting ID: `3bc7bc02-9511-4bfc-aadb-0a628084dd28`
- Title: Darwin API
- Known participants:
  - Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Private Notes

- okta authenticate
- BaseUrl
- OktaAut

## Summary

# Project Overview

- Goal: real-time energy data collection for assets NC3 and NC4 (ActivePower values in kWh)
- Target: one value per minute, delivered in real time

# Scraping Approach

- Preferred: scraper runs every minute, one value per call
- Acceptable alternative: scraper runs every 5 minutes, collecting minute 0 through 4, then publishes
  - Uncertainty around whether the API returns historical minute-by-minute data or only the value at the exact moment of the call
  - Historical endpoint tested but appeared buggy or delayed during the call
  - Worth investigating further as a fallback

# Darwin API and Documentation

- No formal written documentation (no Confluence equivalent)
- Available resources:
  - Postman collection file (sent via Teams by Matteo's contact)
  - 2-3 video walkthroughs from the RNF team in France
- Matteo to send all of the above via chat

# Authentication (Okta)

- Auth method: OAuth 2.0 via Okta (OktaProd environment)
- Flow: open Postman collection, go to Authorization, click "Get New Access Token"
  - Redirects to Okta login, returns a bearer token
- Base URL and endpoints are in the Postman file
- Access to the Darwin API must be formally requested; Matteo will handle this for Brian

# Next Steps

- Send Postman collection file, videos, and API documentation (Matteo)
  - Full summary to be shared via Teams chat after the call.
- Request Darwin API access on Brian's behalf (Matteo)
  - Access must be formally requested; Matteo will also share the technical contact from the RNF France team.

Last Updated: 2026-09-19
