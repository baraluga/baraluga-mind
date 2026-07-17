# Technical Activities

Source type: Granola meeting notes
Meeting ID: `75b233e6-2950-4e1b-87b7-71cf21fdf657`
Meeting date/time: Jul 17, 2026 4:00 PM GMT+8
Known participants:

- Brian Alexander Peralta (note creator) from Icloud <ba.peralta@icloud.com>

Note: This is not a verbatim transcript. It preserves the available Granola-generated meeting notes and summary.

## Discussion Notes / Summary

### Team Standup Updates

- Grafana redeployment in progress, including service account setup.
- TA-91 (Grafana/Loki deployment in signups cluster) blocked:
  - IP address must be registered before DNS record and certificate can be requested.
  - Consulting with Milo on the correct procedure.
- Prosumer simulations stuck and unrunnable; migration fully blocked.
- Meteomatics client migration pipeline created; not yet revisited.
- Meeting with Abstract held; ADO-to-new-repo migration list from Bong to be worked on this afternoon.
- SNS publisher role created (Nil helped with permissions yesterday).
  - Role attached to Grafana service account, but STSS/web identity error persists.
  - Jeka messaged for namespace access; demo later today means SNS ticket won't close today.
- Brian: reviewing Joyce's PR on the SFF idiomatics client repo.

### Prosumer Simulation Blockage

- Prosumer simulations cannot run due to saturated shared infrastructure capacity.
- Issue is not a prosumer application failure; it's a shared AWS infrastructure problem.
- Alarm strategy discussion: Joyce raised restoring prosumer-specific alarms.
  - Broader suggestion: implement account-level global alarms, since the root cause is shared capacity.

### AWS Cost and CrowdStrike Incident

- Security team flagged 1,200+ EC2 instances in the AWS account without CrowdStrike agent.
  - Instances are M3 medium (GMR); running since July 11th, roughly one week.
  - Instances are reserved/running even when not in use.
- Root cause: compute environment minimum CPU set to 1,200, causing AWS Batch to provision that many CPUs continuously.
  - Kubernetes "1600" = 1.6 CPUs; AWS "1600" = 1,600 physical processors; easy to misconfigure.
  - All GMR environments have maximum vCPUs set to 1,600 (likely a default); Prosumer is set to 512.
- Immediate action taken: minimum CPU reduced to zero during the meeting.
  - Desired capacity was at 1,600 before the fix.
- Fix expected to also resolve the prosumer compute capacity issue.

## Next Steps / Action Items Present in Granola

- Verify CrowdStrike agent coverage on GMR compute instances.
  - Instances were provisioned from ngloud images following the CrowdStrike AMI guide, but agent is still missing; needs investigation.
- Review and reduce maximum vCPU limits across all compute environments.
  - All GMR environments are at 1,600 max vCPUs; teams should apply discretion and set appropriate limits to avoid runaway costs.
- Submit AWS support request for VPC CPU limit increase.
  - Current CPU limits may block future scaling; a support request is needed before hitting the ceiling again.

Last Updated: 2026-07-17
