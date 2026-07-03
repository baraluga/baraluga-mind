# Daily Standup

Source type: Granola meeting notes
Meeting ID: `f585a9f5-12bb-4979-9757-a260365f3a09`
Date: 2026-06-22 14:15 GMT+8
Participants known to Granola: Brian Alexander Peralta

Note: This is from Granola notes/summaries, not a verbatim transcript.

## Discussed

- Tickets 1114 and 1087 were blocked by India environments not being ready.
- Ticket 1114: SMP India developed on GitHub, scraper DAGs detached, confirmed in dev, not yet merged to India prod.
- Ticket 1087: DAG-to-environment sync; India still piggybacking on Japan.
- OIDC creation for GitHub/AWS connection was blocked, with Alfred helping.
- Airflow Git sync and Grafana dashboard tickets were blocked pending India prod environment.
- ADO-to-Walmart pipeline migration needed an equivalent pipeline setup.
- India dev and QA Airflow login were working; Joyce endorsed setup to Michael.
- RDS credentials for dev were needed from Milo; new DB should be created and old one deleted.
- Joyce was updating IAM role stack for production, following Japan prod's Airflow/Grafana role pattern.
- EFS stack did not exist; prod needs an EFS volume.
- Need to confirm whether SMP prod database is a cluster or separate database.
- CDH dataset disassociation incident was caused by Japan dataset registration script disassociating India datasets.
- India datasets appeared orphaned in CDH UI because SMP India prod still pointed to the Japan SMP project.
- Fix: reintroduce datasets to Japan prod config, then migrate to India project long-term.
- Francois flagged need for incident management training before next prod issue.
- MS Teams email still got 403 even after switching to NPRM68 mailbox.
- Walmart node pipeline contact misunderstood the requirement and was setting up something different.
- Copilot DAG agent template uses four fields and creates PR plus README handover.
- Two Confluence pages were created for capacity work: high-level design and data freshness strategy.
- Capacity work for Octo was nearly complete pending Ushu-san go-signal.

## Next Steps

- Milo to send RDS credentials and set up new dev database.
- Contact Pierre about MS Teams email permissions.
- Brian to write Copilot DAG agent summary for Francois.
- Francois to test Copilot agent on Japan repo.
- Francois to share steering committee minutes with team.

Last Updated: 2026-07-04
