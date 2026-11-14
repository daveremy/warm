---
title: "Mapping four charter-like models (Charterion, AEON, CEAD, Salesforce) onto WARM v0.11"
date: 2026-11-11
yardstick: warm-model-v0.11.md
planned-changes: synthesis.md, table "The v0.12 change list" (V1-V15)
sources:
  - "A: El Hassani, Charterion v2.0, Zenodo 10.5281/zenodo.22829848 (September 2026)"
  - "B: Longmire and Longmire, AEON, Zenodo record 20349596 (2026-05-22)"
  - "C: deVadoss, CEAD, arXiv:2605.08258v1 (2026-05-07)"
  - "D: Salesforce Architects, The Agentic Enterprise - The IT Architecture for the AI-Powered Future (undated page)"
status: analysis; read-only mapping, one rater, not second-rated
---

# Mapping Charterion, AEON, CEAD and Salesforce onto WARM v0.11

## Summary

These four sources were chosen because each looked closest to WARM's domain or to its "roles before agents" order. Read in full, none of them has a domain in WARM's sense: a charter of goals, roles, workflow, knowledge, tools, rules and acceptance criteria that several agents and people fill. What each one has instead:

- **Charterion** has a "charter", but a charter binds one agent: "agent a may act within business scope σ ... up to level ℓ, and ... principal π ... is accountable for what a does under it" (Def. 7.1). The business scope (capability, process, step) does exist apart from agents, and several agents and staffed human roles act in it.
- **AEON** has nine "subdomains" separate from agents, each bound by per-plane contracts. They are enterprise IT functions, each with "its own runtime, its own internal architecture, its own engineering function", and not charters of work.
- **CEAD** has "Capability before agent: define the business capability and owner before defining the agent role or prompt". The capability is recorded inside one agent's contract (the ACC).
- **Salesforce** uses "single business domain" and "multi-domain" only as maturity labels. It never defines a domain.

Three of WARM's four claims survive in narrowed form. One does not:

- Claim (iv) is **refuted**. Charterion defines an agent as a principal with "an identity to which authority and accountability attach, it may be instantiated many times". It also keeps that identity apart from the running configuration (model, prompt, tools), which can drift.
- Claim (ii) is **weakened**. AEON's capability registry records, for each capability, "the subdomain that provides it", and agents discover one another through it. That is a directory of who provides what, though not of who is accountable.
- Claims (i) and (iii) **stand, weakened**. Salesforce's design is the opposite of WARM's persistent agent: "Agents are instantiated for specific tasks, and the specific agent instances are decommissioned afterwards."

Charterion is far more precise than WARM about people's part. It separates three things WARM merges into Approvals and "a person may fill a role": a step reserved to people, an escalation decided by a named person, and approval of authority itself. It also checks that each of these has a current, reachable, not-overloaded human.

## What I read, and how

| Source | What was opened | Read in full | Not read |
|---|---|---|---|
| WARM v0.11 | `warm-model-v0.11.md` | All 513 lines | — |
| synthesis.md | Lines 63-79 | The v0.12 change list table only (V1-V15) | Everything else |
| search.md | grep for each source name; rows #7, #28, #32, #35 of tables 6.1 and 6.2, sections 7 and 8 | Those rows | The rest |
| A. Charterion v2.0 | `Charterion_v2.0_Specification.pdf` from Zenodo record 22829848 (290 PDF pages; extracted with pypdf). PDF page = printed page + 24 | PDF pp. 1-8 (front matter, claims, version history); table of contents; pp. 28-31 (ch. 2); 38-58 and 60-70 (ch. 5-8, start of ch. 9); 93-95 (ch. 16); 99-104 (ch. 18); 110-113 (ch. 21); 190-197 (ch. 27); 209-216 (ch. 29.1-29.3.1); glossary entries for agent, charter, instance, principal, reserved step, slice, performer role; p. 273 (App. L) | Ch. 9.4-15, 17, 19-20, 22-26, 28, 29.3.2 onward, 30-31; App. A, C-K, M-S. Keyword counts below cover all 290 pages |
| B. AEON | `AEON-White-Paper.pdf`, Zenodo record 20349596 (49 pp.) | All | — |
| C. CEAD | arXiv PDF 2605.08258v1 (8 pp.) | All | — |
| D. Salesforce | The primary page, fetched with curl and browser headers. The plain fetch returned "Access Denied", and a signed-in browser refused the domain, which is not registered in `browser-logins.tsv`. Text extracted from the HTML | All page text (reading time stated as 32 minutes); Figure 2 (11 layers) and Figure 3 (capability roadmap by maturity level) viewed as images | Figures 1 and 4-7 (images only, not viewed). Linked pages (Agentic Maturity Model, MuleSoft Agent Fabric) not opened |

PDF extraction dropped many word spaces in Charterion ("Theagentthatwasreviewed"). Quotes below restore word spacing and change nothing else. One deviation from the brief: I read the first 12 lines (front matter only) of `prior-work/mapping-yu-zhu.md` to match the folder's file format. Nothing in it affected any assignment.

**Absence searches.** Each "absent" in the reverse tables rests on a case-insensitive substring count over the whole extracted text of the source (all 290 pages of Charterion). The term list for each WARM part is in the Appendix. Counts were checked by reading the context where a term matched something irrelevant: AEON's "llm" hits are all inside "enrollment", and Charterion's "scheduling" hits are a case study's "scheduling agent".

## Adoption evidence (read 2026-11-11)

| Source | Citations | Other evidence | Named adopters |
|---|---|---|---|
| A. Charterion | OpenAlex `cited_by_count` 0 (concept DOI 10.5281/zenodo.22406488, which v2.0 now resolves under) | Zenodo: 193 downloads (173 unique), 144 views. Self-published by one author; CC BY-NC-SA, commercial use needs a license. The text states: "none is naturalistic", and "It does not claim ... that the layered profile has been used by any organisation" | None |
| B. AEON | OpenAlex 2 (concept DOI 10.5281/zenodo.20349193) | Zenodo: 88 downloads, 124 views. "Draft for discussion. Comments and challenges welcome." Authors state it "does not represent the position of any employer or program" | None |
| C. CEAD | OpenAlex 0. Semantic Scholar returned HTTP 429 (not checked) | arXiv v1 only. Its evaluation over "10,000 enterprise tasks" is stated as an "experimental model" with a logistic success formula (Eq. 1-3). **Inference:** the results come from a parametric simulation, not from running systems | None |
| D. Salesforce | Not applicable (vendor page) | No date on the page. The Wayback Machine's first capture is 2026-03-05. Offered in 17 languages. Vendor guidance from Salesforce Architects | None named on the page |

## Category key

Each inventory row has one **Type**: `clean` (one WARM service, layer, domain part, agent concept or the Directory, fitting well); `strained` (one such target, fitting with friction); `span` (several WARM parts, named); `guidance` (design-time advice, not a system part); `planned` (already in the v0.12 change list, Vn named); `misfit` (no WARM part; when in doubt between strained and misfit I chose misfit). Counting unit: one row per named item. Where a source names a group and its members, I counted the members. Items that only label an experiment (CEAD's A0-A4 baselines) are not counted.

---

## A. Charterion v2.0 (El Hassani)

### A.1 Inventory and assignment

**Layers, aspects, planes and facets**

| # | Item | Definition (verbatim) | Where | Assignment | Type |
|---|---|---|---|---|---|
| A1 | L0 Motivation & Strategy | "why the enterprise acts and what it commits to (drivers, goals, principles, requirements, constraints, obligations, capabilities as intent)" | §27.1 | Span: domain Goals, domain rules; People (who sets them) | span |
| A2 | L1 Business | "who does what: humans, roles, capabilities, processes, steps and their order; which steps the business designates to agents and which it reserves to people" | §27.1 | Span: People layer, domain Roles, domain Workflow | span |
| A3 | L2 Agency | "agents and their instances, charters, delegations, guards, oversight, escalation, validity, caps, configuration, perimeters, bounds; the derived authority, accountability, needs and envelopes" | §27.1 | Span: agent concepts, Identity, Policy, Approvals, V1, V2, V3 | span |
| A4 | L3 Application | "what is acted on and through what: resources ... and tools, the invocable operation surfaces that expose resources at an effect level" | §27.1 | Span: Tools service, domain tools | span |
| A5 | L4 Data & Knowledge | "memories and context stores with their scope, the assertion store, the decision log, provenance" | §27.1 | Span: Memory, Observability, Retrieval | span |
| A6 | L5 Technology / Agentic Runtime | "runtime nodes, orchestrators, tool gateways and MCP servers, model endpoints, policy decision and enforcement points, containment zones, halt controls, telemetry, and the entitlements provisioned in identity management" | §27.1 | Span: Infrastructure layer, Environments, Tools, Models, Policy, Orchestration, Observability, Identity, V3 | span |
| A7 | Warrant / Trust aspect (and the warrant facet) | "every assertion of every layer carries provenance, confidence, validity and status, and every decision is derived from warranted assertions or is unwarranted" | §27.8, §9.1 | No WARM part. Memory records provenance for learned entries only; nothing gates an action on the confidence and validity of the facts it relies on | misfit |
| A8 | Governance aspect | "Roles, bodies, decision rights, the charter lifecycle, gates, the Accepted-Defect Register, evidence-gated promotion and metrics" | §27.8 | Span: Policy, Approvals, Releases, Evaluation, People | span |
| A9 | Boundary aspect | "Mandates, exposures, attested assertions ... apply to every layer at the organisation's edge" | §27.8 | WARM describes one system's boundary; no cross-organization part. Not in V1-V15 (V12 tenancy is several tenants on one platform, not two organizations transacting) | misfit |
| A10 | Design plane | "the enterprise model with its agency layer ... its analysis is a computation over the model that runs on every change" | §5.1 | No WARM part is a formal model of authority checked before provisioning. Evaluation judges behavior and work products, not the structure of authority | misfit |
| A11 | Execution plane | "the substrate an agent queries at the moment of acting ... is this request, by this agent, on this target, admissible now?" | §5.1 | Span: Policy (decide), Approvals (escalate), Memory/Retrieval (assertions consulted) | span |
| A12 | Boundary plane | "the pair of substrates of two organisations with disjoint approvers" | §5.1 | As A9 | misfit |
| A13 | Anchor facet | "Does it exist, and is it the one I mean?" (entity, identifier, type, part-of) | Table 9.1 | No WARM part resolves the identity of the *targets* of action. Identity covers actors only | misfit |
| A14 | Affordance facet | "Can it be done, through what, with what consequence?" (operation, precondition, effect, reversibility) | Table 9.1 | Tools, which mediates calls but keeps no affordance record | strained |
| A15 | Envelope facet | "May I, and where must I stop?" Answer: "permit, deny or escalate" | Table 9.1 | Span: Policy, Approvals | span |
| A16 | Coordination facet | "shared referent, commitment, intent, lock, ownership, accountable unit" | Table 9.1 | No WARM part records locks or intents on shared resources. Orchestration tracks assignments, not contention over resources | misfit |

**The 43 building blocks (Table 29.1).** Block L2-4 names two guards; it is split into rows A30 and A31, so this table has 44 rows.

| # | Block | Definition (verbatim, short) | Assignment | Type |
|---|---|---|---|---|
| A17 | L0-1 Purpose Register | `Pursues(m, g)`: "charter m is issued in pursuit of goal g (informative in v2.0; no condition reads it)" | Domain Goals, but bound per charter (one agent) | strained |
| A18 | L0-2 Obligation Register | "Human-decision obligations ground reserved steps (WF17)"; `Obligation(o, σ, instr, kind)` | Domain rules (WARM rules carry no legal grounding) | strained |
| A19 | L1-1 Agentic Step Designation | "The step is the unit of allocation; the designation is approved, never observed" | Span: domain Workflow, domain Roles | span |
| A20 | L1-2 Reserved-Step Register | `Reserved(s)`: "the business has decided that step s is performed by a human and not by an agent" | Domain rules. WARM has no standing designation that a step is done by people only | strained |
| A21 | L1-3 Staffing Table | `Human, Role, Holds, Performs`: "A role without holders is vacant; vacancy propagates to WF1 and WF9" | Span: domain Roles (people filling roles), Directory (how to reach a role) | span |
| A22 | L2-1 Agent Register | "agent id, platform identity, description, lifecycle state, slice" | Identity (also lifecycle and slice) | strained |
| A23 | L2-2 Charter Register | "charter id, agent, scope (sort and element), level, principal, state, validity, review, cap, rationale record ref." Charter: "agent a may act within business scope σ ... up to level ℓ, and ... principal π ... is accountable" | Span: Policy as V1 grants (scoped, time-limited, revocable), Identity, domain Goals ("who is accountable"). The named accountable human per agent has no WARM home | span |
| A24 | L2-3 Delegation Guard | "Effective level is the meet of the delegator's authority and the declared level (attenuation)" | WARM separates handoff (Orchestration) from authority. No rule that authority passed to another agent attenuates. V1 and V2 do not cover agent-to-agent passing of authority | misfit |
| A25 | L2-5 Oversight Assignment | `Oversight(a, h)`: "human h monitors and can halt agent a" | V3 (stop). WARM names no overseer per agent | planned (V3) |
| A26 | L2-6 Escalation Route | "the human who decides the escalate outcomes that the execution plane raises for a" | Approvals, which does not say who decides for which agent | strained |
| A27 | L2-7 Configuration Digest | "The digest covers model, prompt, tool list and parameters; drift raises ConfigDrift" | Releases (WARM versions changes but does not check that what runs is what was reviewed) | strained |
| A28 | L2-8 Instance Registry | "An instance i of agent a is a running process that acts under the identity of a and holds no charter of its own" | Task agent concept. Conflicts with WARM, where each task agent is an identified actor | strained |
| A29 | L2-9 Perimeter Declaration | "The perimeter is what an orchestrator may dispatch within; a request outside it is returned" | No declared delegation graph in WARM | misfit |
| A30 | L2-4a Separation guard (SoD) | "SoD(s, s′) states that no single agent may cover both steps" | V2 separation of duties | planned (V2) |
| A31 | L2-4b Precedence guard | "Precedence(a, b, x) is the declared resolution of a potential conflict between two agents that may write resource x" | No WARM part for contention between agents over a resource | misfit |
| A32 | L2-10 Blast Bound | "no agent's blast radius shall exceed its declared bound" | No bounded-reach measure in WARM | misfit |
| A33 | L2-11 Load Bound | escalation load per human per period against a bound | Approvals has no bound on a person's load | misfit |
| A34 | L3-1 Resource Inventory | `Resource, Requires(s, x, ℓ)`: the level at which step s needs resource x | Span: domain Workflow, domain tools | span |
| A35 | L3-2 Tool Catalogue | "A tool is an application interface with a declared effect level" | Registry (tool definitions; the effect level is extra) | strained |
| A36 | L3-3 Reversibility Declaration | `Irreversible, Compensation, Reversible, SideEffectScope` | V14 (undo) | planned (V14) |
| A37 | L4-1 Scoped Memory Store | "a memory is an authority channel checked against charter scope" | Memory (scope check added) | strained |
| A38 | L4-2 Assertion Store | "Named as an element in v2.0 so that it can be hosted (L5) and audited" (the substrate of warranted assertions) | No WARM store of warranted facts consulted before acting | misfit |
| A39 | L4-3 Decision Log | "an auditor replays decisions from it" | Observability | clean |
| A40 | L4-4 Register Store | "One element for the versioned registers" | Span: Registry, Releases | span |
| A41 | L4-5 Provenance Record | "a store without it is a repository, not a substrate" | Memory (provenance), applied to every assertion | strained |
| A42 | L5-1 Runtime Node | "A node hosts an actor with authority" | Infrastructure layer | clean |
| A43 | L5-2 Orchestrator | "The control relation of the planner/executor and supervisor patterns" | Orchestration | clean |
| A44 | L5-3 Tool Gateway / MCP Server | "Invokes(a, t) is the tool-level provisioning, analogous to Grant" | Tools | clean |
| A45 | L5-4 Model Endpoint Registry | "approval is of the endpoint (model, version, configuration) for authority up to that level" | Models (the approval part is Policy) | strained |
| A46 | L5-5 Policy Decision Point | "evaluates the admissibility function ... over the approved envelope" | Policy | clean |
| A47 | L5-6 Policy Enforcement Point | "an enforcement point whose DecidedBy is not substrate-backed enforces a policy the model did not derive" | Policy (WARM's "enforcement point", Step 2 point 1) | clean |
| A48 | L5-7 Containment Zone / Sandbox | "a sandbox is a zone whose nodes reach no write-level tool outside it" | Environments | clean |
| A49 | L5-8 Halt Control | "a control the platform reports but no human holds is the halt-on-paper anti-pattern" | V3 | planned (V3) |
| A50 | L5-9 Telemetry Sink | node writes decision requests and outcomes to the decision store | Observability | clean |
| A51 | L5-10 Identity Grant Provisioner | "The grant is the provisioning target of L2, not the source of authority" | Span: Identity, Policy | span |
| A52 | W-1 Assertion Warrant | "four-valued admissibility (permit, deny, escalate, unwarranted)" | Span: Policy, Approvals. "Unwarranted" has no Policy counterpart (WARM gives "unknown" only to Evaluation) | span |
| A53 | W-2 Certificate Issuer / Checker | "a checker recomputes the digest, it never re-derives the need" (a checkable derivation object for each entitlement) | No WARM counterpart | misfit |
| A54 | G-1 Lifecycle Gate | states "Proposed, Analysed, Approved, Provisioned, Active, Under review, Degraded, Retired"; "the gate is a computation over the model, not a meeting" | Span: Releases, Approvals, Policy | span |
| A55 | G-2 Accepted-Defect Register | "A defect the organisation chooses to live with is recorded, never silenced ... An accepted defect past its review date is reported again" | No WARM part records accepted exceptions with an expiry | misfit |
| A56 | G-3 Evidence Record | "reversal rate; denial rate; unwarranted share; escalation acceptance rate" | Span: Evaluation, Improvement | span |
| A57 | G-4 Authority Request Handler | "The agent proposes, never approves" | Span: Approvals, Releases, V2 | span |
| A58 | B-1 Mandate Register | mandates for agents acting across organizations | Cross-organization (as A9) | misfit |
| A59 | B-2 Exposure Declaration | "exposure level X0-X4; external affordance inventory" | As A9 | misfit |
| A60 | B-3 Trust Weight Register | "Set and re-estimated only by A ... never imported from the counterparty" | As A9 | misfit |

**Roles and bodies (Table 18.1, §18.3)**

| # | Item | Definition | Assignment | Type |
|---|---|---|---|---|
| A61 | Agency architect | "Owns the design plane: populates the core, drafts charters and guards" | People layer (a builder role WARM does not name) | strained |
| A62 | Substrate owner | "Owns the execution plane: the assertion store, the admissibility service, the decision log" | People layer (operator) | strained |
| A63 | Domain authority | "Answers for the anchor and affordance content of a domain; resolves conflicts and unwarranted outcomes in it" | People layer. "Domain" is used but never defined (23 occurrences in 290 pages) | strained |
| A64 | Principal | "The human, or holder of the role, named by a charter; accountable for what the agent does under it" | Domain Goals ("who is accountable"), but per agent | strained |
| A65 | Approver | "Commits envelope and ownership assertions; issues mandates; must be in Acc(g,·)" | Approvals (approves authority, not actions) | strained |
| A66 | Overseer | "Monitors and can halt an agent; decides its escalations" | Span: V3, Approvals | span |
| A67 | Agent platform team | "Runs the agents; applies provisioning targets to identity management" | People layer (operator) | strained |
| A68 | Auditor | "Reads the decision log and the registers; replays decisions" | People layer | strained |
| A69 | Agent (role) | "A non-human principal; may observe, request and propose; may not approve" | Agent | strained (type-level identity; see A28) |
| A70 | Agency Governance Board | "decides: acceptance of defects with enterprise-level consequence ... write-level capability charters ... the span bound β" | People layer | strained |
| A71 | Charter Review | "the standing forum of agency architect, principals and overseers that exercises the routine gates" | People layer | strained |
| A72 | Boundary Review | "declares exposures, approves mandates and re-estimates trust weights" | As A9 | misfit |

**Core constructs, rules and artifacts**

| # | Item | Definition | Where | Assignment | Type |
|---|---|---|---|---|---|
| A73 | Agent (definition) | "a software system that receives a goal, decomposes it into steps ... under authority conferred on it by the organisation ... An agent is a non-human principal: it has an identity to which authority and accountability attach, it may be instantiated many times" | Def. 2.1 | Agent. Identity sits at the type level | strained |
| A74 | Capability / Process / Step (core sorts) | "capabilities and the processes that realise them"; "steps of a process and their control-flow order" | Table 6.1 | Span: Domains layer, domain Workflow | span |
| A75 | Slice | "The unit of adoption and conformance: a set of capabilities or processes, their resources and agents" | Glossary | Domains layer, as a scope of adoption and not a charter | strained |
| A76 | Action levels | "L = {read < propose < commit < autonomous}" | Def. 6.1 | No WARM vocabulary of authority levels | misfit |
| A77 | Admissibility function | "ADM : Q × S → {permit, deny, escalate, unwarranted}" | Def. 9.3 | Counted under A11 and A52 | (not counted) |
| A78 | Granularity rule | "Charters at commit and autonomous should be as narrow as the steps that need them" | §7.5 | Design-time guidance (parallels WARM's handoff grain) | guidance |
| A79 | Evidence-gated promotion rule | "A charter's level shall be raised only at gate G6, only by one step in L, and only if ... its Evidence Record satisfies the organisation's thresholds" | §18.8 | Span: Evaluation, Releases, Approvals | span |
| A80 | Authority Request Protocol | "gives the agent a way to ask the architecture for authority ... an agent may propose any assertion about its own authority; it may approve none" | ch. 16 | V2 (an agent cannot grant itself authority) | planned (V2) |
| A81 | Charter Rationale Record | "per write-level charter: business purpose, why this scope and level, why not narrower" | §21.5 | Design-time guidance | guidance |
| A82 | Agency Grid; five actor questions; four architect questions | grid of "planes (rows) against the five questions of an actor"; A1 "Which human is accountable for this agent's write access?" | §2.3, §5.2 | Design-time guidance | guidance |
| A83 | Matrices (Authority, Need-vs-Grant, Contention, SoD, Oversight Span) | generated projections | §21.3 | Design-time guidance (one row for the five) | guidance |
| A84 | Viewpoints (7 v1.0, 3 v1.1, 4 v2.0) | "Viewpoints are defined in the manner of ArchiMate" | §21.4, Tables 21.2-21.4 | Design-time guidance (one row) | guidance |
| A85 | Agentic patterns (10) | planner/executor, supervisor, critic, human-in-the-loop gate, sandboxed tool use, kill-switch, compensable write, memory-scoped assistant, approved-model routing, boundary mandate exchange | §29.3 | Design-time guidance (one row) | guidance |
| A86 | WF1 Accountable authority | "Every agent with write-level authority has at least one accountable human" | Table 7.1 | No WARM rule that each acting agent traces to an accountable person | misfit |
| A87 | WF2 Covered designation | "Every step designated for agent performance is covered by some agent" | Table 7.1 | Directory (WARM: "A responsibility with no accountable domain is a gap"), at step grain | strained |
| A88 | WF3 Justified provisioning | "Provisioned grants equal derived needs" | Table 7.1 | Policy (least privilege; WARM has no derivation) | strained |
| A89 | WF4 Separation of duty | "No agent covers both steps of a separation-of-duty pair" | Table 7.1 | V2 | planned (V2) |
| A90 | WF5 Declared coordination | "Any two agents that may write the same resource from concurrent steps have a declared precedence" | Table 7.1 | As A31 | misfit |
| A91 | WF6 Bounded delegation | "No delegation declares a level above the delegator's authority in its scope" | Table 7.1 | As A24 | misfit |
| A92 | WF7 Watched autonomy | "Every agent with autonomous authority is under human oversight" | Table 7.1 | V3 | planned (V3) |
| A93 | WF8 Reserved-step integrity | "No agent holds write-level authority over a reserved step" | §8.1 | Domain rules applied by Policy | strained |
| A94 | WF9 Escalation reachability | "Every agent with write-level authority is reachable, and no human's span exceeds the bound" | §8.2 | No WARM requirement that an approval reach a current, available person | misfit |
| A95 | WF10 Temporal currency | write-level charters have validity and review dates; a stale charter "loses one level" | §8.3 | V1 (limited in time); graceful degradation is new | planned (V1) |
| A96 | WF11 Independent separation | "The two sides of a separation-of-duty pair are covered only by pairwise independent agents" (no common delegator) | §8.4 | V2 (does not cover the common-delegator case) | planned (V2) |
| A97 | WF12 Compensable autonomy | autonomous authority over an irreversible write only if "a compensation for that resource is available" | §8.5 | V14 | planned (V14) |
| A98 | WF13 Configuration currency | "the running configuration of its agent shall equal" the reviewed digest | §8.11 | Releases | strained |
| A99 | WF14 Chartered instantiation | "every running instance shall be an instance of a chartered or delegated-to type, no type shall exceed its declared cardinality" | §8.12 | Span: Identity, Scheduling (concurrency limit) | span |
| A100 | WF15 Staffed reservation | "every reserved step shall have a role assigned to perform it with at least one current holder" | §8.13 | No WARM check that a role reserved to people has a current holder | misfit |
| A101 | WF16 Bounded cap composition | "the sum of the permit caps an agent delegates ... shall not exceed the sum of the permit caps of its own charters" | §8.14 | Rests on delegation and caps (A24, A91) | misfit |
| A102 | WF17 Grounded obligation | "no agent shall hold autonomous authority on a step within the scope of a human-decision obligation" | §8.15 | Domain rules | strained |
| A103 | WF18 Delegation perimeter | "every delegation shall follow a declared collaboration edge, no agent shall delegate transitively to itself" | §8.16 | As A29 | misfit |
| A104 | WF19 Bounded blast radius | "no agent's blast radius shall exceed its declared bound" | §8.17 | As A32 | misfit |
| A105 | WF20 Bounded escalation load | "no human shall receive, in any period π, more escalate decisions than the declared bound" | §8.19 | As A33 | misfit |
| A106 | WF21 Justified tool exposure | Fig. 5.2 label only | Fig. 5.2 | Tools (definition not read) | strained |
| A107 | WF22 Scoped memory | Fig. 5.2 label only | Fig. 5.2 | Memory (definition not read) | strained |
| A108 | WF23 Mediated write | "every write-level tool call [must] pass an enforcement point fed by the approved envelope" | §27.7 | Policy; the same condition as WARM's Governance point 1 | clean |
| A109 | WF24 Approved model endpoint | "whether the model that drives an autonomous agent is approved for that level" | §27.7 | Models | strained |
| A110 | WF25 Reachable halt | "whether the overseer of WF7 can actually stop the agent where it runs" | §27.7 | V3 | planned (V3) |
| A111 | WF26 Contained hosting | "whether the agent runs inside the zone its blast bound assumes" | §27.7 | Environments | strained |
| A112 | CC1-CC8 coherence conditions | "six conditions CC1-CC6 ... make the relation checkable" between planes; CC7 certified envelope; CC8 "observed hosting, serving, routing ⊆ declared". **Only partly read** | §5.1, Fig. 5.2 | Span: Policy, Observability, Releases | span |
| A113 | Inv-1 to Inv-5 | "an approval by a non-human, an authorising observed envelope assertion, or a self-sourced envelope assertion is refused" (Inv-1 to Inv-3); Inv-5 decisions logged with supporting assertions. **Inv-4 only partly read** | §18.6 | V2 (non-self-authorisation); Inv-5 is Observability | planned (V2) |

A77 is not counted. Counted items: 112.

### A.2 Reverse direction (Charterion)

See the combined table in section "Reverse direction, all four sources".

### A.3 The questions that matter most (Charterion)

**(a) An area of work as an entity separate from agents?** In part, but the "charter" is not it. The charter binds one agent:

> "A charter Charter(m, a, σ, ℓ, π) states that agent a may act within business scope σ—a capability, a process or a single step—up to level ℓ, and that principal π (a human, or a role whose holders are humans) is accountable for what a does under it." (Def. 7.1)

The scope σ is a business element modeled independently of agents (L1, owned by the "domain authority" for structure and by the principal for designations). Several agents can be chartered on the same scope: WF4, WF5 and WF11 exist because they can. People fill roles that perform reserved steps (`Performs(r, s)`, WF15). So a capability or process in Charterion holds agents and people. Checked against WARM's seven parts:

- **Goals:** L0 goals, linked per charter by `Pursues`, which is "informative in v2.0; no condition reads it".
- **Roles:** human roles (`Role`, `Holds`, `Performs`). Agents do not fill roles; they hold charters.
- **Workflow:** `Process`, `Step`, `Before`, `Agentic`, `Reserved`.
- **Knowledge:** only as memory scoped to σ, `MemoryScope(k, σ)`.
- **Tools:** `Requires(s, x, ℓ)` and tools that expose resources.
- **Rules:** SoD, precedence, reserved steps, obligations, caps.
- **Acceptance criteria:** none for work products. The Evidence Record thresholds judge charters, not outputs.

The construct Charterion itself calls the unit of grouping is the slice, "a set of capabilities or processes, their resources and agents", and it is a unit of adoption and conformance, not a charter. "Domain" appears 23 times and is never defined.

**(b) A record of who is accountable for what, usable for handing over work?** Several registers, none built for handoff:

- **Charter Register:** each entry holds "charter id, agent, scope (sort and element), level, principal, state, validity, review, cap, rationale record ref." The model derives `Covers(a, s)` (which agent covers each step) and `Acc(a, h)` (which human answers for each agent). WF2 requires every agentic step to be covered. *Inference:* a step-to-agent and agent-to-human map can be computed from the registers, but the text never presents it as a lookup an agent uses to find where to send work. Agents query the substrate for admissibility, not for a destination.
- **Staffing Table (L1-3):** "Human, Role, Holds, Performs". It records which role performs which reserved step and who holds the role.
- **Agent Register:** "agent id, platform identity, description, lifecycle state, slice".
- **Delegation Register, Guard Register, Principal & Vacancy Register, Authority Request Register, Grant Reconciliation Ledger, Mandate Register, Exposure Declaration, Trust Weight Register, Envelope Register, Decision Log, Commitment Ledger** (Table 21.1, Table 21.3). All record authority, evidence or cross-organization terms.

Accountability runs to a person per agent (the principal), not to an area of work per responsibility.

**(c) Identity versus definition and instance; persistent versus task agents.** Charterion separates three things:

- **The agent:** "a non-human principal: it has an identity to which authority and accountability attach, it may be instantiated many times" (Def. 2.1).
- **Its configuration:** "model identity and version, system prompt, tool set, runtime version" (Def. 8.8). It can change while the agent and charter stay the same: "The agent that was reviewed at gate G2 is not necessarily the agent that runs: model, prompt, tool set and runtime version change without a change to the charter" (§8.11).
- **Its instances:** "a running process that acts under the identity of a and holds no charter of its own" (Def. 8.9). The framework adds: "An agent type is chartered once and instantiated many times, ephemerally" (§8.12).

The identity sits at the type: instances share it. Charterion has no agent that persists across tasks with its own memory and channel. Searches for "persistent", "long-lived" and "long-running" returned 0 hits, and "ephemeral" returned 1.

**(d) Steps reserved for people; who may approve what.** This is the most developed part of the source. Charterion separates three kinds of human decision:

- **Steps a person performs:** "Reserved(s) states that the business has decided that step s is performed by a human and not by an agent" (Def. 8.1). WF8 keeps agents' write authority off these steps. WF15 requires a staffed role for each. WF17 grounds them in legal instruments. "Note that read and propose authority over a reserved step are permitted: an agent may prepare the file on which a human decides."
- **Escalations:** "escalate means the approved envelope permits the action subject to a human decision ... taken by the escalation human" (§9.3). WF9 requires that human to exist and bounds their span. WF20 bounds their load: "When the load exceeds what a person can decide with attention, the escalate outcome degrades in fact to permit".
- **Approval of authority:** "Approved content has been validated by a human in H and is the only content that can authorise an action" (§9.1). Inv-1 refuses "an approval by a non-human". The agent "may observe, request and propose; may not approve" (Table 18.1).

The decision-rights matrix (Table 18.2) assigns each decision to a role: designate a step agentic or reserved (principal decides); accept accountability (principal); decide an escalation (overseer); accept a WF1, WF4 or WF8 defect (Board).

WARM's Approvals ("Hold chosen actions until a person authorizes them, and record the decision") covers only the second kind. WARM has no standing designation of a step only people may do, and no rule about who may approve what or whether that person is available.

**(e) What Charterion does better.**

1. **Reserved and staffed steps.** WF8, WF15 and WF17 are quoted above. To match, WARM would add a designation that a step or responsibility is reserved to people, as a domain rule. It would also require that the role performing it has a current holder.
2. **An accountable person for every agent that can change state.** "WF1 Accountable authority: Every agent with write-level authority has at least one accountable human." WARM states accountability per domain ("who is accountable" under Goals), not per agent or per role assignment. To match, WARM would require that each identity able to act traces to an accountable person.
3. **A reachable, not-overloaded approver.** "a person watching a hundred agents watches none" (§8.2). To match, the Approvals contract would name who decides for each agent or role, and would state what happens when nobody can.
4. **Attenuating delegation and independent separation.** "When an orchestrator delegates one side of a pair to a sub-agent and performs the other itself ... WF4 is satisfied ... and the separation is void, because one planner controls both executions" (§8.4). V2 as written would miss this. To match, V2 would add that agents under a common starting agent are not independent for separation of duties.
5. **Configuration drift.** WARM says definition, harness and model changes are "versioned and evaluated" but has no check that the running configuration equals the reviewed one. WF13 has one.
6. **Graceful degradation of stale authority.** "a charter that has passed its review date does not vanish ... but loses one level". This sharpens V1's "limited in time".
7. **A fourth decision outcome.** "unwarranted means the substrate cannot stand behind an answer; its remedy is re-observation or a human answer". WARM gives "unknown" only to Evaluation.

---

## B. AEON (Longmire and Longmire)

### B.1 Inventory and assignment

| # | Item | Definition (verbatim) | Where | Assignment | Type |
|---|---|---|---|---|---|
| B1 | AEON (the control plane) | "the architectural layer that orchestrates composition without executing the composed capabilities ... decides what is composed, by whom, under what authority, with what evidence, against what policy" | §1 | Span: Identity, Policy, Observability, Orchestration, Registry | span |
| B2 | Identity plane | "owns the resolution of any subdomain action to the principal that authorized it" | §7.1 | Identity | clean |
| B3 | Authority plane | "answers a question the subdomains cannot answer themselves: is this action authorized?" | §8 | Policy | clean |
| B4 | Evidence plane | "Every action taken by any subdomain on behalf of any principal contributes to the evidence plane" | §9 | Observability | clean |
| B5 | Integration plane | "orchestrates composition across subdomain boundaries" (workflows and the agent network) | §10 | Span: Orchestration, Messaging, Tools | span |
| B6 | Capability composition | "the architectural function that asks what the enterprise can do, how new capabilities are introduced ... and how capabilities are retired" | §11 | Span: Registry, Releases, V6 | span |
| B7 | Meta-orchestration runtime | "the actual platform that Enterprise IT builds and operates" hosting the planes | §12.1 | Platform layer | clean |
| B8 | Principal | "a human person identified through enterprise IDAM infrastructure" | §7.1 | Span: People layer, Identity | span |
| B9 | Delegation chain and authority tokens | "AEON issues scoped sub-tokens ... each cryptographically derived from the root token and carrying constrained scope"; root token carries "the authorized scope, and the expiration" | §7.3 | V1 grants (scoped, time-limited, derived) | planned (V1) |
| B10 | Federation broker | "an architectural service that mediates between IDAMs while preserving each IDAM's authority over its own principals" | §7.2 | Cross-classification federation; not in WARM or V12 | misfit |
| B11 | Revocation propagation | "terminating active agents under the affected principal, invalidating outstanding delegations, freezing operations in progress" | §7.4 | V3 (suspend or revoke) | planned (V3) |
| B12 | Degraded operation | "time-bounded cached capabilities with cryptographic expiry" | §7.5 | Span: Identity, Reliability | span |
| B13 | Identity plane subdomain contract | what subdomains "consume", "promise", and "The architectural guarantees" | §7.6 | Identity contract (WARM specifies none) | strained |
| B14 | Authorization decision: seven types | "Allow ... Deny ... Constrain ... Redact ... Route ... Log ... Escalate" | §8.1 | Span: Policy, Approvals (escalate), Observability (log) | span |
| B15 | Policy decomposition | "compiles the enterprise policy into subdomain-specific enforcement bundles" | §8.2 | Policy (and V7 for rule changes) | strained |
| B16 | Compose-and-evaluate | "composes the relevant policy across all subdomains involved, evaluates the composition ... and returns a decision that all subdomains can rely on" | §8.3 | Policy (cross-domain composite evaluation is not described in WARM) | strained |
| B17 | Authority currency | "a continuous-evaluation pattern rather than a cache-at-session-start pattern" | §8.4 | V1 (checked when the action runs) | planned (V1) |
| B18 | Behavioral constraint layer | "constraints ... that operate orthogonally to principal-based authorization ... the substrate refuses regardless of what the principal requests" | §8.5 | V5 (content); Policy | planned (V5) |
| B19 | Authority plane subdomain contract | subdomains "promise to consult the authority plane before consequential actions, to honor the full decision" | §8.6 | Policy contract | strained |
| B20 | Canonical, append-only evidence capture | "each record carries a hash that depends on the prior record's hash" | §9.1 | Observability | clean |
| B21 | Publish-and-acknowledge aggregation | runtimes "publish evidence records ... AEON's evidence plane acknowledges receipt, verifies the signatures" | §9.2 | Observability | clean |
| B22 | Cross-subdomain forensics | "trace the chain forward from a principal authentication event ... or backward from an incident" | §9.3 | Observability | clean |
| B23 | Retention and records posture | "The retention policy is set at the policy plane and enforced by the evidence plane" | §9.4 | Policy (rules on stored data) | clean |
| B24 | Worker-facing evidence access | "Workers can query their own evidence to see what their substrate did" | §9.5 | V13 (subject's control over stored data) | planned (V13) |
| B25 | Evidence plane subdomain contract | publish "for every action they perform, to publish in the canonical schema" | §9.6 | Observability contract | strained |
| B26 | Workflow descriptor | "specifies the subdomain interactions, the data flow between them, the failure handling, and the result composition" | §10.1 | Orchestration | clean |
| B27 | Agent network protocol | "how agents discover other agents (through the capability registry ...), how they authenticate to each other ..., how they exchange authority ..., how they coordinate" | §10.2 | Span: Messaging, Orchestration, Directory, Identity | span |
| B28 | Subdomain adapter | "translates between the subdomain's internal capability representation and the integration plane's canonical capability contract" | §10.3 | Span: Tools, domain tools | span |
| B29 | Integration plane subdomain contract | "promise to register capabilities through the capability registry, to expose capabilities through compliant adapters" | §10.5 | Orchestration contract | strained |
| B30 | Capability registry | "the canonical record of what the enterprise can do ... the subdomain that provides it ... the principals authorized to invoke it under what conditions" | §11.1 | Span: Registry (with V6 owner), Directory (provider per capability) | span |
| B31 | Capability lifecycle | "proposed, qualified, operational, deprecated, retired" | §11.2 | V6 (registration as a gate, adding an entry is a release) | planned (V6) |
| B32 | Composition patterns (6) | "Sequential ... Parallel ... Conditional ... Iterative ... Compensating ... Negotiated" | §11.3 | Orchestration (compensating relates to V14) | strained |
| B33 | Capability versioning | "The registry maintains version history" | §11.4 | Registry | clean |
| B34 | Retirement discipline | "The AEON team reviews the registry on a defined cadence, identifies capabilities that are candidates for deprecation" | §11.5 | Releases | strained |
| B35 | Capability composition subdomain contract | "promise to register ... participate in the lifecycle process ... honor retirement decisions" | §11.6 | Registry contract | strained |
| B36 | Runtime observability | "Every plane exposes metrics ... operational state: healthy, degraded, failed, in maintenance" | §12.5 | Observability | clean |
| B37 | Runtime operational posture | "failure modes are tested through chaos engineering practice. Its recovery procedures are exercised" | §12.4 | Reliability | clean |
| B38 | AEON function (team) | "small and senior ... reports within Enterprise IT, typically to a Chief Architect" | §13 | People layer (operators) | strained |
| B39 | Subdomain teams | "build and operate their subdomains and compose into AEON through the architectural contracts" | §5, §13.3 | People layer | strained |
| B40 | Chief Architect | provides "the institutional backing that makes the architectural authority real" | §13.3 | People layer | strained |
| B41 | Architecture-as-code | "plane contracts, the policy decompositions, the workflow descriptors ... are version-controlled" | §13.4 | Design-time guidance (and Releases) | guidance |
| B42 | Governance cadences | "Weekly operational reviews, monthly architecture review boards, quarterly strategic reviews" | §13.5 | Design-time guidance | guidance |
| B43 | Federated AEON instances | "coordinated instances across the classification environments" | §14.1 | Cross-classification; no WARM part | misfit |
| B44 | Cross-domain composition | "A workflow can reach down from CUI to unclassified ... A workflow cannot reach up" | §14.5 | As B43 | misfit |
| B45 | Propose-and-confirm (curation) | "She curates it: she accepts some remediations, rejects others, modifies the rest. Her curation is captured cryptographically" | §4 | Approvals (person's decision, including change of the draft) | clean |
| B46 | Institutional preconditions (5) | "A consolidated enterprise IDAM ... policy-as-code ... A central architecture function with real authority ... multi-year horizon ... senior control-plane talent" | §3 | Design-time guidance (one row) | guidance |
| B47 | Minimal coherent subset and phases 0-3 | "the identity plane, the authority plane, and a minimal evidence plane, supporting one or two high-value cross-subdomain workflows" | §16 | Design-time guidance (one row) | guidance |
| B48 | Concern mechanisms (procurement guardrails, risk register, funding gate) | "tie AEON contract compliance to funding and project approval" | §17.2 | Design-time guidance (one row) | guidance |
| B49 | Subdomain (concept) | "The subdomains are the capability areas the control plane orchestrates ... Each subdomain has its own runtime, its own internal architecture, its own engineering function, and its own vendor relationships" | §5 | Domains layer: a separate area, but an organizational IT unit with its own systems, not a charter | strained |
| B50 | Governance and Strategy | "executive direction, strategic planning, portfolio management ... compliance, risk, audit, and legal" | App. A | Span: People layer (directing), Domains layer | span |
| B51 | AIDEX | "the worker-facing AI digital experience substrate" | App. A | Span: Channels, Harness. An agent product, not an area of work | span |
| B52 | DevSecOps | "software delivery, CI/CD ... release management, and pipeline governance" | App. A | Domains layer (WARM's Software Factory) | strained |
| B53 | Cybersecurity | "security operations ... and the agentic AI guardrails that constrain substrate behavior" | App. A | Span: Domains layer, Policy (guardrails) | span |
| B54 | Digital Engineering | "model-based systems engineering ... engineering models, digital thread" | App. A | Domains layer | strained |
| B55 | Enterprise Platforms | "ERP, PLM, CRM, workflow platforms, the systems of record themselves" | App. A | Span: Providers layer, Tools. Systems of record, not an area of work | span |
| B56 | Human Capital | "HR, talent management, learning and development" | App. A | Domains layer | strained |
| B57 | Insights and Intelligence | "data governance, data architecture, master data management, analytics" | App. A | Span: Domains layer, Retrieval | span |
| B58 | Infrastructure and Operations | "compute, network, storage ... site reliability engineering ... including the AEON runtime itself" | App. A | Span: Infrastructure layer, Reliability | span |

Counted items: 58.

### B.3 The questions that matter most (AEON)

**(a) An area of work as an entity of its own?** Yes, separate from agents, but not defined by WARM's parts. "AEON is the control plane. The subdomains are the capability areas the control plane orchestrates" (§5). "The subdomain teams are not part of the AEON team ... the subdomain teams build and operate their subdomains" (§5). People and agents both work in a subdomain: "Agents in one subdomain negotiate with agents in other subdomains on behalf of their principals" (§10.2).

What defines a subdomain is the capability scope it exposes (Appendix A) and the contracts it accepts per plane: "What the subdomains consume ... What the subdomains promise ... The architectural guarantees" (§7.6). Those contracts govern how a subdomain *consumes the platform*. They are not a charter of its own work. Against WARM's seven parts: no goals, no roles (only "subdomain teams"), no workflow (each subdomain's internals are "outside the scope of this paper"), no knowledge, rules only as inherited enterprise policy, no acceptance criteria. Tools appear as adapters.

The nine subdomains are organizational IT functions with "its own runtime ... and its own vendor relationships". One of them, AIDEX, is an agent product rather than an area of work.

**(b) A record of who is accountable for what?** The capability registry is the closest thing to WARM's Directory found in this round:

> "Every capability any subdomain exposes is registered in the registry along with its metadata: the subdomain that provides it, the capability description in canonical form, the adapter that exposes it, the policy constraints that apply to its use, the lifecycle stage ..., the evidence requirements, the audit posture, the dependencies on other capabilities, and the principals authorized to invoke it under what conditions." (§11.1)

Agents use it to find each other: "how agents discover other agents (through the capability registry developed in Section 11)" (§10.2). One entry holds an invocable capability and its providing subdomain. It does not hold a responsibility or an accountable area, and it says nothing about exclusivity ("exactly one"). The word "accountable" appears 4 times in AEON, always about human principals.

**(c) Identity versus definition and instance; persistent versus task.** AEON gives agents no identity of their own. "Her AIDEX substrate acts under her delegated authority, carrying her identity in every downstream action" (§4). "The principal is a human person" (§7.1). Agents appear only as carriers of a delegation chain. There is no agent definition, no instance, and no persistent or task distinction. Searches for persistent, long-lived, ephemeral and transient returned 0 hits. "Instance" appears 51 times, every one about AEON deployment instances.

**(d) Steps reserved for people; who may approve what.** The authority plane's "Escalate requires the action to be confirmed by a higher authority before it executes ... a second authority must approve" (§8.1). AIDEX uses propose-and-confirm: "The remediation she signs is her curated work, not the substrate's unreviewed output" (§4). For the architecture itself, the lifecycle process specifies "who proposes ..., who qualifies ..., who approves transitions between lifecycle stages" (§11.2). Between AEON and subdomains: "Neither can override the other within the other's scope" (§13.3). AEON names no steps reserved to people. Escalate matches WARM's Approvals. Propose-and-confirm matches WARM's "changes the draft" outcome.

**(e) What AEON does better.**

1. **Contracts in three parts.** Each plane's contract states what subdomains consume, what they promise and what the plane guarantees. WARM's Limit 4 says it has no service contracts. This consume/promise/guarantee form is a ready template, and it already covers failure ("Degraded operation", §7.5) and revocation latency ("measured in seconds with hard upper bounds enforced by policy", §7.4).
2. **Seven decision types instead of allow or deny.** "The decision is not a binary allow or deny" (§8.1). WARM's Policy decides "whether an action is allowed". Matching would add constrain, redact, route and log outcomes, with escalate going to Approvals.
3. **Composite authorization across areas.** "No single subdomain can authorize the composite action" (§4). WARM's handoff example checks rules in the receiving domain only. It does not say who evaluates a request whose rules come from two domains at once.
4. **Worker access to their own evidence** (§9.5). This goes beyond V13 because it is the acting person's own record, not only the data subject's.

---

## C. CEAD (deVadoss)

### C.1 Inventory and assignment

| # | Item | Definition (verbatim) | Where | Assignment | Type |
|---|---|---|---|---|---|
| C1 | Intelligent enterprise agent (7 conditions) | "a software actor that satisfies ... Goal-directed intent handling ... LLM-mediated cognition ... Tool-mediated action ... Bounded autonomy ... State and memory ... Observable accountability: it has an owner, identity, trace, evaluation record, cost record, and escalation path ... Uncertainty handling" | §III.A | Agent (identified actor with owner) | strained |
| C2 | Autonomy levels L0-L4 | "L0 Observe ... L1 Draft ... L2 Prepare ... human approves submission ... L3 Bounded execute ... L4 High-autonomy execute" | §III.B | No WARM vocabulary of autonomy levels | misfit |
| C3 | Intent and Outcome Layer | "Users, applications, process triggers, and APIs submit intents. The layer captures user identity, business purpose, tenant, data context, expected outcome" | §V.B | Span: Channels, Scheduling (triggers), Identity, V12 (tenant) | span |
| C4 | Agent Design Plane | "maintains the capability map, agent boundaries, ACCs, autonomy levels ... It answers whether an agent should exist, what it owns, what it must not own, which other capabilities it may invoke, and how success is measured" | §V.B | Span: Domains layer, Registry, Directory (capability map with owners). A design-time plane; WARM has none | span |
| C5 | Agent Runtime Plane | "supervisors, planners, specialist agents, memory/RAG components, deterministic validators, verifiers, tool routers, and human-approval workflows" | §V.B | Span: Harness, Orchestration, Memory, Retrieval, Evaluation, Approvals | span |
| C6 | Enterprise Capability Plane | "Existing SOA services, microservices, data products, SaaS APIs, knowledge bases, MCP servers ... and external A2A peers" | §V.B | Span: Tools, Providers layer, Retrieval | span |
| C7 | Supporting Control and Assurance Plane | "Identity, authorization, policy, security review, privacy review, model evaluation, red-teaming, release gates, audit, incident response, and change management" | §V.B | Span: Identity, Policy, Evaluation, Releases, Observability, Reliability | span |
| C8 | Agent Capability Contract (ACC) | "the core design artifact ... the record of the design decision that justifies an agent's existence" | §V.C | Span: agent definition (Registry), domain Goals, domain rules, domain tools, acceptance criteria. One contract per agent | span |
| C9 | ACC: Business capability and owner | "Names the durable capability, accountable product owner, operating team, funding model, and retirement owner" | Table II | Domain Goals ("who is accountable"), per agent | strained |
| C10 | ACC: Purpose and non-purpose | "what the agent is allowed to do and explicitly what it must not do" | Table II | Domain Roles (duties) | strained |
| C11 | ACC: Autonomy level | "L0-L4 action authority, approval requirements, reversibility expectations, and fallback behavior" | Table II | Domain rules | strained |
| C12 | ACC: Interaction topology | "supervised, specialist, peer, verifier, broker, deterministic-workflow adjunct, or human-assistive" | Table II | Orchestration | strained |
| C13 | ACC: Input/output schemas | "typed inputs, outputs, structured plans, evidence, citations, decisions, and error formats" | Table II | Agent definition | strained |
| C14 | ACC: Tool inventory and scopes | "permitted tools, service accounts, OAuth scopes, rate limits, write permissions, and disallowed tools" | Table II | Span: domain tools, Policy, Secrets, Scheduling | span |
| C15 | ACC: Data classification | "allowed data classes, retention, residency, privacy, and cross-tenant restrictions" | Table II | Policy (rules on stored data) | clean |
| C16 | ACC: State and memory design | "short-term context, long-term memory, write permissions, retrieval filters, poisoning defenses, deletion, and audit" | Table II | Memory | strained |
| C17 | ACC: Model behavior policy | "allowed model families, routing rules, context limits, temperature ceilings, fallback models" | Table II | Models | clean |
| C18 | ACC: Verification design | "deterministic validators, verifier/critic prompts, test oracles, confidence thresholds" | Table II | Acceptance criteria | strained |
| C19 | ACC: Human interaction | "ambiguity, risk, cost, confidence, legal, financial, or customer-impact triggers for human approval" | Table II | Domain rules (which actions need approval) | strained |
| C20 | ACC: Evaluation evidence | "offline tests, adversarial tests, regression suites, production canaries, and acceptance thresholds" | Table II | Evaluation | clean |
| C21 | ACC: Observability and audit | "trace schema, spans, model/tool calls, token/cost metrics ... incident replay" | Table II | Observability | clean |
| C22 | ACC: Versioning and deprecation | "prompt, model, tool, memory, and policy versions with rollback and retirement criteria" | Table II | Releases | clean |
| C23 | Registries (SOA discipline) | "other systems must discover what an agent can do and who owns it" | §IV.A | V6 (registry entries have owners) | planned (V6) |
| C24 | Contracts (SOA discipline) | "agents must publish capabilities, inputs, outputs, constraints, and expected effects" | §IV.A | Agent definition | strained |
| C25 | Versioning (SOA discipline) | "agent prompts, models, tools, memories, and policies change and must be release-managed" | §IV.A | Releases | clean |
| C26 | Runtime pattern: supervised tool-using agent | "a supervisor enforces the ACC, validates outputs, and handles escalation" | §V.D | Design-time guidance | guidance |
| C27 | Runtime pattern: brokered specialist agents | "only where specialization maps to separate capabilities, data boundaries, evaluation oracles, or release owners" | §V.D | Design-time guidance | guidance |
| C28 | Runtime pattern: verifier or challenger agents | "justified when independent critique materially improves safety or correctness" | §V.D | Design-time guidance | guidance |
| C29 | Runtime pattern: peer-to-peer collaboration | "appropriate when independently owned agents collaborate" | §V.D | Design-time guidance | guidance |
| C30 | Runtime pattern: human-in-the-loop execution | "Human approval is not an exception path; it is part of the interaction design" | §V.D | Design-time guidance (Approvals) | guidance |
| C31 | Principle 1: Capability before agent | "define the business capability and owner before defining the agent role or prompt" | §V.E | Design-time guidance (WARM's "domain defines roles before agents fill them") | guidance |
| C32 | Principle 2: Boundary before topology | "decide ownership, data, action, state, and evaluation boundaries before deciding whether to use one agent or many" | §V.E | Guidance | guidance |
| C33 | Principle 3: Contract-first | "every production agent requires an ACC" | §V.E | Guidance | guidance |
| C34 | Principle 4: Small number of durable agents | "prefer a few accountable agents over many role-playing prompt wrappers" | §V.E | Guidance | guidance |
| C35 | Principle 5: Autonomy is a design variable | "assign L0-L4 autonomy by action risk, reversibility, confidence, and evidence" | §V.E | Guidance | guidance |
| C36 | Principle 6: Least privilege follows design | "tool access is scoped per task, data class, action type, and autonomy level" | §V.E | V1 (grants scoped to the task) | planned (V1) |
| C37 | Principle 7: Memory is designed state | "memory requires ownership, retention, deletion, poisoning defenses, provenance, and review" | §V.E | Guidance | guidance |
| C38 | Principle 8: Deterministic checks first | "schema validation, policy checks, and business-rule validation should run before LLM critique" | §V.E | Guidance | guidance |
| C39 | Principle 9: Evaluate systems | "measure end-to-end task success, safe success, tool misuse ..." | §V.E | Guidance | guidance |
| C40 | Principle 10: Protocols are not trust boundaries | "MCP, A2A, APIs, and event buses need enterprise identity, authorization, and audit controls" | §V.E | Guidance (WARM Governance point 1) | guidance |
| C41 | Principle 11: Graceful degradation | "agents must know when to stop, ask, escalate, or fall back" | §V.E | Guidance | guidance |
| C42 | Principle 12: Retire agents | "unused, low-quality, duplicate, or unsafe agents should be deprecated like services" | §V.E | Guidance | guidance |
| C43 | Micro-agent proliferation (anti-pattern) | "creating many small agents because microservices became familiar" | §IV.C | Guidance | guidance |
| C44 | Decomposition criteria | "different business capabilities have different accountable owners; different agents need materially different data or tool permissions; ..." | §VIII.B | Guidance (WARM's "one worker or a team" considerations) | guidance |
| C45 | Safe success | "functional success with neither policy violation nor memory poisoning" | §VI.D | Evaluation (a metric definition) | strained |
| C46 | Recommendations 1-13 | e.g. "Start with a capability map. Identify business capabilities, owners, data classes, actions, and risk before naming agents"; 13 "kill switches, rollback, memory quarantine" | §IX | Guidance (one row; #13 overlaps V3) | guidance |
| C47 | Clarifying questions | "What business capability is the agent responsible for? Who owns that capability? ... which actions must remain human-owned?" | §II.A | Guidance | guidance |

Counted items: 47.

### C.3 The questions that matter most (CEAD)

**(a) An area of work as an entity of its own?** Only as a design input. "Capability before agent: define the business capability and owner before defining the agent role or prompt." The capability map lives in the Agent Design Plane, which "maintains the capability map, agent boundaries, ACCs ... It answers whether an agent should exist, what it owns, what it must not own" (§V.B). The capability is then recorded in each agent's ACC: "Business capability and owner — Names the durable capability, accountable product owner, operating team, funding model, and retirement owner." That makes it a per-agent contract.

Several agents per capability is discouraged: "Consolidate agents that share owner, data, tools, evaluation, and lifecycle" (Rec. 11). Splitting is justified when "different business capabilities have different accountable owners" (§VIII.B). Against WARM's seven parts: the ACC has goals (capability and owner), rules (autonomy, data classification, human interaction), tools, knowledge (memory design), and acceptance criteria (verification design, evaluation evidence). It does not define workflow or roles as positions filled by several actors. **Inference:** CEAD's capability bounds one agent or a small set of agents with the same owner. It is not a charter that several agents and people fill.

**(b) A record of who is accountable for what?** Two items:

- The ACC field "Business capability and owner", one per agent.
- An SOA-style registry: "other systems must discover what an agent can do and who owns it" (§IV.A).

So CEAD records an owner per agent and per capability, and states that discovery should return the owner. It describes no registry entry format. The owner is a person or team ("accountable product owner, operating team"), not an area of work.

**(c) Identity versus definition and instance; persistent versus task.** An agent "has an owner, identity, trace, evaluation record, cost record, and escalation path" (§III.A), and the ACC versions "prompt, model, tool, memory, and policy" (Table II). *Inference:* versioning the ACC while the agent keeps its owner and identity separates the agent from its definition implicitly. CEAD never says so outright. "Durable" refers to business capabilities ("durable business capabilities") and to agents as long-lived products ("a few accountable agents"; "treat every agent as a product with ... a retirement path"). It does not distinguish runtime persistence from per-task instances. A search for persistent, long-lived and ephemeral found one hit, "durable agent", in Principle 4.

**(d) Steps reserved for people; who may approve what.** Clarifying questions ask "which actions must remain human-owned?" (§II.A). Autonomy levels assign humans to execute (L1) or approve submission (L2). The ACC records "triggers for human approval" (Table II). "Human approval is not an exception path; it is part of the interaction design for irreversible, regulated, ambiguous, or high-impact actions" (§V.D). CEAD has no designation of who approves and no staffing of reserved steps. Its human-owned actions are close to Charterion's reserved steps in intent but carry no mechanism.

**(e) What CEAD does better.**

1. **Purpose and non-purpose.** The ACC states "explicitly what it must not do". WARM's Roles field is "duties" only. Matching would add exclusions to a role.
2. **A test for when to create an agent.** The decomposition criteria give one ("different business capabilities have different accountable owners; different agents need materially different data or tool permissions; tasks require different evaluation oracles; ..."). WARM sets "no number of agents per domain" and gives considerations only for teams. This is guidance and needs no model change.

---

## D. Salesforce, "The Agentic Enterprise - The IT Architecture"

### D.1 Inventory and assignment

**Layers (11; Figure 2 marks Agentic, AI/ML, Semantics and Enterprise Orchestration as new)**

| # | Item | Definition (verbatim) | Assignment | Type |
|---|---|---|---|---|
| D1 | Experience Layer | "the primary interface for human users ... hands off user intentions to the Agentic Layer ... facilitate human escalations and approvals" | Channels | clean |
| D2 | Agentic Layer | "the default runtime environment ... The configuration state of AI agents are stored and managed in this layer. Agents are instantiated for specific tasks, and the specific agent instances are decommissioned afterwards" | Span: Harness, Tasks, Registry, Memory, Policy | span |
| D3 | AI/ML Layer | "a centralized intelligence hub, offering AI models as a set of shared services" | Span: Models, Providers layer, Infrastructure (self-hosted) | span |
| D4 | Enterprise Orchestration Layer | "the control plane for end-to-end work ... provides the shared context and long-running memory to each new instance of an AI agent" | Span: Orchestration, Policy, Memory, Improvement | span |
| D5 | Application and App Services Layer | "exposes existing business application functionality as composable and modular tools and services for agents to use" | Span: Tools, Providers layer | span |
| D6 | Semantic Layer | "encodes and manages business entities, concepts, definitions, and inter-relationships, creating an enterprise ontology" | A shared cross-domain ontology is neither a platform service nor one domain's knowledge in WARM | misfit |
| D7 | Data Layer | "the foundational source of truth ... secure, governed access to all enterprise data" | Span: Retrieval, Infrastructure, domain knowledge | span |
| D8 | Infrastructure Layer | "compute, storage, network, and cloud capabilities required to run AI and agentic workloads" | Infrastructure layer | clean |
| D9 | Integration Layer | "the universal communication fabric for all systems ... through APIs, events, protocols, and middleware" | Span: Tools, Messaging, Registry | span |
| D10 | IT Operations and Observability Layer | "monitors and manages the health and operational performance of agents and the entire system" | Span: Observability, Reliability, Improvement | span |
| D11 | Security and Governance Layer | "identity management, threat detection, GRC, and AI-specific security measures" | Span: Identity, Policy, Evaluation | span |

**Key technology capabilities**

| # | Capability | Definition (short verbatim) | Assignment | Type |
|---|---|---|---|---|
| D12 | Conversational AI & Digital Assistants | "Enable the UX by default to feature AI assistance" | Channels | clean |
| D13 | Attribution & Transparency UI | "showing citations, sources of files/systems, and the approach/rationale" | Channels | strained |
| D14 | Proactive & Ambient Notification Service | "Enables agents to proactively push insights or alerts to users on the most appropriate channel" | Channels | clean |
| D15 | Omnichannel Experiences | "conversations and tasks follow the person instead of the app" | Channels | clean |
| D16 | Multi-Modal Capabilities | "text, voice, image, touch, video, and AR/VR" | Channels | clean |
| D17 | Context-Aware Personalization & Dynamic UI | "UI generation on the fly" | UI generation is outside WARM | misfit |
| D18 | Agent Runtime Environment | "Manages the lifecycle, execution, and resource allocation for AI agents" | Span: Harness, Tasks, Scheduling | span |
| D19 | Agent Lifecycle Management Suite | "development frameworks, dev and test tooling, and management systems for agent activities and version control" | Releases | strained |
| D20 | Agent Reasoning Engine | "decompose goals, plan, and decide what tools to use" | Harness (reasoning is out of WARM's scope) | strained |
| D21 | Agent Memory and Context Store | "Allows agent instances to recall and maintain context about previous interactions" | Memory | clean |
| D22 | Agent Interoperability Protocols | "A2A ... Model Context Protocol" | Span: Messaging, Tools | span |
| D23 | Tool Registry | "A curated set of internal and externally supported tools for agents to invoke" | Registry | clean |
| D24 | Agent Registry | "A curated ecosystem of pre-built AI solutions and agents that supports discovery and capability matching" | Registry | clean |
| D25 | Distributed Agent Policy Enforcement | "allowing agents to self-check compliance before taking actions" | Policy. Conflicts with WARM: a cross-cutting service must act "without the cooperation of the agent" | strained |
| D26 | Agent Self-Reflection & Adaptation Framework | "with human approval, trigger improvements or suggest modifications to itself" | Improvement | clean |
| D27 | Pre-built Foundation Models | "Large ML models trained on a broad spectrum of data" | Providers layer | clean |
| D28 | Retrieval-Augmented Generation | "grounds foundation models in enterprise-specific data" | Retrieval | clean |
| D29 | AI Trust, Safety & Governance Hub | "bias detection, explainability, and safety monitoring" | Span: Policy (V5), Evaluation, Observability | span |
| D30 | Model Gateway | "a single entry point for all model inference requests ... to optimize for cost, performance, and compliance" | Models | clean |
| D31 | Model Development Workbench | "data preprocessing, model training, and experimentation" | Building models is outside WARM | misfit |
| D32 | MLOps & Lifecycle Automation Pipeline | "automating the end-to-end lifecycle of models from training to deployment and retirement" | Releases (model training is outside WARM) | strained |
| D33 | Model Serving & Inference Runtime | "deploying trained models as secure API endpoints" | Infrastructure layer (WARM: a self-hosted model runs on infrastructure) | strained |
| D34 | Model & Asset Registry | "repository for all AI/ML assets, including models, datasets, and source code" | Registry | strained |
| D35 | Synthetic Data Generation and Management | "generate and manage synthetic data" | Outside WARM | misfit |
| D36 | Hybrid Workflow Execution Engine | "executes the 'blended orchestration model,' providing centralized oversight while allowing for local agent choreography" | Orchestration | clean |
| D37 | Process Governance & Constraint Engine | "applies declarative business rules, policies, and constraints to all in-flight processes" | Policy | clean |
| D38 | Shared Memory and Context Management | "A shared memory layer accessible to all actors in a workflow" | Span: Sessions, Memory | span |
| D39 | Process Modeling Studio | "machine-legible, semantically rich process models that define both deterministic and dynamic, goal-oriented steps" | Domain Workflow (design tool) | strained |
| D40 | Process Optimization and Simulation | "what-if simulations, and predictive optimization" | Improvement | strained |
| D41 | Process Discovery & Health Monitoring | "report on business metrics of process health" | Observability | strained |
| D42 | Digital Twin Process Modeling | "A real-time mirror of live workflows for testing, simulating changes" | No WARM part | misfit |
| D43 | Modular Application Services | "published as machine-readable actions for agents to call" | Tools | strained |
| D44 | Agent Embedding SDKs | "embed agents directly into application UIs" | Channels | strained |
| D45 | Dynamic UI Generation Services | "generate or modify UI components in real-time" | Outside WARM | misfit |
| D46 | AI-Native UI Frameworks | "Front-end frameworks designed with built-in support for handling AI-driven UIs" | Outside WARM | misfit |
| D47 | Agent-Infused Systems of Engagement | "productivity and collaboration applications that incorporate AI agent capabilities" | Channels | strained |
| D48 | AI-Enhanced Low-Code / No-Code | "create custom apps and services using natural language" | Outside WARM | misfit |
| D49 | App Guardrails for Agent Usage | "rate limiting, scoped permissions, and telemetry" | Span: Policy, Scheduling, Observability | span |
| D50 | Metadata Service | "descriptive metadata, including data lineage, ownership, and classifications" | Retrieval | strained |
| D51 | Business Glossary & Taxonomy Management | "define and agree upon standard business terms" | Domain knowledge | strained |
| D52 | Semantic Model Management | "create, manage, and govern semantic models and ontologies" | As D6 | misfit |
| D53 | Enterprise Knowledge Graph | "stores and maps the relationships between business entities" | As D6 | misfit |
| D54 | Metadata Ingestion & Harmonization Engine | "populates and maintains the Enterprise Knowledge Graph" | As D6 | misfit |
| D55 | Semantic Query Engine | "Interprets natural language queries and constructs structured queries" | Retrieval | strained |
| D56 | Semantic Reasoning Engine | "derives implicit knowledge and hidden relationships from the EKG" | As D6 | misfit |
| D57 | VectorDB | "storing and querying high-dimensional vector embeddings, critical for RAG" | Retrieval | strained |
| D58 | Intelligent Analytical Data Pipelines | "data ingestion, transformation, and loading (ETL/ELT)" | Data engineering is outside WARM | misfit |
| D59 | Enterprise Data Lakehouse | "A central repository for structured, semi-structured, and unstructured data" | Infrastructure layer | strained |
| D60 | Zero-Copy Data Federation & Search | "querying, and searching data across multiple stores without physical data movement" | Retrieval | strained |
| D61 | Natural Language to SQL | "converting natural language queries into SQL" | Retrieval | strained |
| D62 | Enterprise Data Catalog & Discovery Service | "A centralized, searchable inventory of all data assets" | Retrieval (named sources) | strained |
| D63 | Master & Reference Data Management | "the 'golden record' for critical business entities" | Outside WARM | misfit |
| D64 | Adaptive Data Quality Service | "detect and remediate data quality issues" | Outside WARM | misfit |
| D65 | Data Contracts | "Machine-readable agreements between data producers and consumers" | Outside WARM | misfit |
| D66 | AI-Specialized Data Stores | "time-series or graph databases" | Infrastructure layer | strained |
| D67 | AI-Ready Data Fabric | "a unified, virtualized view of data across disparate physical systems" | Retrieval | strained |
| D68 | Real-Time Data Processing | "processing and analyzing multi-modal data streams continuously" | Outside WARM | misfit |
| D69 | Infrastructure as Code | "Automated provisioning and management of infrastructure with CI/CD deployment pipelines" | Releases ("the infrastructure the system manages") | clean |
| D70 | Hybrid & Multi-Cloud AI Infrastructure | "public cloud elasticity and specialized infrastructure" | Infrastructure layer | clean |
| D71 | AI-Optimized Compute, Storage, and Network | "Dynamically allocates and scales infrastructure resources" | Infrastructure layer | clean |
| D72 | Edge AI Infrastructure | "deployed at the edge of the network" | Infrastructure layer | clean |
| D73 | Self-Healing Infrastructure | "manage system recovery without manual input" | Reliability | clean |
| D74 | Sustainable AI Computing | "Energy-efficient approaches" | A concern with no WARM part | misfit |
| D75 | Cost- & Carbon-Aware Autoscaling | "FinOps and sustainability signals to drive scaling and placement" | Infrastructure layer (cost is a WARM concern) | strained |
| D76 | Operational Data Connectivity Pipeline | "automatic schema mapping, data transformation, and workflow generation" | Data integration, outside WARM | misfit |
| D77 | Adaptive API Management and Service Mesh | "dynamically register, discover, and govern services with adaptive policy enforcement for agents" | Tools | strained |
| D78 | Semantic Knowledge Adapters | "a shared vocabulary and data model across agents and applications" | As D6 | misfit |
| D79 | Event-Driven Integration Fabric | "messaging and streaming backbone that enables decoupled, asynchronous communication" | V11 (events) | planned (V11) |
| D80 | Agent Protocol Gateway | "A gateway for MCP services that allows agents to securely discover tools and trigger actions" | Tools | clean |
| D81 | Composable Capability Catalog & Marketplace | "a centralized, governed catalog for all enterprise capabilities—APIs, services, agent skills, models, and datasets" | Registry | strained |
| D82 | Real-Time Monitoring & Observability Platform | "logs, metrics, and traces ... with extensions for ML metrics and agent behavior" | Observability | clean |
| D83 | FinOps & Cloud Cost Management | "optimizing the infrastructure costs associated with AI and agentic workloads" | Observability (cost is a WARM concern) | strained |
| D84 | Agent and ML-specific Monitoring | "Logs each step of an agent's run in an immutable audit trail" | Observability | clean |
| D85 | AIOps, Incident and Change Management | "predict potential IT issues, identify root causes, and create remediation workflows" | Span: Reliability, Releases | span |
| D86 | Closed Learning Feedback Loop | "Integrates observability telemetry from agents back into MLOps pipelines, enabling automated model retraining or prompt adjustment" | Improvement | clean |
| D87 | Semantic Observability Engine | "detection of semantic anomalies in agent behavior" | Evaluation | strained |
| D88 | LLM Input/Output Security & Guardrails | "block unsafe content, PII leaks, and jailbreaks" | V5 | planned (V5) |
| D89 | Zero Trust Architecture with AI Verification | "granular, just-in-time access for agents based on their specific task" | V1 | planned (V1) |
| D90 | Agent Security Framework | "Fine-grained permission models, monitoring for harmful behaviors, and containment mechanisms to safely interrupt agent activities" | Span: Policy, V3, Environments | span |
| D91 | AI Model Security | "controls at each stage of the model lifecycle to protect against poisoning, extraction" | Outside WARM | misfit |
| D92 | Privacy-Preserving AI | "federated learning and differential privacy" | Outside WARM | misfit |
| D93 | AI-Enhanced GRC | "Use of AI agents to continuously monitor IT architecture compliance" | Domains layer (a compliance domain) | strained |
| D94 | Policy-as-Code Engine | "A single source of truth for defining business rules and compliance constraints" | Policy | clean |
| D95 | Continuous Red-Teaming | "Automated, ongoing adversarial testing of AI models and agents" | Evaluation | strained |

**Principles, maturity levels and business capabilities**

| # | Item | Definition (short verbatim) | Type |
|---|---|---|---|
| D96-D103 | 8 principles: Composability and modularity; Data and semantic first; IT and business observability embedded; Trust-throughout; Agent-first with human oversight ("the ability for humans to monitor, intervene in, and override any step of an agent's process"); Reactive and multimodal interaction; AI-ready infrastructure; Open ecosystem | design guidance | guidance (8) |
| D104 | Level 0 | "fixed-rule chatbots and co-pilots" | guidance |
| D105 | Level 1: Information Retrieval Agents | "Enhance human worker productivity by providing a trusted, conversational interface for querying enterprise knowledge" | guidance |
| D106 | Level 2: Simple Orchestration, Single Domain Agents | "Automate routine tasks and orchestrate low-complexity workflows within a single business domain" | guidance |
| D107 | Level 3: Multi-Domain Orchestration Agents | "Automate complex, end-to-end business processes that span organizational and functional boundaries" | guidance |
| D108 | Level 4: Multi-Agent, Multi-Domain Orchestration | "enabling dynamic, emergent collaboration between agents" | guidance |
| D109-D114 | 6 business capabilities: Augmented Human Productivity; Adaptive Capability Improvement; Elastic Workforce Capacity; Predictive Operational Resilience; Autonomous Process Execution; Transboundary Orchestration | business outcomes, not system parts | guidance (6) |

Counted items: 114.

### D.3 The questions that matter most (Salesforce)

**(a) An area of work as an entity of its own?** No. "Domain" appears 16 times and is never defined. Uses: "work within and across business domains"; "within a single business domain" (Level 2); "Cross-domain agentic workflows" (Figure 3); "a centralized Enterprise Knowledge Graph (EKG) that links data across domains". The Level 2 to Level 4 progression treats a domain as the scope of an agent's or workflow's reach, which is the frame WARM's prior-work reading already found in Microsoft and OpenAI. No charter, roles, workflow or acceptance criteria are tied to a domain. **Inference:** the "Enterprise Orchestration Layer" holds per-process models ("critical business processes in machine-legible semantically rich formats", with KPIs from the Semantic Layer). That is the nearest thing to WARM's Workflow and Goals, and it is attached to a process, not to an area of work.

**(b) A record of who is accountable for what?** No. The page names four registries:

- Agent Registry: "A curated ecosystem of pre-built AI solutions and agents that supports discovery and capability matching".
- Tool Registry: "A curated set of internal and externally supported tools for agents to invoke".
- Model & Asset Registry: "repository for all AI/ML assets, including models, datasets, and source code".
- Composable Capability Catalog & Marketplace: "APIs, services, agent skills, models, and datasets—annotated with semantic metadata".

It also names the Enterprise Data Catalog and the Metadata Service ("data lineage, ownership, and classifications"). The page describes no entry contents beyond those phrases. "Owner" appears once, and only for data ownership in the Metadata Service. "Accountable" appears 0 times.

**(c) Identity versus definition and instance; persistent versus task.** The page separates stored configuration from task instances and has *only* task instances:

> "The configuration state of AI agents are stored and managed in this layer. Agents are instantiated for specific tasks, and the specific agent instances are decommissioned afterwards. This implementation enables agents to be always invoked from the latest configuration state based on offline optimizations" (Agentic Layer)

> "This layer provides the shared context and long-running memory to each new instance of an AI agent for critical workflows." (Enterprise Orchestration Layer)

Continuity therefore lives in the configuration and in shared workflow memory, not in a persistent agent. The page gives agents an identity only in security terms ("just-in-time access for agents based on their specific task"). It does not say whether an instance has an identity of its own.

**(d) Steps reserved for people; who may approve what.** "Agent-first with human oversight: ... the ability for humans to monitor, intervene in, and override any step of an agent's process. Agents require self-reflective capabilities to proactively seek human guidance if its confidence over decision-making falls below pre-programmed thresholds." The Experience Layer provides "the dynamic UI and visualizations that facilitate human escalations and approvals within agentic workflows." The orchestration layer "can ensure appropriate levels of human involvement (e.g., exception handling)". Self-adaptation acts "with human approval". The page names no reserved steps and no approver. Approval is a UI and orchestration feature, close to WARM's Approvals but without the hold-and-record contract.

**(e) What Salesforce does better.**

1. **Shared, long-running memory across task instances of one workflow** (Enterprise Orchestration Layer). WARM's Sessions covers "a stretch of an agent's work" and Memory covers "what agents learn". Neither holds shared context for every actor in a long workflow. To match, WARM would state where workflow-scoped context lives, which today is not clear between Sessions, Memory and Orchestration.
2. **Business KPIs per process, fed back from observed agent work** ("continually tracks and evaluates key performance indicators (KPIs)"). This is close to WARM's Goals, Evaluation and Improvement, and more concrete.

One conflict rather than an improvement: "Distributed Agent Policy Enforcement: Enables enterprise-wide governance by allowing agents to self-check compliance before taking actions." WARM requires a cross-cutting service to act "without the cooperation of the agent that performs it". The Salesforce item is guidance WARM rejects, and WARM is right to.

---

## Reverse direction, all four sources

F = fully, P = partly, A = absent (after the search listed in the Appendix). Where = section or item number.

| WARM part | A. Charterion | B. AEON | C. CEAD | D. Salesforce |
|---|---|---|---|---|
| Harness | A as a component; Def. 2.1 describes the loop in prose | A | P: runtime plane "planners" (C5) | P: Reasoning Engine, Runtime Environment (D18, D20) |
| Sessions | A (only protocol binding names "steps/sessionStart") | P: "The chain is constructed at session start" (§7.3) | P: ACC "short-term context" (C16) | P: context store, omnichannel continuity (D15, D21) |
| Tasks | A | P: descriptor failure handling; "freezing operations in progress" (B11, B26) | P: "maintain task state" (C1) | P: runtime lifecycle; "transactional integrity of workflows and rollback logic" (D4, D18) |
| Environments | F: Containment Zone / Sandbox (A48) | A | A | P: "containment mechanisms" (D90) |
| Scheduling | P: instance `Cardinality` (A99) | A | P: "process triggers"; "rate limits" (C3, C14) | P: events, rate limiting, autoscaling (D49, D75) |
| Memory | F: Scoped Memory Store (A37) | A | F: ACC memory design (C16) | F: Memory and Context Store (D21) |
| Retrieval | P: "retrieved context, vector stores" listed as memories | P: retrieval from subdomains via integration (B5) | P: "memory/RAG components" (C5) | F: RAG, Semantic Query Engine (D28, D55) |
| Artifacts | A (its "artefacts" are the framework's own documents) | P: evidence records "artifacts produced" (§9.1) | A | A |
| Models | F: Model Endpoint Registry (A45) | A | F: ACC model behavior policy (C17) | F: Model Gateway (D30) |
| Tools | F: Tool Gateway, Tool Catalogue (A35, A44) | P: adapters (B28) | P: capability plane, tool scopes (C6, C14) | F: Agent Protocol Gateway (D80) |
| Registry | P: Agent Register, Tool Catalogue (A22, A35) | F: capability registry (B30) | P: SOA registries (C23) | F: Agent and Tool Registries (D23, D24) |
| Directory | P: computable step-to-agent and agent-to-human map; not a lookup for handoff (A23, A87) | P: registry names "the subdomain that provides it" (B30) | P: ACC capability and owner (C9) | A |
| Messaging | P: protocol bindings only | P: agent network protocol (B27) | P: "A2A-like protocols" (C29) | P: Interoperability Protocols (D22) |
| Orchestration | F: Orchestrator, delegation (A43) | F: workflow descriptor (B26) | P: interaction topology (C12) | F: Hybrid Workflow Execution Engine (D36) |
| Channels | A (no human or application interface to agents) | P: AIDEX "worker-facing" (B51) | P: Intent and Outcome Layer (C3) | F: Experience Layer (D1) |
| Identity | F: Agent Register, Def. 2.1 (A22, A73) | F: identity plane, people only (B2) | P: "enterprise identity" (C1) | P: Zero Trust (D89) |
| Secrets | A: "Charterion does not specify ... the cryptographic mechanics of identity, credentials and attestation" | A | P: "service accounts, OAuth scopes" (C14) | A |
| Policy | F (A46, A47) | F (B3) | F (C7, C15) | F (D37, D94) |
| Approvals | F: escalation human, approver role (A26, A65) | F: escalate; propose-and-confirm (B14, B45) | P: L2 "human approves submission"; triggers (C2, C19) | P: "human escalations and approvals" in the UI (D1) |
| Observability | F: Decision Log, Telemetry (A39, A50) | F: evidence plane (B4) | F: ACC observability (C21) | F (D82, D84) |
| Evaluation | P: Evidence Record rates (A56) | P: capability qualification "evaluates them against architectural fit" (§11.2) | F: ACC evaluation evidence (C20) | P: red-teaming, semantic observability (D87, D95) |
| Improvement | P: evidence-gated promotion, re-scoping from requests (A79, §16.2 step 6) | A | A | F: Self-Reflection, Closed Learning Feedback Loop (D26, D86) |
| Releases | P: lifecycle gates, config digest (A27, A54) | P: capability lifecycle, versioning (B31, B33) | F: ACC versioning, release gates (C22, C25) | P: Lifecycle Suite, IaC (D19, D69) |
| Reliability | P: halt and containment only | P: degraded operation, chaos testing (B12, B37) | P: "incident response" (C7) | P: Self-Healing, AIOps (D73, D85) |
| Layer: People | F: humans, roles, principals, overseers | F: principals, workers | P: owners, approvers | P: human workers |
| Layer: Domains | P: capability and process scope (A74); slice | P: subdomains (B49) | P: capability map (C4) | P: "business domain" undefined (D106) |
| Layer: Platform | P: execution plane substrate (A11) | F: meta-orchestration runtime (B7) | P: runtime plus control planes | F: Agentic, AI/ML and Orchestration layers |
| Layer: Infrastructure | F: L5 nodes (A42) | P: I&O subdomain (B58) | A | F (D8) |
| Layer: Providers | P: "vendor reference architectures" only as comparison; Providers not modeled | P: vendor components (§6.2) | P: "external LLM providers"; SaaS APIs (C6) | P: Foundation Models (D27) |
| Part: Goals | P: L0 goals, Pursues per charter (A17) | A | P: ACC capability and owner (C9) | P: process KPIs (D4) |
| Part: Roles | P: human roles only; agents hold charters (A21) | A | P: purpose and non-purpose (C10) | A |
| Part: Workflow | F: processes, steps, order, designations (A19, A74) | A (subdomain internals out of scope) | A | P: process models (D39) |
| Part: Domain knowledge | P: memory scoped to a scope (A37) | A | P: memory design (C16) | P: Semantic Layer, cross-domain (D6) |
| Part: Domain tools | F: Requires and Exposes per step (A34, A35) | P: adapters (B28) | F: tool inventory per agent (C14) | P: app services (D43) |
| Part: Domain rules | F: SoD, reserved, obligations, caps | P: enterprise policy only (B15) | F: ACC autonomy, data classification, human interaction | P: process constraints (D37) |
| Part: Acceptance criteria | A for work products; promotion thresholds judge charters | A | F: verification design, evaluation evidence (C18, C20) | A |
| Directory (service) | see row above | see row above | see row above | see row above |

---

## Counts per source

Computed from the Type column of each inventory table (script output, 2026-11-11).

| Source | Items | Clean | Strained | Spans | Guidance | Already planned | Misfits |
|---|---|---|---|---|---|---|---|
| A. Charterion | 112 | 9 | 33 | 24 | 6 | 12 | 28 |
| B. AEON | 58 | 13 | 16 | 15 | 5 | 6 | 3 |
| C. CEAD | 47 | 6 | 11 | 7 | 20 | 2 | 1 |
| D. Salesforce | 114 | 25 | 30 | 15 | 19 | 3 | 22 |

Planned items by Vn:

- Charterion: V1 (A95), V2 (A30, A80, A89, A96, A113), V3 (A25, A49, A92, A110), V14 (A36, A97).
- AEON: V1 (B9, B17), V3 (B11), V5 (B18), V6 (B31), V13 (B24).
- CEAD: V1 (C36), V6 (C23).
- Salesforce: V1 (D89), V5 (D88), V11 (D79).

Misfits fall into five groups:

1. **Authority between agents.** Delegation, precedence, perimeter, blast radius, cap composition: A24, A29, A31, A32, A90, A91, A101, A103, A104.
2. **Human capacity and accountability.** A33, A86, A94, A100, A105.
3. **A design-time model of authority, warranted facts and target resolution.** A7, A10, A13, A16, A38, A53.
4. **Out of scope.** Cross-organization or cross-classification (A9, A12, A58-A60, A72, B10, B43, B44) and data or model engineering (Salesforce).
5. **Vocabulary WARM lacks.** Autonomy levels (A76, C2), accepted defects (A55), shared ontology (D6 and related).

---

## What WARM might change

Each candidate states the evidence, the supporting sources and the confidence.

| # | Change | Evidence | Sources | Confidence |
|---|---|---|---|---|
| W1 | **Narrow the claims in "What WARM adds".** Drop "an agent is an identified actor" as a contribution. Say that areas of work separate from agents exist in enterprise architecture (capabilities, processes, subdomains), and that what WARM adds is a domain defined by seven parts that agents and people fill. Say that capability registries naming a provider exist, and that WARM's Directory differs by recording accountability for responsibilities at the handoff grain | Charterion Def. 2.1 and its own statement that "the agent as a principal ... these are stated, since 2025, by the Cloud Security Alliance, NIST, OWASP, IMDA, Google"; AEON §11.1; CEAD Principle 1 | A, B, C | High |
| W2 | **An accountable person for each agent identity, or for each role assignment.** Every identity that can change state traces to a named person who answers for it, recorded with the identity or the role assignment, and checked (no identity whose accountable person is missing or whose role is vacant) | Charterion WF1, Prop. 7.3 ("a charter whose principal is a role nobody holds ... common when agents outlive the reorganisation"); CEAD "it has an owner"; AEON principal chain | A, C, B | High |
| W3 | **Separate three human relations in Step 4 and in Approvals.** (1) A step or responsibility reserved to people: a domain rule saying no agent performs it, with a staffed role. (2) An escalation decided by a named person. (3) Approval of authority (grants, rules). Approvals keeps (2). (1) goes to domain Roles and rules. (3) joins V1 and V2 | Charterion Def. 8.1, WF8, WF15, Table 18.2; CEAD "which actions must remain human-owned"; AEON escalate vs lifecycle approval | A, C, B | High that the gap is real; medium on placement |
| W4 | **Attenuation and independence in delegated authority** (extend V1 and V2). Authority a starting agent passes to a task agent never exceeds its own. Two agents under a common starting agent are not independent for separation of duties | Charterion WF6, Prop. 7.2, WF11 and its rationale; AEON scoped sub-tokens derived from the root | A, B | Medium-high |
| W5 | **The Approvals contract names the decider and covers availability.** For each held action: who decides, what happens if no current person can, and a bound on how many decisions one person receives | Charterion WF9, WF20 ("the escalate outcome degrades in fact to permit") | A | Medium |
| W6 | **Running configuration equals reviewed configuration.** Releases or Evaluation records the configuration that was evaluated and detects drift in what runs | Charterion WF13 | A (CEAD versioning supports it weakly) | Medium |
| W7 | **Policy outcomes beyond allow and deny.** Name escalate (to Approvals), constrain, redact, route and log, and an "unknown" outcome when the facts relied on are stale or uncertain | AEON §8.1; Charterion §9.3 | B, A | Medium |
| W8 | **Use AEON's consume / promise / guarantee form as the template for WARM's missing service contracts** (Limit 4) | AEON §7.6, §8.6, §9.6, §10.5, §11.6 | B | Medium |
| W9 | **State whose identity a task agent acts under.** WARM says the platform retains "the identity under which it acted" but not whether that is its own, its starting agent's or a person's. The sources split three ways: Charterion instances act "under the identity of" their type; AEON agents carry the human principal's identity; Salesforce does not say | Charterion Def. 8.9; AEON §4, §7.3 | A, B | Medium |
| W10 | **Add a role's exclusions ("non-purpose") to domain Roles** | CEAD ACC "explicitly what it must not do" | C | Low-medium |
| W11 | **State where workflow-scoped shared context lives** (between Sessions, Memory and Orchestration) | Salesforce Enterprise Orchestration Layer, Shared Memory and Context Management | D | Low-medium |
| W12 | **Autonomy levels as a named vocabulary for domain rules** (observe, draft or propose, act with confirmation, act alone) | Charterion Def. 6.1; CEAD L0-L4 | A, C | Low |
| W13 | **Record accepted exceptions with an expiry** (a rule the system knowingly does not meet) | Charterion §18.7 | A | Low |
| W14 | **Scope statement for cross-organization work.** Say that agents of two organizations transacting are out of scope | Charterion boundary plane; AEON federation | A, B | Low |

---

## What this does to WARM's claims

| Claim | Verdict | Deciding quotation |
|---|---|---|
| (i) No published model has a domain as a charter separate from its agents | **Stands as worded, weakened.** No source has a charter of an area of work that agents and people fill. Charterion's charter is per agent. AEON's subdomains are separate from agents but are IT units with contracts for consuming the platform. CEAD's capability sits inside one agent's contract. The broader statement "no model separates an area of work from its agents" would be **false**: AEON and Charterion both do | Charterion: "A charter Charter(m, a, σ, ℓ, π) states that agent a may act within business scope σ" (Def. 7.1). AEON: "The subdomains are the capability areas the control plane orchestrates ... Each subdomain has its own runtime, its own internal architecture, its own engineering function, and its own vendor relationships" (§5, App. A) |
| (ii) No published model has a directory of which domain is accountable for what | **Weakened.** AEON's capability registry records, per capability, the subdomain that provides it, and agents discover each other through it. It does not record accountability, exclusivity or responsibilities at the handoff grain. Charterion's registers let one compute which agent covers each step and which human answers for each agent, but they are not presented as a handoff lookup. CEAD records an owner per agent. The claim survives only with the word "accountable" doing the work, and the paper should say so and cite AEON | AEON: "Every capability any subdomain exposes is registered in the registry along with its metadata: the subdomain that provides it ... and the principals authorized to invoke it" (§11.1); "how agents discover other agents (through the capability registry ...)" (§10.2) |
| (iii) No published model distinguishes persistent agents from task agents as WARM does | **Stands, weakened.** Charterion distinguishes a chartered type from ephemeral instances. Salesforce makes every agent a task instance with stored configuration and shared memory. Neither has an agent that persists across tasks with its own memory and channel. Salesforce's design is the opposite of WARM's persistent agent | Salesforce: "Agents are instantiated for specific tasks, and the specific agent instances are decommissioned afterwards. This implementation enables agents to be always invoked from the latest configuration state". Charterion: "An agent type is chartered once and instantiated many times, ephemerally" (§8.12) |
| (iv) No published model treats an agent as an identified actor distinct from its definition | **Refuted.** Charterion defines the agent as a principal with an identity to which authority and accountability attach. It keeps that identity, and the charter, separate from the configuration (model, prompt, tools), whose change it detects as drift. Charterion also credits the agent-as-principal idea to earlier security and standards bodies. Where WARM still differs: Charterion's identity is per type, shared by instances, while WARM identifies each agent | Charterion: "An agent is a non-human principal: it has an identity to which authority and accountability attach, it may be instantiated many times" (Def. 2.1); "The agent that was reviewed at gate G2 is not necessarily the agent that runs: model, prompt, tool set and runtime version change without a change to the charter" (§8.11); "Charterion does not claim to have invented the agent as a principal, the human sponsor, scoped or attenuating delegation ... these are stated, since 2025, by the Cloud Security Alliance, NIST, OWASP, IMDA, Google and others" (How to read) |

What the sources state and what I infer are kept apart above. The inferences:

- Charterion's registers can produce a step-to-agent map.
- CEAD's results come from a simulation.
- CEAD implicitly separates agent and definition through ACC versioning.
- Salesforce's process models are the nearest thing it has to Workflow and Goals.

Every other verdict rests on the quoted text.

## Appendix: search terms used for absence claims

Case-insensitive substring counts over the full extracted text of each source:

- **Harness:** agent loop, harness, context window, reasoning engine, planner, loop
- **Sessions:** session, conversation, thread, checkpoint, resume
- **Tasks:** task lifecycle, retry, cancel, durable, job, "run "
- **Environments:** sandbox, zone, isolat, workspace, contain
- **Scheduling:** schedul, cron, trigger, queue, rate limit, concurren, event
- **Memory:** memory, remember, learn
- **Retrieval:** retriev, rag, knowledge base, search, grounding
- **Artifacts:** artifact, artefact, output, work product, report
- **Models:** model endpoint, model gateway, model routing, foundation model, llm, model famil, fallback model
- **Tools:** tool, mcp, adapter, gateway, api
- **Registry:** registry, catalog, catalogue, register
- **Directory:** directory, accountable, owner, responsib, who owns
- **Messaging:** a2a, agent-to-agent, message, messaging, protocol
- **Orchestration:** orchestrat, handoff, workflow, delegat, supervisor
- **Channels:** channel, interface, user experience, conversational, invoke, api
- **Identity:** identity, principal, authenticat, idam
- **Secrets:** secret, credential, vault, key manag, password, token
- **Policy:** policy, permission, authoriz, authoris, guardrail, retention
- **Approvals:** approv, human-in-the-loop, human in the loop, escalat, confirm
- **Observability:** observab, trace, audit, telemetry, log
- **Evaluation:** evaluat, eval, test, red-team, red team, verif
- **Improvement:** improve, optimi, feedback loop, self-reflection, retrain, learning
- **Releases:** version, release, rollback, roll back, deploy, change manag
- **Reliability:** reliab, recover, availab, self-heal, incident, degrad, chaos
- **People:** human, person, people, worker, employee
- **Domains:** domain, charter, subdomain, capability area, business capabilit
- **Platform:** platform, control plane, runtime
- **Infrastructure:** infrastructure, compute, node, cloud, network, storage
- **Providers:** vendor, provider, external service, saas, third-party, third party
- **Goals:** goal, objective, purpose, outcome, kpi
- **Roles:** role
- **Workflow:** workflow, process, step
- **Domain knowledge:** knowledge, ontology, glossary, semantic
- **Domain tools:** tool, connector, api
- **Domain rules:** rule, constraint, obligation, reserved
- **Acceptance criteria:** acceptance, criteria, threshold, success, oracle
- **Persistent versus task:** persistent, long-lived, long-running, ephemeral, instance, instantiat, decommission, transient, durable agent

Notable zero or near-zero results:

- AEON: llm 0 real hits (all inside "enrollment"); memory 1; secret 0; "accountable" 4, all about human principals.
- Salesforce: "accountable" 0; secret 0; "owner" 1.
- Charterion: persistent 0; long-lived 0; ephemeral 1; secret 0, with credentials stated as out of scope.
- CEAD: persistent 0; "durable agent" 1.
