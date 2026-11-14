---
title: "Mapping AAM/5C (Goujon, arXiv:2610.30221) onto WARM v0.11"
date: 2026-11-11
yardstick: warm-model-v0.11.md
source: "Laurent Goujon, Agentic Architecture of Information Systems. The AAM/5C Model: A Reference Model for Distributed Autonomy, arXiv:2610.30221, manuscript V7.83-EN (English translation), October 2026"
status: mapping by one reader; not checked by a second rater
---

# Mapping AAM/5C onto WARM v0.11

## Summary

AAM/5C and WARM describe different things. AAM/5C is a model for making an enterprise information system (IS) run itself: every IT component (gateway, microservice, database, cluster) gets its own agent, and the model's center of gravity is one rule, R-AUT, that controls who may turn an agent's proposal into an act. WARM is a model of the system around agents doing sustained work in several areas of work. The overlap is largest in Governance and Operations, and smallest in Runtime, Knowledge and the Domain layer.

| Count | Value |
|---|---|
| Inventory items | 153 |
| Clean one-part fits | 20 |
| Strained one-part fits | 45 |
| Spans | 36 |
| Guidance (design-time, method, adoption) | 34 |
| Misfits | 18 |

The main results:

1. **The source has no domain.** It has no entity for an area of work, separate from agents or otherwise. "Domain" appears five times in 120 pages, never as an area of work. "Partitioning by domain" is one undefined phrase in a reply to an objection about throughput. Its RACI matrix (Table 14) assigns 14 governance activities to six governance roles and four stakeholders; it assigns no area of work. Its "agentic registry" is a security allowlist, not a directory. This confirms, from a full reading, what WARM v0.11 said after a partial one.
2. **The source splits what WARM's Policy service does in one place.** R-AUT gives proposal, decision, issuance of a one-act token, enforcement and execution to five different holders, with separate signing keys, so that no one component can authorize itself. WARM has no issuing step and does not require decision and enforcement to be separate. Three of the 18 misfits (act token, capability envelope, ephemeral authority surface) are this one gap.
3. **The source makes WARM's enforcement-point condition measurable.** Its hypothesis H8b, "no agentic act bypasses the PEP", is tested by reconciling a log kept on the resource side against the enforcement point's admissions. WARM states the condition and gives no way to check it.
4. **Other misfits point to responsibilities WARM does not assign:** undoing an agent's effect in the world, an emergency stop outside the governance path, stability among many autonomous agents (oscillation), peer consensus before an act, attestation of the integrity of an agent's context, consistency of state across agents, offline continuity, and separation of duties.
5. **Several misfits are out of WARM's scope by design:** the source's capabilities Comprehend and Choose, and its belief-desire-intention vocabulary, describe how one agent reasons. WARM excludes that on purpose.
6. **WARM's own text has a gap the source exposes:** WARM names no service that versions and releases rules. Improvement and Releases list agents, skills, the platform and infrastructure, not rules, while the source treats the policy catalog as the most carefully released object in the system.

## What was read

Source file: the arXiv PDF of 2610.30221 (v1, 2026-10-21), manuscript "V7.83-EN", 120 numbered pages; the PDF's page numbers equal the manuscript's ("n / 120"). Text was extracted page by page with pypdf and read in order.

| Pages | Content | Read |
|---|---|---|
| 1-18 | Title, license, Executive Summary, contents, lists of figures, tables and listings, abbreviations, Preface, Introduction (objective, reading conventions, epistemic grid, state of the art) | in full |
| 19-24 | Chapter 1 (cognitive complexity wall, five Capabilities, A2A and MCP, autonomy levels) | in full |
| 25-33 | Chapter 2 (foundations, five Capabilities and seven layers, R-AUT, agent typology, end-to-end act) | in full |
| 34-40 | Chapter 3 (problem, hypotheses H1-H10, Table 4, evaluation framework) | in full |
| 41-47 | Chapter 4 (six entities, dependency formalization, strata, DAL loop, patterns) | in full |
| 48-52 | Chapter 5 (positioning, Table 6, autonomy levels, migration roadmap, Table 7) | in full |
| 53-55 | Chapter 6 (L1, L2, L3) | in full |
| 56-69 | Chapter 7 (CoT-Validate-Sign-Execute, Listing 2 in Rego, L4-L7, PEP, envelope, key lifecycle, guarantee contract, threats, stability) | in full |
| 70-79 | Chapter 8 (EU AI Act, separation of powers, AOM roles, policy changes, indicators, business model) | in full |
| 80-91 | Chapters 9-11 (assessment, limits, milestones, regulated adoption, conclusion, five principles, author's note) | in full |
| 92-98 | Definitions G.1-G.116 | in full |
| 99-104 | Reference Documents, Declarations | read; references skimmed for content, not checked |
| 105-111 | Appendix 1 (protocols), Appendix 2 (dwell time, TLA+ consensus) | in full |
| 112-117 | Appendix 3 (H7/H8, Table 13 threat matrix, Table 14 RACI), Appendix 4 (14 objections) | in full |
| 118-120 | Appendix 5 (personas), Index | in full |

**Not read:** the content of figures F.1 to F.19. They are images; only their captions were available as text. Figure F.4 ("AAM/5C architecture in layers L1 to L7") and F.15 (separation of powers) may carry relations not stated in the text. The French original and the HAL and Zenodo copies were not compared. The translation was "produced with the assistance of artificial intelligence tools" and validated by the author (p. 104), so wording may differ from the French.

**Searches.** Every absence claim below rests on case-insensitive searches of the extracted text, run with a script that prints each hit with its page. Each search was confirmed able to find a positive (for example, "registry" returned 6 hits, "domain" 5). The terms are listed where each absence is claimed.

## The source in brief

These points matter for every assignment below. All are stated by the source.

- **Scope:** the "agentification" of a large organization's IS, to reduce incident remediation time and toil. Its examples are SRE incidents, zero-day isolation, inventory outages, price changes and energy-aware placement. It "reports no empirical results" and marks every number as a design target.
- **Agents are per component:** "An agentic IS is an Information System in which each component ... is endowed with its own agent" (§1.2.2). A "functional component" couples "a deterministic execution engine and a probabilistic cognitive agent" (G.58).
- **Seven layers** (L1 Channels, L2 Digital and Application, L3 Integration, L4 Orchestration and Processes, L5 Security and Compliance, L6 Data, Knowledge and Governance, L7 Infrastructure and Physical), each with "a single responsibility", on the OSI principle (§2.2.2).
- **One rule, R-AUT:** "L4 proposes, L6 decides, L5 issues, the PEP verifies, the target layer materializes" (Figure F.5 caption).
- **A human operating model (AOM)** of six roles, five human and one held by an agent, that writes, signs, audits and revises the policies (§8.4).

## 1-2. Inventory and assignments

Legend for "Assigned to": **Service** = one WARM service; **Layer** = a WARM layer; **Domain part** = one of the seven parts; **Agent concept** = agent, definition, persistent agent, task agent or role; **SPAN** = several WARM parts, named; **Guidance** = builder, design-time, research-method or adoption guidance that is not a part of a running system; **MISFIT** = WARM has no place for it. Fit is marked only for one-part assignments. Where a choice was between a strained fit and a misfit, the item was called a misfit.

All 153 quotes were checked by script against the extracted text (whitespace and line-break hyphenation normalized). "Kind" is the reader's label, not the source's.

| # | Item | Kind | Where | Definition (verbatim, short) | Assigned to | Fit | Reason |
|---|---|---|---|---|---|---|---|
| 1 | Capture | capability | §1.3.1, Table 2 | "perceive the state of the component and of its environment, qualify the signal against service commitments, route it to reasoning" | SPAN: Domain workflow (intake) + Scheduling (event trigger) + Tools | span | Perceiving a managed IT component is domain work for an IT-operations domain; the event start is Scheduling; the telemetry hookup is Tools. |
| 2 | Comprehend | capability | §1.3.1, Table 2 | "diagnose in context, down to the root cause, by combining probabilistic reasoning and logical invariants" | MISFIT: none (WARM Step 0 excludes single-agent reasoning) | misfit | Out of scope by WARM's own statement: 'WARM does not describe how a single agent reasons'. |
| 3 | Choose | capability | §1.3.1, Table 2 | "plan an explainable action — remediation, reconfiguration, resource optimization — under cost and risk constraints" | MISFIT: none (single-agent planning, out of scope) | misfit | Planning inside one agent is out of WARM's scope; only the model choice it implies touches Models. |
| 4 | Coordinate | capability | §1.3.1, Table 2 | "negotiate among peers, through the A2A protocol, access to resources and service commitments, without a central orchestrator" | SPAN: Messaging + Orchestration | span | A2A carries the messages (Messaging); negotiation of who gets what is coordination (Orchestration). Peer consensus itself has no WARM home (see item on consensus). |
| 5 | Control | capability | §1.3.1, Table 2 | "execute only an act that is authorized under a signed policy, under the R-AUT rule (§2.2.3): this is action control" | SPAN: Policy + Identity + Observability (+ token issuance, a misfit) | span | Decision and enforcement are Policy; the responsible human is Identity; the log is Observability; the issuing step has no WARM service. |
| 6 | L1 Channels | layer | §2.2.2, §6.2, G.69 | "the boundary of the Information System with users, partners and terminals" | SPAN: Channels + Policy (PEP at gateway) + Domain tools | span | Same word as WARM Channels, but L1 is the boundary of the managed business system (customers, bots) as well as the operators' console. |
| 7 | L2 Digital and Application | layer | §2.2.2, §6.3 | "the functional identity of components — their APIs — and their service commitments" | MISFIT: none (closest: Providers, or domain tools) | misfit | L2 is the managed application estate with agents embedded in it. WARM has no layer for the systems agents operate on as the subject of their work; it reaches them only through Tools. |
| 8 | L3 Integration | layer | §2.2.2, §6.4 | "the Agentic Service Bus. It holds the lifecycle and the beliefs of agents ... and reconciles heterogeneous representations" | SPAN: Messaging + Sessions + Policy (enforcement point) + Scheduling (flow regulation) | span | One layer holds message transport, agent state, a PEP and backpressure, which WARM puts in four services across three groups. |
| 9 | L4 Orchestration and Processes | layer | §2.2.2, §7.3 | "transforms a desire into a structured intention. Its language models produce plans through Chain-of-Thought reasoning, in a sandbox" | SPAN: Harness + Environments + Tasks | span | The reasoning loop is Harness, the sandbox is Environments, Saga compensation is Tasks. 'Orchestration' here does not mean WARM's Orchestration. |
| 10 | L5 Security and Compliance | layer | §2.2.2, §7.4 | "continuously evaluates agent behavior ... carries the A2A negotiation ... arbitrates conflicts ... and issues the act token" | SPAN: Evaluation + Messaging + Orchestration (+ token issuance, a misfit) | span | Coordination and security are in one layer; WARM separates Interaction from Governance. |
| 11 | L6 Data, Knowledge and Governance | layer | §2.2.2, §7.5 | "transforms data into actionable knowledge and injects, through MCP, security, compliance and budget policies ... renders the authorization decision" | SPAN: Retrieval + Policy | span | WARM separates Knowledge from Governance; the source fuses them because the policies travel as context. |
| 12 | L7 Infrastructure and Physical | layer | §2.2.2, §7.6 | "the execution substrate, which adjusts its compute resources to actual loads ... and ... its energy resources" | Layer: Infrastructure | strained | The substrate is WARM Infrastructure, but L7 also holds agents that change it; WARM's Infrastructure is passive. |
| 13 | Blocks I and II (upper and lower layers) | structure | Reading conventions, §2.2.2 | "Layers L1 to L3 are called "upper" and form Block I (operational anchoring); layers L4 to L7 are called "lower"" | Guidance: presentation convention | guidance | A reading device, not a part of a running system. |
| 14 | Agent groups: Perception, Cognition, Governance | structure | Reading conventions, §2.3 | "Agents are divided into three groups — Perception (L1–L2), Cognition (L3–L4–L5), Governance (L6–L7)" | MISFIT: none | misfit | WARM groups services, not agents, and does not classify agents by stack position. The source's 'Governance' group includes L7 infrastructure agents, which WARM's Governance group would not. |
| 15 | Sensory agent | agent type | Table 3, G.101 | "Monitors signals, filters noise, detects deviations from service objectives" | Agent concept: role | strained | A role, but defined by stack position (L1-L2); the area of work it serves (IT operations) is never named. |
| 16 | Executive agent | agent type | Table 3, G.54 | "Holds the component's local state and beliefs; turns the qualified signal into a desire; presents authorized acts to the PEP" | Agent concept: role | strained | A role per component; it also holds state, which WARM would put in Sessions. |
| 17 | Cognitive agent | entity / agent type | §4.2.2, Table 3, G.29 | "Probabilistic component of a functional component, belonging to L4: it reasons and proposes acts, subject to the decision of L6" | Agent concept: agent | strained | An actor, but defined as 'a capability of the component', one per component, with no stated identity, roles or persistence. |
| 18 | Social agent | agent type | Table 3, §7.4.1, G.105 | "negotiates via A2A with neighboring agents, arbitrates conflicts and, on the decision of L6, issues the act tokens and capability envelopes" | SPAN: Messaging + Orchestration (+ token issuance, a misfit) | span | One agent combines negotiation, arbitration and authorization issuance. WARM would split these across Interaction and Governance. |
| 19 | Governor agent | agent type | Table 3, G.60 | "renders the authorization decision: it submits each plan proposed by L4 to the policy engine ... it issues no token" | Agent concept: role (platform role held by an agent, WARM Step 4 'Provisional') | clean | Matches WARM's provisional rule that a component providing a platform service (here Policy) may be an agent. |
| 20 | Infrastructure agents and L7 components (autonomous provisioner, energy sobriety agent, hardware self-healing agent) | agent type / components | Table 3, §7.6, G.65 | "Materialize the infrastructure acts verified by the PEP, report back and close the observability loop" | Agent concept: role | strained | Roles in an unnamed infrastructure-operations area of work; WARM would place their subject in Infrastructure and their work in a domain. |
| 21 | Business micro-agents | agent type | §2.2.2, §6.3 | "which extend microservices [Newman 2021] and each carry their own DAL loop" | Agent concept: persistent agent | strained | Long-lived by implication (they hold a cache and state), but the source never states lifetime; identity is the microservice, not a role. |
| 22 | A2A Mediator | role (system role) | §8.4.1, G.2 | "system role, held by an L5 agent ... it facilitates complex negotiations between agents and detects mutual deadlocks" | Agent concept: role (platform role held by an agent; service = Orchestration) | clean | Exactly WARM's provisional case: an agent in a platform role, supervised and audited by people. |
| 23 | Functional component / double helix / one agent per component | entity | §1.2.2, §4.2.1, G.46, G.58 | "it combines two inseparable strands ... a deterministic execution engine and a probabilistic cognitive agent" | MISFIT: none | misfit | The source fuses the agent with the resource it operates. WARM keeps agents on the platform and the systems they act on behind Tools; it has no unit that is both. |
| 24 | Execution engine | entity part | §4.2.1, G.53 | "Deterministic component of a functional component, which executes its operations, including the agentic acts decided by L6" | Domain part: domain tools | strained | It is the managed system's runtime, reached by agents; in WARM that is the far side of a domain tool. |
| 25 | Triple dependency graph F-Dep / O-Dep / C-Dep | entity | §4.2.3, D.C1, G.24, G.113 | "one must understand the intention of the other in order to decide well" | Domain part: domain knowledge | strained | A dependency map of the managed IS is knowledge for an IT-operations domain; WARM has no runtime dependency model between components. |
| 26 | Dependency operators ⊕, ≺, ⊗ (policy priority and arbitration) | formalism | Listing 1 | "≺ is a strict total order on the policies in force ... a policy that the order does not yet rank is not in force" | Service: Policy | strained | Precedence among conflicting rules is part of evaluating rules, but WARM says nothing about rule precedence. |
| 27 | Signed policy | entity | §4.2.4, G.103 | "a deterministic rule, written in a policy language ... that bounds what the AI may propose" | Domain part: domain rules | strained | Content of rules is what domains supply in WARM; here one central organization writes and signs them for the whole system. |
| 28 | Policy engine | component | §7.2, G.84 | "establishes in bounded time ... whether the plan complies with the signed policies, and returns the same verdict for the same input" | Service: Policy | clean | Evaluate rules on an action. |
| 29 | Context | entity | §4.2.5, G.34 | "the agent's working memory, supplied by MCP. It is filtered according to the need to know" | SPAN: Harness (context window) + Retrieval (supply) | span | WARM's table puts working memory in the Harness and fetching in Retrieval; need-to-know filtering is Policy. |
| 30 | Context provider (MCP server of L6) | component | §7.5, G.36 | "aggregates the IS's heterogeneous sources into a single context object, filtered before its injection into L4" | Service: Retrieval | strained | Fetches from named sources, but also acts as a PEP and materializes data accesses. |
| 31 | Primitive action | entity | §4.2.6, G.86 | "the elementary authorized act ... characterized by its criticality (low, moderate, high), its reversibility and its explainability trace" | Domain part: domain tools | strained | A tool operation, but WARM tools carry no criticality or reversibility attributes. |
| 32 | Five internal strata of a component | structure | §4.3, Table 5 | "They describe the interior of a component; they are to be confused neither with the seven layers of the IS nor with the five Capabilities" | Guidance: builder guidance (internal build of one component) | guidance | Implementation detail of a single agent-plus-resource unit. |
| 33 | DAL loop (Distributed Autonomy Loop) | pattern | §4.4, D.C2, G.41 | "Perception, Deliberation, Validation, Execution, Learning" | SPAN: Harness + Policy + Tools + Improvement | span | A per-agent loop whose Validation step is a call to Policy. Compare WARM's workflow template, whose 'verify' comes after execution. |
| 34 | DAL variants (L4-DAL, L6-DAL, AOM-DAL) | pattern | §4.4 | "Every autonomy loop of the model reduces to one of three variants, depending on the step it reinforces" | Guidance: builder guidance | guidance | Design choices about which step to emphasize. |
| 35 | Learning step / socio-technical learning loop (PDCA on policies) | pattern | §4.4, B.C3 | "a PDCA cycle ... applied to policies: explicit criteria trigger their human review, so that no frozen policy becomes a bottleneck" | Service: Improvement | strained | Evidence to proposed change to human decision is WARM's Improvement, but WARM's Improvement names agents, skills and the platform, not rules. |
| 36 | Autonomic patterns (self-configuration/optimization, self-healing/protection, self-explanation) | pattern | §4.6 | "The classical properties of autonomic computing ... become, in the model, reusable patterns" | Guidance: builder guidance (domain work of IT operations) | guidance | These heal and tune the managed IS, not the agent platform, so they are not WARM's Reliability. |
| 37 | Reversibility invariant | rule | §4.4, D.C3, G.90 | "Every act executed autonomously must be reversible in less than 5 minutes ... An act for which the invariant cannot be upheld ... is escalated to the AOM" | SPAN: Policy (rule) + Approvals (escalation) | span | The rule decides what may run without a person; the escalation is Approvals. The undo mechanism itself is a separate misfit. |
| 38 | Attested snapshot and designated means of reversal | mechanism | §4.4 | "a means of reversal designated before the act — a preserved prior state or a tested compensation ... and an attested snapshot" | MISFIT: none (closest: Tasks recovery, Releases rollback) | misfit | No WARM service owns undoing an agent's effect in the outside world. Releases rolls back changes to the system itself; Tasks retries and cancels. |
| 39 | Saga / long-running transaction manager | component | §7.3, G.95 | "compensates a failure with compensating transactions executed in reverse order ... then replans" | Service: Tasks | strained | Recovery of a unit of work is Tasks, but compensation of external effects goes beyond retry and cancellation. |
| 40 | Process optimizer | component | §7.3 | "spots bottlenecks and proposes workaround paths" | Domain part: workflow | strained | Optimizing business processes is domain work on a domain's workflow; no domain is named. |
| 41 | State guarantor | component | §7.3 | "verifies the consistency of states among the L2 micro-agents" | MISFIT: none | misfit | Consistency of state across several agents has no WARM service; Sessions and Memory are per agent or per stretch of work. |
| 42 | Formally defined sandbox | component | §7.3, G.C1, G.96 | "an isolated environment, invariants written as policies, signed traces: a plan leaves it only if no test reveals a violation in it" | SPAN: Environments + Evaluation | span | Isolation is Environments; testing a plan against invariants before acting is Evaluation applied before execution. |
| 43 | R-AUT rule | rule | §2.2.3, G.88 | "distributes the authorization of an agentic act among proposal (L4), decision (L6), token issuance (L5), verification (PEP) and materialization" | SPAN: Harness + Policy + Identity + Tools + Observability (+ issuance, a misfit) | span | WARM covers proposal, decision, enforcement and logging, but in one Policy service; it has no separate issuing authority. |
| 44 | Proposal step (L4) | rule step | §2.2.3 | "The cognitive agent forms an intention to act and submits it, with the context of its reasoning, to L6 through MCP" | Service: Harness | strained | The Harness carries out tool calls the model asks for; here the request never executes itself and goes to a decider first. |
| 45 | Decision step (L6) | rule step | §2.2.3 | "The governor agent renders the authorization decision in accordance with the signed policy in force ... it issues no token" | Service: Policy | clean | Whether an action is allowed. |
| 46 | Evaluation proof | artifact | §2.2.3, G.52 | "Object that L6 signs to record its verdict, authorization or denial" | Service: Policy | strained | It exists because the source splits decision from enforcement; WARM's single Policy service needs no such object between its parts. |
| 47 | Issuance step / act token | artifact / rule step | §2.2.3, §7.2 step 3, G.5 | "Atomic authorization, with explicit scope and bounded duration, issued by L5 on the decision of L6 and verified by the PEP" | MISFIT: none (closest: Identity, Secrets) | misfit | Identity says who acts; Secrets releases stored values at the point of use. Neither mints a single-use grant bound to a decision. |
| 48 | Verification step / Policy Enforcement Point and its five checks | component | §2.2.3, §7.4.3, G.82 | "Deterministic component, interposed between the agent and the resource, that performs five checks before any execution" | Service: Policy | clean | Enforcement is in Policy's responsibility, and WARM's Governance condition names enforcement points. |
| 49 | Materialization step (target layer) | rule step | §2.2.3 | "The verified act is executed by the layer that holds the resource ... which reports back on it" | Service: Tools | strained | Carrying out the call is Tools; the source's targets also include a bus, a gateway and a data provider. |
| 50 | Fail-closed (deny by default) | rule | §2.2.3, §7.4.2 | "the failure of a check results in the rejection of the act (fail-closed: deny by default)" | Service: Policy | clean | A property of how Policy decides. |
| 51 | Action control | principle | §1.1, §7.4.2, G.6 | "each agentic act is authorized individually, or by bounded class by means of a capability envelope, and for a short duration" | Service: Policy | clean | WARM's Policy already decides per action. |
| 52 | Ephemeral authority surface | construct | §1.1, A.C2, G.49 | "Set of acts an agent is authorized to perform within a time × scope window" | MISFIT: none | misfit | WARM has no notion of a time-bounded grant held by an agent; permissions are implicit in Policy. |
| 53 | Capability envelope | mechanism | §7.4.3, G.26 | "Authorization decided by L6 and issued in advance by L5, which delimits a bounded right to act ... local verification by the PEP" | MISFIT: none (closest: Policy) | misfit | A pre-issued, locally verified grant for when the decider is down. WARM has no issuance step and no account of Governance under its own outage. |
| 54 | Atomic revocation | mechanism | §1.1, A.C3, G.14 | "Withdrawal of an agentic authority within a bounded time, independently of the agent's internal state" | SPAN: Identity + Policy | span | WARM never mentions revocation; it would fall between Identity (credentials) and Policy (permissions). |
| 55 | Quarantine list | mechanism | §7.4.2, §7.4.3 | "the agent is placed in quarantine and its tokens in progress are revoked" | SPAN: Identity + Policy | span | Suspending an actor is an Identity state that Policy enforces. |
| 56 | Guarantee contract (six points) | rule | §7.4.3 | "These are obligations of the specification, which every implementation of the model must meet" | SPAN: Policy + Observability + Releases | span | Log before transmission (Observability), single use and revocation freshness (Policy), return to earlier policy (Releases). This is the kind of service contract WARM says it does not yet specify. |
| 57 | Key lifecycle (five service keys, rotation, compromise procedure) | mechanism | §7.4.3 | "The entire security of the model rests on signatures: a lost key blocks the system, a compromised key makes it arbitrary" | Service: Secrets | strained | Holding keys is Secrets; rotation, epochs and a compromise procedure are not in WARM's statement. Custody itself is left unspecified by the source. |
| 58 | Separation of key holders | rule | §7.4.3 | "No entity — human, agentic or administrative — holds two of these keys" | SPAN: Secrets + Identity | span | Which identity may hold which secret; WARM states no such rule. |
| 59 | Epoch (and rollback by republishing under a new epoch) | mechanism | §7.4.3, §8.4.4, G.50 | "Monotonic number carried by every signed object ... an object presented under an epoch earlier than the minimum accepted epoch is rejected" | SPAN: Releases + Policy | span | Versioning with a way back is Releases; rejecting stale objects is Policy enforcement. |
| 60 | Merkle context proof / proof function | mechanism | §7.4.3 | "the signed root ... suffices to prove that an element belongs to the attested context and has not been modified" | MISFIT: none (closest: Memory provenance) | misfit | No WARM service attests the integrity of what is placed in an agent's context. Memory records where an entry came from; that is not attestation. |
| 61 | I-ATT invariant (attested vs self-declared attributes) | rule | §7.2, G.64 | "An authorization may rest only on attested attributes ... A self-declared attribute may only add a restriction" | Service: Policy | strained | A rule on what Policy may trust. WARM says a cross-cutting service must act without the agent's cooperation, but says nothing about the provenance of a decision's inputs. |
| 62 | Separation of powers / tripartite model | principle | §8.3, G.102 | "L4 proposes ... L6 decides ... L5 issues the act token, arbitrates conflicts ... and monitors behaviors" | SPAN: Harness + Policy (+ issuance, a misfit) | span | The institutional view of R-AUT. WARM's Improvement proposes-a-person-decides-Releases-applies is the same pattern for changes, not for acts. |
| 63 | Non-collusion by signature | argument | §8.3, H.C1 | "no layer can alone widen the space of authorized acts, except the governor agent of L6, whose compromise suffices" | Guidance: design argument | guidance | A security argument about the design, not a running part. |
| 64 | Cognitive Zero Trust / Zero Trust agent | principle / component | §7.4.1, G.32, G.116 | "no intent generated by L4 is presumed legitimate: L5 continuously assesses its consistency with the role and context of the issuing agent" | SPAN: Evaluation + Policy | span | Runtime assessment of behavior (Evaluation) used as an input to an authorization decision (Policy). |
| 65 | CoT-Validate-Sign-Execute pattern | pattern | §7.2, G.C3, G.37 | "reason, have L6 validate it on attested attributes, receive an act token, execute under monitoring" | SPAN: Harness + Policy + Tools + Observability (+ issuance) | span | The R-AUT chain as a four-step recipe. |
| 66 | Three prohibited drifts (decorative reasoning, facade validation, signature without a log) | rule / audit check | §7.2 | "a zero denial rate in L6, or a zero rejection rate at the PEP, is a warning signal, not a sign of quality" | Service: Evaluation | strained | Assessing the governance mechanism itself against criteria; carried out by a person each quarter. |
| 67 | Service objectives of the pattern and error budget | rule | §7.2 | "a budget consumed too quickly freezes changes and mobilizes the platform team" | SPAN: Reliability + Releases | span | Availability targets are Reliability; freezing changes is a Releases decision. |
| 68 | Explainability log | artifact | §7.2, G.55 | "brings together, for each agentic act, the reasoning, the evaluation proof, the token and the execution trace" | Service: Observability | clean | Evidence of what agents did. Its five-year retention is a Policy rule on stored data. |
| 69 | Act log (resource side) | artifact | §3.2.4, G.4 | "Log of the acts recorded on the resource side ... kept independently of the policy engine" | Service: Observability | clean | Evidence collected independently of the decider. |
| 70 | Authorization log | artifact | G.15 | "Log of the authorizations issued on the L5–L6 side" | Service: Observability | clean | Evidence of decisions. |
| 71 | Trace reconciliation (instrument for H7b and H8b) | method / check | §3.2.4, App. 3 §3.1 | "H8b verifies that every act in the act log was transmitted by a PEP with an attested identity" | Service: Evaluation | clean | An independent check with a stated coverage, which is WARM's Evaluation including its 'unknown' discipline. |
| 72 | Agentic act | definition | G.7 | "Act originated by an agent ... Human and scripted acts do not fall under it: they remain subject to the IS's access controls" | Service: Identity | strained | Classifying an act by its originator is Identity's job; WARM's Governance does not exempt people or scripts. |
| 73 | Responsible human identity carried by every act token | rule | §7.2 step 3, G.79 | "it carries the responsible human identity, in OpenID Connect (OIDC), the authorized act and its scope" | Service: Identity | clean | WARM Identity: 'who is acting ... and on whose behalf'. |
| 74 | Criticality (low, moderate, high) | attribute | §4.2.6, G.38 | "Classification of an act as low, moderate or high criticality, qualified by the signed policy" | Service: Policy | strained | Used by rules, but WARM has no classification of actions. |
| 75 | Declared policy coverage / policy validity domain | rule | §5.3.2, §5.4.1 | "A catalog of signed policies ... with declared coverage — where no policy applies, no agent acts" | Service: Policy | clean | Default deny outside the rules' scope. |
| 76 | Catalog of signed policies | registry-like artifact | §5.4.1 | "drafted, reviewed and versioned, with declared coverage" | Service: Policy | strained | WARM does not say where rules are held and versioned; the Registry holds agents, tools and skills only. |
| 77 | Policy authority (policy signing key) | component / role | §7.4.3 | "The policy signing key, held by the L6 policy authority; it seals the policy corpus" | Service: Releases | strained | Sealing a version of the rules is a release, but WARM's Releases does not list rules among what it releases. |
| 78 | Agentic constitution | artifact | §8.4.1, G.8 | "Limits of agent autonomy, defined by the Intent Architect ... translated into signed policies of L6" | Domain part: domain rules | strained | Limits are rules; here they are one system-wide set, not a domain's. |
| 79 | Escalation to the AOM | mechanism | §4.4, §3.3.3, G.38 | "The system must refuse the act (R-AUT) and escalate to the competent AOM role" | Service: Approvals | strained | A person decides, but the source refuses the act and escalates; it does not hold the act pending. Finding 'the competent AOM role' is a lookup the source does not specify. |
| 80 | Graduated escalation thresholds | rule | §10.3, J.C2 | "autonomous execution, after-the-fact supervision, prior human validation or exclusion, depending on the risk level and the amount" | SPAN: Policy + Approvals | span | Deferred to future work by the source. |
| 81 | Global emergency stop | mechanism | §8.2, §11.2 | "A global emergency stop, independent of the authorization chain, alerts on a criticality threshold" | MISFIT: none (closest: Tasks cancellation, Policy) | misfit | A stop deliberately outside the normal governance path has no WARM service. |
| 82 | Dual signature | mechanism | §8.3, §8.4.4 | "approved by human dual signature — Intent Architect and Policy Auditor" | Service: Approvals | strained | Approvals holds for 'a person'; two distinct approvers is not stated. |
| 83 | Permissive vs restrictive policy changes | rule | §8.4.4 | "Permissive changes ... are authorized beforehand ... Restrictive changes ... apply without delay ... and are notified afterward" | SPAN: Releases + Approvals | span | An asymmetric release rule: approval only for changes that widen what agents may do. |
| 84 | Agentic gateway (Agentic API Gateway) | component | §6.2, G.9 | "it turns exchanges into signals and distinguishes a user from a scraping bot" | SPAN: Channels + Policy | span | Entry point for requests plus a PEP; bot detection is domain work of a security domain. |
| 85 | Interface agents | component | §6.2 | "which adapt the display to the context, for example to a simplified mode during saturation" | Agent concept: role | strained | Agents inside a customer-facing product; a domain role of a product domain the source does not name. |
| 86 | Edge (IoT) agents | component | §6.2 | "which filter sensor data at the source so as not to clog integration" | Agent concept: role | strained | Same as interface agents. |
| 87 | Partner connectors | component | §6.2 | "which negotiate exchanges between companies via A2A" | SPAN: Channels + Messaging | span | Applications of another organization reaching agents (Channels) over A2A (Messaging). |
| 88 | Local business rule engines | component | §6.3 | "which arbitrate transactions in real time" | Domain part: domain rules | strained | Business logic of the managed application, not agent governance. |
| 89 | Cognitive cache ordered by Lamport clocks | mechanism | §6.3, F.C2 | "a local memory that allows an agent to keep serving when its central source is unavailable, and then to resynchronize cleanly" | MISFIT: none (closest: Sessions, Reliability) | misfit | Offline continuity and later reconciliation of an agent's working data works the same whatever the subject, so by WARM's test it is platform, but no service holds it. |
| 90 | Autonomous degraded mode | mechanism | §6.3, G.17 | "it serves from its local cache and negotiates with its peers, within the limits of a caution policy" | Service: Reliability | strained | Keeps work available during a failure, but of a dependency of the work, not of a platform service. |
| 91 | A2A negotiators | component | §6.3 | "which represent the micro-agents in the negotiation carried by L5" | Service: Messaging | strained | Carrying a micro-agent's side of a negotiation. |
| 92 | Agentic service bus | component | §6.4, G.11 | "interprets and prioritizes messages according to their business intent" | Service: Messaging | strained | Delivers messages, and also prioritizes them by business meaning and holds agent beliefs. |
| 93 | Schema mediators | component | §6.4 | "which reconcile heterogeneous formats by learning, under L6 validation" | Domain part: domain tools | strained | Integration logic for particular systems of record. |
| 94 | Semantic flow regulation / flow regulators | mechanism | §6.4, F.C3, G.100 | "slowing down first the messages that matter least to the business when a system saturates" | Service: Scheduling | strained | Admission under limited capacity is in WARM's Scheduling, but for agent work, not for business messages between systems. |
| 95 | Intent-Based IS | principle | §6.1, F.C1 | "one declares what one wants to obtain; the system breaks it down into operational rules ... and continuously verifies that the intention is being met" | SPAN: Goals + Policy + Evaluation | span | People set the goal, rules bound it, and continuous checking is Evaluation. |
| 96 | Compliance sentinel | component | §7.4.1 | "monitors compliance with the EU AI Act and data residency" | Service: Evaluation | strained | Assessing behavior against criteria, here regulatory, at runtime. |
| 97 | Threat hunter | component | §7.4.1 | "spots attacks — prompt injections, for example — by analyzing behavioral drift" | SPAN: Observability + Evaluation | span | Collecting and judging behavior. |
| 98 | Semantic Data Fabric | component | §7.5, G.99 | "presents relational tables in the form of knowledge graphs" | Service: Retrieval | strained | A representation of named sources for fetching; WARM says nothing about representation. |
| 99 | Integrity agent | component | §7.5 | "guarantees the quality and non-alteration of the sources" | MISFIT: none (closest: Memory currency) | misfit | WARM has no responsibility for the integrity of sources; Retrieval returns 'whatever the source now holds'. |
| 100 | Model registry and attestation of the served model | mechanism | Table 13 | "digest of the model and its version verified at session opening and recorded in the log" | Service: Models | strained | Model mediation is Models; attestation of what model is served is not in WARM. |
| 101 | Model choice per act and multi-model abstraction | rule | §7.2 step 1, §3.3.4 | "a small model suffices for the routine acts of L7, while a large model is justified for the complex transactions of L4" | Service: Models | clean | Choosing the model per task. |
| 102 | A2A protocol | protocol | §1.3.2, G.1 | "Protocol for horizontal cooperation between peer agents: it conveys intents rather than function calls" | Service: Messaging | clean | WARM lists A2A as an industry term for Messaging. |
| 103 | Agent Cards | artifact | §1.3.2 | "Agent Cards describe each agent's capabilities there" | Service: Registry | clean | Discovery metadata for agents. |
| 104 | MCP protocol | protocol | §1.3.2, G.73 | "the model makes it the channel of their reasoning context: security policies, legal constraints, budget, service objectives" | SPAN: Tools + Retrieval + Policy (distribution of rules) | span | WARM files MCP under Tools; the source uses it mainly to deliver context and signed policies. |
| 105 | Dual control loop (dynamic horizontal, static vertical) | pattern | §2.3.1 | "Two loops answer these two needs, one among peers, the other under signed policy" | SPAN: Orchestration + Policy | span | Matches WARM's relation that Interaction coordinates and Governance constrains. |
| 106 | Negotiation scope | rule | §2.3.1 | "To scale, an agent negotiates only with its direct dependencies" | Guidance: builder guidance | guidance | A scaling choice for coordination. |
| 107 | Minimal A2A consensus / peer quorum (Byzantine bound) | mechanism | §7.8, App. 2 §2.2 | "an agent cannot commit a high-criticality act without the agreement of the peers concerned" | MISFIT: none (closest: Approvals, which holds for a person) | misfit | Agreement among peer agents as a precondition to act has no WARM service. |
| 108 | Hysteresis, average dwell time, IT resonance syndrome, critical delay, governance stability | mechanism | §7.8, §8.5, App. 2 §2.1, G.20, G.63, G.68 | "Autonomous agents that each react to their own signals can work against one another and amplify each other" | MISFIT: none | misfit | Stability of many autonomous controllers acting on one system works the same whatever the subject, so by WARM's test it is platform; no service or listed concern holds it. |
| 109 | TLA+ specification of A2A consensus | formal artifact | App. 2 §2.2, Listing 3 | "This excerpt is not executable as it stands" | Guidance: design-time specification | guidance | A design artifact. |
| 110 | Agentic registry | registry | §7.7.1, §8.2, G.10 | "Inventory of the authorized agents and MCP servers, kept by the AOM; only registered servers, with their digests, are admitted" | SPAN: Registry + Policy | span | Inventory is Registry; admitting only registered, digest-matched servers is Policy. |
| 111 | Nine threats, countermeasure matrix, defense in depth | threat model | §7.7, Table 13, Fig. F.13 | "Seven threats target the protocols themselves; each calls for its own countermeasure" | Guidance: design-time threat model | guidance | Security analysis that WARM treats as a concern across groups. |
| 112 | Quarterly red team campaign | activity | §7.7.2, §8.4.1, Table 14 | "The matrix of Figure F.13 sets the minimum scope of a quarterly red team exercise" | Service: Evaluation | strained | Assessing governance against an attack set; done by people. |
| 113 | Behavioral drift detection and recalibration | mechanism | §7.7.1, G.22 | "detected by differential analysis of explainability traces, corrected by periodic recalibration" | SPAN: Evaluation + Improvement | span | Detection from evidence, then a proposed change. |
| 114 | Agentic Operating Model (AOM) | operating model | §8.4, G.12 | "organizes human work around three functions: defining intent, managing context, auditing compliance" | SPAN: People layer + roles | span | A human organization that governs the whole agent system; WARM has people and roles but no governance organization as such. |
| 115 | Intent Architect | role | §8.4.1, G.66 | "defines the business objectives and the agentic constitution, that is, the limits of autonomy, and recalibrates the agents" | SPAN: Goals + domain rules (held by a person) | span | Sets goals and limits for the whole system, not for one area of work. |
| 116 | Context Guardian | role | §8.4.1, G.35 | "guarantees the integrity and freshness of the data supplied to the agents" | Agent concept: role | strained | A human role over Knowledge services; WARM's roles belong to domains, and its platform roles are stated only for agents. |
| 117 | Policy Engineer | role | §8.4.1, G.85 | "drafts, versions and tests the L6 policies and the capability envelopes ... whose release to production the Engineer prepares without authorizing it" | Agent concept: role | strained | Same: a governance role, not a domain role. |
| 118 | Policy Auditor | role | §8.4.1, G.83 | "audits the policies and their application ... the Auditor drafts no policy within the scope being controlled" | Agent concept: role | strained | Same. |
| 119 | Skills Engineer | role | §8.4.1, G.104 | "(skills: the tooled competencies of agents) — develops and validates the primitive actions that agents may invoke" | Agent concept: role | strained | Same; and 'skills' here means tools, not WARM's skills. |
| 120 | Incumbent and deputy for each human role | rule | §8.4.1 | "Each human role is held by an incumbent and a deputy, both designated" | Guidance: organizational guidance | guidance | Staffing rule. |
| 121 | Role incompatibilities (separation of duties) | rule | §8.4.2 | "The same person cannot be both Policy Engineer and Policy Auditor over the same scope" | MISFIT: none (closest: Identity + Policy) | misfit | WARM states no separation-of-duties rule among roles or between who writes and who approves rules. |
| 122 | Three lines of defense | framework | §8.4.2 | "First line — agentic operations ... Second line — agentic assurance and risk ... Third line — internal audit" | Guidance: organizational guidance | guidance | An external control framework applied to the roles. |
| 123 | AOM responsibility matrix (RACI, Table 14) | matrix | §8.4.3, App. 3 §3.3, Table 14 | "Table 14 allocates governance activities among the AOM roles (§8.4.1) and the control stakeholders" | Domain part: roles (of a governance area of work) | strained | It assigns governance activities to governance roles. In WARM that is the roles part of one domain (governance), not the Directory, which assigns areas of work to domains. |
| 124 | Control stakeholders (business owner, CISO, data protection officer, internal audit) | people | §8.4.3, Table 14 | "the 6 roles and 4 control stakeholders (business owner, CISO, data protection officer, internal audit)" | Layer: People | clean | People who direct and approve. |
| 125 | Human on the loop, 'where the rules are set' | principle | §1.1, §11.2 | "The human remains in the loop where the rules are set and where the acts that commit the organization are decided" | Layer: People | clean | WARM's People direct and approve. |
| 126 | Ten steering indicators (Table 8) | metrics | §8.6, Table 8 | "Governance is steered through a dashboard of ten indicators" | SPAN: Observability + Evaluation | span | Measured evidence and judgments against targets. |
| 127 | Measured action control (latency, TPR, FPR on a labeled attack set) | method / check | §8.6, H.C3 | "measured by replay on a labeled attack set (prompt injections, tool poisoning, privilege escalations, emergency-path bypasses)" | Service: Evaluation | clean | Assessing behavior against stated criteria. |
| 128 | Explainability test | method / check | App. 1 §1.3 | "verifies that a human auditor can justify every agentic act from its trace alone" | Service: Evaluation | clean | Assessing a work product (the trace) against criteria. |
| 129 | Sector-modulated thresholds | guidance | §8.6 | "These thresholds are modulated according to the criticality of the sector" | Guidance: calibration guidance | guidance | Parameter values. |
| 130 | Business model for H10 (TCO, net savings, cash ratio, minimum size) | economic model | §8.7, Tables 9-10 | "H10 posits a ratio above 2.5 between the net savings from autonomization and the total cost of ownership" | Guidance: economic guidance | guidance | WARM treats cost as a concern touching several services, not a part. |
| 131 | Toil, MTTR, PAR, TCR (metric definitions) | definitions | G.75, G.81, G.109, G.111 | "Toil — Manual, repetitive, automatable task with no enduring value" | Guidance: metric definitions | guidance | Measures of outcomes, not parts. |
| 132 | Epistemic grid ([TG], [RH], [DT], [EM]) | method | Reading conventions | "a grid that is the only one in the book" | Guidance: research method | guidance | Status labels for claims. |
| 133 | Defensibility scale | method | Reading conventions, §3.3.1, C.C3 | "a five-level defensibility scale qualifies the maturity of the six sub-problems" | Guidance: research method | guidance | Maturity labels. |
| 134 | Hypotheses H1 to H10 (incl. H7a/H7b, H8a/H8b) | method | §3.2, Table 4 | "each accompanied — except for the analytical statements H7a and H8a — by a metric, a measurement instrument and a refutation condition" | Guidance: research method | guidance | Claims to test. |
| 135 | Sub-problems SP1 to SP6 | method | §3.1, G.107 | "agentic integration, distributed coordination, governance and security, systemic stability, performance and cost, reproducibility" | Guidance: research method | guidance | Problem decomposition. |
| 136 | Statistical reproducibility and seeds | method | §3.3, C.C2, G.98, G.108 | "at 95%, over at least 1,000 independent runs of the same scenario" | Guidance: research method | guidance | Evaluation design. |
| 137 | Refutation convention and Scenarios 1 to 4 | method | §3.3.3, App. 1 §1.1-1.2 | "A verdict is valid only if nothing that decides it was chosen after the measurement" | Guidance: research method | guidance | Pre-registration. |
| 138 | Validation milestones G0 to G5 | method | §9.3, Table 11 | "six milestones with quantified stopping criteria" | Guidance: research method | guidance | Research plan. |
| 139 | Reproducibility package | method | App. 1 §1.4 | "every result published on the model is accompanied by an artifact package" | Guidance: research method | guidance | Publication practice. |
| 140 | Autonomy levels 0 to 4 and eligibility criteria | scale | §1.5, §5.3, E.C1, G.19 | "Level 4 — Governed autonomous IS (AAM/5C objective)" | Guidance: maturity scale | guidance | Describes how far a system has gone, not a part. |
| 141 | Migration roadmap (Phases 0 to 4, Phase 0 deliverables, transition milestones) | roadmap | §5.4, E.C2, Table 7 | "No agent is therefore activated before five deliverables are operational and verified" | Guidance: adoption guidance | guidance | Order of building; WARM has the analogous 'platform and Software Factory first' guidance. |
| 142 | Correspondence matrix to agent frameworks (Table 6) | mapping | §5.2, E.C3, Table 6 | "the concept is available natively, it is obtained by assembling existing mechanisms (construction), or it requires an external module (extension)" | Guidance: implementation mapping | guidance | The same kind of exercise as WARM's three-platform mapping. |
| 143 | Conditions of adoption in a regulated environment (Chapter 10) | conditions | Ch. 10, J.C1 | "stated but not resolved" | Guidance: adoption guidance | guidance | DORA, model risk, supply chain, resilience, sovereignty, EA standards. |
| 144 | EU AI Act alignment (Articles 9, 13, 14) | compliance mapping | §8.2 | "The model nevertheless adopts the high-risk requirements as a design reference" | Guidance: compliance guidance | guidance | Regulatory mapping. |
| 145 | Governance by design | principle | §8.1, §11.3, J.C3, G.59 | "a safeguard built into the architecture holds as long as it lies on the path of the act" | Guidance: design principle | guidance | Same claim as WARM's condition that Governance covers an action only if it passes an enforcement point. |
| 146 | Five principles for an IS that lets AI act | principles | §11.4 | "Separate who proposes, who decides and who executes, so that no component can, on its own, turn an error into an act" | Guidance: design principles | guidance | Each restates an item above. |
| 147 | Neuro-symbolic principle / L4-L6 cybernetic coupling | principle | §1.4, §2.1, B.C1, G.77 | "A probabilistic engine can propose but cannot prove; a rules engine can verify but cannot propose" | Guidance: design principle | guidance | Constrains how Policy is implemented (deterministic), which WARM leaves open. |
| 148 | Equivalent requisite variety | principle | §2.1, B.C2 | "the variety proper to each agent and the coordination variety between agents must, together, cover that of the disturbances" | Guidance: theoretical foundation | guidance | Argument for escalation to people. |
| 149 | Six theoretical foundations | foundations | §2.1 | "The model rests on six theoretical foundations" | Guidance: theoretical foundation | guidance | Lineage. |
| 150 | Cognitive complexity wall, cognitive debt, distributed cognitive load | problem framing | §1.1, §1.2.1, A.C1, G.30 | "the threshold beyond which the complexity of the Information System ... exceeds what a team can hold in its head" | Guidance: problem framing | guidance | Motivation. |
| 151 | BDI vocabulary (beliefs, desires, intentions across L3 and L4) | vocabulary | §1.1, §2.2.2, G.21 | "beliefs held in L3, desires addressed to cognition" | MISFIT: none (single-agent reasoning, out of scope) | misfit | An internal model of one agent's mind, spread across two layers. |
| 152 | Partitioning by domain | design avenue | App. 4, Objection 9 | "it proposes a design avenue, to be sized and tested (§10.8): partitioning by domain, with observability of decisions by OpenTelemetry traces" | Guidance: scaling guidance | guidance | A way to shard authorization for throughput; 'domain' is undefined there. |
| 153 | Personas and 'In Practice' vignettes | presentation | App. 5, Table 15 | "Seven personas illustrate the chapters" | Guidance: presentation | guidance | Illustration. |

## 3. The reverse direction: what of WARM the source has

Status: **full** = the source has the responsibility as WARM states it; **partly** = some of it, or under a different scope; **absent** = searched for and not found.

### The 24 services

| Group | WARM service | In the source | Where | Searched (hits) |
|---|---|---|---|---|
| Runtime | Harness | partly | The L4 cognitive agent reasons with "Chain-of-Thought reasoning, in a sandbox" and receives its context through MCP (§2.2.2, §7.2 step 1). Table 6 maps the loop to LangGraph, AutoGen, CrewAI and Semantic Kernel. No service owns the loop; it is inside each component. | "harness" (0), "loop" (many), "context" |
| Runtime | Sessions | absent (agent state only) | L3 "holds the lifecycle and the beliefs of agents" (§2.2.2); the executive agent "holds the component's local state". Nothing keeps the history of a stretch of work so it can pause, resume or hand off. | "session" (2, both unrelated: NIST session credential; model attestation "at session opening"), "history" (0), "resum" (0), "pause" (0), "checkpoint" (0) |
| Runtime | Tasks | partly | The Saga manager compensates and replans long-running transactions (§7.3); the task completion rate is an indicator (Table 8). No lifecycle of a unit of work, no retry or cancellation. | "task" (several, mostly "task completion rate"), "retry/retries" (0), "cancel" (3, all Gartner) |
| Runtime | Environments | partly | The sandbox is "an isolated virtual machine" where a plan is tested before it is proposed (§7.3). Agents act on real components, not in an isolated place. | "sandbox" (many) |
| Runtime | Scheduling | partly | Work starts from signals (event-driven perception, L1-L3). Semantic flow regulation throttles business messages by importance (§6.4). No time-based start, no limits on concurrent agent work. | "schedul" (7, none a scheduler), "cron" (0), "periodic" (7, none a timer), "concurren" (1, unrelated), "queue" (3) |
| Knowledge | Memory | absent | The Learning step says "the result and its trace feed the agent" (§4.4) with no store. "Memory" means working memory (context) or a local cache. | "memory" (7), "learn" (9), "persist" (2, unrelated) |
| Knowledge | Retrieval | full | The L6 context provider "aggregates the IS's heterogeneous sources into a single context object" (G.36); the Semantic Data Fabric; MCP as the context channel. | "retriev" (0); found under "context provider", "MCP" |
| Knowledge | Artifacts | absent | No store of work products. The explainability log stores evidence, not products. | "artifact" (9: research artifacts, SLSA, the reproducibility package) |
| Capabilities | Models | partly | Model choice per act for cost (§7.2), "multi-model abstraction" against provider dependence (§3.3.4), attestation of the served model and a "model registry" (Table 13). No mediating service. | "model provider", "multi-model", "model registry" |
| Capabilities | Tools | full | MCP servers, primitive actions, a versioned allowlist of tools, tool-description digests (§7.7.1, Table 13). | "MCP", "tool" |
| Capabilities | Registry | partly | The agentic registry inventories "the authorized agents and MCP servers" (G.10); Agent Cards describe capabilities (§1.3.2). No versioned agent definitions or skills loaded when a task needs them. | "registry" (6), "catalog" (7), "Agent Card" (3) |
| Interaction | Directory | absent | See 4(c). Nothing records which area of work is accountable for which responsibility, or how to reach it. | "domain" (5), "partition" (3), "owner" (4), "ownership" (12, all "total cost of ownership"), "accountab" (5), "responsib" (31), "director" (0), "department" (0), "business unit" (0), "line of business" (0), "who is responsible" (0), "area of" (1, EU AI Act) |
| Interaction | Messaging | full | A2A between peer agents (§1.3.2), signed messages over mutual TLS (§7.7.1). | "A2A" |
| Interaction | Orchestration | partly | A2A negotiation, local mediation, the A2A Mediator detects deadlocks (§2.3.1, §8.4.1). Coordination is explicitly "without a central orchestrator". No assignment of work by one agent to another, and no tracking of the result that comes back. | "orchestrat", "delegat" (7: token delegation, framework mechanism names), "handoff" (0), "subagent/spawn/worker" (0) |
| Interaction | Channels | partly | L1 is the IS boundary with "users, partners and terminals"; operators "observe the system and bring their intentions" through L1 and a console (§2.2.2, §8.2). There is no account of people conversing with agents or requesting work from them. | "channel", "console" |
| Governance | Identity | full | Every act token "carries the responsible human identity, in OpenID Connect" (§7.2); peers present "a machine identity whose key is valid at the current epoch" (App. 2 §2.2.2). | "identity", "OIDC" |
| Governance | Secrets | partly | Five signing keys, holders, rotation, epochs and a compromise procedure (§7.4.3). Key custody is "not specified in this book". How an agent uses a credential without seeing it is not addressed; standing credentials are treated as a defect ("Agent using a persistent token", Table 8). | "secret" (3), "vault" (1), "credential" (3), "custody" (4) |
| Governance | Policy | full, and split further | Decision (L6), enforcement (PEP), retention ("retained for 5 years", §7.2), need-to-know filtering (§4.2.5), deny by default. | "policy" (very many) |
| Governance | Approvals | partly | Dual human signature on permissive policy changes (§8.4.4); irreversible acts and policy conflicts "escalated to the AOM" (§4.4, §3.3.3); graduated human-validation thresholds deferred to future work (§10.3). No mechanism that holds one act pending a person. | "approv" (13), "human validation" (4), "escalat" (25) |
| Operations | Observability | full | Explainability log, act log, authorization log, OpenTelemetry (§3.2.4, §7.2, App. 4 Obj. 9). | "log", "trace" |
| Operations | Evaluation | full | Measured action control on a labeled attack set, the explainability test, trace reconciliation, sandbox testing, red team, refutation and "inconclusive" verdicts (§8.6, App. 1, App. 3 §3.1). The source also requires the coverage of a record to be published, "without it, a zero count does not distinguish the absence of bypasses from the absence of observation", which is WARM's "unknown" discipline. | "evaluat", "red team", "measure" |
| Operations | Improvement | partly | Learning step and PDCA review of policies; recalibration of agents by the Intent Architect (§4.4, B.C3, §7.7.1). Improves policies and agent calibration; nothing improves skills or the platform. | "learn" (9), "improve" (3), "recalibrat" (6) |
| Operations | Releases | partly | Policy release by dual signature under a new epoch, rollback by republishing, error budgets that freeze changes, pinned MCP server versions (§8.4.4, §7.2, §7.7.1). No release of agents or skills. | "version" (26), "rollback/rolling back/redeploy" (7) |
| Operations | Reliability | partly | Service objectives and an error budget for the context provider and policy engine (§7.2); degraded mode; the envelope as continuity when the decider fails; RTO and RPO deferred (§10.5). The source's "self-healing" heals the managed IS, not the platform. | "availab" (18), "resilien", "RTO" |

### The five layers

| WARM layer | In the source | Where |
|---|---|---|
| People | full | AOM roles, control stakeholders, operators; "Humans, where the rules are set" (§11.2). People appear as rule writers, signers, auditors and escalation targets. They do not appear as requesters of work or as subjects of it. |
| Domains | absent | No area-of-work entity (searches listed under Directory). |
| Platform | partly, not named | No platform layer. Platform responsibilities are spread over L3 to L6. A "governance platform (policy engine, logging, observability, simulated attack campaigns)" appears only as a cost item (§8.7.2). Searched "platform" (13 hits: cost items, personas, audience). |
| Infrastructure | full | L7 Infrastructure and Physical. Unlike WARM, it contains agents that change it. |
| Providers | partly | "Dependence on a model provider" and "compromise of the model provider" (§3.3.4, §7.7.1); public MCP servers. Integrated packages (Salesforce, SAP, Workday) are excluded as having "their own governance" (§9.2). |

### The seven domain parts

The source has an equivalent of every part except a per-domain scope. Each exists once, for the whole system.

| Domain part | In the source | Where |
|---|---|---|
| Goals | partly, system-wide | The Intent Architect "defines the business objectives" (§8.4.1); declared intents in the Intent-Based IS (§6.1); service objectives per component. |
| Roles | partly, system-wide | Six AOM roles (§8.4.1) and six agent types by layer (Table 3). |
| Workflow | partly, generic | The DAL loop and the CoT-Validate-Sign-Execute pattern (§4.4, §7.2). The same steps for every act; there is no workflow per area of work. |
| Domain knowledge | partly | Context via MCP, the Semantic Data Fabric, the dependency graph (§4.2.3, §7.5). |
| Domain tools | partly | Primitive actions and MCP servers, developed by the Skills Engineer (§4.2.6, §8.4.1). |
| Domain rules | full, system-wide | The signed policy catalog (§5.4.1). Rules are partitioned inside a policy, not by domain: Listing 2 caps discounts by `input.attested.product_segment`. |
| Acceptance criteria | partly | Sandbox invariants checked before an act (§7.3); after the fact, a "correctness rate — the share of actions judged relevant after the fact" (§3.3.2). No criteria for work products of an area of work. |

### The Directory

Absent. Searched as listed above. The nearest items, none of which records which area of work is accountable for a responsibility and how to reach it:

| Nearest item | Why it is not a Directory |
|---|---|
| Agentic registry (G.10) | An allowlist of authorized agents and MCP servers with digests. It says what may run, not who is accountable for what. |
| Agent Cards (§1.3.2) | Describe an agent's capabilities. A capability catalog is what WARM calls the Registry. |
| RACI matrix (Table 14) | Assigns governance activities to governance roles. Static, organizational, and about running the governance itself. |
| "escalate to the competent AOM role" (§3.3.3) | Requires finding the competent role, but the source does not say how. |
| "a register of responsibilities" (§10.3) | Named once, as a condition for settling "Liability for a loss caused by an autonomous action", deferred to future work. It is about legal liability for acts, not routing work. |
| "Layer or role" column of Table 13 | Assigns each threat's countermeasure to a layer or role. A design-time table. |

## 4. Findings

### (a) Misfits and spans, and what each suggests

Misfits (18):

| # | Misfit | What it suggests about WARM |
|---|---|---|
| 2, 3, 151 | Comprehend, Choose; BDI vocabulary | Nothing. Single-agent reasoning is out of WARM's scope by Step 0. |
| 7 | L2 Digital and Application | A boundary question. WARM has no named place for the systems agents operate on as the subject of their work (an enterprise's own applications). WARM reaches them through Tools and might call them Providers or "infrastructure the system manages". Inference: worth one sentence in Step 1, not a new layer. |
| 14 | Agent groups by stack position | Nothing. WARM classifies services, not agents, by design. Note the word clash on "Governance". |
| 23 | Functional component (agent fused with its resource) | Nothing for WARM's structure; it is a different architecture. Inference: under WARM, the source's design is one domain (IT operations) whose agents each hold a role tied to one component. WARM can describe that; the source's fusion of agent and resource is an implementation choice. |
| 38 | Attested snapshot and designated means of reversal | **Missing responsibility.** No WARM service owns undoing an agent's effect in the outside world. WARM's Releases rolls back changes to the system; Tasks retries and cancels. WARM already notes that repeating an effect "depends on the contract between Tasks, Tools and the outside system"; compensation belongs in that contract. |
| 41 | State guarantor (consistency of state across agents) | Possibly missing, low weight. WARM's Sessions and Memory are per agent or per stretch of work; WARM has no statement about consistency of state that several agents share. Its own Tasks note ("duplicated state") touches it. |
| 47, 52, 53 | Act token, ephemeral authority surface, capability envelope | **Missing responsibility or a service to split.** WARM has no step that turns a positive decision into a scoped, time-bounded, single-use grant that an enforcement point checks. See 4(b). |
| 60 | Merkle context proof | **Missing responsibility (attestation).** Nothing in WARM attests that the context an agent or a policy decision used is unaltered. |
| 81 | Global emergency stop | **Missing responsibility.** A stop that works when Governance itself is wrong or compromised. WARM's provisional note already asks for a way to repair a service "that does not pass through itself"; the source applies the same reasoning to Policy. |
| 89 | Lamport-ordered local cache | Possibly missing, low weight. Offline continuity and reconciliation of an agent's working data is generic, so by WARM's test it belongs to the platform. Could fit inside Sessions or Reliability if either were widened. |
| 99 | Integrity agent | Same gap as 60: integrity of sources. WARM's Retrieval deliberately returns "whatever the source now holds". |
| 107 | Minimal A2A consensus / peer quorum | Possibly a generalization of Approvals ("hold until authorizers agree", where authorizers can be peer agents) or an Orchestration contract. Low confidence; the source calls its own stability claims heuristic. |
| 108 | Hysteresis, dwell time, resonance | **A concern that is not a group**, like Security and Cost: stability of many autonomous agents acting on shared resources. It touches Orchestration, Policy and Scheduling. The source itself marks it [RH] and unmeasured. |
| 121 | Role incompatibilities (separation of duties) | **A missing relation** in Governance: who writes a rule and who approves it must be distinct identities. WARM says its relations among people are "not developed in detail"; this is one to develop. |

Spans (36), grouped by what they suggest:

| Spans | What they suggest |
|---|---|
| L3, L4, L5, L6, social agent (8, 9, 10, 11, 18) | The source's layers mix responsibilities that WARM keeps apart: L5 puts negotiation (Interaction) with token issuance and behavior checks (Governance and Operations); L6 puts knowledge with authorization. Nothing for WARM: these spans follow from a stack design and support WARM's choice of single-responsibility services. |
| R-AUT, Control, separation of powers, CoT-Validate-Sign-Execute, guarantee contract (5, 43, 56, 62, 65) | Same split as the token misfits; see 4(b). |
| Atomic revocation, quarantine, epoch, separation of key holders (54, 55, 58, 59) | WARM's Identity, Secrets and Policy statements do not mention revocation, suspension of an actor, or rotation. A one-clause addition each, not a new service. |
| Reversibility invariant, graduated thresholds, permissive vs restrictive changes (37, 80, 83) | Approvals is more varied in the source than "hold for a person": escalation without holding, thresholds by risk and amount, and approval only for changes that widen authority. |
| Cognitive Zero Trust, threat hunter, drift detection, indicators (64, 97, 113, 126) | Evaluation used at runtime as an input to Policy. WARM states Operations observes Governance; it does not state that Evaluation results feed Policy decisions. A relation, not a service. |
| Agentic registry, MCP (104, 110) | Registry plus admission. WARM's Registry says what exists; deciding what may be loaded is Policy. No change. |
| Context (29) | Already split this way in WARM's "Where what an agent knows is kept" table. No change. |
| Capture, Coordinate, DAL loop, dual control loop, sandbox (1, 4, 33, 42, 105) | The source's per-agent loop puts authorization (Validation) between plan and act, and testing before acting. WARM's workflow template verifies after execution. Inference: WARM could note that verification can come before an act (a dry run) as well as after. |
| Agentic gateway, partner connectors, L1 (6, 84, 87) | Channels plus an enforcement point. Supports WARM's widening of Channels to applications. No change. |
| AOM, Intent Architect, Intent-Based IS (95, 114, 115) | People setting goals and limits for the whole system rather than for one area of work. See 4(c). |
| Service objectives and error budget (67) | Reliability and Releases already relate in WARM ("A release can require an approval"); an exhausted error budget freezing releases is another such relation. No change. |

### (b) Relations the source states that WARM does not, or contradicts

**R-AUT against WARM's Governance.** The source states the rule as five steps (§2.2.3):

| R-AUT step | Holder | Source's wording | WARM equivalent |
|---|---|---|---|
| Proposal | L4 cognitive agent | "forms an intention to act and submits it ... to L6" | The Harness carries out a tool call the model asks for, and "Policy checks each call" (Example, step 2). |
| Decision | L6 governor agent | "renders the authorization decision ... recorded in an evaluation proof that it signs; it issues no token" | Policy: "whether an action is allowed". Approvals for a person's decision. |
| Issuance | L5 issuance service | "issues the act token — atomic, with explicit scope, with a bounded validity period, bound to the verdict ... No agent issues, renews or extends its own token" | **None.** Secrets "release[s] each one only to the component that needs it, at the point of use"; Identity establishes "who is acting ... and on whose behalf". |
| Verification | PEP | "deterministic and non-cognitive, placed on the execution path, verifies the token before any materialization and records the admitted act" | Policy ("evaluate and enforce"); WARM Step 2 point 1, enforcement points. |
| Materialization | the target layer | "executed by the layer that holds the resource" | Tools. |

What the comparison shows:

1. **Agreement on the enforcement point, with the source going further.** WARM: "Governance covers an action only if the action passes an enforcement point. A call that reaches a tool, a model or a store without passing one is not governed, whatever the rules say." The source: "An agentic act not presented to a PEP is an unauthorized act." WARM's statement is descriptive (such an act is ungoverned); the source's is normative (such an act is forbidden), and it turns the condition into a refutable hypothesis, H8b, measured "on the resource side by verifying that each act in the act log was forwarded by a PEP of attested identity". The source also names the instrument's blind spot: "This instrument does not see an act that an agent causes to be executed under the identity of a script or a human". WARM's condition has the same blind spot and does not say so.
2. **The source separates decision from enforcement; WARM puts both in Policy.** WARM's Policy is one responsibility, "Evaluate and enforce rules". The source requires the decider, the issuer and the enforcer to be different components with different keys, so that "no component can, on its own, turn an error into an act" (§11.4) and "a compromised agent can propose, it cannot authorize itself" (Introduction). Inference: WARM, as written, would map an implementation in which an agent's own harness evaluates and enforces its rules cleanly to Policy. The source would reject that implementation ("local issuance is excluded by construction"). This is not a contradiction of a WARM relation; it is a constraint WARM does not state. It also does not contradict WARM's single-responsibility cut: the source's PEP "does not deliberate and interprets no intent", so decide and enforce are two responsibilities that WARM currently names as one.
3. **Issuance has no WARM home, but WARM's own example already has the shape.** WARM's dispute example, steps 6 and 7: "The proposed send is checked. The rule requires a person, so the action is held ... The person approves. Only then is the mail credential released and the message sent." That is decide (Policy, Approvals), then release (Secrets), then act (Tools): the R-AUT order. What WARM does not state, and the source does, is the binding: the release is for that one act, its scope matches the decision, it expires, and the enforcing point checks the link. In WARM, Secrets releases a stored credential; the source mints a new grant per act and treats a standing credential as a defect (Table 8, indicator 6: "Agent using a persistent token — Block it and migrate it to action control").
4. **Approvals sits at a different place.** The source puts people "where the rules are set" (§11.2): they co-sign policies, and an act needs a person only when it is irreversible, when policies conflict, or when no policy covers it. It does not describe holding an act pending a person; it denies and escalates. WARM's Approvals holds the act. Inference: both are valid; WARM's Approvals statement fits per-act human approval and does not describe rule-level approval or escalation-after-denial.
5. **Identity and attribution.** Both put the person on whose behalf an act runs into the record (WARM Identity: "on whose behalf"; source: the token "carries the responsible human identity"). The source adds a rule WARM lacks: acts under a pre-issued envelope, which no person requested, are "attributed to the co-signatories of the policy that underlies the envelope" (§7.4.3). WARM does not say whom an unattended job's act is attributed to.
6. **Logging as a precondition of enforcement.** The source's guarantee contract: "the PEP writes the admitted act to the explainability log before transmitting it to the target layer; the failure of this write amounts to rejection." WARM says Operations observes Governance; it does not say that a failure to record blocks the act.
7. **Inputs to a decision.** The source's I-ATT invariant: "An authorization may rest only on attested attributes ... A self-declared attribute may only add a restriction". WARM requires a cross-cutting service to "act on an action without the cooperation of the agent that performs it", which covers the action side. I-ATT covers the input side: the decision must not trust what the agent says about itself. WARM is silent on that.
8. **Determinism of the decider.** WARM: "A platform service may use a model or an agent inside it." The source requires the authorization verdict to come from "a deterministic symbolic layer", wrapped by a governor agent, because "a probabilistic engine can propose but cannot prove". Not a contradiction: the source's governor is an agent around a deterministic engine, which WARM permits. Inference: for Policy specifically, WARM could state that the same input gives the same verdict.
9. **Governance under its own failure.** The source states what happens when the decider is unavailable: low and moderate acts proceed under pre-issued envelopes, high-criticality and irreversible acts are denied (§7.4.3, "Accepted bound"). WARM does not address the availability of Governance services.
10. **Scope of governed acts.** The source applies R-AUT to agentic acts only: "Human and scripted acts do not fall under it: they remain subject to the IS's access controls" (G.7). WARM's Identity covers "each agent, person and service" and does not exempt people or scripts. A difference of scope, not a contradiction.

Other relations stated by the source and absent from WARM:

- **Asymmetric change control:** permissive changes need prior dual approval; restrictive changes "apply without delay ... because a default refusal creates no new security risk" (§8.4.4). WARM says a release "can require an approval" and does not distinguish direction.
- **Evaluation feeds Policy at runtime:** L5's behavioral assessment is an "attested attribute ... passed to L6, which decides" (G.116). WARM states Operations observes and changes the other groups; not that an Evaluation result is an input to a Policy decision.
- **Release of policy changes is rate-limited for stability:** "the Policy Auditor ensures that no permissive change is propagated below τD" (§8.5). WARM has no relation between Releases and the stability of running agents.

### (c) Business domains, ownership, roles and RACI, registry, agent lifetime

**Does the source have a domain as an entity separate from agents?** No. The source has no area-of-work entity at all. All five uses of "domain":

| Page | Use | Meaning |
|---|---|---|
| 50 | "the validity domain of a policy plays the role of the vehicle's operational domain" | Where a policy applies (by analogy to SAE J3016). |
| 50 | "escalates outside its domain" | Same: outside policy coverage. |
| 50 | "within a bounded domain" | Same. |
| 116 | "partitioning by domain" (twice in context) | Undefined; see below. |

**"Partitioning by domain."** Full context (Appendix 4, Objection 9, "Does action control hold at 100,000 acts per second?"): "The book does not establish it; it proposes a design avenue, to be sized and tested (§10.8): partitioning by domain, with observability of decisions by OpenTelemetry traces. A verdict cache is excluded: it would delay the handling of revocations. Scaling goes through the capability envelope (§7.4.3), not through memorizing past decisions." The phrase is a throughput technique for the authorization chain. The book never says what a domain is, who owns it or what partitions it. Inference: it most likely means sharding policy evaluation by scope. It is not WARM's domain, and it is not evidence for or against WARM's Step 4.

**What the source partitions by instead.** By technical layer (L1 to L7), by component ("each component ... is endowed with its own agent"), and, for governance, by "scope", which it never defines: "The same person cannot be both Policy Engineer and Policy Auditor over the same scope; holding both roles over disjoint scopes is allowed and declared" (§8.4.2); "A policy change ... changes at once the authorized behavior of all the agents within a scope" (§8.4.4). Business areas appear only in passing: "business micro-agents — for example the inventory agent" (§6.3), a pilot on "an identified banking business process (fraud control or dynamic know-your-customer)" (Table 11), sector thresholds for finance, healthcare and industry (§8.6), and discount caps keyed by `product_segment` inside one policy (Listing 2). Inference: in WARM's terms the source describes one domain (operating an enterprise IS) plus a governance function, and its business agents (inventory, pricing) do the work of domains it never names. This matches WARM's "When the Domain layer matters": "A system built for one purpose has one domain and may never name it."

**Ownership and accountability.** The source assigns accountability per act and per rule, not per area of work:

- Per act: "every act token carries the identity of a responsible human" (§11.2); principle 3, "Attach every act to a policy and to a human who answers for it" (§11.4).
- Per rule: policies are "approved by human dual signature — Intent Architect and Policy Auditor" (§8.3); envelope acts are "attributed to the co-signatories of the policy" (§7.4.3).
- Per agent: once, in a vignette: "Karim owns the inventory agent of an omnichannel retailer" (§6, In Practice; persona table: "owner of the inventory agent"). No ownership relation is defined.
- For the whole: the "business owner" stakeholder is Accountable for one RACI row, the annual risk reassessment.
- Deferred: "Liability for a loss ... will also have to be settled: an enforceable chain of decision, a register of responsibilities and articulation with internal control and insurance" (§10.3).

WARM's Step 4 says "exactly one domain is accountable for each responsibility" at the grain where work is handed between domains, and the Directory records it. The source has nothing at that grain.

**Roles.** "The AOM comprises six roles: five are held by people, the sixth by an agent" (§8.4.1): Intent Architect, Context Guardian, Policy Engineer, Policy Auditor, Skills Engineer, and the A2A Mediator ("system role, held by an L5 agent"). Every one is a governance role for the whole system. The agent types of Table 3 (sensory, executive, cognitive, social, governor, infrastructure) are roles by stack position. No role is defined by an area of work. The A2A Mediator is the one clean match to a WARM idea: WARM's provisional rule that "A component that provides a platform service may itself be an agent ... Such a role belongs to the platform."

**RACI (Table 14).** Columns: the six AOM roles plus four control stakeholders (business owner, CISO, data protection officer, internal audit). Rows, all 14:

| RACI activity | WARM service it touches |
|---|---|
| Definition of the agentic constitution | Policy (rule content), Goals |
| Writing, versioning and testing of Rego policies | Policy, Releases |
| Putting a policy into production after dual signature | Releases, Approvals |
| Periodic review of capability envelopes | Policy |
| Curation of the Semantic Data Fabric | Retrieval |
| Development and validation of primitive actions | Tools |
| Review of MCP servers before adoption | Registry, Policy |
| Continuous audit of traces, drift detection, search for pattern drifts | Evaluation, Observability |
| Detection of A2A mutual deadlocks | Orchestration |
| Quarterly red team campaign | Evaluation |
| Triggering of the emergency stop | (misfit: emergency stop) |
| Immediate restriction of a policy | Policy, Releases |
| Handling of a compliance incident | Evaluation, Policy |
| Annual risk reassessment and acceptance of residual risk | People (business owner accountable) |

**Plainly: the RACI assigns governance activities only.** Every row is an activity of governing the agent system; no row names an area of business work (inventory, payments, pricing). It is therefore not a directory in WARM's sense, which records "which domain is accountable for each responsibility, and how to reach a role of that domain". In WARM terms, Table 14 is the roles part of one domain: governance of the agent system itself. WARM v0.11 described it as "a matrix that assigns governance activities to governance roles"; the full reading confirms that description.

**Registry.** "Agentic registry — Inventory of the authorized agents and MCP servers, kept by the AOM; only registered servers, with their digests, are admitted" (G.10). It answers "what is allowed to run", a Registry-plus-Policy question. It carries no responsibilities, no accountable party and no route to a role. The only other registries are a "model registry" (one table cell, Table 13) and a "reliable service catalog" that Phase 0 assumes the estate already has (§5.4.1).

**Long-lived versus per-task agents.** The source does not draw the distinction. Agents are per component and implicitly long-lived: "Each agent continuously runs a Distributed Autonomy Loop" (§4.4); micro-agents keep local caches (§6.3); the executive agent "holds the component's local state". Searches for "subagent", "spawn" and "worker" return nothing; no agent starts another. What the source makes short-lived is authority: act tokens valid "300 to 800 ms", envelopes with "a short expiry", "ephemeral authority surface". Inference: the two models make opposite things ephemeral. WARM keeps identity and records and lets agents be short-lived (task agents); the source keeps agents and makes their permissions short-lived. These are compatible: a WARM task agent could act under per-act tokens.

**Compared with WARM Step 0 and Step 4.**

| WARM | The source |
|---|---|
| An agent is "an identified actor that carries out one or more assigned roles". | A cognitive agent is "a capability of the component"; each agent has one type by layer. Identity is a machine identity with a key (App. 2). No agent holds several roles. |
| An agent definition describes a role, can be shared and revised. | No agent definition. "Recalibration" by the Intent Architect changes agents (§7.7.1); how is not stated. |
| Persistent agents and task agents, by lifetime. | Not distinguished; all agents implied persistent. |
| A domain is a charter with seven parts, and does not act. | No domain. The seven parts exist once, for the whole system (see section 3). |
| One domain is accountable for each responsibility; the Directory records it. | Accountability per act (a responsible human) and per policy (two signatories). No register of responsibilities, except as deferred liability work. |

### (d) Same word, different meaning

| Word | Source | WARM |
|---|---|---|
| channels | L1, "the boundary of the Information System with users, partners and terminals", including bot detection on customer traffic. | The service that carries requests and results between agents and the people and applications that use them. |
| registry | Agentic registry: an allowlist of authorized agents and MCP servers, with digests, for admission. | Versioned definitions of agents, tools and skills, found and loaded when a task needs them. |
| orchestration | L4 "Orchestration and Processes": an agent's reasoning and planning, plus long-running transaction management. Also "agent orchestration frameworks" for libraries such as LangGraph. Coordination among agents is explicitly "without a central orchestrator". | Coordinating assignments among agents, people and fixed steps: who does what and the results that come back. |
| governance | (1) L6, "Data, Knowledge and Governance"; (2) an agent group, Governance (L6-L7), which includes L7 infrastructure agents; (3) a "governance platform" of policy engine, logging, observability and attack campaigns; (4) "governance by design". | A group of four services: Identity, Secrets, Policy, Approvals. Observability and Evaluation are in Operations. |
| domain | Where a policy applies ("validity domain of a policy"), and once, undefined, "partitioning by domain". | An area of work, defined by a charter of seven parts. |
| skills | "the tooled competencies of agents": the primitive actions the Skills Engineer builds. | Packaged instructions for a kind of task, held in the Registry. |
| evaluation | L6's "evaluation proof": the record of a policy verdict. | Assessing behavior and work products against criteria. |
| capability | One of the five functions (Capture to Control); "capability envelope", a bounded authorization. | Capabilities group: Models, Tools, Registry. |
| layer | Seven layers "on the principle of the OSI model", each with one responsibility, a request path from L1 to L7. | Five logical categories relative to a system boundary; the service groups are "not a layering". |
| sandbox | A test space where a plan is dry-run before it is proposed. | A place where an agent acts, isolated from others (Environments). |
| context | "the agent's working memory, supplied by MCP". | The same idea, held by the Harness; WARM does not tie it to one protocol. |
| agent | A probabilistic part of an IT component. | An identified actor that fills roles. |

## 5. Counts

| Category | Count | Share |
|---|---|---|
| Inventory items | 153 | 100% |
| Clean one-part fits | 20 | 13% |
| Strained one-part fits | 45 | 29% |
| Spans | 36 | 24% |
| Guidance | 34 | 22% |
| Misfits | 18 | 12% |

The 65 one-part fits break down as follows.

| Target | Clean | Strained |
|---|---|---|
| A WARM service | 16 | 24 |
| An agent concept | 2 | 11 |
| A domain part | 0 | 9 |
| A WARM layer | 2 | 1 |

Clean fits by target: Policy 6, Observability 3, Evaluation 3, People layer 2, Identity 1, Messaging 1, Registry 1, Models 1, and two platform roles held by agents (governor agent, A2A Mediator). No item fits a domain part cleanly. Thirteen of the 16 clean service fits are in Governance and Operations.

Notes on the counts:

- Granularity was chosen by the mapper. Some items group several named things (for example, one item for all three L7 agents, one for the stability mechanisms). A finer split would raise the counts of strained fits and misfits more than clean fits.
- Guidance is high (22%) because about half the book is research method, adoption and economics.
- Compared with the three platform mappings in WARM v0.11 (64% to 67% to one service or layer), this source fits less: 42% to one part, clean or strained. The source is a reference model, not a product, and its subject differs, so the comparison is loose.

## What WARM might change

Each item gives the change, the evidence in this source, and a confidence. Confidence reflects one source read by one mapper with no second rater.

| # | Candidate change | Evidence | Confidence |
|---|---|---|---|
| 1 | Name rules among the things Releases versions and Improvement proposes changes to, and say where rules are held (Registry or Policy). | WARM's Improvement lists "agents, skills and the platform"; Releases lists "agents, skills, the platform and the infrastructure"; neither lists rules, though Step 4 has domains supply them. The source's policy catalog is "drafted, reviewed and versioned"; policies are released under epochs with dual signature and rolled back by republishing (§5.4.1, §8.4.4); its learning loop is "a PDCA cycle ... applied to policies". | high |
| 2 | Give WARM's enforcement-point condition a way to check it: an independent record on the resource side, reconciled against enforcement-point admissions, published with its coverage, and with the stated blind spot (acts run under a person's or a script's identity). | H8b, its instrument and its limit (§3.2.4, App. 3 §3.1); the Phase 0 closure criterion (§5.4.1). | high |
| 3 | State the decide-then-grant relation in Governance: a credential or grant is released only on a positive Policy or Approvals decision, scoped to that action, time-bounded, and checked by the enforcement point. Either widen Secrets ("release values and issue grants") or split a grant-issuing responsibility out of Policy. WARM's own dispute example already follows this order. | R-AUT issuance step, act token, capability envelope, ephemeral authority surface (3 misfits, 5 spans); NIST SP 800-207's split of policy engine, administrator and PEP, which the source cites as precedent. | medium |
| 4 | Say whether WARM requires the component that decides to be separate from the one that enforces, and from the one that proposes. At minimum, state that an agent cannot grant itself authority. | R-AUT; "local issuance is excluded by construction"; non-collusion argument (§8.3). | medium |
| 5 | Add revocation and suspension to the statements of Identity and Policy, and rotation to Secrets. | Atomic revocation, quarantine list, epochs, key lifecycle (§7.4.2, §7.4.3). | medium |
| 6 | State that a failed write of the record of an action blocks the action (Observability as a precondition of enforcement), or record that WARM chooses not to. | Guarantee contract, "Log before transmission" (§7.4.3); H7a. | medium |
| 7 | Assign a responsibility for undoing an agent's effect in the world: a designated means of reversal before an act, and compensation on failure. Most likely as part of the Tasks contract that WARM already says depends on "Tasks, Tools and the outside system". | Reversibility invariant, attested snapshot, Saga (§4.4, §7.3). | medium |
| 8 | Say what happens when a Governance service is unavailable (deny by default, or a bounded pre-authorization). | Capability envelope and its "Accepted bound" (§7.4.3). | medium-low |
| 9 | Add an emergency stop that does not pass through Policy, or say where it lives. | Global emergency stop "independent of the authorization chain" (§8.2); RACI row. WARM's provisional note on services that cannot recover through themselves. | medium-low |
| 10 | Add the input side to the cross-cutting condition: a Policy decision rests only on attributes the acting agent did not produce. | I-ATT (§7.2), Listing 2. | medium-low |
| 11 | Widen Approvals beyond "a person authorizes": several approvers, escalation after denial, approval only for changes that widen authority, thresholds by risk. | Dual signature, escalation to the AOM, permissive vs restrictive changes, graduated thresholds (§8.3, §8.4.4, §10.3). | medium-low |
| 12 | Develop one people relation WARM says is undeveloped: separation of duties between who writes a rule and who approves it. | Role incompatibilities, separation of key holders (§8.4.2, §7.4.3). | medium-low |
| 13 | Add "stability" to "Concerns that are not groups", next to Security and Cost: many autonomous agents acting on shared resources can oscillate; it touches Orchestration, Policy and Scheduling. | IT resonance syndrome, hysteresis, dwell time, minimal consensus (§7.8, §8.5, App. 2). The source marks all of it [RH] and unmeasured. | low |
| 14 | Say where the systems agents operate on as the subject of their work sit (an enterprise's own applications): Providers, "infrastructure the system manages", or the far side of domain tools. | L2 misfit; functional component (§2.2.2, §4.2.1). | low |
| 15 | Attestation of context and source integrity as part of Retrieval or Memory. | Merkle context proof, integrity agent, Context Guardian (§7.4.3, §7.5, §8.4.1). | low |

No change suggested by: Comprehend, Choose and the BDI vocabulary (out of scope by design); the source's layer mixing (it supports WARM's cut rather than challenging it); the source's evidence on domains and the Directory. The source neither has a Directory nor argues against one. It offers no support for WARM's Domain layer and no evidence against it; it is one more system that does without domains.

## What in WARM the source does not have

- **A Domain layer and the domain charter.** No area-of-work entity; the seven parts exist once, system-wide.
- **The Directory**, and any routing of work by responsibility.
- **Persistent agents versus task agents.** No agent starts another; no subagents, workers or handoffs.
- **Agent definitions** separate from agents, shareable and revisable.
- **Sessions** (history to pause, resume, hand off), **Memory** (a store of what agents learn) and **Artifacts** (work products).
- **Scheduling** of work at a time, and limits on how much agent work runs at once.
- **Delegation between agents of different areas**, with a result coming back (WARM's Orchestration and its "delivery is not acceptance").
- **Skills** as instructions, and **Improvement and Releases of agents and skills**.
- **The Harness as a service**, separable from the rest of the platform.
- **The platform test** ("works the same whatever the work is about"), or any rule for what belongs to the platform.
- **People as requesters and as subjects of the work.** The source's people write, sign and audit rules.
- **The implementation relation**: the source maps its concepts to four frameworks (Table 6), but does not distinguish a model part from its implementations as a general relation.

## Limits of this mapping

- One mapper, no second rater, and the mapper knew WARM. WARM v0.11's own threats to validity apply.
- Figure content was not read.
- The English text is an AI-assisted translation of a French original that was not consulted.
- "Kind" and item granularity are the mapper's choices; the counts depend on them.
- Statements marked "Inference" are the mapper's; everything quoted is from the source or from WARM v0.11.
