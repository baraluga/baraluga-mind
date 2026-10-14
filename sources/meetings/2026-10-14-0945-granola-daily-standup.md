# Granola Capture: Daily Standup

Source Type: meeting
Source: Granola
Meeting Date: 2026-10-14 09:45 GMT+8
Meeting URL: https://notes.granola.ai/d/a6d8993b-d29e-4c24-9966-09e21ec53da7
Granola ID: a6d8993b-d29e-4c24-9966-09e21ec53da7

## Known Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### SMB DAGs Permission Fix

- Users could open DAGs and figures but list navigation failed because read permission for TL detail was missing.
- The fix was applied, values were updated, and user access was confirmed.
- Brandon created the bug ticket, which was sent to Francois for validation; the fix was deployed to QA and production.

### Darwin and HPX

- The Darwin ticket was unblocked, but image building is still blocked by the ECR-push role; Brian is awaiting Michael's go-ahead to proceed in Airflow.
- The HPX scope was realigned with Mateo's plan, including an HPD metric. The ticket was raised to two points and remains blocked.

### Other Platform Work

- Two social-connector tickets are active, including ticket 1284 at three points. The dashboard-delay approach remains undecided pending a chat decision.
- CDH tenant setup needs a data-source role approved or added to the trust policy.
- Pre-production Okta errors were fixed, while Dev 3 issues remain under investigation; missing environment variables or a fresh minigib deployment are suspected.
- Azure resources were deployed and trace work completed. A Dev 3 alert flagged a slow endpoint above 100 ms.

## Next Steps Captured In Granola

- Await Michael's approval to continue the Darwin Airflow deployment.
- Finalize the dashboard-delay approach.
- Check the CDH tenant data-source role or trust policy.
- Investigate the Dev 3 environment errors.
- Send Carmine's APE release notes to Karmina privately.

Last Updated: 2026-10-15
