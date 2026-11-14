# Platform mapping: predictions, written before any inventory was read

Written 2026-11-11 13:55 MST by sagan, before the three inventories exist. Purpose: WARM's limit 3 says it has not been mapped to another agent platform. This is the first such mapping. The inventories are made by researchers who are not shown WARM; I map them afterwards.

Platforms: Amazon Bedrock AgentCore (managed cloud), LangGraph with its hosted platform and LangSmith (framework), OpenClaw (personal agent platform; The author tried it before LifeOS and LifeOS grew from its goals).

## What would count against WARM
- **Missing service:** a platform component that fits no WARM service and is not Infrastructure or a Provider.
- **Wrong cut:** a component that all three platforms treat as one thing and WARM splits across two or more services, or the reverse.
- **Empty service:** a WARM service that none of the three platforms has and that only LifeOS has (it may be an accident of one system).
- **Group that does not hold:** a platform whose own grouping cuts across WARM's six groups in a consistent way.

## Predictions
- P1. At least 90% of the components in each inventory map to one WARM service or to the Infrastructure or Providers layer. I expect no more than two misfits per platform.
- P2. AgentCore has clear counterparts for Sessions or Environments (its runtime), Memory, Identity, Tools (its gateway), Observability and Environments (browser and code execution). I expect it to lack six or more of the 22: Approvals, Human channels, Messaging, Scheduling, Registry, Releases, Evaluation are my candidates.
- P3. LangGraph has counterparts for Harness (the graph loop), Sessions (threads and checkpoints), Memory (its store), Orchestration, Tasks (runs), Scheduling (cron), Approvals (interrupts), Observability and Evaluation (LangSmith), Releases (deployments). I expect it to lack Human channels, Environments and most of Governance except Approvals.
- P4. OpenClaw has counterparts for Human channels (its messaging gateway), Scheduling (heartbeats and cron), Sessions, Memory (files), Registry (skills), Tools, Harness and Messaging between agents. I expect it to lack Evaluation, Releases and Tasks, with Policy and Approvals partial.
- P5. None of the three has a domain concept with parts like WARM's seven, or a directory of responsibilities. OpenClaw comes closest (agents with their own workspace and persona).
- P6. The most likely missing service in WARM is cost or usage metering (budgets and quotas). The second is distribution of skills or agents between systems (a marketplace).
- P7. The most likely wrong cut is Sessions versus Memory versus Artifacts: platforms may treat "state" as one thing.
- P8. No platform contradicts the two cross-cutting groups: each treats identity, policy and observability as applying across the rest.

## After the inventories
For every WARM service with no match I run a targeted search of that platform's documentation before writing "absent", and I name the search.
