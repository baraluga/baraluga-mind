# Application Team Meeting

Source type: Granola meeting notes
Meeting ID: `16a02c37-5832-4213-8a46-f11a57c97f01`
Meeting date/time: 2026-08-04 17:00 GMT+8
Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This capture preserves available Granola notes and summaries. It is not a verbatim transcript.

## Discussion Notes / Summary

### AI Corner: GitHub Copilot DAG Onboarding Agent (Brian)

- Built a custom Copilot agent to streamline DAG contributor onboarding for SMP India and SMP Japan.
- Two-step workflow:
  - Contributor creates a GitHub issue using a DAG creation template (inputs: DAG name + cron schedule).
  - Issue assigned to Copilot, which scaffolds the DAG and opens a PR for human review.
- Agent is grounded in the current codebase, so it self-adapts as standards evolve.
- Avoids maintaining Confluence pages for code minutiae; Confluence reserved for spikes and architectural decisions.
- Tested with two humans: François (PO) and Mateo (candidate contributor for SMP India).
- Cost: ~50-70 Copilot credits per full flow, depending on model used.
- Model quality affects output; no way yet to fix which model the agent uses.
- Agents stored in the `.github` org-level repository, making them visible across all Copilot sessions in the organization.

### Walnut Migration Update (Michael)

- All SFF/common component cities migrated to Walnut GitHub.
- Artifactory access now available, but currently supports Python packages only.
  - Teams needing binary or other package types should flag this.
- SFF composite pipelines and artifacts migration complete.
- Project-specific repository migrations in progress; tech leads should coordinate with POs.
- Personal access tokens still in use; functional user setup still pending.
  - Workaround: link a functional user to an existing project (e.g., Consumer) in ServiceNow.
  - Nikki flagged a GitHub service account token option as a potential alternative.
  - Dedicated meeting proposed to align on the best authentication approach.

### Spec-Driven Development Pilot: Omniron (Yanik / JB)

- Goal: build a full application from scratch using an AI agent workflow, without writing code manually.
- Architecture: orchestrator + six specialized agents (PO, architect, tech lead, front end, back end, sub-agents).
  - Agents feed from shared markdown standards in the `.github` org repository.
  - Standards are updated first when gaps are found; agents then re-apply the new version.
- Progress: orchestration ran end-to-end; web app ready for deployment; next step is AWS deploy and compliance review.
- Key learnings so far:
  - Large markdown files consumed excessive tokens; split into smaller thematic files to reduce cost.
  - Bad inter-agent communication caused looping iterations and high token burn.
  - Added safeguards (shell command checks) to prevent agents falsely reporting completion.
- Current token cost: ~5,000 tokens per scoped run; one recent run consumed the full standard license allocation.
- Do not adopt SDD or these agents in other projects yet; fine-tuning still in progress.
- Next step: dedicated workshop during a chapter/knowledge-sharing session for the full team.

### Demand and Project Pipeline Overview

- Upcoming: Onset Energy (Alan/JB), SDB metadata, Delphi extension (awaiting stakeholders back from vacation).
- Kicking off: Kiva industrialization (kick-off tomorrow, 5th August).
- In development: ABS Index Builder App (Joyous and Hook).
- Near completion: WOW (close to production release), Best-of Sign-ups (Jaka onboarded).
- Ongoing support/monitoring: AWS migration, Walnut and Centiment migration, Pyrene, Storm.
- Focus this period: AWS migration and Walnut/Centiment migration.
- Recruitment: still searching for a Senior Software Engineer in the Philippines; multiple technical interviews underway.

### Team Updates and Announcements

- QRM 1st anniversary recap: "Slice of Success" celebration held 10th July at Ortigas office.
  - Cupcake decorating activity; teams grouped by flavor/decoration theme.
- Upcoming workshop: requirement solicitation and stakeholder management, 28th August (Friday).
- Promethe/Tempo transition: final parallel run throughout August; fill in Promethe every Friday.
  - Tempo decommissioned end of August.
- Anniversaries: Hook (4 years), Pierre (13 years).
- August birthdays: Joyce (16th), Nico (27th).
- New team member: Rudy (Pierre), based in French-speaking Belgium near Tournai.
  - Background: data engineer/architect; previously at BNP Asset Management and ING.
  - Experience: Spark pipelines, event-driven ingestion, Kafka, Kubernetes, private/hybrid cloud, AWS, IBM Cloud.
- Career Explorer reminder: update Sezane skills profile and career trajectory; Bong conducting development and learning reviews.

## Next Steps / Action Items From Granola

- No separate next steps/action-items section was provided by Granola beyond the summary bullets above.

Last Updated: 2026-08-04
