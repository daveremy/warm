---
log_id: "2026-11-11-1705-59-warm-against-fourteen-published-reference-models-d"
title: "WARM against published models, round 2: synthesis and amendments to v0.12"
date: 2026-11-11
author: sagan
tags: [research, warm, agents]
---

# Round 2: eight more published models, and the amendments to v0.12

2026-11-11, sagan. The documented search (`search.md`) found 48 sources the first round had not seen. The eight most complete were mapped in a second round: `mapping-round2-charters.md` (Charterion v2.0, AEON, CEAD, Salesforce's "The Agentic Enterprise") and `mapping-round2-platforms.md` (AOS-0001 with AOS-0000, Steinder and Franke, the ASOC manifesto, EAAF). With round 1 that makes fourteen published models compared with WARM. Every amendment below is my recommendation and is reversible; The author has not picked them.

## Search flow (from `search.md`)
1,634 records screened; 1,314 after de-duplication; 258 passed title screening; 61 included; 13 already known; 48 new. Could not open: a Cloud Security Alliance ten-layer reference architecture (behind a form) and three others.

## Counts, round 2
| Source | Items | Clean | Strained | Spans | Guidance | Already planned | Misfits |
|---|---|---|---|---|---|---|---|
| Charterion v2.0 (read in part: about 110 of 290 pages) | 112 | 9 | 33 | 24 | 6 | 12 | 28 |
| AEON | 58 | 13 | 16 | 15 | 5 | 6 | 3 |
| CEAD | 47 | 6 | 11 | 7 | 20 | 2 | 1 |
| Salesforce | 114 | 25 | 30 | 15 | 19 | 3 | 22 |
| AOS-0001 and AOS-0000 | 69 | 10 | 5 | 22 | 24 | 3 | 5 |
| Steinder and Franke | 37 | 14 | 0 | 15 | 6 | 0 | 2 |
| ASOC manifesto | 60 | 13 | 12 | 12 | 9 | 4 | 10 |
| EAAF | 43 | 10 | 4 | 13 | 11 | 0 | 5 |

## Round-2 predictions scored (`predictions.md`, S1 to S5)
| # | Prediction | Result |
|---|---|---|
| S1 | Charterion's charter and AEON's subdomain each bound one agent or one capability | HALF RIGHT: Charterion's charter binds one agent. AEON's nine subdomains exist apart from agents; they are IT functions with contracts, without roles, workflow or acceptance criteria |
| S2 | None of the eight has a directory of which area of work is accountable for what | CONFIRMED, narrowly: AEON's capability registry records the subdomain that provides each capability, and agents discover each other through it. It records a provider, not who is accountable |
| S3 | AOS's persistent identity versus transient instance matches WARM's agent versus definition, not persistent versus task | PARTLY: it is a third distinction, identity versus running instance, and WARM had no word for the instance |
| S4 | CEAD is the closest precedent for "a domain defines roles, agents fill them" | PARTLY: "Define the business capability and owner before defining the agent role or prompt", recorded inside one agent's contract |
| S5 | At most 3 further changes; cost becomes a named concern | WRONG: 11 further changes; cost was already a concern and stays one |

## What round 2 does to WARM's claims (this replaces "What no source has" in `synthesis.md`)
| Claim | Verdict | Deciding evidence |
|---|---|---|
| No published model treats an agent as an identified actor distinct from its definition | REFUTED. Withdraw it | Charterion (Def. 2.1): an agent is "a non-human principal" with an identity that "may be instantiated many times"; it credits the idea to the Cloud Security Alliance, NIST and OWASP since 2025. AOS separates "a persistent agent identity" from "a transient runtime instance". What differs: Charterion's identity belongs to a type of agent, WARM's to each agent. Steinder and Franke take the opposite view: identity is "a function of" the agent's goal, model and skills |
| No published model has a directory of which domain is accountable for what | STANDS, NARROWED. Cite AEON | AEON's capability registry (its section 11.1) records the providing subdomain and the principals allowed to invoke a capability. Charterion's Charter Register and Staffing Table let one compute which agent covers a step and which person answers for the agent. Neither records one accountable area of work per responsibility as a lookup for handing work over. EAAF has agents negotiate responsibilities, the opposite of a directory set by people |
| No published model has a domain as a charter separate from its agents | STANDS AS WORDED ONLY. "No model separates an area of work from its agents" would be false | AEON's subdomains and Charterion's business scopes are areas of work apart from agents. Neither has roles that several agents and people fill, a workflow and acceptance criteria. AWS writes a charter per agent. CEAD defines the capability and owner before the agent |
| No published model distinguishes persistent agents from task agents | STANDS, NARROWED | Charterion has types and short-lived instances. Salesforce has only per-task agents ("instantiated for specific tasks ... decommissioned afterwards"). EAAF's "Task Agents" is a type of job, not a lifetime. Zhu rejects long-lived agents |
| WARM's six groups are cut in a reasonable place | STANDS | Three sources split deciding from executing, a different axis. ASOC's two cross-cutting planes match WARM's two cross-cutting groups. Yu et al.'s ten responsibilities line up with WARM's parts |
| The service list is complete enough | ONE RESPONSIBILITY WAS MISSING | Nothing in WARM owned which agents exist (amendment A1) |

## Amendments to v0.12 (specification)
| # | Amendment | Sources | Confidence |
|---|---|---|---|
| A1 | **A 25th service, Lifecycle, in Runtime.** Responsibility: "Create, suspend, resume and end agents, and keep the list of which agents exist." Industry terms: agent lifecycle, provisioning, decommissioning, orphaned agents, sprawl. It is the first Runtime service that concerns an agent as a whole; Tasks concerns a unit of work. It takes the "suspend an actor" half of V3 at run time (Identity still revokes the identity). An agent that nobody owns or lists (an orphan) is its failure case. In the reference implementation this is the launcher that starts, stops and lists the persistent agents, and the board that lists running task agents. The platform now has 25 services: Runtime 6, Knowledge 3, Capabilities 3, Interaction 4, Governance 4, Operations 5. Runtime row order: Harness, Sessions, Tasks, Environments, Scheduling, Lifecycle | AOS, Steinder and Franke, EAAF, OpenClaw (agent provisioning was a misfit in the platform mapping), AAGMM (sprawl), and run-time suspension in Microsoft, AWS and Google | High that the gap is real; my call that it is a service and not a widening of Identity and Tasks. THE AUTHOR DECIDES |
| A2 | **Withdraw and narrow the claims** as in the table above, wherever the model or deck says what no published model has | Charterion, AEON, AOS | High |
| A3 | **The running instance is named.** Step 0: an agent is the identity; a running instance of it can be restarted or moved, and it is not the agent. Credit: Charterion, AOS, and security guidance since 2025 for agents as identified principals | AOS, Charterion | High |
| A4 | **An accountable person.** Identity: every agent identity traces to a person who is accountable for it. Step 0 and the Identity row | Charterion, CEAD | High |
| A5 | **Three kinds of human decision.** New short passage near Approvals (Step 2 or Step 3): (1) steps reserved for people, which an agent may not carry out at all (a domain rule; the Finance example's "the person places every order himself" is one); (2) actions held until a person approves them (Approvals); (3) the granting of authority itself, which only a person gives. WARM's Approvals covers the second | Charterion (strongest), AEON, CEAD | High that the gap is real |
| A6 | **Delegation only narrows.** Add to V1: a grant passed to another agent can only be narrower in scope, time and budget than the one it came from. Add to V2: agents started by the same agent do not count as independent of each other for separation of duties | Narrowing: AOS, ASOC. Independence: Charterion, AEON | High |
| A7 | **Evaluation before and during an action.** Evaluation row: assess behavior and work products against stated criteria, before, during or after an action. Policy may use an assessment, such as a risk score, as an input to its decision | AOS, ASOC, EAAF, Steinder and Franke | High that the gap is real; medium on placement |
| A8 | **Budgets ride in the grant.** Cost in "Concerns that are not groups": a budget is carried in a grant, enforced by Scheduling's limits and metered by Observability | AOS, Steinder and Franke | Medium |
| A9 | **Tools declare their effects.** A tool's definition in the Registry declares its side effects, whether they can be undone and whether a retry is safe. This is what lets Tasks decide whether to retry (with V14) | AOS, Steinder and Franke | Medium-high |
| A10 | **Tasks keeps the request.** The Tasks contract keeps the original request unchanged: its objective, its constraints and what counts as done | AOS, ASOC | Medium |
| A11 | **Policy decisions are more than allow and deny.** A decision may allow, deny, hold for a person, narrow the action, or be unknown | AEON, Charterion | Medium |
| A12 | **A task agent's identity.** Step 0: a task agent acts under an identity of its own, and the record says on whose behalf | Charterion, Salesforce | Medium |

Open contract questions added to the list in Step 3 (not changes to a service): who decides an approval when the named person is unavailable, and how much one person can be asked to approve; whether the configuration that runs is the one that was reviewed; precedence between rule sources.

## Recorded and not adopted, round 2
| Item | Sources | Why not |
|---|---|---|
| Artifacts has no full counterpart in any of the seven systems that could have one; Steinder and Franke argue a file system is enough | all round-2 platform models, the three platforms | The author decided on 2026-11-11 to keep Artifacts and state the gap. The gap statement is strengthened. QUESTION FOR THE AUTHOR stays open |
| Trust and reputation as a standing score of an actor; consent records; appeal of a decision; billing; responsibility across suppliers | AOS, ASOC | Systems of several organizations; WARM describes one system |
| AEON's consume / promise / guarantee form for a contract | AEON | A good template for the papers on each group |
| Autonomy levels as a vocabulary; exclusions ("must not do") on roles; accepted exceptions with an expiry; where shared context for a long workflow lives | CEAD, Charterion, Salesforce | One or two sources each, low confidence |
| Scheduling decides where work runs as well as when; "authorized" and "done" as separate records; identity that attests the current definition, model and harness | AOS, EAAF, Steinder and Franke | Low confidence |
| Planning, reflection, uncertainty estimation inside one agent | AOS, ASOC, EAAF, Steinder and Franke | Out of scope by Step 0 |

## Threats to validity, round 2
One mapper per group of four sources and no second rater. Charterion was read in part. Salesforce's page was read as text with two of its seven figures. ASOC's layer contents exist only as figure labels. Forty of the 48 new sources were not mapped. None of the fourteen models has a named adopter that the readers could find; the most-cited has 19 citations.

## Corrections after the full read of Charterion and one follow-up (2026-11-11 20:05; `charterion-full.md`)
- All four verdicts are unchanged by the remaining 180 pages.
- Charterion's agents are long-lived and keep memory between actions; it has ONE kind of agent, and anything started for a task, a subagent included, is an instance that "acts under the identity of a and holds no charter of its own" (Def. 8.9). So the difference from WARM is that WARM gives each task agent its own identity, not "type versus each agent".
- Charterion's agents cannot fill roles ("never a Business Actor, because accountability stays with humans"), and the service its agents call answers only about one named agent's own authority; it is not a lookup for handing work over.
- NEW SOURCE, read in the primary: Microsoft's Cloud Adoption Framework, "Process to build agents across your organization" (ms.date 2025-12-01, updated 2026-06-26), section "Define the agent charter": "The charter serves as the authoritative reference for what the agent system accomplishes and what it must avoid ... Include system responsibilities that map to specific business objectives, agent roles that prevent functional overlap, and prohibited actions that establish compliance guardrails." A charter for a SYSTEM of agents with responsibilities, roles and rules: the word and much of the idea of WARM's domain charter exist in a widely used vendor framework. Missing there: workflow, knowledge, tools and acceptance criteria in the charter; roles filled by people; a record across charters of who is accountable for what. The same page warns of "uncontrolled agent sprawl" and has users "view and delete their specific memory history". The claim about a domain as a charter is narrowed again in the model.
- Parts Charterion has that WARM lacks and the first mapping missed (not adopted; candidates for the contract tier): a check that the agents seen running match the list of agents that should exist; no access before an agent has an accountable person and a recorded role; memory as a path by which access leaks between agents; a regular comparison of an agent's access with what its work needs.
