---
title: "Mapping two published models (Yu et al.; Zhu) onto WARM v0.11"
date: 2026-11-11
yardstick: warm-model-v0.11.md
sources:
  - "A: Yu, Rabhi, Zhu, Lu, arXiv:2610.14818v1 (10 Oct 2026)"
  - "B: Lucian Zhu, arXiv:2608.08516v1 (9 Aug 2026, Independent Draft v2)"
status: analysis; read-only mapping, one rater, not second-rated
---

# Mapping Yu et al. and Zhu onto WARM v0.11

## What was read

**Yardstick.** `warm-model-v0.11.md`, read in full. No other file in the `warm/` folder was read.

**Source A: Yu, Rabhi, Zhu, Lu, "A Reference Architecture for Integrating Agentic AI into Enterprise Software"** (arXiv:2610.14818v1).
- Read in full from the arXiv HTML: Abstract, I to VIII (all subsections), Tables I to VI and the reference list.
- Fig. 1 and Fig. 2 are not in the HTML. Their text was read from the arXiv PDF, extracted with pdf.js.
- Fig. 3, the sequence diagram of the worked example, is an image. Only its caption and the prose that describes it were read.
- **The paper does not list the 44 normalized capabilities.** It gives only the count (§III-A) and prose lists per responsibility (§IV-B to IV-D), and those prose lists do not add up to 44: they come to about 54 items. The authoritative list of 44 was taken from the authors' replication package, cited in the paper at §VI-D footnote 1: `github.com/Inspiring-Ming/AI-Agent-for-ESG`, files `synthesis/output/table_capability_set.tex` and `synthesis/output/summary.csv`. That table's per-responsibility counts (L0 4, L1 2, L2 6, L3 6, L4 3, L5 5, L6 7, L7 3, L8 4, L9 4) agree with the paper's statement that the seven responsibilities the case instantiates hold "33 of the 44" (§VI-A). Capability names below are quoted from that table, and the definitions come from the paper's prose for each responsibility.

**Source B: Lucian Zhu, "Fluid Structure, Rigid Record"** (arXiv:2608.08516v1).
- Read in full from the arXiv HTML: Abstract, §1 to §8 (all subsections), Tables 1 to 5, the text of Figures 1 to 3 (SVG text in the HTML) and the reference list.
- A PDF copy was also extracted and spot-checked. It held nothing that the HTML lacked.

Nothing that was asked for was left unread, apart from the Fig. 3 image in A.

## Method

Each source was inventoried before any assignment was made, and quotes were copied from the extracted text. Each item then got exactly one category: one WARM service; a WARM layer; one domain part; a WARM agent concept; a span of several WARM parts; builder or design-time guidance; or MISFIT. A fit is marked **clean** or **strained**, each with a one-line reason. Doubtful fits were called misfits. Interactions between two parts (A's T1 to T8) are assigned as spans of the parts they connect, and the table notes whether WARM states that relation.

Single rater; no second rater sampled these rows. Where a row says what a source "states", the quote shows it. Statements marked *inference* are mine.

---

## Source A: Yu, Rabhi, Zhu, Lu (2026)

### A.1 Inventory and assignment

Legend for the Category column: **S** = one WARM service, **L** = a WARM layer, **D** = a domain part, **AC** = an agent concept, **SPAN** = a span of several WARM parts, **G** = guidance, **MISFIT** = no place in WARM.

#### Groupings of responsibilities (§I)

| ID | Item | Definition (verbatim) | Sec. | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|---|
| A-G1 | Design context | "design context (L0)" | I | People + Goals + Domain rules + design-time guidance | SPAN | Groups a single responsibility; see L0. |
| A-G2 | Interaction and access | "interaction and access (L1–L2)" | I | Channels + Governance group (Identity, Secrets, Policy) + Observability | SPAN | Joins a working service with a cross-cutting group. WARM keeps these apart. |
| A-G3 | Agentic execution and enterprise integration | "agentic execution and enterprise integration (L3–L6)" | I | Runtime + Capabilities + Knowledge + Orchestration | SPAN | Covers most of WARM's working groups. |
| A-G4 | Runtime and operational support | "runtime and operational support (L7–L9)" | I | Scheduling/Tasks/Messaging + Infrastructure + Operations group | SPAN | Joins infrastructure with Operations. |

#### Responsibilities L0 to L9 (§IV-B to IV-D)

| ID | Item | Definition (verbatim) | Sec. | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|---|
| L0 | Business & Solution Design (Decide) | "translates business objectives and enterprise constraints into requirements"; "establishes ownership, accountability, risk, and regulatory requirements"; "rather than acting as a runtime step" | IV-B | People + Goals + Domain rules + Acceptance criteria + design-time guidance | SPAN | A design-time responsibility. WARM has no design-time part; its content is split across People and charter parts, at system level rather than per domain. |
| L1 | Client & Experience (Interact) | "provides the interaction surfaces through which users and software clients access agentic capabilities"; "owns interaction and presentation, not agent reasoning or coordination" | IV-B | Channels | S | Clean. Serves people and programs, as v0.11's Channels does. |
| L2 | Access, Identity & Safety Control (Protect) | "protects the controlled system boundary and establishes the identity, authority, tenant, and policy context associated with a request" | IV-B | Identity + Secrets + Policy + Observability (access audit) | SPAN | WARM's Governance group, minus Approvals, plus audit. |
| L3 | Agent & Workflow Orchestration (Coordinate) | "controls goal-directed execution"; "agent runtime and control flow, execution constraints, in-flight execution context, prompt and runtime configuration, and execution state, recovery, and continuity" | IV-C | Harness + Sessions + Tasks + Orchestration (+ Registry for agent discovery; Approvals/Channels for human intervention) | SPAN | The largest span: one responsibility in A covers four WARM services across two groups. |
| L4 | Model Access & Inference (Infer) | "provides controlled access to model inference while isolating execution logic from particular model providers" | IV-C | Models | S | Clean. |
| L5 | Enterprise Context & Knowledge (Ground) | "provides persistent enterprise information and governed context"; "owns the retrieval and assembly of persistent context" | IV-C | Memory + Retrieval (+ Policy for data governance) | SPAN | A joins Memory and Retrieval, and also claims context assembly, which WARM gives to the Harness. |
| L6 | Tool & Action Runtime (Act) | "resolves, validates, authorizes, executes, and records invocations of capabilities that interact with enterprise systems or produce effects outside agent coordination" | IV-C | Tools + Registry + Policy + Secrets + Approvals + Environments + Observability | SPAN | Seven WARM services sit at A's point of action. |
| L7 | Async & Event Infrastructure (Decouple) | "supports asynchronous, event-driven, and long-running communication"; "changes delivery semantics without taking ownership of the operation communicated" | IV-D | Scheduling + Tasks + Messaging + Infrastructure | SPAN | WARM Messaging is agent-to-agent only. A's L7 carries tasks and events between components; nothing in WARM owns that. |
| L8 | Platform & Delivery Infrastructure (Operate) | "provides the compute, connectivity, storage, resilience, and delivery environment (infrastructure as code, CI/CD, release management)"; "owns platform operation rather than agent behavior" | IV-D | Infrastructure layer + Releases + Reliability | SPAN | A layer plus two Operations services. |
| L9 | Evaluation, Observability & Improvement (Improve) | "correlates operational and evaluation evidence across the architecture to assess system behavior and support diagnosis and improvement" | IV-D | Observability + Evaluation + Improvement | SPAN | Three of WARM's five Operations services, as one responsibility. |

#### Boundary invariants (§IV-A)

| ID | Item | Definition (verbatim) | Sec. | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|---|
| I1 | Coordination–Execution Separation | "L3 owns execution coordination, including control flow and the decision to request an external capability, whereas L6 owns the authorization and execution of that capability against the target resource." | IV-A | Harness/Orchestration vs Tools + Policy | SPAN | WARM's Harness "carries out the tool calls"; A puts execution in Tools. See finding b1. |
| I2 | Execution-State–Knowledge Separation | "L3 owns information whose purpose and lifecycle are bound to coordinating an active execution"; "L5 owns information intended to be independently indexed or retrieved as reusable context across executions" | IV-A | Sessions/Tasks vs Memory/Retrieval | SPAN | Agrees with WARM's cut "by what is kept". |
| I3 | System-Access–Resource-Authority Separation | "Requesting an action is distinct from being authorized to perform it"; "propagated authority should be scoped and time-limited, and L6 re-authorizes at execution time" | IV-A | Identity + Policy + Tools + Retrieval | SPAN | WARM has no statement on delegated authority, its scope or its expiry. |
| I4 | Evidence-Ownership–Correlation Separation | "Responsibilities L1–L8 remain authoritative producers of evidence about their local operations, while L9 correlates that evidence" | IV-A | Observability | S | Strained: WARM's Observability "collects evidence" and does not say who is authoritative for it. |

#### Typed interactions T1 to T8 (Table I)

| ID | Item | Definition (verbatim) | Sec. | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|---|
| T1 | Client Request / Response, L1↔L2↔L3 | "Carries client intent through the controlled boundary at L2 to L3 and returns responses, status, or artifacts through L2 egress control" | Tbl I | Channels → Identity/Policy → Harness/Sessions | SPAN | WARM states the trigger (Channels) and that Governance constrains it. It does not state an egress check on results. |
| T2 | Identity & Authority Context, L2→L3/L5/L6 | "Propagates principal, tenant, entitlement, delegated-authority, policy, and trace context; receiving responsibilities retain resource-specific enforcement." | Tbl I | Identity + Policy + Observability (trace) | SPAN | WARM does not state propagation of authority context. |
| T3 | Inference Request / Result, L3↔L4 | "Requests model capabilities under specified constraints and returns model output, validation status, model metadata, and usage information." | Tbl I | Harness ↔ Models | SPAN | WARM states this relation ("The Harness sends context to Models"). |
| T4 | Context Query / Grounded Context, L3↔L5 | "Expresses an information need and returns governed context, evidence, metadata, and provenance" | Tbl I | Harness ↔ Memory/Retrieval | SPAN | WARM states this relation. |
| T5 | Action Intent / Observation, L3↔L6 | "Requests execution of an external capability and returns its result, status, error, state-change evidence, or provenance." | Tbl I | Harness ↔ Tools | SPAN | WARM states this relation. |
| T6 | Async Task / Observation Event, L3/L6↔L7 | "Mediates tasks and observations through asynchronous or event-driven delivery while preserving ownership in the originating and receiving responsibilities." | Tbl I | Tasks + Scheduling + Messaging | SPAN | WARM does not state this relation. |
| T7 | Operational & Evaluation Evidence, L1–L8→L9 | "Provides locally produced traces, events, outcomes, usage, cost, audit information, and provenance" | Tbl I | Observability | S | Clean. Matches "Operations observes the other five". |
| T8 | Improvement Feedback, L9→L0 / relevant | "Returns evaluation findings, failure evidence, and quality, cost, or performance observations to inform governed architectural or configuration changes." | Tbl I | Improvement | S | Clean. Matches "Improvement proposes, a person or release process decides". |

#### The 44 normalized capabilities (replication-package table; definitions from §IV prose)

| ID | Capability (verbatim name) | Resp. | Definition or context (verbatim, §IV) | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|---|
| NC01 | Business objectives and success criteria | L0 | "use cases and expected value" | Goals | D | Strained: "success criteria" is business-level and could also be read as acceptance criteria. |
| NC02 | Governance risk ownership and lifecycle control | L0 | "establishes ownership, accountability, risk, and regulatory requirements" | People + Directory content + Domain rules + Releases (lifecycle) | SPAN | Ownership set at design time, with no runtime record. |
| NC03 | Architectural requirements and constraints | L0 | "architectural principles and system boundaries" | Design-time guidance | G | Not part of a running system. |
| NC04 | Delivery and adoption planning | L0 | "delivery and adoption" | Design-time guidance | G | Organizational rollout. Not part of a running system. |
| NC05 | Client request and response handling | L1 | "interaction surfaces through which users and software clients access agentic capabilities" | Channels | S | Clean. |
| NC06 | Multi-channel interaction surface | L1 | "web applications, enterprise communication channels, and programmatic clients" | Channels | S | Clean. |
| NC07 | Principal authentication | L2 | "user and agent identity and authentication" | Identity | S | Clean. |
| NC08 | System-level authorization and entitlement propagation | L2 | "system-level access authorization and delegation context" | Identity + Policy | SPAN | Authorization is Policy; propagating on whose behalf an actor works is Identity. |
| NC09 | Inbound and outbound safety control | L2 | "boundary-level safety controls"; "Input and output guardrails sit at the L2 boundary" | Policy | S | Clean: WARM lists guardrails under Policy. |
| NC10 | Ingress traffic and abuse control | L2 | "ingress and traffic control" | Policy + Scheduling | SPAN | WARM lists "rate limits" under Scheduling, but throttling at the boundary is a decision on whether an action may proceed, which is Policy. WARM's boundary between the two is unclear here. |
| NC11 | Input data protection and egress control | L2 | "input and data protection"; "egress and data control" | Policy | S | Strained: WARM Policy's "how it is protected" covers stored data, not data leaving the system. |
| NC12 | Security audit logging | L2 | "access auditing" | Observability | S | Clean ("audit log" is a WARM term). |
| NC13 | Task decomposition and planning | L3 | Fig. 2: "Interpret goals; plan next step" | — | MISFIT | WARM Step 0 excludes single-agent reasoning ("planning, reflection"). Multi-agent decomposition would be Orchestration, but the sources cited for NC13 (S01, S02) are surveys of agent reasoning. Out of scope by design. |
| NC14 | Execution coordination and workflow routing | L3 | "agent runtime and control flow" | Harness + Orchestration | SPAN | Within one agent this is the loop; across agents it is Orchestration. A does not separate the two. |
| NC15 | Working context and execution state | L3 | "in-flight execution context"; "execution state, recovery, and continuity" | Harness (context window) + Sessions | SPAN | |
| NC16 | Bounded and iterative execution control | L3 | "execution constraints"; "terminating a task that exceeds its budget belongs to L3" | Harness + Tasks + Policy | SPAN | Budget limits are Policy; cancellation is Tasks; the call cap is in the loop. |
| NC17 | Agent discovery and collaboration | L3 | "collaboration among multiple agents"; realization "Agent registry; A2A or direct calls" | Registry + Orchestration + Messaging | SPAN | Discovery here means a catalog, not WARM's Directory. |
| NC18 | Human review and intervention | L3 | "human interaction or intervention"; realization "Clarification, review, pause/resume" | Approvals + Channels + Sessions | SPAN | |
| NC19 | Unified model access and invocation | L4 | "unified model access"; "model invocation" | Models | S | Clean. |
| NC20 | Model selection and routing policy | L4 | "model selection and routing, provider policy and capacity controls" | Models | S | Clean. |
| NC21 | Inference output contract validation | L4 | "a response must call a registered tool or answer; refusals and truncated outputs count as failures" (§V-A) | Models | S | Strained: WARM does not say whether validating a model's output belongs to Models' mediation or to the Harness. |
| NC22 | Enterprise information sources and stores | L5 | "information sources, ingestion and preparation, enterprise context stores" | Retrieval + Domain knowledge + Providers | SPAN | The sources themselves are domain knowledge or external systems; fetching from them is Retrieval. |
| NC23 | Retrieval and context assembly | L5 | "L5 owns the retrieval and assembly of persistent context, while L3 determines how that context is used" | Retrieval + Harness | SPAN | A boundary disagreement: WARM gives context assembly to the Harness. |
| NC24 | Persistent and retrievable memory | L5 | "enterprise context stores and persistent memory" | Memory | S | Clean. |
| NC25 | Knowledge provenance and lineage | L5 | T4: "returns governed context, evidence, metadata, and provenance" | Memory + Retrieval | SPAN | WARM gives provenance only to Memory ("where each entry came from"). |
| NC26 | Data governance and access constraints | L5 | "data governance"; "L5 applies access and tenant constraints during retrieval" | Policy | S | Clean: rules on data, enforced at Retrieval. |
| NC27 | Tool and skill invocation | L6 | "tool integration and execution" | Tools | S | Strained: "skill" here is a callable capability, not a WARM skill, which is a set of instructions held in the Registry (term clash). |
| NC28 | Tool discovery registry and metadata | L6 | "tool and capability registration" | Registry | S | Clean. |
| NC29 | Action and result validation | L6 | "invocation validation and adaptation"; "reliability and outcome handling" | Tools | S | Strained: validating arguments is mediation; validating results comes close to Evaluation. |
| NC30 | Resource-specific authorization and credentials | L6 | "resource-specific authorization and credential binding" | Policy + Secrets | SPAN | |
| NC31 | Approval gate for consequential actions | L6 | "L6 can apply an action-policy or approval gate before execution" | Approvals | S | Clean. |
| NC32 | Execution isolation and sandboxing | L6 | "Isolate execution of the relevant L6 capability"; "Sandbox or restricted runtime" | Environments | S | Clean. |
| NC33 | Action audit and provenance | L6 | "action audit and provenance" | Observability | S | Clean. |
| NC34 | Task queues and decoupled invocation | L7 | "queues, event streaming, and delivery-reliability mechanisms such as retry, ordering, and idempotency" | Scheduling | S | Strained: WARM's queues decide when work starts; A's queues decouple calls between components, which WARM leaves unplaced (Infrastructure, by inference). |
| NC35 | Long-running and background execution | L7 | "Long-running or background execution"; "Queue or durable task mechanism" | Tasks | S | Clean ("durable execution" is a Tasks term). |
| NC36 | Event streaming and subscription | L7 | "Event-driven coordination required"; "Publish/subscribe or event stream" | — | MISFIT | WARM's Scheduling starts work on an event, and its Messaging delivers between agents. No service owns publishing and subscribing to events. WARM's own platform mapping recorded "outbound events" and did not adopt it. |
| NC37 | Runtime compute and deployment environment | L8 | "compute, connectivity, storage" | Infrastructure | L | Clean. |
| NC38 | Scaling networking and storage | L8 | "infrastructure autoscaling belongs to L8" | Infrastructure | L | Clean. |
| NC39 | Resilience and recovery | L8 | "resilience" | Reliability | S | Clean. A places it under infrastructure; WARM places it under Operations. Same responsibility. |
| NC40 | Infrastructure configuration and release | L8 | "infrastructure as code, CI/CD, release management" | Releases | S | Clean: WARM Releases covers "the infrastructure the system manages". |
| NC41 | Telemetry traces logs and metrics | L9 | "telemetry, execution lineage" | Observability | S | Clean. |
| NC42 | Offline evaluation and regression testing | L9 | "evaluation and testing" | Evaluation | S | Clean. |
| NC43 | Online quality cost and performance monitoring | L9 | "usage and cost analysis" | Observability + Evaluation | SPAN | |
| NC44 | Failure analysis and improvement feedback | L9 | "root-cause analysis, and continuous improvement" | Improvement | S | Clean. |

#### Variation points (Table II)

| ID | Condition (verbatim) | Consequence (verbatim) | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|
| VP1 | "Multiple collaborating agents" | "Enable L3 agent collaboration, discovery, and coordination interactions" | Orchestration + Messaging + Registry | SPAN | |
| VP2 | "Deterministic execution constraints" | "Constrain allowable execution transitions in L3" (State machine, DAG, or workflow rules) | Workflow | D | Clean: fixed steps are a domain's workflow, carried by Orchestration and Tasks. |
| VP3 | "Human participation required" | "Enable L3 human interaction and intervention" | Approvals + Channels + Sessions | SPAN | |
| VP4 | "Protected or consequential external effect" | "Enable an L6 action-policy or approval gate" | Policy + Approvals | SPAN | Clean as a span; WARM sends rules that authorize actions to these two. |
| VP5 | "Untrusted or high-risk execution" | "Isolate execution of the relevant L6 capability" | Environments | S | Clean. |
| VP6 | "Delegated or deferred execution" | "Scope and expire propagated authority (T2); L6 re-authorizes at execution time" | Identity + Policy | SPAN | WARM states neither scoping nor expiry of delegated authority. |
| VP7 | "Multi-turn or resumable sessions" | "Durably store L3 execution state; cross-session reuse belongs to L5 (I2)" | Sessions | S | Clean. |
| VP8 | "Persistent cross-execution context required" | "Enable L5 persistent memory and governed retrieval" | Memory | S | Clean. |
| VP9 | "Multiple models or provider constraints" | "Enable L4 model routing and provider policy" | Models | S | Clean. |
| VP10 | "Semantic reuse beneficial" | "Enable L4 semantic caching" | — | MISFIT | No WARM responsibility covers reusing earlier model results. Models is the nearest. WARM's mapping recorded "caching" from one platform and did not adopt it. Semantic caching is also not among A's own 44 capabilities. |
| VP11 | "Long-running or background execution" | "Mediate relevant interactions through L7" | Tasks | S | Clean. |
| VP12 | "Event-driven coordination required" | "Enable L7 event infrastructure" | — | MISFIT | Same gap as NC36. |
| VP13 | "Recovery from multi-step state-changing operations" | "Coordinate recovery in L3 and compensating actions through L6" (Saga or compensation pattern) | Tasks + Tools | SPAN | Consistent with WARM's note that repeating an effect depends on the contract between Tasks, Tools and the outside system. |
| VP14 | "Standardized tool or context interoperability desired" | "Use standardized realization of selected L5/L6 interactions" (MCP) | Choice of mechanism | G | |
| VP15 | "Direct synchronous interaction sufficient" | "Bypass L7 for the relevant interaction" | Choice of mechanism | G | |

#### Other stated rules, relations and actors

| ID | Item | Definition (verbatim) | Sec. | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|---|
| R1 | Not a pipeline | "L0–L9 are responsibility boundaries, not a processing pipeline" | IV | Statement about the model | G | Agrees with WARM's "The relations are not a layering". |
| R2 | Model confinement | "model-driven behavior is confined to selecting the next step (L3) and performing inference (L4), while access control, context retrieval, action execution, and every control are conventional software" | IV-C | Implementation rule | G | Contradicts WARM's "A platform service may use a model or an agent inside it" (finding b11). |
| R3 | Guardrail placement | "Guardrails and verifiers [18] are not a separate responsibility; each is placed where the checked decision is owned." | IV-C | Policy + Retrieval + Models + Harness + Tools + Observability | SPAN | WARM has guardrails as one service (Policy) with enforcement points. |
| R4 | Untrusted results | "returns the observation, which L3 treats as untrusted input rather than instruction" | IV-C | Harness | S | Strained: WARM says nothing on how the loop treats what tools return. |
| R5 | When to separate physically | "Responsibilities should be physically separated where they require distinct credentials, trust, scaling, or change cadence" | VII-A | Deployment guidance | G | Agrees with WARM's "One boundary for each service is an experiment". |
| R6 | Confidentiality coordination | "retrieval authorization (L5), provider data policy (L4), and retention (L9) need coordinated policy set at L0" | VII-A | Policy + Retrieval + Models + Observability + People | SPAN | A puts retention in L9; WARM puts it in Policy. |
| R7 | How to apply the architecture | "an architect identifies the responsibilities a target system requires, enables condition-dependent capabilities ..., selects realization mechanisms ..., and places controls according to the invariants" | IV-E | Builder procedure | G | |
| R8 | Agents of another party | "A2A can realize communication with agents coordinated by L3 or, for agents owned by another party, reached through L6" | IV-E | Messaging/Orchestration vs Tools + Providers | SPAN | Who owns an agent decides how it is reached. WARM does not state this (finding b10). |
| R9 | Hosting relation | "L8 hosts the runtime responsibilities"; Fig. 2 "runs on / deployed by" | IV, Fig. 2 | Infrastructure | L | Clean: "the platform runs on infrastructure". |
| R10 | Conditional capabilities | Fig. 2: "conditional: enabled only when its condition holds (Table II)"; "Variability can therefore alter which capabilities are enabled ... without redefining the responsibilities themselves" | IV-E | Design method | G | WARM says only "a system does not need all twenty-four". |
| X1 | End users | Fig. 2 "Users & clients": "End users" | Fig. 2 | People | L | Clean. |
| X2 | Enterprise apps; API clients | Fig. 2 "Users & clients": "Enterprise apps", "API clients" | Fig. 2 | — | MISFIT | WARM's Channels serves applications, but no WARM layer holds a calling application. Providers covers only what the platform calls, not what calls the platform. |

Not inventoried: the ESG case components (Table III), the seven case questions (Table IV), the probe results (Table V) and the mapping of Lu et al. (Table VI). They are evidence about the architecture, not parts of it.

### A.2 Reverse direction: does Source A have each WARM part?

Terms were searched in the body text, Abstract through Conclusion, with case-insensitive substring matching. Counts are in brackets. Each "cron" hit was the company name "Micron".

| WARM part | In A? | Where, or what was searched |
|---|---|---|
| **Harness** | Partly | Inside L3 ("agent runtime and control flow"). §VII-A calls the whole an "execution harness" [harness 1]. Context assembly is claimed by L5. |
| **Sessions** | Partly | VP7 "Multi-turn or resumable sessions" → L3 execution state. L1's "client sessions" are UI sessions. |
| **Tasks** | Partly | L3 execution state and recovery; NC35 durable background execution; VP13 saga. No separate lifecycle responsibility. |
| **Environments** | Fully | NC32, L6 isolation. |
| **Scheduling** | Partly | Queues and events in L7 (NC34, NC36). Nothing starts work at a time. Searched: schedul [0], cron [0 real], timer [0], periodic [0], trigger [0]. |
| **Memory** | Fully | NC24, inside L5. |
| **Retrieval** | Fully | NC23, L5. |
| **Artifacts** | Partly (no store) | Returned through L1/T1 ("responses, status, or artifacts"); nothing stores or versions them. Searched: artifact [2], version [1], output store [0]. |
| **Models** | Fully | L4. |
| **Tools** | Fully | L6. |
| **Registry** | Partly | Tool registry (NC28); an agent registry appears only as a realization in VP1. No registry of agent definitions, prompts or skills. Searched: registr [3], skill [0 in paper; 1 in the capability table]. |
| **Directory** | Absent | No runtime record of which area of work is accountable for what. Ownership is architectural (which responsibility owns a decision), and L0 sets "ownership, accountability" at design time. Searched: directory [0], owner/ownership [20, all about responsibilities owning decisions], accountab [2], department [0]. |
| **Messaging** | Partly | A2A appears as a realization; L7 delivery is between components. Searched: messag [2]. |
| **Orchestration** | Fully | L3. |
| **Channels** | Fully | L1, including programmatic clients. |
| **Identity** | Fully | L2 (NC07, NC08), I3, T2. |
| **Secrets** | Fully | L2 "secrets management"; L6 "credential binding". |
| **Policy** | Fully, but split up | L2, L5, L6 and the guardrail rule R3. |
| **Approvals** | Fully | NC31. The case requires an approver "who holds the override entitlement and is not the submitter". |
| **Observability** | Fully | L9, I4, T7. |
| **Evaluation** | Fully | NC42, NC43. |
| **Improvement** | Fully | NC44, T8. |
| **Releases** | Partly | Infrastructure and CI/CD release only (NC40, L8). No versioning of agents, prompts or skills is named; L0's "lifecycle control" is a governance phrase. Searched: release [1], version [1], rollback [0]. |
| **Reliability** | Fully | NC39. |
| **People** layer | Partly | "End users"; approvers in the case; L0 implies people who decide. |
| **Domains** layer | Absent | Searched: domain [4]. The hits are "domain-specific structure" (related work), "failure domains" (I-A), "one domain and one existing system" (VII-B) and "further domains" (VIII). In A, "domain" means the application area of a deployment. Searched: charter [0], department [0]. |
| **Platform** | Fully | L1 to L7 and L9 as runtime responsibilities. |
| **Infrastructure** layer | Fully | L8. |
| **Providers** layer | Partly | L4 "isolating execution logic from particular model providers"; external enterprise systems are reached through L6. |
| **Goals** | Partly, system level | NC01. |
| **Roles** | Partly, people only | Entitlement roles (portfolio manager, compliance officer). No agent roles. Searched: role [5]. |
| **Workflow** | Partly | L3 control flow; VP2. |
| **Domain knowledge** | Partly, system level | L5 enterprise knowledge. |
| **Domain tools** | Partly, system level | L6. The case's tools are reused services of the existing system. |
| **Domain rules** | Partly | L0 governance. In the case, the fund mandate (a domain rule) is held inside an L6 service: "The service holds the mandate; the request cannot change it" (§V-A). |
| **Acceptance criteria** | Partly | Fig. 2 L0 "evaluation criteria"; L9 evaluation; the L3 "number check". |
| Agent / definition / persistent / task agent | Agent undefined; definition partly ("prompt and runtime configuration"); persistent agent absent; task agent absent | Searched: persistent [10, all about memory or knowledge], resident [0], long-lived [0], long-running [2, about execution], temporary [0], worker [0]. |

### A.3 Counts for Source A

| Inventory items | Clean one-part fits | Strained one-part fits | Spans | Guidance | Misfits |
|---|---|---|---|---|---|
| 97 | 33 | 8 | 42 | 9 | 5 |

The 42 spans include 4 groupings, 8 of the 10 responsibilities and 6 two-party interactions; spanning is built into those items. Of the 44 capabilities on their own: 26 clean, 6 strained, 9 spans, 2 guidance, 2 misfits (NC13, NC36).

---

## Source B: Zhu (2026)

### B.1 Inventory and assignment

#### Layers and modules (§3)

| ID | Item | Definition (verbatim) | Sec. | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|---|
| B1 | Persistent layer | "answers what reusable capabilities and organizational memory exist?" | 3.1 | Registry + Memory + Artifacts + Observability (Log) | SPAN | Cut by lifetime, not by question. |
| B2 | Coordination layer | "answers what world and what state changes are available to this identity now?" | 3.1 | Policy + Identity + Harness (compiled view) | SPAN | |
| B3 | Runtime layer | "answers who performs this task, in what dependency shape, against which working set?" | 3.1 | Orchestration + Tasks + Sessions + Environments | SPAN | |
| B4 | Human-interaction layer | "answers how does a principal express intent, inspect state, correct decisions, and stop the system?" | 3.1 | People + Channels + Approvals + stop path | SPAN | |
| B5 | Policy Π | "Π is policy enforced outside model inference" | 3.1 | Policy | S | Clean. |
| B6 | Specialization/Role-Group Agent Pool | "A resident entry is a reusable specification, not a permanently busy digital employee"; "It waits dormant in the pool" | 3.2 | Registry | S | Strained: entries also carry "default P&P templates", which WARM keeps in Policy, not in a definition. |
| B7 | Four-store record system | "separates four stores by lifecycle and consistency requirement" | 3.2 | Sessions/Tasks + Observability + Artifacts + Memory/Registry | SPAN | |
| B8 | Runtime store R | "task cards, approved cache, working payloads, grants, heartbeat, board state"; "disposable sandbox; rebuild or re-cache" | Tbl 2 | Sessions + Tasks + Environments | SPAN | |
| B9 | Log E | "accepted events, authority use, lineage, handoff and decision records"; "kernel appends; no agent edits or deletes"; "The Log is the source of truth for accepted state changes" | Tbl 2, 3.2 | Observability + Tasks + Sessions | SPAN | The audit record is made the source of truth for state. WARM keeps evidence (Observability) and state (Sessions, Tasks) apart. |
| B10 | Artifact Store F | "approved deliverables, datasets, design records, versioned payloads"; "reviewer-authorized promotion with lineage and content hash" | Tbl 2 | Artifacts | S | Clean. The first prior-work counterpart of WARM's Artifacts. |
| B11 | Knowledge store K | "reviewed patterns, references, workflows, skills, incident lessons"; "approved change proposal only"; "reusable semantic/procedural memory" | Tbl 2 | Memory + Registry (skills) + Retrieval | SPAN | B keeps skills in a memory store, which v0.11 moved out of Memory. Its change rule (approved proposals only) agrees with v0.11. |
| B12 | Archival | "Archiving excludes obsolete versions from default retrieval; it does not delete their existence. Each document family has one current pointer" | 3.2 | Artifacts (versions) + Retrieval + Policy (retention) | SPAN | |
| B13 | Registrar | "may maintain manifests, current pointers, checksums, indexes, and compaction schedules. It is an Operation specialization—a librarian, not an editor" | 3.2 | Artifacts + Retrieval + Reliability, carried out by an agent | SPAN | Matches WARM's provisional "component that provides a platform service may itself be an agent". |
| B14 | Recovery semantics (Prop. 1) | "If Runtime is lost, deterministic replay reconstructs task state from the event prefix"; "The stores should therefore fail independently, with separate recovery-point and recovery-time objectives" | 3.2 | Reliability | S | Strained: depends on the Log being the source of state, which WARM does not state. |

#### Coordination: Permission and Privilege (§3.3)

| ID | Item | Definition (verbatim) | Sec. | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|---|
| B15 | Permission | "the externally enforced boundary of resources it may read, tools and channels it may invoke, and regions it may write" | Def. 2 | Policy | S | Clean. |
| B16 | Privilege | "the set of organizational state changes its decision may cause: for example approve, reject, promote, publish, spawn, grant, revoke, adjust, or HALT" | Def. 3 | — | MISFIT | WARM has no concept of authority over organizational state as distinct from permission to act. Its Approvals holds an action "until a person authorizes" it, so an approving agent has no place. Policy could encode privilege only as one more permission, which loses B's distinction. |
| B17 | Compiled working view | "For task τ, the harness compiles the agent's working view"; "a clean, authorized world: broad enough for the task, narrow enough to exclude unrelated or dangerous state" | 3.3, Eq. 7 | Harness + Policy + Retrieval | SPAN | |
| B18 | P&P task lease γ | "deny-by-default, task-bound, time-limited, and non-transferable except through an explicitly attenuating spawn operation. Grant and revocation are both logged." | 3.3, Eq. 8 | Policy + Identity + Tasks | SPAN | WARM has no grant that is bound to a task and expires (compare A's VP6). |
| B19 | State-change validity and kernel commit | "A proposed event e changes organizational state only if" Schema ∧ LeaseActive ∧ Authorized ∧ Precondition; "Natural language may propose e; the non-agent kernel commits it." | 3.3, Eq. 9 | — | MISFIT | No WARM service validates and commits organizational state changes. The parts are spread across Policy, Tasks, Artifacts and Observability, and nothing in WARM is the single commit point B requires. |
| B20 | Fail-closed authority (Prop. 2) | "Stopping new lease issuance and revoking active leases prevents subsequent material state changes by agents"; "A side channel ... that bypasses the harness invalidates the property." | 3.3 | Policy | S | Clean. The same condition as WARM's "Governance covers an action only if the action passes an enforcement point". |

#### Runtime: Workflow Protocol, task cards, Task Group (§3.4)

| ID | Item | Definition (verbatim) | Sec. | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|---|
| B21 | Workflow Protocol W | "an external system module under the Control Plane, not an agent with residual discretion"; "translate a validated task input into a task graph; select specializations and a topology; initialize the runtime working set; issue and revoke P&P; expose a lightweight board; and execute circuit breakers or kill commands" | 3.4 | Orchestration + Tasks + Policy (grants) + Environments + Reliability | SPAN | B's coordinator also grants authority. WARM keeps granting in Governance. |
| B22 | Typed task card τ | "g is the goal, I approved inputs, O required outputs, κ completion and evaluation criteria, D dependencies, b budget, d deadline, r risk class, and ℓ lineage pointers" | 3.4, Eq. 10 | Tasks | S | Strained: WARM gives no task schema. Its handoff ("the facts, what is wanted, what counts as done") is informal. |
| B23 | Topology selection φ | "single, parallel, centralized, decentralized, hybrid" | Eq. 11 | Orchestration | S | Clean: "who does what, what depends on what". |
| B24 | Task Group G | "the set of active Task Groups"; "Dynamic Task Group: temporary specialist workers" | 3.1, Fig. 1 | Task agent (a team of them) | AC | Strained: WARM has no named unit for a temporary team. |
| B25 | Fan-out limit f_max | "Each aggregator has a fan-out parameter f_max because its context bandwidth is a designed resource." | 3.4 | Orchestration | S | Strained: a limit set by the context bandwidth of one agent, not by system capacity (Scheduling). |
| B26 | Net-utility selection objective | "The selection objective is net organizational utility, not maximum agent count" | Eq. 13 | Design guidance | G | WARM Step 4 gives the same considerations informally. |
| B27 | Board | "Eligible cards appear on a board filtered by specialization and Permission." | 3.4 | Tasks + Scheduling | SPAN | |
| B28 | Claim is commitment | "Claiming a card consumes a work-in-progress slot, starts a heartbeat, activates the lease, and records a budget and deadline commitment." | 3.4 | Tasks + Scheduling + Policy + Reliability | SPAN | |
| B29 | Completion tuple h | "c is the claim, e evidence, p̂ confidence or uncertainty, and k measured cost"; "distinguishes 'submitted' from 'believed correct'" | Eq. 14 | Orchestration + Evaluation | SPAN | |
| B30 | Records carry; messages point | "Agent-to-agent messages remain useful as interrupts ... They are not the canonical work object." | 3.4 | Messaging + Tasks + Artifacts | SPAN | Contradicts WARM's "Messaging carries the request" (finding b14). |
| B31 | Objective handoff | "a card withholds that preference and specifies only the deliverable standard"; "a conditional mechanism to test" | 3.4 | Workflow-design guidance | G | |

#### Human-interaction layer (§3.5)

| ID | Item | Definition (verbatim) | Sec. | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|---|
| B32 | Human principal H | Fig. 1 "goal, veto, org kill"; "The human remains the correction endpoint, organization-kill holder, and one key for Major or Emergency changes." | 3.1, 3.5 | People | L | Clean. |
| B33 | Control Plane C | "the organization's OA/admin interface"; "task initiation, board inspection, P&P state, decision queues, FLAGs, budgets, and shutdown"; "owns a minimal independent cache"; "Data-plane failure must not remove the brake." | 3.5 | Channels + Approvals + Observability + stop path | SPAN | WARM has no operator console. Its stop part is B57. |
| B34 | Translation Agent T | "a secretary and interpreter, not a machine CEO"; "convert human language into proposed task cards, surface ambiguities, and render machine state back"; "cannot approve its own interpretation" | 3.5 | Role (intake) | AC | Strained: WARM does not say whether intake is a platform role or a domain role. |

#### Role Groups (§4)

| ID | Item | Definition (verbatim) | Sec. | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|---|
| B35 | Role Group (the concept) | "Role Group asks what relationship to organizational truth and change is safe?"; "the domain does not confer the power"; "fixed constitutional categories" | 4 | — | MISFIT | WARM's role is "a position with stated duties" in a domain. B's Role Group is a profile of authority that crosses domains. WARM has no such second axis; the nearest is Policy. |
| B36 | Operation | "low organization-wide; narrow task runtime"; "produce, transform, call tools, submit evidence"; cannot "approve own output, write durable stores directly" | Tbl 3 | Role | AC | Strained: defined by authority, not by duties in a domain. |
| B37 | Reviewer | "high scoped change authority: approve, reject, promote, adjust, roll back, grant/revoke"; "cannot trigger its own broad read window" | Tbl 3, 4 | Role + Approvals + Releases (promotion) | SPAN | |
| B38 | Supervisor | "high observational coverage across four stores"; "sample work, run canaries, test provenance, adversarially challenge"; cannot "approve, promote, rewrite" | Tbl 3, 4 | Role + Evaluation + Observability + Tasks (HALT) | SPAN | |
| B39 | Collaboration loop | "Operation submits work and evidence. Supervisor observes the record and ... sends a FLAG ... to Reviewer. Reviewer ... commits or rejects a typed decision. The Workflow Protocol then recompiles P&P" | 4 | Evaluation + Approvals + Orchestration + Policy | SPAN | |
| B40 | FLAG | "A FLAG must carry a replayable evidence pointer." | 4 | Evaluation | S | Strained: a report of a suspected defect, routed onward; WARM's Evaluation does not route. |
| B41 | Task HALT | "Its ability to HALT a task is a separate circuit-breaker authority" | 4 | Tasks | S | Clean (cancellation). |
| B42 | Second key / countersignature | "Major or irreversible change requires a second key from a distinct Reviewer, a deterministic control, or the human." | 4 | Approvals | S | Strained: the second key need not be a person. |

#### Design laws and corollaries (§2.2)

| ID | Item | Definition (verbatim) | Sec. | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|---|
| B43 | Law L1, Dormancy | "An agent without an active task has zero standing organizational P&P beyond a private workspace and harmless baseline functions." | 2.2 | Policy | S | Strained: WARM does not say whether a persistent agent holds standing authority between tasks. |
| B44 | Law L2, Specialization justifies residency | "A resident agent specification exists only because a durable capability bundle is repeatedly useful"; "Commodity work is temporary." | 2.2 | Persistent agent | AC | Strained: B's "resident" is a dormant specification with no memory or channel of its own (finding c4). |
| B45 | Law L3, AgentSpec = Specialization × RoleGroup | "An organizational identity is specialization times Role Group" | 2.2, Eq. 1 | Agent definition | AC | Strained: puts authority into the definition and equates the definition with identity. WARM says "A definition is not the agent". |
| B46 | Law L4, instantiation and topology follow the task | "It may instantiate temporary, possibly heterogeneous workers that inherit attenuated P&P and cannot expand their own scope." | 2.2 | Task agent + Orchestration + Policy | SPAN | WARM agrees that a persistent agent starts task agents. Attenuated inheritance of authority is not in WARM. |
| B47 | Corollary: records, not sessions | "write work as records and pass pointers, not sessions" | 2.2 | Design rule | G | Close to WARM's guidance on keeping unattended work out of conversations. |
| B48 | Corollary: no agent controls every power | "no agent controls every power" | 2.2 | Policy | S | Strained: WARM states no separation-of-duties rule. |
| B49 | Corollary: manage the world | "manage the world rather than narrate behavior inside a noisy world" | 2.2 | Design rule | G | |
| B50 | Functional translation criterion | "A mechanism from human organization design is transferred only after identifying the failure-generating constraint it addresses." | Def. 1 | Method | G | |
| B51 | Organization-theory translations | Table 1 (8 mechanisms, e.g. "Permission compiles a narrow task view") | 2.1 | Design rationale | G | |

#### Robustness, escalation, measurement (§6)

| ID | Item | Definition (verbatim) | Sec. | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|---|
| B52 | Prevent | "deny-by-default P&P, task-card schema validation, dependency-cycle checks, objective handoffs, budget ceilings, and write asymmetry" | 6.1 | Policy + Tasks | SPAN | |
| B53 | Detect | "heartbeat, acceptance tests, Supervisor sampling, canary tasks, integrity checks, and measured anomalies" | 6.1 | Evaluation + Observability + Reliability | SPAN | |
| B54 | Contain (including lineage quarantine) | "per-group runtime sandboxes, channel circuit breakers, and lineage quarantine: when an artifact is contaminated, descendants become unverified and stop propagating" | 6.1 | Environments + Reliability + Artifacts | SPAN | Artifact lineage is not in WARM. |
| B55 | Recover | "re-cache, deterministic replay, clean-context restart, task return to the board, and rollback" | 6.1 | Reliability + Tasks + Releases | SPAN | |
| B56 | Learn / proposal-based learning | "creates a reviewed incident proposal for Knowledge or policy; the incident never edits the constitution directly"; "only reviewed transitions alter Knowledge or policy" (7.3) | 6.1, 7.3 | Improvement | S | Clean. The same split as WARM's (proposes / decides / Releases). |
| B57 | Independent stop path and kill scopes | "Organization kill: human-only, one action, always available—stop new leases and revoke every active lease"; "acts on leases rather than negotiating through the failed data plane" | 6.3, Fig. 3 | — | MISFIT | No WARM service is responsible for stopping agents. Reliability restores; Policy decides one action at a time. WARM's provisional rule (a service "cannot rely on its own service to recover") points at the same need but names no owner. Task kill alone would be Tasks. |
| B58 | Supervision tree | "temporary worker → resident specialization lead → review domain → human" | 6.2 | Reliability + Orchestration + People | SPAN | |
| B59 | Restart scopes | "one-for-one for an isolated worker, rest-for-one for its downstream lineage, and one-for-all only for inseparable shared state" | 6.2 | Reliability | S | Clean. |
| B60 | Restart-intensity limit (N,T) | "converts repeated failure into escalation" | 6.2 | Tasks | S | Strained: retry is Tasks; turning failure into escalation has no WARM owner. |
| B61 | Error classification | "transient, deterministic, or systemic" | 6.3 | Tasks + Reliability | SPAN | |
| B62 | Typed escalation routes | "Its route is typed as ASSIGN, BLOCK, REVIEW, FLAG, or HALT." | 6.3 | Orchestration + Approvals + Tasks + Evaluation | SPAN | |
| B63 | Decision classes | Standard / Normal / Major / Emergency by "reversibility and blast radius" | Tbl 5 | Policy + Approvals | SPAN | |
| B64 | Break-glass identity | "break-glass identity within predefined bounds" | Tbl 5 | Identity | S | Strained: an emergency identity with special authority; WARM's Identity only establishes who is acting. |
| B65 | Circuit breakers and bulkheads | "Circuit breakers and bulkheads apply familiar distributed-systems patterns" | 6.3 | Reliability | S | Clean. |
| B66 | Per-task metering | "model and tool cost, wall time, retries, human minutes, evidence volume, P&P changes, and incidents" | 6.4 | Observability | S | Clean. |
| B67 | Diagnostic measures χ_coord, A_audit, E_amp | "The first exposes coordination tax; the second tests whether 'power is recorded' is actually true; the third measures propagation." | 6.4 | Observability + Evaluation | SPAN | |
| B68 | Enforced budgets | "Task-, group-, and organization-level ceilings HALT execution" | 6.4 | Policy | S | Clean (spending limits). |
| B69 | Error budget | "an error budget freezes change work after a service objective is exhausted" | 6.4 | Reliability + Releases | SPAN | WARM states no relation between Reliability and Releases. |
| B70 | Criteria versioned and hidden | "acceptance criteria and monitoring policy must therefore be versioned and, when appropriate, hidden from the producer's writable context" | 6.4 | Acceptance criteria + Evaluation + Policy + Releases | SPAN | |
| B71 | Human-offline policy | "During human-offline periods, only pre-approved, reversible Standard work proceeds automatically; higher-risk decisions queue or HALT." | 3.5 | Policy + Approvals | SPAN | |
| B72 | Logical before physical separation | "In a small, low-risk prototype, one model may perform Review and Supervision in clean, sequential contexts"; "For consequential work, identities and contexts must be distinct" | 4 | Deployment guidance | G | |
| B73 | Agent OS analogy | "Only as a future research lens, the architecture resembles an operating system." | 7.3 | Future research | G | |
| B74 | Hypotheses H1–H5 and evaluation plan | "The framework makes falsifiable predictions"; baselines B0–B4; ablations | 7.1 | Research method | G | |

#### Cross-cutting concepts

| ID | Item | Definition (verbatim) | Sec. | Assignment | Cat. | Fit / reason |
|---|---|---|---|---|---|---|
| B75 | Integrated control path | "Persistent Pool + Rigid Record → (Workflow Protocol + P&P) → Dynamic Task Group" | 5, Eq. 15 | Registry + Artifacts/Memory/Observability + Orchestration + Policy + task agents | SPAN | |
| B76 | Temporary workers | "instantiate temporary workers"; "every child receives attenuated grants and remains low/low" | 1, 4 | Task agent | AC | Clean. |
| B77 | Specialization | "domain specialization—for example evidence retrieval, financial modeling, interface design, or provenance checking"; "domain context, tools, skills, evaluation priors, or a stable working style" | 2.2, 3.2 | Agent definition + Domain knowledge + Domain tools + Acceptance criteria | SPAN | |
| B78 | Records-as-completion rule | "Work is considered organizationally complete only when its material result and authority exercise are represented by valid records." | 3.2 | Tasks + Observability + Artifacts | SPAN | Close to WARM's "Delivery alone establishes neither that the work was accepted nor that it was done". |

### B.2 Reverse direction: does Source B have each WARM part?

Same search method as for A, over Abstract through Conclusion.

| WARM part | In B? | Where, or what was searched |
|---|---|---|
| **Harness** | Partly | "the harness compiles the agent's working view"; the harness mediates material actions (3.3, 7.2). The loop itself is not described [harness 3]. |
| **Sessions** | Partly, demoted | Runtime store holds working state. B argues against sessions as the work carrier: "durable work can remain entangled with sessions" [session 6]. |
| **Tasks** | Fully | Task card, claim, heartbeat, return to board, HALT, replay. |
| **Environments** | Partly | "per-group runtime sandboxes"; the runtime store as "disposable sandbox". |
| **Scheduling** | Partly | Board, work-in-progress slots, budgets. Nothing starts on time. Searched: schedul [2: "compaction schedules", "research on scheduling"], cron [0], timer [0], periodic [1: the Control Plane cache is "periodically recorded"], trigger [1: a Reviewer cannot "trigger" its read window]. Events start work ("An event or task causes the system to select ..."), with no named mechanism. |
| **Memory** | Partly | The Knowledge store is organizational "semantic/procedural memory" behind review. No memory belongs to an agent. |
| **Retrieval** | Partly | Compiled view; "progressive disclosure by task and specialization"; archival rules. Searched: retriev [2]. |
| **Artifacts** | Fully | Artifact Store: versioned, promoted, hashed, with lineage. |
| **Models** | Absent | Model cost (C_model) and "model families ... should also differ" for review only. Searched: provider [0], routing [1, "C_routing", coordination cost], model gateway [0]. |
| **Tools** | Partly | Tools exist inside Permission. No tool-mediation service apart from the harness. |
| **Registry** | Partly | The Specialization pool holds templates. Skills sit in Knowledge. Searched: registr [3, all "Registrar"]. |
| **Directory** | Absent | No record of which area of work is accountable for what. The board filters by specialization, which routes by capability. Searched: directory [0]; owner [1, in the AI Assistance Disclosure, outside the model]; accountab [4: "accountable history of work", "accountability must survive", "reconstruct accountability", "accountability, traceability, restorability" in §3.2]; responsib [2, neither about areas of work]. |
| **Messaging** | Partly | Messages are interrupts only. |
| **Orchestration** | Fully | Workflow Protocol (non-agent), topology, Task Group. |
| **Channels** | Partly | Control Plane plus Translation Agent, for the human principal only. No interface for calling applications. |
| **Identity** | Partly | Distinct identities for consequential work; break-glass identity; leases name the agent. No identity service. |
| **Secrets** | Partly | Withholding a "credential"; "Shared secrets ... invalidate the guarantee." No secrets service [secret 2]. |
| **Policy** | Fully | Π, Permission, leases, Prop. 2. |
| **Approvals** | Partly, different | Reviewer agents approve; the human is "one key" for Major or Emergency changes. |
| **Observability** | Fully | Log, metering, A_audit. |
| **Evaluation** | Partly | Acceptance tests, canaries, Supervisor sampling, calibration of confidence. |
| **Improvement** | Fully | Learn; proposal-based learning. |
| **Releases** | Partly | Versioned policy and Knowledge changes, rollback and promotion. No release service [release 0]. |
| **Reliability** | Fully | Supervision tree, restart scopes, replay, circuit breakers, separate recovery-point and recovery-time objectives per store. |
| **People** layer | Fully | Human principal and human layer. |
| **Domains** layer | Absent | Searched: domain [6]. Hits: "domain context", "domain specialization", "the domain does not confer the power", "review domain", "domain-specific calibration", "domain-sharded Review". None defines an area of work with goals, rules and accountability. Searched: charter [0], department [0]. |
| **Platform** | Partly | The coordination and runtime layers, plus the stores. |
| **Infrastructure** layer | Absent | Searched: infrastructure [0], deploy [0], machine [0]. |
| **Providers** layer | Absent | Searched: provider [0], vendor [0]. |
| **Goals** | Partly | The task card's goal g; the principal's goal. |
| **Roles** | Present, different | Role Groups (authority) plus specializations (capability). |
| **Workflow** | Fully, as a platform module | Workflow Protocol, task graph. |
| **Domain knowledge** | Partly | Knowledge store; a specialization's "reference packs". |
| **Domain tools** | Partly | Tools in a specialization's configuration. |
| **Domain rules** | Partly | Π, decision classes, human-offline policy, all organization-wide. |
| **Acceptance criteria** | Partly | Task card κ; criteria hidden from the producer. |
| Agent / definition / persistent / task agent | Agent: instance of an AgentSpec. Definition: fully (AgentSpec). Persistent agent: a dormant template, not an actor (see c4). Task agent: fully (temporary workers). | |


### B.3 Counts for Source B

| Inventory items | Clean one-part fits | Strained one-part fits | Spans | Guidance | Misfits |
|---|---|---|---|---|---|
| 78 | 13 | 15 | 37 | 9 | 4 |

---

## Findings

### (a) Misfits and spans, and what each suggests about WARM

**Misfits**

| Item | Source | What it suggests |
|---|---|---|
| NC36, VP12: event streaming and publish/subscribe | A | **A missing service, or a WARM boundary in the wrong place.** Scheduling starts work on an event and Messaging delivers between agents, but no service owns distributing events. This is the second source to show it: WARM's platform mapping recorded "outbound events" from one platform. Either widen Messaging to "deliver messages and events between agents and services" or name it as Infrastructure. |
| VP10: semantic caching | A | **Probably nothing (an optimization), with low weight.** A second source after one platform in WARM's mapping. An optional clause in Models ("may reuse earlier results") would place it. A itself does not count it among its 44 capabilities. |
| NC13: task decomposition and planning | A | **Nothing.** Out of scope by WARM's Step 0. A puts single-agent reasoning inside its orchestration responsibility; WARM deliberately does not model it. |
| X2: enterprise apps and API clients as callers | A | **A small gap in the layers.** WARM names applications as users of Channels but places them in no layer. Providers holds what the platform calls; nothing holds what calls the platform. Either say callers sit outside the boundary, or widen People to "people and applications that request work". |
| B16: Privilege | B | **A WARM boundary drawn in the wrong place, or a missing concept.** WARM has access (Policy) and person approval (Approvals). It has no authority to change organizational state (approve, promote, grant, halt) that can be held by a role, including an agent's. |
| B19: validating and committing state changes in a non-agent kernel | B | **Possibly a missing service. More likely a contract WARM has not written.** WARM's parts cover the pieces, but no service is the system of record for a committed state change. WARM's "contracts are not specified" limit covers this; B shows what the contract would have to say. |
| B35: Role Group as an axis of authority, orthogonal to domain | B | **A missing concept.** WARM's role is a position with duties in a domain, and its authority comes from domain rules applied by Policy and Approvals. B adds a second, fixed axis (Operation, Review, Supervision) that does not depend on domain. WARM could express it as Policy templates, but it has no name for it. |
| B57: independent stop path (organization kill) | B | **A missing responsibility.** WARM has nothing that stops agents or revokes all authority by a path that does not depend on the data plane. The nearest are Reliability (which restores) and WARM's provisional note that a service "cannot rely on its own service to recover". |

**Spans**

Most spans fall into a few patterns:

1. **A's L3 spans Harness, Sessions, Tasks and Orchestration** (also NC14, NC15, NC16). A keeps them as one responsibility and separates them only from knowledge (I2) and execution (I1). This is evidence that WARM's four-way split is not what other authors draw. It is not evidence that the split is wrong: A gives no test that would distinguish them. *Suggests:* nothing, or a note that the Runtime services commonly come as one bundle (WARM already says this of harness products).
2. **A's L5 spans Memory and Retrieval, and claims context assembly** (NC23). The same pattern: A splits by lifecycle, not by who wrote the content. *Suggests:* WARM's Harness/Retrieval boundary for assembling context is contestable. B sides with WARM ("the harness compiles the agent's working view").
3. **A's L6 holds seven WARM services at the point of action**, and A's L2 holds most of Governance at the boundary. A's principle, "each is placed where the checked decision is owned", splits WARM's Policy into decisions taken in one place and enforcement at many. *Suggests:* the Policy responsibility should say where enforcement happens (finding b5).
4. **A's L7 spans Scheduling, Tasks, Messaging and Infrastructure.** *Suggests:* WARM has no home for asynchronous transport between components (see NC36).
5. **A's L9 is three of WARM's Operations services, and A's L8 holds Releases and Reliability with infrastructure.** *Suggests:* nothing. These are groupings, and WARM's services survive inside them.
6. **B's stores cut across WARM services by lifetime and write rule** (B7 to B12): the Log as source of truth for state (B9), Knowledge holding skills (B11). *Suggests:* WARM's "responsibilities, not bins" stance holds. B9 shows that one store can serve both Observability and Tasks, which WARM allows.
7. **B's Workflow Protocol (B21) joins Orchestration with granting authority.** *Suggests:* a contrary design, recorded as a relation (b13).
8. **B's Reviewer and Supervisor (B37, B38) join roles with platform services.** *Suggests:* Approvals and Evaluation can be carried out by agents in a role. WARM's provisional rule on platform-role agents covers Evaluation ("a reviewer that evaluates work") but not Approvals, which WARM makes person-only.
9. **Delegated, time-bound authority (A: I3, VP6, T2; B: B18, B43, B46).** Two independent sources span Identity and Policy with something neither WARM service states: authority scoped to a task, expiring, narrowed when passed to a sub-worker, and checked again at execution time. *Suggests:* add this to Identity or Policy (see changes).

### (b) Relations stated by a source that WARM does not state, or that contradict a WARM relation

| # | Relation in the source | WARM's position | Verdict |
|---|---|---|---|
| b1 | A I1: the orchestrator decides to request an action; the action responsibility authorizes and executes it. | Harness "carries out the tool calls the model asks for"; Tools "mediate calls". | A partial contradiction in wording. WARM puts "carry out" in the Harness; A puts it in Tools. |
| b2 | A I2: execution state vs reusable knowledge. | The cut by what is kept (Sessions, Tasks, Memory). | Agrees. |
| b3 | A I3, T2, VP6: authority is set at the boundary, propagated, scoped and given an expiry, and checked again at the resource when execution is deferred or delegated. | Identity establishes "on whose behalf"; Policy decides. Nothing on propagation or expiry. | Not stated in WARM. B's lease (B18) states the same thing independently. |
| b4 | A I4: each responsibility is the authoritative producer of evidence about its own operations; L9 only correlates. | Observability "collects evidence". | Not stated. Compatible with WARM. |
| b5 | A R3: guardrails are not a separate responsibility; each sits where the checked decision is owned. A's case enforces entitlements at L6 on each call. | Policy is one service; Governance covers an action only if it passes an enforcement point. | Compatible, but A goes further: decisions are distributed, not just enforcement points. |
| b6 | A §IV-C, L6: the approval gate belongs to the action responsibility and runs "before execution". | Approvals is a Governance service separate from Tools. | Location differs; the responsibility is the same. |
| b7 | A R6: retention is placed in L9 (Operations), coordinated by policy set at L0. | Retention is part of Policy (v0.11, M7). | Contradicts on placement. |
| b8 | A T8: evaluation findings go back to L0 (design) or the relevant responsibility "to inform governed ... changes". | Improvement proposes; a person or release process decides; Releases makes the change. | Agrees. |
| b9 | A L7: async infrastructure "changes delivery semantics without taking ownership of the operation communicated". | Messaging only carries; Orchestration tracks. | Agrees, and extends the rule beyond agent-to-agent messages. |
| b10 | A R8: an agent that L3 coordinates is reached as a collaborator; an agent "owned by another party" is reached through the tool responsibility (L6). | Directory says how to reach a role; external services are Providers reached by Tools. | Not stated. Ownership decides the route. This bears on what a Directory entry should say about agents outside the system. |
| b11 | A R2: models only choose the next step and infer; "every control" is conventional software. | "A platform service may use a model or an agent inside it." | Contradicts, but on implementation, which WARM's test deliberately ignores. A states a design rule; WARM states a classification. |
| b12 | A L8 places CI/CD in platform delivery infrastructure. | CI belongs to the Software Factory domain; the parts beneath it are platform services. | Different referent: A means the delivery pipeline of the agent system itself. Not a direct contradiction (see d). |
| b13 | B §3.4: the coordinator (Workflow Protocol) issues and revokes authority for each task. | Orchestration coordinates assignments; Governance (Policy) constrains. Orchestration grants nothing. | Contradicts WARM's separation. B lets the coordinator grant authority, because each grant is tied to the task. |
| b14 | B §3.4: "Records carry; messages point." The handoff is a change in which records are visible; messages are only interrupts. | Messaging "carries the request"; Orchestration tracks the assignment and the result. | A partial contradiction. WARM lets the message carry the request; B makes the record the carrier. Both agree that delivery is not acceptance. |
| b15 | B Tbl 2, §3.2: the Log is the source of truth for accepted state changes, and runtime state is rebuilt by replay. | Observability records; Sessions and Tasks hold state. | Not stated. Allowed by WARM's "one store may serve more than one", but B makes evidence authoritative over state, which WARM does not address. |
| b16 | B §4: Operation cannot approve its own output; Reviewer cannot activate itself; Supervisor cannot change what it inspects. "No agent controls the full chain." | No separation-of-duties rule. | Not stated. A's case states the same rule for people: the approver must not be the submitter (§V-A). Two sources. |
| b17 | B §3.5, §6.3: the stop path does not pass through the data plane. | Provisional: an agent that provides Messaging or Reliability needs a way to start and be repaired that does not pass through itself. | B generalizes WARM's provisional rule from repair to stopping. |
| b18 | B §6.4: an exhausted error budget freezes change work. | No relation between Reliability and Releases. | Not stated (Operations services relating to each other). |
| b19 | B §6.4: acceptance criteria are hidden from the producer's writable context. | Acceptance criteria are carried by Evaluation. Nothing on who may see them. | Not stated. |
| b20 | B §6.1 Learn, §7.3: "only reviewed transitions alter Knowledge or policy". | Improvement proposes; Releases changes. | Agrees, and supports v0.11's choice not to apply changes automatically. |

### (c) Areas of work, accountability, registries, and long-lived versus per-task agents (WARM Steps 0 and 4)

1. **Domains.** Neither source has a domain as WARM defines one: a charter with goals, roles, workflow, knowledge, tools, rules and criteria, holding a set of responsibilities.
   - A is a one-domain system (ESG portfolio compliance). Its L0 holds charter-like content (objectives, requirements, governance, ownership, accountability, evaluation criteria) for the whole system and at design time. This is consistent with WARM's "When the Domain layer matters": a single-purpose system has one domain and does not name it.
   - B uses "domain" for a specialization, and says authority does not come from the domain ("the domain does not confer the power"). In WARM, a domain's rules decide who may authorize what (for example, Communications' approval rule). B's later "domain-sharded Review" and the "review domain" in its supervision tree suggest that B's review may eventually be split by area of work. *Inference:* that would be the first point where B needs something like WARM's domains.
2. **Ownership and accountability.**
   - In A, accountability is architectural: each responsibility "owns" decisions, information or effects (§III-B), and L0 sets "ownership, accountability". No runtime record says which part of an organization is accountable for a kind of work.
   - In B, accountability means the record of who did what with which authority ("reconstruct accountability"; A_audit). That is accountability for actions, not for areas of work.
   - WARM's Directory (accountability for scoped responsibilities, by domain) has no counterpart in either. This confirms WARM v0.11's claim 3 ("No source read has a directory ...") for these two papers.
3. **Registries and directories.** A has a tool registry (NC28) and, as an option, an agent registry for discovery (VP1). B has the Specialization pool and a Registrar that keeps indexes. All three are catalogs or indexes, which matches WARM's finding that "the registry is a catalog".
4. **Long-lived versus per-task agents.**
   - A has no such distinction. Searched: persistent, resident, long-lived, temporary, worker. "Long-running" refers to execution.
   - B distinguishes **dormant resident specifications** from **temporary workers**: "A resident entry is a reusable specification, not a permanently busy digital employee"; "There is no digital employee permanently nailed to a position"; "its durable identity lies in the record, policy, and reusable specialization templates." A resident, once activated, acts as a team lead for a task. It has no memory of its own (memory is the organization's Knowledge store) and no channel of its own (the Control Plane is the channel). So B's resident sits between WARM's agent definition (held in the Registry) and a task agent that coordinates other task agents. It is not WARM's persistent agent, which keeps "its identity, its session history, what it has learned, and a channel".
   - B's Law L3 makes identity the product of specification and Role Group. WARM says an agent's identity persists through a change of definition. These two contradict each other.
   - **Correction to WARM v0.11.** Its prior-work paragraph says Zhu "distinguishes resident agents from task-scoped ones, as WARM distinguishes persistent agents from task agents". That overstates the match. B distinguishes a dormant template from active instances, and deliberately has no long-lived actor.
   - B's Law L1 (zero standing authority without a task) bears on a question WARM leaves open: what authority a persistent agent holds between tasks.
5. **Agents in platform roles.** B's Registrar ("an Operation specialization") and Translation Agent are agents doing platform-type work under narrow authority. This agrees with WARM's provisional rule that such roles belong to the platform. B adds a constraint WARM lacks: such an agent has no authority over content ("a librarian, not an editor"; "cannot approve its own interpretation").

### (d) Same word, different meaning

| Term | WARM | Source A | Source B |
|---|---|---|---|
| Layer | One of five logical categories (People, Domains, Platform, Infrastructure, Providers) | A never uses "layer". L0 to L9 are "responsibilities" and "responsibility boundaries", closer in size to WARM's services and groups. (WARM v0.11 calls them "ten layers"; that should be "ten responsibilities".) | Four layers cut by lifetime and function (persistent, coordination, runtime, human) |
| Responsibility | What a part is accountable for: one per service, a set per domain | A grouping of capabilities with one architectural purpose and owner, roughly a WARM group | Used only in passing |
| Capability / Capabilities | A group (Models, Tools, Registry) | A normalized function (44 of them); also "external capability" for an invoked tool | "capability bundle" (a specialization) |
| Harness | The service that runs the agent loop | "execution harness" in which "deterministic services, verifiers, and policy controls retain authority", wider than WARM's | The enforcement and mediation layer that compiles views and through which every material action must pass |
| Domain | An area of work defined by a charter | The application area of a deployment; also "failure domains" | A specialization's field; "review domain" |
| Role | A position with stated duties in a domain | A human entitlement role (portfolio manager) | Role Group: a fixed profile of authority across domains |
| Identity | A service that establishes who is acting | Principal identity (same as WARM) | Also "organizational identity = specialization × Role Group" |
| Session | The history and state of a stretch of an agent's work | Also a client session (L1) and a "signed session" token | A conversation context, to be kept out of the work record |
| Artifact | Anything an agent produces and stores | Something returned to the client | Only approved, promoted deliverables. Drafts live in Runtime as "candidate artifacts". |
| Knowledge | A group: Memory, Retrieval, Artifacts | Enterprise knowledge (L5), including memory | A reviewed store that includes skills, called "procedural memory" |
| Skill | Instructions, versioned in the Registry | "Tool and skill invocation": a callable capability | A reviewed entry in Knowledge |
| Workflow | A domain part | Control flow inside L3 | The Workflow Protocol, a non-agent platform module |
| Runtime | A group (Harness, Sessions, Tasks, Environments, Scheduling) | "Tool & Action Runtime" (L6), "agent runtime" (L3) | A layer and a store (volatile task state) |
| Supervisor / supervision | Not used | Not used | (1) a Role Group that observes with little authority to change; (2) an Erlang-style restart hierarchy. Two senses in one paper, and both differ from the everyday "manager". |
| Improvement | An Operations service that proposes changes | The name of L9, which also holds observability and evaluation | "Learn" |
| Persistent | A persistent agent | Persistent memory and knowledge | The persistent layer (records and templates) |
| Registry | A versioned catalog of definitions | A tool registry; an optional agent registry | "Registrar": an agent that maintains indexes |
| Policy | Rules on actions and stored data | "action policy" at L6; "provider policy" at L4 | Π, enforced outside inference (same as WARM) |

---

## Counts per source

| Source | Inventory items | Clean one-part fits | Strained fits | Spans | Guidance | Misfits |
|---|---|---|---|---|---|---|
| A: Yu et al. | 97 | 33 | 8 | 42 | 9 | 5 |
| B: Zhu | 78 | 13 | 15 | 37 | 9 | 4 |

The counts are not directly comparable with WARM's platform mapping. Here, groupings, interactions and composite modules are counted as items, and they span by construction. In A, 26 of the 44 capabilities fit one WARM part cleanly.

---

## What WARM might change

Each candidate gives its evidence and a confidence. "Two sources" means two independent papers, or one paper plus WARM's own earlier platform mapping.

| # | Candidate change | Evidence | Confidence |
|---|---|---|---|
| 1 | **Correct the prior-work paragraph about Zhu.** B's "resident" is a dormant specification that activates as a task's team lead, and B rejects long-lived actors ("not a permanently busy digital employee"). It is not WARM's persistent agent. | B §1, §3.2, §8 quotes in c4 | High (a factual correction) |
| 2 | **Correct "ten layers" for Yu et al.** The paper calls them "ten responsibilities" and "responsibility boundaries, not a processing pipeline", and never uses "layer". | A §I, §IV; term search [layer 0] | High (a factual correction) |
| 3 | **Add delegated, time-bound authority to Identity or Policy.** Authority propagated on behalf of a principal is scoped to a task, expires, is narrowed when passed to a sub-worker, and is checked again at execution time. | A I3, T2, VP6; B lease (Eq. 8), Laws L1 and L4 | High (two independent sources, both explicit; WARM's own contract list already names "delegation" as unspecified) |
| 4 | **State a separation-of-duties rule in Governance:** whoever requests or produces an action does not approve it. | A §V-A (approver "is not the submitter"), Table V probe; B §4 ("Operation cannot approve ... No agent controls the full chain") | High that both sources state it; medium that it belongs in the model rather than in domain rules |
| 5 | **Add an independent stop path:** stopping agents and revoking authority by a path that does not depend on the data plane. It could sit in Reliability, in Policy, or as a responsibility of its own. | B §3.5, §6.3, Fig. 3; WARM's own provisional rule for Messaging and Reliability agents | Medium (one source, but it extends a rule WARM already has) |
| 6 | **Give an event-distribution responsibility a home**, by widening Messaging to events between services or by stating that it is Infrastructure. | A NC36, VP12, T6, L7; WARM's platform mapping ("outbound events", not adopted) | Medium (two sources) |
| 7 | **Say in Policy that enforcement happens at the service that owns the resource**, and that a decision made at the boundary does not authorize the action. | A I3, R3, §V-A (L6 enforces entitlements on each call); B Prop. 2 ("A side channel ... invalidates the property") | Medium (WARM's point 1 implies this but does not assign it) |
| 8 | **Reword the Harness** from "carry out the tool calls" to "request tool calls, which Tools executes after its own checks". | A I1 and its probe (Table V) | Medium-low (a wording change; WARM's Tools already "mediates") |
| 9 | **Name authority over organizational state (privilege) as distinct from access**, and allow Approvals to be given by a designated role, not only a person (for example a reviewer agent, or a second key). | B Def. 3, Tbl 3, Tbl 5 (second key "from a distinct Reviewer, a deterministic control, or the human") | Low (one source; it conflicts with WARM's rule that approvals are a person's; a design choice for the author) |
| 10 | **Add lineage and approval status to Artifacts** (candidate or approved; produced from which inputs), so that a faulty artifact can be quarantined together with its descendants. | B Tbl 2, §6.1 (lineage quarantine), archival with a current pointer | Medium-low (one source, but the only prior-work counterpart of a service no mapped platform has) |
| 11 | **Give applicability conditions for each service**, for example "Messaging: when more than one agent works together", in the way A's variation points do. | A Table II, R10, §VI-A | Medium (a usable aid for "a system does not need all twenty-four") |
| 12 | **Place calling applications in the layer model** (outside the boundary, or under People as "requesters"). | A Fig. 2 "Enterprise apps", "API clients"; WARM's own "people and applications" under Channels | Medium-low |
| 13 | **Revisit tenancy** as part of Identity ("on whose behalf ... in which tenant") and Policy scoping. | A L2, I3, T2, NC08 (multi-tenant); WARM's platform mapping (tenancy from one platform, not adopted) | Low-medium (two sources) |
| 14 | **State whether evidence or state is authoritative** when one store serves Observability and Tasks. | B Tbl 2, Prop. 1 | Low (one source; probably belongs in a later paper on contracts) |
| 15 | **Say what authority a persistent agent holds between tasks.** B says none (dormancy). WARM is silent. | B Law L1 | Low-medium (one source, but a real gap) |
| 16 | **Name typed outcomes of a task beyond done**: blocked, escalated, flagged, halted, as results that Orchestration tracks. | B §6.3 (ASSIGN, BLOCK, REVIEW, FLAG, HALT), Eq. 14 | Low |
| 17 | **No change on the split of Memory and Retrieval, or of the four Runtime services.** A joins them, but gives no argument that would favor joining. | A L3, L5 | Low that WARM should change |
| 18 | **No change on domains or the Directory.** Neither source has them, which confirms WARM's claim of novelty for these two papers. It is not evidence that they are needed. | A.2, B.2 | Not a change |

### What in WARM the sources do not have

| WARM part | A | B |
|---|---|---|
| Domains layer; a domain as a charter | Absent | Absent |
| Directory of accountable domains | Absent (ownership only at design time) | Absent |
| Persistent agent (identity, memory, channel across tasks) | Absent | Rejected by design |
| Agent identity that persists through a change of definition | Absent | Contradicted (identity = specification × Role Group) |
| Scheduling by time | Absent | Absent |
| Artifacts as a versioned store | Absent | Present |
| Models as a mediating service | Present | Absent |
| Infrastructure and Providers layers | Present | Absent |
| Registry of agent definitions and skills, changed through Releases | Tools only | Partly (pool; skills in Knowledge) |
| Releases for agents and skills | Infrastructure only | Partly (reviewed changes) |
| Sessions as a service of its own | Folded into L3 | Demoted (records over sessions) |
| Improvement separate from Evaluation | Joined in L9 | Separate ("Learn") |
| The platform test ("works the same whatever the work is about") | Absent. A splits by ownership of decisions, information, control or effects (§III-B), a different test. | Absent. B splits by lifetime and write rule. |
| People in several relations (director, role-holder, requester, subject) | Users and approvers only | Principal only (goal, veto, kill) |
| Implementation as one relation at every layer | Partly (a traceability chain from source to component) | Absent |

## Limits of this mapping

- One rater, who had read WARM first. No second rater.
- A's 44 capabilities come from the authors' replication package, not the paper. The package's table and the paper's counts agree, but the paper's prose lists do not match the table one for one.
- Quotes were taken from text extracted from HTML and PDF. Mathematical symbols are given as they render, for example "p̂" and "γ".
- Assigning interactions and composite modules as spans raises the span counts by construction. The capability-level counts for A give the cleaner comparison.
