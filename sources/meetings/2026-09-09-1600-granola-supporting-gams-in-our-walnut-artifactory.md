# Supporting GAMS in Our Walnut Artifactory

## Metadata

- Source: Granola
- Meeting ID: `e3be2c0f-9cc9-4b3f-84a2-d0464d56c313`
- Date: 2026-09-09 16:00 GMT+8
- Captured by: Brian Alexander Peralta
- Known participants:
  - Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Context and Background

- Team discussed GAMS mathematical software distribution and binary hosting.
- Current state: GAMS installer is hosted externally, with a move toward internal artifact management.
- Michael already aligned with Stefan and Nicole: they will manage versioning as a temporary solution until the GAMS license server is finalized.

### GAMS Installer Details

- Installer sizes: 138 MB for Windows, with a similar size for Linux.
- Pipeline downloads the installer on every run, then installs Python components from it.
- Frequency is "once in a blue moon" for one project; higher frequency is expected for Matt's team because more people are involved.
- Current workaround: some teams use SharePoint; pipeline will shift to Artifactory.

### Artifactory vs. S3 Decision

- Proposal: use a single generic Artifactory repository for all projects using GAMS.
  - Avoid per-project repos because they create too much maintenance overhead.
  - Teams like Dashitecture, needing Windows and Linux only, would use this shared repo.
- S3 is a viable fallback if Artifactory costs are prohibitive.
  - Downside: it requires a publishing mechanism for the GAMS team to upload new versions.
- File browser developed internally was mentioned as another alternative, but the preference is to keep everything in JFrog/Artifactory if cost allows.
- Current license: Enterprise X, 125 GB base consumption for storage and transfer across the whole engine team.
  - Pricing was shown as about $59.50/month, but this was flagged as likely incorrect and needing verification.

### Traffic and Cost Concerns

- Main concern is traffic, not storage: 10 builds equals about 1 GB of transfer for the 138 MB installer.
- Need to clarify with the Wallnut team whether large binary packages incur extra charges under the current plan.
- If there is no extra cost, proceed with Artifactory as planned.
- If there is extra cost, evaluate S3 or other alternatives.
- Alternative noted but deprioritized: custom build images with GAMS pre-installed, because they are too much trouble.

### Next Steps

- Create Wallnut ticket on Artifactory traffic and storage limits. Owner: Nilo.
  - Ask whether large binary packages around 138 MB, with pipeline-triggered downloads, incur extra charges; contact Pierre for help and cc the lead.
- Create a single generic Artifactory repo for GAMS and integrate it with the pipeline.
  - Proceed in parallel with the Wallnut inquiry; do not deploy to production stages yet.
- Keep the lead on copy for Wallnut replies.
  - Additional questions from Wallnut may need technical input to answer.

Last Updated: 2026-09-10
