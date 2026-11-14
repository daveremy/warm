---
title: "Charterion v2.0, the pages the first mapping did not read, against WARM v0.12"
date: 2026-11-11
yardstick: warm-model-v0.12.md (Steps 0-4, glossary, "What WARM adds, and its limits")
earlier-mapping: prior-work/mapping-round2-charters.md, section A (against WARM v0.11)
source: "El Hassani, Charterion v2.0, Zenodo 10.5281/zenodo.22829848, Charterion_v2.0_Specification.pdf (290 PDF pages, 2,284,217 bytes, downloaded 2026-11-11)"
status: analysis; read-only; one reader, not second-rated
---

# Charterion v2.0: the unread pages, read

## Summary

I read every PDF page the first mapper did not read (list in section 5). The full text does not change any of the four verdicts.

| Claim | Verdict after the full reading | Deciding text |
|---|---|---|
| (i) No model has a domain as a charter that several agents and people fill | **Unchanged.** No unread part defines a domain, an organizational unit, a team of agents, or acceptance criteria for work products. Agents never fill roles: the ArchiMate profile forbids it | "Software actor that performs steps; never a Business Actor, because accountability stays with humans" (Table E.1, Agent row, p. 248) |
| (ii) No model has a directory of which area of work is accountable for which responsibility, used to hand work over | **Unchanged.** No register is presented as a lookup for handing work over. The reference substrate service that agents call answers admissibility questions about one named agent only | MCP tools of the substrate service: "admissible", "authority_of agent", "envelope_of agent", "why", "request_authority", "model_snapshot" (Table K.2, p. 272); "the routing of the human decision is the organisation's workflow system's" (p. 94) |
| (iii) No model distinguishes agents that persist across tasks from agents created for one task | **Unchanged in verdict; the reasoning must be corrected.** Charterion's agent is long-lived and can retain memory between actions, so "no agent ... with its own memory" is wrong. It still has one kind of agent; what is started per task is an instance with no identity of its own, and instance-level identity was considered and set aside | "An instance i of agent a is a running process that acts under the identity of a and holds no charter of its own" (Def. 8.9, p. 61); "Z.2 Instance-aware core. Stating Charter, Auth and Acc on instances rather than types" (Appendix J, p. 268, not adopted) |
| (iv) Withdrawn claim: an agent as an identified actor distinct from its definition | **Withdrawal confirmed.** Identity belongs to the chartered agent, which Charterion calls an agent type; all its instances share it. Its configuration (model, prompt, tools) is kept apart from it | "An agent type is chartered once and instantiated many times, ephemerally. The core semantics is stated on types" (§8.12, p. 61); "type identity as the agent identifier; instance as a sub-identifier or session" (Table K.1, p. 271) |

Two findings the earlier work did not have:

1. Charterion reports that Microsoft's Cloud Adoption Framework uses the term "agent charter" for "a governance document stating an agent system's responsibilities, roles and prohibited actions" (p. 153). That is the closest wording to WARM's domain charter seen in this search, and the WARM prior-work files do not mention the Cloud Adoption Framework. It is per agent system, as reported by Charterion; I did not read Microsoft's text. It should be read before claim (i) is published.
2. The earlier mapping's statement that Charterion has no agent "with its own memory" is wrong (section 4).

Page numbers below are PDF pages. Printed page = PDF page − 24. Quotations are from text extracted with PyMuPDF, which kept word spaces; I changed nothing in them.

---

## 1. The unread chapters and appendices, item by item

Type key (as in the earlier mapping): `clean` (one WARM v0.12 part fits well), `strained` (one part, with friction), `span` (several parts, named), `guidance` (design-time advice), `out of scope`, `misfit` (no WARM part). WARM part names are those of v0.12: the 25 services, the five layers, the seven domain parts, the agent concepts (agent, definition, instance, persistent agent, task agent), the points of "How the groups relate", and the three kinds of human decision.

### Front matter, PDF pp. 9-25 (normative language, contents, lists of tables and figures)

No constructs. Two facts matter: the v2.0 conditions "WF21–WF26 and CC8, belong to the layered profile, are vacuous when it is not declared and are required at no conformance level" (p. 9), and Table 24.3 lists "Microsoft CAF" among the frameworks compared (p. 19).

### Chapter 1. Purpose, scope and conformance (pp. 26-27)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| Purpose | "an enterprise model in which agents are principals: elements of the architecture on a par with people, applications and technology" | 26 | WARM's agent as an identified actor; WARM is not an enterprise model | guidance |
| Scope exclusions | "Charterion does not cover: the internal design of agents (planning, memory, prompting); model-level safety and alignment; threat modelling ...; the cryptographic mechanics of identity, credentials and attestation; or the interception of tool calls at run time" | 26 | Matches WARM Step 0's exclusion of reasoning. Charterion excludes the services WARM centers on (Memory internals, Secrets, Tools mediation) | out of scope |
| Model, method and tool conformance | "Three things can conform to Charterion." A model conforms if conditions "hold or every failing condition is recorded in the Accepted-Defect Register" | 26-27 | No WARM part. WARM Limit 4 says WARM does not state how to tell that a system conforms | misfit |
| What Charterion is not | "not an identity-and-access-management product, a policy engine or an agent runtime; it produces the target entitlement set such products should enforce and consumes the decision logs they produce" | 27 | Places Charterion above Identity, Policy and Observability as their design-time source | guidance |

### Chapter 3. The paradigm shift (pp. 32-33)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| Five inversions (Table 3.1) | quality, coverage, maintenance, governance, language, from "Human addressee" to "Machine actor" | 32 | Positioning of EA practice | guidance |
| Charterion pipeline | "the model is queried at the moment of acting, returns an admissibility decision with its warrant, the agent acts or escalates, and the evidence of the action returns to the model that authorised it" | 32 | Policy (decide), Approvals (escalate), Observability and Improvement (evidence returns) | span |
| Human position as a construct | "reserved steps, oversight, escalation reachability and accountability chains are facts the semantics reasons over, so that the question 'who answers for this action' has one computable answer at every instant" | 33 | Three kinds of human decision; Identity (accountable person per agent identity) | span |

### Chapter 4. Principles and grounding (pp. 34-37)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| X1 No authority without a charter | "An agent acts only under a charter that binds it to a business scope at a stated level under a stated principal." | 34 | Policy grants, issued per agent and not per role | strained |
| X2 No charter without a principal | "Every charter that confers a write level names a human, or a role with a current holder, who is accountable." | 34 | Identity: "record the person accountable for each agent identity" (v0.12) | clean |
| X3 No entitlement without a need | "Every provisioned entitlement is justified by a step the agent covers" | 34 | Policy and Secrets; WARM has no derivation of entitlements from work | strained |
| X4 No autonomy without oversight | "watched by a reachable human, and no human watches more agents than the organisation has decided a person can" | 34 | Lifecycle and point 4 (stop); Approvals; the open question on approver load (Step 3) | span |
| X5 No mandate beyond charter | "no more authority abroad than it holds at home, and no more after delegation than before" | 34 | Point 2: "A grant passed to another agent can only be narrower"; cross-organization part out of scope | strained |
| X6 No answer without warrant | "returns unwarranted rather than a default wherever its evidence is absent, expired, ambiguous or too weak" | 34 | Policy's "unknown" outcome (v0.12), without per-fact warrant | strained |
| Twelve design principles | e.g. Principle 3 "Delegation attenuates and accountability persists"; Principle 7 "Observed and approved are kept apart ... no agent approves"; Principle 8 "Human reservation is explicit"; Principle 10 "Authority is finite in time ... agents outlive the reorganisations that created them" | 34-35 | P3 point 2; P7 point 3 and the third kind of human decision; P8 the first kind; P10 grants limited in time. The rest are EA method | guidance |
| Theoretical, empirical and design-science grounding | five bodies of work; survey of 150 practitioners; "What the framework has not yet had is a naturalistic evaluation" | 36-37 | Evidence statement | out of scope |

### §8.9-8.10. Action levels against external scales; stratum 5 (p. 59)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| Table 8.2 | maps read, propose, commit, autonomous to Parasuraman's ten levels and CSA L0-L5; "L5 ... not admissible in Charterion" | 59 | Candidate W12 (autonomy vocabulary for domain rules) | guidance |
| Proposition 8.4 | stratum 5 "preserves the v1.0 semantics" | 59 | Formal property of the framework | out of scope |

### Chapter 9.3 (end) to 9.7. The execution plane (pp. 71-73)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| Proposition 9.1 P1-P3 | "(P1, deny dominance) If any approved envelope rule evaluates to deny, the outcome is deny"; "(P2, approved-only authorisation) ... observed or derived envelope content never contributes"; "(P3, monotonicity in warrant) ... can change the outcome only towards unwarranted" | 71 | P1 is one answer to WARM's open question on rule precedence (Step 3). P2 is point 3. P3 has no WARM part | span |
| Substrate Lifecycle | six phases: "Observe ..., Reconcile ..., Commit (human principals approve changes to envelope and ownership assertions; nothing else requires approval), Serve ..., Account ..., and Detect drift" | 71 | Memory and Retrieval (observe, reconcile); third kind of human decision (commit); Policy (serve); Observability (account); Memory currency and Improvement (drift) | span |
| Inv-1 Human approval | "An assertion with ε = approved records an approver in H. An agent cannot approve." | 72 | Point 3; third kind of human decision | clean |
| Inv-2 Separation of observed and approved | "Envelope assertions authorise only when approved. Observed envelope content may be stored ... but the admissibility function does not read it." | 72 | No WARM distinction between observed and approved facts | misfit |
| Inv-3 Non-self-authorisation | "No envelope assertion whose subject is agent g may have g as its source ... and no agent may be the approver of any assertion." | 72 | Point 3: "An agent cannot grant itself authority" | clean |
| Inv-4 Declared boundary (now read in full) | "Every assertion has a finite validity interval, and the admissibility function returns unwarranted rather than a default when a premise is absent, expired, ambiguous or below θact." | 72 | Policy "unknown" (v0.12); WARM puts no validity on facts | strained |
| Inv-5 Accountability | "Every decision is logged with its supporting assertions, and the log is append-only and readable by the auditor." | 72 | Observability | clean |
| Execution-plane levels 0-4 | "Five cumulative levels give the path from a documentation-oriented EA practice to a warrant-bearing substrate" | 72 | Maturity scale; no WARM part | guidance |
| Def. 9.4 Level of an operation; envelope entry | operation level set "by its effect and reversibility assertions"; an envelope entry "permits ⟨g, op, x, ·, t⟩ when current and level(op) ≤ ℓ" | 72-73 | Registry's declared side effects (v0.12) plus Policy | span |
| Def. 9.5 Charter-derived envelope | envelope entries where "Need(g, x, ℓ) holds", with "approver set Acc(g, ·)" and escalation conditions | 73 | Policy grants derived from per-agent authority | strained |

### Chapter 10. The boundary plane (pp. 74-76)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| Mandate (Def. 10.1) | "a portable, signed form of an approved envelope assertion; it is presented to the counterparty with every request" | 74 | Two organizations transacting | out of scope |
| Exposure (Def. 10.2) | "the part of its substrate it declares to foreign agents" | 74 | as above | out of scope |
| Attested status, trust weight, effective confidence (Def. 10.3) | "κeff = κ · tA(B)" | 74 | as above | out of scope |
| Reciprocal commitment (Def. 10.4) | "the debtor organisation is committed to the creditor to bring about the consequent once the antecedent holds" | 74 | as above | out of scope |
| Two-sided admissibility (Def. 10.5), X-Inv-1, X-Inv-2, X-P1 to X-P4 | "An escalate outcome is decided by a human of the side that produced it" | 75 | as above | out of scope |
| Exposure levels X0-X4 | "X0 Closed ... X4 Settling" | 75 | as above | out of scope |
| From charters to mandates | "A mandate for agent g is issued by a human h ∈ Acc(g, ·)" | 76 | as above | out of scope |

### Chapter 11. Cross-plane coherence (pp. 77-82)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| CC1 Grounded envelope | "Every approved envelope entry is justified by a derived need at or above its level" | 77 | Policy: a grant must trace to authority given by people | strained |
| CC2 Complete envelope | "Every derived need is served by a current approved envelope entry at or above its level" | 77 | No WARM check that each role's needed access is in force | misfit |
| CC3 Bounded mandate | "Every mandate is within the needs and caps of the agent's charters" | 77 | cross-organization | out of scope |
| CC4 Level alignment | "no irreversible autonomy on a slice the substrate cannot warrant" | 78 | Point 1 (an action is governed only if it passes an enforcement point), turned into a precondition for granting authority | strained |
| CC5 Accountability continuity | "The approver of every envelope entry and the issuer of every mandate for agent g is a human accountable for g" | 78 | Identity (accountable person) with the third kind of human decision | span |
| CC6 Evidence return | "Every denied, escalated, unwarranted or later-reversed decision in the log is attributable to at least one charter of the requesting agent, and is counted in that charter's evidence record" | 78 | Observability and Improvement | span |
| Theorems 11.1, 11.2; Proposition 11.1 | end-to-end accountability; boundary attenuation; polynomial checking | 78-79 | Formal properties | out of scope |
| Authority certificate (Def. 11.1) and CC7 | "an authority certificate carried by every envelope entry and every decision-log record, checkable by fact lookups"; CC7: every approved entry "shall carry an authority certificate that the checker accepts" | 80 | No WARM counterpart (earlier A53) | misfit |
| Propositions 11.2-11.4, Corollary 11.1, erratum E20 | soundness, completeness (restated), auditability, complexity | 80-82 | Formal properties | out of scope |

### Chapter 12. Overview of the method (pp. 84-85)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| Continuous Method | "a design loop that runs on every change to the model, an operation loop that runs on every action, and a boundary loop that runs on every relationship" | 84 | Releases (design changes), Policy and Observability (operation) | guidance |
| Bridge B1 | "needs → envelope; Acc → approvers" | 84 | Policy and the third kind of human decision | span |
| Bridge B2 | "attributed evidence → refine" | 84 | Improvement | clean |
| Phase template | "purpose; inputs ...; activities; outputs ...; roles ...; automated checks ...; and exit criteria" | 84-85 | | guidance |
| Slice discipline | "a set of capabilities or processes, the resources they touch and the agents chartered on them ... The slice is the unit of adoption, of conformance and of reporting." | 85 | Not a domain: no goals, roles or criteria of its own | guidance |

### Chapter 13. The design loop (pp. 86-89)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| D1 Populate the core | "Obtain the business, application and technology facts the analysis needs"; Requires facts are supplied "typically by the domain authority of each process" | 86 | EA modeling | guidance |
| D2 Charter the agents | "State, as facts, what each agent may do and who answers for it"; "record Delegation for each agent-to-agent hand-off the design intends" | 86 | Identity (accountable person), Policy (authority), a declared hand-off graph WARM lacks (earlier A29) | span |
| D2 exit criterion | "Every agent in the platform inventory has at least one charter or is recorded as decommissioned." | 86 | Lifecycle (list of agents) with Identity | span |
| Agent onboarding procedure | six steps ending "the agent's platform identity is bound to its Agent constant. No agent shall receive an entitlement before step 5." | 87 | Lifecycle (create), Identity, Policy, Approvals | span |
| D3 Analyse | "Compute the least model and evaluate every condition" | 87 | Evaluation applied to the authority structure, which WARM's Evaluation does not cover | strained |
| D4 Refine | "Resolve or accept every defect"; "Agency architect proposes; principals and the Agency Governance Board decide" | 87 | Improvement proposes, people decide, Releases changes | span |
| D5 Provision from the model | "Make the architecture the source of entitlements and of the run-time envelope" | 87 | Identity, Secrets, Policy | span |
| Grant Reconciliation Ledger | compares "the derived Need set as the target entitlement set ... with the provisioned grants" | 87 | No WARM reconciliation of provisioned access against what roles need | misfit |
| Standard resolutions (Tables 13.1, 13.2) | e.g. WF1: "Assign a holder to the vacant role; re-principal the charter ...; retire the agent"; Uncharted(i): "Stop the instance (O6 incident)" | 88-89 | Remediation guidance | guidance |

### Chapter 14. The operation loop (pp. 90-91)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| O1 Observe | "Agents shall re-observe the slice they acted upon after every permitted action" | 90 | Memory currency; Evaluation after an action. No WARM rule to re-check state after acting | strained |
| O2 Reconcile | "conflicting observations from federated sources are resolved by the domain's precedence rule" | 90 | Memory ("keep it current"); Retrieval | span |
| O3 Commit | "The humans named by Acc approve the envelope entries ... Nothing else requires approval." | 90 | Third kind of human decision | clean |
| O4 Serve | "Escalate outcomes are routed to Esc(g, ·); unwarranted outcomes are routed to the domain authority for re-observation or a human answer" | 90 | Policy; Approvals (named decider) | span |
| O5 Account | Decision Log, Commitment Ledger, "Evidence Record of each charter" | 90-91 | Observability; Evaluation | span |
| O6 Detect drift | "Outcomes are compared with what the estate later shows" | 91 | Memory currency; Improvement | span |
| B1, B2 restated | "B2 is the mechanism by which the architecture learns" | 91 | Improvement | clean |

### Chapter 15. The boundary loop (p. 92)

X1 Declare exposure, X2 Issue mandates, X3 Transact, X4 Reconcile trust: all between two organizations. **Out of scope.**

### Chapter 17. Coexistence with the TOGAF ADM (pp. 96-97)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| Design loop mapped to ADM phases | "D2 is a new activity of Phase B (charters and guards are business-architecture content)" | 96 | EA method | out of scope |
| Layer Ownership Table | the Preliminary Phase decides "who holds the owning role of each layer" | 96 | People layer (owners of model content) | strained |
| Tool Catalogue (Phase C) | "every invocable operation surface an agent can call, the resources it exposes and the effect level of each exposure" | 97 | Registry (tool definitions, declared side effects) | strained |
| Scoped Memory Inventory (Phase C) | "every memory an agent retains between actions, the scope it is declared for ..., the resources whose content it stores and the agents that read or write it" | 97 | Memory | strained |
| Runtime Deployment view (Phase D) | nodes, hosted agents, gateways, endpoints, enforcement points, zones, halts | 97 | Infrastructure layer, Environments, Tools, Models, Policy, Lifecycle | span |
| Defect routing by layer | "Every open defect is now attributed to the layer of the condition that reports it ... and routed to that layer's owner" | 97 | Routing of governance defects to people by layer; not hand-off of agent work | guidance |

### Chapter 19. Regulatory and standards alignment (pp. 105-106)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| Table 19.1 | maps the EU AI Act, ISO/IEC 42001, NIST AI RMF, SP 800-207, NCCoE, IMDA and conduct rules to constructs | 105 | Policy rules from the operator | guidance |
| Obligation as data | "Obligation(o, σ, instr, kind) facts recorded by the regulatory owner" | 106 | Domain rules with a legal source (earlier A18) | strained |
| Regulatory Evidence Report | computed "per obligation, with a verdict of whether the model satisfies it" | 106 | Observability and Evaluation over compliance | out of scope |

### Chapter 20. Metrics (pp. 107-108)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| Design-time defect counts; latent write authority | "write authority over steps the business has not designated for agents" | 107 | Evaluation of the authority structure | strained |
| Agency debt and Agency Debt Index | "authority conferred beyond what is justified, coordinated or watched, accumulating silently until it is paid in incidents" | 107 | No WARM metric | misfit |
| Reach, blast radius, charter granularity, oversight span, coherence counts | per agent or human | 107 | Observability (metrics); blast radius was earlier A32 | span |
| Run-time metrics | "counts and shares of permit, deny, escalate and unwarranted outcomes; reversal rate ...; escalation acceptance rate; median time-to-decision" | 107 | Observability; Evaluation | span |
| Three agent KPIs | "admissible-action rate, escalation rate and reversal rate" | 108 | Evaluation | strained |
| Boundary metrics; v1.1 and v1.2 metrics | per relationship; ADdrift, ADunstaffed, ADattention and others | 108 | cross-organization part out of scope; the rest Observability | span |

### Chapter 21, remainder (p. 114)

Table 21.4 lists the four v2.0 viewpoints (Chapter 30), and the MXF document sections ("core", "agency", "extensions", "bridge", "boundary", "parameters" and "metadata"). **Guidance** (artifacts and exchange format).

### Chapter 22. Reference implementation (pp. 116-121)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| Reasoner and validator modules | "charterion.py, the core reasoner ..., which computes the least model"; all "Python standard library" | 116-117 | An implementation (Step 5) | out of scope |
| Repository check pattern | "the validator should run as a check on every proposed change ... failing the change when any unaccepted WF or CC defect appears" | 116 | Releases gated by Evaluation | strained |
| Integration with runtime and identity systems | "Identity management receives the derived Need set ...; the policy decision point or agent runtime receives the charter-derived envelope as policy ... and returns its decision log" | 118 | Identity, Policy, Observability | span |
| EA repositories over MCP | "an import path for D1 ... they are not a substrate" | 118 | | guidance |
| Reference substrate service | "answers the five questions of the Agency Grid at run time"; "a Level 3 substrate"; "It is a reference for what a substrate must do, not a product" | 119-120 | An implementation of Policy as a decision service reached through Tools | strained |
| Tool conformance | "reproducing the reference least model and defect sets exactly" | 120-121 | | out of scope |

### Chapter 23. Five sector cases (pp. 123-150)

The cases add no construct. Facts that bear on the verdicts:

- Each case is a slice of "five capabilities", "each realised by one process", with agents chartered on them (pp. 123, 128-130, 134, 136). Several agents can hold charters on one capability ("A second agent, claim submission, was chartered commit on the same capability", p. 130).
- "domain" appears once as a plain word: "The modelled slice is the payments and KYC/AML domain" (p. 128). It is not a construct.
- Agents are long-lived: "a legacy cron bot that has run nightly rightsizing since before the platform team existed" (p. 136). A charter can be retired while the agent remains: "The legacy cron bot's charter is retired—the agent remains in the Agent Register with no authority" (p. 137), and an instance can keep running: "UC5 iteration 2 shows the Uncharted pattern: the cron bot's charter was retired in the refined model while an instance of it is still running" (p. 142).
- Vacancies: "All five organisations carry at least one charter whose principal is a role vacated by a reorganisation or a departure" (p. 138).
- Evidence kind: "The cases are the author's ... they do not show that a real estate can be described without loss" (p. 123).

Assignment: **out of scope** (demonstration); the facts are used in section 2.

### Chapter 24. Positioning (pp. 152-163)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| The claim | "Charterion adopts every one of these positions and claims none of them as its own" (agent identity class with a sponsor, scoped rights, non-amplifying delegation, autonomy levels, interception) | 152 | Supports the withdrawal of WARM claim (iv) | guidance |
| Five central contributions | "Enterprise architecture as an authority substrate"; "Business-scoped authority formally derived into technical entitlement"; "A formal semantics"; "Design–run-time–boundary coherence"; "Machine-addressed architecture with explicit epistemic warrant" | 152 | none is a WARM part | guidance |
| Microsoft CAF "agent charter" | "denotes a governance document stating an agent system's responsibilities, roles and prohibited actions"; CAF asks for agent "responsibilities that map to business objectives" and "roles that prevent functional overlap" | 153, 155 | A lead for claim (i): see Summary | guidance |
| Tables 24.1-24.3 | gaps G1-G10; 26 construct rows against 21 works | 154-157 | | guidance |
| Restated novelty claim | "(a) the shift from an enterprise model read by people to a machine-consumed authority substrate ... (b) the combination ... (c) the binding ... (d) ... an independently checkable derivation object" | 158 | | guidance |
| Interfaces (Table 24.4) | what Charterion provides to and requires from identity governance, runtime enforcement, BPM, regulation | 159 | Identity, Policy, Observability | span |
| Layer comparison (Table 24.5); vendor reference architectures | admits three gaps: no "semantic element", no "layer whose object is the run-time composition of work", and it "says nothing about interfaces" for human interaction | 160-161 | Confirms Charterion has no Channels and no Orchestration layer | guidance |

### Chapter 25. Maturity model and Conformance Statement (pp. 165-167)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| Design-plane levels D0-D4 | "D0 Unmodelled ... D1 Chartered ... D2 Well formed ... D3 Governed ... D4 Coherent" | 165 | No WARM maturity scale | misfit |
| Maturity stages 0-4 (Table 25.1) | "Documented ... Inventoried ... Analysed ... Governed ... Coherent" | 166 | as above | misfit |
| Roadmap | "shall not confer write-level authority on a slice below execution Level 3 (CC4)" | 165 | Point 1 as a sequencing rule | guidance |
| Conformance Statement | per slice: version, targets and levels, profiles, parameters, Accepted-Defect Register, recommendations not followed, tools, date and agency-debt vector | 166 | No WARM part (Limit 4) | misfit |
| Profile recommendations by level (Table 25.2) | e.g. "staffing D2 every reserved step declared at D2 should have a performer role" | 167 | | guidance |

### Chapter 26. Validation (pp. 169-188)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| Evidence kinds | analytical, experimental, demonstrative, and from v1.2 "demonstrative on third-party models"; "No construct has naturalistic evidence" | 169 | Evidence statement | out of scope |
| Testable propositions AP1-AP23 | e.g. "AP11 (retired on paper, still running) On first import of instance facts ..., Uncharted is non-empty in slices that retired a charter in the preceding quarter" | 171, 175, 184, 187 | AP11 is evidence for a Lifecycle reconciliation check | guidance |
| Limitations 1-23 | e.g. "1. No naturalistic evaluation"; "12. No threat model"; "20 The runtime facts of the cases are author-proposed" | 171-172, 175-176, 184-185, 187 | | out of scope |
| Comparative and field-study protocols | two-arm design; slice selection | 172-173, 176-177 | | out of scope |
| Injection studies, scalability, regression, mechanization, benchmark, third-party models | e.g. "All 450 injections were detected"; Lean 4 proofs of five propositions; three public ArchiMate repositories | 173-186 | | out of scope |
| Agenda items 1-19 | item 19: "A semantic or knowledge element for L4" | 173, 177, 185, 188 | | out of scope |

### Chapter 28. The runtime and knowledge metamodel (pp. 198-208)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| Seven sorts (Def. 28.1) | "tools T, model endpoints Λ, memories K, stores ς ∈ V, nodes N, policy points ΠP and zones Z" | 198 | Tools, Models, Memory, Observability (stores), Infrastructure, Policy, Environments | span |
| Pursues(m, g) | "charter m serves goal g (informative; read by no rule)" | 199 | Domain goals, bound per charter | strained |
| Tool(t), Exposes(t, x, ℓ), Reversible(t), SideEffectScope(t, x) | "an application interface or service an agent can call"; "every change t makes can be undone by a compensating call" | 199 | Registry (tool definitions declare side effects, whether they can be undone) | clean |
| Memory(k), MemoryScope(k, σ), Stores(k, x), Accesses(a, k, ℓ) | "k ∈ K is a memory or context store retained between actions"; "agent a reads (ℓ=read) or writes (ℓ≥commit) memory k" | 199 | Memory, with a read and write scope WARM lacks | strained |
| Store(ς, kind) | "the assertion store, the decision log or a register" | 199 | Observability (decision log); Registry | span |
| Invokes(a, t) | "agent a is bound to call tool t (tool-level provisioning, the analogue of Grant)" | 199 | Tools with Policy | span |
| Node, Hosts, Orchestrates, Gateway, Routes | "n ∈ N is a runtime node; n executes a; orchestrator n dispatches a"; "n mediates tool calls (a tool gateway or MCP server)" | 199 | Infrastructure, Lifecycle (which agents run where), Orchestration, Tools | span |
| ModelEndpoint, Serves, ApprovedFor | "λ is approved for agents holding authority up to level ℓ" | 199 | Models with Policy | span |
| PEP, PDP, Enforces, DecidedBy, SubstrateBacked | "enforcement point π mediates every call of t; π obtains its decisions from decision point π′" | 199 | Policy; point 1 (enforcement point) | clean |
| Zone, InZone, RequiresZone, ClassZone | "z ∈ Z is a containment zone"; "agent a, resp. every agent of class c ..., shall run inside z" | 199 | Environments | clean |
| Halt(h, n) | "human h holds a control that stops every agent hosted on n" | 199 | Lifecycle and point 4 (stop that does not pass through the agent) | clean |
| Telemetry(n, ς) | "node n writes its decision requests and outcomes to store ς" | 199 | Observability | clean |
| Runtime observation list O | "an observed hosts, serves, routes or invokes assertion" | 199 | Observability | clean |
| Decision T-A-2 | "Instances of an agent on a node are covered by Hosts(n, a) read with the instance profile ...; a per-instance placement would double the predicates of L5" | 200 | Bears on (iii) and (iv) | guidance |
| Need trace (Def. 28.2): ToolFor, MissingTool, ToolExcess, NodeReach, NeedTrace | "the derivation charter → step → resource → tool → node → grant as one derived predicate"; "Each break in the chain is a distinct predicate" | 198, 200 | No WARM part traces authority to the tools and nodes that realize it | misfit |
| WF21 Justified tool exposure | "every resource a bound tool exposes to an agent, it exposes at a level the agent needs" | 201 | Tools with Policy (least privilege on tool bindings) | strained |
| WF22 Scoped memory | "(a) no agent accesses a memory holding content of a resource it has no need on; (b) no scoped memory holds content of a resource that no step of any of its declared scopes requires; (c) no two agents write the same memory without a Precedence between them on it" | 203 | (a), (b): Memory with Policy, strained. (c): contention between agents, misfit as earlier A31 | span |
| WF23 Mediated write | "every tool bound to an agent that exposes some resource at level ≥commit is enforced by a policy enforcement point whose decision point is substrate-backed" | 203 | Point 1 | clean |
| WF24 Approved model endpoint | "(a) ... every model endpoint serving an agent that holds authority at autonomous is approved for autonomous. (b) ... approved for at least commit" | 203 | Models with Policy | strained |
| WF25 Reachable halt | "for every autonomous agent that has an overseer, every node hosting it carries a halt held by one of its overseers" | 203 | Lifecycle and point 4; WARM names no person who holds the stop | strained |
| WF26 Contained hosting | "every agent runs inside every zone it is required to run in" | 203 | Environments | clean |
| CC8 Declared deployment | "every hosting, serving, routing and invocation assertion observed at run time is declared in the model" | 204 | Lifecycle (the list of agents that exist) with Observability; WARM has no check of observed against declared | strained |
| Theorem 28.1, Corollary 28.1, Proposition 28.1 | "The layered profile adds findings and defects; it neither grants nor removes authority" | 204-205 | Formal properties | out of scope |
| Mechanization status, behavior on the cases (Tables 28.4-28.6) | "Lean covers the syntax of stratum 7" (see limitation 21) | 205-208 | | out of scope |
| Design decisions T-A-1 to T-A-8 | e.g. "T-A-3 MissingTool is a finding" | 207 | | guidance |

### Chapter 29.3.2 onward. Patterns and anti-patterns (pp. 217-226)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| P2 Supervisor | "A human, or a supervising agent acting for one, watches an autonomous agent and can stop it." | 217 | Lifecycle and point 4; Observability | span |
| P3 Critic | "A second agent reviews what a first agent proposes before a human, or a committing step, acts on it ... The critic adds a judgement only if it is a different principal in the sense of WF11." | 217 | Point 3 (separation of duties, including agents started by one agent) and Evaluation | span |
| P4 Human gate | "the Reserved step that no agent may write (WF8); the Escalation route ... and the Authority Request Protocol" | 217 | Three kinds of human decision | clean |
| P5 Sandboxed tool use | "An agent calls tools through a gateway inside a containment zone; every write-level call passes an enforcement point whose decisions come from the substrate." | 219 | Environments, Tools, Policy (point 1) | span |
| P6 Kill-switch | "The overseer of an autonomous agent holds a control that stops every instance of it, wherever it runs, and the stop is a logged decision." | 219 | Lifecycle, point 4, Observability | span |
| P7 Compensable write | "the architecture provides a compensating step and the tool that performs it" | 220 | The open question on undoing (Step 3); Registry side-effect declaration | strained |
| P8 Memory-scoped assistant | "An assistant agent keeps state between actions—conversation memory, retrieved context, a vector store—and other agents may read it." | 220 | Memory; bears on (iii) | strained |
| P9 Approved-model routing | "The model endpoint that drives an agent is approved for the level of authority the agent holds." | 221 | Models with Policy | strained |
| P10 Boundary mandate exchange | "An agent of organisation A acts on organisation B's exposed slice under a mandate" | 221 | cross-organization | out of scope |
| Pattern matrix (Table 29.2), Proposition 29.2 | "Each of WF21–WF26 and CC8 is satisfied or made checkable by at least one pattern" | 222-223 | | guidance |
| Anti-pattern: agent as service account | "The agent runs under a technical identity whose entitlements were copied from a template or a team's group" | 224 | Identity (each agent its own identity) | strained |
| Anti-pattern: ungated MCP server | "the approved envelope exists in the substrate and nothing on the call path consults it" | 224 | Point 1 | clean |
| Anti-pattern: shared unscoped memory | "Several agents read and write one memory or vector store with no declared scope" | 224 | Memory | strained |
| Anti-pattern: orchestrator without charter | "A planner dispatches executors with its own privileged identity; the executors' authority is the orchestrator's and no delegation is declared" | 224 | Candidate W9 (whose identity a task agent acts under); point 2 | strained |
| Anti-pattern: halt on paper | "the agent runs on nodes and instances on which the overseer holds no control" | 224 | Point 4 | strained |
| Patterns in the cases (Table 29.4) | qualitative reading | 225-226 | | guidance |

### Chapter 30. Layered viewpoints (pp. 227-233)

| Item | Definition (verbatim) | Page | Assignment | Type |
|---|---|---|---|---|
| Layered Agentic Viewpoint | "how one agent is realised across the six layers"; "The agent is drawn as an active-structure element realised across L2 and L5" | 227-228 | | guidance |
| Authority Flow Viewpoint | "by what chain this agent may change this resource" | 228-229 | | guidance |
| Blast-Radius / Containment Viewpoint | "how far a compromise of this agent propagates, and whether the zone contains it" | 228-229 | | guidance |
| Runtime Deployment Viewpoint | "on what this agent runs, through what it acts, which model drives it, who can stop it" | 228, 231 | | guidance |
| Generation rule | "The four viewpoints are generated, never authored"; the reference toolkit "does not generate diagrams in v2.0" | 233 | | guidance |

### Chapter 31. Migration from 1.x to 2.0 (pp. 234-235)

Terminology change ("layers" of the substrate become "facets"), model and Conformance Statement migration, and a reading-order note. **Out of scope.**

### Appendices A to S, except L (pp. 236-284; bibliography pp. 285-290)

| Appendix | Content and the items it defines | Pages | Assignment | Type |
|---|---|---|---|---|
| A Consolidated formal definitions | index of sorts, predicates, strata, conditions, invariants and propositions; no new item | 236-237 | | out of scope |
| B Glossary (now read in full) | adds, among others: "Charter A statement that an agent may act within a business scope up to a level under an accountable principal"; "Slice The unit of adoption and conformance"; "Instance A running process acting under an agent type's identity, holding no charter of its own"; "Memory What an agent retains between actions"; "Halt A control by which a named human can stop what runs on a node". No entry for domain, team, role (other than performer role), acceptance or work product | 238-243 | as the chapters that define them | (see chapters) |
| C Notation | symbols; "i, Inst(a), SpanI(h) instance; instance count of a type" | 244-245 | | out of scope |
| D Requirements traceability | DR1-DR6, SR1-SR12, XR1-XR6, e.g. "SR7 Instance-level currency"; "SR10 Federation with central commitment ... O2 per-domain precedence" | 246-247 | | guidance |
| E ArchiMate 3.2 profile | Agent: "Software actor that performs steps; never a Business Actor, because accountability stays with humans"; "Performs(r, s) Assignment Business Role → Business Process/Function"; "Instance(i, a) Node / System Software ... realises the Agent component"; v2.0 stereotypes for RuntimeNode, Tool, ToolGateway, ModelEndpoint, Memory, Store, PEP, PDP, Zone, Halt | 248-255 | Decides verdict (i): roles are filled by people only | guidance |
| F Mapping to the TOGAF ADM | Tables F.1, F.3, F.4; "instance (O1, G8) ... retirement — Agent Catalogue instances" | 256-259 | EA method | out of scope |
| G Model Exchange Format | MXF 1.0-2.0 sections and skeletons | 260-264 | | out of scope |
| H Version policy | minor versions may not change semantics; v2.0 is "a major version ... by the letter of the policy" | 265 | | out of scope |
| I Comparative replication protocol | coding marks, evidence rule, tie-breaks, inter-rater procedure | 266-267 | Method for comparing models | guidance |
| J Candidates for a major version | Z.1-Z.10, including "Z.2 Instance-aware core. Stating Charter, Auth and Acc on instances rather than types" and "Z.10 Semantic or knowledge element for L4"; "Version 2.0 ... adopted none of Z.1–Z.9" | 268-269 | Decides verdicts (iii) and (iv) | guidance |
| K Protocol bindings | Table K.1 (bindings to the Agent Control Standard, IETF AIMS, OAuth token exchange, AuthZEN, XACML); Table K.2 (six MCP tools of the substrate service); "subagent-start becomes Instance and, where declared, Delegation facts" | 270-272 | Identity, Policy, Approvals, Observability bindings | span |
| M Regulatory Evidence Report | per-obligation computed evidence and verdict | 274 | | out of scope |
| N Adversarial assumptions | "(A1) the adversary controls one or more agents entirely ... but not the repository, the reasoner, the identity system or the substrate's commit path" | 275 | Security concern (WARM: not a group) | guidance |
| O Reference trust estimator | Beta estimator of tA(B) | 276 | cross-organization | out of scope |
| P Open Group submission path | outline; "Nothing has been submitted" | 277-278 | | out of scope |
| Q, R, S Change logs | errata E1-E21; v2.0 additions | 279-284 | | out of scope |
| Bibliography | references only | 285-290 | | out of scope |

---

## 2. The four verdicts

### (i) A domain as a charter that several agents and people fill: unchanged

What the unread text states:

- **No domain.** "domain" occurs 27 times in the extracted text (case-insensitive substring, all 290 pages, including "per-domain", "finite domain" and "domain architectures"). It is never defined, and the glossary (pp. 238-243, now read in full) has no entry for it. Its uses name an area whose structure a "domain authority" answers for: "unwarranted outcomes are routed to the domain authority for re-observation or a human answer" (p. 90); "typically by the domain authority of each process" (p. 86). Once it is a plain word: "the payments and KYC/AML domain" (p. 128).
- **No organizational unit.** "organisation unit" occurs three times, all describing TOGAF: "the TOGAF metamodel's Actor and Role describe people and organisation units" (p. 160). Departments and directorates appear only in case narratives.
- **No team of agents.** "team" always means people: "architecture team", "platform team", "a dissolved team" (p. 64), "a digital-channels team" (p. 128). The nearest construct is the orchestrator with its executors, which is a control relation and a delegation between named agents (P1 and the anti-pattern "Orchestrator without charter", p. 224).
- **No acceptance criteria for work products.** "acceptance criteri" and "work product" occur 0 times. Thresholds judge charters: the Evidence Record and promotion thresholds (pp. 91, 107).
- **Agents do not fill roles.** Roles are human: "Performs(r, s) Assignment Business Role → Business Process/Function" (p. 251). The agent is "Software actor that performs steps; never a Business Actor, because accountability stays with humans" (p. 248). This settles the question more firmly than the earlier reading ("Agents do not fill roles; they hold charters").
- **The charter stays per agent.** "Charter A statement that an agent may act within a business scope up to a level under an accountable principal" (glossary, p. 238).

Inference: Charterion separates an area of work (capability, process, step) from its agents, and several agents and staffed human roles act in one area. It still has no entity with goals, roles that agents fill, workflow, knowledge, tools, rules and acceptance criteria. Verdict (i) "stands as worded, weakened" is unchanged.

One lead from outside Charterion: it reports that Microsoft's Cloud Adoption Framework uses "agent charter" for "a governance document stating an agent system's responsibilities, roles and prohibited actions" (p. 153). The WARM prior-work files do not cover it. Read it before publishing claim (i).

### (ii) A directory of which area of work is accountable for which responsibility: unchanged

What the unread text states:

- The substrate service that agents call at run time has six tools: "admissible" (agent, action, resource), "authority_of" (agent), "envelope_of" (agent), "why" (decision id), "request_authority" and "model_snapshot" (Table K.2, p. 272). None takes a step, a responsibility or a request and returns an accountable area or agent. Every question is about one named agent's own authority.
- Hand-offs between agents are declared at design time as delegations of authority between named agents: "record Delegation for each agent-to-agent hand-off the design intends" (p. 86); "delegations only where the agent hands work to existing agents" (p. 87); the perimeter is "what an orchestrator may dispatch within" (earlier A29). These are permission graphs, not a lookup of where work belongs.
- Routing that exists is routing of exceptions to people: escalations to "Esc(g, ·)", unwarranted outcomes "to the domain authority" (p. 90), defects "to that layer's owner" (p. 97). For human decisions after an authority request: "the routing of the human decision is the organisation's workflow system's" (p. 94).
- The v2.0 registers and catalogs (Tool Catalogue, Scoped Memory Inventory, Runtime Deployment view, Layer Ownership Table; pp. 96-97) record tools, memories, hosting and owners of model content. None records which area answers for which responsibility.

Inference: as the earlier mapping said, one could compute a step-to-agent map (Covers) and an agent-to-human map (Acc) from the registers. The text never presents either as a lookup for handing work over, and the domain authority routing (p. 90) has no register behind it: no predicate maps a domain to its authority. Verdict (ii) "weakened; survives only with 'accountable' doing the work, and AEON is the nearest case" is unchanged. Charterion's routing of unwarranted outcomes to "the domain authority" could be cited as a further near case: an area of work with an accountable person, used to route one class of question, with no register.

### (iii) Persistent agents and task agents: unchanged in verdict, reasoning to be corrected

What the full text states:

- **Charterion's agents are long-lived.** "agents outlive the reorganisations that created them" (Principle 10, p. 35); a cron bot "has run nightly rightsizing since before the platform team existed" (p. 136).
- **They can keep memory between actions, per agent.** "Memory(k) k ∈ K is a memory or context store retained between actions" and "Accesses(a, k, ℓ) agent a reads ... or writes ... memory k" (Table 28.1, p. 199); "An assistant agent keeps state between actions—conversation memory, retrieved context, a vector store" (P8, p. 220); glossary "Memory What an agent retains between actions" (p. 242). The same statement is on p. 193, which the earlier mapper read: "Agents retain state between actions—conversation memory, retrieved context, vector stores, caches, scratch files".
- **They have a lifecycle and retirement.** The Agent Register records "lifecycle state" (p. 99, earlier read); "Every agent in the platform inventory has at least one charter or is recorded as decommissioned" (p. 86); a charter can be retired while "the agent remains in the Agent Register with no authority" (p. 137); "an instance of a retired type" is a defect (p. 173).
- **No sessions, no channel.** "session" occurs only in protocol names ("steps/sessionStart") and once in "instance as a sub-identifier or session" (p. 271). Charterion "says nothing about interfaces" through which people interact with agents (p. 161).
- **What is started per task is an instance, not an agent.** "subagent-start becomes Instance and, where declared, Delegation facts" (p. 270); "An instance i of agent a is a running process that acts under the identity of a and holds no charter of its own" (p. 61); instance-level identity was considered and set aside (Z.2, p. 268).
- "persistent", "long-lived", "long-running" and "lifetime" occur 0 times; "ephemeral" once (§8.12).

Inference: Charterion has one kind of identified agent, long-lived and optionally with memory, and anonymous instances of it, which include subagents. It does not distinguish two kinds of agent by lifetime, and nothing in it is an identified agent created for one task. So the claim stands, narrowed as before. The supporting sentence must change: Charterion's agents are not without memory. The difference that remains is that WARM's task agent is an identified agent of its own, and WARM's persistent agent has a session history and a channel, which Charterion lacks.

### (iv) An agent as an identified actor distinct from its definition: withdrawal confirmed

What the full text states:

- Identity sits with the chartered agent and is shared by its instances: "An agent type is chartered once and instantiated many times, ephemerally. The core semantics is stated on types" (§8.12, p. 61); Def. 8.9 (above); "Hosts(n, a) says that n executes a or any instance of it" (T-A-2, p. 200); in bindings, "type identity as the agent identifier; instance as a sub-identifier or session" (Table K.1, p. 271); "Instance(i, a) Node / System Software ... realises the Agent component" (p. 251).
- Instance-level identity is a rejected candidate: "Z.2 Instance-aware core. Stating Charter, Auth and Acc on instances rather than types. Impact: every rule of Figure 7.2 is restated" (p. 268), and "Version 2.0 ... adopted none of Z.1–Z.9" (p. 268).
- The definition is kept apart from the identity: Def. 8.8's configuration digest ("model identity and version, system prompt, tool set, runtime version", earlier read) can drift while the agent and charter stay, and v2.0 adds the model endpoint as a separate element: "the endpoint that serves it is an element of the runtime that several agents share" (WF24 rationale, p. 203).
- Charterion disclaims the idea as its own: "Charterion adopts every one of these positions and claims none of them as its own" (p. 152).

So the identity belongs to each chartered agent, which Charterion calls a type because it can run as many concurrent instances. It is not a class of agents: Charterion has a separate class above the agent, "AgentClass(a, c)" (WF19, p. 64; "every agent of class c", p. 199). Inference: Charterion's agent corresponds to WARM's agent, its configuration digest to WARM's agent definition, and its instance to WARM's instance. The real difference is narrower than "type versus each agent": Charterion lets many concurrent instances, including started subagents, share one identity, and WARM gives each task agent its own (see section 4).

---

## 3. Parts of Charterion that WARM v0.12 has no place for and the earlier mapping did not list

| # | Charterion part | Definition and page | What it suggests WARM change | Confidence |
|---|---|---|---|---|
| N1 | Declared against observed deployment (CC8), with the "Uncharted" instance (WF14, AP11) | "every hosting, serving, routing and invocation assertion observed at run time is declared in the model" (p. 204); "AP11 (retired on paper, still running)" (p. 175) | Give Lifecycle a stated check: compare the agents observed running with the list of agents that exist, and report an agent running that is not listed or whose authority was retired. This is a concrete test for Lifecycle's "orphan" failure case | Medium |
| N2 | Agent onboarding procedure and the D2 exit criterion | "Every agent in the platform inventory has at least one charter or is recorded as decommissioned"; "No agent shall receive an entitlement before step 5" (pp. 86-87) | State in Lifecycle and Identity that an agent is created only with an accountable person and a recorded role, and that no credential is released before that | Medium |
| N3 | Memory as an authority channel (WF22) | "Memory is where authority leaks silently: an agent that may not read the ledger reads a colleague's summary of it" (p. 203) | Add to Memory or Policy: memory entries are scoped, an agent reads only memory whose content its roles may see, and two writers to one memory need a declared order. The earlier mapping listed a "scope check" (A37) but not leakage between agents or contention | Medium |
| N4 | Reconciliation of provisioned access with what work needs (Grant Reconciliation Ledger, CC2, WF21) | "the Grant Reconciliation Ledger shows no unaccepted difference between needs and grants" (p. 87); "every resource a bound tool exposes to an agent, it exposes at a level the agent needs" (p. 201) | Add to Policy, or to Secrets and Tools: a periodic comparison of the credentials and tool bindings an agent holds with what its roles need, in both directions | Medium |
| N5 | Conformance Statement and maturity levels | the per-slice statement "is the document an auditor, a regulator or a counterparty reads first" (p. 166); D0-D4 and stages 0-4 (pp. 165-166) | A model for WARM's missing "how to tell that a system conforms" (Limit 4): a statement per system listing which parts are implemented, the known exceptions, and the evidence | Low-medium |
| N6 | Authority granted only where enforcement exists (CC4, roadmap) | "shall not confer write-level authority on a slice below execution Level 3" (p. 165) | Extend point 1: a grant to change state should not be issued for an action that no enforcement point checks | Low-medium |
| N7 | Re-observation after acting (O1, SR7) | "Agents shall re-observe the slice they acted upon after every permitted action" (p. 90) | Tasks or Evaluation could confirm that an action had the intended effect before the task counts it done | Low |
| N8 | Agency debt index | "authority conferred beyond what is justified, coordinated or watched, accumulating silently until it is paid in incidents" (p. 107) | A summary measure for Observability over the gaps WARM's own checks find | Low |

Two items support candidates the earlier mapping already made: the anti-pattern "Orchestrator without charter" (p. 224) supports W9 (whose identity a task agent acts under) and W4 (attenuation); the critic pattern's "The critic adds a judgement only if it is a different principal in the sense of WF11" (p. 217) supports point 3's rule on agents started by the same agent.

---

## 4. Statements in the earlier mapping that the full text shows wrong or incomplete

1. **Wrong: "Charterion has no agent that persists across tasks with its own memory and channel" (A.3 (c)).** The memory half is wrong: memory "retained between actions" is a v2.0 element accessed per agent (p. 199; also p. 193, which the mapper read). Only the channel and session parts hold. The same sentence feeds verdict (iii) and should be corrected there.
2. **Incomplete: WARM v0.12's sentence "Charterion gives it to a type of agent, and WARM to each agent" ("What WARM adds", item 4).** Charterion's "agent type" is an individual named agent (for example "A6_Settlement"), with a separate AgentClass above it (pp. 64, 199). The accurate difference: Charterion's concurrent instances and started subagents share their agent's identity; WARM gives each task agent its own.
3. **Incomplete: the list of pages read and not read.** The unread list omitted Chapter 1 (pp. 26-27), Chapters 3-4 (pp. 32-37), §8.9-8.10 (p. 59) and most of the front matter. The glossary was read only for named entries.
4. **Refined: A106 and A107 (WF21, WF22, "Fig. 5.2 label only").** Now defined (section 1, Chapter 28). WF22 has a third clause, memory contention between agents, which is a misfit like A31.
5. **Refined: A112 (CC1-CC8 as one span) and A113 (Inv-4 partly read).** CC3 is out of scope, CC5 maps to Identity's accountable person, CC6 to Improvement, CC7 is a misfit, CC8 to Lifecycle and Observability. Inv-4 now maps to Policy's "unknown" outcome, which v0.12 added.
6. **Count: "'Domain' appears 23 times and is never defined."** With PyMuPDF extraction I count 27 substring hits; the earlier pypdf extraction dropped word spaces, which can change counts. "Never defined" holds.
7. **Reverse table, written against v0.11.** It has no Lifecycle row, which v0.12 added. Charterion covers Lifecycle at least partly: the Agent Register's "lifecycle state", agents "recorded as decommissioned", instance cardinality, retirement and halts (pp. 86, 137, 173, 199). Improvement is better matched than "P: evidence-gated promotion": bridge B2 "is the mechanism by which the architecture learns" (p. 91).
8. **Confirmed, no change:** "Agents do not fill roles" (now stated outright, p. 248); "Acceptance criteria: none for work products" (0 hits); Channels absent (p. 161); several agents on one scope (p. 130); no naturalistic evidence (p. 169).

---

## 5. Pages read, and what I could not read

Source: `Charterion_v2.0_Specification.pdf`, Zenodo record 22829848, 290 pages, text extracted page by page with PyMuPDF 2.1 (word spaces preserved).

| Range (PDF pages) | Content | How read |
|---|---|---|
| 9-24 | Normative language, contents, lists of tables and figures | In full |
| 25-27 | Part I title; Chapter 1 | In full |
| 32-37 | Chapters 3-4 | In full |
| 59 | §8.9-8.10 | In full |
| 71-92 | §9.3 (end) to Chapter 15, including Part III title | In full |
| 96-98 | Chapter 17; Part IV title | In full |
| 105-109 | Chapters 19-20; Part V title | In full |
| 114-189 | End of Chapter 21 to Chapter 26; Parts VI-XI titles | In full |
| 198-208 | Chapter 28 | In full |
| 217-235 | §29.3.2 to Chapter 31 | In full |
| 236-284 | Appendices A-K, M-S | In full |
| 285-290 | Bibliography | Read as a list of references; checked for works relevant to WARM (Microsoft 2025, AWS, Salesforce) |

To check quotations I also searched the full text and re-read single passages on pp. 28, 35, 61, 64, 86-87, 94, 99, 193 and 199.

Not read as images: every figure was read only as the text the PDF carries (labels, arrows written as text), not viewed as a picture. Not read: the Microsoft Cloud Adoption Framework page that Charterion cites, and the toolkit, benchmark and Lean files the specification refers to, which are not in the PDF.

Absence searches in section 2 are case-insensitive substring counts over all 290 extracted pages. Before relying on a zero I confirmed the instrument finds known terms ("domain" 27, "retire" 19, "decommission" 5, "session" 9).
