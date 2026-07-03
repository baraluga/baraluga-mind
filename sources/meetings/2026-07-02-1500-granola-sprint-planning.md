# Sprint Planning

Source type: Granola meeting notes
Meeting ID: `ab82f96d-5230-410d-b684-d192279c7abd`
Date: 2026-07-02 15:00 GMT+8
Participants known to Granola: Brian Alexander Peralta

Note: This is from Granola notes/summaries, not a verbatim transcript.

## Discussed

- Sprint capacity was 11 story points.
- Allocation: Brian at 100%, one team member at 50%, Joyce at 0%.
- Tickets pulled included SMP Japan/India resource cleanup, proxy error incident reporting, MS Teams failed email tracking, request MV pipeline with branch protection, secrets process documentation, dependency process documentation, separate Docker images for Japan and India, and TSDB push for interconnector data.
- SER-1087 cleanup remained blocked by proxy errors and unstable SAP Ingest behavior.
- Proxy errors were 403s in FMP Japan prod and FMP India prod; QA was consistently successful.
- SER-1181 should catch Graph API email failures and send SMTP fallback alerts.
- SER-1102 branch protection discussion: core devs can push directly to dev/QA; prod requires PRs for all users.
- Current tests are linting, syntax, and import checks; no unit tests yet because of dependency issues.
- Coverage enforcement and Ruff-based static secret detection were discussed.
- Separate Docker images for Japan and India were added to the sprint as future-proofing.
- TSDB interconnector work can start once Francois provides time series IDs.
- Walnut runner/GEMS Artifactory access remains blocked by certificate trust issues.
- Grafana dashboard backup is desirable but blocked because the API is inside VPN.
- Skipped or deferred items included Y-axis adaptation, user roles management, agentic PR validation, India user access/training, autoscript, and Grafana backup.

## Next Steps

- Brian to write the GEMS service desk report for the proxy incident.
- Brian to investigate Ruff rules for hardcoded secret detection.
- Francois to schedule a technical meeting on user roles and permissions.
- Brian to confirm the Japan team's Y-axis requirement.
- Francois to provide TSDB time series IDs.
- Follow up with Nilo on Walnut runner certificate trust for GEMS Artifactory.

Last Updated: 2026-07-04
