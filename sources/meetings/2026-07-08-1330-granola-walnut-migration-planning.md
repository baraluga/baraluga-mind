# Walnut Migration Planning

Source type: Granola meeting notes

Meeting ID: `2e22ac15-b1df-470f-a869-2a953bfd23dd`

Meeting date/time: 2026-07-08 13:30 GMT+8

Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This is not a verbatim transcript. It preserves the available Granola meeting notes/summaries.

## Discussion Notes / Summary

### Migration Strategy: ADO to GitHub

- Two migration paths identified:
- From ADO directly.
- From non-GitHub sources.
- Migration steps:
- Migrate repo in read-only mode first.
- Recreate pipelines in GitHub.
- Add users after pipeline is stable.
- Turn off ADO access after a few days.
- History preserved on migration: branches, commits, pull requests.
- GitHub CLI import method requires ADO source URL, VPN, username, and ADO personal access token (PAT).
- Transfer via "Danger Zone" UI also possible, but riskier because it requires admin/elevated access.

### Team Structure and Ownership

- Hook and Michael handle the migration.
- Alexander, the CI/CD expert, defines governance pipeline and master branch protection settings.
- Brian: support, automation, and governance oversight.
- Michael: execution lead.
- Ownership structure to be set up per owner/product by Monday.

### Pipelines and Artifacts

- Most migration effort is in pipeline recreation, not repo transfer.
- Simple pipelines, such as prosumer, are straightforward; complex ones need more work.
- Artifact strategy:
- SFF items need a dedicated repo per component for common artifacts.
- SMP common repo to serve as shared artifact source.
- ADO artifacts still in use until migration completes; cannot publish to ADO after cutover.
- Artifactory status: TBD, NA, or ongoing.
- NPM proxy repo in Artifactory identified for package publishing.
- APM library: published to Artifactory, installed via `pip install` from ADO for now.
- Dependencies currently from different sources; consolidation pending.

### Governance and Repo Settings

- Repo visibility defaults:
- Projects: private by default.
- SFF and common repos: tagged as internal.
- SMP common: not internal.
- Secrets management for prod pipelines flagged as a concern, especially SMP secrets.
- ERN/scraper pipeline: focus area, needs general pipeline setup.
- Ticket tracking via Tempo for migration tasks; major ticket to be assigned to Michael.

## Next Steps / Action Items From Granola

- Set up GitHub repo structure and migrate first repo (Michael). Start with read-only migration; pipeline recreation follows after repo is live.
- Define governance pipeline and branch protection rules (Alexander). Cover master branch protection and CI/CD governance settings for GitHub.
- Confirm Artifactory status and artifact publishing plan. Determine if Artifactory is active or still pending; unblocks post-migration artifact publishing.
- Set up per-owner project structure by Monday. Ownership mapped per product/owner; Brian focused on support, automation, and governance.

Last Updated: 2026-07-09
