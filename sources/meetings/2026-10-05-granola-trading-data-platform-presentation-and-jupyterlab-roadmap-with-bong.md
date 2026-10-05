# Granola Capture: Trading Data Platform Presentation and JupyterLab Roadmap with Bong

Source Type: meeting
Source: Granola
Meeting Date: 2026-10-05 14:32 GMT+8
Meeting URL: https://notes.granola.ai/d/12d16a56-bedc-4e0f-8450-3a155038c34a
Granola ID: 12d16a56-bedc-4e0f-8450-3a155038c34a

## Known Participants

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

## Summary

### Presentation Overview and Structure

- 6-slide deck, targeting 30 minutes including Q&A.
- Slide 1: initial need, trading desks gathering data from multiple sources.
  - Current approach: bundle of scripts, no monitoring, no convenient data sharing.
  - Proposed solution: aligned with NG data ecosystem, using TSDB and Common Data Hub, Airflow and Grafana.
- Slide 2: team intro.
  - QRM developers, APAC flexibility.
  - Local leadership: Brian's title TBD, leaning toward "local team leader" over Scrum Master.
  - Product owner in Belgium.
  - Agile methodology: 2-week sprints, requests ideally pushed before next sprint, large demands synced with steering committee.
- Slide 3: India perimeter work delivered via the platform.
  - Volume bits at regional level.
  - Bilateral contracts, KABA and KAFDA site generation: 5-minute schedule, 1-minute granularity.
  - All flowing through TSDB.

### Grafana Demo Plan

- Show 1-2 dashboards in depth rather than a full inventory.
  - Enumerate all available graphs briefly, 1 through 10.
  - Deep-dive on top 3, covering different graph types.
  - Suggested: Bitstack stacked area, bilaterality concept, KABA/KAFDA.
- Demo from prod environment, not QA.
- Mixed audience: Lou Buisson, new VA; historical users familiar with dashboards; new head of India Power, who may need orientation.
- Alert feature: mention email alert capability and MS Teams chat integration, currently under testing.

### Technical Architecture Slide

- Airflow -> TSDB -> Orchid Edge -> Airflow -> CDH -> Grafana.
- Purpose: give stakeholders a clear picture of the data pipeline.

### JupyterLab Integration: Next Period

- Main focus for end of October through end of November or early December.
- Goal: integrate Synapse's JupyterLab work, adding QA and production environments.
- Expected impact: Matteo, Adrien, and Lou will find it easier to create new DAGs independently.
  - Service component, such as scrapers, expected to shrink over time as users get familiar.
  - Service component will not disappear entirely, as Matteo and Adrien are time-constrained.
- Brian has not seen JupyterLab in action yet and needs a demo before the period begins.
  - Demo to include Brian and Michael, likely presented by Eric.
- Integration timeline: estimated 2 sprints, more predictable than ad-hoc scraper work.
- Workload tradeoff to communicate to stakeholders: either accept slower delivery on regular tasks, or increase team size pending availability.
  - To discuss with Bong and Fred.

### Upcoming Milestones

- Steering committee coming up: stakeholders should submit major requests in advance.
- Adrien sync immediately after this meeting: raise ticket 1274, TSDB ID creation, and review ticket 1275, bid contract dashboard for validation.
- Slides to be shared with Brian after the Adrien sync for final review.

## Next Steps Captured In Granola

- Organize JupyterLab demo with Michael and Eric: Brian needs to see it in action before the integration period starts to assess scope and split the work.
- Prepare Grafana alert demo for tomorrow's presentation: show email alert and mention MS Teams chat integration under testing.
- Discuss next-period workload and team capacity with Bong and Fred: align on bandwidth split between JupyterLab integration and regular delivery to Matteo and Adrien.

Last Updated: 2026-10-06
