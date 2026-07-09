# Recruitment 2026

## Summary

Senior Software Engineer recruitment in late June and early July 2026 used a multi-stage process: HR interview, manager interview, take-home plus technical interview, then panel interview. The target profile was senior, with strong Python, cloud experience, quality standards, and some AI-in-workflow awareness.

The process explicitly allows AI tool use, but candidates must explain and defend their work.

## Details

- June 30 pipeline: 33 candidates, 8 new CVs, 23 failed, 1 at panel interview.
- June 30 take-home stage: 5 candidates reached take-home, with 1 failed, 1 high-potential with panel scheduled, 1 technical interview being scheduled, and 2 still completing assignments.
- July 2 application team meeting mentioned 41 candidates and 1 at final interview stage.
- Screening criteria discussed: 9-10+ years experience, Python required, AWS/Azure preferred, and some AI-in-workflow knowledge expected.
- Azure experience was flagged as higher priority than AWS in the June 30 alignment.
- Manager interview checks culture, leadership, architecture definition, quality standards, and scrum familiarity.
- Take-home task: scrape Open-Meteo, normalize/transform/load, and visualize in a dashboard.
- Assessment areas include CI/CD, GitHub Actions, Git hooks, commit hygiene, testing, and security.
- Bonus task: AI agent to query the dataset.
- Technical interview includes code walkthrough, sample code review, and AWS architecture design review.
- Sample code contains deliberate flaws such as a global dictionary memory leak.
- July 8 Matt Mendez interview notes describe a candidate with C# as primary language, self-taught Python, AWS exposure around S3/Lambda/Fargate, and DevOps experience including EC2-to-ECS Fargate migration, canary deployment, CIDR conflict handling, and CDK adoption.
- Matt's take-home used Open-Meteo, local Parquet/DuckDB, IQR-based anomaly detection, a Dash dashboard, and an Anthropic-powered chatbot. S3 and CI/CD were planned but not implemented.
- The July 8 architecture review showed strengths in spotting cross-region latency and transactional-data concerns, but gaps around CloudFront/CDN usage, static API-key risk, and event-loop risk across S3/Lambda/DynamoDB.
- A July 8 pasted note preserved candidate interview prompts about Day 0 technical-lead priorities, Gitflow versus trunk-based development, delayed projects, good and bad git commits, and test culture.
- Panel interview checks communication with EU counterparts and hypothetical problem-solving.
- Remote cheating risk in technical assessments was discussed; in-person attendance was recommended for problem-solving/coding.
- July 9 Angelica Lapastora interview notes describe a Python-heavy candidate with AngularJS, Node.js, Laravel-to-Django migration experience, and a React/Flask/Ollama/RAG dashboard demo built with Claude/Cursor assistance.
- Angelica's demo used manual Open-Meteo pulls, IQR anomaly detection, SQLite, and a terminal-only local chatbot. Flask was justified over Django because the project had one endpoint and did not need Django's MVC/model structure.
- In the AWS serverless design review, Angelica suggested ELB, SNS, SQS, and Secrets Manager improvements, but did not independently spot the DynamoDB stream/S3/Lambda infinite-loop risk.
- Interviewer assessment in the note: medium-low, not clearly senior compared with Matt, with communication often staying at obvious statements. If passing, the next step would be a panel interview with European colleagues.
- Future technical interviews should be at least 1.5 hours to leave enough time for demo and code review.

## Open Questions

- UNCERTAIN: The count moved from 33 candidates on June 30 to 41 candidates on July 2; this likely reflects pipeline growth, but the notes do not reconcile the numbers.
- UNCERTAIN: The Granola title says "Matt Mendez" but the candidate overview says "Matt Mendeswell"; this may be a transcription/name artifact.
- UNCERTAIN: Angelica's exact seniority signal may need calibration against Alfred's assessment and any panel feedback if the process continues.

## Sources

- `sources/meetings/2026-06-23-0945-granola-team-meeting.md`
- `sources/meetings/2026-06-30-1600-granola-recruitment-alignment.md`
- `sources/meetings/2026-07-02-1700-granola-application-team-meeting.md`
- `sources/meetings/2026-07-08-1100-granola-matt-mendez.md`
- `sources/notes/2026-07-08.md`
- `sources/meetings/2026-07-09-1000-granola-tech-interview-angelica-lapastora.md`
- `sources/codex-conversations/2026-07-09-codex-conversations.md`

Last Updated: 2026-07-09
