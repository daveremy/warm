# WARM against three platforms: synthesis

2026-11-11, sagan. First mapping of WARM (v0.10) to systems its author did not build. Closes limit 3 of the model in part.

## Method
1. Three researchers each inventoried one platform from its own documentation without being shown WARM: `inventory-agentcore.md` (146 components), `inventory-langgraph.md` (307), `inventory-openclaw.md` (848).
2. I wrote `predictions.md` before any inventory existed.
3. Three mappers (one per platform, not shown the predictions) assigned every component to one WARM service, another layer, builder tooling, a span of several services, or a misfit; a doubtful fit was to be called a misfit; a service could be called absent only after a recorded search. Outputs: `mapping-agentcore.md`, `mapping-langgraph.md`, `mapping-openclaw.md`.

Threats to validity: the mappers knew WARM; one mapper per platform, no second rater; the evidence is documentation as of 2026-11-11, not running systems; I have read the mappers' reports, not every row of their tables; the change of plan (mappers, not me, did the assignment) was made after the inventories arrived.

## Counts
| Platform | Components | One service | Other layer | Builder tooling | Spans | Misfit | Strained fits |
|---|---|---|---|---|---|---|---|
| Amazon Bedrock AgentCore | 146 | 92 | 5 | 10 | 28 | 11 | 27 of 107 |
| LangGraph, LangSmith Deployment, LangSmith | 307 | 183 | 22 | 55 | 30 | 17 | 60 of 205 |
| OpenClaw | 848 | 329 | 212 (182 are model and media providers) | 256 | 38 | 13 | 113 of 541 |

## Predictions scored
| # | Prediction | Result |
|---|---|---|
| P1 | 90% of components map to one service or layer; at most two misfits per platform | WRONG on all three: 66%, 67%, 64% of all components (71%, 81%, 91% with builder tooling set aside); 11, 17 and 13 misfits |
| P2 | AgentCore lacks six or more services | WRONG: one absent (Scheduling). It has a registry, evaluations, policy and versioning. Six are partial |
| P3 | LangGraph lacks Human channels, Environments and most of Governance | MOSTLY WRONG: nothing absent across the vendor's products; sandboxes exist; seven services partial. The open-source library alone covers about four |
| P4 | OpenClaw lacks Evaluation, Releases, Tasks | HALF RIGHT: nothing absent; Evaluation and Tasks partial; Releases, Policy and Approvals present |
| P5 | No platform has domains with parts like WARM's, or a directory of responsibilities | CONFIRMED on all three |
| P6 | Most likely missing service: cost metering; second: a marketplace | WRONG on cost (mapped to Observability and Policy). Marketplace governance is a misfit in OpenClaw. The misfits I did not predict are below |
| P7 | The contested cut is Sessions, Memory, Artifacts | PARTLY RIGHT: the contested cut is Sessions, Tasks and Memory |
| P8 | No platform contradicts the two cross-cutting groups | PARTLY WRONG: Observability cuts across; identity and policy are rebuilt per surface (LangSmith) or apply only at choke points (AgentCore) |

My errors ran one way: the platforms cover more of WARM's list than I expected, and they have more that WARM lacks.

## Findings across platforms
| Finding | AgentCore | LangGraph | OpenClaw |
|---|---|---|---|
| A program has no place to call an agent (inbound interface) | Invoke API, streaming, session endpoints (5 misfits) | An embedding application has no place in Interaction | OpenAI-compatible endpoints, MCP Relay (4 misfits) |
| The platform runs the improvement loop | Recommendations, A/B testing, optimization | Insights, Engine, Smithtune | Self-learning, dreaming, skill workshop exist (assigned to other services; check) |
| Tasks is not a separate service with its own state | Partial: async status only | One checkpointer is both session history and run log (11 spans) | Built a shared Tasks ledger (2026-03-31), removed it 2026-09-27 as duplicate state |
| Skills are versioned definitions, not memory | Files from Git or S3; Memory has no procedural kind | Versioned repositories in the hub | Spans Memory and Registry |
| Artifacts has no real counterpart | Partial | Partial | Partial |
| Registry is a catalog; no directory of responsibilities; no domain layer | Yes | Yes | Yes (routes by where a message came from) |
| Governance is spread, not one layer | Policy only at choke points; 6 spans across Identity, Secrets, Policy | Identity and policy per product surface | 13 spans across Policy, Approvals, Identity, Environments |
| Admission and capacity control | (rate limits) | Double texting, task queue | Session controller, command queue, lanes (3 misfits) |
| Data lifecycle: retention, purging, protection of stored data | TTL, encryption (as spans) | 7 misfits | (not flagged) |
| Other misfits | Payments (4); Web Answer | Tenancy; outbound webhooks (3); caching (2); vendor licensing | Agent provisioning; standing intents; plugin host; marketplace governance (2) |

Two confirmations: OpenClaw swaps the agent loop while it "keeps ownership of channels, sessions, policy, and state", which is WARM's Harness boundary; and OpenClaw has the persistent-agent and task-agent split. AgentCore's own top-level names include Harness, Memory, Identity, Policy, Observability, Registry and Evaluations.

One independent parallel to LifeOS's history: OpenClaw moved heartbeats into ordinary scheduled jobs (2026-07-23 entries became cron jobs; 2026-08-26 schedules unified under cron, shipped in v2026.8.1 on 2026-08-31; 2026-10-21 monitors migrated to ordinary jobs). Its jobs can still run in the main session, so the separation is a per-job choice there.

## Proposed changes to WARM (for the author; none applied)
| # | Change | Evidence | Confidence |
|---|---|---|---|
| 1 | Replace the judgment test. Classify the responsibility by whether it works the same whatever the work is about; a platform service may use a model inside it | Codex review F03 (blocker); AgentCore Web Answer and Recommendations; LangSmith Engine | High |
| 2 | Add an Improvement service in Operations: turn evidence into proposed changes | AgentCore, LangSmith; LifeOS has it (Kaizen, the dream pass) | High |
| 3 | Skills are versioned definitions held by the Registry and released like other changes; Memory keeps what agents learn | Two platforms; LifeOS keeps skills as files in git | High |
| 4 | Give programs a place: widen Human channels to Channels (people and applications), or add an application interface service | All three platforms | High |
| 5 | Rethink Tasks: a contract every runtime implements (track, retry, cancel), not necessarily a service with its own ledger; state the cut as history (Sessions), run lifecycle (Tasks), learned knowledge (Memory), and say one store may serve several | All three platforms | Medium: needs the author |
| 6 | State the condition on Governance: it covers everything only if every call passes an enforcement point | Two platforms | High |
| 7 | Add a data lifecycle responsibility in Governance (retention, purging, protection of stored data) | LangGraph; WARM's own Step 0 relies on "the retention policy" | Medium |
| 8 | Add admission and capacity control to Runtime (who may run next, queues, limits) | OpenClaw, LangGraph | Medium |
| 9 | Reconsider Artifacts: no platform has a versioned store for work products | All three | Low: may be a real gap in the platforms |
| 10 | Make the directory its own service, separate from the Registry catalog | No platform has it; Registry now carries three responsibilities | The author's call |
| 11 | Say when the Domain layer matters: once a system has several areas of work under one platform. The platforms are single-purpose or leave domains to the customer | All three | High |
| - | Record without adopting: payments, tenancy, agent provisioning, marketplace governance, outbound events, caching | One platform each | - |

## Plan for the deck and the paper (the author's decision, 2026-11-11: slides and paper sections for each mapping)
- Talk: one slide, "Tested against three platforms": what fit, what did not, what changed in the model. Limit 3 becomes a result.
- Appendix: a method slide; one slide per platform (its counts, its top misfits, what it confirms).
- Paper: an evaluation section. Method (blind inventories, predictions written first, the scoring table above); one subsection per platform; findings across platforms; changes made to the model; threats to validity. The three assignment tables as supplementary files.
- Posts: one per platform.

## Still to do
- Read the three mapping files in full and spot-check at least ten assignments per platform against the inventories.
- Check whether OpenClaw's self-learning, dreaming and skill workshop are an improvement loop.
- A second rater on a sample.

## Corrections from the second rater (2026-11-11, `spot-check.md`)
- Agreement on a sample of 36 assignments (12 per platform): 29 agree, 4 disagree, 3 unclear. Clean fits 12 of 12; strained or span 7 of 12; misfit, other layer or builder tooling 10 of 12.
- OpenClaw's self-learning, Skill Workshop and dreaming ARE an improvement loop: they use evidence from past sessions and apply changes (to learned skills; to MEMORY.md), by default with no approval; an opt-in `propose` mode saves drafts for review, and each skill change saves a version first. The mapper filed all three under Memory. So "the platform runs the improvement loop" holds on all three platforms.
- Tasks ledger: the durable task registry was merged 2026-03-29 (PR #52518), not 2026-03-31 (that date is ClawFlow, later TaskFlow, #58227). Removal 2026-09-27 (#159179, "duplicated execution and completion state") confirmed.
- Heartbeats to scheduled jobs: confirmed; the range is 2026-07-22 (#112585) to 2026-10-22 (#180192); the 2026-08-26 step shipped in v2026.8.1 (2026-08-31); the October steps shipped later.
- AgentCore has no scheduling component: confirmed (AWS's own examples schedule agents with EventBridge Scheduler).
- "Still to do" items 1 to 3 above are done by this check, except that the author has still not read every row.
