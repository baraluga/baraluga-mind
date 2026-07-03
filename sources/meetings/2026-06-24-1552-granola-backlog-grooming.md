# Backlog Grooming

Source type: Granola meeting notes
Meeting ID: `70e90612-d607-4ffb-8b8f-ff61c8f089bc`
Date: 2026-06-24 15:52 GMT+8
Participants known to Granola: Brian Alexander Peralta

Note: This is from Granola notes/summaries, not a verbatim transcript.

## Discussed

- Infrastructure deployments were taking significant time while dashboards were moving quickly.
- TV setup for Carlos was completed and acknowledged as a win.
- Caution raised about accepting ad-hoc requests that cannot fit the current sprint.
- Interconnector scraper tasks were top backlog priority.
- Interconnector work needs cadence separation: daily, weekly, monthly, yearly.
- Reconciliation ticket was a placeholder; full description lives in a linked Confluence page.
- Validation approach: recover data from two weeks ago, run equivalent process, compare against IROMI's Excel output.
- Interconnector dashboard should scrape price data, actual flow, and compute regional spread across seven interconnectors.
- Carlos requested interconnector data also pushed to TSDB.
- Fred was coordinating with TSDB team to confirm TSDB insertion acceptability.
- TSDB catalog/provider creation should be owned by Japan team; dev team only needs time series IDs.
- Existing OCT time series may be reusable but needs checking.
- Docker image pipeline and Airflow deployment pipeline were compared; both are currently manual.
- Proposed order: Docker image pipeline first because new dependencies will come before environment changes.
- GEMS Artifactory remains blocked by Zscaler; SMP Tool pipeline is unaffected.
- ADO scraper repo migration ticket should be archived rather than migrated or deleted.
- Grafana dashboard backup is feasible through API plus auto-PR but blocked by VPN/Zscaler access.
- Airflow token expiry/session disconnect was deprioritized.
- AKS secret manager migration was deprioritized unless security explicitly requires it.

## Next Steps

- Implement reconciliation process per Confluence spec.
- Build interconnector dashboard with scraped price and flow data.
- Confirm TSDB catalog ownership and OCT time series reuse with Japan team.
- Confirm with Nilo whether Helm upgrade requires image digest or latest tag.
- Document user secret and Python dependency addition process.
- Archive ADO scraper repos via David Laudie's master spreadsheet.

Last Updated: 2026-07-04
