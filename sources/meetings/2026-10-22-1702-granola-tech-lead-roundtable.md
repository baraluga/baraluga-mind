# Granola Capture: Tech Lead Roundtable

Source Type: meeting
Source: Granola
Meeting Date: 2026-10-22 17:02 GMT+8
Meeting URL: https://notes.granola.ai/d/bd1e8e85-2a28-4a63-81d3-f020b24e3b4f
Granola ID: bd1e8e85-2a28-4a63-81d3-f020b24e3b4f

## Known Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Dependency Security

- Python dependencies should be updated across environments before the next image deployment: `uv` 0.13.4+ and `certify` 26.10.10 were specifically called out. Virtual environments should be regenerated where applicable, and remaining `pip` users should migrate.
- The security working rule is to use the latest patch version of each interpreter because only the latest patch carries security fixes. The PHP vulnerability discussed has no reported impact because PHP is not used.

### SDD Process and Review Controls

- Process deviations should be aligned with the wider group before work begins; ARC001 had restarted without prior alignment, creating confusion.
- Grooming should happen as a human activity before agents are involved, preferably by epic or batch rather than isolated daily micro-groomings so dependencies are visible.
- One developer should run SDD for a story at a time. Human review remains required for AI-generated work: POs review PO specifications and tech leads review architecture decisions.

### Onset Multi-Tenancy and ARC001

- Onset needs multi-tenancy for external companies: users can have different roles across client organisations, with only super-admin stored in Okta and other roles held in internal tables. An impersonation-switcher UI was proposed for choosing the active client role.
- Reina restarted ARC001 using a dependency tree to split isolated work packages among three developers. Results were timeboxed for assessment on 2026-10-23; the approach may be reusable if the parallel output proves useful.
- Continuing Phase 1 without multi-tenancy risks rework and a large breaking change when it is introduced later.

### SDD Enablement

- Alfred is blocked while converting Kiva to SDD because its tooling requires non-standard MCPs and the discovery agent forces repository creation under GitHub rather than a personal repository.
- A dedicated SDD coordination track was proposed for active projects and explorers. Prosumer's Bedrock spike is building a RAG chatbot over documents and code with GitHub tools; Alfred is to be consulted about credit consumption.

## Next Steps Captured In Granola

- Apply the Python dependency updates and regenerate virtual environments before the next image deployment.
- Establish a focused SDD coordination forum and sync with Alfred on the Kiva blocker.
- Assess the ARC001 dependency-tree branch results on 2026-10-23.

Last Updated: 2026-10-23
