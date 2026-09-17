# Granola: Tech Lead Roundtable

Date: 2026-09-17 17:00 GMT+8
Source: Granola
Meeting ID: b1b39545-c9b3-41c7-afef-3bccededf5fa
Captured By: Brian Alexander Peralta <ba.peralta@icloud.com>

## Summary

### AWS Infrastructure Issues

- Lambdas are deployed without VPC binding across multiple projects.
- In the prod account, Prosumer is most compliant, with four subnets specified.
- In the no-prod account, Extruder, The Click, and others are non-compliant.
- This is not urgent but needs fixing; a report should be created.
- CrowdStrike is not working on ephemeral machines, including ARM, Prosumer, and GMR.
- The security group lacks permission to open port 8080 for the proxy.
- Carlo confirmed he lacks permission to fix it.
- Nilo will resolve it by either granting port 8080 access or adding it directly; this applies to GMR and Prosumer.
- For DayClick, the `declick.myengi.com` domain can be used for prod.
- NGIT configures the domain; the team needs to request it and point it to the load balancer.
- The DigiCert certificate is assumed to be the same setup as Prosumer.
- Nika and Reina are the current tech lead tandem for DayClick.
- Private keys must not be shared in Jira, repos, or email.
- Vault should be used for secure file transfer.
- Longer-term, a new process with Pierre should be proposed for handling certificates internally.

### Atlas Project Consultation

- Francois from the QRM/MAD team built a Dash app, "Atlas," fully vibe-coded via Copilot.
- The app deploys manually through PowerShell wrapping Dacli, using personal AWS credentials to push to S3.
- All infrastructure is provisioned by CDH.
- Brian's scope is consultation only, not feature ownership.
- DMS is not taking on Dash skills or deployment accountability.
- CI/CD enablement is intended to make Francois more autonomous.
- Work completed included rewriting the README, introducing `agents.md` for AI guidance, adding Git hooks, unit test scaffolding with coverage thresholds, and workflow YAML files.
- CD is unblocked: CDH support recommended an internal GitHub Runner, QRMDMS.
- Francois should create a service app in Intact for client ID and secret, stored as GitHub secrets.
- The consultation is wrapping up this week.
- DM907, a similar Dash demand, was flagged as a potential pattern worth a common solution.

### Omniland, Onset Energy, and Kiba Updates

- Omniland is automating Docker image publishing to ECR.
- An ADO pipeline, migrating to GitHub, pushes the image to ECR.
- EventBridge catches the new image event, triggers a Step Function to prepare the image for Lambda execution, and notifies the OmniRun API.
- Users have ECR-only permissions.
- Omniland auth is implementing a BFF pattern after a pentest flagged access tokens in browser storage.
- Angular calls a backend endpoint, which redirects to Okta.
- The backend handles token exchange, creates the session, and sets a cookie with the session ID.
- The Lambda authorizer handles both session cookie and machine-to-machine Okta token.
- FastAPI validates the session against the DB.
- The auth flow will be presented to the architecture committee.
- Onset Energy received internal green light; onboarding and kickoff are next week.
- Onset Energy stack: Angular, FastAPI, CDK, full serverless, agentic with DNV third-party integration.
- Onset Energy team: Alan as VPO, Bong as Scrum Master, JB as tech lead, Loreen, Raina, Joyce, and Guido in support.
- Kiba MCP should not store any data; access keys are provided by the user at runtime.
- Post-deploy, Kiba is adding auditing for traceability and rate limiting to MCP.
- The team is collaborating with Yatin Badra's AI Engineering team, SEM, on common MCP architecture.
- Alignment on roles came from Dimitri last week; periodic syncs with the AI Engineering team may be considered.

### Kubernetes Security and General Announcements

- Nilo's Synapse/cluster security audit findings include Prisma vulnerabilities that are hard to track.
- Kyverno policies and monitoring tooling are planned.
- Issues include pods running as root, missing resource requests and limits, and permissive security contexts.
- The production cluster root filesystem is already at 70% with no load.
- Proposed fixes include read-only root filesystem, PVC usage, ephemeral directory size cap around 500 MB, and image labels for build info, department, and support group traceability.
- The goal is to block images from public registries and enforce that through GitHub pipeline blueprints.
- Synapse production test with traders is planned for mid-October.
- AI token tiers were updated to five tiers, including 500, 2,500, and 5,000; billing is per actual consumption, not per tier cap.
- The architecture committee validates security design and best practices, not just alert hygiene.
- The tech leads roles and responsibilities page was published on Confluence.
- A new Sentry server was set up; alerting configuration is in progress before rollout.
- IT requests should use the dedicated IT request channel by tagging IT admin, not DMS One chat.
- The next roundtable is in two weeks.

## Next Steps

- Resolve CrowdStrike port 8080 access for GMR and Prosumer. Owner: Nilo. Grant access or add the port directly; check the chat thread first.
- Request `declick.myengi.com` domain from NGIT. Point it to the prod load balancer with a DigiCert certificate, same setup as Prosumer.
- Wrap up Atlas CI/CD consultation. Owner: Brian. Francois should create the Intact service app for GitHub secrets; project closes this week.
- Present BFF auth flow to the architecture committee. Omniland session-based auth will replace browser token storage.
- Publish Kubernetes security and governance PowerPoint. Owner: Nilo. Cover security context, Kyverno policies, image labels, and cluster node sizing.
