# Francois Help

Source type: Granola meeting notes
Meeting ID: `11c00bd4-5003-49ca-9ea7-5e293b168ce6`
Date: 2026-07-07 15:30 GMT+8
Participants known to Granola: Brian Alexander Peralta

Note: This is from Granola notes/summaries, not a verbatim transcript.

## Discussed

### Context and Introductions

- Francois Caffon was shown a demo of Granola and Airflow.
- Francois expressed interest in both.
- A follow-up session may be needed to answer his questions.

### GitHub Copilot for PR Fixes

- A contributor had a failing pipeline check caused by unsorted imports and no local testing.
- Copilot can fix pipeline errors directly in GitHub without checking out the repo.
- This makes PR fixing more accessible to non-Python contributors.
- Copilot commits the fix to the existing PR automatically.
- Token usage is unclear: likely org budget, not personal tokens, but should be confirmed with IT/Irun.

### Local Environment Setup

- SMP India README installation steps were walked through.
- Key finding: GEMS Artifactory credentials are no longer needed; README was outdated.
- Only required credentials: SMP Common via Walnut Artifactory.
- Username field should use the account name, not a personal/nephew name; incorrect value caused a 401.
- Brian updated the README during the call to remove obsolete GEMS Artifactory credential steps for Japan and India repos.

### Pipeline Tests and Contributor Workflow

- Tests are currently skipped in pipeline because of Zscaler proxy dependency for GEMS and Walnut Artifactory auth.
- Pipeline tests remain blocked until the GitHub migration team / Ilo sorts out the Walnut runner.
- Once unblocked, re-enabling tests should be a config change.
- Workaround: reviewers run tests locally before approving merges.
- PRs require at least one code reviewer; contributors cannot self-approve.
- Preference: keep PR review in the loop initially to catch poorly written or suboptimal DAGs.
- Tests still need to be written; current PR had none.

### Grafana Dashboard Setup

- Contributor lacks edit rights in dev but has rights in QA.
- Full flow to add a dashboard:
  - Register dataset and schema in CDH, through UI or code.
  - Assign dataset to the CDH project for dev/QA/prod.
  - Add the data source to the CDH project in Grafana.
  - Dashboard should then be visible and editable.
- SMP Dashboard repo README has the full guide.
- Carlos precedent: Carlos handled CDH setup himself; Brian only added the data source to the CDH project.

## Next Steps

- Update PR rules to prevent self-merge by contributors.
- Complete Grafana dashboard end-to-end as a solo exercise.
- Use the solo Grafana exercise to demonstrate self-service capability to Material and Adrian, then replicate with Carlos.
- Confirm Copilot token billing model with Irun.

Last Updated: 2026-07-08
