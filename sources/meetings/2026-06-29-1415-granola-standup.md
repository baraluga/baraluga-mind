# Standup

Source type: Granola meeting notes
Meeting ID: `d6fc8ff4-e97b-4c34-b774-3ca67f802cb6`
Date: 2026-06-29 14:15 GMT+8
Participants known to Granola: Brian Alexander Peralta

Note: This is from Granola notes/summaries, not a verbatim transcript.

## Discussed

- Yoko ticket was closed based on Friday's agreement: if okay in production, it can be closed.
- No Yoko dashboard was found at root level of production Grafana, supporting closure.
- AWS resource tagging work for SCR-1087 was underway, adding application ID and environment tags.
- Same application ID is used for Japan and India environments.
- India resources were mostly tagged; Japan tags were being backfilled from two CDK stacks.
- Cleanup ticket SER-227 included README updates across repos and Airflow variable separation up to QA.
- Prod validation was in progress; Mateo and Adrian could access the website but had issues accessing Airflow in India prod.
- Grafana in India prod was accessible; Airflow was not.
- MS Teams email issue: NPRM68 email without `.sem-em` worked for users but not the Teams channel.
- Francois wanted the email issue resolved before 09:00 or a vendor meeting scheduled.
- Interconnector dashboard first draft was published in Grafana QA and sent to Hiromi, KSK, and Hata-san.
- Two dashboard variants were prepared: one with separate JEPX prices and one combined.
- QA was flaky, likely from memory pressure; Airflow QA was crashing intermittently.
- JEPX prices matched the spreadsheet with minor rounding differences; daily values did not align because of timing differences.
- Francois advised allowing more internal validation before sending to Japanese clients.
- Need for fallback alerting when MS Teams email fails was noted.

## Next Steps

- Brian to resolve MS Teams email issue or send technical logs/code to vendor.
- Increase Airflow QA memory allocation.
- Brian to double-check historical interconnector and OCTQ spreadsheet data.
- Francois to prepare sprint backlog and sprint review.

Last Updated: 2026-07-04
