# Granola Meeting Notes: Tech Interview: Angelica Lapastora

- Meeting ID: `87c7ef64-8d5d-40a1-a30c-bbf1b4dbc612`
- Date: 2026-07-09 10:00 GMT+8
- Source type: meeting
- Source: Granola meeting notes
- Participants known to Granola: Brian Alexander Peralta

## Private Notes

- What are models for you? Can you reiterate when it would be appropriate to use models?
- You said tests are important. Why? As a team lead, what would be your "executive order" to make sure tests are given the same importance?
- Not giving senior vibes. Matt was a clear senior.
- Might be her communication style, but it feels too simplistic. She likes to say very obvious things.
- A strong communicator knows how to level with the audience.

## Summary

### Candidate Overview

- Angelica is a Python Philippines member with a strong Python background.
- Prior experience includes AngularJS, Node.js, and a Laravel-to-Django migration project.
- No formal React experience is listed on the CV; she used Claude/Cursor to build the React frontend.
- Prior role included handling 2GB+ files with concurrent chunking.

### Project Demo: Solar and Wind Monitoring Dashboard

- Architecture: React frontend, Flask backend, and Ollama plus RAG chatbot.
- Chatbot runs locally, not in the cloud; SQLite is used for lightweight storage.
- Data is pulled manually from the Open-Meteo API before each backend run.
- ETL pipeline fetches raw data, cleans it using IQR anomaly detection, and stores it in a clean observations table.
- Cleaning rationale included removing negatives, enforcing client rules, and handling API inconsistencies.
- Flask was chosen over Django because the project had one endpoint and did not need MVC/models at that scale.
- Chatbot is not yet integrated into the frontend and still runs in the terminal.

### Architecture Review: AWS Serverless Diagram

- Setup reviewed: Singapore client posts orders through API Gateway to Lambda, data is stored in DynamoDB in Ireland/eu-west-1.
- DynamoDB stream triggers a processor Lambda, which writes CSV to S3.
- S3 event triggers another Lambda that updates order status in DynamoDB.
- Angelica suggested ELB for load balancing, SNS for logging/notifications, and SQS for queuing.
- Security gap identified: API key passed in HTTP header; Angelica suggested AWS Secrets Manager, and the interviewer raised OIDC as an alternative.
- Major issue identified by interviewer: infinite event loop caused by order update triggering the same DynamoDB stream flow repeatedly.
- Angelica did not independently spot the infinite-loop issue.

### Interviewer Assessment

- Questions asked covered React experience, models, when models are appropriate, why tests matter, and how a team lead would enforce test importance.
- Assessment: not giving senior vibes; Matt was a clearer senior comparison.
- Communication felt too simplistic and often stayed at obvious statements.
- She spotted some improvements in the AWS diagram but missed the core infinite-loop issue.
- Initial latency/load approach was reasonable and aligned with current policies.
- Preliminary ranking: medium-low, from Alfred's assessment.
- If passing, next step would be a panel interview with European colleagues.
- Future interviews should be extended to at least 1.5 hours to allow more demo and code review time.

Last Updated: 2026-07-09
