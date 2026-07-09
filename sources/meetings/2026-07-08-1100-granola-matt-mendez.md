# Matt Mendez

Source type: Granola meeting notes

Meeting ID: `aa368308-8b78-4dbc-ae92-6a4d61fc4ce9`

Meeting date/time: 2026-07-08 11:00 GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This is not a verbatim transcript. It preserves the available Granola meeting notes/summaries.

## Discussion Notes / Summary

### Candidate Overview

- Matt Mendeswell, technical interview. This was the second of three stages; final stage is an even interview.
- Interview panel: Alfred (senior backend/infra), Brian (frontend/infra/DevOps), Scrum Master.
- Matt's background: C# developer, self-taught Python learner, DevOps exposure with small tooling.

### Take-Home Exam Walkthrough

- Built "Anomaly Monitor" in Python: fetches solar radiation and wind speed data (10m, 100m) from Open-Meteo API.
- Covers 30-day window; saves to local Parquet/DuckDB. S3 integration was planned but not implemented.
- IQR-based anomaly flagging per site and metric.
- Dash dashboard with Anthropic-powered chatbot that is tool-guarded and not directly connected to raw data.
- Code structure separates concerns across ingest, clean, anomaly, agent, and query modules.
- Used Pydantic for validation and `.env` for environment variable management.
- Unit tests present using pytest and MagicMock; CI/CD was not committed.
- CI/CD plan, unimplemented: Dockerized app deployed to ECS Fargate, snapshots to dated S3 folders.
- Chose Fargate over Lambda due to 15-minute Lambda timeout risk on large fetches.
- Did not finish due to personal time constraints after returning from vacation Monday.
- Acknowledged heavy use of Claude to generate features; transparent about it.

### Architecture Diagram Review

- Diagram: Singapore client calling `POST /order` via API key to API Gateway in Ireland, triggering Lambda, DynamoDB, S3, and a second Lambda loop.
- Issues Matt identified:
- Cross-region latency from Singapore to Ireland.
- Proposed moving DynamoDB to Singapore; acknowledged GDPR may block this.
- Confused by the DynamoDB update loop where a third Lambda writes back to the same table.
- Raised single-source-of-truth concern; suggested RDS/Postgres for transactional data over DynamoDB.
- Issues Alfred surfaced that Matt missed:
- Infinite loop risk: S3 event triggers Lambda, which updates DynamoDB, which re-triggers the stream.
- API key authentication: static keys in a public setting; should rotate or migrate to OIDC.
- CDN/CloudFront as the correct solution for cross-region latency; Matt was unaware.

### Open Technical Discussion and Closing

- Previous infra experience: led EC2-to-ECS Fargate migration for 10+ services with a director and two infra colleagues.
- Used canary deployments to minimize disruption; tested in lower environments first.
- Managed CIDR block conflicts with third-party VPN integrations.
- AWS CDK adopted for newer services to avoid serverless YAML duplication.
- Self-assessed risks if hired:
- Python still at learning stage; C# is primary language and he is not claiming senior Python level.
- AWS strengths: S3, Lambda, Fargate; weakness on infra/networking side.
- Brian shared current DevOps setup: migrating CI/CD from ADO to GitHub; pipelines being re-established.
- Post-call team debrief notes:
- Communication can be more concise and context-aware; tends toward excessive technical detail.
- Python beginner level acceptable given C# background.
- AWS knowledge solid.
- Alfred to share further assessment.

## Next Steps / Action Items From Granola

- Alfred to share further assessment.

Last Updated: 2026-07-09
