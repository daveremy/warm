---
title: "WARM v0.11 against four general platform models: AOS, Steinder and Franke, ASOC, EAAF"
date: 2026-11-11
author: sagan (subagent)
yardstick: warm-model-v0.11.md; v0.12 change list V1-V15 in synthesis.md
status: mapping, round 2 (platform models). Read-only analysis; no other file changed.
---

# WARM v0.11 against four general platform models

## Summary

Four published models were mapped onto WARM v0.11, item by item, and WARM was mapped back onto each. The v0.12 change list (V1 to V15) was treated as already in the model.

The main findings, stated as they cut:

1. **WARM has no owner for the existence of an agent.** Three of the four sources make a run-time agent lifecycle (create, start, suspend, migrate, revoke, end, clean up) a top-level component: AOS "Agent lifecycle" and AOS-0000 "Agent Lifecycle Manager", Steinder and Franke's first primitive "Agent lifecycle", and EAAF's "Agent Lifecycle Manager". AOS names "Orphaned agent" as its failure mode. WARM spreads the pieces over Identity, Sessions, Tasks, Orchestration and the planned V3, and no service knows which agents exist and who started each. v0.11 recorded "agent provisioning" from one platform and did not adopt it; this round adds three more sources. This is the strongest evidence so far that the 24 services miss a responsibility. It contradicts the v0.12 plan that "the service count stays 24".
2. **All four sources use a run-time assessment of risk, confidence or trust as an input to the decision whether an action proceeds.** WARM has Policy (decide) and Evaluation (judge work against criteria) but states no run-time assessment that Policy consumes. The gap is real; where it belongs is less clear (Evaluation widened, or a new Governance service).
3. **None of the four decompositions shows WARM's six groups cut in the wrong place.** Three cut on a different axis (decision versus execution: AOS planes, EAAF control plane, ASOC harness layer). ASOC's two cross-cutting planes, "Governance and Observability" and "Security and Trust", are close to WARM's two cross-cutting groups. EAAF's cut duplicates components across layers and its control plane, and mixes channels for people with tool actions; WARM's placement test resolves those mixes.
4. **Artifacts has no full counterpart in any of the four.** Steinder and Franke argue that it needs none: "POSIX file systems still store agent-produced artifacts." With the three platforms of v0.11, the count is 0 of 7.
5. **No source has domains or a directory of accountability.** Only fragments exist (AOS routes approvals "to an accountable role"; EAAF lists use cases by business area), as with the three platforms. EAAF takes the opposite approach: "agents negotiate responsibilities".

Counts, misfits and candidate changes are in the sections "Counts" and "What WARM might change".

## What was read, and how

All primaries were opened and read as text on 2026-11-11. Nothing below is UNVERIFIED unless marked.

| Source | What was read | How |
|---|---|---|
| A. AOS-0001, Sharma and Shah, arXiv:2608.03214 (draft v0.8, 2026-08-04) | The whole PDF, 72 pages, including the appendices and the references | PDF to text with PyMuPDF, read in full; Figure 4 viewed as an image |
| A. AOS-0000, Sharma and Shah, arXiv:2606.01508 (2026-06-01) | The whole PDF, 24 pages | PDF to text with PyMuPDF; sections 1 to 6 and 8 to 11 read in full, section 7 (Linux and Windows subsystem tables) read in full in compact form |
| B. Steinder and Franke (IBM), arXiv:2607.25076 (2026-07-27) | The whole arXiv HTML except the reference list | HTML to text with lynx; Figure 2 (rossoctl architecture) viewed as an image |
| C. ASOC manifesto, Beheshti et al., arXiv:2607.12619 (2026-07-14) | The whole arXiv HTML except the reference list | HTML to text with lynx; Figure 1 (the ASOC stack) viewed as an image, because the layer contents exist only in the figure |
| D. EAAF, Venkiteela, Sci. J. Comput. Sci. 2(1), 2026, doi:10.64539/sjcs.v2i1.2026.368 | The whole PDF, 17 pages, except the reference list | Journal PDF to text with pypdf; Figures 1 and 9 viewed as images |

Corrections to the search notes in `search.md`:

- **AOS-0001 has 72 pages, not 199.** The search note says "199-page PDF, sections read". The `file` utility reports 199 pages for this PDF; pypdf and PyMuPDF both count 72, and the text ends at page 72 with reference [66]. This mapping read all 72.
- **The IBM paper's venue (IEEE ICWS 2026) is not stated** in the arXiv HTML or on the arXiv abstract page. It comes from the search note and is unverified here.
- **Internal inconsistencies in the sources**, recorded so that nobody re-derives them: AOS-0001's Table 7 lists seven runtime responsibilities and omits "protocol mediation", which its executive summary and §10.9 include; its Figure 4 shows five control boxes plus "Governance Services (Policy Engine, Trust Manager, Decision Engine, Quotas, Compliance)" and six runtime boxes, which do not match Tables 6 and 7. Steinder and Franke's Table I lists "Saga & checkpoint" and "AI-aware proxy" while its thirteen subsections include "Secure Code Execution" and no saga section, so the paper names fourteen distinct primitives. EAAF's figures appear to be machine-generated: labels are garbled ("Governation & Safety Layer", "Orcheration & Coodration Layer", "Telemenry"), the Governance and Safety layer appears twice in Figure 1, the Agent Intelligence layer appears twice in Figure 9, and the control-plane figure is captioned "Figure 9" in the image and "Figure 7" in the text.

Inventory rules. Every named layer, plane, component, primitive, responsibility, registry, object and rule was listed with a short verbatim quote. Each item got exactly one category: **Clean** or **Strained** (one WARM service, layer, domain part, agent concept or the Directory), **Span** (several WARM parts, named), **Guidance** (design-time guidance, including principles and rules), **Planned** (already in V1 to V15), or **Misfit**. A doubtful fit was called a misfit. Items that repeat an earlier item under another name (an interface object that carries a concept already listed) are marked **Folded** and are not counted; the row says which item it repeats.

## Adoption evidence (read 2026-11-11)

| Source | Citations (OpenAlex `cited_by_count`) | Implementation and adopters |
|---|---|---|
| AOS-0001 | 0 | Names "aos-core" as "an evolving reference implementation" with an example conformance statement ("Profile: Embedded Control (experimental)"). A GitHub search for `aos-core` found no matching repository. Acknowledges the Open Compute Project "Unified Intelligent Infrastructure workstream". AOS-0002 to AOS-0010 are "Planned; not yet published". No named adopter. |
| AOS-0000 | 3, of which one is AOS-0001 (self-citation); the other two are "XChronos OS as a Temporal-operating Layer" (Souza Silva) and "Ring-0 by Default: Agents as Operating Systems (AaOS)" (Li, Huang, Xu) | None beyond AOS-0001 |
| Steinder and Franke | 0 | Prototype `rossoctl/rossoctl`: 304 stars, 109 forks, created 2025-03-27, last push 2026-11-07 (GitHub API). The paper states rossoctl implements "a subset" of the primitives. Venue per search note: IEEE ICWS 2026 (unverified). No named adopter. |
| ASOC | 0 | "manifesto", no implementation. Ten senior service-computing authors; points to "the inaugural 2026 IEEE Symposium on Agentic Services" and ICAgentS 2027. No named adopter. |
| EAAF | 19 | No implementation released and no named adopter. The 19 citing works are all from 2026; most appear in multidisciplinary journals, and several are on unrelated subjects (digital twins for smart cities, personalized learning, intrusion detection). The paper's evaluation reports figures (for example "EAAF (Agents) 95% 82% 1-2 min") with no description of the systems, samples or method. My inference: the citation count overstates its standing as a reference model. |

---

## Source A. AOS-0001 and AOS-0000 (Sharma and Shah)

### A.1 Inventory and assignment

Section numbers are AOS-0001's unless marked "AOS-0000".

**Top level**

| # | Item | Definition (verbatim, where) | Assignment | Cat |
|---|---|---|---|---|
| A01 | Agent Operating System (the AOS boundary) | "a vendor-neutral reference operating architecture for distributed agentic systems. AOS contains two internal planes" (Abstract) | Platform layer. Strained: the boundary excludes identity providers, secrets, message brokers, observability backends and model hosting, which WARM's Platform holds as services (see A04) | Strained |
| A02 | Control & Governance Plane | "responsible for intent, policy, trust, authority, confidence, auditability, observability, and human oversight" (Abstract); "converts an objective into an authorized execution directive" (§9.1) | Span: Policy, Approvals, Identity (authority), Observability, Registry (discovery), plus intent and confidence, which have no home (A07, A10) | Span |
| A03 | Runtime & Coordination Plane | "responsible for agent lifecycle, workflow coordination, model and tool routing, context and memory coordination, scheduling, traffic management, and runtime assurance" (Abstract) | Span: Runtime group (Harness, Tasks, Scheduling, Environments), Models, Tools, Orchestration, Memory, Reliability, plus agent lifecycle (A14) | Span |
| A04 | External platform services | "model-serving endpoints, retrieval and vector systems, data stores, knowledge graphs, identity providers, secrets, policy decision points such as Open Policy Agent [22], message brokers, observability backends, API gateways, and enterprise connectors" (§8.5) | Span: implementations of WARM's Models, Retrieval, Identity, Secrets, Policy, Messaging, Observability, Tools, plus Providers and Infrastructure. AOS calls them external; WARM calls the responsibilities platform services and these the components that implement them (Step 5) | Span |
| A05 | Conventional operating systems | "Linux, Windows, hypervisors, and container runtimes manage local processes, filesystems, memory, sockets, credentials, devices, and isolation" (§8.6) | Infrastructure | Clean |
| A06 | Infrastructure | Figure 4: "Compute", "Memory", "Network", "Storage", "Locations", "Power & Cooling" | Infrastructure | Clean |

**Control & Governance Plane responsibilities (Table 6)**

| # | Item | Definition | Assignment | Cat |
|---|---|---|---|---|
| A07 | Intent management | Output "Normalized IntentEnvelope"; ingestion "validates the actor, authority source, objective, constraints, context references, success criteria, and temporal requirements" (§9.2); "The original intent is immutable; revised interpretations or plans are versioned" (§6.2); Intent "I={G,C,A,Π,X,S,T}" | No WARM part holds a per-request objective with its constraints, authority reference and success criteria. Channels carries the request, Tasks tracks the unit of work, acceptance criteria are per domain, not per request. V9 routes an inbound request but does not normalize it or record success criteria | Misfit |
| A08 | Capability discovery | Output "Feasible provider set and ranking evidence"; "Feasibility precedes ranking" (§9.3) | Span: Registry (lookup), Policy (hard constraints), Models (choose among providers by fit, cost, latency). AOS ranks agents, models, tools, workflows and humans in one selection; WARM has model choice only in Models | Span |
| A09 | Policy and trust | Output "Allow, deny, modify, approve, and obligations" (Table 6); "Policy evaluation combines the intent, actor, capability, provider, context, risk class, and current system state" (§9.4) | Span: Policy (decisions and obligations; obligations partly V1) and Approvals (the "approve" outcome); the trust half has no home (A27) | Span |
| A10 | Confidence and risk | Output "ConfidenceDecision and required action"; "Confidence is operational only when it changes behavior" (§7.5); actions "PROCEED ... PROCEED_WITH_WARNING ... RETRY ... FALLBACK ... ESCALATE ... TERMINATE" (Table 13); "Risk(a)=Pr(H∣e,x,a)·Impact(H)·Exposure(a)" (§12.8) | No WARM service holds a run-time assurance state that changes control flow. Evaluation judges against criteria; Policy decides on rules; neither is stated to consume or produce a confidence or risk value during a task | Misfit |
| A11 | Delegation governance | Output "Bounded DelegationContext"; "Downstream delegation can only narrow this context unless an independent authority participates" (§9.7); "Child scope cannot exceed parent scope ... Child expiry cannot exceed parent expiry ... Child budgets cannot exceed remaining parent budgets" (§6.9) | Already planned: V1 (scoped, time-limited, revocable grants) and V2 (no agent grants itself authority). Residual not in V1 or V2: the narrowing rule along a chain, including budgets | Planned |
| A12 | Audit and observability | Output "Semantic events and evidence requirements"; "The control plane determines what evidence the runtime must emit" (§9.8); "Audit is not identical to logs" | Observability. Strained: setting the evidence required by risk is a Policy decision | Strained |
| A13 | Human oversight | Output "Approval, exception, escalation, or stop decision"; "routes each request to an accountable role rather than a generic 'human'" (§9.9) | Approvals. Strained: "stop" is V3; clarification, exception handling and appeal are wider than "hold chosen actions until a person authorizes them"; routing to an accountable role touches the Directory | Strained |

**Runtime & Coordination Plane responsibilities (Table 7 and §10)**

| # | Item | Definition | Assignment | Cat |
|---|---|---|---|---|
| A14 | Agent lifecycle | State "Created, active, paused, migrated, revoked, terminated"; failure "Orphaned agent, duplicate execution, failed revocation" (Table 7); "create, initialize, activate, pause, resume, quiesce, migrate, revoke, terminate, and garbage-collect. The managed object may be a persistent agent identity or a transient runtime instance" (§10.2). AOS-0000 §4.2 "Agent Lifecycle Manager": "maintains durable agent identifiers, capability grants and revocations, context store pointers ... and deterministic termination semantics" | No WARM service owns the existence of an agent. Pieces sit in Identity (who), V3 (suspend, revoke), Sessions (pause, resume), Tasks (a unit of work, not an agent), Orchestration ("the platform starts one"). Nothing records which agents exist, who started each, or cleans them up | Misfit |
| A15 | Workflow coordination | State "Plan-step and dependency state"; "manages dependencies, checkpoints, retries, compensation, timeouts, human tasks, and partial results" (§10.3) | Span: Orchestration (dependencies, results) and Tasks (retry, recovery); compensation is V14 | Span |
| A16 | Model and tool routing | "Routing binds a capability to a provider and protocol"; "Human providers are routed similarly" (§10.4) | Span: Models, Tools; human providers through Approvals and Channels | Span |
| A17 | Context and memory coordination | "Context coordination builds the bounded input for each runtime step"; "Memory coordination manages access to episodic, semantic, procedural, and artifact memory" (§10.5) | Span: Harness (context), Memory, Retrieval. Note: AOS keeps procedural memory in memory, the placement v0.11 reversed | Span |
| A18 | Scheduling | "allocates queues, concurrency, token budgets, model capacity, accelerators, regions, human review slots, and deadlines" (§10.6) | Scheduling. Clean, with one excess: placement by region, which no WARM service names | Clean |
| A19 | Traffic management | "routes, load balancing, retries, rate limits, circuit breakers, backpressure, and cross-region fallback"; "enforces fan-out, depth, token, time, and cost budgets" (§10.7) | Span: Scheduling (rate limits), Tasks (retries), Reliability (circuit breakers, failover), Policy (budgets) | Span |
| A20 | Runtime assurance | "observes whether execution remains within the authorized envelope ... Responses include allow, warn, throttle, isolate, cancel, fallback, escalate, or terminate" (§10.8) | Span: Policy at enforcement points (Governance point 1), Environments (isolate), Tasks (cancel), Reliability, Observability | Span |
| A21 | Protocol mediation | "maps canonical AOS objects to external protocols"; "The adapter does not own policy" (§10.9) | Span: Tools, Messaging, Channels | Span |

**Foundational concepts (§6)**

| # | Item | Definition | Assignment | Cat |
|---|---|---|---|---|
| — | Intent | §6.2 | Repeats A07 | Folded |
| A22 | Identity and Authority | "Identity establishes who or what an actor is; Authority establishes what that actor may request, approve, delegate, or execute"; "Authority is explicit, scoped, time-bounded, and revocable" (§6.8) | Identity for the first half; the authority half is V1 grants | Planned |
| A23 | Context | "the bounded operational state made available to a decision or execution step ... Context is not identical to memory" (§6.3) | Harness ("decide what goes into the context window") | Clean |
| A24 | Capability | "a stable, discoverable description of what an actor or system can perform ... may be provided by an agent, model, tool, API, workflow, human, service, or infrastructure function" (§6.4) | Registry. Strained: WARM's Registry holds definitions of agents, tools and skills, not outcome contracts that a human or a workflow may fill | Strained |
| A25 | Provider | "a concrete implementation that realizes one or more capabilities" (§6.5) | Span: a Registry entry for an agent, model, tool or workflow, or a person through Approvals. Term clash with WARM's Providers layer (section A.4) | Span |
| A26 | Plan | "a bounded and reviewable decomposition of an intent into steps, dependencies, candidate capabilities, checkpoints, and failure actions. A plan is not authorization to execute" (§6.6) | Span: Orchestration (what depends on what), Tasks (records actual execution separately). Single-agent planning is out of WARM's scope; a plan held as a versioned record is not | Span |
| — | Policy (object) | "a machine-evaluable rule or rule set that determines eligibility, constraints, obligations, approvals, and response actions" (§6.7) | Repeats A09 (Policy) | Folded |
| — | Delegation (object) | §6.9 | Repeats A11 | Folded |
| A27 | Trust | "an evaluated relationship describing the degree to which an actor, provider, artifact, or environment is acceptable for a particular intent and policy context ... Trust may decay when evidence becomes stale" (§6.10). AOS-0000 §4.6: "deterministic trust and risk states such as normal, restricted, quarantined, and reviewed" | No WARM part keeps a standing, decaying assessment of an actor or provider. Identity says who; Evaluation judges work; Policy decides. Same family as A10 | Misfit |
| — | Confidence (object) | §6.11 | Repeats A10 | Folded |
| A28 | Evidence and Provenance | "the set of observable artifacts used to justify and reconstruct a control or execution decision" (§6.12) | Observability | Clean |
| A29 | Execution | "the realization of an authorized intent ... has a unique identifier and monotonically recorded lifecycle ... may branch, retry, compensate, fall back, escalate, or terminate" (§6.13) | Tasks | Clean |
| A30 | Semantic resource model | "an authority budget, token budget, context window, model quota, human-approval capacity, data residency allowance, trust relationship, confidence threshold, evidence-retention budget, and time-to-decision" (§6.14) | Span: Scheduling (capacity), Policy (budgets, residency), Models (quota), Approvals (human capacity). WARM treats cost as a concern, not a resource | Span |

**Other named components, registries and interfaces**

| # | Item | Definition | Assignment | Cat |
|---|---|---|---|---|
| A31 | Capability registry | "The registry interface supports registration, update, revocation, lookup, subscription, health, and federation ... A capability advertisement is not a trust guarantee" (§11.4) | Registry. Validation before use is V6 | Clean |
| A32 | Semantic event model | "AOS events use stable semantic names independent of logging backend" (§11.7, Table 10) | Observability (events to subscribers are V11) | Clean |
| A33 | Humans as capability providers | "Treating humans as capability providers avoids embedding approval logic into every workflow" (§10.4); "Their availability, expertise, workload, and response time are schedulable resources" (§15.6) | Span: Approvals, Channels, Scheduling. WARM has people fill roles; AOS routes a person like any other provider | Span |
| — | Canonical objects (§11.2): IntentEnvelope, CapabilityQuery, CapabilityManifest, PolicyDecision, TrustDecision, DelegationContext, ExecutionDirective, ExecutionEvent, ConfidenceRecord, ExecutionResult, AuditEvent | Table 9 | Each carries a concept above (A07, A31, A24, A09, A27, A11, A29, A32, A10, A29, A12) | Folded |
| — | Service provider interfaces (§11.6): CapabilityProvider, CapabilityRegistry, IntentNormalizer, PolicyEvaluator, TrustEvaluator, ConfidenceEvaluator, DelegationContextProvider, ExecutionAdapter, RuntimeScheduler, TrafficManager, ContextProvider, MemoryProvider, AuditSink, ObservabilitySink, HumanApprovalProvider | §11.6 | Interfaces for the items above | Folded |
| A34 | ExecutionDirective as the plane boundary | "a bounded contract between the planes. The runtime may optimize within the declared freedom ... but it cannot relax obligations or expand authority" (§11.5); "Plane 1 invariant ... MUST NOT assert that the work has occurred or succeeded" (§9.10); "Plane 2 invariant ... MUST NOT expand authority" (§10.10) | Span: Policy (the decision, V1 grant) handed to Tasks and the Harness (the execution) | Span |
| A35 | Four states and reconciliation | "intended state, authorized state, observed state, and resulting state. ... AOS controllers reconcile these states" (§8.7) | Design-time guidance | Guidance |
| A36 | Failure contracts | "Every interface declares failure classes rather than returning only generic errors" (§11.11) | Guidance; WARM's open "contract" question (Step 3) | Guidance |
| A37 | Conformance levels and profiles | "AOS-aware ... AOS-compatible ... AOS-conformant profile ... AOS reference implementation" (Table 8); profiles Embedded Control to High Assurance (Appendix E) | Guidance; WARM Limit 4 says conformance is open | Guidance |
| A38 | Deployment profiles | "embedded library, a central service, a regional control domain, a federated global system, an edge hierarchy, or a sovereign isolated deployment" (§13.1) | Guidance; WARM layers are "not a deployment diagram" | Guidance |
| A39 | Reliability dimensions and loop | Table 14 (functional, availability, performance, data and context, robustness, model stability, safety, security, explainability, fairness, agentic, economic); §14.11 six-step loop | Guidance (touches Reliability, Evaluation, Observability) | Guidance |
| A40 | Threat model | Appendix D, twelve threats with controls | Guidance | Guidance |
| A41 | Mathematical model | §12, equations (1) to (18) | Guidance | Guidance |
| A42 | Architecture invariants INV-001 to INV-010 | "Execution MUST NOT occur without an originating intent ..." to "A conforming implementation MUST declare unsupported responsibilities and external dependencies" (Table 16) | Guidance. INV-002 matches Governance point 1; INV-004 is the residual of A11; INV-010 matches WARM Step 5 ("An entry may be left unresolved") | Guidance |
| A43 | AOS domain | "An administrative and trust boundary operating one or more AOS components" (Glossary); federation across domains (§13.5) | WARM describes one system. Cross-organization federation is out of its scope; V12 tenancy is several organizations on one platform, not several platforms | Misfit |
| A44 | Agent (glossary) | "A goal-directed computational actor that can reason, plan, invoke capabilities, and maintain state" | WARM agent concept. Strained: no role, no kind | Strained |
| A45 | Actor (glossary) | "A human, agent, service, device, organization, or runtime identity participating in AOS" | Identity ("each agent, person and service") | Clean |

**Design principles (§7), each counted**

| # | Principle (verbatim title and gist) | Assignment | Cat |
|---|---|---|---|
| A46 | 7.1 "Separation of Control and Execution": "the decision record, execution directive, and observed action remain separate objects" | Guidance. WARM keeps decide and enforce in Policy (V1 leaves the split to an implementation) | Guidance |
| A47 | 7.2 "Capability-Centric Abstraction": "Applications request capabilities instead of binding directly to agents, models, or vendors" | Guidance | Guidance |
| A48 | 7.3 "Authority Preservation and Least Delegation": "The architecture rejects implicit authority expansion through nested agent calls, tool adapters, or asynchronous queues" | Guidance; supports the residual of A11 | Guidance |
| A49 | 7.4 "Deterministic Enforcement Around Probabilistic Reasoning" | Guidance; same as Governance point 1 | Guidance |
| A50 | 7.5 "Confidence as a Control Signal" | Guidance; supports A10 | Guidance |
| A51 | 7.6 "Observability by Construction" | Guidance | Guidance |
| A52 | 7.7 "Explicit State and Legal Transitions" | Guidance; the Tasks contract | Guidance |
| A53 | 7.8 "Runtime, Model, Cloud, and Operating-System Agnosticism" | Guidance | Guidance |
| A54 | 7.9 "Federation over Global Monoliths" | Guidance (out of WARM's single-system scope) | Guidance |
| A55 | 7.10 "Reliability as an End-to-End Property" | Guidance | Guidance |
| A56 | 7.11 "Human Governability and Exception Handling": "approval before action, supervisory review, emergency stop, post-action review, and dispute resolution" | Guidance; supports A13 | Guidance |
| A57 | 7.12 "Economic and Physical Awareness" | Guidance; WARM's cost concern | Guidance |

**AOS-0000 items not already listed**

| # | Item | Definition (AOS-0000) | Assignment | Cat |
|---|---|---|---|---|
| — | Agent Lifecycle Manager (§4.2) | quoted under A14 | Repeats A14 | Folded |
| A58 | Agent Scheduler (§4.3) | "AOS scheduling must optimize goal progress subject to policy, risk, and budget constraints"; outputs "when to require human approval, and when to throttle, suspend, or quarantine an agent" | Span: Scheduling, Approvals, V3 (suspend) | Span |
| A59 | Context and Memory Management (§4.4) | "Ephemeral context ... Durable agent memory ... Retrieved knowledge ... Execution records" | Span: Harness, Memory, Retrieval, Sessions and Observability. Close to WARM's "Where what an agent knows is kept" | Span |
| A60 | Tool and Capability Registry (§4.5) | "a privileged admission and classification mechanism that binds dynamically discovered tools to capability scopes, mediation requirements, and audit policies before use"; a tool definition includes "side effect classification" | V6 (registration is a gate). The side-effect classification is not in V6 | Planned |
| A61 | Layered policy (§4.6) | "Static authorization ... Capability constraints ... Context policy ... Risk policy ... Governance policy introduces approvals, dual control, and escalation" | Policy | Clean |
| — | Trust and risk states (§4.6) | quoted under A27 | Repeats A27 | Folded |
| — | Observability and Audit (§4.7) | "AOS observability must combine system metrics with decision lineage" | Repeats A12 | Folded |
| A62 | Reasoning plane (§3.3) | "performs probabilistic inference, planning, and strategy selection ... must be treated as untrusted with respect to policy" | Span: Harness, Models; single-agent planning out of scope | Span |
| A63 | Execution plane (§3.3) | "performs deterministic tool invocation, system calls, and side effects" | Span: Tools, Environments | Span |
| A64 | Policy plane (§3.3) | "performs authorization, risk checks, compliance constraints, and budget controls" | Span: Policy, Approvals; risk checks have no home (A10) | Span |
| A65 | First-class entities (§3.2) | "agent identity, goal and task graphs, capability sets, context state, and execution records" | Span: Identity, Orchestration and Tasks, V1 (here "capability" means a permission set), Harness, Observability | Span |
| A66 | Trusted Computing Base (§3.4) | "the policy engine, capability validation pipeline, mediation layer, execution sandbox controls, audit subsystem, and deterministic state management mechanisms" | Guidance | Guidance |
| A67 | Determinism at the boundary (§3.5) | "AOS can tolerate nondeterminism inside reasoning. It cannot tolerate nondeterminism in enforcement" | Guidance (Governance point 1) | Guidance |
| A68 | Integration models (§5) | "User-space Runtime", "OS Extension", "Distributed Control Plane", "Subsuming Parts of the OS" | Guidance | Guidance |
| A69 | Bounded autonomy levels (§8.6) | "Read only ... Low risk ... Controlled ... High impact. Actions require approvals or dual control" | Guidance; a classification that a domain's rules would set in Policy | Guidance |

### A.2 Reverse direction: WARM in AOS

See the combined reverse table in section "Reverse direction, all four sources".

### A.3 Findings for AOS

**(a) Misfits and spans**

| Item | Kind | What it suggests about WARM |
|---|---|---|
| A07 Intent management | Misfit | A gap in the Tasks contract, not a new service: a task should keep the original request (objective, constraints, authority reference, success criteria) unchanged, with later interpretations versioned. V9 covers routing an unaddressed request; it does not cover this. |
| A10 Confidence and risk | Misfit | A missing responsibility: a run-time assessment that Policy uses. Candidate placement: widen Evaluation to assess before and during an action, not only after, and state that a Policy decision may take that assessment as input. |
| A14 Agent lifecycle | Misfit | A missing service, or Identity and Tasks under-scoped. See "What WARM might change", change 1. |
| A27 Trust | Misfit | Same family as A10. A standing, evidence-based assessment of an actor or provider. If WARM widens Evaluation (change 2), trust is a stored Evaluation result that Policy reads. |
| A43 AOS domain | Misfit | Nothing: out of scope, because WARM describes one system. Say so in Step 1. |
| A02, A03 planes | Span | A different cut (decision versus execution), not a wrong one. See (b). |
| A04 External platform services | Span | AOS places mechanisms outside its boundary; WARM places the responsibilities inside the platform and lets components implement them. Compatible with WARM Step 5. Nothing to change. |
| A08 Capability discovery, A16 routing, A25 Provider, A33 humans as providers | Span | AOS selects among agents, models, tools, workflows and people in one ranked choice. WARM chooses models in Models and reaches roles through the Directory, and has no place for "pick the best provider of this outcome". Weak evidence for widening Models to "choose the provider" or for nothing; WARM's Directory routes by accountability, which is a different rule. |
| A19 Traffic management, A20 Runtime assurance | Span | Each bundles enforcement-point duties (budgets, circuit breakers, isolation, cancel). They confirm Governance point 1 and point to the budget mechanics in change 4. |
| A30 Semantic resource model | Span | Supports change 4 (budgets as delegated quantities). |
| A15, A17, A21, A26, A34, A58, A59, A62 to A65 | Span | Clean spans; nothing to change. A17 keeps procedural memory in Memory; WARM v0.11 moved skills to the Registry, and AOS gives no argument against that move. |

**(b) Top-level cut compared**

| AOS part | WARM groups and layers it covers |
|---|---|
| Control & Governance Plane: Intent management | Interaction (Channels) and Runtime (Tasks), partly; per-request success criteria have no home |
| Capability discovery | Capabilities (Registry, Models) |
| Policy and trust | Governance (Policy) |
| Confidence and risk | none (Operations: Evaluation, partly) |
| Delegation governance | Governance (Identity, Policy; V1, V2) |
| Audit and observability | Operations (Observability) |
| Human oversight | Governance (Approvals; V3) |
| Runtime & Coordination Plane: Agent lifecycle | none (Governance: Identity; Runtime: Sessions, Tasks, partly) |
| Workflow coordination | Interaction (Orchestration), Runtime (Tasks) |
| Model and tool routing | Capabilities (Models, Tools) |
| Context and memory coordination | Runtime (Harness), Knowledge (Memory, Retrieval) |
| Scheduling | Runtime (Scheduling) |
| Traffic management | Runtime (Scheduling, Tasks), Operations (Reliability) |
| Runtime assurance | Governance (Policy enforcement), Runtime (Environments), Operations (Reliability) |
| External platform services | Platform implementations of Capabilities, Knowledge, Governance, Interaction, Operations; Providers |
| Conventional OS; Infrastructure | Infrastructure |
| (absent) | People layer (humans are actors and approvers only), Domains layer, Directory, Artifacts, Improvement, Releases, Channels as a service |

Where AOS cuts differently: by who owns which state. Plane 1 owns "authoritative intent, policy decisions, trust evaluations, delegation grants, confidence actions, audit obligations, and human-control requirements"; Plane 2 owns "active execution state, provider bindings, runtime queues, workflow progress, context delivery, scheduling decisions, traffic state, and assurance responses" (§8.2). WARM cuts by the question a service answers.

Does the AOS cut look better? For one purpose, yes: it gives the decision record a single owner and makes "authorized" and "done" separate claims, with two invariants that state it. WARM keeps both in Policy and Tasks without a stated invariant between them. For WARM's purposes (naming parts so that a growing system can be described and compared), the AOS cut is worse: it hides Identity, Secrets, Messaging and Observability behind "external" and has no place for people, domains, artifacts, improvement or releases. My inference: the decision-versus-execution split is worth stating inside WARM as a property of Governance (one sentence under V1), not worth adopting as the top-level cut.

**(c) Identity, definition, instance**

AOS states: "The managed object may be a persistent agent identity or a transient runtime instance. AOS distinguishes identity from instance so that an agent can migrate or restart without losing authority and audit continuity" (§10.2). AOS-0000: "the process is only one component of the overall lifecycle and may be restarted or migrated while the agent identity persists" (§2.1), and agents "may remain resident for days or weeks".

AOS has no agent definition. The nearest are the CapabilityManifest (a contract for an outcome) and a provider's "versioned implementation". Its example identities carry versions ("planner-agent-v3", "summary-agent-v1", Appendix A.3), which suggests (my inference) that a new version is a new identity, the opposite of WARM's rule that identity persists through a change of definition.

Against WARM Step 0: **a different distinction, and on one point a more precise one.** WARM separates definition from agent, and persistent agents from task agents by lifetime. AOS separates identity from the running instance (process, container) and says nothing about lifetime across tasks: its "transient runtime instance" is the process that carries an identity, not WARM's task agent, which has an identity of its own. WARM does not name the running instance at all; a persistent agent in WARM can be restarted, moved or run in several sessions, and the model gives no word for the thing that is restarted. AOS's identity/instance split is a precise addition WARM could take.

**(d) Cost, conflict, sprawl, confidence**

| Theme | What AOS does | Where it would belong in WARM |
|---|---|---|
| Cost | The most developed of the four. Cost profile per capability; cost in provider ranking (§12.4); "C_total = C_model + C_tool + C_data + C_network + C_human + C_control" (§12.11); "AOS budgets can be allocated per intent and delegated monotonically to children" (§12.11); traffic management "enforces fan-out, depth, token, time, and cost budgets" (§10.7); "Economic reliability" (§14.10) | Budgets carried in a V1 grant and narrowed along a delegation (change 3, 4); enforced by Scheduling; metered by Observability; model choice in Models. Cost stays a concern, not a service |
| Conflict | Policy conflicts: "the final decision to identify the applicable policy versions and the conflict-resolution rule" (§9.4); federated policy conflict is open (§15.10); contradictory memory "not averaged silently; the system preserves version history and applies a resolution rule or requests clarification" (§14.6); humans "resolve conflicting evidence" (§15.6). AOS-0000: "policy arbitration across cooperating agents remain open research problems". No mechanism for conflicting outputs of two agents | Rule precedence in Policy (change 9); memory contradictions already in Memory ("revises or retires entries that later evidence contradicts"); conflicting agent outputs: Orchestration collects, the accountable domain decides, Approvals if a person must |
| Sprawl | "Orphaned agent" is the representative failure of agent lifecycle (Table 7); lifecycle includes "garbage-collect" (§10.2); "registry spam" is open (§16.2) | Needs the agent lifecycle responsibility (change 1); unregistered agents are V6 |
| Confidence or risk | Central: Confidence object, ConfidenceDecision, six control actions, risk equation, trust (§6.10, §6.11, §9.6, §12.7, §12.8) | Change 2 |

**(e) Same word, different thing**

| Word | AOS | WARM |
|---|---|---|
| Provider | "a concrete implementation that realizes one or more capabilities"; may be internal or a human | The layer of outside sources the platform calls and does not operate |
| Platform services | External dependencies outside AOS: identity providers, secrets, brokers, observability backends | The 24 services of the platform layer, inside the system |
| Capability | AOS-0001: "a stable contract describing an outcome that a provider can realize"; AOS-0000: "Capability sets define which tools and actions are allowed" (a permission set). AOS uses the word two ways across its two papers | A group: "What can agents use?" (Models, Tools, Registry) |
| Domain | "An administrative and trust boundary" | An area of work defined by a charter |
| Registry | Catalog of capabilities and providers with trust, cost, latency and health | Versioned definitions of agents, tools and skills |
| Control plane | Decisions only; "MUST NOT assert that the work has occurred" | WARM has no plane; Governance and Operations are cross-cutting groups |
| Memory | Includes procedural memory | Facts and events; skills are in the Registry |
| Workflow | A kind of provider, and runtime coordination of a plan | A part of a domain's charter |

---

## Source B. Steinder and Franke, "Towards an Agent Operating System" (IBM)

### B.1 Inventory and assignment

| # | Item | Definition (verbatim, where) | Assignment | Cat |
|---|---|---|---|---|
| B01 | Agent-OS | "infrastructure: the platform layer beneath agent applications that enforces the guarantees those applications depend on" (§II-1) | Platform layer | Clean |
| B02 | Memory (State), in the Autonomous Agent Paradigm | "short-term context window ... and long-term stores" (§II-2) | Span: Harness (context window), Memory | Span |
| B03 | Planning (Reasoning) | "the agent's capacity to decompose a goal into a sequence of steps ... an emergent capability of the LLM" (§II-2) | Out of WARM's scope (Step 0: "WARM does not describe how a single agent reasons"). Suggests nothing | Misfit |
| B04 | Action (Tools) | "the means by which the agent affects the external world" (§II-2) | Tools | Clean |
| B05 | Perception (Inputs) | "the ingestion of environmental state: user messages, tool results, retrieved memory, sensor data, and outputs from peer agents, all competing for the finite context budget" (§II-2) | Harness | Clean |
| B06 | Agent lifecycle (primitive) | "An agent is an isolated execution context (container/pod) with an LLM session, tool credentials, context buffer, and memory state. It may be created, run ..., terminated. Agents spawn sub-agents (fork/exec analog) through platform-mediated channels. Agent identity must be a function of its Cloud-OS identity and agent-level properties like goal, skills, tools, model, or context" (§IV-A) | No WARM service owns creating and ending agents (as A14). The identity clause contradicts WARM Step 0 (section B.3 c) | Misfit |
| B07 | Orchestrator (Orchestration and Scheduling) | "manage agent topologies, message-passing infrastructure, and lifecycle, extended with token-budget quotas, semantic loop detection, and multi-dimensional cost accounting" (§IV-B) | Span: Orchestration, Scheduling (quotas), Messaging, Observability (cost accounting), Evaluation (loop detection) | Span |
| B08 | Skills registry | "Skills are self-contained SKILL.md instruction files, loaded on demand ... The Agent-OS requires a semantic SBOM: provenance declaring a skill's domain, model compatibility, and callable tools, enforced at load time" (§IV-C) | Registry; enforcement at load is V6 | Clean |
| B09 | Tool mediation | "MCP Gateways aggregate, route, and enforce authorization with a reversibility model that blocks irreversible calls without elevated authorization" (§IV-D) | Tools (enforcement point for Policy) | Clean |
| B10 | Context management | "the set of techniques for deciding what information occupies the model's context window at any given moment" (§IV-E) | Harness | Clean |
| B11 | A2A communication | "mediate information passing and task delegation ... with platform-level semantic inspection of messages before delivery to guard against injection" (§IV-F) | Messaging (inspection is a Policy content check, V5) | Clean |
| B12 | Agent memory | "platform-enforced memory functions with audit"; open: "semantic conflict detection", "record-level access control", "intent-aware retrieval" (§IV-G) | Memory | Clean |
| B13 | Identity & AuthZ | "SPIFFE provides a viable substrate for agent identity ... fine-grained (e.g., per function) and context-dependent (based on what the agent is doing or has done before) policy enforcement" (§IV-H) | Span: Identity, Policy (context-dependent grants are V1) | Span |
| B14 | Behavioral guardrails | "platform-level behavioral constraints the agent cannot override: blocking disallowed tool calls, PII in outputs, looping behavior, and out-of-scope actions ... risk based assessment, and human-in-the-loop enforcement are necessary elements" (§IV-I) | Policy (content rules are V5) | Clean |
| B15 | Failure detection and recovery | "Detection (trajectory anomaly detection, immutable audit ledgers the agent cannot modify); Prevention (dry-run simulation, copy-on-write sandboxing); Response (saga-pattern compensation, checkpoint/restore)" (§IV-J); failure modes include "planning failures returning HTTP 200" and "self-concealment" | Span: Evaluation (detect a silent failure), Observability (tamper-proof ledger), Environments (copy-on-write), Tasks and Sessions (checkpoint, restore), V14 (compensation). WARM's Reliability is about services, not an agent's work | Span |
| B16 | Saga & checkpoint (Table I only) | "Compensating txns for stochastic workflows" (Table I) | Span: Tasks, Sessions; compensation is V14 | Span |
| B17 | Trajectory observability | "semantic trace correlation: tracing every output back through reasoning, tool calls, and memory retrievals, including freshness metadata" (§IV-K) | Observability | Clean |
| B18 | Secure code execution | "transactional filesystem sandboxing with copy-on-write — staging all agent-generated code in a shadow copy for review before committing" (§IV-L) | Environments | Clean |
| B19 | AI-aware networking (AI-aware proxy) | "a sidecar pattern to intercept all outbound tool calls, validate SPIFFE identity, enforce authorization, exchange tokens (RFC 8693), and emit semantic telemetry"; Table I gap "no KV-cache routing" (§IV-M) | Span: an enforcement point for Tools, Identity, Policy, Secrets (token exchange), Observability; KV-cache routing is Models or Infrastructure | Span |
| B20 | rossoctl "Life-cycle management" pillar | "Abstractions, orchestration, skills management" (Fig. 2) | Span: Orchestration, Registry, plus the lifecycle gap | Span |
| B21 | rossoctl "Networking" pillar | "Gateways for agents and tools with built-in security primitives" (Fig. 2) | Span: Tools, Messaging (gateways for agents) | Span |
| B22 | rossoctl "Identity & Access" pillar | "Multi-layer permission system based on agent identity" (Fig. 2) | Span: Identity, Policy | Span |
| B23 | rossoctl "Resiliency surface" | "Techniques to prevent, detect, mitigate incorrect tool calls, partial failures" (Fig. 2) | Span: Policy, Evaluation, Tasks, Reliability | Span |
| B24 | rossoctl "State management" | "Session state, caching, context management, memory – life cycle management and data security" (Fig. 2) | Span: Sessions, Harness, Memory, Policy (retention). Caching was recorded and not adopted in v0.11 | Span |
| B25 | rossoctl "Observability" pillar | "Trajectory analysis, failure attribution, audit" (Fig. 2) | Observability (failure attribution touches Evaluation) | Clean |
| B26 | Agent Execution Environment / Agent Execution Runtime | "in-network side-cars provides a transparent point of isolation, observability, and control" (§V); "Light-weight in-pod configurable and framework agnostic interception layer" (Fig. 2) | Span: enforcement point for Policy, Environments, Observability | Span |
| B27 | AuthBridge | "Platform-enforced primitives: authorization (AuthBridge), identity attestation (SPIFFE/SPIRE) ... cannot be bypassed by application code" (§V) | Span: Policy, Identity | Span |
| B28 | MCP Gateway; CRDs MCPServer, VirtualMCPServer | "express agent platform policy in the same language as cloud infrastructure policy" (§V) | Tools | Clean |
| B29 | rossoctl UI | "Dashboard: Deploy, Test, Monitor Agents & Tools + Backend API" (Fig. 2) | Span: Releases, Evaluation, Observability (builder and operator tooling) | Span |
| B30 | Kubernetes substrate | "rossoctl extends Kubernetes rather than replacing it" (§V) | Infrastructure | Clean |
| B31 | Enterprise requirements | "regulatory compliance ... data sovereignty ... multi-cloud and on-premises operation ... integration with existing enterprise systems" (§II-4) | Guidance (tenancy is V12) | Guidance |
| B32 | Lesson 1, "Standardization is the exit from experimentation" | §VI | Guidance | Guidance |
| B33 | Lesson 2, "Build on, not in replacement of, the prior layer" | §VI | Guidance | Guidance |
| B34 | Lesson 3, "Specify only what is genuinely new"; "POSIX file systems still store agent artifacts" | §VI | Guidance; evidence against Artifacts as a platform service (finding 4) | Guidance |
| B35 | Lesson 4, "Platform enforces what application code only requests" | §VI | Guidance; Governance point 1 | Guidance |
| B36 | Open research agenda, eight problems | "Stochastic scheduling theory ... Evaluation methodology ... Semantic skill interface contracts ... Agent-aware information flow analysis ... Software supply-chain security for AI-generated code ... Formal policy languages ... Principled context eviction theory ... Agentic RL and meta-learning" (§VII) | Guidance | Guidance |
| B37 | Reversibility classification | "the platform must classify calls as reversible, compensable, or irreversible and require elevated authorization for the last" (§IV-D, §III-A) | Span: Registry (a tool's declared effect class), Policy (requires a grant for irreversible calls), V14. The declaration itself is not in WARM or V1 to V15 | Span |

### B.2 Reverse direction

See the combined table.

### B.3 Findings for Steinder and Franke

**(a) Misfits and spans**

| Item | Kind | What it suggests |
|---|---|---|
| B03 Planning | Misfit | Nothing: out of scope by Step 0. |
| B06 Agent lifecycle | Misfit | Change 1. Also the identity clause (c). |
| B15 Failure detection and recovery | Span | WARM's Reliability ("keep services available") does not cover an agent that returns success for failed work. Detection of a silent failure falls to Evaluation, and recovery to Tasks. Nothing is missing, but WARM never says who notices; one sentence would settle it (change 11). |
| B19, B26, B27 enforcement points | Span | The paper places governance in sidecars and gateways that "cannot be bypassed by application code". Confirms Governance point 1; WARM places no enforcement point in a named service. No change. |
| B37 Reversibility | Span | Supports change 5: tools declare whether their effects can be undone. |
| B07, B13, B16, B20 to B24, B29 | Span | Clean spans of existing services. |

**(b) Top-level cut compared**

| Steinder and Franke primitive | WARM group and service |
|---|---|
| Agent lifecycle | none (Runtime, Governance partly) |
| Orchestrator | Interaction (Orchestration), Runtime (Scheduling) |
| Skills registry | Capabilities (Registry) |
| Tool mediation | Capabilities (Tools) |
| Context management | Runtime (Harness) |
| A2A communication | Interaction (Messaging) |
| Agent memory | Knowledge (Memory) |
| Identity & AuthZ | Governance (Identity, Policy) |
| Behavioral guardrails | Governance (Policy) |
| Failure detection | Operations (Evaluation, Reliability), Runtime (Tasks) |
| Saga & checkpoint | Runtime (Tasks, Sessions) |
| Trajectory observability | Operations (Observability) |
| Secure code execution | Runtime (Environments) |
| AI-aware networking | Infrastructure, with Governance enforcement |
| (absent) | People, Domains, Directory, Channels, Approvals (one phrase only), Secrets (token exchange only), Retrieval, Artifacts, Models selection, Improvement, Releases (skill versions only), Evaluation (a research problem only) |

The cut is by OS analogy: each primitive descends from an OS and a Kubernetes abstraction (Table I). Nine of the fourteen map to one WARM service, which agrees with the search note that it "Maps cleanly onto service-level WARM". It does not look better than WARM's: it has no Interaction or Operations beyond observability, because the OS analogy has no counterpart for people, for judging work, or for changing the system. It is narrower, not differently cut. One point cuts against WARM: the paper refuses new abstractions where an old one suffices and names artifact storage as such a case.

**(c) Identity, definition, instance**

The paper collapses the agent into its running instance: "An agent is an isolated execution context (container/pod) with an LLM session, tool credentials, context buffer, and memory state." Identity is made of the agent's current attributes: "agent identity has a semantic dimension — the agent's current goal, model, and skills — that changes dynamically", and "Agent identity must be a function of its Cloud-OS identity and agent-level properties like goal, skills, tools, model, or context" (§IV-A). Skills are the only definition-like object. Sub-agents are spawned "(fork/exec analog)", so task agents are implied; no agent persists across tasks in the model.

Against WARM Step 0: **a different distinction, and in the opposite direction.** WARM says identity persists through a change of definition, harness or model; this paper makes a change of model or skills a change of identity. My reading is that the paper is after something WARM does not state: authorization must see what the agent currently is (which model, which skills, which version). That is attestation of attributes, which WARM can add to Identity without giving up a persistent identity (change 10). The paper has no persistent agent, so it cannot be compared on that point.

**(d) Cost, conflict, sprawl, confidence**

| Theme | What the paper does | WARM placement |
|---|---|---|
| Cost | "Resource quotas must be multi-dimensional: tokens, tool calls, wall-clock time, and cost"; orchestrators "extended with token-budget quotas, semantic loop detection, and multi-dimensional cost accounting" (§IV-B) | Scheduling (quotas), Observability (accounting); budgets in grants (change 4) |
| Conflict | Orchestration prevents "conflicts on shared resources" (§II-4); semantic memory conflict: "'forecast: increasing' and 'forecast: decreasing' create a semantic conflict invisible to byte-level ACID" (§III-A, §IV-G) | Memory (already keeps entries current); Orchestration |
| Sprawl | Absent. Searched "orphan, sprawl, shadow, unregistered, decommission, retire": one hit, "shadow copy" (§IV-L), unrelated | Change 1 |
| Confidence or risk | "risk based assessment" as a guardrail element (§IV-I); reversibility classes for tool calls (§IV-D). No confidence. Searched "confidence, uncertaint, risk scor": no hits | Change 2 (risk), change 5 (reversibility) |

**(e) Same word, different thing**

| Word | Steinder and Franke | WARM |
|---|---|---|
| Agent | "an isolated execution context (container/pod)" | An identified actor that carries out roles; not a process |
| Identity | A function of goal, model, skills; changes when they change | Persists through a change of definition, harness or model |
| Harness | "bespoke layers of code usually called harnesses" around an agent | Close to WARM's harness product; WARM's Harness service is the loop only |
| Orchestrator | Includes scheduling and agent lifecycle | Orchestration coordinates assignments only |
| Session | "an LLM session" inside the agent | The history of a stretch of work |
| Domain | A skill's subject ("a skill's domain") | An area of work with a charter |

---

## Source C. ASOC manifesto (Beheshti, Dustdar, Benatallah, Casati et al.)

### C.1 Inventory and assignment

The contents of each layer exist only as labels in Figure 1; they are quoted as labels. "Fig. 1" means the stack figure.

**Core concepts (§IV-A)**

| # | Item | Definition (verbatim, where) | Assignment | Cat |
|---|---|---|---|---|
| C01 | Agentic Service | "A service entity that accepts goals, constraints, and context; evaluates possible actions; invokes tools or other services; and returns outcomes with provenance, confidence, cost, risk, and execution metadata" | WARM agent concept, reached through Channels. Strained: an agent defined as a service with a contract, no role or kind | Strained |
| C02 | Delegation Contract | "A formal specification of the scope, authority, constraints, duration, revocability, and accountability conditions under which a human or organisation delegates a goal to an agentic service" | V1 (scoped, time-limited, revocable grant); accountability conditions go beyond V1 | Planned |
| C03 | Agent Harness | "A runtime governance wrapper that mediates an agent's goals, permissions, tools, memory, policies, execution traces, and escalation pathways ... enforcing delegation scope, tool permissions, policy constraints, execution logging, approval gates, circuit breakers, and revocation mechanisms" | Span: Governance group (Policy, Approvals, Identity with V3), Observability, Reliability, and the Harness only in that it wraps the loop. Term clash (C.3 e) | Span |
| C04 | Agentic Service Ecosystem | "A governed, heterogeneous collection of agentic services and conventional services that can be discovered, composed, orchestrated, and managed under shared policies, trust frameworks, and interoperability standards" | Platform layer. Strained: crosses organizations | Strained |
| C05 | Levels of delegation and autonomy L0 to L4 | "Advisory only ... Tool recommendation ... Bounded execution ... Multi-step orchestration ... High-consequence autonomy" with control requirements (Table III) | Guidance (a classification a domain's rules would set) | Guidance |
| C06 | "Agentic Service = Agent + Service Contract + Harness + Governance Metadata" | §IV-A | Guidance | Guidance |

**The ASOC stack (Fig. 1, §IV-B)**

| # | Item | Definition | Assignment | Cat |
|---|---|---|---|---|
| C07 | L1 Human / Organizational Delegation (layer) | "from human/organisational delegation at the top (L1)" (§IV-B) | People layer. Strained: it also holds authority (V1) and goals (domain part) | Strained |
| C08 | L1 Goals | Fig. 1 label | Domain part: Goals. Strained: per delegation, not per area of work | Strained |
| C09 | L1 Constraints | Fig. 1 label | Domain part: Domain rules | Clean |
| C10 | L1 Authority | Fig. 1 label | V1 | Planned |
| C11 | L1 Consent | Fig. 1 label; "Human-agent interaction (goal clarification, consent, intervention, explanation, appeal, and shared control)" (§VI-C) | V13 covers the data subject's control over stored data, not consent to an action. No WARM part records consent to a delegation | Misfit |
| C12 | L1 Human Oversight | Fig. 1 label | Approvals | Clean |
| C13 | L1 Escalation Pathways | Fig. 1 label | Span: Approvals, Directory (to whom), Channels | Span |
| C14 | L1 Appeal Mechanisms | Fig. 1 label; "support human appeal" (§III-D) | No WARM part. Appeal of a decision already made is neither approval nor stop | Misfit |
| C15 | L2 Agentic Interface Layer | "the Agentic Interface (L2)" (§IV-B) | Channels. Strained: it also holds contracts and SLAs | Strained |
| C16 | L2 Goal-Oriented Interfaces | Fig. 1 label; "exposes a goal-oriented interface" (§IV-C) | Same gap as A07: a request carrying a goal and its criteria | Misfit |
| C17 | L2 Capability Descriptions | Fig. 1 label; "Capability contracts specify functional capabilities, goal types, uncertainty characteristics, execution constraints, and resource/trust requirements" (§V-B) | Registry. Strained: outcome contracts, as A24 | Strained |
| C18 | L2 Delegation Contracts | Fig. 1 label | Repeats C02 | Folded |
| C19 | L2 SLA Negotiation | Fig. 1 label; "How should SLAs be defined, negotiated, and enforced between agent principals, providers, and the services they invoke?" (§VI-C) | No WARM part negotiates service levels between agents or suppliers. WARM's open contract question (Step 3) is the nearest | Misfit |
| C20 | L3 Agent Harness Layer | "the flagship layer of the ASOC stack and the most important original concept" (§IV-B) | Repeats C03 | Folded |
| C21 | L3 Runtime Control | Fig. 1 label; "Controllability: The ability to constrain, redirect, or halt agent behaviour" (§V-A) | Span: V3 (stop), Tasks (cancel), Policy | Span |
| C22 | L3 Policy Enforcement | Fig. 1 label | Policy | Clean |
| C23 | L3 Guardrails | Fig. 1 label | Policy (V5 content) | Clean |
| C24 | L3 Permission Boundaries | Fig. 1 label | V1 | Planned |
| C25 | L3 Revocation | Fig. 1 label; "Revocability: The ability to reverse agent-initiated actions where technically feasible" (§V-A) | Two meanings: revoking a grant (V1, V3) and reversing an effect (V14) | Planned |
| C26 | L3 Approval Gates | Fig. 1 label | Approvals | Clean |
| C27 | L3 Circuit Breakers | Fig. 1 label | Reliability. Strained: a breaker on an agent's behavior, not on a failing service | Strained |
| C28 | L3 Audit | Fig. 1 label | Observability | Clean |
| C29 | L4 Agent Reasoning and Planning Layer | "Agent Reasoning and Planning (L4)" | Out of scope (Step 0) | Misfit |
| C30 | L4 LLM Reasoning | Fig. 1 label | Span: Harness, Models | Span |
| C31 | L4 Explicit Task Plans | Fig. 1 label | Orchestration. Strained: a single agent's plan is out of scope | Strained |
| C32 | L4 Rationale Summaries | Fig. 1 label | Observability. Strained | Strained |
| C33 | L4 Memory | Fig. 1 label | Memory | Clean |
| C34 | L4 Reflection | Fig. 1 label | Out of scope: Step 0 names reflection explicitly | Misfit |
| C35 | L4 Uncertainty Estimation | Fig. 1 label; metric "Uncertainty Calibration ... Alignment between agent confidence and actual accuracy" (Table VII) | Same family as A10 | Misfit |
| C36 | L4 Task Decomposition | Fig. 1 label | Orchestration | Clean |
| C37 | L5 Agent-Service Composition Layer | "Agent-Service Composition (L5)" | Orchestration. Strained: includes discovery and selection | Strained |
| C38 | L5 Service Discovery | Fig. 1 label | Registry | Clean |
| C39 | L5 Tool Selection | Fig. 1 label | Span: Harness (the model chooses), Tools | Span |
| C40 | L5 QoS-aware Orchestration | Fig. 1 label; "Agent QoS includes ... latency, throughput, cost ... factual accuracy, reasoning depth, goal-alignment fidelity, and output uncertainty" (§VI-B) | Span: Orchestration, Models (choice by cost and quality), Evaluation | Span |
| C41 | L5 Choreography | Fig. 1 label | Span: Messaging, Orchestration | Span |
| C42 | L5 Workflow Adaptation | Fig. 1 label | Orchestration. Strained: run-time change of a workflow | Strained |
| C43 | L6 Service and Tool Infrastructure Layer | "Service and Tool Infrastructure (L6) at the base" | Providers layer. Strained: also holds databases | Strained |
| C44 | L6 APIs, Microservices, Cloud Services, Enterprise Systems, External Tools | Fig. 1 labels | Providers | Clean |
| C45 | L6 Databases | Fig. 1 label | Infrastructure | Clean |
| C46 | L6 MCP Servers | Fig. 1 label | Tools (the servers are reached through Tools) | Clean |
| C47 | Governance and Observability Plane | "cross-cutting planes spanning all layers" (§IV-B) | Span: Governance group, Operations group (Observability) | Span |
| C48 | Security and Trust Plane | as C47 | Span: Identity, Secrets, Policy; trust has no home (A27) | Span |

**Principles (§V), each with its realization mechanisms**

| # | Item | Definition | Assignment | Cat |
|---|---|---|---|---|
| C49 | Principle 1, Harnessability | "Controllability ... Auditability ... Revocability"; mechanisms "Agent harness, harness-enforced approval gates, revocation tokens, policy enforcement points, sandboxed tool calls, circuit breakers" | Guidance | Guidance |
| C50 | Principle 2, Composability and Interoperability | mechanisms "Capability description language, delegation contract, agent registry and marketplace, MCP/A2A adapters, signed tool manifests, capability verification tests" | Guidance | Guidance |
| C51 | Principle 3, Lifecycle Engineering | "a lifecycle from requirements specification through design, implementation, testing, deployment, operation, monitoring, and retirement"; mechanisms "ADLC framework, agent regression test suites, behavioural drift monitors, versioned prompt/tool/model registries" | Guidance (Releases, Evaluation, Registry) | Guidance |
| C52 | Principle 4, Trustworthiness by Design | "factual reliability ... behavioural alignment ... security ... privacy ... fairness"; mechanisms "policy enforcement framework, alignment verification suites, privacy guard layers, fairness monitors, regulatory compliance evidence schemas" | Guidance | Guidance |
| C53 | Principle 5, Goal-Driven Orchestration | mechanisms "Goal specification language, automated planning and decomposition engine, runtime constraint solver, goal-progress monitor, exception/recovery handlers" | Guidance | Guidance |
| C54 | Principle 6, Observability and Accountability | "An agent provenance graph represents the complete causal structure of an agent's execution"; mechanisms "Semantic audit logs, agent provenance graphs, real-time event streams, policy-decision logs, compliance evidence exporters" | Guidance (Observability; V11) | Guidance |

**Research agenda items (§VI) not already listed**

| # | Item | Definition | Assignment | Cat |
|---|---|---|---|---|
| C55 | Agent registry and marketplace | "there will be registries, discovery mechanisms, reputation systems, billing models, and certification requirements" (§VI-A) | Registry for registries and discovery; reputation, billing and certification are C56 to C58 | Clean |
| C56 | Reputation systems and trust calibration | "Trust must be earned dynamically through operational track record ... runtime enforcement that constrain agent authority in proportion to established trust" (§VI-D) | Same family as A27 | Misfit |
| C57 | Billing models | §VI-A | Out of scope for one system; payments were recorded and not adopted in v0.11. Suggests nothing new | Misfit |
| C58 | Certification | "certification establishes whether an agentic service satisfies domain-specific safety, compliance, security, and accountability requirements for deployment" (§VI-E) | Span: Evaluation (the assessment), Releases (the gate). Domain-specific requirements are acceptance criteria | Span |
| C59 | Responsibility allocation across principals | "responsibility is distributed across a chain of principals that may include the delegating user or organisation, the agent provider, the underlying model provider, the tool or plugin provider, the orchestrating platform, and the deploying organisation" (§VI-A) | No WARM part. WARM's Directory assigns accountability to domains inside one system; WARM's mapping fields (who supplies, who operates) are the nearest hook. Out of scope as legal liability | Misfit |
| C60 | Agentic QoS | "integrates classical measures (latency, throughput, availability, cost) with agent-specific measures: goal-completion fidelity, factual reliability, uncertainty calibration, policy compliance rate, tool-use safety, provenance completeness, and human-oversight effectiveness" (§VI-E, Table VII) | Span: Evaluation, Observability | Span |
| C61 | Emergent behavior governance | "detect harmful emergent behaviours (unintended agent coalitions, resource monopolisation, coordinated misinformation) and to intervene at the governance layer" (§VI-C) | Span: Observability, Evaluation, Policy. No WARM service watches the population of agents as a whole | Span |
| C62 | ASOC threat model | Table VI, seven threats | Guidance | Guidance |
| — | Seven SOC pillars and their ASOC transformations (Table I) | "Agentic capability and delegation contract ... Goal-level agentic service discovery ... Goal-driven orchestration ... Agentic QoS ... Agent Development Lifecycle (ADLC) ... Agent provenance graphs ... Harness-based governance" | Each repeats an item above (C17, C02, C38, C53, C60, C51, C54, C03) | Folded |
| — | Five research dimensions (§VI-A to VI-E) | headings | Containers for C55 to C61 | Folded |

### C.2 Reverse direction

See the combined table.

### C.3 Findings for ASOC

**(a) Misfits and spans**

| Item | Kind | What it suggests |
|---|---|---|
| C11 Consent | Misfit | A small gap in People and Approvals: who agreed to a delegation, and to what. Low weight; one source. |
| C14 Appeal | Misfit | Human oversight is wider than approval and stop (also AOS §7.11: "post-action review, and dispute resolution"). Change 8. |
| C16 Goal-oriented interfaces | Misfit | Same as A07: change 6. |
| C19 SLA negotiation | Misfit | Nothing new: WARM's open contract question. |
| C29, C34 Reasoning layer, Reflection | Misfit | Nothing: out of scope by Step 0. |
| C35 Uncertainty estimation, C56 Reputation and trust calibration | Misfit | Change 2. |
| C57 Billing | Misfit | Nothing: out of scope for one system. |
| C59 Responsibility allocation | Misfit | Nothing in the model; worth one sentence that WARM's Directory is about accountability inside one system, not liability across suppliers. |
| C03 Agent Harness | Span | A term clash (e). ASOC's "harness" is WARM's Governance group wrapped around the loop. |
| C47, C48 planes | Span | Close to WARM's two cross-cutting groups; see (b). |
| C21, C39 to C41, C58, C60, C61 | Span | Spans of existing services. C61 is the only one with no owner in WARM: watching the population of agents. It belongs with change 1 (an owner of which agents exist). |

**(b) Top-level cut compared**

| ASOC part | WARM groups and layers |
|---|---|
| L1 Human/Organizational Delegation | People layer; domain Goals and Rules; Governance (Approvals, V1) |
| L2 Agentic Interface | Interaction (Channels); Capabilities (Registry descriptions) |
| L3 Agent Harness | Governance (Policy, Approvals, Identity), Operations (Observability, Reliability) |
| L4 Agent Reasoning and Planning | outside WARM (single-agent reasoning), with Knowledge (Memory) |
| L5 Agent-Service Composition | Interaction (Orchestration), Capabilities (Registry, Tools, Models) |
| L6 Service and Tool Infrastructure | Providers, Infrastructure, Capabilities (Tools) |
| Plane: Governance and Observability | Governance and Operations groups |
| Plane: Security and Trust | Governance (Identity, Secrets, Policy) |
| (absent) | Runtime group (Sessions, Tasks, Environments, Scheduling, Harness as the loop), Knowledge (Retrieval, Artifacts), Interaction (Directory, Messaging as a service), Operations (Improvement, Releases as a service), Domains layer |

ASOC cuts vertically, from the person who delegates down to the services agents call, with two cross-cutting planes. That the planes are "Governance and Observability" and "Security and Trust" is independent support for WARM's choice of two cross-cutting groups. ASOC's cut is not better: governance appears both as L3 and as a plane, the stack has no runtime substrate at all, and L4 puts single-agent reasoning inside a platform model, which WARM excludes deliberately. ASOC is a research agenda with thin components; the search note's "Thin on each component" holds.

**(c) Identity, definition, instance**

ASOC has no agent identity concept. It lists "agent identity" as missing from OAuth/OIDC (Table V) and makes the deployable unit "Agent + Service Contract + Harness + Governance Metadata". Lifecycle engineering includes "retirement" and "versioning, rollback", which are about a service's versions over development time, not about running agents. It does not distinguish agents that persist across tasks from agents created for one task. Searched "persist, long-lived, resident, transient, ephemeral, sub-agent, spawn, worker, instance": no hits. Against WARM Step 0: absent.

**(d) Cost, conflict, sprawl, confidence**

| Theme | What ASOC does | WARM placement |
|---|---|---|
| Cost | A classical QoS metric: "Computational and financial cost per goal execution; measured in tokens or USD per task" (Table VII); "billing models" in marketplaces (§VI-A) | Observability and Evaluation measure it; billing is out of scope |
| Conflict | No mechanism. "Multi-agent cascade failure: Agents reinforce errors or coordinate harmful behaviour at scale" (Table VI); "unintended agent coalitions, resource monopolisation" (§VI-C) | Observability and Evaluation over the population of agents; no WARM owner (change 1) |
| Sprawl | "retirement" in the lifecycle (§V-C); "retirement protocols" attributed to Deng et al. (Table II); "managing agent populations" (§IV-C) | Change 1 |
| Confidence or risk | Agentic Service returns "confidence, cost, risk" (§IV-A); L4 "Uncertainty Estimation"; trust calibration constrains authority (§VI-D); "Uncertainty Calibration ... expected calibration error" (Table VII) | Change 2 |

**(e) Same word, different thing**

| Word | ASOC | WARM |
|---|---|---|
| Harness | "A runtime governance wrapper" enforcing scope, permissions, approvals, logging, circuit breakers, revocation | The service that runs the agent loop |
| Lifecycle | The development lifecycle (ADLC): requirements to retirement | (WARM has no lifecycle term for agents; Tasks tracks a unit of work) |
| Infrastructure | L6 includes APIs, enterprise systems, external tools | Machines, CI runners, storage, network; external services are Providers |
| Directory | "capability directories" for "dynamic discovery and trust assessment" (§VI-C) | The record of which domain is accountable for what |
| Revocation | Both withdrawing authority and "reverse agent-initiated actions" (§V-A) | Revoking an actor is V3; undoing an effect is V14 |
| Provider | "agent provider, model provider, tool provider" as suppliers who carry liability | The Providers layer; suppliers appear only in a mapping's "who supplies" field |

---

## Source D. EAAF (Venkiteela)

### D.1 Inventory and assignment

| # | Item | Definition (verbatim, where) | Assignment | Cat |
|---|---|---|---|---|
| D01 | Infrastructure Layer | "foundational computational, networking, and storage resources ... a Kubernetes-based agent runtime, serverless execution options, enterprise networking components (VPC, service mesh), Secrets management, and a unified Observability stack"; responsibilities "secure sandboxed environments for executing risky or untrusted actions ... maintaining operational service level agreements" (§4.1.1) | Span: Infrastructure, Environments, Secrets, Observability, Reliability | Span |
| D02 | Enterprise Integration Layer | "the secure and structured interface necessary for agents to interact with mission-critical enterprise systems (ERP, CRM, iPaaS, APIs)"; responsibilities "enforcing policy-controlled API/tool execution, providing accurate semantic mappings between disparate enterprise systems, and supporting the operation of event-driven agents" (§4.1.2) | Span: Tools, Policy, Scheduling (events), and domain tools and knowledge (the semantic mappings) | Span |
| D03 | Enterprise Tool Bus (ETB) | "exposes canonical, standardized tool interfaces to the agents. It handles safe function invocation, provides necessary data transformation utilities" (§4.1.2) | Tools | Clean |
| D04 | Integration Adapters | "platform-specific adapters for seamless connectivity with established systems such as SAP BTP Integration Suite, Boomi AtomSphere, MuleSoft, and various Salesforce APIs" (§4.1.2) | Domain part: Domain tools (WARM's placement test: a connector to one system is domain logic carried by Tools). EAAF places them in a platform layer | Clean |
| D05 | Orchestration & Coordination Layer | "governs how autonomous agents collaborate, coordinate their actions, and sequence tasks" (§4.1.3) | Orchestration | Clean |
| D06 | Multi-agent orchestration patterns | "Supervisor–Worker Model, the Pipeline Orchestrator pattern, and dedicated Specialist Agent Clusters" (§4.1.3); "Supervisor–Worker models, Swarm Intelligence, Chain-of-Expert Agents, and Negotiation Protocols" (§5.1.3); "federated agent clusters" (§1) | Guidance (workflow patterns) | Guidance |
| D07 | Orchestration Engine | "large-task decomposition, intelligent delegation to specialist agents, dependency management across steps, and necessary compensation logic or workflow rollback capabilities" (§4.1.3) | Orchestration (compensation is V14) | Clean |
| D08 | Human-in-the-Loop Interfaces | "approval gating for high-risk tasks, override capabilities for human intervention, and structured human–agent co-planning" (§4.1.3) | Approvals. Strained: override is V3; co-planning is not approval | Strained |
| D09 | Governance & Safety Layer | "the 'authority gatekeeper' ... evaluates whether the agent has the decision authority to execute it. Every proposed tool invocation is passed through the Pre-Action Validation Pipeline" (§4.1.4) | Span: Policy, Approvals, plus the risk scoring that has no home (D11) | Span |
| D10 | Policy Engine | "Enforces fine-grained access policies (RBAC/ABAC) and executes pre-action compliance checks" (§4.1.4) | Policy | Clean |
| D11 | Risk Scoring Engine | "a predictive, real-time evaluation of potentially harmful actions, allowing for dynamic throttling or complete blocking of the action" (§4.1.4) | No WARM home (as A10) | Misfit |
| D12 | Audit & Traceability Service | "comprehensive per-action logging and agent activity trails" (§4.1.4) | Observability | Clean |
| D13 | Safety Guardrails | "model-level safety filtering, strict tool-use guardrails, human approval gates, and autonomous rollback capabilities" (§4.1.4) | Span: Policy (V5), Approvals, Tasks or Releases (rollback) | Span |
| D14 | Identity & Credential Hygiene | "Every agent is assigned a unique identity and must use short-lived, transient credentials" (§4.1.4) | Span: Identity, Secrets (rotation is V8) | Span |
| D15 | Agent Intelligence Layer | "the core reasoning, memory, planning, and cognitive capabilities" (§4.1.5) | Span: Harness, Models, Memory, Retrieval; single-agent reasoning out of scope | Span |
| D16 | Planning Engine | "supporting algorithms like ReAct, Chain-of-Thought" (§4.1.5) | Out of scope (Step 0) | Misfit |
| D17 | State/Memory Manager | "for long-term and short-term context persistence" (§4.1.5) | Span: Sessions, Memory | Span |
| D18 | Retrieval Engine | "enabling RAG and vector stores" (§4.1.5) | Retrieval | Clean |
| D19 | Feedback Loop Executor | "for continuous self-correction and refinement" (§4.1.5) | Out of scope as single-agent reflection (Step 0); it is not WARM's Improvement, which changes agents from evidence across work | Misfit |
| D20 | Agent Types | "Task Agents, dedicated Integration Agents, Compliance Agents, and high-level Supervisor Agents" (§4.1.5) | WARM roles (agent concept). Strained: "Task Agents" is a function, not a lifetime (term clash) | Strained |
| D21 | Agent Interaction Layer | "the standardized protocols and channels through which agents interact with external systems, human users, and their available tools" (§4.1.6) | Span: Channels (people), Tools (systems), Environments (browser, terminal) | Span |
| D22 | Interaction Channels | "direct API invocation, automated browser control, execution of terminal commands, and human communication via chat interfaces (e.g., Slack, Teams)" (§4.1.6) | Span: Channels, Tools, Environments. EAAF mixes how people reach agents with how agents act | Span |
| D23 | Action Validation Pipeline (Interaction layer) and Pre-Action Validation Pipeline (PCE) | "intent understanding, secure tool selection, policy check, safety validation, and sandboxing" (§4.1.6); "evaluates every proposed tool invocation against its Intent Classification, Safety Scoring, Policy Constraints, and Risk Level before granting an Allowed, Blocked, or Requires Approval outcome" (§5.1.2) | Span: Policy, Approvals, Environments; the scoring parts are D11 | Span |
| D24 | Enterprise Tool Abstraction | "Agents view complex enterprise systems as simple, standardized tools" (§4.1.6) | Tools | Clean |
| D25 | EAAF Control Plane | "a unified operational layer that ensures the safe, predictable, and compliant execution of all agentic workloads" (§5) | Span: Governance (Identity, Policy), Interaction (Orchestration), Runtime (Scheduling), Operations (Observability, Releases), and the lifecycle gap | Span |
| D26 | Identity & Access Subsystem (IAAS) | "unique cryptographic identity, a policy-bound namespace, and a dynamic trust score ... short-lived, rotation-based credentials (e.g., OAuth2/JWT, scope-limited keys) issued via enterprise vaults with Just-in-Time (JIT) issuance ... deny-by-default posture" (§5.1.1) | Span: Identity, Secrets (V8), Policy; the trust score has no home (A27) | Span |
| D27 | Policy & Compliance Engine (PCE) | "governs what agents are permitted or forbidden to do ... granular tool-level permissions, strict data access restrictions, region-level data sovereignty requirements (GDPR, PCI), and workflow-specific controls" (§5.1.2) | Policy | Clean |
| D28 | Compliance Agents | "dedicated Compliance Agents continuously monitor for anomalous agent behavior and ensure adherence to regulatory constraints, intervening when necessary" (§5.1.2) | WARM's provisional case: an agent providing a platform service (Policy, Observability). Agent concept, strained | Strained |
| D29 | Orchestration & Scheduling Engine (OSE) | "plan generation, subtask identification, delegation to specialist agents, and advanced error handling ... priority queues, real-time versus batch scheduling, and multi-cloud availability zones" (§5.1.3) | Span: Orchestration, Scheduling, Tasks | Span |
| D30 | Agent Lifecycle Manager (ALM) | "manages the complete creation, maintenance, and retirement of agents, treating them as first-class enterprise assets ... Provisioning (initializing identity/environment), Configuration (policy binding), Execution, Monitoring, Adaptation, and Decommissioning (credential revocation) ... multi-version coexistence, canary rollouts, and automatic rollback ... Continuous Adaptation by managing policy updates, prompt improvements, and incorporating runtime learning signals" (§5.1.4) | Its release part is Releases and its adaptation part is Improvement. Its core, provisioning and decommissioning agents as assets, has no WARM home (as A14) | Misfit |
| D31 | Observability & Telemetry Fabric (OTF) | "Decision logs, Tool-use traces, Agent reasoning snapshots, Memory access events, and multi-agent collaboration logs ... Behavioral Analytics to detect looping, unsafe tool usage patterns, and policy violations ... Immutable Audit Trails" (§5.1.5) | Observability (behavioral analytics touches Evaluation) | Clean |
| D32 | Principle: Autonomy with Accountability | "operational autonomy ... is strictly decoupled from decision authority" (§3.4) | Guidance | Guidance |
| D33 | Principle: Safety First | "No agent action, under any circumstances, should violate established corporate policy, regulatory compliance rules, or the original user intent" (§3.4) | Guidance | Guidance |
| D34 | Principle: Governed Tool-Use | "exclusively through controlled, permissioned, and constantly monitored interfaces" (§3.4) | Guidance (Governance point 1) | Guidance |
| D35 | Principle: Human-Centric Oversight | §3.4 | Guidance | Guidance |
| D36 | Principle: Modular and Extensible Architecture | "Every layer of EAAF must be designed to evolve independently" (§3.4) | Guidance | Guidance |
| D37 | Principle: Multi-Cloud Native | §3.4 | Guidance | Guidance |
| D38 | Functional requirements (5) | "Agent Tool Interaction ... Multi-Agent Collaboration and Coordination ... Enterprise Integration Support ... Human-in-the-Loop Interactions ... Agent Lifecycle Management" (§3.2) | Guidance; the last repeats D30 | Guidance |
| D39 | Non-functional requirements (6) | "Security & Zero-Trust Execution ... Safety & Ethical Compliance ... Reliability & High Availability ... Observability & Auditability ... Scalability & Performance ... Vendor and Model Neutrality" (§3.3) | Guidance | Guidance |
| D40 | ZeroOps | "Humans shift from being 'operators' who perform tasks to 'governors' who set policies and handle high-risk exceptions" (§3.1) | Guidance (People layer) | Guidance |
| D41 | Enterprise use cases | "Opportunity-to-Order ... Self-Healing Middleware & Autonomous Operations ... Agentic DevOps & SDLC ... Finance, Procurement & ERP ... Data Engineering ... Customer Experience" (§6) | Domains layer (areas of work, each a candidate domain). Strained: described as automations, not charters | Strained |
| D42 | Cross-functional multi-domain federation | "a federation of multi-domain agents (Integration, Compliance, Data, Security, Finance, etc.) ... agents negotiate responsibilities, securely share context ... with safety guardrails and approvals managed centrally by the Control Plane" (§6.6) | The nearest thing in any of the four to WARM's Domains. It contradicts the Directory: responsibilities are negotiated at run time, not set by people in advance | Misfit |
| D43 | Future work: Enterprise Agent Standardization Protocol, Enterprise Agent Benchmark | "secure agent identities, cross-platform permission models, and consistent tool registry metadata"; "standardize evaluation methods for governed tool-use reliability" (§8.2) | Guidance (Registry, Evaluation) | Guidance |

### D.2 Reverse direction

See the combined table.

### D.3 Findings for EAAF

**(a) Misfits and spans**

| Item | Kind | What it suggests |
|---|---|---|
| D11 Risk Scoring Engine | Misfit | Change 2. |
| D16 Planning Engine, D19 Feedback Loop Executor | Misfit | Nothing: out of scope. D19 is a useful check that WARM's Improvement is not single-agent self-correction. |
| D30 Agent Lifecycle Manager | Misfit | Change 1. EAAF shows the lifecycle bundles three WARM responsibilities: provisioning and decommissioning (no home), version rollout (Releases), adaptation (Improvement). Only the first is missing. |
| D42 Responsibilities negotiated by agents | Misfit | Nothing to add, but a direct contrast worth stating: WARM's Directory is set by people and agents look it up; EAAF lets agents negotiate. EAAF reports "coordination overhead grows disproportionately beyond roughly fifty agents", which (my inference, unverified given its weak method) is consistent with negotiation costing more than lookup. |
| D02, D21, D22 | Span | EAAF places domain connectors in a platform layer and mixes people's channels with agents' tools. WARM's placement test splits both cleanly: the ETB is Tools, each adapter is domain tools; chat is Channels, browser and terminal are Environments and Tools. Evidence that the test does work. |
| D01 | Span | EAAF places Secrets and Observability in Infrastructure. WARM places the responsibilities in the platform and the backends in Infrastructure. No change. |
| D09, D13, D14, D17, D23, D25, D26, D29 | Span | Spans of existing services, apart from the scoring and trust parts noted. |

**(b) Top-level cut compared**

| EAAF part | WARM groups and layers |
|---|---|
| Agent Interaction Layer | Interaction (Channels), Capabilities (Tools), Runtime (Environments), Governance (Policy) |
| Agent Intelligence Layer | Runtime (Harness), Capabilities (Models), Knowledge (Memory, Retrieval), and out-of-scope reasoning |
| Governance & Safety Layer | Governance (Policy, Approvals, Identity, Secrets), Operations (Observability) |
| Orchestration & Coordination Layer | Interaction (Orchestration), Governance (Approvals) |
| Enterprise Integration Layer | Capabilities (Tools), Domains (domain tools and knowledge), Providers |
| Infrastructure Layer | Infrastructure, Runtime (Environments), Governance (Secrets), Operations (Observability, Reliability) |
| Control Plane: IAAS, PCE, OSE, ALM, OTF | Governance (Identity, Secrets, Policy), Interaction (Orchestration), Runtime (Scheduling), Operations (Releases, Improvement, Observability), and the lifecycle gap |
| (absent) | People as a layer, Directory, Messaging as a service, Artifacts, Evaluation as a service, Sessions as a service, Registry (future work only) |

EAAF cuts six layers "bottom-up" plus a control plane. Several components appear twice: governance in a layer and in the PCE, orchestration in a layer and in the OSE, action validation in the Interaction layer and in the PCE. The cut is not better than WARM's; it is an example of the mixing WARM's test is meant to resolve. The search note's ranking of EAAF as "the most-cited of the enterprise reference architectures found" rests on a citation count whose sources are weak (Adoption evidence).

**(c) Identity, definition, instance**

"Each deployed agent receives a unique cryptographic identity, a policy-bound namespace, and a dynamic trust score" (§5.1.1). Agents are "first-class enterprise assets", provisioned and decommissioned by the ALM, with "multi-version coexistence, canary rollouts, and automatic rollback to the last stable version" (§5.1.4). There is no agent definition separate from the agent; "prompt improvements" and "policy updates" are lifecycle adaptation of the agent itself. "Task Agents" are a functional type next to Integration, Compliance and Supervisor agents, not agents created for one task. Against WARM Step 0: **a different and less precise distinction.** EAAF's versions of an agent are close to WARM's revisions of a definition, but EAAF has no word for the definition and no lifetime split. Its "Task Agents" is a direct term clash with WARM's task agent.

**(d) Cost, conflict, sprawl, confidence**

| Theme | What EAAF does | WARM placement |
|---|---|---|
| Cost | Absent as a platform concern. Searched "cost, budget, billing, spend, token" in the body: no hits for cost or budget; "verifying spend thresholds" (§6.4) is a finance domain rule | Domain rules (Finance), not a platform matter |
| Conflict | "Negotiation Protocols" (§5.1.3); "negotiation agents" (§1); "agents negotiate responsibilities" (§6.6); "Coordination Errors" measured up to 50 agents (Table 4) | WARM avoids it structurally: one accountable domain per responsibility (Directory) |
| Sprawl | ALM "Decommissioning (credential revocation)" (§5.1.4); agents as "formal enterprise assets" with "secure decommissioning of all agents" (§3.2) | Change 1 |
| Confidence or risk | Risk Scoring Engine; Pre-Action Validation Pipeline with "Safety Scoring ... Risk Level"; "dynamic trust score" (§4.1.4, §5.1.1, §5.1.2) | Change 2 |

**(e) Same word, different thing**

| Word | EAAF | WARM |
|---|---|---|
| Task agent | A type of agent by function | An agent that lives for one task |
| Control plane | Identity, policy, orchestration, scheduling, lifecycle, observability: management of the whole | No plane; Governance and Operations are cross-cutting groups |
| Domain | "multi-domain agents (Integration, Compliance, Data, Security, Finance, etc.)": a functional specialty of an agent | An area of work defined by a charter, not an agent |
| Infrastructure | Includes Secrets management and the observability stack | Machines, runners, storage, network |
| Intent | "Intent Classification" of a proposed tool call | (WARM has no intent concept) |
| Orchestration | Includes plan generation and scheduling | Coordinates assignments; Scheduling is separate |

---

## Reverse direction, all four sources

F = fully, P = partly, A = absent. Every A was given only after the search terms in the second column were run over the source's body text (references excluded). "Per request" means the source has the part for one request or one delegation, not as a standing part of an area of work.

| WARM part | Terms searched | A. AOS | B. Steinder and Franke | C. ASOC | D. EAAF |
|---|---|---|---|---|---|
| Harness | harness, loop, context, reasoning | P: context building §10.5; the loop is left to "Agent frameworks ... inside the Runtime & Coordination Plane" §5.3 | F: context management §IV-E; "context-assemble → infer → tool-call → update" §IV-A | P: L4 "LLM Reasoning"; "harness" means a governance wrapper | P: Planning Engine, reasoning cycle §4.1.5 |
| Sessions | session, thread, checkpoint, resume, conversation | P: pause, resume, migrate with "checkpoints, and trace continuity" §10.2 | P: "an LLM session" §IV-A; rossoctl "Session state" | A: no hits for session or checkpoint | P: "state persistence across sessions" §2.5; State/Memory Manager §4.1.5 |
| Tasks | task, execution, retry, cancel, lifecycle, saga | F: Execution §6.13; lifecycle states Appendix C.2; failure contracts §11.11 | P: Saga & checkpoint (Table I); Response §IV-J | P: "exception/recovery handlers", "goal-progress monitor" §V-E | P: "compensation logic or workflow rollback" §4.1.3; "advanced error handling" §5.1.3 |
| Environments | sandbox, isolat, container, workspace | P: runtime assurance isolation §10.8; OS and hypervisors external §8.6 | F: Secure Code Execution §IV-L; agent as isolated execution context §IV-A | P: "sandboxed tool calls" §V-A | F: "secure sandboxed environments for executing risky or untrusted actions" §4.1.1 |
| Scheduling | schedul, cron, trigger, event, queue, concurren | F: Scheduling §10.6; intents from "a monitoring system, or a policy-triggered automation" §6.2 | P: token-budget quotas §IV-B; no time or event triggers | A: no hits for schedul, trigger, cron, queue; only AsyncAPI "event-driven service description" (Table V) | F: "priority queues, real-time versus batch scheduling" §5.1.3; "event-driven agents" §4.1.2 |
| Memory | memory, episodic, long-term | F: memory coordination §10.5, §14.6, §16.6 | F: Agent memory §IV-G | P: L4 label "Memory" only | P: State/Memory Manager §4.1.5 |
| Retrieval | retriev, RAG, knowledge base, vector, grounding | P: "retrieval and vector systems" external §8.5; context retrieves authorized records §10.5 | P: retrieval in memory §IV-G; "retrieved documents" §II-2 | A: no hits for retriev or RAG; "groundedness" is an evaluation metric | F: "Retrieval Engine (enabling RAG and vector stores)" §4.1.5 |
| Artifacts | artifact, artefact, output, work product, report, store | P: "artifact memory" §10.5; "Evidence and provenance artifact" (Table 5) | P: delegated to the OS: "POSIX file systems still store agent-produced artifacts" §IV | A: "artefact" means an engineering artifact of the field | A: no hits for artifact; RCA summaries go to "ticketing systems" (§6.2), a domain tool |
| Models | model rout, routing, provider selection, multi-model, LLM | F: model and tool routing; ranking §12.4; model hosting external | P: KV-cache routing gap (Table I); no model choice | P: QoS-aware orchestration; "versioned prompt/tool/model registries" §V-C | P: "Vendor and Model Neutrality" requirement §3.3; no component |
| Tools | tool, MCP, gateway, adapter, connector | F: routing §10.4; protocol mediation §10.9 | F: Tool mediation §IV-D | P: L5 "Tool Selection", L6 "MCP Servers"; mediation folded into the harness | F: Enterprise Tool Bus §4.1.2 |
| Registry | registr, catalog, manifest, skill | F: capability registry §11.4; AOS-0000 §4.5 (holds capabilities, not agent definitions) | F: Skills registry §IV-C | P: "agent registry and marketplace" §V-B, "versioned prompt/tool/model registries" §V-C | P: "consistent tool registry metadata" as future work only §8.2 |
| Directory | director, accountab, owner, responsib, route | P: reaches a provider for a capability (the "how to reach" half); approvals go "to an accountable role" §9.9; no record of which domain is accountable | A: "routing tasks to the right specialist agent" §II-4 is orchestration | A: "capability directories" §VI-C means discovery; "responsibility-allocation" §VI-A means liability | A: "agents negotiate responsibilities" §6.6 is the opposite approach |
| Messaging | message, A2A, broker, event, pub/sub | P: A2A adapter and event streams §10.9; brokers external §8.5 | F: A2A communication §IV-F | P: A2A in Table V; L5 "Choreography" | P: A2A only as a missing standard §8.1; "securely share context" §6.6 |
| Orchestration | orchestrat, workflow, coordinat, delegat, plan | F: workflow coordination §10.3; Plan §6.6; delegation §9.7 | F: Orchestrator §IV-B | F: goal-driven orchestration §V-E; L5 | F: Orchestration layer §4.1.3; OSE §5.1.3 |
| Channels | channel, chat, interface, endpoint, UI, dashboard | P: IntentEnvelope from "Client, human, upstream agent, monitoring system" (Table 9); "Human task protocol" (Table 11) | A: "platform-mediated channels" §IV-A are for spawning sub-agents; the rossoctl UI is an operator dashboard | P: L2 "Goal-Oriented Interfaces" | P: "human communication via chat interfaces (e.g., Slack, Teams)" §4.1.6 |
| Identity | identity, principal, SPIFFE, authentic | F: Identity and Authority §6.8; trust and identity evaluation §9.5 | F: Identity & AuthZ §IV-H | P: "agent identity" listed as missing from OAuth (Table V) | F: IAAS §5.1.1 |
| Secrets | secret, vault, credential, token, key | P: "secrets" external §8.5; runtime "applies credentials" §10.4 | P: token exchange (RFC 8693) §IV-H, §IV-M | P: "Least-privilege scoped credentials" (Table VI); "agent credential management" §VI-D | F: "Secrets management" §4.1.1; JIT credentials from "enterprise vaults" §5.1.1 |
| Policy | policy, guardrail, permission, rule, retention | F: §6.7, §9.4; AOS-0000 layered policy §4.6 | F: guardrails §IV-I; context-dependent authorization §IV-H | F: L3 policy enforcement; Principle 4 | F: PCE §5.1.2 |
| Approvals | approv, human-in-the-loop, oversight, gate | F: human oversight §9.9; HumanApprovalProvider; sequence B.3 | P: "human-in-the-loop enforcement" §IV-I only; no hits for approv | F: L3 "Approval Gates"; Table III | F: HITL checkpoints §4.1.3; "Requires Approval" outcome §5.1.2 |
| Observability | observab, audit, trace, telemetry, log | F: §9.8, §11.7, §11.8 | F: §IV-K | F: Principle 6; L3 "Audit" | F: OTF §5.1.5 |
| Evaluation | evaluat, benchmark, verif, test, criteria | F: verification "part of the operating path" §14.5; evaluation plan (Table 15) | P: evaluation methodology as an open problem §VII.2; "a verification agent" §II-1 | F: §VI-E evaluation, certification, Agentic QoS | P: evaluation method and benchmark §1, §7; no component |
| Improvement | improv, learn, adapt, refine, feedback, retrospective | A: nearest is §14.11 step 6, "update provider health, trust, and reliability estimates", which changes provider selection, not agents or skills | A: nearest is §VII.8, agentic RL, a research problem | A: nearest are "behavioural drift monitors" §V-C and L5 "Workflow Adaptation" (run-time) | P: ALM "Continuous Adaptation ... prompt improvements, and incorporating runtime learning signals" §5.1.4 |
| Releases | release, version, rollout, rollback, canary, deploy | P: versioning §11.10; "governed import process" §13.7; no rollout or rollback | P: skill versioning and signing §IV-C; rossoctl "Deploy" | P: ADLC "versioning, rollback, and retirement" §V-C | F: ALM "multi-version coexistence, canary rollouts, and automatic rollback" §5.1.4 |
| Reliability | reliab, availab, failover, recover, circuit | F: §14 | P: failure detection and recovery of agents' work §IV-J | P: availability metric (Table VII); circuit breakers | P: "automatic failover, reliable state recovery" as a requirement §3.3, no component |
| People (layer) | human, person, people, user, operator, organization | P: humans as actors, approvers and providers; "Humans remain responsible for policy, approval thresholds, exceptions, appeals, and accountability" §7.11 | P: "under human oversight" §II-1; "human-in-the-loop" §IV-I | F: L1 Human/Organizational Delegation | P: humans as "governors" §3.1; HITL |
| Domains (layer) | domain, area of work, department, charter, business unit | A: "AOS domain" is "An administrative and trust boundary"; nearest are "healthcare, telecom, cybersecurity, finance, and data-center profiles" §15.4 | A: "a skill's domain" §IV-C; "harnesses are domain and model specific" §I | A: "domain-specific" requirements only §VI-E | P: use cases by business area §6; "multi-domain agents" §6.6 |
| Platform (layer) | platform, operating system, control plane | F: the two planes | F: the Agent-OS | F: L3, L5 and the two planes | F: control plane and layers 2 to 4 |
| Infrastructure (layer) | infrastructure, compute, network, storage, Kubernetes | F: §8.6, Figure 4 | F: Kubernetes, Cloud-OS §V | P: L6 "Databases", "Cloud Services" | F: Infrastructure Layer §4.1.1 |
| Providers (layer) | provider, vendor, external service, API | F: external platform capabilities incl. "Model Services (LLM/SLM hosting, inference endpoints)" (Figure 4) | P: MCP servers, external systems; not a layer | F: L6 APIs, cloud services, external tools | P: SAP, Salesforce and other systems §4.1.2; LLM vendors §3.3 |
| Goals (domain part) | goal, objective, purpose | P, per request: Intent goal G §6.2 | P, per agent: "the agent's current goal" §IV-A | P, per delegation: L1 "Goals" | P, per request: "When a high-level goal is received" §5.1.3 |
| Roles | role, position, duty | P: "contextual roles" in authority §6.8; "accountable role" §9.9 | A: "roles are declared at deployment time" §IV-H means RBAC roles | A: "structured organisational roles" only in describing MetaGPT §III-A | P: Agent Types §4.1.5; "role-based agent permissions" §1 |
| Workflow | workflow, plan, process, intake | P, per intent: Plan, workflow coordination | P: orchestrator topologies | P: goal-driven orchestration, choreography | P: orchestration patterns §4.1.3 |
| Domain knowledge | knowledge, ontology, profile | P: "domain ontologies" and industry profiles §15.4 | P: a skill's declared domain §IV-C | A: no standing knowledge of an area of work | P: "enterprise knowledge bases" §4.1.5 |
| Domain tools | adapter, connector, enterprise system | P: "enterprise connectors" external §8.5 | P: tools in general | P: L6 "Enterprise Systems" | F: Integration Adapters §4.1.2, placed in a platform layer |
| Domain rules | compliance, regulation, constraint, rule | P: policy sources "organizational, legal, security, privacy, economic" §6.7 | P: guardrails in general | P: L1 "Constraints"; regulatory constraints §VI-C | P: GDPR, SOX, HIPAA controls §6.4; spend thresholds |
| Acceptance criteria | success criteria, acceptance, criteria, verif | P, per request: success criteria S §6.2; verification §14.5 | A: no hits for "success criteria" or "acceptance"; "correctness" appears only as a problem | P: "Goal Fidelity ... goal-completion score" (Table VII); certification requirements | A: nearest is "validating all changes against established business rules" §6.5 |

Totals per source (F / P / A over 36 rows: 24 services, 5 layers including Platform, 7 domain parts):

| Source | Fully | Partly | Absent |
|---|---|---|---|
| A. AOS | 16 | 18 | 2: Improvement, Domains |
| B. Steinder and Franke | 12 | 18 | 6: Directory, Channels, Improvement, Domains, Roles, Acceptance criteria |
| C. ASOC | 8 | 19 | 9: Sessions, Scheduling, Retrieval, Artifacts, Directory, Improvement, Domains, Roles, Domain knowledge |
| D. EAAF | 14 | 19 | 3: Artifacts, Directory, Acceptance criteria |

The Directory and the Domains layer are absent or only partly present in all four; where "partly" is given (AOS Directory, EAAF Domains), the row says how little is there.

---

## 4(c) across the four: identity, definition, instance

| Source | Separates identity from the running instance | Has an agent definition separate from the agent | Persistent versus task agents | Compared with WARM Step 0 |
|---|---|---|---|---|
| AOS | Yes: "a persistent agent identity or a transient runtime instance" | No (capability manifests and provider versions only) | No | Different, and more precise on one point: it names the running instance, which WARM leaves unnamed |
| Steinder and Franke | No: the agent is the container; identity is "a function of" goal, model, skills | Skills only | Sub-agents implied; no persistent agent | Different, and opposite: a change of model or skills changes identity |
| ASOC | No identity concept | No | No | Absent |
| EAAF | Identity per agent; no instance concept | No; versions of the agent itself | No; "Task Agents" is a function | Different and less precise |

Plainly: no source draws WARM's persistent-versus-task distinction. AOS draws a different one (identity versus instance) that WARM lacks and could take. One source (Steinder and Franke) contradicts WARM's rule that identity persists through a change of model or definition.

## 4(d) across the four: cost, conflict, sprawl, confidence

| Theme | AOS | Steinder and Franke | ASOC | EAAF | Where it belongs in WARM |
|---|---|---|---|---|---|
| Cost | Budgets per intent, delegated monotonically; cost in ranking; cost equation; economic reliability | Multi-dimensional quotas; cost accounting | A QoS metric; billing | Absent | Budgets inside a V1 grant, narrowed along a delegation; enforced by Scheduling; metered by Observability; model choice by Models. Keep cost as a concern (changes 3, 4) |
| Conflict between agents | Policy precedence; memory contradiction; arbitration open | Shared-resource conflicts; semantic memory conflict | Emergent coalitions and cascades, no mechanism | Negotiation protocols; agents negotiate responsibilities | Memory already keeps entries current; Policy needs precedence between rule sources (change 9); conflicting outputs go to the accountable domain, and to Approvals if a person must decide. No new service |
| Sprawl, orphaned agents | "Orphaned agent" failure; garbage-collect | Absent | Retirement in the development lifecycle | Decommissioning in the ALM | An owner of which agents exist (change 1); registration gate is V6 |
| Confidence or risk at run time | Central | Risk-based assessment; reversibility classes | Uncertainty estimation; trust calibration | Risk Scoring Engine; trust score | Change 2; reversibility in change 5 |

## Counts

Counted from the inventory tables; Folded rows excluded.

| Source | Items | Clean | Strained | Spans | Guidance | Already planned | Misfits |
|---|---|---|---|---|---|---|---|
| A. AOS (AOS-0001 and AOS-0000) | 69 | 10 | 5 | 22 | 24 | 3 | 5 |
| B. Steinder and Franke | 37 | 14 | 0 | 15 | 6 | 0 | 2 |
| C. ASOC | 60 | 13 | 12 | 12 | 9 | 4 | 10 |
| D. EAAF | 43 | 10 | 4 | 13 | 11 | 0 | 5 |
| Total | 209 | 47 | 21 | 62 | 50 | 7 | 22 |

Not counted (Folded, repeats of a counted item): nine AOS rows marked with a dash (four section 6 objects, the canonical objects, the service provider interfaces, and three AOS-0000 rows), and in ASOC C18, C20 and two grouped rows. The large Guidance share for AOS comes from its twelve design principles and its supporting chapters (deployment, reliability, threats, mathematics), each counted once.

Misfits, one line each:

- A07 AOS Intent management: no part keeps a request's objective, constraints, authority and success criteria.
- A10 AOS Confidence and risk: no run-time assurance that changes control flow.
- A14 AOS Agent lifecycle: no owner of creating, suspending, migrating, ending and cleaning up agents.
- A27 AOS Trust: no standing, decaying assessment of an actor or provider.
- A43 AOS domain: cross-organization federation; out of scope.
- B03 Steinder and Franke Planning: single-agent reasoning; out of scope.
- B06 Steinder and Franke Agent lifecycle: as A14, plus identity defined by current attributes.
- C11 ASOC Consent: no record of who agreed to a delegation.
- C14 ASOC Appeal mechanisms: no review of a decision already made.
- C16 ASOC Goal-oriented interfaces: as A07.
- C19 ASOC SLA negotiation: the open contract question.
- C29 ASOC Reasoning and planning layer: out of scope.
- C34 ASOC Reflection: out of scope.
- C35 ASOC Uncertainty estimation: as A10.
- C56 ASOC Reputation and trust calibration: as A27.
- C57 ASOC Billing models: out of scope.
- C59 ASOC Responsibility allocation across suppliers: liability; out of scope.
- D11 EAAF Risk Scoring Engine: as A10.
- D16 EAAF Planning Engine: out of scope.
- D19 EAAF Feedback Loop Executor: single-agent self-correction; out of scope.
- D30 EAAF Agent Lifecycle Manager: as A14 (its release and adaptation parts fit Releases and Improvement).
- D42 EAAF negotiated responsibilities: contradicts the Directory's design.

Of the 22 misfits, 9 are out of scope by WARM's own Step 0 or single-system boundary, or are WARM's already-stated open contract question (A43, B03, C19, C29, C34, C57, C59, D16, D19). The other 13 fall into four families: agent lifecycle (A14, B06, D30), run-time assessment of risk, confidence and trust (A10, A27, C35, C56, D11), the per-request objective (A07, C16), and human oversight wider than approval (C11, C14), plus D42, which is a contrast with the Directory and not a gap.

---

## What WARM might change

Confidence: high, medium or low that the change is right. "States" means a source says it; "inference" means my reading.

| # | Candidate change | Evidence | Sources | Confidence |
|---|---|---|---|---|
| 1 | **Add an owner for the existence of agents.** Either a new Runtime service (working name "Agents": start, suspend, resume, move and end persistent and task agents; keep the record of which agents exist, who started each and under which definition; end or flag agents whose task or owner is gone), or widen Identity and Tasks explicitly to carry it. Today no service can answer "which agents are running, and who started this one", so orphan and sprawl detection have no home. This would take the count to 25 and contradicts the v0.12 plan that the count stays 24. | States: AOS Table 7 "Agent lifecycle" with failure "Orphaned agent"; AOS §10.2 "garbage-collect"; AOS-0000 §4.2 "Agent Lifecycle Manager"; Steinder and Franke §IV-A primitive 1 and rossoctl "Life-cycle management"; EAAF §5.1.4 ALM with "Decommissioning". v0.11 recorded "agent provisioning" from one platform. | AOS, Steinder and Franke, EAAF (3 of 4); ASOC only as development lifecycle | High that the gap is real; medium on a new service versus widening Identity and Tasks |
| 2 | **State a run-time assessment that Policy may use.** Widen Evaluation to assess before and during an action as well as after (risk of a proposed action, confidence in a result, trust in an actor or provider, with "unknown" when it cannot assess), and say in Policy that a decision may take these as inputs and may return proceed, hold for approval, retry, fall back or stop. Do not add a service unless the widened Evaluation fails a second domain. | States: AOS §6.10, §6.11, §9.6, Table 13; AOS-0000 §4.6 trust and risk states; Steinder and Franke §IV-I "risk based assessment"; ASOC L4 "Uncertainty Estimation", §VI-D trust calibration; EAAF Risk Scoring Engine and Pre-Action Validation Pipeline. The search reader saw the same in AAGMM and Charterion. | All four | High that the gap is real; medium on placement in Evaluation |
| 3 | **Add attenuation to V1.** A grant passed to another agent, including a task agent, is no wider than the grant of the agent that passed it, in scope, expiry and budget; wider authority needs a new grant from someone who holds it. | States: AOS §6.9, §12.6, INV-004; AOS-0000 §4.6 "Actions should be attributed to both the agent identity and the delegating principal"; ASOC delegation contract (scope, duration, revocability). | AOS, ASOC | High |
| 4 | **Say how cost is controlled, not only that it is a concern.** A task carries budgets (tokens, money, time, number and depth of agents it may start) as part of its grant (change 3); Scheduling enforces them; Observability meters them. Cost stays a concern, not a service. | States: AOS §10.7, §12.11; Steinder and Franke §IV-B. The search reader saw it in three more sources. | AOS, Steinder and Franke | Medium |
| 5 | **Tool definitions declare their effects.** A tool entry in the Registry states whether a call has side effects, whether they can be undone (reversible, compensable, irreversible) and whether a retry is safe; Policy can require a stronger grant or an approval for irreversible calls; Tasks uses it to decide whether a retry may repeat an effect. This gives V14's open question a concrete input. | States: Steinder and Franke §IV-D; AOS §6.4, §10.7, §11.11 and glossary "Consequential action"; AOS-0000 §4.5 "side effect classification". | AOS, Steinder and Franke | Medium-high |
| 6 | **The Tasks contract keeps the original request.** A task records the request as received (objective, constraints, the authority it was made under, success criteria), unchanged; later interpretations and plans are versioned beside it, and what was done is recorded apart from what was planned. Domain acceptance criteria remain per domain; this adds per-task criteria. | States: AOS §6.2 ("The original intent is immutable"), §6.6, §10.3; ASOC L2 "Goal-Oriented Interfaces", Principle 5 "Goal specification language". | AOS, ASOC | Medium |
| 7 | **Name the running instance.** Add to Step 0: an agent runs as one or more instances (a process or session that can be restarted or moved); identity, memory and history belong to the agent, not the instance. | States: AOS §10.2; AOS-0000 §2.1. | AOS | Medium |
| 8 | **Human oversight is wider than approval.** Either widen Approvals ("hold actions or questions for a person's decision": clarify a request, approve, review an uncertain result, hear an appeal) or state that clarification belongs to Channels and appeal is outside the model. | States: AOS §7.11, §9.9; ASOC L1 "Escalation Pathways", "Appeal Mechanisms", "Consent". | AOS, ASOC | Low-medium |
| 9 | **Policy states precedence between rule sources.** When rules from a domain, the operator and a person conflict, the decision records which rule applied and why. | States: AOS §9.4; AOS-0000 open problem "policy arbitration across cooperating agents". | AOS | Medium-low |
| 10 | **Identity attests what an agent currently is.** The Identity row adds: attest the definition version, model and harness under which an actor is acting, so Policy can use them, without making them part of the identity. | States: Steinder and Franke §IV-A, §IV-H; AOS §6.10 (attestation as a trust input). | Steinder and Franke, AOS | Low-medium |
| 11 | **Say who notices an agent's silent failure.** One sentence: Reliability keeps services available; a task that reports success for failed work is detected by Evaluation and recovered by Tasks. | States: Steinder and Franke §IV-J ("planning failures returning HTTP 200", "self-concealment"). | Steinder and Franke | Low |
| 12 | **Re-examine Artifacts.** None of the four has a full counterpart, and Steinder and Franke argue no new abstraction is needed because "POSIX file systems still store agent-produced artifacts". Combined with v0.11's three platforms, 0 of 7 have it. Either restate why versioned storage of work products is a platform responsibility (not just a file system the platform uses) or demote it. | States: Steinder and Franke §IV, §VI Lesson 3; absence in ASOC and EAAF (searched); partial in AOS. | Steinder and Franke (against); absence in all | Low that WARM is wrong; high that the evidence for Artifacts is thin |
| 13 | **State the decision-execution split as a property of Governance.** One sentence under V1: the record that an action was authorized and the record that it happened are separate, and neither component may claim the other. | States: AOS §8.2, §9.10, §10.10, INV-006; AOS-0000 §3.3. | AOS (EAAF and ASOC implicitly) | Medium-low |
| 14 | **Scheduling decides where as well as when.** Placement across machines or regions under residency rules has no named owner; Step 2 already asks "how, where and when". | States: AOS §10.6, §12.10; EAAF §5.1.3 "multi-cloud availability zones". | AOS, EAAF | Low |

### Do the decompositions say WARM is cut in the wrong place?

- **The six groups: no source shows a wrong cut.** Three sources cut on another axis, decision versus execution (AOS planes, EAAF control plane, ASOC harness layer). That axis is real and WARM states it only through V1; change 13 adds it as a property, not as a regrouping. ASOC's two cross-cutting planes independently match WARM's two cross-cutting groups. EAAF's layers duplicate components and mix concerns that WARM's placement test separates, which is evidence for the test.
- **The 24 services: one responsibility is missing.** Three of four sources give the run-time lifecycle of agents a top-level component, and AOS names the failure (orphaned agents) that WARM cannot locate. Unless Identity and Tasks are widened explicitly, WARM's list is incomplete. This is the finding to settle before publishing, because v0.12 says the count stays at 24.
- **One service is weakly supported.** Artifacts has no full counterpart in any of the seven systems now mapped (three platforms, four models).
- **Governance lacks an input every source has.** Risk, confidence or trust as a run-time input to Policy appears in all four. WARM can place it in Evaluation without a new service, but it has to say so.
- **The Domain layer and the Directory remain unique to WARM.** Not one of the four has either. EAAF's run-time negotiation of responsibilities is the only alternative found, and its own results report coordination trouble beyond about fifty agents. This is consistent with WARM's claim that the Directory is new; it is not evidence that the Directory works.

### Limits of this mapping

- One mapper, who knew WARM and wrote no predictions first; no second rater.
- Assignments rest on the sources' text. Three of the four have no running system I could inspect; rossoctl exists but its code was not read.
- ASOC's layer contents are figure labels without definitions, so its assignments are the least certain.
- EAAF's reported results lack a method, and its figures appear machine-generated; its components were mapped as written.
- The F/P/A totals depend on the threshold for "partly". Where a source had only a phrase, I used P and quoted the phrase.
