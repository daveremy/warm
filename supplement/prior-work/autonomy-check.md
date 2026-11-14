---
title: "Autonomy in fourteen published reference models for agent systems"
date: 2026-11-11
author: research subagent (read-only, one output file)
question: "How does each of the fourteen models treat autonomy: agents carrying work to completion without a person approving each action?"
status: one reader, no second rater
---

# Autonomy in fourteen published reference models

## How this was done

The fourteen models are the ones listed in `synthesis.md` (round 1: six) and `synthesis-round2.md` (round 2: eight).

For each model I first grepped the mapping files for autonomy language, then grepped the source text itself. The source texts are the copies the mappers downloaded, under `~/.cache/sagan/de94046e-scratchpad/`. Below, `S/` stands for that folder. Line numbers are from those text files.

Search terms used on every source (case-insensitive): `autonom`, `human-in`, `in the loop`, `oversight`, `approv`, `pre-author`, `threshold`, `escalat`, `irreversib`, `delegat`, `long-running`, `long-lived`, `persistent`. Extra terms per source are named in that source's section.

Quoting conventions:
- Charterion's PDF text lost most word spaces ("autonomousauthority"). I restored the spaces and changed nothing else.
- AAM/5C, CEAD, AOS and EAAF break words across lines with a hyphen ("esca -lated"). I rejoined those words.
- Every quote below was re-checked against the source text file named with it, unless section D says otherwise.

Sources and files:

| # | Model | Identifier | Text read |
|---|---|---|---|
| 1 | Yu, Rabhi, Zhu, Lu | arXiv:2610.14818v1 | `S/dl/2610.14818.txt` (HTML text), `S/dl/2610.14818.pdf.txt` |
| 2 | Zhu, "Fluid Structure, Rigid Record" | arXiv:2608.08516v1 | `S/dl/2608.08516.txt` |
| 3 | Goujon, AAM/5C | arXiv:2610.30221, V7.83-EN | `S/aam/aam.txt` |
| 4 | Microsoft Multi-Agent Reference Architecture | github.com/microsoft/multi-agent-reference-architecture, commit `adbefc18` | `S/ms/repo/docs/**/*.md` |
| 5 | AWS Prescriptive Guidance on agentic AI (six guides) | docs.aws.amazon.com/prescriptive-guidance/latest/... | `S/aws/<guide>/*.clean` |
| 6 | Google Cloud Architecture Center, agentic AI pages | cloud.google.com/architecture/... | `S/google/body-*.txt` (17 pages) |
| 7 | El Hassani, Charterion v2.0 | Zenodo 10.5281/zenodo.22829848 | `S/charterion/c.txt` (all 290 pages, searched) |
| 8 | Longmire and Longmire, AEON | Zenodo record 20349596 | `S/dl/aeon.txt` |
| 9 | deVadoss, CEAD | arXiv:2605.08258v1 | `S/cead/c.txt` |
| 10 | Salesforce, "The Agentic Enterprise - The IT Architecture" | architect.salesforce.com/docs/architect/fundamentals/guide/agentic-enterprise-it-architecture.html | `S/sf/body.txt` |
| 11 | Sharma and Shah, AOS-0001 and AOS-0000 | arXiv:2608.03214, arXiv:2606.01508 | `S/dl/aos.txt`, `S/dl/aos0.txt` |
| 12 | Steinder and Franke, "Towards an Agent Operating System" | arXiv:2607.25076 | `S/dl/ibm.txt` |
| 13 | Beheshti et al., ASOC manifesto | arXiv:2607.12619 | `S/dl/asoc.txt` |
| 14 | Venkiteela, EAAF | doi:10.64539/sjcs.v2i1.2026.368 | `S/dl/eaaf.txt` |

---

## Per model

### 1. Yu, Rabhi, Zhu, Lu (arXiv:2610.14818)

**1. Position on autonomy.** Not found. The word stem `autonom` occurs 0 times in `S/dl/2610.14818.txt`, `S/dl/2610.14818.pdf.txt` and `S/dl/2610.14818.body`. The paper treats human approval as a conditional capability, not as a position on autonomy: "capabilities such as multi-agent collaboration, persistent memory, asynchronous execution, human approval, or execution isolation may apply only under particular workload, integration, or governance conditions" (line 142).

**2. Levels.** Not found (searched `autonom`, `level`, `degree`). It has a table of conditions and the capability each one enables (Table II), not levels.

**3. What lets an agent act with no person approving.** A policy gate at the action layer, L6, that decides each action: "Pre-action verification of consequential effects sits in L6, whose action-policy or approval gate permits, refuses, or escalates an action" (line 248). Table II, condition to realization: "Protected or consequential external effect | Enable an L6 action-policy or approval gate | Policy service or human approval" (lines 466-470). Scoped delegated authority: "Delegated or deferred execution | Scope and expire propagated authority (T2); L6 re-authorizes at execution time" (lines 486 onward). In the worked example a compliant action proceeds with no person: "On submission, L6 re-runs the mandate check and clears a compliant trade. For a breach with a requested override, it holds the trade until a principal who holds the override entitlement and is not the submitter approves it" (line 612).

**4. What a person does, and when.** People set the rules at design time: "The use case, the mandate limits, and the rule that a second person approves overrides are L0 decisions that set the requirements" (line 610). L0 "establishes ownership, accountability, risk, and regulatory requirements that constrain decisions elsewhere, rather than acting as a runtime step" (line 230). At run time a person approves exceptions only (the override above). Separately, when "Human participation required", L3 provides "Clarification, review, pause/resume" (Table II, lines 450-458).

**5. Long-lived agents.** Not addressed as agent lifetime. It addresses long-running execution and persistent memory, not persistent agents: "Long-running or background execution | Mediate relevant interactions through L7" (line 546); "Persistent cross-execution context required | Enable L5 persistent memory and governed retrieval" (lines 510-514). Searched `long-lived`, `persistent agent`, `resident`: no hit about an agent's lifetime.

### 2. Zhu, "Fluid Structure, Rigid Record" (arXiv:2608.08516)

**1. Position.** Unattended autonomy is a risk that the design limits on purpose. Section heading: "Human control limits unattended autonomy." (line 1117). "The present target is a human-supervised organization. Offline policy deliberately queues or halts higher-risk decisions. This sacrifices 24-hour decision throughput to preserve a human correction endpoint; fully autonomous constitutional amendment is out of scope." (line 1119). "The normal state is closed, so failure tends toward safety rather than residual autonomy." (line 315).

**2. Levels.** Not autonomy levels as such. It defines four risk-based decision classes that set who must authorize a change. "Table 5: Risk-based decision classes. Thresholds are organization-specific and must be calibrated." Rows (lines 955-1036): "Standard | repeated, low blast radius, reversible | operator under pre-approved policy | automatic rollback; sampled later"; "Normal | material but reversible | scoped Reviewer decision | logged evidence and rollback plan"; "Major | high blast radius or difficult to reverse | Reviewer plus independent second key or human | checkpoint, explicit evidence, human-visible decision"; "Emergency | containment or recovery after incident | break-glass identity within predefined bounds | immediate record plus mandatory post-incident review".

**3. What lets an agent act with no person approving.** Pre-approved policy for a class of work: "During human-offline periods, only pre-approved, reversible Standard work proceeds automatically; higher-risk decisions queue or HALT." (line 632). Scoped, expiring grants: "A task activates a scoped lease; completion, timeout, budget break, or HALT revokes it." (line 315). Pre-authorized templates: "A resident operator may instantiate workers under a pre-authorized template, yet every child receives attenuated grants and remains low/low." (line 742). Review by another agent in place of a person: the Reviewer role "can approve or reject work, promote candidate payloads, authorize durable Knowledge, change a workflow, issue a new lease, roll back a reversible transition" and "Major or irreversible change requires a second key from a distinct Reviewer, a deterministic control, or the human." (line 746).

**4. What a person does, and when.** "The human remains the correction endpoint, organization-kill holder, and one key for Major or Emergency changes." (line 632). "Organization kill: human-only, one action, always available—stop new leases and revoke every active lease." (line 1037). So a person is one possible key for Major changes and holds the stop; Standard work runs without a person; Normal work needs a Reviewer, not a person.

**5. Long-lived agents.** Addressed, and rejected. "There is no digital employee permanently nailed to a position. ... When work ends, the team dissolves and the grants disappear." (line 163). "A resident entry is a reusable specification, not a permanently busy digital employee. ... It waits dormant in the pool." (line 397). "Because agents are dormant by default, shutdown does not need to persuade or locate a permanently autonomous workforce" (line 1037).

### 3. Goujon, AAM/5C (arXiv:2610.30221)

**1. Position.** A goal, with conditions. "Level 4 — Governed autonomous IS (AAM/5C objective)" (`S/aam/aam.txt` line 814). "The guiding principle is that intelligence proposes but never acts without validation: every act executed autonomously must be explicitly authorized, continuously audited and reversible" (lines 40-42). "The model does not claim that this level is attainable for all scenarios" (lines 816-818).

**2. Levels.** Yes, five (§1.5, §5.3). "Level 0 — Passive IS: no action is triggered by the system; Level 1 — Assisted IS: scripts execute recurring tasks that the human triggers; the system decides nothing; Level 2 — Supervised IS: the system detects and recommends acts from an explicit, bounded catalog; the human decides on their execution; every recommendation is logged; Level 3 — Conditional IS: the system executes low- or moderate-criticality acts without continuous supervision and escalates outside its domain; the AOM is sized to absorb the flow of escalations; Level 4 — Governed autonomous IS: the system also executes high-criticality acts within a bounded domain; every agentic act in the scope follows R-AUT (§2.2.3) and respects the reversibility invariant (§4.4)." (lines 1950-1961).

**3. What lets an agent act with no person approving.** Each act is validated by a separate layer (L6 decides, L5 issues a token, an enforcement point checks it), not by a person. A pre-authorized envelope covers classes of acts: "Pre-authorized capability envelope. ... It is an authorization decided by L6 and issued in advance by L5, which delimits a bounded right to act. It has five properties: A restricted, explicit scope (classes of acts, resources, quotas); A short expiry; Local verification by the PEP, which compares the act to the scope of the envelope as it would to that of a token, without calling the control plane; Revocation by event; A posteriori audit, as for an act token; lacking a human identity of its own, a covered act is attributed to the co-signatories of the policy that underlies the envelope (§8.3)." (lines 2495-2509). Bound: "The envelope covers only classes of acts of low or moderate criticality, qualified as such by the signed policy. Acts of high criticality ... remain under synchronous authorization, and irreversible acts, whatever their criticality, require human validation (§4.4)" (lines 2519-2522). Risk thresholds (stated as future work for banks): "autonomous execution for reversible, low-stakes acts, after-the-fact supervision for intermediate cases, human validation before execution above a threshold, and exclusion of certain acts from the scope of autonomy (J.C2, Figure F.18)" (lines 3511-3514). A self-declared attribute can only tighten: "A self-declared attribute may only add a restriction — lowering a ceiling, requiring human validation — never lift one" (lines 2299-2300).

**4. What a person does, and when.** Sets rules, decides irreversible acts, holds the stop. "for routine acts, the human supervises without executing (human-on-the-loop). The human remains in the loop where the rules are set and where the acts that commit the organization are decided: the human writes and co-signs the policies (§8.3), every act token carries the identity of a responsible human (§7.2), every irreversible act is submitted to the human (§4.4), and the human holds the emergency stop (§8.2)." (lines 3598-3603). "An act for which the invariant cannot be upheld — an irreversible act in particular — is not executed autonomously: it is escalated to the AOM, whatever its criticality." (lines 1749-1751).

**5. Long-lived agents.** Agents run continuously; no task-agent kind. "Each agent continuously runs a Distributed Autonomy Loop (DAL)." (line 1719). What is short-lived is the authority (act tokens, envelopes with "A short expiry"), not the agent. The mapper's searches for "subagent", "spawn" and "worker" found nothing (`mapping-aam5c.md` line 421; not re-run by me).

### 4. Microsoft Multi-Agent Reference Architecture

**1. Position.** A risk. "Output accountability: As agents act autonomously or semi-autonomously, ensuring traceability and responsibility for generated outputs is essential." and "Without strong governance in place, organizations risk uncontrolled automation, data exposure, hallucinated outputs, and non-compliance with regulations." (`S/ms/repo/docs/governance/Governance.md` lines 22-32). "Unlike static models, agentic systems may modify their own behavior through reflection, planning or tool selection. This introduces the possibility of agents evolving independently of their original design." (`versioning/Behaviors.md` lines 35-39).

**2. Levels.** Not for action autonomy. It has a versioning maturity model whose top level is "Autonomous Governance | Agents participate in their own lifecycle management (e.g., self-versioning proposals). | Requires robust oversight to prevent unintended evolution. | Implement policy engines, human-in-the-loop controls, and risk-aware routing." (`versioning/Maturity.md` line 16). That scale is about managing agent versions, not about which actions run without a person.

**3. What lets an agent act with no person approving.** Policy decided in advance at the tool layer: "MCP server abstracts tool APIs from agents. Policies control access, parameters, and invocation flow." and in the sequence diagram "Policy-->>MCP: Access granted with constraints" (`reference-architecture/Patterns.md` lines 202-216). "Only approved capabilities can be executed in runtime." (`security/Security.md` line 27). "Operational boundaries: It's critical to define the scope of what agents are allowed to do, particularly in dynamic orchestration settings." (`governance/Governance.md` line 25). For releases, metrics in place of people: "Use telemetry to compare agent performance across versions and automate approvals using the collected metrics." (`versioning/Recommendations.md` lines 61-62). No run-time rule found that sends a single action to a person when a condition fails.

**4. What a person does, and when.** Before deployment of high-risk agents and for disputed cases: "Ensure that high-risk agents undergo rigorous testing and human-in-the-loop oversight before deployment." (`versioning/Recommendations.md` lines 54-55). "Human review | For gray areas or disputed calls" (`evaluation/ToolCall.md` line 73). Memory: "a queue for human review is often a governance requirement" (`memory/Memory-Pipelines.md` line 216). A stop: "Include manual override mechanisms (e.g., pause/disable an agent class) without affecting the overall system." (`security/Security.md` lines 89-90). Per-action human approval at run time: not found.

**5. Long-lived agents.** Mentioned, not defined as a kind. "Support rotating credentials for long-lived agents." (`security/Security.md` line 22). "Choose when: building autonomous, long-running agents where no fixed retrieval policy can be defined up front." (`memory/Memory-Architecture-Patterns.md` lines 167-168).

### 5. AWS Prescriptive Guidance (six guides)

**1. Position.** Both. A goal: "By embedding trust mechanisms into the agent lifecycle, organizations can permit their systems to operate autonomously with accountability." and "Ultimately, trusted autonomy accelerates adoption" (`S/aws/strategy-operationalizing-agentic-ai/focus-areas-trust.clean` lines 88-97). A risk: "Autonomous agents challenge traditional control models. Their ability to reason and act independently introduces risk if they're not properly managed." (same file, lines 4-6). "Instead of rigid stages ... we need a model that embraces autonomy, uncertainty, and emergence." (`software-delivery.clean` lines 27-29).

**2. Levels.** An "evolutionary model" of agent kinds: "The agent autonomy, complexity, and business impact progressively increases. ... Observer agents surface insights from noise. ... Assistant agents support human decision-making. ... Autonomous agents act independently within defined boundaries. ... Orchestrator agents coordinate multi-agent workflows. ... Innovator agents generate new strategic possibilities." (`focus-areas-agent-intent-scope.clean` lines 42-59). "Autonomy levels" are named without a definition: "Role-based certification programs match autonomy levels to demonstrated competence." (`govern-architect-agentic-ai/governance-models.clean` lines 114-115).

**3. What lets an agent act with no person approving.** A bounded zone set in advance: "A zone of intent defines a bounded space where an agent can operate with autonomy, within constraints. The goal is to shift from micromanaging every task to designing environments where agents can act, learn, and collaborate safely. You specify the what (the desired outcome), the why (the intent), and the guardrails (the constraints, policies, and trust boundaries). Given those boundaries and this information, the agent figures out the how." (`software-delivery.clean` lines 29-37). Run-time thresholds: "Embed trust enforcement at runtime through intelligent guardrails. This includes rate controls and throttling based on behavioral patterns or workload conditions, resource boundaries enforced alongside auto-scaling, and decision scoring to evaluate risk. Build triggers to engage human-in-the-loop workflows when thresholds are exceeded." (`focus-areas-trust.clean` lines 21-25). A policy engine: "Amazon Bedrock AgentCore Policy – Cedar-based engine to implement contextual grounded fine-grained authorization on AgentCore data plane operations" (`govern-architect-agentic-ai/agents-layer.clean` lines 121-123). Agents watching agents: "Introduce reflective agents that continuously observe agent behavior and system patterns." (`focus-areas-trust.clean` lines 33-34).

**4. What a person does, and when.** At critical decisions and when thresholds are exceeded (above); at the policy level: "Establish governance boards that review agent policies, approve capability changes, and oversee incident response protocols." (`focus-areas-trust.clean` lines 40-42). "Autonomous team agents ... guide business processes in the background while keeping humans in control at critical decision points." (`govern-architect-agentic-ai/the-internal-productivity-landscape.clean` lines 54-57). Each agent's charter asks "Where does the agent's autonomy begin and end?" (`focus-areas-agent-intent-scope.clean` line 19).

**5. Long-lived agents.** Mentioned, not defined as a kind. "Agents can run in autonomy for hours, need to retain context and at the same time be fully isolated from other agent instances." (`govern-architect-agentic-ai/agents-layer.clean` lines 13-15). Background theory: "Continuity: The agent operates persistently over time, without requiring constant human intervention." (`agentic-ai-foundations/nwana-typology.clean` lines 25-26).

### 6. Google Cloud Architecture Center, agentic AI pages

**1. Position.** Not stated as a goal or a risk. Autonomy is a selection criterion: "AI agents are suitable when you need AI to complete goal-focused tasks with some degree of autonomy." (`S/google/body-choose-design-pattern-agentic-ai-system.txt` lines 19-20). One question for choosing a pattern: "Human involvement: Does your task involve high-stakes decisions, safety-critical operations, or subjective approvals that require human judgment?" (lines 68-70).

**2. Levels.** Not found (searched `autonomy level`, `level of autonomy`, `degree`; only the "some degree of autonomy" line above).

**3. What lets an agent act with no person approving.** Access granted in advance to an agent identity, and deny-by-default gateways: "You use IAM access policies and IAP to grant each agent identity only the permissions that it needs to perform its tasks" and Agent Gateway prevents "tool misuse by enforcing default-deny access policies" (`body-choose-agentic-ai-architecture-components.txt` lines 161-187). Review by another agent: "Based on the evaluation, the critic can approve the content, reject it, or return it to the generator with feedback for revision." (`body-choose-design-pattern-agentic-ai-system.txt` lines 263-265). No rule found that lets an action proceed when stated conditions hold and sends it to a person otherwise.

**4. What a person does, and when.** At checkpoints placed in the workflow at design time, for critical actions: "At a predefined checkpoint, the agent pauses its execution and calls an external system to wait for a person to review its work." and "Use the human-in-the-loop pattern for tasks that require human oversight, subjective judgment, or final approval for critical actions. Such actions include approving a large financial transaction" (lines 520-536). The same paragraph on most architecture pages: "Human oversight: Incorporate a human-in-the-loop flow in business-critical systems so human supervisors can review outputs and approve, override, or pause agent actions." (e.g. `body-agentic-ai-bidirectional-multimodal-streaming.txt` lines 226-228). "Validation for critical actions: Include human-in-the-loop (HITL) validation for critical tasks like booking non-refundable tickets." (`body-agentic-ai-system-with-grounding-using-maps.txt` lines 150-151).

**5. Long-lived agents.** Not addressed as a kind of agent. Persistence appears as session state and memory: "it uses a persistent session state and long-term memory to create a personalized experience" (`body-agentic-ai-interactive-learning.txt` lines 11-12). A runtime limit: "the maximum request timeout for Cloud Run services is up to one hour, which might constrain long-running agentic tasks." (`body-choose-agentic-ai-architecture-components.txt` lines 785-786).

### 7. Charterion v2.0 (El Hassani)

**1. Position.** Neither goal nor risk as such. Autonomy is an authority level an agent may hold under conditions. "X4. No autonomy without oversight. An agent that acts without per-action confirmation is watched by a reachable human, and no human watches more agents than the organisation has decided a person can. (WF7, WF9.)" (`S/charterion/c.txt` lines 1334-1336). On irreversible acts: "it does not forbid autonomy on irreversible operations—a payments organisation may well want a settlement agent that does not wait for a person—but requires that the architecture, not the incident review, name what happens next" (lines 2528-2531).

**2. Levels.** Yes. "Definition 6.1 (Action levels). All authority in Charterion is qualified by a level from the totally ordered set L = {read < propose < commit < autonomous} ... At read an agent may observe a resource; at propose it may prepare a change that a person or another authorised agent commits; at commit it may change the resource, each change being confirmed or reversible under a declared procedure; at autonomous it may change the resource without per-action confirmation." (lines 1911-1918). The four levels "compress the ten-level scale of Parasuraman et al. (2000)" (line 1919). Table 8.2 maps them to other scales and states a fifth level is excluded: "L5 (indicative) not admissible in Charterion: WF7 requires oversight and WF9 requires reachability" (lines 2652-2655). The text credits the idea to others: "Charterion does not claim to have invented the agent as a principal, the human sponsor, scoped ... autonomy levels, human oversight or run-time interception" (line 232 onward).

**3. What lets an agent act with no person approving.** A charter, approved by a person, at a level, produces a run-time envelope that a decision function checks at each action. "X1. No authority without a charter. An agent acts only under a charter that binds it to a business scope at a stated level under a stated principal." (lines 1327-1328). "Definition 9.5 (Charter-derived envelope) ... each with provenance σ = the charter identifiers from which the need derives, approver set Acc(g,·) restricted to H, validity equal to the intersection of the validity intervals of those charters, and the following rules: a threshold rule from Cap when the quantitative profile is in use (permit below λpermit, escalate up to λescalate, deny above); a separation-of-duty rule for every SoD(s, s′) with s covered by g; and an escalation condition naming Esc(g,·) for every entry at ℓ ≥ commit whose charter is Stale, and for every entry at autonomous (the human of Oversight may halt)." and "every envelope entry has a human approver by Proposition 7.3" (lines 3333-3343). The run-time function returns permit, deny, escalate or unwarranted (Algorithm 1, lines 3195-3240); "escalate is routed to a human named in the design model (Section 8.2), not to 'the user'; unwarranted is grounded in the warrant of the assertions consulted and is kept distinct from escalate" (lines 3261-3263). Condition on irreversible acts: "Condition 8.5 (WF12: Compensable autonomy). No agent holds autonomous authority over a step that writes an irreversible resource unless a compensation for that resource is available" (line 2520). Authority is time-limited: "Charters carry a validity interval and a review date; expired charters confer nothing" (line 1396). An agent cannot grant itself authority: "an agent may propose any assertion about its own authority; it may approve none." (line 4082). Another agent may commit at the propose level (Def. 6.1 above) and may supervise: "A human, or a supervising agent acting for one, watches an autonomous agent and can stop it." (line 12251).

**4. What a person does, and when.** Charters and approves authority in advance; watches agents at the autonomous level; answers escalations; is the only source of new authority. "X2. No charter without a principal. Every charter that confers a write level names a human, or a role with a current holder, who is accountable." (lines 1329-1330). "WF7 Watched autonomy | Every agent with autonomous authority is under human oversight" (lines 2262-2265). The Authority Request Protocol "gives the architecture a way to answer through its human gates, so that the model remains the single origin of authority even when the initiative comes from the agent" (lines 4080-4082).

**5. Long-lived agents.** Agents are long-lived; per-task processes are instances without their own authority. "agents outlive the reorganisations that created them" (line 1397). "Definition 8.9 (Instance). An instance i of agent a is a running process that acts under the identity of a and holds no charter of its own." (lines 2737-2738). `charterion-full.md` (line 376) reports that "persistent", "long-lived", "long-running" and "lifetime" occur 0 times; I did not re-run that count.

### 8. AEON (Longmire and Longmire)

**1. Position.** Autonomy beyond set bounds is a risk the platform constrains: "Targeting-adjacent inference, manipulation of certain categories of sensitive data, generation of content in restricted domains, agent autonomy beyond specified bounds, and similar boundaries are constrained at the runtime behavior layer." (`S/dl/aeon.txt` lines 769-773). No statement of autonomy as a goal found.

**2. Levels.** Not found (searched `autonomy level`, `levels of autonomy`, `maturity level`). It defines seven decision types instead (item 3).

**3. What lets an agent act with no person approving.** The principal's standing, delegated authority, checked by an authority plane at each consequential action. Delegation: "When AEON-resolved principals invoke agents, the agents inherit a delegated authority from the principal. ... every action anywhere in the enterprise traces back to a human principal through a verifiable cryptographic chain" (lines 564-569). "AEON receives the authentication assertion and constructs an authority token that carries the principal's identity, the federation context, the authorized scope, and the expiration." (lines 572-575). Decision types: "The decision is not a binary allow or deny. ... Allow permits the action without modification. Deny refuses the action ... Constrain permits the action subject to constraints ... Redact ... Route ... Log ... Escalate requires the action to be confirmed by a higher authority before it executes. Escalation applies when the action is consequential enough that the principal's standing authorization is insufficient and a second authority must approve." (lines 679-703). Subdomains "promise to consult the authority plane before consequential actions, to honor the full decision ... and to refuse to perform actions for which they have not received authority plane sanction." (lines 789-793).

**4. What a person does, and when.** The principal's authority is the root. A "second authority" confirms escalated actions; the text does not say this must be a person (lines 701-703). Policy that cannot be compiled stays with escalation: "The architectural response is the seven decision types and the escalate option for actions that exceed compilable policy." (lines 1698-1699). The "manual oversight focuses on exceptions rather than routine operations" sentence (line 1199) is about operating AEON's own runtime platform, not about agents' actions.

**5. Long-lived agents.** Not found. Searched `persist`, `lifetime`, `ephemeral`, `long-lived`, `long-running`, `spawn`: only "delegation chain extension when the subdomain spawns agents" (line 644). The delegation chain "is constructed at session start" (line 572).

### 9. CEAD (deVadoss, arXiv:2605.08258)

**1. Position.** A design variable, not a goal. "Autonomy is a design variable: assign L0–L4 autonomy by action risk, reversibility, confidence, and evidence, not by model capability alone." (`S/cead/c.txt` lines 463-465). "In regulated enterprise settings, the objective is not autonomous completion at any cost; it is safe completion with evidence, reversibility where possible, and appropriate human participation." (lines 570-573). Scope excludes "unrestricted autonomous systems: in enterprises, intelligent agents must remain bounded by policy, data classifications, identity, audit, release controls, and human approval for high-risk actions." (lines 66-69).

**2. Levels.** Yes. "Enterprises should avoid a binary 'agent allowed/not allowed' model. We define five autonomy levels: L0 Observe: retrieve, summarize, classify, or explain; no system changes. L1 Draft: produce recommendations or drafts; human executes. L2 Prepare: prepare structured actions; human approves submission. L3 Bounded execute: execute reversible or low-risk actions under policy and budget. L4 High-autonomy execute: execute high-impact workflows only with explicit enterprise risk acceptance, continuous monitoring, and strong rollback/escalation mechanisms." (lines 221-235).

**3. What lets an agent act with no person approving.** A per-agent contract (ACC) that declares the level: "Autonomy level | Declares L0–L4 action authority, approval requirements, reversibility expectations, and fallback" (Table II, line 422). "Bounded autonomy: it can choose among actions within explicit authority, policy, and approval boundaries." (lines 205-206). "Least privilege follows design: tool access is scoped per task, data class, action type, and autonomy level." (lines 466-467). Agent review: multi-agent design is justified when "one agent must verify, challenge, or approve another agent's work" (line 674). The run-time check that compares an action with the declared level is not described.

**4. What a person does, and when.** Decides at design time which actions stay human, and approves high-risk actions: "What decisions may the agent make, and which actions must remain human-owned?" (lines 104-105). "Human approval is not an exception path; it is part of the interaction design for irreversible, regulated, ambiguous, or high-impact actions." (lines 449-451). "Make humans part of the system. Human approval should be explicit, observable, and risk-based, not an afterthought." (lines 720-721).

**5. Long-lived agents.** Prefers few durable agents. "Small number of durable agents: prefer a few accountable agents over many role-playing prompt wrappers." (lines 461-462). Every production agent needs a contract "that describes authority, interfaces, memory, verification, and retirement" (lines 459-460). No per-task agent kind found.

### 10. Salesforce, "The Agentic Enterprise - The IT Architecture"

**1. Position.** A goal. "Agent-first with human oversight: Enable AI agents to be the default tool to solve business use cases" (`S/sf/body.txt` line 65). "Autonomous Process Execution: A digital workforce can execute complex, multi-step tasks 24/7 at machine speed (with humans in the loop)" (line 41). Maturity level 4: "Thematic investments focus on creating a self-improving, autonomous system." (line 233). Risk is also named: "More granular and dynamic controls are needed given the risk of agents causing cascading risks due to their ability to operate at machine speeds." (line 64).

**2. Levels.** An "Agentic Maturity Model" of capability, not of action autonomy: "agent capabilities grow from information retrieval agents (Level 1) to simple single-domain orchestration (Level 2), complex multi-domain orchestration (Level 3), and multi-agent orchestration (Level 4). Level 0 is fixed-rule chatbots and co-pilots." (line 209).

**3. What lets an agent act with no person approving.** Permissions granted by task intent, risk-based controls, and policy as code: "Enforce dynamic, granular permissions based on the intent of the agent's tasks (data access, actions, and so on) and implement ... risk-based validation controls." (line 64). "Policy-as-Code Engine: A single source of truth for defining business rules and compliance constraints in a declarative, machine-readable format to set guardrails for agent behavior." (line 205). The orchestration layer ensures "appropriate levels of human involvement (e.g., exception handling), bounded autonomy for AI agents, and enforce compliance" (line 77). Escalation is triggered by the agent's own confidence, not by a policy check: "Agents require self-reflective capabilities to proactively seek human guidance if its confidence over decision-making falls below pre-programmed thresholds." (line 65).

**4. What a person does, and when.** Monitors and can intervene at any step; handles exceptions; approves self-modification. "This includes the ability for humans to monitor, intervene in, and override any step of an agent's process." (line 65). Orchestration "integrates human oversight at critical junctures" (line 77). "Agent Self-Reflection & Adaptation Framework: Provides a mechanism for an agent to analyze its own performance and, with human approval, trigger improvements or suggest modifications to itself." (line 101).

**5. Long-lived agents.** Only per-task instances: "Agents are instantiated for specific tasks, and the specific agent instances are decommissioned afterwards. This implementation enables agents to be always invoked from the latest configuration state" (line 90). Work runs continuously ("24/7", line 41), but the agent instance does not.

### 11. AOS-0001 and AOS-0000 (Sharma and Shah)

**1. Position.** Autonomy is accepted; the aim is control at the boundary. "The research challenge is not in making agents autonomous, but in making autonomy deterministic at the boundary." (`S/dl/aos0.txt` lines 65-66).

**2. Levels.** Yes, in AOS-0000: "8.6 Bounded Autonomy Levels. AOS deployments benefit from explicit autonomy levels that align with enterprise change management. 1. Read only. No side effects. Tools limited to observation and retrieval. 2. Low risk. Limited and reversible side effects under strict scopes. 3. Controlled. Broader actions with full policy, audit, and anomaly monitoring. 4. High impact. Actions require approvals or dual control and may require additional verification steps." (`aos0.txt` lines 634-640).

**3. What lets an agent act with no person approving.** A deterministic policy function and confidence thresholds. "π(I, a, c, x, s) → {allow, deny, modify, approve} × Ω ... The outcome approve indicates that an additional approval authority is required before execution." and "Policy can require human approval or stronger runtime isolation for high-impact actions." with the example rule "human_approval_if: side_effecting_action" (`S/dl/aos.txt` lines 598-621). "A high-impact action may require high confidence, independent verification, and human approval. A reversible or informational action may proceed with warning." (lines 1007-1009). Control actions: "PROCEED | Confidence and policy thresholds satisfied | Execute within directive and standard evidence profile" and "ESCALATE | Human judgment or independent authority required | Pause and create accountable review task" (lines 1459-1464). Capabilities set in advance: "A capability specifies which tools can be invoked, which resource scopes apply, which parameter ranges are permitted, which time windows are valid, and whether human approval is required." (`aos0.txt` lines 273-275). Delegation narrows: "Delegated scope, budget, and lifetime MUST NOT exceed the parent grant without independent authority." (`aos.txt` line 2175).

**4. What a person does, and when.** Sets policy and thresholds, decides exceptions. "Humans remain responsible for policy, approval thresholds, exceptions, appeals, and accountability. Human-in-the-loop is not one generic step; it includes approval before action, supervisory review, emergency stop, post-action review, and dispute resolution." (`aos.txt` lines 852-853). "The control plane routes each request to an accountable role rather than a generic 'human.'" and "Human unavailability is a failure mode that policy must handle explicitly through timeout, alternative approver, safe fallback, or termination." (lines 1032-1037). Approvals "are not substitutes for deterministic policy. They are governance mechanisms for high impact operations" (`aos0.txt` lines 631-633).

**5. Long-lived agents.** Addressed. "The managed object may be a persistent agent identity or a transient runtime instance. AOS distinguishes identity from instance so that an agent can migrate or restart without losing authority and audit continuity." (`aos.txt` lines 1065-1066). "Long-running agentic systems require declared lifecycle states." (line 833). "Durable agent memory is persistent state across long-lived tasks and must be versioned." (`aos0.txt` line 248).

### 12. Steinder and Franke, "Towards an Agent Operating System" (IBM)

**1. Position.** Irreversible autonomous action is named as a risk; oversight is a platform duty. Agent-OS ensures "the whole system remains auditable and under human oversight" (`S/dl/ibm.txt` lines 198-199). Agents may call "tools with irreversible consequences — sent emails, executed financial transactions, deleted production records" (line 352). No statement of autonomy as a goal found.

**2. Levels.** Not found (searched `level`, `autonomy level`). It classifies operations by reversibility instead: "the platform must classify calls as reversible, compensable, or irreversible and require elevated authorization for the last." (line 570).

**3. What lets an agent act with no person approving.** A gateway that authorizes by operation class: "MCP Gateways aggregate, route, and enforce authorization with a reversibility model that blocks irreversible calls without elevated authorization." (lines 575-577). Guardrails: "Guardrails are platform-level behavioral constraints the agent cannot override: blocking disallowed tool calls, PII in outputs, looping behavior, and out-of-scope actions." (lines 675-677). "the tool mediation layer must intercept and authorize every action" (line 249). Who gives "elevated authorization" is not stated.

**4. What a person does, and when.** Not specified beyond this: "As guardrails in AI systems cannot be enforced with the same determinism as in classical ones, risk based assessment, and human-in-the-loop enforcement are necessary elements." (line 677).

**5. Long-lived agents.** Not distinguished. The agent loop is per task: it "runs until the task is complete, a resource limit is exhausted, or the platform intervenes" (lines 239-241). "An agent is an isolated execution context (container/pod) with an LLM session, tool credentials, context buffer, and memory state. It may be created, run ..., terminated. Agents spawn sub-agents" (lines 515-519).

### 13. ASOC manifesto (Beheshti et al.)

**1. Position.** A goal, made acceptable by governance. "The agent harness is the core ASOC mechanism through which autonomy is converted into governed autonomy." (`S/dl/asoc.txt` line 269). "Harnessability is not a restriction on agent capability; it is the engineering condition that makes capable agents deployable." (line 349). It names the tension as a research question: "how do they manage the tension between agent autonomy and organisational control?" (line 439).

**2. Levels.** Yes. "TABLE III: Levels of Delegation and Autonomy in ASOC. Each level maps a degree of agent autonomy to the minimum ASOC control requirements a delegation contract must enforce." L0 "Advisory only | Provenance and explanation"; L1 "Tool recommendation | Human approval"; L2 "Bounded execution | Delegation contract and harness"; L3 "Multi-step orchestration | Continuous monitoring and revocation"; L4 "High-consequence autonomy | Certification, audit, and liability model" (lines 272-293).

**3. What lets an agent act with no person approving.** A delegation contract enforced by a harness. "Delegation Contract: A formal specification of the scope, authority, constraints, duration, revocability, and accountability conditions under which a human or organisation delegates a goal to an agentic service." (line 267). The harness "mediates the boundary between model capability and service accountability by enforcing delegation scope, tool permissions, policy constraints, execution logging, approval gates, circuit breakers, and revocation mechanisms." (line 269).

**4. What a person does, and when.** Delegates the goal and the contract; approves at L1 and at consequential actions in the examples. A clinical example needs "a harness enforcing human approval before consequential" actions (lines 218-219; the sentence continues past the extracted line). A measure: "Human-Oversight Effectiveness | Degree to which review gates intercept harmful actions before execution; measured by escalation interception rate" (lines 516-520). It does not say which actions at L2 to L4 require a person.

**5. Long-lived agents.** Not found as a distinction. Searched `persistent`, `long-lived`, `long-running`, `lifetime`. The only time term is a delegation's "duration" (line 267) and "lifecycle engineering" of agents as services (line 37).

### 14. EAAF (Venkiteela)

**1. Position.** A goal. Title: "An Enterprise Agentic Architecture Framework for Agentic AI Governance and Scalable Autonomy" (`S/dl/eaaf.txt` line 72). "It ensures safe autonomy" (line 34). "Autonomy with Accountability: Agents are empowered with operational autonomy, meaning they can independently navigate complex IT landscapes, decompose tasks, and execute technical workflows. However, this is strictly decoupled from decision authority." (lines 457-462).

**2. Levels.** Not defined. Autonomy is measured as a percentage: "Table 1. Task Success & Autonomy. Execution Mode Success Rate Autonomy Level Avg. Completion Time. Human 72% 0% ... EAAF (Agents) 95% 82%" (lines 1117-1121). No definition of "Autonomy Level" found.

**3. What lets an agent act with no person approving.** A pre-defined authority checked by a pre-action pipeline. "Every proposed tool invocation is passed through the Pre-Action Validation Pipeline, which checks risk scores and policy constraints. If a proposed action exceeds the agent's pre-defined authority, it is either blocked or routed for human approval, regardless of the agent's technical capability to perform the task." (lines 647-653). The pipeline "evaluates every proposed tool invocation against its Intent Classification, Safety Scoring, Policy Constraints, and Risk Level before granting an Allowed, Blocked, or Requires Approval outcome." (lines 811-815). Example: an "Autonomous Procurement Agent" performs a "Compliance Check (verifying spend thresholds), escalating to finance personnel only when anomalies occur." (lines 1005-1012). Agents also watch agents: "dedicated Compliance Agents continuously monitor for anomalous agent behavior ... intervening when necessary." (lines 816-819).

**4. What a person does, and when.** Sets policy and handles high-risk exceptions. "Humans shift from being 'operators' who perform tasks to 'governors' who set policies and handle high-risk exceptions flagged by the safety layer." (lines 360-363). "High-stakes actions such as financial transactions or security configuration changes require explicit authorization from the Governance Layer or human-in-the-loop checkpoints." (lines 462-466). "High-risk actions must never be executed without explicit, logged authorization." (lines 414-416).

**5. Long-lived agents.** Agents are managed assets with a lifecycle; no stated split by lifetime. "Agents must be treated as formal enterprise assets. The architecture must provide a standardized framework for the provisioning, policy configuration, runtime execution, monitoring, versioning, and secure decommissioning of all agents." (lines 400-405). "Task Agents" is a listed agent type (line 710), not a lifetime. Some agents run continuously: "Security and Compliance Agents to continuously monitor systems" (lines 1018-1020).

---

## A. Summary table

| # | Model | 1. Position | 2. Levels | 3. What lets an agent act without a person | 4. What a person does | 5. Long-lived agents |
|---|---|---|---|---|---|---|
| 1 | Yu et al. | Not found ("autonom" 0 hits) | None | L6 action-policy gate: permits, refuses or escalates; scoped, expiring delegated authority, re-authorized at execution | Sets rules at design time (L0); approves overrides (exceptions) | Long-running execution and persistent memory only |
| 2 | Zhu | Risk; deliberately limited | 4 risk-based decision classes | "Pre-approved policy" for Standard work; scoped expiring leases; agent Reviewer for Normal; second key for Major | Correction endpoint; one key for Major or Emergency; holds org kill | Rejected: agents dormant, workers temporary |
| 3 | AAM/5C | Goal (Level 4), with conditions | Levels 0-4 | Each act validated by L6 policy; pre-authorized capability envelope for low/moderate classes; irreversible never autonomous | Writes and co-signs policy; decides irreversible acts; holds stop | Agents run continuously; authority short-lived |
| 4 | Microsoft | Risk | Versioning maturity 1-4 only | Policy engine at MCP layer; approved capabilities; metric-based release approval | Pre-deployment review of high-risk agents; disputed cases; pause or disable | Mentioned ("long-lived agents"), not a kind |
| 5 | AWS | Goal and risk | Evolutionary model (observer to innovator) | Zones of intent; runtime thresholds; Cedar policy engine; reflective agents | Critical decisions; when thresholds are exceeded; governance boards | Mentioned ("autonomy for hours"), not a kind |
| 6 | Google | Not stated; selection criterion | None | IAM least privilege; default-deny gateway; critic agent | At predefined checkpoints for critical actions | Session state and memory only |
| 7 | Charterion | Admissible under conditions ("No autonomy without oversight") | read < propose < commit < autonomous; L5 inadmissible | Human-approved charter at a level gives a run-time envelope; permit / escalate / deny by threshold; compensation required for irreversible | Charters and approves authority; oversees autonomous agents; answers escalations; only source of new authority | Long-lived agents; per-task instances hold no charter |
| 8 | AEON | Risk beyond bounds | None (7 decision types) | Principal's standing delegated authority; authority plane decides allow, constrain, ..., escalate | Root principal; "second authority" for escalations (person not specified) | Not found |
| 9 | CEAD | Design variable | L0-L4 | Contract declares autonomy level and approvals; L3 under policy and budget | Decides human-owned actions; approves irreversible, regulated, ambiguous or high-impact actions | Prefers "a few" durable agents |
| 10 | Salesforce | Goal ("Agent-first") | Maturity 0-4 (capability) | Intent-based permissions; policy as code; agent self-escalates on low confidence | Monitor, intervene, override any step; exceptions; approve self-modification | Per-task instances only |
| 11 | AOS | Accepted; control at boundary | 4 bounded autonomy levels | Policy function allow / deny / modify / approve; PROCEED on thresholds; capabilities set in advance | Sets policy and thresholds; approves exceptions; emergency stop | Persistent identity vs transient instance |
| 12 | Steinder and Franke | Risk (irreversible acts) | None; reversible / compensable / irreversible | Gateway blocks irreversible calls without elevated authorization | Not specified ("human-in-the-loop enforcement are necessary") | Not distinguished; per-task loop |
| 13 | ASOC | Goal, as governed autonomy | L0-L4 delegation and autonomy | Delegation contract enforced by a harness | Delegates goal; approves at L1 and consequential steps | Not found |
| 14 | EAAF | Goal ("Scalable Autonomy") | None defined; autonomy as % | Pre-defined authority; pre-action pipeline: Allowed, Blocked, Requires Approval | Sets policy; handles high-risk exceptions | Agents as assets with lifecycle; no lifetime split |

---

## B. Which models state the idea

The idea, in the reader's words: "a person authorizes a class of actions in advance, under stated conditions; at run time the system checks the conditions and lets the action proceed with no person asked; holding an action for a person is the fallback."

Each part of the idea is tested separately: (a) a person authorizes in advance, (b) a class of actions under conditions, (c) a run-time check lets the action proceed, (d) holding for a person is the fallback.

| Model | Verdict | Closest passage |
|---|---|---|
| Charterion | Equivalent, and more complete | "a threshold rule from Cap when the quantitative profile is in use (permit below λpermit, escalate up to λescalate, deny above) ... every envelope entry has a human approver by Proposition 7.3" (c.txt lines 3336-3342) |
| AAM/5C | Equivalent, and more complete | "It is an authorization decided by L6 and issued in advance by L5, which delimits a bounded right to act. ... A restricted, explicit scope (classes of acts, resources, quotas); A short expiry; Local verification by the PEP ... Revocation by event; A posteriori audit ... attributed to the co-signatories of the policy that underlies the envelope" (aam.txt lines 2498-2509) |
| Zhu | Equivalent | "During human-offline periods, only pre-approved, reversible Standard work proceeds automatically; higher-risk decisions queue or HALT." (line 632) |
| AOS | Equivalent | "Humans remain responsible for policy, approval thresholds, exceptions" (aos.txt line 852); "PROCEED | Confidence and policy thresholds satisfied" and "ESCALATE | Human judgment or independent authority required | Pause and create accountable review task" (lines 1459-1464) |
| EAAF | Equivalent | "If a proposed action exceeds the agent's pre-defined authority, it is either blocked or routed for human approval" (eaaf.txt lines 651-653); "governors who set policies" (line 362) |
| Yu et al. | Equivalent in the worked example | "L6 re-runs the mandate check and clears a compliant trade. For a breach with a requested override, it holds the trade until a principal who holds the override entitlement and is not the submitter approves it" (line 612); the mandate is an "L0 decision" (line 610) |
| AEON | Equivalent, with one gap | "Escalation applies when the action is consequential enough that the principal's standing authorization is insufficient and a second authority must approve." (aeon.txt lines 702-703). Gap: the "second authority" is not stated to be a person |
| CEAD | Partial | "L3 Bounded execute: execute reversible or low-risk actions under policy and budget" (line 230) and an ACC that "Declares L0–L4 action authority, approval requirements, reversibility expectations, and fallback" (line 422). The run-time check is not described |
| ASOC | Partial | "Delegation Contract: A formal specification of the scope, authority, constraints, duration, revocability, and accountability conditions under which a human or organisation delegates a goal to an agentic service." (line 267). The harness enforces it; the fallback to a person is listed ("approval gates") but no rule says when |
| AWS | Partial | "A zone of intent defines a bounded space where an agent can operate with autonomy, within constraints" (software-delivery.clean line 29) plus "Build triggers to engage human-in-the-loop workflows when thresholds are exceeded." (focus-areas-trust.clean lines 24-25). The two pieces are on different pages and are not tied together |
| Steinder and Franke | Partial | "a reversibility model that blocks irreversible calls without elevated authorization" (ibm.txt lines 576-577). The class is reversibility; who authorizes in advance and who gives elevated authorization are not stated |
| Salesforce | Partial, different mechanism | "Agents require self-reflective capabilities to proactively seek human guidance if its confidence over decision-making falls below pre-programmed thresholds." (body.txt line 65). The agent's own confidence, not a check of conditions a person set, triggers the hold |
| Microsoft | Not found as a whole | Closest: "Policy-->>MCP: Access granted with constraints" (Patterns.md) and "It's critical to define the scope of what agents are allowed to do" (Governance.md line 25). No run-time hold for a person |
| Google | Not found as a whole | Closest: IAM grants "each agent identity only the permissions that it needs" (components page lines 183-185) and a human checkpoint "At a predefined checkpoint" (design-pattern page line 521). The checkpoint is fixed in the workflow, not a conditional fallback |

Sources that state more than the sentence:
- **Charterion** adds: the authorization has a validity interval and review date; an agent at the autonomous level must be watched by a named, reachable person, with a cap on how many agents one person watches; autonomy over an irreversible resource needs a compensating step in the model; a fourth outcome, "unwarranted", for when the evidence behind a decision is too weak, kept separate from "escalate"; an agent can request authority but cannot approve its own; escalations go to a named person, not "the user".
- **AAM/5C** adds: the advance authorization is short-lived and revocable by event; each act covered by it is audited and attributed to the people who co-signed the policy; irreversible acts are excluded from it regardless of criticality; a self-declared attribute can only add restrictions.
- **Zhu** adds: the authorization is a lease that ends at completion, timeout, budget break or halt; the required authority scales on two axes (reversibility, blast radius); an agent Reviewer, not a person, decides the middle class.
- **AOS** adds: delegated scope can only narrow; the person asked is an accountable role; the unavailability of a person is a failure mode with stated responses (timeout, alternative approver, safe fallback, termination).

---

## C. Where the sources disagree

1. **Can an irreversible act run without a person?**
   - No: AAM/5C, "irreversible acts, whatever their criticality, require human validation (§4.4)" (aam.txt line 2522).
   - Yes, under a condition: Charterion, "it does not forbid autonomy on irreversible operations—a payments organisation may well want a settlement agent that does not wait for a person" if a compensation step exists (c.txt lines 2528-2529).
   - Not necessarily a person: Zhu, "Major or irreversible change requires a second key from a distinct Reviewer, a deterministic control, or the human." (line 746). Steinder and Franke require "elevated authorization" without naming who gives it (line 570).

2. **Can the highest level act without a person?**
   - Yes: AAM/5C Level 4 "also executes high-criticality acts within a bounded domain" (line 1959); CEAD L4 executes "high-impact workflows only with explicit enterprise risk acceptance, continuous monitoring, and strong rollback/escalation mechanisms" (lines 232-235); ASOC L4 "High-consequence autonomy" requires "Certification, audit, and liability model" (line 292), not approval.
   - No: AOS-0000's top level, "High impact. Actions require approvals or dual control" (aos0.txt line 639); EAAF, "High-risk actions must never be executed without explicit, logged authorization." (line 414).
   - Charterion's top admissible level is "autonomous", but it must be watched; the level above, "decides everything, ignores the human", is "not admissible" (c.txt lines 2650-2655).

3. **Can another agent stand in for the person?**
   - Yes for some decisions: Zhu's Reviewer approves Normal changes (Table 5); Charterion's propose level lets "a person or another authorised agent" commit, and "a supervising agent acting for one" may watch (lines 1915, 12251); Google's critic "can approve the content" (line 263); AOS lets "independent authority" replace human judgment for ESCALATE (line 1464).
   - The approver is a person in Yu et al.'s example ("a principal who holds the override entitlement and is not the submitter", line 612) and in AAM/5C for irreversible acts.

4. **Who triggers the hold?**
   - A check of conditions a person set: Charterion, AAM/5C, AOS, EAAF, Yu et al., Zhu.
   - The agent's own confidence: Salesforce ("seek human guidance if its confidence ... falls below pre-programmed thresholds", line 65). AAM/5C restricts this kind of input: a self-declared attribute "may only add a restriction ... never lift one" (line 2300). These two are compatible for adding a hold; AAM/5C forbids the agent's input from removing one.

5. **Is autonomy a goal?**
   - Goal: AAM/5C (Level 4 "objective"), Salesforce ("Agent-first"), EAAF ("Scalable Autonomy"), AWS ("trusted autonomy accelerates adoption").
   - Not a goal: CEAD ("the objective is not autonomous completion at any cost", line 571); Zhu ("The present target is a human-supervised organization", line 1119).

6. **What happens when no person is available?**
   - Zhu: higher-risk decisions "queue or HALT" (line 632).
   - AAM/5C: high-criticality acts are blocked: "for these acts, denial by default is better than a right to act whose revocation would no longer be guaranteed" (lines 2522-2524).
   - AOS: "timeout, alternative approver, safe fallback, or termination" (line 1037).
   - The others: not found.

7. **Should agents be long-lived?**
   - No: Zhu ("There is no digital employee permanently nailed to a position", line 163); Salesforce ("instantiated for specific tasks ... decommissioned afterwards", line 90).
   - Yes: CEAD ("prefer a few accountable agents", line 461); AAM/5C ("continuously runs", line 1719); Charterion ("agents outlive the reorganisations that created them", line 1397); AOS (persistent identity).

---

## D. Limits

**Could not determine.**
- Whether AEON's "second authority" for escalation is a person.
- Who gives the "elevated authorization" in Steinder and Franke.
- Which actions at ASOC levels L2 to L4 require a person.
- What EAAF means by "Autonomy Level" in Table 1; no definition found.
- How CEAD's runtime checks an action against the declared autonomy level.

**Not read.**
- AWS: the guides the mappers found and did not read, which may say more on autonomy: "Security for agentic AI on AWS", the semantic-layer guide, the Well-Architected Agentic AI Lens, most of the serverless and multi-tenant guides; and the enterprise multi-account guide, which returned "page not found" (`mapping-vendors.md` lines 43, 363-364). I did not fetch them.
- Figures that exist only as images: AAM/5C figures F.1 to F.19 (including F.18, the escalation thresholds); five of seven Salesforce figures; ASOC Figure 1 (read by the mapper as an image, not by me); the Yu et al. Fig. 3 sequence diagram.
- Charterion: I searched all 290 pages of the extracted text and read the passages around each hit. I did not read every chapter.
- The AWS and Google pages: I searched the local text copies. I did not read every page in full.
- Microsoft's Cloud Adoption Framework page on agent charters, cited in `synthesis-round2.md`, is not one of the fourteen and was not examined.
- I used no WebFetch. Every quote comes from a local copy.

**Quotes taken from a mapping file without a re-check against the source.**
- The AAM/5C statement that searches for "subagent", "spawn" and "worker" found nothing (`mapping-aam5c.md` line 421). I did not re-run them.
- The Charterion count of 0 for "persistent", "long-lived", "long-running" and "lifetime" (`charterion-full.md` line 376). I did not re-run it.

Every other quote was re-checked against the local source text named with it.

**Local copies.**
- The Salesforce text is the mapper's extraction from the HTML (`S/sf/body.txt`). The live page returned "Access Denied" to a plain fetch (`S/sf/sf.html`).
- The Google text is the page body extracted to `S/google/body-*.txt`.
- Line numbers refer to those files, not to printed pages.
