---
title: "Second rater: five mappings of fourteen published models onto WARM v0.12"
date: 2026-11-11
author: second rater (subagent)
yardstick: warm-model-v0.12.md, Steps 0 to 4 and the glossary
---

# Second rater: five mappings of fourteen published models onto WARM v0.12

## Summary

- 126 inventory items were sampled, 9 from each of the 14 sources: 3 the mapper marked clean, 3 strained or span, 3 misfit, guidance or out of scope.
- I agreed with the mapper on 107, disagreed on 8 and found 3 unclear. 8 more differ only because v0.12 added a part (grants in Policy, the Lifecycle service, the accountable person in Identity, assessment as an input to Policy). Agreement, leaving out the v0.12 rows, is 107 of 118 (91%).
- By the mapper's category: clean 39 of 42 (93%), strained or span 36 of 41 (88%), misfit, guidance or out of scope 32 of 35 (91%). Unlike the earlier platform second rating, not every clean row held: 1 disagreement and 2 unclear rows were marked clean.
- No disagreement reverses a finding. Most are about where an item's weight falls inside a span, or about a convention (whether a pattern is guidance, whether a connector to one enterprise system is a domain tool).
- Part 2: (a) Charterion's identity belongs to an agent type, not to each individual agent, and the section that says so is 8.12, not 8.11. (b) AEON's registry records the providing subdomain, not who is accountable, and states no rule of one provider per capability. (c) AOS's identity-versus-instance split is WARM's agent-versus-instance distinction, not persistent versus task agent. (d) All three lifecycle parts create and end agents. Only AOS suspends and resumes them, and none states that it keeps a list of agents.

## Method

**What I read first.** `warm-model-v0.12.md`, Steps 0 to 5 (lines 1 to 447) and the glossary (lines 642 to 671). I did not read "Compared with published models", "What WARM adds, and its limits", "Changes from v0.11", `synthesis.md`, `synthesis-round2.md` or `predictions.md` before Parts 1 and 2 were recorded. See "Limits" for one incidental exposure during Part 2.

**Sampling.** A script parsed every inventory table of the five mapping files into rows, keeping each row's mapper category. Category groups: clean; strained or span; misfit, guidance or out of scope. The groups excluded rows marked "planned" (already in the v0.12 change list), "folded" (not counted by the mapper), rows with no category (the reverse-direction tables), and a few rows whose cells contained a literal `|` that the parser could not split. In each group, rows were taken in table order and picked at the 1/6, 1/2 and 5/6 positions, so no pick is a first row. If the strained-or-span picks held no strained row, or the third group's picks held no misfit row, the middle pick was replaced by the median strained or misfit row. Every source had at least 3 rows in every group, so every source has 9 items.

**Blind assignment.** The script printed each sampled item's ID, name and quoted definition with the assignment, category and reason columns removed. I wrote all 126 assignments to a file before printing the mapper's columns. Where a definition was too thin (AOS 7.12, Steinder and Franke's Lessons 2 and 4, EAAF's Human-Centric Oversight, ASOC's figure labels), I read the passage in the primary source first. Five verdicts were checked against a primary after the reveal, to settle a disagreement, not to change my assignment: Zhu Table 5, Charterion ABB-L5-1 and ABB-G-1, AOS §8.7, and the v0.11 text.

**Verdict rule.** *Agree*: the same part, or spans whose main parts agree and whose category group (one part, span, guidance or misfit) is compatible. A span that adds or drops a minor part still counts as agreement. *Disagree*: a different main part, or a different kind of answer (a running part versus guidance; a span versus a misfit). *Unclear*: the evidence supports both readings. *Differs because of v0.12*: my assignment uses a part that v0.12 added and v0.11 lacked.

**Primary sources opened** (downloaded on 2026-11-11 into the scratchpad and converted to text): AOS-0001 (arXiv 2608.03214, 72 pp.) and AOS-0000 (2606.01508); Steinder and Franke (arXiv HTML 2607.25076); ASOC (arXiv HTML 2607.12619); EAAF (journal PDF, 17 pp.); Charterion v2.0 (Zenodo 22829848, 290 pp.); AEON (Zenodo 20349596, 49 pp.); Zhu (arXiv 2608.08516, a local copy already in the scratchpad). Page numbers below are PDF pages; Charterion's printed page is the PDF page minus 24.

## Part 1. Sampled items

Item IDs are `<source>-<n>`; picks 1 to 3 are the mapper's clean rows, 4 to 6 strained or span, 7 to 9 misfit, guidance or out of scope. "Source row" gives the mapper's row ID and its line in the mapping file. Long mapper assignments are cut at about 140 characters.

| # | Source row | Item | Mapper category | Mapper assignment | Second rater | Verdict | Reason |
|---|---|---|---|---|---|---|---|
| Yu-1 | NC06 (mapping-yu-zhu.md:98) | Multi-channel interaction surface | clean | Channels | Channels | agree | Same service. |
| Yu-2 | NC33 (mapping-yu-zhu.md:125) | Action audit and provenance | clean | Observability | Observability | agree | Same service. |
| Yu-3 | VP7 (mapping-yu-zhu.md:148) | Multi-turn or resumable sessions | clean | Sessions | Sessions | agree | Same service. |
| Yu-4 | L6 (mapping-yu-zhu.md:62) | Tool & Action Runtime (Act) | span | Tools + Registry + Policy + Secrets + Approvals + Environments + Observability | Span: Tools + Policy + Observability (+ Registry to resolve) | agree | Both a span centered on Tools, Policy and Observability; the mapper names four more services at the point of action. |
| Yu-5 | NC27 (mapping-yu-zhu.md:119) | Tool and skill invocation | strained | Tools | Tools | agree | Same service; the mapper's note on the clash over "skill" is right. |
| Yu-6 | VP1 (mapping-yu-zhu.md:142) | Multiple collaborating agents | span | Orchestration + Messaging + Registry | Span: Orchestration + Messaging + Registry | agree | Same three services. |
| Yu-7 | NC13 (mapping-yu-zhu.md:105) | Task decomposition and planning | misfit | — | Out of scope (single-agent reasoning) | agree | Both out of scope as single-agent reasoning. |
| Yu-8 | VP15 (mapping-yu-zhu.md:156) | Direct synchronous interaction sufficient | guidance | Choice of mechanism | Design-time guidance | agree | Both a design choice, not a running part. |
| Yu-9 | R7 (mapping-yu-zhu.md:168) | How to apply the architecture | guidance | Builder procedure | Design-time guidance | agree | Both a builder method. |
| Zhu-1 | B15 (mapping-yu-zhu.md:258) | Permission | clean | Policy | Policy | agree | Same service. |
| Zhu-2 | B41 (mapping-yu-zhu.md:299) | Task HALT | clean | Tasks | Span: Tasks + Policy | disagree | The item is the separate authority to halt, not the cancellation; Tasks alone does not carry who may halt (Policy, and v0.12 point 4), so I would not call it clean. |
| Zhu-3 | B66 (mapping-yu-zhu.md:334) | Per-task metering | clean | Observability | Observability | agree | Same service. |
| Zhu-4 | B11 (mapping-yu-zhu.md:249) | Knowledge store K | span | Memory + Registry (skills) + Retrieval | Span: Memory + Registry (skills) + Retrieval (+ Releases) | agree | Same span. |
| Zhu-5 | B40 (mapping-yu-zhu.md:298) | FLAG | strained | Evaluation | Span: Observability + Evaluation | agree | Both put the item on Evaluation; I add Observability for the evidence pointer. |
| Zhu-6 | B63 (mapping-yu-zhu.md:331) | Decision classes | span | Policy + Approvals | Span: Releases + Approvals | disagree | Zhu's Table 5 classes are classes of change authority with rollback requirements ("Change authority is calibrated on two axes"), so Releases belongs in the span; the mapper has Policy + Approvals. |
| Zhu-7 | B26 (mapping-yu-zhu.md:274) | Net-utility selection objective | guidance | Design guidance | Design-time guidance | agree | Both design guidance. |
| Zhu-8 | B35 (mapping-yu-zhu.md:293) | Role Group (the concept) | misfit | — | Misfit | agree | Both misfit; authority categories across domains. |
| Zhu-9 | B72 (mapping-yu-zhu.md:340) | Logical before physical separation | guidance | Deployment guidance | Design-time guidance | agree | Both deployment or design guidance. |
| AAM5C-1 | 45 (mapping-aam5c.md:121) | Decision step (L6) | clean | Service: Policy | Policy | agree | Same service. |
| AAM5C-2 | 71 (mapping-aam5c.md:147) | Trace reconciliation (instrument for H7b and H8b) | clean | Service: Evaluation | Span: Observability + Evaluation | agree | Both Evaluation as the holder; I add Observability for the records it reads. |
| AAM5C-3 | 124 (mapping-aam5c.md:200) | Control stakeholders (business owner, CISO, data protection officer, internal audit) | clean | Layer: People | People layer | agree | Same layer. |
| AAM5C-4 | 20 (mapping-aam5c.md:96) | Infrastructure agents and L7 components (autonomous provisioner, energy sobriety agent, ha | strained | Agent concept: role | Span: Infrastructure + Reliability + Observability | unclear | Depends on whether AAM/5C's L7 is the agent system's own infrastructure or the managed estate's; the mapper reads it as roles in an IT-operations domain, I read it as platform infrastructure care. The quoted definition does not settle it. |
| AAM5C-5 | 64 (mapping-aam5c.md:140) | Cognitive Zero Trust / Zero Trust agent | span | SPAN: Evaluation + Policy | Span: Policy + Evaluation | agree | Same span. |
| AAM5C-6 | 100 (mapping-aam5c.md:176) | Model registry and attestation of the served model | strained | Service: Models | Span: Models + Observability (open question on running config) | agree | Both Models as the holder, with attestation unowned. |
| AAM5C-7 | 36 (mapping-aam5c.md:112) | Autonomic patterns (self-configuration/optimization, self-healing/protection, self-explana | guidance | Guidance: builder guidance (domain work of IT operations) | Design-time guidance | agree | Both guidance. |
| AAM5C-8 | 53 (mapping-aam5c.md:129) | Capability envelope | misfit | MISFIT: none (closest: Policy) | Policy (grant) | differs because of v0.12 | v0.12 adds grants to Policy, which places the envelope; the mapper's remaining point (acting while the decider is down) is still unowned in v0.12. |
| AAM5C-9 | 145 (mapping-aam5c.md:221) | Governance by design | guidance | Guidance: design principle | Design-time guidance | agree | Both guidance restating WARM's enforcement-point condition. |
| Microsoft-1 | A42 (mapping-vendors.md:124) | Long-term memory (LTM) | clean | Memory | Memory | agree | Same service. |
| Microsoft-2 | A77 (mapping-vendors.md:159) | Code-based evaluation; LLM-as-a-judge | clean | Evaluation | Evaluation | agree | Same service. |
| Microsoft-3 | A134 (mapping-vendors.md:216) | Tool Adapters | clean | Tools | Tools | agree | Same service. |
| Microsoft-4 | A25 (mapping-vendors.md:107) | Monitor component | span | Span: Registry (keep entries current) + Reliability (uptime) | Span: Observability + Reliability | agree | Both a span with Reliability; we differ on the second part (Registry versus Observability). |
| Microsoft-5 | A46 (mapping-vendors.md:128) | Procedural memory | strained | Memory | Span: Memory + Registry (skills) | agree | Both rest on Memory and note that learned procedures sit between Memory and the Registry. |
| Microsoft-6 | A122 (mapping-vendors.md:204) | User Application | span | Span: Channels + Identity + Sessions | Span: Channels + Identity + Sessions (+ Memory) | agree | Same span. |
| Microsoft-7 | A12 (mapping-vendors.md:94) | Modular monolith (design option) | guidance | Guidance (Infrastructure, Releases) | Design-time guidance | agree | Both guidance. |
| Microsoft-8 | A93 (mapping-vendors.md:175) | Manual override (pause or disable an agent class) | misfit | **Misfit** | Lifecycle | differs because of v0.12 | v0.12's Lifecycle suspends a running agent; note the item acts on an agent class, which Lifecycle as written (per agent) does not quite cover. |
| Microsoft-9 | A144 (mapping-vendors.md:226) | Pattern 2: Dynamic Agent Registry (service mesh for agents) | guidance | Guidance (Registry, Identity, Secrets, Evaluation, Releases) | Span: Registry + Identity + Lifecycle (+ Releases gate) | differs because of v0.12 | I accept the mapper's convention that a pattern is guidance; its parts would now include Lifecycle, since provisioning is Lifecycle's industry term in v0.12. |
| AWS-1 | B028 (mapping-vendors.md:405) | Agent-to-system protocols | clean | Tools | Tools | agree | Same service. |
| AWS-2 | B067 (mapping-vendors.md:444) | API activity audit (CloudTrail, as component) | clean | Observability | Observability | agree | Same service. |
| AWS-3 | B151 (mapping-vendors.md:552) | Framework capability: tool integration (1) | clean | Tools | Tools | agree | Same service. |
| AWS-4 | B042 (mapping-vendors.md:419) | Authentication context propagation | span | Span: Identity + Secrets | Identity | agree | Same principal part; the mapper adds Secrets for the token. |
| AWS-5 | B094 (mapping-vendors.md:478) | Specialized role classes (decision, knowledge, execution agents) | strained | Agent concept (role) | Agent concept: Role (strained) | agree | Same agent concept, strained. |
| AWS-6 | B164 (mapping-vendors.md:565) | AgentCore capabilities: Runtime, Memory, Gateway, Identity, built-in tools, Observability  | span | Runtime → Harness+Environments+Sessions (span); Memory → Sessions+Memory (span); Gateway → Tools+Registry (span); Identity → Identity (cl... | Span: Harness + Environments + Memory + Tools + Identity + Observability | agree | Same span (the mapper splits it into six sub-assignments). |
| AWS-7 | B025 (mapping-vendors.md:402) | Citizen-developer (no-code) agent creation | guidance | Guidance (builder tooling) | Design-time guidance (builder tooling) | agree | Both builder tooling. |
| AWS-8 | B140 (mapping-vendors.md:536) | Beliefs and intentions; perceive, reason, act loop (5) | misfit | **Misfit** (out of scope) | Out of scope (single-agent reasoning) | agree | Both out of scope. |
| AWS-9 | B176 (mapping-vendors.md:577) | MCP deployment models: local stdio, local SSE, remote streamable HTTP (3) | guidance | Guidance (Tools, Infrastructure) | Design-time guidance | agree | Both guidance. |
| Google-1 | C019 (mapping-vendors.md:773) | API management: prebuilt connectors | clean | Tools | Tools | agree | Same service. |
| Google-2 | C082 (mapping-vendors.md:836) | Continuous evaluation | clean | Evaluation | Evaluation | agree | Same service. |
| Google-3 | C121 (mapping-vendors.md:875) | Per-role model selection | clean | Models | Models | agree | Same service. |
| Google-4 | C030 (mapping-vendors.md:784) | Graph-based workflows | span | Span: Orchestration + Approvals | Span: Orchestration + Approvals + Sessions | agree | Same span; I add Sessions for checkpoints. |
| Google-5 | C070 (mapping-vendors.md:824) | Use case: research assistant (planner, researcher, evaluator, report composer agents) | strained | Domains layer | Design-time guidance | disagree | A use-case example in vendor guidance is an illustration, not a domain of a running system; the mapper places it in the Domains layer. |
| Google-6 | C118 (mapping-vendors.md:872) | Third-party MCP servers | span | Span: Tools + Providers | Providers | agree | Both rest on Providers. |
| Google-7 | C027 (mapping-vendors.md:781) | External state management | guidance | Guidance (Sessions) | Sessions | agree | The mapper files a recommended practice as guidance naming Sessions; I named Sessions. Same part, convention differs. |
| Google-8 | C051 (mapping-vendors.md:805) | Coordinator pattern | guidance | Guidance (Orchestration) | Orchestration | agree | As Google-7, for Orchestration. |
| Google-9 | C120 (mapping-vendors.md:874) | Prompt caching | misfit | **Misfit** | Design-time guidance (cost technique; no WARM owner) | agree | Both say no WARM part owns caching; the mapper calls it misfit, I called it guidance. |
| Charterion-1 | A42 (mapping-round2-charters.md:118) | L5-1 Runtime Node | clean | Infrastructure layer | Span: Environments + Harness | unclear | Charterion maps the node to ArchiMate Node and System Software (Infrastructure), but "the halt, zone and telemetry facts attach to it", which reads as an isolated place an agent acts (Environments). Not a clean fit either way. |
| Charterion-2 | A46 (mapping-round2-charters.md:122) | L5-5 Policy Decision Point | clean | Policy | Policy | agree | Same service. |
| Charterion-3 | A50 (mapping-round2-charters.md:126) | L5-9 Telemetry Sink | clean | Observability | Observability | agree | Same service. |
| Charterion-4 | A15 (mapping-round2-charters.md:86) | Envelope facet | span | Span: Policy, Approvals | Policy | agree | Policy with escalation to Approvals in both. |
| Charterion-5 | A54 (mapping-round2-charters.md:130) | G-1 Lifecycle Gate | span | Span: Releases, Approvals, Policy | Span: Lifecycle + Releases + Approvals | differs because of v0.12 | The gate's states (Proposed to Retired) are "attribute state on charterion:Charter"; v0.12's Lifecycle now carries creating and retiring an agent, beside Releases and Approvals. |
| Charterion-6 | A88 (mapping-round2-charters.md:174) | WF3 Justified provisioning | strained | Policy (least privilege; WARM has no derivation) | Policy (strained) | agree | Same service, strained. |
| Charterion-7 | A16 (mapping-round2-charters.md:87) | Coordination facet | misfit | No WARM part records locks or intents on shared resources. Orchestration tracks assignments, not contention over resources | Span: Orchestration + Directory + Tasks | disagree | Ownership and an accountable unit are what the Directory records, and commitments are Orchestration; only locks and intents on shared resources lack a part. A span with a gap, not a misfit. |
| Charterion-8 | A72 (mapping-round2-charters.md:153) | Boundary Review | misfit | As A9 | Out of scope (several organizations) | agree | Both outside WARM because it concerns two organizations. |
| Charterion-9 | A94 (mapping-round2-charters.md:180) | WF9 Escalation reachability | misfit | No WARM requirement that an approval reach a current, available person | Span: Identity + Approvals | differs because of v0.12 | v0.12 adds the accountable person to Identity and the open question on approver availability and load; the requirement itself is still only an open question. |
| AEON-1 | B4 (mapping-round2-charters.md:273) | Evidence plane | clean | Observability | Observability | agree | Same service. |
| AEON-2 | B22 (mapping-round2-charters.md:291) | Cross-subdomain forensics | clean | Observability | Observability | agree | Same service. |
| AEON-3 | B36 (mapping-round2-charters.md:305) | Runtime observability | clean | Observability | Span: Observability + Reliability | agree | Both Observability; I add Reliability for health state. |
| AEON-4 | B13 (mapping-round2-charters.md:282) | Identity plane subdomain contract | strained | Identity contract (WARM specifies none) | Identity (strained) | agree | Both Identity, strained (no service contracts in WARM). |
| AEON-5 | B32 (mapping-round2-charters.md:301) | Composition patterns (6) | strained | Orchestration (compensating relates to V14) | Orchestration | agree | Same service. |
| AEON-6 | B53 (mapping-round2-charters.md:322) | Cybersecurity | span | Span: Domains layer, Policy (guardrails) | Domain layer (a security domain) | agree | Both a domain plus Policy. |
| AEON-7 | B41 (mapping-round2-charters.md:310) | Architecture-as-code | guidance | Design-time guidance (and Releases) | Design-time guidance (practice, uses Releases) | agree | Both guidance. |
| AEON-8 | B44 (mapping-round2-charters.md:313) | Cross-domain composition | misfit | As B43 | Policy (strained) | disagree | A rule that a workflow may not carry data from a higher classification to a lower is a Policy rule on what may enter and leave; the mapper files it as a misfit by reference to federated instances (B43), which is a different item. |
| AEON-9 | B47 (mapping-round2-charters.md:316) | Minimal coherent subset and phases 0-3 | guidance | Design-time guidance (one row) | Design-time guidance (adoption) | agree | Both adoption guidance. |
| CEAD-1 | C17 (mapping-round2-charters.md:380) | ACC: Model behavior policy | clean | Models | Span: Domain rules + Models (+ Policy) | agree | Both Models (Step 4 sends a model preference to Models). |
| CEAD-2 | C21 (mapping-round2-charters.md:384) | ACC: Observability and audit | clean | Observability | Observability | agree | Same service. |
| CEAD-3 | C25 (mapping-round2-charters.md:388) | Versioning (SOA discipline) | clean | Releases | Releases | agree | Same service. |
| CEAD-4 | C5 (mapping-round2-charters.md:368) | Agent Runtime Plane | span | Span: Harness, Orchestration, Memory, Retrieval, Evaluation, Approvals | Span: Harness + Orchestration + Memory + Retrieval + Evaluation + Tools + Approvals | agree | Same span (I add Tools). |
| CEAD-5 | C11 (mapping-round2-charters.md:374) | ACC: Autonomy level | strained | Domain rules | Span: Domain rules + Policy + Approvals | agree | Both rest on domain rules. |
| CEAD-6 | C19 (mapping-round2-charters.md:382) | ACC: Human interaction | strained | Domain rules (which actions need approval) | Span: Domain rules + Approvals | agree | Both domain rules on approval. |
| CEAD-7 | C28 (mapping-round2-charters.md:391) | Runtime pattern: verifier or challenger agents | guidance | Design-time guidance | Design-time guidance | agree | Both guidance. |
| CEAD-8 | C2 (mapping-round2-charters.md:365) | Autonomy levels L0-L4 | misfit | No WARM vocabulary of autonomy levels | Misfit | agree | Both misfit (no autonomy-level vocabulary). |
| CEAD-9 | C43 (mapping-round2-charters.md:406) | Micro-agent proliferation (anti-pattern) | guidance | Guidance | Design-time guidance | agree | Both guidance. |
| Salesforce-1 | D15 (mapping-round2-charters.md:465) | Omnichannel Experiences | clean | Channels | Channels (strained; + Sessions) | agree | Same service. |
| Salesforce-2 | D30 (mapping-round2-charters.md:480) | Model Gateway | clean | Models | Models | agree | Same service. |
| Salesforce-3 | D80 (mapping-round2-charters.md:530) | Agent Protocol Gateway | clean | Tools | Tools (+ Registry discovery) | agree | Same service. |
| Salesforce-4 | D11 (mapping-round2-charters.md:456) | Security and Governance Layer | span | Span: Identity, Policy, Evaluation | Span: Identity + Policy + Observability | agree | Same span core (Identity, Policy); we differ on the third part. |
| Salesforce-5 | D43 (mapping-round2-charters.md:493) | Modular Application Services | strained | Tools | Domain tools (reached through Tools) | disagree | Enterprise application services published as actions are connectors to particular systems, which WARM's placement test makes domain tools carried by Tools; the platforms mapper placed EAAF's adapters that way, this mapper placed these in Tools. |
| Salesforce-6 | D77 (mapping-round2-charters.md:527) | Adaptive API Management and Service Mesh | strained | Tools | Span: Tools + Registry + Policy | disagree | "Register, discover and govern" is three responsibilities (Tools, Registry, Policy); a strained one-part fit understates it. |
| Salesforce-7 | D42 (mapping-round2-charters.md:492) | Digital Twin Process Modeling | misfit | No WARM part | Misfit | agree | Both misfit. |
| Salesforce-8 | D64 (mapping-round2-charters.md:514) | Adaptive Data Quality Service | misfit | Outside WARM | Misfit (enterprise data platform) | agree | Both outside WARM. |
| Salesforce-9 | D105 (mapping-round2-charters.md:553) | Level 1: Information Retrieval Agents | guidance | (guidance; no assignment column) | Design-time guidance (maturity level) | agree | Both guidance (maturity level). |
| AOS-1 | A06 (mapping-round2-platforms.md:72) | Infrastructure | clean | Infrastructure | Infrastructure layer | agree | Same layer. |
| AOS-2 | A29 (mapping-round2-platforms.md:114) | Execution | clean | Tasks | Tasks | agree | Same service. |
| AOS-3 | A45 (mapping-round2-platforms.md:137) | Actor (glossary) | clean | Identity ("each agent, person and service") | Identity (strained) | agree | Same service. |
| AOS-4 | A08 (mapping-round2-platforms.md:79) | Capability discovery | span | Span: Registry (lookup), Policy (hard constraints), Models (choose among providers by fit, cost, latency). AOS ranks agents, models, tool... | Span: Registry + Models/Orchestration (selection) | agree | Same span core (Registry, Models). |
| AOS-5 | A13 (mapping-round2-platforms.md:84) | Human oversight | strained | Approvals. Strained: "stop" is V3; clarification, exception handling and appeal are wider than "hold chosen actions until a person author... | Span: Approvals + Directory + Lifecycle | agree | Both rest on Approvals with Directory and stop noted. |
| AOS-6 | A59 (mapping-round2-platforms.md:162) | Context and Memory Management (§4.4) | span | Span: Harness, Memory, Retrieval, Sessions and Observability. Close to WARM's "Where what an agent knows is kept" | Span: Harness + Memory + Retrieval + Sessions | agree | Same span. |
| AOS-7 | A35 (mapping-round2-platforms.md:127) | Four states and reconciliation | guidance | Design-time guidance | Misfit | disagree | §8.7 describes run-time controllers that "reconcile these states" and "may cancel, isolate, or escalate", which is a running mechanism with no WARM owner, not design guidance. |
| AOS-8 | A14 (mapping-round2-platforms.md:90) | Agent lifecycle | misfit | No WARM service owns the existence of an agent. Pieces sit in Identity (who), V3 (suspend, revoke), Sessions (pause, resume), Tasks (a un... | Lifecycle | differs because of v0.12 | v0.12's Lifecycle was added from this item. |
| AOS-9 | A57 (mapping-round2-platforms.md:154) | 7.12 "Economic and Physical Awareness" | guidance | Guidance; WARM's cost concern | Design-time guidance (principle; touches Scheduling, Models) | agree | Both guidance under WARM's cost concern. |
| SteinderFranke-1 | B05 (mapping-round2-platforms.md:266) | Perception (Inputs) | clean | Harness | Harness (strained) | agree | Same service. |
| SteinderFranke-2 | B12 (mapping-round2-platforms.md:273) | Agent memory | clean | Memory | Memory | agree | Same service. |
| SteinderFranke-3 | B25 (mapping-round2-platforms.md:286) | rossoctl "Observability" pillar | clean | Observability (failure attribution touches Evaluation) | Span: Observability + Evaluation | agree | Both Observability with Evaluation for attribution. |
| SteinderFranke-4 | B13 (mapping-round2-platforms.md:274) | Identity & AuthZ | span | Span: Identity, Policy (context-dependent grants are V1) | Span: Identity + Policy | agree | Same span. |
| SteinderFranke-5 | B21 (mapping-round2-platforms.md:282) | rossoctl "Networking" pillar | span | Span: Tools, Messaging (gateways for agents) | Span: Tools + Messaging + Policy | agree | Same span core (Tools, Messaging). |
| SteinderFranke-6 | B27 (mapping-round2-platforms.md:288) | AuthBridge | span | Span: Policy, Identity | Policy | agree | Both Policy (the mapper adds Identity for attestation). |
| SteinderFranke-7 | B06 (mapping-round2-platforms.md:267) | Agent lifecycle (primitive) | misfit | No WARM service owns creating and ending agents (as A14). The identity clause contradicts WARM Step 0 (section B.3 c) | Span: Lifecycle + Environments + Identity + Orchestration | differs because of v0.12 | Lifecycle now owns create and terminate; the mapper's second point (identity as a function of goal, skills, model) still contradicts WARM Step 0 after v0.12. |
| SteinderFranke-8 | B33 (mapping-round2-platforms.md:294) | Lesson 2, "Build on, not in replacement of, the prior layer" | guidance | Guidance | Design-time guidance | agree | Both guidance. |
| SteinderFranke-9 | B35 (mapping-round2-platforms.md:296) | Lesson 4, "Platform enforces what application code only requests" | guidance | Guidance; Governance point 1 | Design-time guidance | agree | Both guidance. |
| ASOC-1 | C22 (mapping-round2-platforms.md:403) | L3 Policy Enforcement | clean | Policy | Policy | agree | Same service. |
| ASOC-2 | C33 (mapping-round2-platforms.md:414) | L4 Memory | clean | Memory | Memory | agree | Same service. |
| ASOC-3 | C45 (mapping-round2-platforms.md:426) | L6 Databases | clean | Infrastructure | Providers (strained) | unclear | A figure label only ("Databases" in L6 Service and Tool Infrastructure); Infrastructure (storage) and Providers or Tools (systems agents call) are both readable. |
| ASOC-4 | C08 (mapping-round2-platforms.md:389) | L1 Goals | strained | Domain part: Goals. Strained: per delegation, not per area of work | Domain part: Goals | agree | Same domain part. |
| ASOC-5 | C32 (mapping-round2-platforms.md:413) | L4 Rationale Summaries | strained | Observability. Strained | Observability (strained) | agree | Same service, strained. |
| ASOC-6 | C48 (mapping-round2-platforms.md:429) | Security and Trust Plane | span | Span: Identity, Secrets, Policy; trust has no home (A27) | Span: Identity + Secrets + Policy | agree | Same span. |
| ASOC-7 | C14 (mapping-round2-platforms.md:395) | L1 Appeal Mechanisms | misfit | No WARM part. Appeal of a decision already made is neither approval nor stop | Misfit | agree | Both misfit (appeal). |
| ASOC-8 | C49 (mapping-round2-platforms.md:435) | Principle 1, Harnessability | guidance | Guidance | Design-time guidance | agree | Both guidance. |
| ASOC-9 | C56 (mapping-round2-platforms.md:447) | Reputation systems and trust calibration | misfit | Same family as A27 | Span: Evaluation + Policy | differs because of v0.12 | v0.12 lets Policy use an Evaluation assessment, which places trust-gated authority; a standing, decaying trust record per actor is still unowned. |
| EAAF-1 | D04 (mapping-round2-platforms.md:530) | Integration Adapters | clean | Domain part: Domain tools (WARM's placement test: a connector to one system is domain logic carried by Tools). EAAF places them in a plat... | Domain part: Domain tools | agree | Same domain part. |
| EAAF-2 | D12 (mapping-round2-platforms.md:538) | Audit & Traceability Service | clean | Observability | Observability | agree | Same service. |
| EAAF-3 | D27 (mapping-round2-platforms.md:553) | Policy & Compliance Engine (PCE) | clean | Policy | Policy | agree | Same service. |
| EAAF-4 | D08 (mapping-round2-platforms.md:534) | Human-in-the-Loop Interfaces | strained | Approvals. Strained: override is V3; co-planning is not approval | Span: Approvals + Channels + Orchestration (+ Lifecycle for override) | agree | Both rest on Approvals with override and co-planning noted. |
| EAAF-5 | D20 (mapping-round2-platforms.md:546) | Agent Types | strained | WARM roles (agent concept). Strained: "Task Agents" is a function, not a lifetime (term clash) | Agent concept (strained) | agree | Same agent concept, strained. |
| EAAF-6 | D28 (mapping-round2-platforms.md:554) | Compliance Agents | strained | WARM's provisional case: an agent providing a platform service (Policy, Observability). Agent concept, strained | Span: Evaluation + Policy (+ Lifecycle) | agree | Both the provisional case of an agent providing platform services. |
| EAAF-7 | D16 (mapping-round2-platforms.md:542) | Planning Engine | misfit | Out of scope (Step 0) | Out of scope (single-agent reasoning) | agree | Both out of scope. |
| EAAF-8 | D35 (mapping-round2-platforms.md:561) | Principle: Human-Centric Oversight | guidance | Guidance | Design-time guidance | agree | Both guidance. |
| EAAF-9 | D40 (mapping-round2-platforms.md:566) | ZeroOps | guidance | Guidance (People layer) | Design-time guidance | agree | Both guidance. |

## Agreement counts

| Source | Agree | Disagree | Unclear | Differs because of v0.12 | Agreement (excl. v0.12) |
|---|---|---|---|---|---|
| Yu | 9 | 0 | 0 | 0 | 9/9 |
| Zhu | 7 | 2 | 0 | 0 | 7/9 |
| AAM5C | 7 | 0 | 1 | 1 | 7/8 |
| Microsoft | 7 | 0 | 0 | 2 | 7/7 |
| AWS | 9 | 0 | 0 | 0 | 9/9 |
| Google | 8 | 1 | 0 | 0 | 8/9 |
| Charterion | 5 | 1 | 1 | 2 | 5/7 |
| AEON | 8 | 1 | 0 | 0 | 8/9 |
| CEAD | 9 | 0 | 0 | 0 | 9/9 |
| Salesforce | 7 | 2 | 0 | 0 | 7/9 |
| AOS | 7 | 1 | 0 | 1 | 7/8 |
| SteinderFranke | 8 | 0 | 0 | 1 | 8/8 |
| ASOC | 7 | 0 | 1 | 1 | 7/8 |
| EAAF | 9 | 0 | 0 | 0 | 9/9 |
| **Total** | **107** | **8** | **3** | **8** | **107/118 (91%)** |

| Mapper category | Items | Agree | Disagree | Unclear | Differs because of v0.12 | Agreement (excl. v0.12) |
|---|---|---|---|---|---|---|
| clean | 42 | 39 | 1 | 2 | 0 | 39/42 (93%) |
| strained/span | 42 | 36 | 4 | 1 | 1 | 36/41 (88%) |
| misfit/guidance/out | 42 | 32 | 3 | 0 | 7 | 32/35 (91%) |

### The disagreements and unclear rows

| Item | Mapper | Second rater | Why |
|---|---|---|---|
| Zhu-2 Task HALT | Tasks, clean | Tasks + Policy | The item is the separate authority to halt, not the cancellation. |
| Zhu-6 Decision classes | Policy + Approvals | Releases + Approvals | Zhu's Table 5 classes are about change authority with rollback ("Change authority is calibrated on two axes: reversibility and blast radius"). |
| Google-5 Research-assistant use case | Domains layer, strained | Guidance | A use case in vendor guidance is an example, not a domain of a running system. |
| Charterion-7 Coordination facet | Misfit | Orchestration + Directory + Tasks | Only locks and intents on shared resources lack a part; ownership and the accountable unit are Directory content. |
| AEON-8 Cross-domain composition | Misfit (as federated instances) | Policy, strained | A no-write-down rule on data flow is a Policy rule; the mapper refers it to a different item. |
| Salesforce-5 Modular Application Services | Tools, strained | Domain tools | WARM's placement test makes a connector to one system domain logic; the platforms mapper treats EAAF's adapters that way. |
| Salesforce-6 Adaptive API Management | Tools, strained | Tools + Registry + Policy | "Register, discover, and govern" is three responsibilities. |
| AOS-7 Four states and reconciliation | Guidance | Misfit | §8.7 describes controllers that act at run time ("may cancel, isolate, or escalate"). |
| AAM5C-4 Infrastructure agents (unclear) | Role in an IT-operations domain | Infrastructure + Reliability + Observability | Depends on whether L7 is the agent system's own infrastructure or the managed estate's. |
| Charterion-1 Runtime Node (unclear) | Infrastructure, clean | Environments + Harness | ArchiMate Node, but "the halt, zone and telemetry facts attach to it". |
| ASOC-3 L6 Databases (unclear) | Infrastructure, clean | Providers, strained | A figure label with no definition. |

Two conventions differ between mappers, and both affect counts across sources more than any single row. (1) The vendors mapper files a recommended pattern or practice as guidance and names the service in brackets (Google C027, C051; Microsoft Pattern 2). The other mappers assign such items to the service. I counted these rows as agreement. (2) Connectors to particular enterprise systems are domain tools in the platforms file (EAAF D04), but Tools in the charters file (Salesforce D43).

## Part 2. The evidence behind four verdicts

### (a) Charterion: an agent as a non-human principal whose identity may be instantiated many times

- Definition 2.1, §2.1, PDF p. 28 (printed p. 4): "An agent is a non-human principal: it has an identity to which authority and accountability attach, it may be instantiated many times, and its behaviour is bounded by the operations it can reach rather than by a fixed programme (Yao et al., 2023; Schick et al., 2023; Wang et al., 2024; Xi et al., 2025)."
- The credit to security bodies is not in Definition 2.1. Definition 2.1 cites papers on LLM agents. The credit is in the front matter, "What this document claims, and what it does not", PDF p. 7: "Charterion does not claim to have invented the agent as a principal, the human sponsor, scoped or attenuating delegation, autonomy levels, human oversight or run-time interception; these are stated, since 2025, by the Cloud Security Alliance, NIST, OWASP, IMDA, Google and others, and Chapter 24 credits them."
- §8.11, PDF p. 60 (printed p. 36), is about configuration drift, not instances: "The agent that was reviewed at gate G2 is not necessarily the agent that runs: model, prompt, tool set and runtime version change without a change to the charter." It supports a different point: identity and charter are kept separate from configuration.
- §8.12, PDF p. 61 (printed p. 37), is the passage on instances: "An agent type is chartered once and instantiated many times, ephemerally. The core semantics is stated on types; the instance profile records running instances, bounds their number and counts the oversight span over instances." Definition 8.9 on the same page: "An instance i of agent a is a running process that acts under the identity of a and holds no charter of its own."

**Reading.** The stated reading is supported in substance: Charterion's agent is a non-human principal with an identity, it may be instantiated many times, and Charterion credits security and standards bodies. Two corrections apply. The credit is in the front matter, and the instantiation passage is §8.12, not §8.11. **The identity belongs to a type of agent.** Instances act "under the identity of" the type and hold no charter of their own. This differs from WARM, where several agents may share one definition and each task agent "acts under an identity of its own" (Step 0). Charterion's chartered agent sits between WARM's agent definition and WARM's agent. Its short-lived instances are the nearest thing to WARM's task agents, but they have no identity of their own. Charterion is precedent for "an agent is an identified principal". It is not precedent for one identity per individual agent.

### (b) AEON's capability registry

- §11.1, PDF p. 26: "The capability registry is the canonical record of what the enterprise can do. Every capability any subdomain exposes is registered in the registry along with its metadata: the subdomain that provides it, the capability description in canonical form, the adapter that exposes it, the policy constraints that apply to its use, the lifecycle stage (proposed, qualified, operational, deprecated, retired), the evidence requirements, the audit posture, the dependencies on other capabilities, and the principals authorized to invoke it under what conditions."
- Same page: "The registry is the source of truth for capability discovery." And: "the architectural authority over the registry's contents belongs to Enterprise IT."
- §10.2 "The Agent Network", PDF p. 24: "The protocol specifies how agents discover other agents (through the capability registry developed in Section 11), how they authenticate to each other ...".

**Reading.** The stated reading is accurate: the registry records the providing subdomain and the principals authorized to invoke each capability, and agents discover other agents through it. **It does not record who is accountable.** "The subdomain that provides it" names a supplier of a capability. A capability is "what the enterprise can do", not a responsibility at the grain of a handoff. Where AEON uses the word accountability, it attaches to principals and the identity chain, not to subdomains (for example §7 The Identity Plane, PDF p. 15: "This chain is what makes agentic accountability possible"). **One provider per capability is not stated.** Each entry names "the subdomain" in the singular, but no passage forbids two subdomains from registering the same capability. The nearest control is the lifecycle process in §11.2, which keeps the registry from "becoming a dumping ground". So AEON's registry is a catalog with a provider field and access rights. WARM's Directory records the domain accountable for each scoped responsibility, and exactly one domain is accountable at that grain.

### (c) AOS: "a persistent agent identity" and "a transient runtime instance"

- §10.2 Agent Lifecycle Management, PDF p. 33: "Agent lifecycle includes create, initialize, activate, pause, resume, quiesce, migrate, revoke, terminate, and garbage-collect. The managed object may be a persistent agent identity or a transient runtime instance. AOS distinguishes identity from instance so that an agent can migrate or restart without losing authority and audit continuity."

**Reading. It is a different distinction from persistent versus task agent.** AOS separates the identity of one agent from the running copy that can be restarted or moved. That is WARM's agent-versus-instance distinction in Step 0 ("an instance of an agent can be restarted or moved, and it is not the agent"). WARM's persistent-versus-task split is about how long a role lasts: across many sessions and tasks, or for one task. AOS says nothing in this passage about task-scoped agents. A task agent in WARM also has an identity and can have instances. Citing AOS for the identity-versus-instance point is correct. Citing it for the persistent-versus-task split, as `search.md` §7(c) does, is not.

### (d) Agent-lifecycle parts in AOS, Steinder and Franke, and EAAF

Test statement: "create, suspend, resume and end agents, and keep the list of which agents exist."

- **AOS.** Table 7, §8.4, PDF p. 27: "Agent lifecycle | Created, active, paused, migrated, revoked, terminated | Orphaned agent, duplicate execution, failed revocation". §10.2, PDF p. 33, as quoted under (c). AOS-0000 §4.2 "Agent Lifecycle Manager", PDF p. 7: "The lifecycle manager maintains durable agent identifiers, capability grants and revocations, context store pointers with retention and classification metadata, and deterministic termination semantics." **Fair, with additions.** Create, pause, resume and terminate are all there. The list of which agents exist is implied by "durable agent identifiers" and by the "Orphaned agent" failure, but it is not stated as a duty. AOS also includes migration, revocation (which WARM gives to Identity) and capability grants (which WARM gives to Policy).
- **Steinder and Franke.** §IV-A "Agent as an first-class entity", Agent-OS primitive: "An agent is an isolated execution context (container/pod) with an LLM session, tool credentials, context buffer, and memory state. It may be created, run (context-assemble → infer → tool-call → update), terminated. Agents spawn sub-agents (fork/exec analog) through platform-mediated channels. Agent identity must be a function of its Cloud-OS identity and agent-level properties like goal, skills, tools, model, or context." Table I row: "Process | Pod / container | Agent lifecycle | Probabilistic behavior; semantic identity | Partial | Near". **Partly fair.** Creating and ending agents, and starting sub-agents, are there. Suspend, resume and a list of agents are not. The primitive mainly defines what an agent is (an isolated context with a semantic identity), by analogy to the process. It is not a part that manages a population of agents. Its identity clause also contradicts WARM Step 0, where identity persists through a change of definition or model.
- **EAAF.** §5.1, Control Plane, item 4, PDF p. 11: "The ALM manages the complete creation, maintenance, and retirement of agents, treating them as first-class enterprise assets. The lifecycle includes Provisioning (initializing identity/environment), Configuration (policy binding), Execution, Monitoring, Adaptation, and Decommissioning (credential revocation). For stable evolution, ALM facilitates multi-version coexistence, canary rollouts, and automatic rollback to the last stable version. This system enables Continuous Adaptation by managing policy updates, prompt improvements, and incorporating runtime learning signals based on execution feedback." **Fair only for creating and ending agents.** Suspend and resume are not named. A list is implied by "first-class enterprise assets" but not stated. Most of the rest is what WARM gives to Releases (versions, canary, rollback), Improvement (continuous adaptation) and Policy (policy binding).

**Overall.** Each of the three has a top-level part for the existence of agents, so the v0.11 claim of absence was false. Creating and ending agents is the core all three share. Only AOS suspends and resumes agents. None states that it keeps a list of which agents exist; AOS comes closest, through its orphaned-agent failure and durable identifiers. So WARM's Lifecycle is a fair statement of what the three have in common, plus a list duty that rests mainly on AOS's named failure. The three parts are not one cut: EAAF's includes release management, and Steinder and Franke's includes a definition of what an agent is.

## Part 3. The mappers' candidate changes, read after Parts 1 and 2

I read each file's "What WARM might change" section and the conclusions next to it.

### Candidate changes my sample gives reason to doubt

1. **Platforms #1, the 25th service (Lifecycle), in its scope, not in the gap.** My sample confirms the gap (AOS A14, Steinder and Franke B06, Microsoft A93). But the evidence describes three different parts, as Part 2(d) shows. The "keep the list" duty is stated by none of the three, and suspending and resuming an agent is stated only by AOS. The candidate's sentence "three of four make the lifecycle of a running agent a top-level component" is true, but it overstates how far they agree on what that component does.
2. **Charters W1, and v0.12's credit to Charterion, need the type-level caveat.** The retraction ("an agent is an identified actor" is not new) stands. But Charterion's identity belongs to a type and is shared by its instances, so it is not precedent for WARM's identity per individual agent, nor for a task agent with an identity of its own. The charters mapper says this (W9, and the verdict on claim iv), and its section citation should be §8.12. v0.12 Step 0 cites Charterion without the caveat.
3. **Vendors #4, suspension in Policy, which v0.12 superseded with Lifecycle.** Microsoft's sampled item suspends an agent *class*. v0.12's Lifecycle acts on agents one at a time. A stop applied to every agent built from one definition needs a home: Policy denying an actor class, or the Registry or Releases disabling a definition.
4. **Platforms #2, run-time assessment placed in Evaluation.** This covers judging a proposed action. It does not cover a standing trust score per actor that decays and that later decisions read (ASOC §VI-D; AOS A27 "Trust may decay when evidence becomes stale"; EAAF's IAAS gives each agent "a dynamic trust score"). My ASOC-9 row is still only partly placed in v0.12.
5. **Vendors #12, domain parts written for one agent, and the vendors' "Domains layer" rows.** The one sampled row of this kind, Google's research-assistant use case (C070), is an illustration in guidance that the mapper filed under the Domains layer, as it did C069 and C071. Use cases like these are weaker evidence than design rules such as C072 ("Clearly define the business goal of the agentic AI system and the task that each agent performs"), and the count of domain-like parts in the vendor sources should not include them.
6. **Platforms #13, the decision-execution split, does not cover AOS §8.7.** It adds separate records of "authorized" and "happened". AOS's controllers also act on a gap between them (cancel, isolate, escalate). The mapper filed that row as guidance, so no candidate places it.

### Gaps my sample suggests that no mapper listed

- **Acting on divergence between what was authorized and what is observed** (AOS §8.7, mis-filed as guidance). Observability records, Evaluation judges, and point 1 states a check, but no part owns the corrective act. Candidates: Reliability, or Tasks (cancel), with Lifecycle (isolate).
- **Stopping all agents of one definition or class** (Microsoft A93). Lifecycle is written per agent, and Identity revokes one identity.
- **A standing trust or reputation record per actor** (ASOC, AOS, EAAF). Listed by the platforms mapper as a misfit (AOS A27) but not carried into a candidate change.
- **Rules on information flow between classification levels** (AEON §14.5). Policy's content rules cover what enters and leaves models and tools, not flow between workflows at different levels. Low importance outside regulated settings.
- **Method, not model.** The two cross-mapper conventions above (patterns as guidance; connectors to particular enterprise systems as Tools or as domain tools) should be settled before counts are compared across sources.

## Limits

- One rater, who read WARM before the sources and works for the same author as the mappers. Hiding the mapper's assignment was mechanical, but the mapper's IDs and the order of the tables were visible.
- The sample is 126 of about 1,400 rows. "Planned" and "folded" rows were not sampled. Some rows were dropped by the parser because their cells contained `|`; this affects which rows could be picked, not any verdict.
- **Incidental exposure.** During Part 2, a `grep -n -i instance warm-model-v0.12.md` printed seven one-line fragments from the sections I was told not to read (lines 535, 562, 565 and 601 of "Compared with published models", 694 and 695 of "What WARM adds", and 738 of "Changes from v0.11"). This happened after all Part 1 assignments and verdicts were written to file. The fragments concerned Charterion's and AOS's agent identity; my Part 2(a) and (c) readings come from the quoted primary text.
- Not opened: the AAM/5C primary (verdict AAM5C-4 stays unclear for that reason), the vendor pages, Salesforce, CEAD and Yu et al. No sampled item from those needed the primary to be judged, except AAM5C-4.
- Charterion's PDF text drops word spaces. Quotations restore the spacing and change nothing else.
