# Supporting GAMS Installer Thing

## Metadata

- Source: Granola
- Meeting ID: `e2ec2677-0123-45a2-9545-e56e1760f61d`
- Date: 2026-09-08 15:15 GMT+8
- Captured by: Brian Alexander Peralta
- Known participants:
  - Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### GAMS Installer Background

- GAMS installer previously downloaded directly from S3 (public bucket), then copied into Docker image.
- GAMS has multiple components: C binaries (architecture-specific) and Python components.
- Windows and Linux versions differ; Mac support is unclear (Apple M-series package exists).
- Previously, all versions were stored in a personal image; some projects also stored installer in Artifactory.

### Current Problem: S3 Access Closed

- Joyce shared the original S3 download URL/script, but it now returns a 403.
- GAMS appears to have moved distribution behind CloudFront, removing direct S3 access.
  - Likely to prevent abuse of public bucket (cheaper via CloudFront).
- GitHub pipelines currently skip GAMS-dependent steps and are set to block.
- Azure pipelines still work; they have not migrated yet because of other priorities: security fixes and FE.

### Artifactory as a Solution: Concerns

- Michael found the GAMS executable already stored in Artifactory.
  - Concern: GAMS is a third-party commercial binary, not a Python component.
  - Storing it internally may raise licensing/distribution issues; the license is a secret text file and cannot be committed.
- Adding GAMS to Artifactory creates ongoing maintenance burden.
  - Version updates frequently, for example weekly; someone must publish each new version.
  - Would require a pipeline task capable of downloading executables from Artifactory.
  - No equivalent download task exists in GitHub pipelines yet.
- Preferred approach: avoid hosting GAMS internally if a public or official source is available.

### Options on the Table

- Option A: Download directly from GAMS S3/CloudFront, preferred if access can be restored.
- Option B: Create a dedicated S3 bucket to host GAMS installers internally.
  - Simpler than Artifactory for mathematicians downloading locally.
  - Mathematicians would manage it, similar to how they manage the math feed.
- Option C: Add a generic repository in JFrog Artifactory for executables.
  - JFrog supports generic repositories for binaries.
  - Adds product lifecycle management overhead to pipelines.

### Next Steps

- Reach out to Stefan Kaminski. Owner: Brian.
  - Understand why GAMS was added to Artifactory and whether direct S3 download is still viable or if an alternative exists.
- Contact GAMS technical support. Owner: Brian.
  - Explain the pipeline use case: direct S3 download no longer works. Ask for an official alternative. Jose can provide a contact via the license center.

Last Updated: 2026-09-09
