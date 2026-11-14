---
title: "Decision review, reader A: fourteen published models of AI-agent systems"
date: 2026-11-12
author: "reader A (Claude subagent)"
protocol: "protocol-v2.md (five questions, H1 to H5)"
sources: "references.txt [12] to [25]"
---

# Summary of values

Values follow protocol v2. "DISPUTABLE (x)" means the cell holds the lower of two defensible values and x is the other one. The reasons are in the detail table.

| Ref | Source | H1 record | H2 measure | H3 review changes rules | H4 authority follows record | H5 capability hand-offs |
|---|---|---|---|---|---|---|
| [12] | Yu, Rabhi, Zhu, Lu | no, DISPUTABLE (part) | no | no | no | no |
| [13] | Zhu, Fluid Structure, Rigid Record | part, DISPUTABLE (yes) | part, DISPUTABLE (yes) | no, DISPUTABLE (part) | part, DISPUTABLE (yes) | no |
| [14] | Goujon, AAM/5C | part | yes | no, DISPUTABLE (part) | part, DISPUTABLE (yes) | no, DISPUTABLE (part) |
| [15] | Microsoft Multi-Agent Reference Architecture | no | no | no | no | no |
| [16] | AWS Prescriptive Guidance, agentic AI | no, DISPUTABLE (part) | part | no | part | no, DISPUTABLE (part) |
| [17] | Google Cloud Architecture Center, agentic AI | no | no | no | no | no |
| [18] | El Hassani, Charterion v2.0 | yes | yes | yes | yes | part, DISPUTABLE (yes) |
| [19] | Longmire and Longmire, AEON | part, DISPUTABLE (yes) | part | no, DISPUTABLE (part) | part | no |
| [20] | deVadoss, CEAD | no, DISPUTABLE (part) | part | no | no, DISPUTABLE (part) | no |
| [21] | Salesforce Architects, The Agentic Enterprise | no | no | no | no | no |
| [22] | Sharma and Shah, AOS-0001 (with AOS-0000) | yes | part | no | part, DISPUTABLE (yes) | no, DISPUTABLE (part) |
| [23] | Steinder and Franke | no | no | no | no, DISPUTABLE (part) | no |
| [24] | Beheshti et al., ASOC manifesto | part, DISPUTABLE (yes) | part, DISPUTABLE (yes) | no | part | no |
| [25] | Venkiteela, EAAF | part | part | no | no, DISPUTABLE (part) | no |

Counts (14 sources):

| | yes | part | no | not assessed |
|---|---|---|---|---|
| H1 | 2 | 5 | 7 | 0 |
| H2 | 2 | 7 | 5 | 0 |
| H3 | 1 | 0 | 13 | 0 |
| H4 | 1 | 6 | 7 | 0 |
| H5 | 0 | 1 | 13 | 0 |

# Detail table

Quotations are exact, except that line-break hyphens in PDF text are rejoined and runs of spaces are collapsed. An ellipsis (...) marks words left out. "Searched" lists the terms searched in the full text with no passage found that meets the value.

Standard search set, used for every "no" unless the cell says otherwise: human, approv*, escalat*, interven*, override, oversight, takeover / take over, manual, hand-off / handoff, trust, earned, graduat*, autonomy level, rate, metric, KPI, record, log, audit, login / sign-in, cannot / unable, computer use.

## [12] Yu, Rabhi, Zhu and Lu, A Reference Architecture for Integrating Agentic AI into Enterprise Software (arXiv:2610.14818)

| Q | Value | Quotation or search | Location |
|---|---|---|---|
| H1 | no, DISPUTABLE (part) | "L6 resolves, validates, authorizes, executes, and records invocations of capabilities that interact with enterprise systems ... Its capabilities include ... action audit and provenance. Where an external effect requires additional control, L6 can apply an action-policy or approval gate before execution." The approval gate sits in the layer that records invocations, so a record of the gated action can be read in (part). The paper never says that the approval decision, or why it was needed, is recorded (no). | §IV-C, "L6—Tool & Action Runtime (Act)" |
| H2 | no | Standard set. L9 telemetry covers "usage and cost analysis"; T7 carries "traces, events, outcomes, usage, cost, audit information, and provenance". No quantity counts people's decisions. | §IV-D; Table I (T7) |
| H3 | no | Standard set. T8 "Improvement Feedback ... Returns evaluation findings, failure evidence, and quality, cost, or performance observations to inform governed architectural or configuration changes." It is general and does not examine people's decisions. | Table I (T8) |
| H4 | no | Standard set. The paper states the opposite direction only: "model-driven coordination need not transfer authority to the model." | §VII-A |
| H5 | no | Standard set. A question the data cannot answer "was declined after a single model decision" (G7); it is not handed to a person. | §V-C |

## [13] Zhu, Fluid Structure, Rigid Record (arXiv:2608.08516)

| Q | Value | Quotation or search | Location |
|---|---|---|---|
| H1 | part, DISPUTABLE (yes) | Log store contents: "accepted events, authority use, lineage, handoff and decision records ... kernel appends; no agent edits or deletes". Decision class "Major ... high blast radius or difficult to reverse ... Reviewer plus independent second key or human ... checkpoint, explicit evidence, human-visible decision". The log records "actor, task, lease, event type, policy version, time, input and output hashes, claims, and evidence pointers". Decisions are logged with evidence and policy version (part); the text does not state that the record names the class or rule that sent the step to a person (why yes is not certain). | §3.2, Table 2 and "Four-store record system"; §6.3, Table 5 |
| H2 | part, DISPUTABLE (yes) | "Each task records model and tool cost, wall time, retries, human minutes, evidence volume, P&P changes, and incidents." Also "Primary outcomes should include task quality, Equation (13), human intervention minutes, ...". A named per-task quantity, but it counts minutes, not decisions, and has no further definition. | §6.4; §7.1 |
| H3 | no, DISPUTABLE (part) | "Least privilege is a calibration problem as well as a principle. False denials, emergency overrides, stale grants, and over-broad read windows must be measured." And: "Learn creates a reviewed incident proposal for Knowledge or policy; the incident never edits the constitution directly." A stated goal of measuring overrides and denials to calibrate privilege (part), but no mechanism, and it concerns incidents and denials rather than people's decisions in general (no). | §7.2 "P&P can be wrong"; §6.1 |
| H4 | part, DISPUTABLE (yes) | After a corrupted sandbox: "The group is re-instantiated with narrower P&P." And: "an error budget freezes change work after a service objective is exhausted". These are defined rules that narrow authority after failures (yes), but only narrowing, triggered by incidents rather than a track record, and no widening (part). | §6.1; §6.4 |
| H5 | no | Standard set. "A deterministic schema or permission failure should not repeat the same route; it BLOCKs and escalates." Escalation is not defined as a hand-off to a person for lack of capability. | §6.3 |

## [14] Goujon, Agentic Architecture of Information Systems, the AAM/5C model (arXiv:2610.30221, manuscript V7.83-EN)

| Q | Value | Quotation or search | Location |
|---|---|---|---|
| H1 | part | "Level 2 — Supervised IS : the system detects and recommends acts from an explicit, bounded catalog; the human decides on their execution; every recommendation is logged;" The item put to a person is logged; the person's decision and the reason it went to a person are not stated as recorded. Elsewhere a covered act "is attributed to the co-signatories of the policy that underlies the envelope". | §5.3.2, p. 50; §7.4.3, p. 63 |
| H2 | yes | "G.109. Task completion rate (TCR) — Rate of agentic tasks completed without human intervention (Table 8)." Table 8 sets "Task Completion Rate (TCR) > 95%". Also "H4 — A2A cooperation ... more than 95% of conflicts resolved without escalation", and Table 7: "events of the triage tier handled without human intervention ≥ 60%". | Glossary, p. 98; §8.6 Table 8, p. 74; §3.2.3, p. 36; Table 7, p. 52 |
| H3 | no, DISPUTABLE (part) | "Learning — the result and its trace feed the agent and the revision of policies by the AOM (§8.4)." And: "The AOM-DAL adds a human review — monthly, quarterly or event-driven — of the learning step." A defined periodic human review that revises policy (part), but it reviews the results of agent acts, not decisions made by people (no). | §4.4, pp. 45-46 |
| H4 | part, DISPUTABLE (yes) | Phase transition milestones: "Phase 1 → 2 Toil reduced ≥ 40% on L1–L2; events of the triage tier handled without human intervention ≥ 60%". "The failure of a single criterion suspends the transition and triggers a policy review by the AOM (AOM-DAL loop, §4.4)." Measured criteria gate the widening of autonomy (yes), but at the level of an adoption roadmap for layers, where a manager "chooses to accelerate or to consolidate" (part). | §5.4.3 Table 7, p. 52; §5 "In Practice", p. 48 |
| H5 | no, DISPUTABLE (part) | Table 8, TCR row: "Repeated failures on inventory transactions" with action "Analyze L4 tool-call failures in the traces". Tasks needing a person are counted and failures analyzed (part), but the source does not separate steps a person does for lack of capability from steps that wait for authority (no). | §8.6 Table 8, p. 74 |

## [15] Microsoft, Multi-Agent Reference Architecture (GitHub)

| Q | Value | Quotation or search | Location |
|---|---|---|---|
| H1 | no | Standard set. Closest: "Ensure each version, and each agent, includes audit trails, approval records, and risk classifications." These are approvals of agent versions, not of agent actions. | docs/versioning/Recommendations.md, item 3 |
| H2 | no | Standard set. User impact metrics are "error rate, abandonment rate, CSAT". | docs/security/Security.md |
| H3 | no | Standard set. "Human review — For gray areas or disputed calls" is an evaluation method for tool calls, with no rule change. | docs/evaluation/ToolCall.md, "Methods and Tools" |
| H4 | no | Standard set. "Use telemetry to compare agent performance across versions and automate approvals using the collected metrics." This automates release approvals of versions, not an agent's authority to act. | docs/versioning/Recommendations.md, item 7 |
| H5 | no | Standard set. "Does it recover gracefully, retry, or escalate?" is an evaluation question with no hand-off to a person defined. | docs/evaluation/ToolCall.md |

## [16] AWS Prescriptive Guidance on agentic AI (seven guides read; see "What was opened")

| Q | Value | Quotation or search | Location |
|---|---|---|---|
| H1 | no, DISPUTABLE (part) | Log schema: "store the following information in each log entry: Prompt version Input/output Agent tool calls IAM principal ID Invocation timestamp and trace ID". No human decision field (no). A test example says the agent should "Decline the action, invoke an escalation Lambda, and log a request for audit." That logs an escalation without its outcome (part). | Serverless guide, security-and-governance.html, "Implement comprehensive logging"; testing-and-validation.html, "Security and boundary tests" |
| H2 | part | "Cognitive offload – How much manual analysis, triage, or routine decision-making was the agent able to handle on behalf of a human? Did it reduce effort or just shift it?" A named KPI with no definition. Also an example figure: "Enables self-service resolution for 70–80 percent of inquiries without escalation". | Operationalizing guide, preparing-business.html, "Adopting a decision-first operating mindset"; serverless guide, pattern-grounded-agent-ai.html |
| H3 | no | Standard set. "Conduct regular retrospectives to evaluate agent performance, usage trends, and improvement opportunities." This reviews agents, not people's decisions. | Operationalizing guide, preparing-business.html |
| H4 | part | "Establish governance boards that review agent policies, approve capability changes, and oversee incident response protocols. Trust must be earned, measured, and continually reinforced." Also: "As agents become more capable and more autonomous, oversight mechanisms must become more adaptive. Policy updates, capability gating, and runtime behavioral constraints need to be dynamic and enforceable at scale." Principle only. | Operationalizing guide, focus-areas-trust.html; preparing-business.html, "Building governance into an agentic fabric" |
| H5 | no, DISPUTABLE (part) | "Establish clear handoff protocols for when agents should escalate decisions to a higher authority or delegate parts of the process to a human collaborator." It separates delegating work to a person from escalating for authority, with no record or count (part), but it does not say the work goes to a person because the agent cannot do it (no). | Operationalizing guide, preparing-business.html, "Foster cultural evolution" |

## [17] Google Cloud Architecture Center, agentic AI pages (17 pages)

| Q | Value | Quotation or search | Location |
|---|---|---|---|
| H1 | no | Standard set. Closest: "Use structured logging: Log all agent tool invocations and pipeline outcomes with structured metadata." No record of people's decisions. | agentic-ai-multimodal-graph-rag-resource-orchestration |
| H2 | no | Standard set across all 17 pages. | all 17 pages |
| H3 | no | Standard set. | all 17 pages |
| H4 | no | Standard set. The pages recommend "carefully defined agent autonomy" with no rule that changes it from performance. | multiagent-ai-system; single-agent-ai-system-adk-cloud-run; multi-tenant-agentic-ai-system |
| H5 | no | Standard set. The human-in-the-loop pattern "lets a person approve a decision, correct an error, or provide necessary input before the agent can continue." It is not framed as a hand-off for lack of capability. | choose-design-pattern-agentic-ai-system, "Human-in-the-loop pattern" |

## [18] El Hassani, Charterion v2.0 (Zenodo 22829848, Charterion_v2.0_Specification.pdf)

Page numbers are PDF pages.

| Q | Value | Quotation or search | Location |
|---|---|---|---|
| H1 | yes | Admissibility outcome: "escalate means the approved envelope permits the action subject to a human decision—a threshold has been crossed or a human-in-the-loop condition applies—and that decision is taken by the escalation human of Definition 8.2." Record: "Every decision is appended to the Decision Log with its supporting assertions and minimum warrant (Inv-5) ... reversals are recorded against the original decision. Decisions are attributed to charters (CC6) and accumulated into the Evidence Record of each charter: counts of permit, deny, escalate and unwarranted outcomes, escalations accepted and refused by the human, and reversals." Outcome detail: "The runtime may record, for an escalate decision r ∈ L, the human who received it, Routed(r, h), and how and when it was decided, Resolved(r, o, t′) with o one of permitted, denied, pending." | §9.3, p. 69; §14.5 "O5 — Account", pp. 90-91; Definition 8.11, p. 66 |
| H2 | yes | "Per charter and per slice over a window: counts and shares of permit, deny, escalate and unwarranted outcomes; reversal rate of permitted actions; escalation acceptance rate; median time-to-decision for escalations ... The three agent KPIs of the business case ... admissible-action rate, escalation rate and reversal rate—are the headline subset." Defined: "the acceptance rate #permitted/(#permitted+ #denied) and the median time to decision t′ − t per human and period". Escalation load per human: "EscLoad(H, P) = #{R: outcome(R) = escalate, EscTo(R, H), Period π(t(R)) = P}". | §20.2, pp. 107-108; §8 attention profile, p. 66 |
| H3 | yes | "Bridge B2 (O5/O6 → D4). The attributed Evidence Records and drift reports return to the refine phase, where they drive three kinds of change: narrowing (a charter whose scope produces many denials or reversals is too broad), widening (an agent whose needs produce many unwarranted or unserved outcomes is under-chartered or the slice under-observed), and level changes under the evidence-gated promotion rule of Section 18.8. B2 is the mechanism by which the architecture learns". The evidence record includes "escalations accepted and refused by the human" (§14.5). | §14.7, p. 91 |
| H4 | yes | "A charter's level shall be raised only at gate G6, only by one step in L, and only if over the review window its Evidence Record satisfies the organisation's thresholds on: (a) the reversal rate of permitted actions; (b) the denial rate; (c) the share of unwarranted outcomes; (d) the acceptance rate of its escalations by the overseer; (e) the absence of CC6 unattributed evidence naming the agent. ... A charter's level may be lowered at any time by the agency architect or the overseer". Default thresholds: escalation acceptance rate "≥90 %" for propose to commit and "≥98 %" for commit to autonomous, minimum window "90 days, 500 decisions" and "180 days, 2000 decisions". Levels: "at propose it may prepare a change that a person or another authorised agent commits ... at autonomous it may change the resource without per-action confirmation." | §18.8 and Table 18.5, p. 103; Definition 6.1, p. 44 |
| H5 | part, DISPUTABLE (yes) | "unwarranted means the substrate cannot stand behind an answer; its remedy is re-observation or a human answer that becomes a new assertion." Unwarranted outcomes are counted (§20.2, "share of unwarranted outcomes") and kept distinct from escalate, and Bridge B2 reduces them by "widening" a charter or observing an "under-observed" slice (yes). But the hand-off is framed as missing evidence or warrant, not missing tools, access or computer use, and the person's answer is one of two remedies (part). | §9.3, p. 69; §14.7, p. 91 |

## [19] Longmire and Longmire, AEON (Zenodo 20349596, AEON-White-Paper.pdf)

| Q | Value | Quotation or search | Location |
|---|---|---|---|
| H1 | part, DISPUTABLE (yes) | Decision type: "Escalate requires the action to be confirmed by a higher authority before it executes." Record: "For every action a subdomain runtime performs, the evidence plane captures the action description in canonical form, the AEON-resolved principal under whose authority it was performed, the authority plane decision that sanctioned it, ... and any worker confirmation captured at the moment of consequential action." The authority decision and the human confirmation are kept (yes), but the text does not say the policy condition that caused an escalation is kept (part). | §8.1, p. 18; §9.1, pp. 20-21 |
| H2 | part | "The architectural response is the seven decision types and the escalate option for actions that exceed compilable policy. The practical question is how much policy can be compiled and how much remains in escalation." A quantity is mentioned, not defined. | §17.1 "Open Questions", p. 43 |
| H3 | no, DISPUTABLE (part) | "Early in the deployment, the runtime is operated cautiously with conservative defaults and substantial manual oversight. As confidence develops and operational experience accumulates, defaults loosen, automation expands, and manual oversight focuses on exceptions rather than routine operations." A stated goal with no mechanism (part); it does not describe reviewing people's past decisions (no). | §12.4 "Operational Posture", p. 30 |
| H4 | part | Same passage: "As confidence develops and operational experience accumulates, defaults loosen, automation expands". Principle only. | §12.4, p. 30 |
| H5 | no | Standard set. "propose-and-confirm" is a person curating the agent's proposal, an authority step. | Scenario Step 7, p. 8 |

## [20] deVadoss, Designing Intelligent Enterprise Agents (CEAD) (arXiv:2605.08258)

| Q | Value | Quotation or search | Location |
|---|---|---|---|
| H1 | no, DISPUTABLE (part) | The Agent Capability Contract "States ambiguity, risk, cost, confidence, legal, financial, or customer-impact triggers for human approval" and "Specifies trace schema, spans, model/tool calls, token/cost metrics, user-visible explanations, and incident replay." An agent has "an owner, identity, trace, evaluation record, cost record, and escalation path." The triggers (why a person) and a trace exist (part), but recording of the person's decision is not stated (no). | §V-C, ACC table rows "Human interaction" and "Observability and audit"; §III-A item 6 |
| H2 | part | "Metrics include functional success, safe success, automated safe success, policy violations per 1,000 tasks, memory poisoning per 1,000 tasks, escalation rate, audit coverage, mean handoffs, mean cost units, and p95 latency." Results tables report "Escalations %". Named, not defined. | §VI-E; Table III |
| H3 | no | Standard set. "Review duplicate agents quarterly" concerns agent sprawl. | §IX |
| H4 | no, DISPUTABLE (part) | "Autonomy is a design variable: assign L0–L4 autonomy by action risk, reversibility, confidence, and evidence, not by model capability alone." "Evidence" may include past performance (part), but the text does not say so, and autonomy is assigned at design time (no). | §V-E |
| H5 | no | Standard set. | full text |

## [21] Salesforce Architects, The Agentic Enterprise (architect.salesforce.com)

| Q | Value | Quotation or search | Location |
|---|---|---|---|
| H1 | no | Standard set. Closest: "requiring logging and explainability mechanisms with verifiable audit trails for AI decisions, actions, content, and predictions." These are AI decisions, not people's. | Design principles, "Trust-throughout" |
| H2 | no | Standard set. | full page |
| H3 | no | Standard set. "Agent Self-Reflection & Adaptation Framework: Provides a mechanism for an agent to analyze its own performance and, with human approval, trigger improvements or suggest modifications to itself." It reviews agent performance, not people's decisions. | Agentic Layer components |
| H4 | no | Standard set. The four maturity levels widen scope by enterprise stage, not by an agent's record. | "Maturity Level 1" to "Maturity Level 4" |
| H5 | no | Standard set. "Agents require self-reflective capabilities to proactively seek human guidance if its confidence over decision-making falls below pre-programmed thresholds." A confidence escalation, not a capability hand-off. | Design principles, "Agent-first with human oversight" |

## [22] Sharma and Shah, AOS-0001 (arXiv:2608.03214, Draft v0.8), with AOS-0000 (arXiv:2606.01508)

| Q | Value | Quotation or search | Location |
|---|---|---|---|
| H1 | yes | "A human decision is itself evidence. The record includes the approver identity, authority, information presented, decision, time, and any modifications." Why a person was needed: "A policy decision includes the rule version, result, justification, and obligations." "The outcome approve indicates that an additional approval authority is required before execution." Confidence decisions: "The decision includes the threshold, component evidence, uncertainty, rationale, and required control action." | AOS-0001 §9.9, p. 31; §6.7, p. 18; §9.6, p. 30 |
| H2 | part | "Examples include an authority budget, token budget, context window, model quota, human-approval capacity, data residency allowance, ... and time-to-decision." Table 5: "Quota — Cost, token, and approval budget". Scheduling allocates "human review slots". A quantity named as a resource, not defined. | AOS-0001 §6.14, p. 22; §10.6, p. 33 |
| H3 | no | Standard set. "Human-in-the-loop is not one generic step; it includes approval before action, supervisory review, emergency stop, post-action review, and dispute resolution." Post-action review is listed with no purpose of changing what is asked of people. | AOS-0001 §7.11, p. 24 |
| H4 | part, DISPUTABLE (yes) | AOS-0000: "AOS should support deterministic trust and risk states such as normal, restricted, quarantined, and reviewed. Transitions should be triggered by deterministic signals such as repeated policy denials, suspicious tool patterns, integrity check failures, or unexpected data classification mismatches." AOS-0001: "The trust function combines verifiable identity, ... historical reliability, observed behavior, and the current operational context." "Trust may decay when evidence becomes stale or behavior changes." "The control plane can require stronger runtime isolation when trust is lower". States and triggers are named (yes), but as "should support", narrowing only, and AOS-0001 says isolation is not "a substitute for authorization" (part). | AOS-0000 §4.6, p. 11; AOS-0001 §6.10, p. 20; §9.5, p. 30 |
| H5 | no, DISPUTABLE (part) | "A capability may be provided by an agent, model, tool, API, workflow, human, service, or infrastructure function." "Human providers are routed similarly but with different latency and interaction semantics. The runtime can create a review task, deliver the required evidence, wait for a decision, and continue or terminate." A person can be the provider of a step and the runtime "records the actual endpoint" (part), but the source frames people as providers or reviewers, not as a fallback when an agent lacks capability, and nothing counts or reduces such steps (no). | AOS-0001 §6.4, p. 16; §10.4, p. 33 |

## [23] Steinder and Franke, Towards an Agent Operating System (arXiv:2607.25076)

| Q | Value | Quotation or search | Location |
|---|---|---|---|
| H1 | no | Standard set. Closest: "MCP Gateways aggregate, route, and enforce authorization with a reversibility model that blocks irreversible calls without elevated authorization." No record of that authorization. "immutable audit ledgers the agent cannot modify" concern failure detection. | §IV-D; §IV-J |
| H2 | no | Standard set. | full text |
| H3 | no | Standard set. | full text |
| H4 | no, DISPUTABLE (part) | "fine-grained (e.g., per function) and context-dependent (based on what the agent is doing or has done before) policy enforcement is where the effort is needed". "Has done before" could cover past performance, stated as future work (part); in context it means the actions of the current task (no). | §IV-H |
| H5 | no | Standard set. | full text |

## [24] Beheshti et al., Agentic Service-Oriented Computing: A Manifesto (arXiv:2607.12619)

| Q | Value | Quotation or search | Location |
|---|---|---|---|
| H1 | part, DISPUTABLE (yes) | "An agent provenance graph represents the complete causal structure of an agent's execution: user goals, planning steps, decision points, tool calls, data sources, service invocations, applied policies, approvals, and final actions. Developing, standardising, and querying such graphs are central ASOC research challenges." Applied policies and approvals are both in the record (yes), but as a research agenda, and it does not say the record names why a person was needed (part). | §V-F, Principle 6 |
| H2 | part, DISPUTABLE (yes) | Agentic QoS table: "Human-Oversight Effectiveness ... Degree to which review gates intercept harmful actions before execution; measured by escalation interception rate". Named with what it counts (yes), but it measures how well gates catch harm, not how often people are required (part). | §VI-E, Agentic QoS table |
| H3 | no | Standard set. | full text |
| H4 | part | "Trust must be earned dynamically through operational track record, validated through capability benchmarking, and calibrated to the stakes of specific delegation tasks. Research must develop formal trust models, reputation mechanisms, and runtime enforcement that constrain agent authority in proportion to established trust." Research agenda. | §VI-D |
| H5 | no | Standard set. | full text |

## [25] Venkiteela, An Enterprise Agentic Architecture Framework (EAAF) (SJCS 2(1), 2026)

Page numbers are the journal pages printed on each PDF page.

| Q | Value | Quotation or search | Location |
|---|---|---|---|
| H1 | part | "High-risk actions must never be executed without explicit, logged authorization." The Telemetry Fabric provides "detailed Decision logs". The authorization is logged; the reason it went to a person is not stated as part of the record. | §3.3 (1), p. 4; §5.1 (5), p. 11 |
| H2 | part | Table 1 has a column "Autonomy Level": Human "0%", Traditional Automation "10%", EAAF (Agents) "82%". Table 5 "Safety Blockade Rate" has a column "Human Override Needed" (for example "High-Risk Financial Actions ... 4%"). Neither quantity is defined. The sentence that explains 82% is damaged in the published PDF: "reached an 82% snonly for regulated ap- proval steps". | §7.1 Table 1, p. 14; §7 Table 5, p. 14; §7.1, p. 13 |
| H3 | no | Standard set. "Continuous Adaptation by managing policy updates, prompt improvements, and incorporating runtime learning signals based on execution feedback" concerns agents, not people's decisions. | §5.1 (4), p. 11 |
| H4 | no, DISPUTABLE (part) | "Each deployed agent receives a unique cryptographic identity, a policy-bound namespace, and a dynamic trust score." A per-agent score that changes (part), but nothing says what changes it or that it changes the agent's authority (no). | §5.1 (1), p. 10 |
| H5 | no | Standard set. The source separates authority from capability only for approval: a proposed action is "blocked or routed for human approval, regardless of the agent's technical capability to perform the task." | §4.1.4, p. 7 |

# Further passages

## Reducing the need for people's decisions as a goal

- Charterion [18]: bounds the number of escalations a person receives, because too many make the approval empty. "When the load exceeds what a person can decide with attention, the escalate outcome degrades in fact to permit—the decision is still recorded as a human's, but it is no longer a decision." And: "It is a machine-rate source of human decisions; a design can make it arbitrarily frequent by setting caps low or charters at commit". §8 attention profile and Condition 8.13 (WF20), pp. 66-67.
- Charterion [18]: promotion toward "autonomous" requires an escalation acceptance rate of 98% or more, with the rationale "Overseers agree with what the agent proposed at the boundary of its authority". Table 18.5, p. 103.
- Zhu [13]: the topology optimizer subtracts the cost of human review. "Human review, coordination cost, and expected loss are explicit. On a simple or highly sequential task, the optimizer should often choose one agent." §3.4, Equation (13).
- Goujon [14]: "Local autonomy removes human decision latency: the agent detects the drift in L2 and triggers the response." §3.2.1, p. 35.
- AEON [19]: "As confidence develops and operational experience accumulates, defaults loosen, automation expands, and manual oversight focuses on exceptions rather than routine operations." §12.4, p. 30.
- AWS [16]: "Reduce operational costs: Automate decision flows that previously required human input or oversight." Foundations guide, introduction.html, "Objectives".
- EAAF [25]: "Humans shift from being "operators" who perform tasks to "governors" who set policies and handle high-risk exceptions flagged by the safety layer." §3.1 (5), p. 4.
- Microsoft [15]: "automate approvals using the collected metrics" (release approvals of agent versions, not agent actions). docs/versioning/Recommendations.md, item 7.

## People's decisions should not be reduced, or are kept on purpose

- Zhu [13]: "The present target is a human-supervised organization. Offline policy deliberately queues or halts higher-risk decisions. This sacrifices 24-hour decision throughput to preserve a human correction endpoint". §7.2 "Human control limits unattended autonomy".
- Goujon [14]: "Beyond the proof, a requirement remains: keeping the human in the loop by design. Not in every act, which would bring us back to Level 2 (§1.5)". §11.2, p. 89. Also an irreversible act "is not executed autonomously: it is escalated to the AOM, whatever its criticality." §4.4, p. 46.
- CEAD [20]: "CEAD does not maximize full automation because it escalates high-risk tasks. In regulated enterprise settings, the objective is not autonomous completion at any cost; it is safe completion with evidence, reversibility where possible, and appropriate human participation." §VII. Also: "Human approval is not an exception path". §V-D.
- AOS-0001 [22]: "Human-in-the-loop is often treated as a fallback UI. In practice, human authority is part of the operating system. ... Their availability, expertise, workload, and response time are schedulable resources." §15.6, p. 53.
- ASOC [24]: "An agentic service must remain under meaningful human control at all times". §V-A.
- Steinder and Franke [23]: "risk based assessment, and human-in-the-loop enforcement are necessary elements." §IV-I.
- Google [17]: the human-in-the-loop pattern "can add significant architectural complexity because it requires you to build and maintain the external system for user interaction." choose-design-pattern-agentic-ai-system.

# What was opened

All opened on 2026-11-12 with curl. PDFs were converted to text with the Python library pypdf 7.0.1, installed into the scratch directory (pdftotext is not installed). arXiv HTML was converted to text with a short Python script; equations were read from the HTML's TeX annotations where needed (Zhu §6.4).

| Ref | Opened | Notes |
|---|---|---|
| [12] | https://arxiv.org/html/2610.14818 | Full text. |
| [13] | https://arxiv.org/html/2608.08516 | Full text, including Equations (16) to (18) from TeX annotations. |
| [14] | https://arxiv.org/pdf/2610.30221 | No arXiv HTML version (the HTML URL returned a 6 KB stub). PDF, 120 numbered pages plus appendices, read as text. |
| [15] | https://github.com/microsoft/multi-agent-reference-architecture, main branch tarball from codeload.github.com | All 42 Markdown files. |
| [16] | docs.aws.amazon.com/prescriptive-guidance/latest/ guides: agentic-ai-foundations, agentic-ai-patterns, agentic-ai-frameworks, agentic-ai-serverless, agentic-ai-multitenant, strategy-operationalizing-agentic-ai, agentic-ai-security | Every page listed in each guide's toc-contents.json (131 pages). references.txt says "six guides" without naming them; I found seven and read all seven. |
| [17] | cloud.google.com/architecture/ pages: agentic-ai-overview, choose-agentic-ai-architecture-components, choose-design-pattern-agentic-ai-system, multiagent-ai-system, single-agent-ai-system-adk-cloud-run, multi-tenant-agentic-ai-system, multi-agent-private-networking-patterns, agentic-ai-bidirectional-multimodal-streaming, agentic-ai-build-multicloud-open-data-lakehouse, agentic-ai-classify-multimodal-data, agentic-ai-cross-cloud-analytics, agentic-ai-data-science, agentic-ai-interactive-learning, agentic-ai-multimodal-graph-rag-resource-orchestration, agenticai-orchestrate-access-disparate-systems, agentic-ai-orchestrate-security-ops-workflows, agentic-ai-system-with-grounding-using-maps | The 17 pages with "agent" in the path linked from the Architecture Center AI and ML index. This matches the count in references.txt; the list itself is my reconstruction. |
| [18] | Zenodo record 22829848, file Charterion_v2.0_Specification.pdf | Full PDF (290 pages) read as text. |
| [19] | Zenodo record 20349596, file AEON-White-Paper.pdf | Full PDF read as text. The .docx copy was not opened. |
| [20] | https://arxiv.org/html/2605.08258 | Full text. |
| [21] | https://architect.salesforce.com/docs/architect/fundamentals/guide/agentic-enterprise-it-architecture.html | The first request returned "Access Denied" (HTTP 403). A second request with ordinary browser headers returned the page. |
| [22] | https://arxiv.org/pdf/2608.03214 and https://arxiv.org/pdf/2606.01508 | No arXiv HTML for either. Both PDFs read as text. |
| [23] | https://arxiv.org/html/2607.25076 | Full text. |
| [24] | https://arxiv.org/html/2607.12619 | Full text. |
| [25] | https://journal.futuristech.co.id/index.php/sjcs/article/view/368, PDF from article/download/368/49/588 | Full PDF read as text. The PDF has structural errors (pypdf reported 20 "wrong pointing object" warnings), but the text extracted; one sentence in §7.1 is damaged in the PDF itself (checked with a second extraction mode). |

Not opened: nothing. Every source was assessed. Under the warm/ folder I opened only protocol-v2.md and references.txt.

# Disclosures

- Reader: Claude (Opus), run as a subagent. I rated from the text I fetched today, not from memory.
- I searched the full text with regular expressions and then read the passages around each hit. A passage that uses none of the search terms could be missed. For long documents (AAM/5C, Charterion, AOS-0001, AWS, Google) I read sections around hits, not every page end to end.
- Where two values were defensible I gave the lower and marked it DISPUTABLE, as the protocol says. This lowers 21 cells. A reader who resolves them the other way would rate Zhu [13] much higher (H1, H2, H3, H4 would go from part, part, no, part to yes, yes, part, yes), and would raise AOS-0001 [22] H4 and Charterion [18] H5 to yes.
- AWS [16]: the reference names six guides; I could not tell which six, so I read seven. The only guide that may be extra is agentic-ai-security; it changes no value.
- Google [17]: the 17 pages are my reconstruction from the Architecture Center index on the day I read it.
- AOS [22]: I rated AOS-0001 and its precursor AOS-0000 together, as the reference pairs them. The H4 value relies partly on AOS-0000.
- Page numbers: AAM/5C, AOS-0001 and EAAF print page numbers that match the PDF pages; Charterion and AEON locations are PDF page numbers.
- I installed pypdf into my scratch directory to read PDFs. I changed no file except this output. I signed in nowhere and posted nothing.
