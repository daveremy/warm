---
title: "WARM against published reference models: synthesis and the v0.12 change list"
date: 2026-11-11
author: sagan
tags: [research, warm, agents]
---

# WARM against published reference models: synthesis

2026-11-11, sagan. The author asked whether a more systematic review could affect the model, and asked for one if so. It does. This file is the synthesis of three mappings and the specification for WARM v0.12. Every change below is my recommendation and is reversible; The author has not picked them.

## Method
1. Predictions written first: `predictions.md` (R1 to R8).
2. Three mappers (not shown the predictions) each read the full primary text of their sources, listed every named component with a verbatim definition, and assigned each to one WARM v0.11 part, a span, design-time guidance or a misfit. A doubtful fit was to be called a misfit. Outputs: `mapping-yu-zhu.md`, `mapping-aam5c.md`, `mapping-vendors.md`.
3. A fourth reader ran a documented search with a written protocol: `search.md` (its count and any further sources are added when it finishes).

Sources mapped: Yu, Rabhi, Zhu and Lu (arXiv:2610.14818); Zhu (arXiv:2608.08516); Goujon, AAM/5C (arXiv:2610.30221, all 120 pages); Microsoft's Multi-Agent Reference Architecture; AWS Prescriptive Guidance on agentic AI (six guides); Google Cloud's agentic AI architecture pages.

Threats: one mapper per source and no second rater; the mappers knew WARM; two vendor inventories were extracted by sub-readers and spot-checked (22 quotes, all matched); some AWS and Google pages were not read (listed in `mapping-vendors.md`); figures that are images were read by caption only.

## Counts
| Source | Items | Clean fit | Strained | Spans | Guidance | Misfits |
|---|---|---|---|---|---|---|
| Yu et al. | 97 | 33 | 8 | 42 | 9 | 5 |
| Zhu | 78 | 13 | 15 | 37 | 9 | 4 |
| Goujon, AAM/5C | 153 | 20 | 45 | 36 | 34 | 18 |
| Microsoft | 153 | 48 | 17 | 36 | 47 | 5 |
| AWS, reference-architecture guide | 87 | 24 | 18 | 30 | 15 | 0 |
| AWS, all six guides | 385 | 73 | 46 | 72 | 149 | 45 (40 are single-agent reasoning, out of WARM's scope) |
| Google Cloud | 144 | 56 | 25 | 32 | 26 | 5 |

The counts do not compare across sources: the granularity differs, and groupings and interactions span by their nature.

## Predictions scored
| # | Prediction | Result |
|---|---|---|
| R1 | 80% of each source's components map to one WARM part | WRONG on all six: 36% to 56% (clean plus strained). Reference models are made of groupings and interactions, which span |
| R2 | No source has a directory of which area of work is accountable for what | CONFIRMED on all six |
| R3 | No source gives an area of work a charter with its own workflow and acceptance criteria | CONFIRMED, with one near case: AWS writes the same parts as a charter for each agent ("intent and scope") |
| R4 | Misfits concentrate in events, the client layer and business design | PARTLY: events and calling applications, yes. The larger group of misfits was in governance mechanics, which I did not predict |
| R5 | Two sources have a part WARM lacks; guesses: context management, guardrails, cost, oversight roles | PARTLY: content guardrails, yes. The real gaps were a grant step, a stop path and intake routing |
| R6 | A source splits a WARM service in a way that looks right | CONFIRMED: AAM/5C splits Policy into deciding, issuing a grant and enforcing |
| R7 | No source contradicts the two cross-cutting groups; one makes observability or security a layer | CONFIRMED: Yu et al. and AAM/5C both have such layers |
| R8 | The review changes the model in 2 to 5 places | WRONG: 15 |

Four confirmed, two partly right, two wrong. As with the platform mapping, the errors ran one way: the published models have more that WARM lacked than I expected.

## What no source has
The Directory; a domain as a charter separate from its agents; one accountable domain per responsibility; an agent as an identified actor distinct from its definition; the split between persistent and task agents (AutoGen and Zhu come nearest; Zhu rejects long-lived agents); the platform test stated as a test; Evaluation reporting "unknown". This is the part of WARM that the review leaves distinct.

## Where WARM was thin: Governance
Three or more sources agree on each of these, and WARM v0.11 states none of them.

| Finding | Sources |
|---|---|
| A grant step: authority scoped to one task or action, time-limited, issued only on a positive decision, checked again when the action runs, revocable | Yu et al., Zhu, AAM/5C |
| Separation of duties: whoever proposes or performs an action does not approve it; an agent cannot grant itself authority; whoever writes a rule does not approve it | Yu et al., Zhu, AAM/5C |
| A way to stop or suspend an agent at run time that does not depend on the agent or on the path it would stop | Zhu, AAM/5C, Microsoft, AWS, Google Cloud |
| A check that makes "every call passes an enforcement point" testable | AAM/5C (the vendors' gateways embody it) |
| Policy covers what may be said (content rules), not only what may be done | Microsoft, AWS, Google Cloud |
| Registration is a gate: a tool or agent must be registered to be used, and admission is a release | Microsoft, AWS, Google Cloud |

## The v0.12 change list (specification)
The service count stays 24. No figure changes.

| # | Change to make in the model | Sources | Confidence |
|---|---|---|---|
| V1 | **Grants.** In the Policy row and in a new paragraph under "How the groups relate": a positive decision is issued as a grant, scoped to the action or the task, limited in time and revocable; the grant is checked when the action runs, not only when it is requested. Say that AAM/5C gives deciding, issuing and enforcing to separate components, and that WARM keeps them in Policy and leaves the split to an implementation | Yu, Zhu, AAM/5C | High |
| V2 | **Separation of duties.** New point under "How the groups relate": the actor that proposes or performs an action does not approve it; an agent cannot grant itself authority; whoever writes a rule does not approve it. Example from the reference implementation: one agent writes a change, another reviews it, and a person approves a message sent in their name | Yu, Zhu, AAM/5C | High |
| V3 | **Stop.** Identity row gains "and suspend or revoke an actor". New point: a system needs a way to stop an agent that does not pass through the agent or through a service the agent provides. Tasks cancels a unit of work; Identity suspends the actor. This generalizes the provisional rule about agents that provide Messaging or Reliability | Zhu, AAM/5C, Microsoft, AWS, Google | High |
| V4 | **A check for the Governance condition.** Add to point 1: it can be checked by comparing a record kept at the resource with what the enforcement point admitted; actions taken under a person's or a script's identity are the blind spot | AAM/5C | High |
| V5 | **Policy covers content.** Policy row: rules on what may be done, what may be said, and what is kept. Industry terms gain "content filters" | Microsoft, AWS, Google | High |
| V6 | **Registration is a gate; entries have owners.** In the Registry text: Policy may require that an agent, tool or skill be registered before it is used; adding an entry is a release; each entry names its owner, which is separate from the Directory's accountable domain | Microsoft, AWS, Google | High |
| V7 | **Releases covers rules.** Releases row: changes to agents, skills, rules, the platform and the infrastructure | AAM/5C | High |
| V8 | **Secrets rotate.** Secrets row gains "and rotate or revoke it" | AAM/5C | Medium |
| V9 | **Intake routing.** New short subsection in Step 4 after the Directory text: an inbound request that names no agent has to reach one. Channels delivers by address; when the address does not settle it, the request is routed by what it is about, using the Directory. The component that classifies the request may be an agent providing this platform service. All three vendor architectures have such a router | Microsoft, AWS, Google | High that the gap is real; medium on placement |
| V10 | **Handoff as a tool call.** In the handoff paragraph: a handoff can also be carried as a tool call, when the other agent is exposed as a tool; Orchestration still tracks the assignment | Microsoft, AWS, Google | Medium |
| V11 | **Events.** Messaging row: deliver messages between agents, and events to their subscribers. Scheduling still starts work on an event | Yu, platform mapping | Medium |
| V12 | **Tenancy is a concern.** "Concerns that are not groups" gains tenancy (several organizations or users on one platform): it touches Identity, Policy, Environments and the stores | AWS, Google, Yu, LangGraph | Medium |
| V13 | **The subject's control over stored data.** Policy's rules on what is kept include the right of the person the data is about to see, correct and delete it. Mention in the People paragraph of Step 1 | Microsoft, Google | Medium |
| V14 | **Undo is an open contract question.** In the contracts paragraph of Step 3, add undoing an action's outside effects to the list of what a contract has to settle, and say no service owns it yet | AAM/5C, Zhu | Medium |
| V15 | **Where applications sit.** One sentence in Step 1: an application that calls an agent comes in through Channels; a system that agents act on is reached through Tools; when the system does not operate them, both are Providers | Yu, AAM/5C | Low |

## Recorded and not adopted
| Item | Sources | Why not |
|---|---|---|
| Caching (semantic cache, prompt cache) | Yu, Microsoft, Google, LangGraph | An optimization inside Models or Retrieval; no responsibility of its own |
| Metering, pricing, marketplace | AWS, OpenClaw | Commercial concerns of a platform vendor |
| Model training and fine-tuning | AWS | Outside a system that calls models |
| Approvals by a designated role or by several approvers | Zhu, AAM/5C | WARM's Approvals is a person's decision by design. DECIDED by the author, 2026-11-11 19:45: an agent that merges reviewed changes acts under Policy (a rule people wrote) with Evaluation as the review; it is not a second kind of approval. |
| Role Group: a fixed authority profile across domains | Zhu | One source |
| A single kernel that commits every state change; peer consensus before an act; context integrity proofs | Zhu, AAM/5C | Implementation designs, one source each |
| Harness "requests" tool calls and Tools "executes" them | Yu | A wording refinement; it would change two figures |
| Applicability conditions for each service (when a system needs it) | Yu | Worth doing in the papers on each group |
| Single-agent reasoning (planning, reflection, beliefs and intentions) | AWS, AAM/5C, Yu, Microsoft, Google | Out of scope by Step 0 |

## A crosswalk worth showing in the paper
Yu et al.'s ten responsibilities line up with WARM's parts closely enough to print side by side: L0 business and solution design (People, and a domain's goals, rules and criteria); L1 client and experience (Channels); L2 access, identity and safety control (Governance); L3 agent and workflow orchestration (Harness, Sessions, Tasks, Orchestration); L4 model access and inference (Models); L5 enterprise context and knowledge (Memory, Retrieval); L6 tool and action runtime (Tools, Registry, Environments, with Governance at the point of action); L7 async and event infrastructure (Scheduling, Tasks, Messaging); L8 platform and delivery infrastructure (Infrastructure, Releases, Reliability); L9 evaluation, observability and improvement (Operations). Two independent decompositions arriving at nearly the same cut is evidence for the cut. Yu et al. have no Domains layer, no Directory, no agent kinds and no Artifacts store.

## Corrections already made to v0.11 text
Yu et al. define ten "responsibilities", not layers. Zhu's resident entry is a dormant template activated to lead one task's team, not a persistent agent; Zhu rejects long-lived agents.
