---
title: "WARM v0.11 mapped against three vendor reference architectures (Microsoft, AWS, Google Cloud)"
date: 2026-11-11
yardstick: warm-model-v0.11.md
status: first mapping; one mapper; not reviewed
---

# WARM v0.11 against three vendor reference architectures

This document maps three vendor-published descriptions of agent systems onto WARM v0.11, component by component, and reports where they do not fit. The yardstick is `warm-model-v0.11.md` only: its five layers, 24 services with one responsibility each, the seven domain parts, its agent concepts, and the Directory.

## Summary

| Source | Inventory items | Clean | Strained | Spans | Guidance | Misfits |
|---|---|---|---|---|---|---|
| A. Microsoft, Multi-Agent Reference Architecture | 153 | 48 | 17 | 36 | 47 | 5 |
| B. AWS Prescriptive Guidance, agentic AI series (6 guides) | 385 | 73 | 46 | 72 | 149 | 45 (40 out of scope) |
| B, reference architecture guide only ("Governing and architecting", GA) | 87 | 24 | 18 | 30 | 15 | 0 |
| C. Google Cloud Architecture Center, agentic AI pages | 144 | 56 | 25 | 32 | 26 | 5 |

Counts are not comparable across sources. The sources differ in granularity, and the AWS count includes three guides (foundations, frameworks, patterns) whose items were grouped by assignment (Section B.1.4-B.1.6). Most AWS misfits are properties and modules of a single agent, which WARM's Step 0 places out of scope.

Main results, each stated in full in "What WARM might change":

1. **All three sources route an inbound request to an agent by its content or its requester**, before any agent runs (Microsoft's Classifier, AWS's routing workflow, Google's dispatcher agent and tenant-routing portal). WARM has no place for this.
2. **None of the three has WARM's Directory.** All three have registries; their entries describe agents, tools and skills and how to reach them. Microsoft and AWS add owners; none records which area of work is accountable for a responsibility.
3. **None separates a domain from its agents.** Microsoft and AWS map a domain to an agent; Google's multi-tenant architecture gives a business unit its own agent, tools, rules and data, which is the nearest any source comes to WARM's Step 4. AWS writes WARM's domain parts (outcome, autonomy limits, success criteria, guardrails) as a charter for each agent.
4. **None states WARM's persistent/task distinction.** Agents are applications or services; continuity is per user (memory), not per agent.
5. **Registries are governance records** carrying owners, approval status, permissions, metrics and (at Microsoft) credentials, and registration is a precondition for permission in all three. WARM splits this over Registry, Directory, Policy, Approvals, Observability and Secrets.
6. **Run-time suspension of an agent** ("pause/disable an agent class", "pause agents", "circuit breakers for abnormal behavior") appears in all three and has no WARM place.
7. **Content guardrails** (Bedrock Guardrails, Model Armor, safety classifiers) are strained in WARM's Policy, which is worded for actions.

## Method

**Yardstick.** WARM v0.11 (`warm-model-v0.11.md`, read in full on 2026-11-11; it was edited on disk during this work, in two sentences of its prior-work section that do not touch the definitions used here). No other file in the WARM folder was read.

**Sources.** Read on 2026-11-11. Microsoft: the GitHub repository, cloned at commit `adbefc18` (2026-10-27), every Markdown chapter. AWS: six guides of the Prescriptive Guidance series, from each guide's table of contents; the reference architecture guide and the operationalizing guide in full by this mapper; three further guides in full by a delegated reader that produced a verbatim inventory; key pages of the serverless and multi-tenant guides. Google: the 17 pages of the Architecture Center's "Agentic AI" section, read by a delegated reader that produced a verbatim inventory. Each section lists the pages, their dates, what was read and what could not be opened.

**Procedure.** For each source: (1) inventory every named component, layer, building block, pattern and capability, with a short verbatim definition and its page, before assigning; (2) assign each item to exactly one of: a WARM service, a layer, a domain part, an agent concept, a span of several WARM parts, guidance (a design-time arrangement, not a part of a running system), or misfit; mark one-part fits clean (C) or strained (S); (3) for every WARM part, say whether the source has it, after a recorded search; (4) findings. When in doubt between a strained fit and a misfit, the item was called a misfit. "Out of scope" misfits are items WARM's Step 0 excludes on purpose (how a single agent reasons).

**Checks.** Fourteen Google quotes and eight AWS quotes taken from the delegated inventories were checked against the fetched page text by exact string match; all 22 matched. The Microsoft and the two primary AWS guides were quoted from text this mapper read.

**Limits.** One mapper, who knew WARM before reading the sources; no second rater. The delegated inventories for AWS (F, W, P) and Google were not re-read page by page by the mapper. Assignments in grouped rows (B.1.4-B.1.6) apply to every item in the row unless the row states a split. The AWS series has guides that were found and not read (security; semantic layer; most of serverless and multi-tenant), and one guide that could not be opened (enterprise multi-account architecture: AWS "page not found" on 2026-11-11). Documentation is evidence of what vendors describe, not of what their products do. Statements labeled "suggests" or "candidate" are the mapper's inference; quoted text is what a source states.

**Fit codes** used in every table: **C** clean one-part fit, **S** strained one-part fit, **Sp** span, **G** guidance, **M** misfit.

## A. Microsoft, Multi-Agent Reference Architecture

**What it is.** A Markdown book in the GitHub repository `microsoft/multi-agent-reference-architecture`, cloned on 2026-11-11 at commit `adbefc18` (committed 2026-10-27). It describes itself as "a conceptual guide ... for architecting robust multi-agent systems", "both opinionated ... and agnostic" (README). Its center is one pattern: an orchestrator agent that delegates to specialized agents found in an agent registry.

**Pages read.** Every Markdown file under `docs/`, plus `README.md` and `SUMMARY.md`, and the labels of `docs/reference-architecture/architecture.drawio.svg`. All URLs are `https://github.com/microsoft/multi-agent-reference-architecture/blob/main/<path>`. Dates are each page's own "Last updated" line; all were read on 2026-11-11.

| Path | Last updated | Read |
|---|---|---|
| README.md, SUMMARY.md | (none) | full |
| docs/Introduction.md | 2025-05-16 | full |
| docs/building-blocks/Building-Blocks.md | 2025-05-28 | full |
| docs/design-options/Design-Options.md, Modular-Monolith.md, Microservices.md | 2025-05-15, 2025-05-15, 2025-05-16 | full |
| docs/agent-registry/Agent-Registry.md | 2025-05-15 | full |
| docs/agents-communication/Agents-Communication.md, Request-Based.md, Message-Driven.md | 2025-06-30, 2025-06-04, 2025-06-30 | full |
| docs/memory/Memory.md, Memory-Architecture-Patterns.md, Short-Term-Memory.md, Long-Term-Memory.md, Memory-Pipelines.md | 2026-08-04 (all five) | full |
| docs/observability/Observability.md | 2025-10-21 | full |
| docs/evaluation/Evaluation.md, ToolCall.md | 2025-10-21 | full |
| docs/security/Security.md, Threat-Model.md | 2025-05-12 | full |
| docs/governance/Governance.md, Experimentation-To-Productization.md | 2025-05-13, 2025-05-29 | full |
| docs/governance/DevOps-And-DataOps-On-Agents-Lifecycle.md | (file is empty, 0 bytes) | **could not read: empty** |
| SUMMARY "Data exchange protocols" | (link target is empty) | **no page exists** |
| docs/context-engineering/Context-Engineering.md, Iteractive-Optimization-Loop.md, Agents-Orchestration.md, Tools.md | 2025-07-03, 2025-07-03, 2025-07-07, 2025-07-14 | full |
| docs/versioning/Versioning.md, Behaviors.md, Strategies.md, Recommendations.md, Maturity.md | 2025-09-24/25 | full (not linked from SUMMARY.md; present in the repo) |
| docs/reference-architecture/Reference-Architecture.md, Patterns.md, Conversational-SequenceDiagram.md | 2025-08-18, 2025-05-14, 2025-05-16 | full |
| docs/References.md, docs/Contributors.md | 2025-06-30 | full (no components) |

Two links inside the pages are broken: Security.md links to `./the` for the threat model, and Threat-Model.md links to a `Multi-agent-security.md` that does not exist. Reference-Architecture.md links pattern 9 to a `docs/Multi-Agent-Patterns.md` that does not exist; the pattern is in Patterns.md.

### A.1 Inventory and assignment

Page codes: INT Introduction, BB Building-Blocks, DO Design-Options (MM Modular-Monolith, MS Microservices), REG Agent-Registry, COM Agents-Communication (RB Request-Based, MD Message-Driven), MEM Memory (MAP Memory-Architecture-Patterns, STM Short-Term-Memory, LTM Long-Term-Memory, MP Memory-Pipelines), OBS Observability, EV Evaluation (TC ToolCall), SEC Security (TM Threat-Model), GOV Governance (E2P Experimentation-To-Productization), CE Context-Engineering (IOL loop, AO Agents-Orchestration, TL Tools), VER Versioning (BEH, STR, REC, MAT), RA Reference-Architecture, PAT Patterns.

Fit column: **C** clean, **S** strained, **Sp** span, **G** guidance, **M** misfit.

| ID | Item | Definition (verbatim, short) | Page | Assignment | Fit | Reason |
|---|---|---|---|---|---|---|
| A01 | Separation of Concerns (principle) | "each agent has a distinct and well-defined responsibility" | INT | Guidance | G | A design principle. It is stated for agents, where WARM states one responsibility per service and per domain. |
| A02 | Secure by Design (principle) | "strict authentication, authorization, and policy enforcement for every agent interface" | INT | Guidance (uses Identity, Policy) | G | Principle, not a part. |
| A03 | Observability & Traceability (principle) | "traced end-to-end across the system using common identifiers" | INT | Guidance (uses Observability) | G | Principle. |
| A04 | Agent Registration & Lifecycle Governance (principle) | "Agents should be explicitly registered, versioned, and validated before being included in production" | INT | Guidance (uses Registry, Releases, Evaluation) | G | Principle that joins three WARM services. |
| A05 | Failure Isolation & Graceful Degradation (principle) | "Failures in one agent should not cascade to others" | INT | Guidance (uses Reliability) | G | Principle. |
| A06 | Context Management (principle) | "clear rules and policies regarding what context or conversational state is shared among agents and for how long" | INT | Guidance (uses Policy, Sessions, Memory) | G | Principle. |
| A07 | Orchestrator agent | "acts as the central coordinator ... formulates a high-level plan composed of individual tasks ... aggregates and synthesizes their outputs" | BB | Span: Orchestration + agent (a coordinating role) + Channels (receives "incoming requests—whether from users or external services") | Sp | One agent both coordinates assignments (platform) and plans and synthesizes the answer (work whose content depends on the subject). WARM separates these. |
| A08 | Specialized agents | "domain-focused experts ... Each one is responsible for a distinct area of expertise—for example, one agent might be responsible for finding flights" | BB | Agent concept (an agent filling a role) | S | Fits "agent fills a role", but the source's "domain" is the grain of a single function (finding flights), far below WARM's domain. |
| A09 | Agent is not a task or a tool (rule) | "A specialized agent is not the same as a task or a tool ... agents should be structured around meaningful, cohesive capabilities" | BB | Guidance | G | Sizing advice; agrees with WARM's grain argument for responsibilities. |
| A10 | Composite agent | "if agents are tightly coupled, group them into a single composite agent exposed to the orchestrator as one unit" | BB | Guidance (uses Orchestration) | G | An arrangement of agents. |
| A11 | Agents registry | "centralized data service and source of truth for managing all specialized agents ... like a dynamic directory—cataloging each agent's identity, capabilities, operational status, version, and metadata tags" | BB | Span: Registry + Directory (how to reach) + Reliability (operational status) | Sp | Holds definitions and versions (Registry), endpoint and auth to reach an agent (WARM puts "how to reach" in the Directory), and liveness. |
| A12 | Modular monolith (design option) | "all components ... reside within a single codebase and are deployed as one application" | MM | Guidance (Infrastructure, Releases) | G | Deployment topology. |
| A13 | Microservices (design option) | "each component ... is encapsulated as an independent service running within its own process" | MS | Guidance (Infrastructure, Releases) | G | Deployment topology. |
| A14 | Orchestration Layer (onion) | "Handles workflow and high-level coordination" | MM | Orchestration | C | Same responsibility. |
| A15 | Specialized Agent Layer (onion) | "Implements the core agent-specific business logic" | MM | Domains layer (domain work) | S | Business logic is domain work; WARM does not place domain logic "inside" an agent module. |
| A16 | AI Layer (onion) | "Interfaces with language models ... providing a unified API for all AI tasks" | MM, MS | Models | C | Mediates model calls. |
| A17 | Knowledge Layer (onion) | "Interfaces with AI models, vector stores, files, web data, data analytics platforms" | MM, MS | Retrieval | S | Mostly Retrieval; the monolith text also lists "AI models", which belong to Models. |
| A18 | Storage / Persistence Layer (onion) | "Manages persistence, data retrieval, and caching" | MM, MS | Infrastructure | S | Generic persistence beneath Sessions, Memory and Artifacts. WARM has no storage service, by design. |
| A19 | Integration Layer (onion) | "Connects the system to external APIs and services" | MM, MS | Tools | C | Mediates external calls. |
| A20 | API Layer (microservice) | "Exposes network endpoints (REST, gRPC, etc.) for agent operations" | MS | Channels | S | Endpoint by which a program calls an agent; also used agent to agent, which WARM gives to Messaging. |
| A21 | Service Layer (microservice) | "Implements the agent's core business logic (task delegation, reasoning, workflow, etc.)" | MS | Span: Harness (reasoning loop) + Orchestration (delegation) + Domains (workflow) | Sp | Three WARM parts in one code layer. |
| A22 | Register component (discovery) | "A register mechanism is necessary to input Agent information into the repository" (registry-initiated or agent self-register) | REG | Registry | C | Adding entries. |
| A23 | Repository component (storage) | "a storage mechanism that houses all the available Agent Information" | REG | Registry | C | Holding entries. |
| A24 | View component | "lists all the available agents or ... provides filtering capabilities" | REG | Registry | C | Finding entries. |
| A25 | Monitor component | "regularly call the registered agents for uptime and information" | REG | Span: Registry (keep entries current) + Reliability (uptime) | Sp | Health checking is not a Registry responsibility in WARM. |
| A26 | Agent Information (registry entry) | `name`, `description`, input/output, "how to communicate ... `url` and `authentication`"; for humans "`tags` or `owners`" | REG | Span: Registry + Directory (how to reach; owner) | Sp | WARM's Registry entry is a versioned definition; the reach information and the owner are Directory content. |
| A27 | Evaluation of registering agent | "During the registration process, it's recommended to contain a validation step to evaluate the validity of the agent" | REG, PAT#2 | Span: Evaluation + Releases (admission is a release gate) | Sp | Registration doubles as release; WARM keeps Registry, Evaluation and Releases separate. |
| A28 | Request-based communication | "all interactions ... are initiated by explicit requests" | RB | Guidance (uses Channels, Orchestration) | G | Interaction style. |
| A29 | Synchronous request-reply (non-streaming, server-streaming) | "The client sends a request ... and waits for a single, complete response" | RB | Guidance (Channels) | G | Interaction style. |
| A30 | Asynchronous request-reply (polling, streaming) | "receives an immediate acknowledgment (containing a unique task ID) ... polls a status endpoint" | RB | Span: Channels + Tasks | Sp | A client-facing task handle with status is Tasks exposed through Channels. |
| A31 | Streaming only from orchestrator to client (rule) | "only stream responses from the orchestrator agent to the end client—not between the orchestrator and internal expert agents" | RB | Guidance | G | Rule of arrangement. |
| A32 | Message-driven communication | "agents interact asynchronously by exchanging discrete messages—such as commands, events, or responses—via a broker or event bus" | MD | Messaging | C | Delivery between agents. |
| A33 | Message broker / event bus | "Message queues/brokers can act as a buffer ... Built-in retries, dead-letter queues, and durable message storage" | MD | Messaging | C | Carrier. |
| A34 | Dead-letter queue | "capture and inspect failed messages for debugging or reprocessing" | MD | Messaging | S | Delivery failure handling; reprocessing touches Reliability. |
| A35 | Correlation IDs | "attach unique identifiers to track message flows across the distributed system" | MD | Span: Orchestration (match results to assignments) + Observability (trace) | Sp | Used for both purposes in the text. |
| A36 | Parallel fan-out | "The orchestrator fans out commands to multiple agents, then waits for all responses" | MD | Guidance (Orchestration, Messaging) | G | Pattern. |
| A37 | Chained task sequencing | "a sequence of commands, where the output of each step is used as input for the next" | MD | Guidance (Orchestration) | G | Pattern. |
| A38 | Circuit breakers | "Protect against cascading failures by implementing circuit breaker patterns in agent communication" | MD | Guidance (Reliability) | G | Practice. |
| A39 | Event sourcing | "consider event sourcing to maintain an audit trail and enable replay" | MD | Guidance (Observability, Sessions) | G | Practice. |
| A40 | Agent communication protocols (A2A, ANP, ACP) | "particularly suited for structured request-based communication between agents" | RB | Messaging | S | Protocols also carry discovery cards and task state, beyond delivery. |
| A41 | Short-term memory (STM) | "maintain recent context within an active session (also known as conversation history) ... session-scoped, token-limited ... trimmed, summarized, or discarded" | MEM | Sessions | S | The store is Sessions; trimming and summarizing for the model is Harness work. |
| A42 | Long-term memory (LTM) | "persistence of information across sessions ... a compressed, distilled representation of what happened" | MEM | Memory | C | Same. |
| A43 | Working memory | "The context actually assembled for a single inference call. It is not a store, it is a _composition_" | MEM | Harness | C | WARM places working memory in the Harness. |
| A44 | Semantic memory | "Extracted facts and attributes" | MEM | Memory | C | Facts. |
| A45 | Episodic memory | "Complete past interactions and events, timestamped" | MEM | Memory | C | Events. |
| A46 | Procedural memory | "Learned workflows and methods"; "only becomes a distinct concern when the procedure was never written down" | MEM | Memory | S | WARM's Memory holds "facts and events"; written procedures are skills in the Registry. Microsoft's carve-out (unwritten, learned procedures stay in memory) is a third kind WARM does not name. |
| A47 | Knowledge sources ("Memory is not a knowledge base") | "authoritative, shared, permission controlled, and change independently of any conversation" | MEM | Retrieval | C | Matches the WARM split of Memory and Retrieval. |
| A48 | Permission-trimmed index | "retrieve it on demand through a permission-trimmed index ... access control is evaluated at query time" | MEM, MAP | Span: Retrieval + Policy | Sp | Fetch plus an access rule enforced inside the fetch. |
| A49 | Four memory decisions | "What to remember ... Where to store it ... How to retrieve it ... Which boundaries share memory" | MAP | Guidance (Memory) | G | Design checklist. |
| A50 | Storage strategies (vector, graph, hybrid, simple persistence) | "Storage strategy should be chosen per memory sub-type" | MAP | Guidance (Memory, Infrastructure) | G | Implementation choice. |
| A51 | Memory retrieval patterns (RAG over history, summarization buffer, fact extraction + injection, on-demand search) | "These patterns compose" | MAP | Guidance (Harness, Memory, Sessions) | G | Implementation choice. |
| A52 | Memory archetypes (auto-injected layered; on-demand tool-based; retrieval over permission-trimmed index; extract-and-update memory layer; self-managed tiered) | e.g. "A dedicated memory service sits beside the agent" | MAP | Guidance (Memory as a service) | G | Five arrangements; the extract-and-update archetype is Memory as a separate service, as WARM has it. |
| A53 | Memory scoping (session, global, project/workspace, channel, role) | "Scope defines who and what a memory is visible to. It must be an explicit attribute of every memory entry" | MAP | Span: Memory + Policy | Sp | Scope is stored by Memory and enforced as an access rule. |
| A54 | STM design approaches (shared, distributed, hybrid "private chat") | "memory is shared only within explicit subgroups of agents" | STM | Guidance (Sessions, Policy) | G | Arrangement of session stores. |
| A55 | Session document data model | "Session ID ... Source ... Session Status ... Summary ... Token Count ... Promotion State" | STM | Sessions | C | History and state of a stretch of work. |
| A56 | Context window management (sliding window, progressive summarization) | "A token-limit mechanism is mandatory" | STM | Harness | C | Compaction. |
| A57 | Thread resumption | "load the session document, produce (or reuse) a thread summary, and send that summary plus the most recent turns" | STM | Span: Sessions + Harness | Sp | Reload (Sessions) plus context assembly (Harness). |
| A58 | Working memory assembly | "assembled per turn from four sources, each with its own share of the token budget" | STM | Harness | C | Deciding what goes into context. |
| A59 | Session end (discard, archive, promote) | "three distinct decisions must be made about its content" | STM | Span: Sessions + Policy (archive) + Memory (promote) | Sp | Three services act on one event. |
| A60 | Multi-channel session boundaries | "Session boundaries are channel-specific" | STM | Span: Channels + Sessions | Sp | Session lifetime set by channel. |
| A61 | Data retention / archiving job | "Define policies for how long data remains in hot storage before being archived or deleted" | STM | Policy | C | WARM Policy holds rules on stored data. |
| A62 | Memory entry data model | `scope`, `source_session_id`, `confidence`, `version`, `tier`, `sensitivity`, `expires_at`, `pinned` | LTM | Memory | C | Entries with provenance, kept current. |
| A63 | Memory lifecycle (extraction, consolidation, reinforcement, decay, versioning, deletion) | "A memory is not written once and kept forever ... each stage needs an owner in the architecture" | LTM | Memory | C | "keep it current". |
| A64 | Relevance scoring and decay; tier demotion; batch curation job | "memories that nobody accesses fade over time"; "The batch job is a curation job" | LTM | Memory | C | Keeping entries current (the job is started by Scheduling). |
| A65 | Memory scope decision framework | "scope = f(use_case, duration, sensitivity)" | LTM | Guidance (Memory, Policy) | G | Design method. |
| A66 | User control over memory | "Users must be able to see, edit, and delete what the system remembers about them"; "Incognito or temporary mode"; "Clear ownership" | MEM, LTM | **Misfit** | M | A data subject's rights over stored data. It could be spread over Memory, Policy and Channels, but no WARM part is responsible for it, and WARM says the person-as-subject relation is "not developed". |
| A67 | Memory data protection | "Encryption at rest and in transit ... Never store credentials ... Audit trail for every memory access ... Memory must not feed model training" | LTM | Span: Policy + Observability | Sp | Rules on stored data plus audit. |
| A68 | Memory governance model | "Admin controls for enabling memory per team, per agent, and per channel ... a named owner for the memory data of each scope" | LTM | Span: Policy + People (named owner) | Sp | Configuration rules plus a human owner. |
| A69 | Operating memory at scale (separate conversation storage from memory processing; async extraction; rate limits; size budgets; memory activity log) | "Separate conversation storage from memory processing" | LTM | Guidance (Memory, Scheduling, Observability) | G | Operating advice. |
| A70 | Memory adoption roadmap (3 phases) | "Memory capability is best delivered in phases" | LTM | Guidance | G | Rollout plan. |
| A71 | Memory retrieval pipeline (context window, query, aggregator, dedupe, reranker, budget, write-back) | "produce the best possible context that fits the available token budget" | MP | Span: Harness (assembly, budget) + Memory (ranked recall, access write-back) | Sp | WARM: the Harness "reads Memory ... into the context window". |
| A72 | STM session-end pipeline | "converts a raw conversation into structured, searchable short-term memory entries that are ready for later promotion" | MP | Memory | S | A staging tier of extracted facts between Sessions and Memory; WARM has no staging tier. |
| A73 | STM-to-LTM promotion pipeline | "decide which short-term facts have earned durable, cross-session status" | MP | Memory | C | Retaining what was learned, with provenance and audit; started by Scheduling. |
| A74 | Observability (AI) | "expanding the traditional pillars of logs, metrics, and traces ... agent actions, tool usage, model invocations" | OBS | Observability | C | Same. |
| A75 | Observability key areas (agent communication, performance, error handling, security & compliance) | e.g. "Detecting failures, cascading errors, and recovery mechanisms" | OBS | Observability | C | Evidence collection areas. |
| A76 | Evaluation | "analyzes that data to determine how well agents are performing against defined success criteria and business requirements" | EV | Evaluation | C | Same. |
| A77 | Code-based evaluation; LLM-as-a-judge | "deterministic and programmatic criteria"; "leverages Large Language Models ... to assess" | EV | Evaluation | C | Methods. |
| A78 | Offline and online evaluation | "Pre-deployment testing using curated datasets"; "Production monitoring with real user interactions" | EV | Evaluation | C | Phases. |
| A79 | Evaluation feedback loop | "Offline Evaluation → Deploy Agent Version → Online Evaluation & Monitoring → Collect Data & Examples → Dataset Enrichment → Iteration & Refinement" | EV | Span: Evaluation + Improvement + Releases | Sp | The WARM Operations chain in one loop. |
| A80 | Evaluation by component (orchestrator, specialized agents, registry) | "Discovery accuracy: Verify correct agent selection" | EV | Evaluation | C | Targets. |
| A81 | Tool call evaluation | "tool calls represent the bridge between reasoning and action" | TC | Evaluation | C | Target. |
| A82 | Identity enforcement | "Agents and orchestrators authenticate ... RBAC governs agent execution ... mutual authentication ... rotating credentials for long-lived agents" | SEC | Span: Identity + Policy (RBAC) + Secrets (rotation) | Sp | Three Governance services. |
| A83 | Scoped agent capabilities | "Agent registry enforces capability declarations ... Only approved capabilities can be executed in runtime" | SEC | Span: Registry + Policy | Sp | The registry is an enforcement point here; in WARM it only holds definitions. |
| A84 | Data governance & storage policies | "All storage layers ... support encryption-at-rest. Retention policies are configurable per agent" | SEC | Policy | C | Rules on stored data. |
| A85 | Secure communication | "encrypted via HTTPS or mutual TLS. MCP protocol supports signed payloads" | SEC | Span: Identity + Messaging + Infrastructure (network) | Sp | WARM treats security as a concern across groups. |
| A86 | Policy-controlled tool invocation | "MCP server validates tool access policies before invocation. Integration layer enforces audit logging" | SEC | Span: Tools + Policy + Observability | Sp | The tool gateway is the enforcement point (WARM's Governance point 1). |
| A87 | Memory management and redaction | "Long-term memory undergoes PII redaction and consent-based storage" | SEC | Span: Memory + Policy | Sp | Rule on what is kept. |
| A88 | LLM usage and guardrails | "Responses are filtered by safety classifiers and optionally passed through moderation APIs" | SEC | Policy | S | WARM's Policy decides "whether an action is allowed"; filtering model output for content is not an action check. |
| A89 | Auditability | "Every orchestration and agent call is logged with metadata: timestamp, caller identity, input hash, output hash" | SEC | Observability | C | Evidence. |
| A90 | Adversarial testing and red teaming | "Simulate attacks (prompt injection, message corruption, impersonation)" | SEC | Evaluation | S | Security testing; WARM's Evaluation is against stated criteria. |
| A91 | Agent versioning and rollback | "Version every agent's logic, prompt configuration, and communication contract ... immediate rollback" | SEC | Releases | C | Same. |
| A92 | Business continuity and user safety | "SLOs for agent performance ... runtime health checks ... tied to release gates" | SEC | Span: Reliability + Releases + Evaluation | Sp | Three services in one control. |
| A93 | Manual override (pause or disable an agent class) | "manual override mechanisms (e.g., pause/disable an agent class) without affecting the overall system" | SEC | **Misfit** | M | Suspending a class of agents at run time. Policy checks single actions, Releases rolls back versions, Reliability restores; none suspends a running agent. |
| A94 | Enterprise data protection in RAG (indexing, retrieval, agent, identity layers) | "filter on relevant sensitivity or permissions based on agent or user role or identity" | SEC | Span: Retrieval + Policy + Identity | Sp | Access rules applied at index and at fetch. |
| A95 | Compliance considerations (consent flows, on-premise, DLP) | "Support for GDPR/CCPA consent flows" | SEC | Guidance (Policy, Infrastructure) | G | Considerations. |
| A96 | STRIDE threat model | "outlines potential threats and mitigation strategies" | TM | Guidance (Identity, Policy, Observability, Reliability) | G | Design-time analysis. |
| A97 | Governance concerns (data provenance; output accountability; operational boundaries; model oversight) | "Output accountability: ... ensuring traceability and responsibility for generated outputs" | GOV | Guidance | G | Concerns, not parts. |
| A98 | Governance committee and roles | "a cross-functional governance committee ... clear roles and responsibilities for model development, approval, deployment, and monitoring" | GOV | People layer | C | People who direct and approve. |
| A99 | Guardrails across the AI lifecycle | "detect and filter unsafe or policy-violating outputs ... Monitor for model drift, prompt injection" | GOV | Span: Policy + Observability + Evaluation | Sp | Three services. |
| A100 | Govern data access and use | "Classify data according to sensitivity and restrict agent access" | GOV | Span: Policy + Identity | Sp | Rule plus actor. |
| A101 | Training and documentation | "Train teams on your RAI framework" | GOV | Guidance (People) | G | Organizational practice. |
| A102 | Experimentation-to-productization flow | "Experimentation Phase → ... → Handoff to Engineering → ... → Deployment to Production" | E2P | Guidance (Evaluation, Releases) | G | Delivery process. |
| A103 | Deterministic routing validation | "Ensure deterministic tests for routing and decision-making logic" | E2P | Evaluation | C | Test target. |
| A104 | Governance gates | "Define clear **gates**: including Responsible AI reviews, security audits, and performance benchmarks" | E2P | Span: Releases + Approvals + Evaluation | Sp | Human sign-off on a release, informed by evaluation. |
| A105 | Context engineering | "the practice of designing, preparing, and managing this information to shape model behavior" | CE | Guidance (Harness) | G | A practice; its runtime part is the Harness. |
| A106 | Iterative optimization loop | "Get it right ... Test it right ... Analyze ... Optimize ... Repeat" | IOL | Guidance (Evaluation, Improvement) | G | A human improvement practice. |
| A107 | Static tools (agents exposed to the orchestrator as tools) | "Pre-load the language model with a static number of tools representing the specialized agents" | AO | Guidance (Registry, Harness) | G | Arrangement. |
| A108 | Vector similarity search over agent tools | "perform a vector search using the user prompt to retrieve the most relevant agents" | AO | Registry | S | Discovery over registry entries by meaning, at run time, by the orchestrator. Close to what WARM gives the Directory (find who handles this), but by capability, not accountability. |
| A109 | Semantic cache | "use prior user prompts and their corresponding most relevant tools to address similar user prompts" | AO | **Misfit** | M | Caching has no WARM place. v0.11 recorded caching from one platform and did not adopt it; this is a second vendor. |
| A110 | Deterministic logic outside the model | "Contextual data that is static or deterministic ... should be handled outside of language model interactions" | TL | Guidance (Domains: domain logic; Tools) | G | Design advice. |
| A111 | Tool granularity and responsibility | "Group closely related responsibilities ... Avoid excessive generalization" | TL | Guidance (Tools) | G | Design advice. |
| A112 | What changes agent behavior (model, prompt, tools; memory; self-modification; dependencies; multi-agent; drift) | "Agentic agents' behavior is affected through the model used and its version, the prompt and system context, and tool availability" | BEH | Guidance (Releases, Evaluation) | G | Agrees with WARM Step 0 that definition, harness and model changes are versioned and evaluated; adds memory. |
| A113 | Immutable agents | "Freeze agents at deployment for auditability and rollback" | STR | Releases | C | Release discipline. |
| A114 | Semantic versioning for agents | "Apply major/minor/patch logic to behavioral and architectural changes" | STR | Releases | C | Versioning. |
| A115 | Forking and branching | "Create forks of agents for experimentation, A/B testing or domain-specific adaptations" | STR | Releases | S | Variants per "customer groups or business units" also imply per-scope definitions in the Registry. |
| A116 | Shadow agents | "Deploy new agent versions in shadow mode alongside production agents" | STR | Span: Releases + Evaluation | Sp | Release technique for gathering evaluation evidence. |
| A117 | Rollback protocols | "revert to a known-good state" | STR | Releases | C | Way back. |
| A118 | Versioned registry with governance metadata | "centralized registries to track agent versions, lineage, dependencies, and governance metadata ... audit trails, approval records, and risk classifications" | REC | Span: Registry + Approvals (records) + Policy (risk class) | Sp | WARM's Registry holds definitions only. |
| A119 | Rollback snapshots including memory state | "rollback snapshots that include behavioral logic, memory state, and tool configurations" | REC | Span: Releases + Memory | Sp | WARM's Releases does not version memory; WARM says memory persists through a definition change. |
| A120 | Ring deployment (inner, middle, outer) | "an inner ring to test ... a middle ring that includes trusted users ... an outer ring that covers the full rollout" | REC | Releases | C | Staged release. |
| A121 | Versioning maturity model (Ad-Hoc, Scripted, Managed, Autonomous Governance) | Level 4: "Agents participate in their own lifecycle management (e.g., self-versioning proposals)" | MAT | Guidance (Releases, Improvement) | G | Maturity scale; level 4 is agent-proposed change, i.e. Improvement. |
| A122 | User Application | "The interface layer that facilitates user interaction ... handles: User authentication and session management ... User preference management" | RA | Span: Channels + Identity + Sessions | Sp | WARM's Channels carries; authentication and sessions are separate services. |
| A123 | Orchestrator (Semantic Kernel) | "central coordination component that manages the flow of requests and responses ... ensuring appropriate routing, maintaining context, and handling the lifecycle of requests" | RA | Span: Orchestration + Tasks (request lifecycle) + Harness (context) + Reliability (fallback) | Sp | A harness product bundle in WARM's sense. |
| A124 | Classifier (NLU, SLM, LLM) | "understanding user inputs and determining the appropriate routing ... directed to the most suitable agent" | RA | **Misfit** | M | Routing an inbound request to an agent by intent. Channels carries, the Directory records accountability, Orchestration coordinates assignments; none chooses the receiving agent from the request's content. |
| A125 | Knowledge Layer (RA) | "Repositories of structured and semi-structured knowledge that agents can reference. They provide domain-specific information" | RA | Retrieval | S | The repositories' content is domain knowledge; the fetch is Retrieval. |
| A126 | Supervisor Agent | "coordinating the activities of other agents ... Introduce agent supervisors as the architecture scales across domains—these components help manage and abstract groups of related agents" | RA | Span: agent (coordinating role) + Orchestration | Sp | Close to WARM's "coordinating agent and task agents" in a domain, but the group is defined by agent similarity, not by a charter. |
| A127 | Agent #1-#4 (local or remote) | "Each agent focuses on a particular domain (e.g., finance, healthcare, coding) or function (e.g., summarization, research, creative writing)" | RA | Agent concept | S | Same as A08; "domain" and "function" are interchangeable here. |
| A128 | Local vs remote agents | "Local agents run within the same environment as the orchestrator. Remote agents operate across network boundaries" | RA | Guidance (Infrastructure) | G | Deployment choice. |
| A129 | MCP Client component | "Enables standardized communication with external tools via MCP ... Handles authentication and authorization for tool access" | RA | Tools | C | Client side of tool mediation. |
| A130 | Conversation History | "A persistent store of user-agent interactions ... provides an audit trail of system behavior" | RA | Sessions | C | Record that remains after work. |
| A131 | Agent State | "Persistent storage of agent operational status, configuration, and runtime state ... recovery from failures, and adaptation based on past experiences ... maintain learned behaviors" | RA | Span: Sessions (checkpoint) + Tasks (recovery) + Memory (learned) + Registry (configuration) | Sp | One store for what WARM cuts into four by what is kept. |
| A132 | Registry Storage | "capabilities, endpoints, security credentials, performance metrics, and version history" | RA | Span: Registry + Secrets + Observability | Sp | Credentials stored in the registry; WARM keeps them in Secrets. |
| A133 | Integration Layer & MCP Server | "A standardized interface layer that connects agents to external tools, services, and data sources" | RA | Tools | C | Same. |
| A134 | Tool Adapters | "Convert native tool APIs to MCP-compatible formats" | RA | Tools | C | Mediation. |
| A135 | Security Gateway | "Manages authentication and authorization" | RA | Span: Identity + Policy | Sp | Two services at the tool boundary. |
| A136 | Request Router | "Directs requests to appropriate tools" | RA | Tools | C | Mediation. |
| A137 | Response Formatter | "Ensures consistent response formats" | RA | Tools | C | Mediation. |
| A138 | Monitoring System (tools) | "Tracks usage, performance, and errors" | RA | Observability | C | Evidence. |
| A139 | Evaluation; Observability (diagram boxes) | (diagram labels; defined in their chapters) | RA svg | Evaluation; Observability | C | Same names. |
| A140 | Vector DBs (diagram) | (label only) | RA svg | Infrastructure | S | Storage technology under Retrieval and Memory. |
| A141 | Policy Engine | "Evaluate access rules and validate parameters" | PAT#6 | Policy | C | Same. |
| A142 | Audit Log | "Log tool invocation and response" | PAT#6 | Observability | C | Evidence. |
| A143 | Pattern 1: Semantic Router with LLM fallback | "Use a lightweight NLU or SLM classifier for initial routing. If classifier confidence is low, escalate to a more expensive LLM" | PAT | Guidance (uses the A124 classifier, Models) | G | Pattern; its cost cascade is Models' "choose the model". |
| A144 | Pattern 2: Dynamic Agent Registry (service mesh for agents) | "Agents register with descriptors (capabilities, tags, embeddings) ... runtime resolution by orchestrator"; sequence: "Generate agent ID and credentials ... Probe agent endpoint ... Validate schema ... Check security requirements ... Evaluate new configuration" | PAT | Guidance (Registry, Identity, Secrets, Evaluation, Releases) | G | Pattern; the registry mints identity and credentials. |
| A145 | Pattern 3: Semantic Kernel orchestration with skills | "Each 'skill' encapsulates an agent function. Orchestrator chains skills with memory, planning, and goals" | PAT | Guidance (Orchestration, Memory) | G | Pattern; "skill" means a callable function here (term clash, A.4d). |
| A146 | Pattern 4: Local and remote agent execution | "Local supervisor delegates tasks to local or remote agents" | PAT | Guidance | G | Pattern. |
| A147 | Pattern 5: Layered (onion) architecture | "Separation of concerns by functional domain" | PAT | Guidance | G | Pattern (A14-A21). |
| A148 | Pattern 6: MCP integration layer | "MCP server abstracts tool APIs from agents. Policies control access, parameters, and invocation flow" | PAT | Guidance (Tools, Policy, Observability) | G | Pattern. |
| A149 | Pattern 7: RAG | "Pre-indexed content stored in vector DBs. Orchestrator and agents query for grounding facts" | PAT | Retrieval | C | Fetch from named sources. |
| A150 | Pattern 8: Conversation-aware orchestration | "Conversation history is stored and retrieved by orchestrator" | PAT | Guidance (Sessions, Memory, Orchestration) | G | Pattern. |
| A151 | Pattern 9: Agent-to-agent communication (orchestrator-mediated; direct with orchestrator notification; pub/sub) | "Agents interact via orchestrator or directly through scoped protocols. Registry tracks active agents and routing preferences" | PAT | Guidance (Orchestration, Messaging, Observability) | G | Pattern; the orchestrator "Approve[s] direct communication", acting as a policy point. |
| A152 | Pattern 10: Skill chaining with planning support | "Planner creates execution path from available skills" | PAT | Guidance (Orchestration) | G | Pattern. |
| A153 | Planner | "Planners that can decompose complex tasks into simpler steps" | RA, PAT | **Misfit** (out of scope) | M | Single-agent planning; WARM Step 0 excludes it. Suggests nothing. |

The inventory leaves out diagram labels with no definition ("Agents pool", "Source Bases", "Agent Layer"), the security risks table in Long-Term-Memory.md (threats, not parts), and the metrics lists.

### A.2 Counts

| Inventory items | Clean one-part fits | Strained fits | Spans | Guidance | Misfits |
|---|---|---|---|---|---|
| 153 | 48 | 17 | 36 | 47 | 5 |

The five misfits are A66 (user control over memory), A93 (manual override of an agent class), A109 (semantic cache), A124 (intent classifier) and A153 (planner, out of scope by WARM's Step 0).

### A.3 Reverse direction: WARM against Microsoft

Absence was checked with case-insensitive `grep -ril` over `docs/` for: sandbox, isolat, artifact, schedul, cron, trigger, approv, human-in-the-loop, human review, owner, accountab, secret, credential, responsib, business unit, team, domain, persistent, long-lived, long-running, ephemeral, lifetime, pause, disable, cache, tenant, payment, cost, budget, retry, recover. The instrument returned positives for most terms, so a zero is a real absence in the text as of 2026-11-11.

| WARM part | Microsoft has it | Where |
|---|---|---|
| Harness | Partly | Working memory (A43), context window management (A56), working memory assembly (A58), "Allocate context window" step in the Orchestrator sequence. No component is named for running the loop; the Orchestrator bundles it (A123). |
| Sessions | Fully | STM (A41), session data model (A55), Conversation History (A130), thread resumption (A57). |
| Tasks | Partly | Task ID and status endpoint in asynchronous request-reply (A30); "track correlation IDs and message state to know which tasks have completed" (MD); Supervisor "Error handling and retry mechanisms" (RA). No component. |
| Environments | Absent | "sandbox" appears only for the experimentation phase (E2P); "isolat" hits are about memory and failure isolation. No sandbox, workspace or browser for agents to act in. |
| Scheduling | Partly | Only "Scheduled trigger" for the memory promotion pipeline and the archiving "ETL/Archiving Job" (MP, STM). No "cron"; "trigger" hits are events on memory and release gates. Rate limiting appears as DoS mitigation (TM). |
| Memory | Fully | Four memory chapters (A42-A73). The most detailed part of the source. |
| Retrieval | Fully | Knowledge sources, permission-trimmed index, Knowledge Layer, RAG (A47, A48, A125, A149). |
| Artifacts | Absent | "artifact" occurs only as "deployment artifact" (MM) and "versioned artifacts" for prompts (MP). No store for work products. |
| Models | Partly | AI Layer (A16); classifier cost cascade (A143). No model routing component. |
| Tools | Fully | Integration Layer & MCP Server and sub-components (A129-A137). |
| Registry | Partly | Agents only (A11, A22-A26). Tools are discovered through MCP; skills are code functions, not registered definitions. |
| Directory | Absent (partial precursor) | `owners` tag "for categorization or classification" for humans (A26), and endpoint and auth for reaching an agent. Nothing records which area of work is accountable for what. |
| Messaging | Fully | Message-driven communication, broker (A32-A34). |
| Orchestration | Fully | Orchestrator agent, Supervisor agent, communication patterns (A07, A126, A36, A37). |
| Channels | Fully | User Application (A122), client request patterns (A28-A31), API Layer (A20). |
| Identity | Fully | Identity enforcement (A82). |
| Secrets | Partly | "rotating credentials for long-lived agents" (A82); "Never store credentials, tokens, or passwords" in memory (LTM); but the registry generates and stores credentials (A132, A144). No secret store. |
| Policy | Fully | Policy Engine (A141), RBAC, retention policies (A61, A84). |
| Approvals | Partly | Human review queues and gates around development and memory: governance gates (A104), "queue for human review" for memory candidates (MP), human review of disputed tool calls (TC), "human-in-the-loop controls" at maturity level 4 (MAT). No run-time hold of an agent's action for a person. |
| Observability | Fully | A74, A75, A89. |
| Evaluation | Fully | A76-A81, A103. |
| Improvement | Partly | Evaluation feedback loop (A79), iterative optimization loop (A106), level-4 "self-versioning proposals" (A121). All are human practices or a future maturity level; no component. |
| Releases | Fully | Versioning chapters (A113-A120), A91. |
| Reliability | Partly | Failure isolation principle (A05), circuit breakers, dead-letter queues, monitor component uptime (A25), SLOs (A92), registry "Backup and recovery mechanisms". No restoring service. |
| People layer | Partly | Governance committee (A98), Admin in the registration sequence, users. |
| Domains layer | Partly | Specialized agents per "domain" (A08, A127); supervisors for "groups of related agents" (A126). No charter, no domain separate from its agents. |
| Platform layer | Partly | Not named. Its content is spread over the reference architecture's components. |
| Infrastructure layer | Partly | Deployment options (A12, A13), storage layer, local vs remote (A128). |
| Providers layer | Partly | External tools, AI models (diagram "External Tools"). |
| Goals | Partly | "Goal" participant that confirms "intent and goal alignment" (PAT#3); evaluation "against defined success criteria and business requirements". Per agent, not per area of work. |
| Roles | Partly | Each specialized agent's "distinct area of expertise". Role and agent are not separated. |
| Workflow | Partly | Orchestrator plans; chained sequencing. Built per request by the orchestrator, not defined for an area of work. |
| Domain knowledge | Fully | Knowledge Layer "domain-specific information" (A125); "domain business rules" as semantic memory (MEM). |
| Domain tools | Partly | Each agent's MCP tools; "Specialized algorithms for domain-specific tasks" (RA). |
| Domain rules | Partly | Tool policies (TC: "Define tool policies"); "Certain tools may be restricted by role or context". |
| Acceptance criteria | Partly | Specialized agent evaluation: "Measure accuracy and completeness of domain-specific outputs" (EV). |
| Directory (as a whole) | Absent | See Directory row. |

### A.4 Findings

**(a) Misfits and spans, and what each suggests about WARM**

| Item | Kind | What it suggests |
|---|---|---|
| A124 Classifier (intent routing at intake) | Misfit | A missing responsibility or a boundary in the wrong place. Choosing which agent receives an inbound request is done before any agent runs, so WARM's agent-consults-the-Directory story does not cover it. Either Channels routes as well as carries, or Orchestration includes intake routing, or the Directory is queryable by intent. Microsoft builds a whole pattern on it (A143). |
| A93 Manual override (pause or disable an agent class) | Misfit | A missing responsibility: suspending or quarantining an agent or a class of agents at run time. Candidate home: Policy (deny all actions of an actor) or Reliability; WARM states neither. |
| A66 User control over memory | Misfit | The person-as-subject relation, which WARM flags as undeveloped, has concrete platform duties here: see, edit, delete, opt out, incognito. Suggests Policy's rules on stored data include subject-initiated requests, and Memory supports them. |
| A109 Semantic cache | Misfit | Caching. WARM v0.11 recorded it from one platform and did not adopt it; Microsoft is a second source. Still probably an implementation concern of Models, Registry or Retrieval rather than a service. Low weight. |
| A153 Planner | Misfit, out of scope | Nothing. WARM excludes single-agent reasoning. |
| A07, A123, A126 Orchestrator, Supervisor | Span | The source's central component bundles Orchestration, Tasks, Harness and the planning and synthesis of the answer. WARM's split (Orchestration coordinates, the agent does the work) holds, but Microsoft never separates them. Nothing to change; a mapping must record the bundle. |
| A11, A26, A132, A83, A118 Registry variants | Span | Microsoft's registry holds reach information (endpoint, auth), owners, credentials, health, approval records and risk classes, and enforces capability declarations. Evidence that in practice "registry" is a broad governance record. Supports WARM's separate Directory for reach and ownership; contradicts WARM on credentials (Secrets) and on enforcement. |
| A131 Agent State | Span | One store for status, configuration, runtime state and learned behavior. WARM's cut by "what is kept" (Sessions, Tasks, Memory, Registry) is a refinement Microsoft does not make. Nothing to change. |
| A71, A57, A41 Memory pipelines, resumption, STM | Span | Microsoft's "memory" covers what WARM splits across Harness, Sessions and Memory. Consistent with WARM's table "Where what an agent knows is kept". |
| A72 Session-end pipeline (staging tier) | Strained | A staging tier of candidate facts awaiting promotion. Could be stated as part of Memory's "keep it current". |
| A119 Rollback snapshots including memory | Span | A boundary question: WARM's Releases versions agents, skills, platform and infrastructure, and says memory persists through a definition change. Microsoft wants memory state inside a rollback. WARM should say whether a release can roll memory back. |
| A27, A104, A116 Registration evaluation, governance gates, shadow agents | Span | The Operations chain (Evaluation, Approvals, Releases) is used as a unit around admission. Consistent with WARM; no change. |
| A53, A48, A94 Scoping, permission-trimmed retrieval | Span | Access rules enforced inside Memory and Retrieval queries. Consistent with WARM's enforcement-point condition on Governance. |
| A21, A15 Service and agent layers | Span | Code layering, not a responsibility model. Nothing. |

**(b) Relations Microsoft states that WARM does not, or that contradict WARM**

1. *Registry as enforcement point.* "Agent registry enforces capability declarations and metadata tagging. Only approved capabilities can be executed in runtime" (SEC) and "Enforce RBAC on registry lookups" (TM). WARM: the Registry holds definitions; Policy enforces; and "Finding a destination grants nothing". Microsoft gates the lookup itself. Contradicts WARM's placement; a mapping would record Policy implemented inside the registry.
2. *Registry issues identity and credentials.* Pattern 2's sequence: "Generate agent ID and credentials" inside the registry. WARM has Identity and Secrets separate from the Registry.
3. *Registration is a release gate.* Registration includes evaluation and may be denied (PAT#2). WARM's Releases makes changes; WARM does not state that being registered is the point at which an agent is released. A relation WARM could state: Registry admission is a Release that Evaluation and Approvals can gate.
4. *Orchestrator routes all communication.* "it's recommended to route all communication through the orchestrator ... Avoid direct agent-to-agent messaging unless necessary" (BB); and the orchestrator "Approve[s] direct communication" (PAT#9). WARM leaves the topology open and puts permission in Policy; here the orchestrator acts as a policy point. Not a contradiction of WARM, which is topology-neutral; a stated preference WARM does not take.
5. *Evaluation analyzes observability data.* "Observability gives us metrics, but evaluation is the process of analyzing that data" (OBS). Matches WARM (Observability records, Evaluation judges).
6. *Memory is not knowledge.* "Knowledge sources ... act as long-term recall, not memory" (MEM). Matches WARM's Memory/Retrieval cut, stated more sharply than WARM states it.
7. *Procedural memory.* Microsoft keeps "Learned workflows and methods" in memory unless written down, in which case they belong "in a knowledge source or in a tool". WARM v0.11 puts written procedures (skills) in the Registry, not in Retrieval or Tools. Partial contradiction: Microsoft would put a written runbook in Retrieval. WARM's answer depends on whether the runbook is a skill an agent loads (Registry) or material it fetches (Retrieval); WARM does not draw that line.
8. *Version includes memory.* "versioning must account for code and model changes as well as memory snapshots" (BEH). Contradicts WARM's statement that memory persists through a change of definition, harness or model. Microsoft's point is reproducibility: behavior depends on memory too.
9. *Governance and Operations are not separate groups in Microsoft.* Its Governance chapter is organizational (committee, RAI policy, red-teaming); its Security chapter holds the run-time controls. Neither is described as cross-cutting over the others. No contradiction; no confirmation either.

**(c) Domains, ownership, registries, persistence, compared with WARM Step 0, Step 4 and the Directory**

- *Domains.* "These systems reflect the natural structure of organizations: different roles, responsibilities, and domains mapped to individual or composite agents, each optimized for specific knowledge or workflows" (INT). "Specialized agents are domain-focused experts ... Each one is responsible for a distinct area of expertise" (BB). "Each agent focuses on a particular domain (e.g., finance, healthcare, coding) or function (e.g., summarization, research, creative writing)" (RA). Compared with WARM: Microsoft maps a domain onto an agent (or a composite agent); WARM separates the domain (a charter) from the agents that fill its roles. Microsoft's domain grain ranges from an industry (healthcare) to a single function (finding flights, summarization); WARM fixes the grain at "the grain at which an agent of another domain would hand work over".
- *Supervisors over groups.* "Introduce agent supervisors as the architecture scales across domains—these components help manage and abstract groups of related agents. Use hierarchical organization (e.g., supervisor → agent group)" (RA). The nearest thing to a WARM domain with a coordinating agent; the group is defined by similarity of agents, not by a charter.
- *Bounded contexts.* Microservices "Agents encapsulate their own logic, state, and dependencies" listed under "**Bounded Contexts**" (MS). The DDD term is applied to an agent, not to an area of work.
- *Ownership and accountability.* Registry metadata may include "`tags` or `owners`" for "categorization or classification" (REG). "a named owner for the memory data of each scope" (LTM). "in enterprise deployments memory typically belongs to the organization, not the individual" (LTM). "We also need to consider which team in the organization owns the agents, if they are being shared across the enterprise" (BEH). "Output accountability: As agents act autonomously or semi-autonomously, ensuring traceability and responsibility for generated outputs is essential" (GOV). "Define clear roles and responsibilities for model development, approval, deployment, and monitoring" (GOV). Ownership attaches to agents, memory scopes and models, never to an area of work, and "accountability" means traceability of outputs. Nothing like WARM's "exactly one domain is accountable for each responsibility".
- *Registry entries.* An entry is "Agent Information": `name`, `description`, expected input and output, communication mechanism, `url`, `authentication`, and for humans `tags` and `owners` (REG); Registry Storage adds "capabilities, endpoints, security credentials, performance metrics, and version history" (RA); recommendations add "lineage, dependencies, and governance metadata ... audit trails, approval records, and risk classifications" (REC). Entries describe agents (what exists, how to call it). WARM's Registry entry is a versioned definition of an agent, tool or skill; WARM's Directory entry is a scoped responsibility, its accountable domain and how to reach a role. Microsoft's entry carries WARM's "how to reach" but no responsibility and no accountable domain. Microsoft also calls its registry "a dynamic directory", the closest wording to WARM's Directory in any source, but the directory lists agents by capability.
- *Long-lived versus per-task agents.* Microsoft does not distinguish them. The only lifetime language is "rotating credentials for long-lived agents" (SEC) and "Self-Managed Tiered Memory ... autonomous, long-running agents" (MAP). Agents are long-lived services in the registry; specialized agents "may coordinate their own sub-agents" (BB) with no stated lifetime. WARM's persistent/task distinction has no counterpart. Memory is scoped per user, session, project or channel, not per agent.

**(d) Same word, different meaning**

| Term | Microsoft | WARM |
|---|---|---|
| Domain | An agent's area of expertise, from an industry down to a single function ("finding flights") | An area of work defined by a charter, at the grain at which work is handed between areas |
| Skill | "Each 'skill' encapsulates an agent function" (PAT#3); a callable, "stateless, composable" capability (PAT#10) | A packaged set of instructions for a kind of task, held as a versioned definition in the Registry |
| Directory | "like a dynamic directory" describing the agent registry (BB) | A separate service recording accountability for responsibilities |
| Orchestrator | An agent that plans, delegates and synthesizes (BB), or the Semantic Kernel component that also holds context and request lifecycle (RA) | A platform service that coordinates assignments; it does not do the work |
| Memory | Short-term memory = session history; working memory = context; long-term memory = cross-session | Memory = what is learned across sessions only; session history is Sessions; context is Harness |
| Knowledge Layer | Repositories of knowledge and, in the onion version, the interface to "AI models, vector stores, files, web data" | Knowledge is a group (Memory, Retrieval, Artifacts) |
| Governance | Organizational RAI program (committee, policies, training) | A service group (Identity, Secrets, Policy, Approvals) that constrains every other group |
| Artifact | Deployment artifact; versioned prompt artifacts | A work product an agent stores |
| Session | Conversation-bound; "Session ID ... groups all messages within the same conversation" | A stretch of an agent's work, conversational or not |

## B. AWS Prescriptive Guidance on agentic AI

**What it is.** A series of guides, not one document. The guide the task names ("Agentic AI architecture in the enterprise") is a chapter of *Governing and architecting the diversity of agentic AI at scale* (first published 2026-04-23), which is the only guide in the series that presents a layered enterprise reference architecture. *Building serverless architectures for agentic AI on AWS* presents a second, five-layer "serverless reference architecture". The other guides supply vocabulary, patterns and strategy.

**Guides found and what was read.** Page lists come from each guide's `toc-contents.json`; all pages were fetched on 2026-11-11 (23:02 UTC) and converted to text. URLs are `https://docs.aws.amazon.com/prescriptive-guidance/latest/<guide>/<page>.html`. Dates are each guide's own "Document history".

| Guide (path) | Published / updated | Read |
|---|---|---|
| Governing and architecting the diversity of agentic AI at scale (`govern-architect-agentic-ai`) | 2026-04-23 | All 18 pages in full, by this mapper. Code **GA**. |
| Operationalizing agentic AI on AWS (`strategy-operationalizing-agentic-ai`) | 2025-08-12 | All 14 pages in full, by this mapper. Code **OP**. |
| Foundations of agentic AI on AWS (`agentic-ai-foundations`) | 2025-07-14 | All 22 pages in full, by a delegated reader that extracted a verbatim inventory; this mapper assigned from that inventory. Code **F**. |
| Agentic AI frameworks, protocols, and tools on AWS (`agentic-ai-frameworks`) | 2025-07-14; Platforms section added 2026-01-16 | All 29 pages, as for F. Code **W**. |
| Agentic AI patterns and workflows on AWS (`agentic-ai-patterns`) | 2025-07-14 | All 23 pages, as for F. Code **P**. |
| Building serverless architectures for agentic AI on AWS (`agentic-ai-serverless`) | (not checked) | 5 of 24 pages: introduction, core-principles, orchestration-models (skimmed), designing-serverless-ai-architectures (full), pattern-agentic-ai-orchestration (skimmed). Code **SL**. |
| Building multi-tenant architectures for agentic AI on AWS (`agentic-ai-multitenant`) | (not checked) | 2 of 10 pages: agent-fundamentals (first half), employing-control-planes-in-agentic-environments (full). Not inventoried; quoted in findings. Code **MT**. |
| Enterprise multi-account architecture for running agentic AI in production on AWS (`agent-ops-maturity-roadmap-for-enterprise-ai`) | appears in web search | **Could not open**: every URL returned the AWS "page-not-found" page on 2026-11-11. |
| Security for agentic AI on AWS (`agentic-ai-security`); Semantic Layer for Agentic AI using Ontology, Symbolic Reasoning, and Virtual Knowledge Graph | found by web search (PDFs) | Not read. |
| AWS Well-Architected Agentic AI Lens | found by web search; a Well-Architected lens, not Prescriptive Guidance | Not read. |

The delegated reader recorded one gap in P: `agent-patterns` promises "three interrelated dimensions, which are further discussed later in this guide", and no page names them.

### B.1 Inventory and assignment

Rows in the F, W and P tables group items with the same assignment; the **n** column gives the number of named items in the row, and the counts use n. GA, OP and SL rows are one item each.

#### B.1.1 Governing and architecting (GA): the enterprise reference architecture

Pages: INTRO introduction, UC use-case typologies (IP internal productivity, BA business applications), GOV governance (SC governance scope, GM governance models), EA enterprise-architecture, EU gen-AI end-user layer, NG non-gen-AI applications layer, AL agents layer, MA model access, TL tools, KB knowledge bases, XL cross-layer concerns.

| ID | Item | Definition (verbatim, short) | Page | Assignment | Fit | Reason |
|---|---|---|---|---|---|---|
| B001 | Simple chatbot | "answer questions based on internal and public knowledge" | IP | Guidance (use-case class) | G | Classifies applications for governance rigor. |
| B002 | Personal AI assistant | "a digital assistant focused entirely on your individual needs"; "Access rights are tied to each individual user" | IP | Agent concept (persistent agent acting for one person) | S | WARM's persistent agent, but defined by whom it serves, not by a role. |
| B003 | Autonomous team agent | "designed to handle complete workflows for specific organizational roles ... in the background while keeping humans in control at critical decision points" | IP | Agent concept (agent filling a role) | C | An agent holding an organizational role and its workflow, unattended, with approvals. |
| B004 | Domain-specialized business applications | "tailored to specific industries and technical domains" | BA | Guidance (use-case class) | G | Use-case class; "domain" = industry or technical field. |
| B005 | Customer-facing applications | "must handle edge cases gracefully, knowing when to escalate to human agents" | BA | Guidance (use-case class) | G | Use-case class. |
| B006 | Agent, tool, and MCP registry management | "centralized registries documenting all deployed agents, including their capabilities, permissions, security classifications, rate limits, and approval processes, data access patterns, ownership, and business purpose" | SC | Span: Registry + Directory (ownership, business purpose) + Policy (permissions, rate limits) + Observability (performance, incident history) | Sp | The governance record of every asset. |
| B007 | LLM model catalog | "tracks which foundation models are approved for which use cases, including regional availability, quota allocations, and lifecycle information ... their product owners" | SC | Span: Models + Policy (approved uses, quotas) | Sp | WARM's Registry holds agents, tools and skills, not models; nothing in WARM catalogs models. |
| B008 | Quality control and approval processes (agent evaluation frameworks) | "only agents meeting minimum standards can be shared through the organization ... automated testing ... with human review" | SC | Span: Evaluation + Approvals + Releases | Sp | A release gate. |
| B009 | Model approval | "considers performance benchmarks, cost constraints, data residency requirements, and alignment with responsible AI principles" | SC | Span: Evaluation + Approvals | Sp | Gate on adding a model. |
| B010 | Platform standards (approved stack) | "define the approved technology stack for agentic AI development" | SC | Guidance (People decide) | G | Organizational standard. |
| B011 | Governance as code | "embeds policy enforcement directly into the platform" | SC | Policy | C | Rules enforced by the platform. |
| B012 | Sandbox environments (for experimentation) | "designated sandbox environments provide spaces for experimentation with clear boundaries" | SC | Environments | S | Isolation for builders, not for running agents. |
| B013 | Mitigating shadow AI | "Making the governed path more attractive than the shadow path" | SC | Guidance | G | Organizational practice. |
| B014 | Multi-level access and agent permissions | "Each agent operates with a core identity that defines its scope of permissions"; "Agents should only be able to invoke other agents for which they have explicit authorization" | SC | Span: Identity + Policy | Sp | Actor plus rule. |
| B015 | Lineage and audit requirements | "agent and tool invocations be logged with sufficient detail to reconstruct the complete chain of actions" | SC | Observability | C | Evidence. |
| B016 | Access reviews and accountability for decisions | "regular access reviews, detection and escalation procedures for violations, clear accountability for decisions" | SC | Span: People + Policy | Sp | Human review of rules. |
| B017 | Centralized governance | "a single enterprise-wide authority for policies, approvals, and ecosystem management" | GM | Guidance (People layer) | G | Organizational model. |
| B018 | Federated governance | "distributes responsibility to business units while maintaining alignment through shared standards" | GM | Guidance (People layer) | G | Organizational model. |
| B019 | Hybrid governance | "combines centralized oversight with federated execution" | GM | Guidance (People layer) | G | Organizational model. |
| B020 | Citizen developer enablement | "A citizen developer is a business user who creates AI applications without specialized technical skills"; "permissions are extended as they demonstrate competence" | GM | Guidance (builder tooling) | G | Builder enablement. |
| B021 | Template library | "libraries of tested and compliant agent templates, tool integrations, and prompt patterns as building blocks" | GM | Registry | S | Reusable definitions; WARM's Registry holds definitions of agents, tools and skills, not templates. |
| B022 | Applications layer: Generative AI end-user applications | "user-facing applications that enable interaction with agentic AI systems ... They also provide interfaces to schedule and monitor the execution of agents" | EA, EU | Span: Channels + builder tooling (no-code) + Scheduling (schedule) + Observability (monitor) | Sp | A product category, not a responsibility. |
| B023 | Conversational interfaces | "enable natural language interaction with AI agents through chat (text or multimodal) and voice experiences" | EU | Channels | C | Carries requests and results for people. |
| B024 | Productivity augmentation | "integrate AI capabilities directly into daily workflows and productivity tools" | EU | Channels | S | Embedding agents in existing tools. |
| B025 | Citizen-developer (no-code) agent creation | "provide no-code/low-code platforms for creating custom agents" | EU | Guidance (builder tooling) | G | Design-time. |
| B026 | Connector-based integration | "Pre-built and custom connectors that enable seamless integration with third-party applications and data sources" | EU | Tools | C | Connectors. |
| B027 | API-based integration | "RESTful and WebSocket APIs for real-time communication with enterprise systems" | EU | Channels | C | Applications call agents. |
| B028 | Agent-to-system protocols | "Standardized protocols (such as MCP) for connecting AI applications with external data sources and tools" | EU | Tools | C | Tool mediation. |
| B029 | Event-driven patterns | "Webhook and event subscriptions ... for asynchronous workflows" | EU | Scheduling | S | Work started by an event; also delivery (Messaging). |
| B030 | Embedded experiences | "Widgets and iframes for seamless integration into existing applications" | EU | Channels | C | Surface. |
| B031 | Identity federation | "Single sign-on (SSO) ... for secure end-user access control" | EU | Identity | C | Who is acting. |
| B032 | Off-the-shelf vs custom applications | "Organizations can choose between two primary approaches" | EU | Guidance | G | Build choice. |
| B033 | Applications layer: Non-GenAI applications | "business systems ... not inherently agentic but can consume agentic AI services or expose their functions as tools that agents can invoke" | EA, NG | Span: Providers (systems the platform calls) + Channels (systems that call agents) | Sp | A layer for the enterprise's own systems of record; WARM's Providers are "what the platform calls and does not operate". |
| B034 | Bidirectional integration | "applications both consume AI services and provide capabilities to agents" | NG | Span: Channels + Tools | Sp | Both directions. |
| B035 | Business logic access | "exposes domain-specific rules and processes that agents can leverage" | NG | Domain part: domain tools (carrying domain rules) | S | WARM: a domain's rules may "stay in the domain's own logic"; here they live in an external system exposed as a tool. |
| B036 | System of record integration | "connects agents to authoritative data sources for reading and writing business data" | NG | Domain part: domain tools | C | A connection this work needs. |
| B037 | Process automation | "allows agents to initiate and participate in enterprise workflows" | NG | Domain part: workflow | S | The workflow lives in an enterprise system outside the agent platform. |
| B038 | Secure delegation | "enables agents to act on behalf of users with appropriate permissions" | NG | Identity | C | "on whose behalf". |
| B039 | Tool exposure (function wrapping, parameter validation, response formatting) | "business functionality exposed as callable tools that agents can invoke using protocols such as MCP" | NG | Tools | C | Mediation. |
| B040 | Event-driven integration (state change notifications, process triggers, alert generation) | "systems publish events when business objects change" | NG | Scheduling | C | Work started by an event. |
| B041 | Data access patterns (direct querying, cached views, permission-aware access, semantic transformation, knowledge graphs) | "Permission-aware access – data access that respects user authorization contexts" | NG | Retrieval | S | Fetch, with access rules and indexing folded in. |
| B042 | Authentication context propagation | "ensuring that user identity is preserved when agents act on their behalf ... on-behalf-of tokens" | NG | Span: Identity + Secrets | Sp | Actor and credential. |
| B043 | Rate limiting (protect enterprise systems) | "protecting traditional enterprise systems that were designed for human access from overload" | NG | Scheduling | S | WARM's Scheduling covers "limits on how much may run at once"; this limit is on calls to one tool target. |
| B044 | Maintenance window coordination | "ensure that agents are not trying to access systems during maintenance window hours" | NG | Policy | S | A time rule on whether an action may proceed. |
| B045 | Credential management | "secure storage and rotation of secrets necessary for agent to access tools and other systems" | NG | Secrets | C | Same. |
| B046 | Error handling | "graceful degradation when backend systems are unavailable" | NG | Reliability | S | Degradation in the caller, not restoring a service. |
| B047 | Semantic or format transformation | "converting between AI-friendly formats and enterprise data structures" | NG | Tools | S | Adapter logic. |
| B048 | Agents layer | "the central coordination hub for interactions between users, foundation models, tools, and knowledge sources ... contains the agent runtime environments, orchestration mechanisms, and supporting infrastructure" | EA, AL | Span: Runtime group (Harness, Sessions, Environments) + Memory + Registry + Messaging + Orchestration + Identity + Policy + Evaluation | Sp | AWS's layer = most of WARM's platform; model access, tools and knowledge are split off as "core services". |
| B049 | Agent execution | "Agents can run in autonomy for hours, need to retain context and at the same time be fully isolated from other agent instances ... persist conversation across executions, and secure ways to execute code and interact with browser" | AL | Span: Harness + Sessions + Environments | Sp | Three Runtime services. |
| B050 | AgentCore Runtime (as runtime component) | "executing agents securely at scale ... session persistence and isolation, large payloads, multi-protocol support and bidirectional streaming" | AL | Span: Harness (hosting) + Environments + Sessions | Sp | A harness-product bundle. |
| B051 | AgentCore Memory (as memory component) | "persistence for both short-term conversation history and long-term extracted insights" | AL | Span: Sessions + Memory | Sp | Two WARM services in one product; "can be shared across agent sessions with fine-grained access control" adds Policy. |
| B052 | AgentCore Identity (as identity component) | "authentication with IAM and OAuth providers for both inbound and outbound"; "centralized identity and credential management service" | AL, SC | Span: Identity + Secrets | Sp | Outbound credentials are Secrets. |
| B053 | Compute for agent logic (Lambda; ECS/Fargate) | "serverless computing for custom agent logic and tool implementations"; "container-based agent deployments" | AL | Infrastructure | C | Where things run. |
| B054 | Agent registry and catalog | "Agent capabilities, permissions, and purpose; Metadata on ownership, version history, and dependencies; Performance metrics and usage statistics; Approval status and governance classifications" | AL | Span: Registry + Directory (ownership, purpose) + Approvals (approval status, access requests) + Policy (permissions) + Observability (usage) | Sp | Key evidence: "Registries should support self-service access requests and authorization delegation to the tool or agent owners." |
| B055 | Multi-agent coordination | "agent-to-agent communication through standardized protocols ... message formatting and state sharing conventions, appropriate state isolation, authentication and authorization between collaborating agents, and permissions verification for delegated actions" | AL | Span: Messaging + Orchestration + Identity + Policy | Sp | Four services. |
| B056 | Event backbone (EventBridge, as component) | "event-driven backbone for multi-agent messaging" | AL | Messaging | C | Delivery. |
| B057 | Workflow orchestration (Step Functions, as component) | "orchestration for complex multi-agent workflows with checkpoints and error recovery" | AL | Span: Orchestration + Tasks | Sp | Coordination plus durable run tracking. |
| B058 | Agent state store (DynamoDB, as component) | "fast, scalable storage for agent state and shared memory" | AL | Span: Sessions + Memory | Sp | One store, two WARM services. |
| B059 | Agent quality and safety | "evaluation frameworks for reliability and accuracy, safety testing ..., performance monitoring and regression detection, and feedback loops for continuous improvement" | AL | Span: Evaluation + Observability + Improvement | Sp | The Operations chain. |
| B060 | Guardrails (Bedrock Guardrails, as component) | "content filtering, denied topics, word filters, and sensitive information redaction" | AL, MA | Policy | S | Content rules on model input and output, not action rules. |
| B061 | Agent evaluations (AgentCore Evaluations, as component) | "automated assessment tools to measure how well agents or tools perform specific tasks" | AL | Evaluation | C | Same. |
| B062 | Model and retrieval evaluations (Bedrock Evaluations, as component) | "evaluate LLMs and semantic retrieval systems using programmatic metrics, human evaluators and LLM-as-judge" | AL | Evaluation | C | Same. |
| B063 | Access control and authentication | "identity propagation from users through agent chains, permission boundaries for agent actions and tool access, audit trails of agent decisions and actions, and circuit breakers for abnormal behavior patterns" | AL | Span: Identity + Policy + Observability + Reliability | Sp | "Circuit breakers for abnormal behavior" is the run-time suspension also found at Microsoft (A93). |
| B064 | Gateway interceptors | "request and response interceptor to evaluate, filter, manipulate and block MCP tool calls and responses" | AL | Policy | S | An enforcement point that can also rewrite calls. |
| B065 | Policy engine (AgentCore Policy, as component) | "Cedar-based engine to implement contextual grounded fine-grained authorization on AgentCore data plane operations" | AL | Policy | C | Same. |
| B066 | Secrets store (Secrets Manager, as component) | "secure credential storage and automatic rotation for service accounts" | AL | Secrets | C | Same. |
| B067 | API activity audit (CloudTrail, as component) | "comprehensive API activity logging and audit trail generation" | AL | Observability | C | Evidence. |
| B068 | Alerting and remediation (EventBridge) | "real-time alerting and remediation" | AL | Reliability | S | Remediation; alerting is Observability. |
| B069 | Model access component | "controls access to foundation models with policy enforcement, safety measures including guardrails, and cost tracking/allocation capabilities" | EA, MA | Span: Models + Policy + Observability (cost) | Sp | WARM's Models plus an enforcement point. |
| B070 | Cloud-native model access pattern | "Direct access to cloud provider model services" | MA | Guidance (Models) | G | Choice of implementation. |
| B071 | LLM gateway pattern | "Unified API interfaces across multiple model providers through a controlled intermediary ... centralized policy enforcement ... Consistent monitoring, cost management" | MA | Models | S | Models as WARM defines it, bundling a Policy enforcement point. |
| B072 | Guardrails implementation | "filter inappropriate content, enforce compliance requirements, validate inputs and outputs to prevent prompt injection" | MA | Policy | S | Content rules. |
| B073 | Tools component | "manages discovery and secure execution of tools ... authorization capabilities to ensure tools can be used only by the right actors and for the right context" | EA, TL | Span: Tools + Registry (discovery) + Policy | Sp | Three services. |
| B074 | In-runtime tools | "Tools execute directly within the agent's runtime environment as inline function calls" | TL | Guidance (Tools) | G | Arrangement. |
| B075 | Direct access with remote tools | "Agents invoke tools through direct connections to remote services using standardized protocols" | TL | Guidance (Tools) | G | Arrangement. |
| B076 | Tools gateway pattern | "A centralized gateway service manages tool discovery, security, versioning, and invocation" | TL | Span: Tools + Registry + Policy + Releases + Observability | Sp | A gateway that is also the tool catalog. |
| B077 | Tool governance considerations | "Tool registration and approval workflows ... Access control policies ... Usage tracking ... Version management ... Quality validation ... Discovery and search" | TL | Span: Registry + Approvals + Policy + Observability + Releases + Evaluation | Sp | Six services. |
| B078 | Tools gateway (AgentCore Gateway, as component) | "centralized tool server providing a unified interface where agents can discover, access, and invoke tools" | TL | Span: Tools + Registry | Sp | Catalog in the gateway. |
| B079 | Targets and REST API transformation | "each target (API, MCP server, or service) exposes multiple tools"; "converts existing REST APIs into MCP servers" | TL | Tools | C | Mediation. |
| B080 | Code execution and browser tools | "secure and scalable access to isolated code execution and web browsing environments" | TL | Environments | C | Places to act. |
| B081 | Knowledge bases component | "provides access to enterprise data through knowledge bases that can leverage vector stores, graph storage ... It also provides role-based access control" | EA, KB | Span: Retrieval + Policy | Sp | Fetch with access rules. |
| B082 | Retrieval Augmented Generation | "agents retrieve relevant information from a knowledge base through semantic search, then provide that retrieved context to the LLM" | KB | Retrieval | C | Fetch from named sources (the Harness places it in context). |
| B083 | Vector and graph database options | "Organizations select vector databases based on specific requirements" | KB | Guidance (Infrastructure) | G | Product choice. |
| B084 | Knowledge base governance | "data lineage tracking ... Access control ... Data retention and lifecycle management ... retrieval quality metrics ... Source attribution ... multi-tenancy isolation" | KB | Span: Retrieval + Policy + Observability + Evaluation | Sp | Four services. |
| B085 | Cross-layer concern: Observability | "end-to-end request tracing ...; performance monitoring ...; cost tracking with granular attribution to business units or applications; quality monitoring ...; and usage analytics" | XL | Span: Observability + Evaluation (quality monitoring) | Sp | Cross-cutting, as WARM's Operations group. |
| B086 | Cross-layer concern: Security | "identity and access management ... Data protection ... Prompt security ... Supply chain security validating models and dependencies ... Network isolation" | XL | Span: Identity + Policy + Infrastructure + Releases (supply chain) | Sp | WARM treats security as a concern, not a group, as AWS does. |
| B087 | Cross-layer concern: Discoverability | "Observability, security and discoverability span multiple layers" (named on EA; not defined on XL) | EA | Registry | S | WARM has discovery inside one working service (Registry); AWS makes it cross-cutting. Named, never defined. |

#### B.1.2 Operationalizing (OP)

Pages: IN introduction, FA focus-areas, F1 intent-scope, F2 composability, F3 multitenancy, F4 trust, F5 lifecycle, F6 model-alignment, SD software-delivery, PB preparing-business.

| ID | Item | Definition (verbatim, short) | Page | Assignment | Fit | Reason |
|---|---|---|---|---|---|---|
| B088 | Agent intent and scope (role definition) | "What specific outcome is the agent responsible for? Who is it acting on behalf of? Who benefits? Where does the agent's autonomy begin and end? What happens when it fails?"; "A well-scoped agent has a clear job, defined responsibilities, and measurable success criteria" | F1 | Span: domain parts goals + roles + domain rules + acceptance criteria | Sp | A charter written per agent rather than per area of work. |
| B089 | Agent evolutionary model (observer, assistant, autonomous, orchestrator, innovator agents) | "The agent autonomy, complexity, and business impact progressively increases" | F1 | Guidance | G | A maturity scale for agent design. |
| B090 | Agents modeled as departments | "Model agents like organizational departments: modular, specialized, and interoperable" | F2 | Guidance (Domains) | G | Maps a department to an agent; WARM maps a department to a domain charter. |
| B091 | Multi-agent orchestration patterns (swarm, graph, hierarchical) | "help agents discover capabilities and request services from one another dynamically" | F2 | Guidance (Orchestration) | G | Patterns. |
| B092 | Arbiter agent | "a neutral authority that facilitates task delegation based on known capabilities and fallback strategies ... makes sure that sensitive or regulated tasks are routed only to agents that meet identity and policy requirements. It acts as a gatekeeper for policy-bound workflows" | F2 | Span: Orchestration + Policy, provided by an agent | Sp | WARM's provisional "platform service provided by an agent". |
| B093 | Self-coordinating peer agents | "delegate sub-tasks, share context, and resolve dependencies directly" | F2 | Guidance (Orchestration, Messaging) | G | Topology. |
| B094 | Specialized role classes (decision, knowledge, execution agents) | "Decision agents, such as policy enforcers, resource allocators, and risk evaluators" | F2 | Agent concept (role) | S | Roles typed by function; several (policy enforcers, quality controllers) are WARM platform services. |
| B095 | Scaling rules | "load-based agent instantiation, context-aware resource allocation, and automated capability discovery and registration" | F2 | Span: Scheduling (start agents on load) + Registry | Sp | Two services. |
| B096 | Distributed messaging substrate | "ready-to-use modules within a distributed messaging substrate" | F2 | Messaging | C | Delivery. |
| B097 | Agent templates, versioning, CI/CD | "Adopt versioning, CI/CD pipelines, and agent templates" | F2 | Span: Releases + Registry | Sp | Change and definitions. |
| B098 | Capability registries (control plane) | "define what each agent can do and support versioned metadata for peer discovery" | F2 | Registry | C | Versioned entries, found when needed. |
| B099 | Task arbitration logic (control plane) | "uses arbiter or supervisor agents to route tasks based on context, availability, and policy" | F2 | Span: Orchestration + Policy | Sp | Coordination with a policy check. |
| B100 | Lifecycle and state tracking (control plane) | "enables real-time decision context and safe handoffs" | F2 | Span: Tasks + Sessions | Sp | Run tracking plus state for handoff. |
| B101 | Agentic platform abstractions | "Standardized communication protocols ... Built-in orchestration logic and dynamic routing ... Shared context and memory management between agents ... Fallback handling and graceful degradation" | F2 | Guidance (Messaging, Orchestration, Memory, Reliability) | G | A list of what a platform should provide. |
| B102 | Dynamic configuration toggling (AppConfig) | "safe, dynamic configuration toggling across agent instances"; "manage agent behavior by tenant or environment" | F2, F3 | Releases | S | Run-time feature flags change behavior without a release of the definition; WARM's Releases "versions and releases changes". |
| B103 | Shared artifacts and agent-generated outputs store | "storing structured prompt histories, shared artifacts, or agent-generated outputs" | F2 | Artifacts | S | A store for outputs; no versions stated. |
| B104 | Multi-tenancy | "Architect agents and orchestration platforms with tenant-aware memory, configuration, and identity"; "Build agent deployment as a service" | F3 | **Misfit** | M | Tenancy has no WARM place. v0.11 recorded it from one platform and did not adopt it; AWS gives it a whole guide and a focus area. |
| B105 | Tenant-aggregated observability | "a unified observability layer where agent telemetry is aggregated by tenant context" | F3 | Observability | S | Attribution by tenant. |
| B106 | Identity-first control system | "Each agent must operate with a verifiable identity, scoped permissions, and traceable execution history ... audit, reverse, or restrict agent actions" | F4 | Span: Identity + Policy + Observability | Sp | "reverse" agent actions (compensation) has no WARM place. |
| B107 | Runtime guardrails | "rate controls and throttling based on behavioral patterns or workload conditions, resource boundaries enforced alongside auto-scaling, and decision scoring to evaluate risk" | F4 | Policy | S | Includes risk scoring of decisions, beyond allow/deny. |
| B108 | Human-in-the-loop triggers | "Build triggers to engage human-in-the-loop workflows when thresholds are exceeded" | F4 | Approvals | C | Hold for a person on a rule. |
| B109 | Transparency and explainability | "structured telemetry through logging, traces, and reasoning summaries ... decision trails and impact tracing ... drift detection" | F4 | Span: Observability + Evaluation | Sp | Evidence and judgment. |
| B110 | Reflective agents | "continuously observe agent behavior and system patterns ... contribute to governance feedback loops that can initiate revalidation, adaptation, or decommissioning of capabilities" | F4, PB | Span: Observability + Evaluation + Improvement, provided by agents | Sp | Operations services implemented as agents. |
| B111 | Governance boards | "review agent policies, approve capability changes, and oversee incident response protocols" | F4 | People layer | C | People who direct and approve. |
| B112 | AgentOps (agent CI/CD, version histories) | "CI/CD pipelines that are tailored for agents ... test prompt outputs, validate tool integrations ... Maintain version histories of prompts, policies, and model interactions" | F5 | Span: Releases + Evaluation | Sp | Release pipeline with tests. |
| B113 | Improvement register and feedback loops | "Use feedback loops from observability data to initiate retraining, prompt tuning, or agent retirement. Incorporate system-wide reflection mechanisms, such as an improvement register" | F5 | Improvement | C | Evidence turned into proposed changes. |
| B114 | Performance telemetry dashboard | "shows decision accuracy, latency, cost, and reliability" | F5 | Observability | C | Evidence. |
| B115 | Agent artifacts and training data storage | "Amazon S3 and Amazon Elastic File System (Amazon EFS) for storing agent artifacts and training data" | F5 | Releases | S | Build artifacts of agents (term clash with WARM Artifacts). |
| B116 | Retraining and fine-tuning workflows | "Use AWS Step Functions to automate complex retraining or validation workflows ... custom model tuning or fine-tuning" | F5 | **Misfit** | M | Training a model for an agent. Models only mediates calls; Improvement and Releases name agents, skills, platform and infrastructure, not models. |
| B117 | Business model alignment (pricing per decision, session or outcome; ROI metrics; marketplace) | "Define pricing strategies based on decisions, sessions, or outcomes" | F6 | **Misfit** | M | Metering and monetization. Commercial, mostly out of scope; v0.11 recorded payments and did not adopt. The metering part touches Observability. |
| B118 | Zones of intent | "a bounded space where an agent can operate with autonomy, within constraints. You specify the what (the desired outcome), the why (the intent), and the guardrails" | SD | Span: domain parts goals + domain rules | Sp | A charter for one agent's autonomy. |
| B119 | Delivery lifecycle for agentic AI (intent design, scaffolding, behavioral evaluation, continuous orchestration, feedback and adaptation) | "Testing becomes behavioral evaluation"; "Shift from acceptance criteria to behavioral guardrails" | SD | Guidance | G | Delivery process; contradicts WARM's "acceptance criteria" wording (B.4b). |
| B120 | New delivery roles (intent designers, behavioral testers, observability engineers) | "become core to delivery" | SD | Guidance (People) | G | Organization. |
| B121 | AgentOps teams | "These teams jointly own the entire lifecycle of an agent, from design and deployment to retraining and monitoring" | PB | People layer | S | Owners of agents, not of areas of work. |
| B122 | Human handoff protocols | "clear handoff protocols for when agents should escalate decisions to a higher authority or delegate parts of the process to a human collaborator" | PB | Span: Approvals + Orchestration (assignment to a person) | Sp | Escalation and delegation to people. |
| B123 | Centers of excellence and training | "Create centers of excellence to share best practices" | PB | Guidance | G | Organization. |
| B124 | A2A (peer interaction) | "allows agents to negotiate task ownership, share context, and coordinate workflows" | PB | Span: Messaging + Orchestration | Sp | Protocol for delivery and assignment. |
| B125 | MCP (context exchange) | "shared schemas for exchanging contextual data between agents and their environments. It standardizes how functions are invoked" | PB | Tools | C | Tool mediation. |
| B126 | Capability platform | "a unified intelligence layer ... Agents become modular, reusable, and discoverable services" | PB | Guidance | G | Vision. |
| B127 | Decision-first KPIs (decision quality, time-to-action, cognitive offload) | "evaluate decision quality, time-to-action, and responsiveness to change" | PB | Evaluation | S | Business measures of agent decisions. |

#### B.1.3 Serverless reference architecture (SL)

Page: designing-serverless-ai-architectures, unless stated.

| ID | Item | Definition (verbatim, short) | Page | Assignment | Fit | Reason |
|---|---|---|---|---|---|---|
| B128 | Event trigger or interface layer | "the entry point to your serverless AI system. It captures user interactions, system events, or data changes and emits them as structured events" | SL | Span: Channels + Scheduling (events) | Sp | Both of WARM's trigger services. |
| B129 | Processing layer | "transforms or enriches data before passing it to the AI model ... input validation, formatting, metadata tagging, language detection, and data enrichment" | SL | Span: Harness (prepare context) + Orchestration (branching) + domain logic | Sp | A pipeline stage. |
| B130 | Inference layer | "runs the machine learning (ML) or foundation model (FM) inference ... Integrate Retrieval Augmented Generation (RAG) context" | SL | Span: Models + Retrieval | Sp | Includes predictive and classification models. |
| B131 | Post-processing or decisioning layer | "refines or acts upon the inference results ... make decisions based on model confidence, classifications, or external business rules" | SL | Span: Tools + Orchestration + domain rules | Sp | A pipeline stage. |
| B132 | Output or storage layer | "handles the delivery of results to users or systems and persists structured outputs for auditing, analytics, or feedback loops" | SL | Span: Channels + Artifacts + Observability | Sp | A pipeline stage. |
| B133 | Design considerations across layers (resilience, observability, security, cost, extensibility) | "Each layer should fail and retry independently" | SL | Guidance | G | Cross-cutting advice. |
| B134 | Traditional event-driven four layers (application, orchestration, service, data) | "the system is structured into four logical layers" | SL | Guidance | G | Background. |

#### B.1.4 Foundations (F)

| Row | Items (n) | Definition sample (verbatim) | Page | Assignment | Fit | Reason |
|---|---|---|---|---|---|---|
| B135 | Pillars and agency: autonomy, asynchronicity, agency, goal-directed behavior, decision-making, contextual reasoning (6) | "Agents pursue objectives and evaluate progress toward them." | three-pillars | **Misfit** (out of scope) | M | Properties of a single agent's behavior. |
| B136 | Delegated intent (1) | "Agents act on behalf of a person, system, or organization and have an embedded sense of purpose." | three-pillars | Identity | S | WARM's Identity records "on whose behalf"; the "sense of purpose" is the agent's. |
| B137 | Actor model, its attributes, multi-agent systems (3) | "Each actor encapsulates its own state, interacts solely through asynchronous message passing, and can create new actors and delegate tasks." | actor-agent-cognition, autonomy-to-ai | Guidance (lineage of Messaging, Orchestration) | G | Background theory. |
| B138 | Nwana typology attributes: autonomy, social ability, reactivity, proactivity, adaptability and learning, mobility (6) | "The agent interacts with other agents or humans by using communication mechanisms." | nwana-typology | **Misfit** (out of scope) | M | Agent properties. |
| B139 | Continuity (1) | "The agent operates persistently over time, without requiring constant human intervention." | nwana-typology | Agent concept (persistent agent) | S | Persistence of operation, not of identity and memory. |
| B140 | Beliefs and intentions; perceive, reason, act loop (5) | "Agents analyze current beliefs, goals, and contextual knowledge by using a plan library or logic system." | autonomous-collaboration, perceive-reason-act | **Misfit** (out of scope) | M | Single-agent cognition. |
| B141 | Core modules: perception, cognitive, goals, planning, decision-making, action, physical actuation, integrated interaction, learning, learning modes x3; traditional perceive, reason, goals and plans, decision-making, act, actuators, execution (19) | "The cognitive module serves as the deliberative core of the software agent." | core-modules, traditional-agents | **Misfit** (out of scope) | M | Internal architecture of one agent, which WARM Step 0 excludes. |
| B142 | Tool invocation; act channel "Tools" (2) | "Agents often extend their capabilities by using specialized tools to accomplish sub-tasks" | core-modules, traditional-agents | Tools | C | Tool calls. |
| B143 | Short-term memory (module) (1) | "Stores transient context, such as dialogue state, current task information, and recent observations." | core-modules | Sessions | S | Also holds task information (Tasks). |
| B144 | Long-term memory (module); reason sub-module Memory; agent store (3) | "Agent state, user history, decisions, and outcomes are stored in a long-term agent memory store" | core-modules, traditional-agents, generative-ai-agents | Memory | C | Retained across sessions. |
| B145 | Knowledge base (reason sub-module); RAG (2) | "Provides access to symbolic rules, ontologies, or learned models (such as embeddings, facts, and policies)." | traditional-agents, generative-ai-agents | Retrieval | S | The knowledge base also holds "policies", which WARM puts in Policy. |
| B146 | Generative-AI enhancements: LLMs as cognitive engines, tool use through prompting, context-aware planning, prompt context as memory, in-context learning, in-context prompt chaining (6) | "Instead of using symbolic knowledge bases, agents encode memory, plans, and goals as prompt tokens" | generative-ai-agents | Harness | S | Context assembly and the loop; planning parts are out of scope. |
| B147 | Continued pretraining and fine-tuning (1) | "LLMs can be continued pretrained on custom collections" | generative-ai-agents | **Misfit** | M | Model training (as B116). |
| B148 | Taxonomy classes: traditional AI, software agents, agentic AI (3) | "Agentic AI ... brings together autonomy, asynchrony, and agency" | comparison | Guidance | G | Classification. |

#### B.1.5 Frameworks, protocols and tools (W)

| Row | Items (n) | Definition sample (verbatim) | Page | Assignment | Fit | Reason |
|---|---|---|---|---|---|---|
| B149 | Framework (definition) (1) | "prewritten software code that provides a structured environment, common functionality, and the tools and orchestration capabilities" | frameworks | Guidance (builder tooling) | G | Build-time. |
| B150 | Framework capability: agent orchestration (1) | "coordinates the flow of information and decision-making across single or multiple agents" | frameworks | Orchestration | S | Also "decision-making", which is the agents' work. |
| B151 | Framework capability: tool integration (1) | "enables agents to interact with external systems, APIs, and data sources" | frameworks | Tools | C | Mediation. |
| B152 | Framework capability: memory management (1) | "provides persistent or session-based state ... More advanced frameworks incorporate long-term memory" | frameworks | Span: Sessions + Memory | Sp | Two services. |
| B153 | Framework capability: workflow definition (1) | "supports structured patterns like chains, routing, parallelization, and reflection loops" | frameworks | Guidance (Orchestration) | G | Pattern support. |
| B154 | Framework capability: deployment and monitoring (1) | "facilitate the transition from development to production with observability" | frameworks | Span: Releases + Observability | Sp | Two services. |
| B155 | Framework features presented as capability categories: collaboration patterns, model-first design, MCP integration, graph-based workflows, memory abstractions, component library, role-based agent design, task delegation, agent collaboration, process management, conversational agents, asynchronous architecture, code generation, data-centric architecture, workflows orchestration, agentic retrieval, observability and evaluation, managed deployment, observability stack, unified framework (20) | "You define autonomous agents with specific roles, goals, and backstories to enable specialized expertise." | strands-agents, langchain-langgraph, crewai, autogen, llamaindex | Guidance (builder tooling) | G | Features of build frameworks. |
| B156 | Human-in-the-loop (framework feature) (1) | "Support for optional human participation in otherwise autonomous agent workflows when needed." | autogen | Approvals | S | Participation, not only authorization. |
| B157 | Orchestrator agent with ledgers (Magentic-One) (1) | "decomposes high‑level goals and tracks progress by using structured ledgers ... delegates subtasks to specialized agents" | autogen | Span: Orchestration + Tasks + agent | Sp | Coordinator agent. |
| B158 | Bedrock Agents capabilities: fully managed service, API-driven development, action groups, knowledge base integration, advanced prompt templates, tracing, versioning and aliases (7) | "Create multiple versions of your agent and deploy them through aliases for controlled rollouts." | bedrock-agents | Action groups → Tools; knowledge base integration → Retrieval; prompt templates → Harness; tracing → Observability; versioning and aliases → Releases; fully managed service → span (Harness + Infrastructure); API-driven development → guidance | Sp | A harness product. Counted as 5 clean, 1 span, 1 guidance. |
| B159 | Supervisor plus specialized agents (FinOps example) (1) | "a central FinOps Supervisor agent delegates tasks to specialized agents" | bedrock-agents | Guidance (Orchestration) | G | Example arrangement. |
| B160 | Platform (definition) (1) | "provide the foundational runtime, orchestration, and integration layers that you need to deploy, scale, and manage production-grade agentic systems" | agentic-ai-platforms | Platform layer | C | Same idea as WARM's platform, minus domains. |
| B161 | Platform capabilities: runtime orchestration; state, context and memory; security, identity and governance; tool integration; observability and auditability; cross-model interoperability (6) | "Support cross-model interoperability, allowing agents to use multiple foundation models in a single environment." | why-platforms-matter | One WARM group or service each: Runtime + Orchestration; Sessions + Memory; Governance; Tools; Observability; Models | Sp | Six capabilities; four are single services, two are spans. Counted as 4 clean and 2 spans. |
| B162 | Platform types: managed, open-source, hybrid (3) | "Hybrid solutions integrate managed and self-hosted components" | types-of-agentic-ai-platforms | Guidance | G | Procurement choice. |
| B163 | Platform selection considerations (6) | "Choose solutions that provide detailed telemetry, traceability, and audit logs" | platform-selection-considerations | Guidance | G | Criteria. |
| B164 | AgentCore capabilities: Runtime, Memory, Gateway, Identity, built-in tools, Observability (6) | "Provides a secure, serverless, scalable environment to host and run your agents" | amazon-bedrock-agent-core | Runtime → Harness+Environments+Sessions (span); Memory → Sessions+Memory (span); Gateway → Tools+Registry (span); Identity → Identity (clean); built-in tools → Environments (clean); Observability → Observability (clean) | Sp | Counted as 3 clean and 3 spans. Already mapped in WARM v0.11 (AgentCore was one of its three platforms). |
| B165 | AgentCore key features and approaches: fully managed, long/short-term memory, tool discovery through one endpoint, secure infrastructure, observability, session isolation, modularity, gateway ingress/egress auth (8) | "Enable your agents to discover and use tools through a single, secure endpoint." | amazon-bedrock-agent-core, protocol-based-tools | Guidance (restates B164) | G | Feature list of the same product. |
| B166 | MCP (role); MCP Streamable HTTP; MCP inter-agent extension (3) | "MCP provides a communication layer that enables agents to interact with external data and services, and you can also use it to enable agents to interact with other agents." | getting-started-with-mcp, agent-to-agent-protocols | Span: Tools + Messaging | Sp | One protocol for both. |
| B167 | A2A protocol and capability manifest (2) | "allows agents to discover each other, advertise their capabilities, negotiate tasks, and share context ... Each agent publishes a capability manifest" | getting-started-with-a2-a | Span: Messaging + Registry (manifest) + Orchestration (negotiation) | Sp | Three services. |
| B168 | A2A interaction modes: direct peer messaging, semantic task negotiation, capability-based discovery, session anchoring; negotiation patterns (5) | "Semantic task negotiation, where agents select the most suitable peer" | getting-started-with-a2-a | Guidance (Messaging, Orchestration, Registry, Sessions) | G | Interaction patterns. |
| B169 | Communication patterns (request/response, stateful dialogues, multi-agent collaboration, team-based workflows) and protocol considerations (security model, deployment environment, framework compatibility, scalability) (8) | "Hierarchical agent teams with defined roles" | agent-to-agent-protocols | Guidance | G | Selection guidance. |
| B170 | Protocol selection and implementation steps (open standards, maturity, managed services, abstraction layers, etc.) (8) | "Implement adapters between your systems and specific protocols." | selecting-agentic-protocols, implementation-strategy, protocol-selection | Guidance | G | Practice. |
| B171 | Tool categories: protocol-based (MCP, function calling, tool use), framework-native (3 frameworks) (8) | "Protocol-based tools use standardized protocols for agent-to-tool communication" | tool-categories | Tools | C | Kinds of tool interface; counted as 8 clean. |
| B172 | Meta-tools: workflow tools (state management, branching, retry) (4) | "Manage agent execution flow, branching logic, and state management." | tool-categories, meta-tools | Span: Orchestration + Tasks (retry) + Sessions (state) | Sp | Platform responsibilities exposed to the model as tools. Counted as 1 span item and 3 sub-items as guidance. |
| B173 | Meta-tools: agent graph tools (task delegation, result aggregation, conflict resolution) (4) | "Coordinate multiple agents in complex workflows." | tool-categories, meta-tools | Orchestration | S | Orchestration as a tool the model calls. Counted as 1 strained and 3 guidance. |
| B174 | Meta-tools: memory tools (conversation history, knowledge bases, vector stores; MCP resources as memory) (5) | "Provide persistent storage and retrieval of information across agent sessions." | tool-categories, meta-tools | Span: Sessions + Memory + Retrieval | Sp | "Knowledge bases" under memory; counted as 1 span and 4 guidance. |
| B175 | Meta-tools: reflection tools (1) | "Enable agents to analyze and improve their own performance." | tool-categories | Improvement | S | Self-improvement by the agent, not a proposal to a release process. |
| B176 | MCP deployment models: local stdio, local SSE, remote streamable HTTP (3) | "Tools run on remote servers" | protocol-based-tools | Guidance (Tools, Infrastructure) | G | Deployment. |
| B177 | MCP tool security features: OAuth, permission scoping, capability discovery, structured errors (4) | "Fine-grained access control for tools" | protocol-based-tools | Span: Identity, Policy, Registry, Tools | Sp | Counted as 4 items: Identity C, Policy C, Registry S, Tools C. |
| B178 | Tool integration strategy (4) and security best practices (authentication and authorization; data protection; monitoring and auditing) (3) | "Rotate credentials – Regularly update API keys and access tokens." | tool-integration-strategy, security-best-practices-for-tool-integration | Guidance (Tools, Identity, Secrets, Policy, Observability) | G | Practice; counted as 7 guidance. |

#### B.1.6 Patterns and workflows (P)

| Row | Items (n) | Definition sample (verbatim) | Page | Assignment | Fit | Reason |
|---|---|---|---|---|---|---|
| B179 | Pattern categories: agentic patterns, agent patterns, LLM workflows, agentic workflow patterns; agent pattern definition (5) | "Agent patterns are reusable design templates that describe the structure and behavior of individual agents." | introduction, agent-patterns | Guidance | G | Taxonomy of guidance. |
| B180 | Principles (asynchronous, autonomy, agency) and core building blocks (perception, reason, action) (4) | "Agents act with purpose, on behalf of a user or system, toward specific goals" | agent-patterns | **Misfit** (out of scope) | M | Single-agent properties. |
| B181 | Agent patterns: basic reasoning, tool-based (functions), tool-based (servers), computer-use, coding, speech and voice, workflow orchestration, memory-augmented, simulation and test-bed, observer and monitoring, multi-agent collaboration (11) | "Workflow orchestration agents manage and coordinate multistep tasks ... delegate work to subagents or other systems, maintain execution context" | agent-patterns pages | Guidance (each names the WARM services it uses: e.g. computer-use uses Environments; memory-augmented uses Sessions, Memory; observer uses Observability, Scheduling) | G | Single-agent design templates. |
| B182 | Agent RAG (1) | "RAG enables agents to retrieve relevant external information before engaging the LLM." | basic-reasoning-agents | Retrieval | C | Fetch. |
| B183 | Agent shell / orchestration layer (1) | "The input is handed off to the agent shell or orchestration layer. This step includes any preprocessing, prompt templating, and goals identification." | basic-reasoning-agents | Harness | C | The loop's context preparation. |
| B184 | Tool registry (1) | "The agent uses internal metadata or a tool registry to search for available tools, schemas, and relevant capabilities." | tool-based-agents-for-calling-functions | Registry | C | Tool definitions found when needed. |
| B185 | Tool server (1) | "delegating tool execution to an external server that has a dedicated runtime environment for tools, scripts, and composite agents" | tool-based-agents-for-servers | Span: Tools + Environments | Sp | Mediation plus isolated execution. |
| B186 | Agent registries (for worker selection) (1) | "find the right worker agent for the task based on metadata, domain, and prior success rate" | workflow-orchestration-agents | Span: Registry + Directory (by domain) + Observability (success rate) | Sp | Selection "by domain" is Directory-like. |
| B187 | Worker agent (1) | "receives the event or prompt and begins running commands. It can track execution state, retry on failure, and pass intermediate results to the next agent" | workflow-orchestration-agents | Agent concept (task agent) | C | Per-task agent. |
| B188 | Roles in multi-agent collaboration (planner, researcher, executor, critic, explainer); manager agent; supervising agent (3) | "A \"manager\" agent or initiating context defines the objective." | multi-agent-collaboration | Agent concept (role) | S | Roles by cognitive function, not by area of work. Counted as 3 strained. |
| B189 | Shared memory or blackboard (1) | "Multi-agent memory or blackboard system" | multi-agent-collaboration | Span: Memory + Sessions | Sp | Shared working state and memory. |
| B190 | Communication layer (1) | "Messaging and coordination between agents" | multi-agent-collaboration | Span: Messaging + Orchestration | Sp | Both in one layer. |
| B191 | Orchestration layer (1) | "Kickoff, timeout, fallback, and retry logic" | multi-agent-collaboration | Span: Orchestration + Tasks | Sp | Retry and timeout are Tasks. |
| B192 | Agent identification (1) | "Role-based tool or agent invocation and boundary enforcement" | multi-agent-collaboration | Span: Identity + Policy | Sp | Two services. |
| B193 | Emergent interaction (1) | "Enable dynamic task routing or escalation" (via "event pipelines or agent registries") | multi-agent-collaboration | Orchestration | S | Routing through a registry or event bus. |
| B194 | Memory layers: short-term, long-term structured, long-term semantic, storage, orchestration of memory lifecycle, reasoning (6) | "Long-term (structured) ... Facts, relationships, and logs" | memory-augmented-agents | Short-term → Sessions; long-term → Memory (2); storage → Artifacts ("transcripts, structured memories, and files"); memory orchestration → Memory; reasoning → Models | Sp | Counted as 5 clean (Sessions, Memory x2, Memory, Models) and 1 span (storage: Sessions + Memory + Artifacts). |
| B195 | Simulation components (environment, agent logic, feedback loop, memory and replay, visualization) (5) | "Reward tracking, outcome scoring, and behavior logging" | simulation-and-test-bed-agents | Guidance (Environments, Evaluation) | G | Components of one pattern. |
| B196 | Observer components (event ingestion, preprocessing, reasoning engine, storage and memory, alerting and escalation) (5) | "Trigger downstream systems or agents" | observer-and-monitoring-agents | Guidance (Scheduling, Observability, Reliability) | G | Components of one pattern. |
| B197 | LLM-augmented cognition blocks: prompting, retrieval, tool use, memory (4) | "Incorporating persistent or a session-based state into the reasoning loop" | overview-of-llm-augmented-cognition | Harness (prompting) C; Retrieval C; Tools C; Sessions + Memory (Sp) | Sp | Counted as 3 clean and 1 span. |
| B198 | LLM workflows: prompt chaining, parallelization, orchestration, evaluator / reflect-refine loop (4) | "A central orchestrator agent uses an LLM to plan, decompose, and delegate subtasks to specialized worker agents" | workflow-for-* | Guidance (Orchestration; Evaluation for the evaluator loop) | G | Patterns. |
| B199 | Routing workflow; classifier or router agent; dispatcher (3) | "a classifier or router agent uses an LLM to interpret the intent or category of a query, then routes the input to a specialized downstream task or agent" | workflow-for-routing | **Misfit** | M | The same intake routing as Microsoft's Classifier (A124); counted as 1 misfit and 2 guidance. |
| B200 | Agentic workflow patterns; cognition-augmented workflow; enrichment (3) | "Agentic architectures add cognitive augmentation to an event-driven system." | agentic-workflow-patterns | Guidance | G | Patterns. |

### B.2 Counts

Counting rule for grouped rows: each named item counts once, with the split stated in the row's reason.

| Guide | Inventory items | Clean | Strained | Spans | Guidance | Misfits |
|---|---|---|---|---|---|---|
| GA, governing and architecting (the reference architecture) | 87 | 24 | 18 | 30 | 15 | 0 |
| OP, operationalizing | 40 | 7 | 8 | 13 | 9 | 3 |
| SL, serverless reference architecture (five layers) | 7 | 0 | 0 | 5 | 2 | 0 |
| F, foundations | 59 | 5 | 11 | 0 | 6 | 37 |
| W, frameworks, protocols and tools | 128 | 25 | 5 | 16 | 82 | 0 |
| P, patterns and workflows | 64 | 12 | 4 | 8 | 35 | 5 |
| **AWS total** | **385** | **73** | **46** | **72** | **149** | **45** |

Of the 45 misfits, 40 are out of scope by WARM's Step 0 (properties and internal modules of a single agent: B135, B138, B140, B141, B180). The five that bear on WARM are B104 multi-tenancy, B116 and B147 model training, B117 metering and monetization, and B199 intake routing.

The reference architecture proper (GA) has no misfit: every item it names is a WARM service, a span of services, or guidance. Its 30 spans are the finding.

### B.3 Reverse direction: WARM against AWS

Searched with `grep -il` over the GA, OP and SL pages for: schedul, cron, "on a schedule", artifact, "work product", owner, accountab, approv, human-in-the-loop, directory, domain, "business unit", persistent, long-running, ephemeral, per-task, lifetime, tenant, cach, rollback, kill, suspend, decommission. The delegated reader searched F, W and P (its terms and hit counts are in its grep record: registr, catalog, owner, accountab, approv, cron, artifact, version, rollback, secret, credential, identit, govern, compliance, guardrail, policy, audit, human, schedul, trigger, tenant, domain, session, persist). "directory", "cron", "per-task", "lifetime", "suspend" and "work product" have no hit in GA, OP or SL.

| WARM part | AWS has it | Where |
|---|---|---|
| Harness | Partly | Agents layer hosts "agent runtime environments" (B048); runtime product (B050); "agent shell or orchestration layer" (B183). Context assembly is not named as a responsibility in GA. |
| Sessions | Fully | "persist conversation across executions" (B049); AgentCore Memory short-term history (B051); session isolation (B050). |
| Tasks | Partly | Step Functions "checkpoints and error recovery" (B057); "Lifecycle and state tracking" (B100); worker agent "track execution state, retry on failure" (B187). No named service. |
| Environments | Fully | "secure ways to execute code and interact with browser" (B049); code execution and browser tools (B080). |
| Scheduling | Partly | Event-driven integration (B040), end-user "interfaces to schedule ... the execution of agents" (B022), "load-based agent instantiation" (B095), rate limiting (B043). No "cron"; "schedul" hits in GA are use-case text ("organizes your schedule", "Production scheduling agent") and B022. |
| Memory | Fully | "long term memory" of "insights derived from the conversations" (EA); B051, B144. |
| Retrieval | Fully | Knowledge bases component and RAG (B081, B082). |
| Artifacts | Partly | S3 for "shared artifacts, or agent-generated outputs" (B103); output or storage layer (B132). No versions; GA does not mention it. |
| Models | Fully | Model access component, LLM gateway with model routing (B069, B071). |
| Tools | Fully | Tools component and gateway (B073, B076, B078). |
| Registry | Fully | Agent registry and catalog (B054); tool catalog in the gateway (B076); "Agent, tool, and MCP registry" (B006); capability registries (B098). Skills are not named; prompt templates and "agent templates" are (B021, B097). |
| Directory | Partly | Registry entries include "ownership, and business purpose" (B006) and owners who approve access (B054). No entry records which area of work is accountable for a responsibility. |
| Messaging | Fully | Event backbone (B056), messaging substrate (B096). |
| Orchestration | Fully | Step Functions, arbiter and supervisor agents (B057, B092, B099). |
| Channels | Fully | Applications layer (B022-B031), API-based integration (B027). |
| Identity | Fully | B014, B031, B038, B052. |
| Secrets | Fully | Credential management (B045), Secrets Manager (B066). |
| Policy | Fully | Governance as code, AgentCore Policy, interceptors (B011, B064, B065). |
| Approvals | Partly | Human-in-the-loop triggers (B108); "keeping humans in control at critical decision points" (B003); approval of agents and models before sharing (B008, B009). Run-time holds are one sentence in OP; GA states approvals mostly at registration. |
| Observability | Fully | Cross-layer concern (B085), lineage (B015). |
| Evaluation | Fully | Agent quality and safety (B059), evaluations (B061, B062). |
| Improvement | Fully | Improvement register (B113), reflective agents (B110), "feedback loops for continuous improvement" (B059). |
| Releases | Partly | AgentOps CI/CD and version histories (B112), versioning and aliases (B158). "rollback" appears once (OP lifecycle). GA does not describe releases. |
| Reliability | Partly | Error handling (B046), alerting and remediation (B068), circuit breakers (B063). No restoring service. |
| People layer | Fully | Governance models, boards, AgentOps teams, citizen developers (B017-B020, B111, B121). |
| Domains layer | Partly | "business units" (B018, B085), "domain-specialized applications" (B004), "Model agents like organizational departments" (B090). No charter separate from agents. |
| Platform layer | Fully | "Agentic AI platforms provide the foundational runtime, orchestration, and integration layers" (B160); GA's agents layer plus core services. |
| Infrastructure layer | Fully | Compute (B053), vector stores (B083), network isolation (B086). |
| Providers layer | Partly | Model providers through the gateway (B071); third-party systems as non-GenAI applications (B033). |
| Goals | Partly | "What specific outcome is the agent responsible for?" (B088); zones of intent "the what (the desired outcome), the why (the intent)" (B118). Per agent. |
| Roles | Partly | "give it a job title" (B088); autonomous team agents "for specific organizational roles" (B003); role classes (B094). Role and agent not separated. |
| Workflow | Partly | Process automation in enterprise systems (B037); orchestration patterns. Not defined per area of work. |
| Domain knowledge | Fully | Knowledge bases "domain-specific information" (KB); "Business logic access" (B035). |
| Domain tools | Fully | System of record integration (B036); non-GenAI applications as tools (B033). |
| Domain rules | Partly | "Business logic access – exposes domain-specific rules" (B035); guardrails with "domain-specific customization" (B072); zones of intent "the guardrails" (B118). |
| Acceptance criteria | Partly | "measurable success criteria" per agent (B088). OP says to "Shift from acceptance criteria to behavioral guardrails" (B119). |
| Directory (as a whole) | Absent | See Directory row. |

### B.4 Findings

**(a) Misfits and spans, and what each suggests about WARM**

| Item | Kind | What it suggests |
|---|---|---|
| B104 Multi-tenancy (and the whole multi-tenant guide; GA's "multi-tenancy isolation" for shared knowledge bases, B084) | Misfit | A missing concern, probably not a missing service. Tenancy cuts across Identity (tenant identity), Policy (isolation), Memory and Sessions (tenant-scoped data), Observability (per-tenant telemetry) and Releases (per-tenant configuration). WARM v0.11 recorded it from one platform; AWS now gives it a guide and a focus area. Candidate: list tenancy with Security and Cost as a "concern that is not a group", and say which services carry a tenant scope. |
| B116, B147 Retraining and fine-tuning | Misfit | A boundary question for Models, Improvement and Releases: WARM changes agents, skills, platform and infrastructure, never the model weights. If the system trains its own models, the trained model is a released change. Candidate: add models to the list of things Releases versions and Improvement may propose. |
| B117 Business model alignment (pricing, metering, marketplace) | Misfit | Mostly out of scope (commercial). The metering part ("consumption and metering data for billing", MT control plane) is attribution, which WARM puts under the Cost concern and Observability. |
| B199 Routing workflow (classifier or router agent) | Misfit | Same intake-routing gap as Microsoft's Classifier (A124). Second source. |
| B048 Agents layer | Span | AWS groups WARM's Runtime, Interaction, much of Governance and Evaluation into one "agents layer" and splits Models, Tools and Retrieval out as "core services". WARM's Capabilities and Knowledge groups correspond to AWS's core services, which supports WARM's grouping of those three. AWS has no counterpart to WARM's working/cross-cutting distinction except "cross-layer concerns". |
| B006, B054 Registries | Span | The registry entry carries capabilities, permissions, ownership, business purpose, approval status, metrics and incidents. Evidence that practitioners want one governance record per asset; WARM splits it over Registry, Directory, Policy, Approvals and Observability. A mapping can show the split, but WARM should say that one product commonly implements all five. |
| B069, B071, B073, B076, B078 Gateways | Span | Model and tool gateways bundle mediation with policy enforcement, discovery and versioning. WARM's Governance point 1 (enforcement points) predicts this. No change; a mapping records the bundle. |
| B051, B058, B152 Memory products | Span | Short-term and long-term in one product. WARM's cut by what is kept still applies. |
| B088, B118 Agent intent and scope; zones of intent | Span | AWS writes a charter (outcome, beneficiary, autonomy limits, failure handling, success criteria, guardrails) for each agent. These are WARM's domain parts, attached to an agent instead of an area of work. Evidence that WARM's seven parts are recognizable; evidence against WARM's claim that they belong to a domain rather than to an agent. |
| B092, B110 Arbiter agent; reflective agents | Span | Platform responsibilities (policy-checked delegation; evaluation and improvement) provided by agents. Supports WARM's provisional statement that a platform service may be implemented by an agent, and its unresolved rule about how such an agent is repaired. |
| B128-B132 Serverless layers | Span | A request pipeline (trigger, preprocess, infer, postprocess, output). A different axis from WARM's responsibilities; every stage is a span. Nothing to change. |
| B087 Discoverability as a cross-layer concern | Strained | AWS places discovery beside observability and security as cross-cutting. WARM places it in Registry, a working service. A boundary question only if discovery must apply to actions without the agent's cooperation, which AWS does not claim. |

**(b) Relations AWS states that WARM does not, or that contradict WARM**

1. *Registry gates access, and owners approve it.* "Registries should support self-service access requests and authorization delegation to the tool or agent owners. Registries should integrate with MCP gateway access controls to enforce the required access policies" (AL). WARM: "Finding a destination grants nothing"; authorization is Identity, Policy and Approvals. AWS makes the registry the place where access is requested and the owner the approver. Not a contradiction of the separation, but a relation WARM does not state: the Directory's or Registry's owner is the default approver for access.
2. *Tools gateway is the tool registry.* "A centralized gateway service manages tool discovery, security, versioning, and invocation" (TL). WARM separates Tools (mediation) from Registry (definitions). AWS joins them for tools and separates them for agents (B054). Implementation bundling; no change.
3. *Observability, security and discoverability are cross-layer* (EA). Agrees with WARM that observability is cross-cutting; security as a concern also agrees. Discoverability does not (see B087).
4. *Governance as an organizational model.* Centralized, federated, hybrid governance (B017-B019) is a property of how people divide authority, which WARM leaves to People ("People set this division"). AWS says the governance model "is influenced by, and influences, architectural decisions" (GM). WARM states no such coupling.
5. *Acceptance criteria are replaced by guardrails.* "Shift from acceptance criteria to behavioral guardrails"; "some Agile practices become less useful, such as ... strict acceptance criteria" (SD). Contradicts WARM's seventh domain part in wording. AWS's reason is non-determinism. WARM's Evaluation already returns judgments, not identical results, so the contradiction is about the word "acceptance", not about having stated criteria (AWS still asks for "measurable success criteria", B088).
6. *An arbiter agent routes regulated tasks only to eligible agents* (B092). A relation between Orchestration and Policy that WARM leaves implicit: the assignment itself is policy-checked, not only the resulting action.
7. *Reflective agents can initiate "revalidation, adaptation, or decommissioning of capabilities"* (B110). WARM: Improvement proposes, "a person or a release process decides". AWS's wording allows agents to initiate changes; whether a person decides is not stated.
8. *LLM inference is "stateless" and so can be centralized behind a gateway; agentic managed services are stateful and "difficult to abstract"* (GM). A relation between statefulness and governance model that WARM does not state.

**(c) Domains, ownership, registries, persistence, compared with WARM**

- *Business domains.* GA classifies applications by use case, not by area of work: "Domain-specialized applications ... tailored to specific industries and technical domains" (BA). OP: "Use domain-specific problem statements to shape agent responsibilities" (FA); "Model agents like organizational departments: modular, specialized, and interoperable" (F2); agents "need to operate at scale, across departments, domains, and user contexts" (foundation). The serverless guide says its layers give "clear separation of concerns across business domains" (SL). In AWS, a domain shapes an agent; WARM separates the domain's charter from its agents.
- *Business units.* Federated governance "distributes responsibility to business units" (GM); cost attributed "to business units or applications" (XL); multi-tenancy serves "multiple customers, departments, or workflows" (F3). Business units are units of governance and cost, not areas of work with charters.
- *Ownership and accountability.* Registry entries hold "ownership, and business purpose" (SC) and "Metadata on ownership" (AL); the model catalog lists each application's "product owners" (SC); "authorization delegation to the tool or agent owners" (AL); "Without clear ownership, auditability, or policy constraints, they may drift" (F4); AgentOps teams "jointly own the entire lifecycle of an agent" (PB); "clear accountability for decisions" (SC); "operationalize autonomy without surrendering accountability" (SD). Ownership attaches to agents, tools and applications, held by people or teams. WARM attaches accountability to a domain for each responsibility, recorded in the Directory. AWS has owners of assets; WARM has accountable domains for responsibilities. They are different relations and both may be needed: WARM has no "owner of an agent" (the person or team who answers for a definition), and AWS has no "domain accountable for a responsibility".
- *Registries and their entries.* Agent registry entry: "Agent capabilities, permissions, and purpose; Metadata on ownership, version history, and dependencies; Performance metrics and usage statistics; Approval status and governance classifications" (AL). Governance registry entry: "capabilities, permissions, security classifications, rate limits, and approval processes, data access patterns, ownership, and business purpose ... version history, dependencies, performance metrics, and incident history" (SC). Capability registry: "what each agent can do and support versioned metadata for peer discovery" (F2). A2A manifest: `can`, `needs`, `meta` (W). Model catalog: approved use cases, regions, quotas, lifecycle, applications, product owners (SC). WARM's Registry holds versioned definitions of agents, tools and skills; AWS's registry entry holds no definition (instructions, skills) and many governance fields. "business purpose" is the nearest AWS field to a Directory responsibility, but it describes the agent, not a responsibility with one accountable domain.
- *Long-lived versus per-task.* No AWS guide defines the distinction. "Agents can run in autonomy for hours" (AL); "load-based agent instantiation" (F2); worker agents in workflow orchestration that "track execution state, retry on failure" (P); "Continuity: The agent operates persistently over time" (F); AgentCore Memory supports "both ephemeral and long-term memory modes" (SL orchestration-models). The personal assistant (B002) and autonomous team agent (B003) are implicitly persistent agents. WARM's two kinds by lifetime are absent as a stated distinction.

**(d) Same word, different meaning**

| Term | AWS | WARM |
|---|---|---|
| Layer | GA: applications, agents, core services; SL: pipeline stages | People, Domains, Platform, Infrastructure, Providers |
| Domain | An industry or technical field ("specific industries and technical domains"); a problem statement shaping an agent | An area of work defined by a charter |
| Artifact | "agent artifacts and training data" (build outputs, B115); "shared artifacts, or agent-generated outputs" (B103) | A work product stored with versions |
| Orchestration layer | "Kickoff, timeout, fallback, and retry logic" (P), i.e. WARM's Tasks plus Orchestration | Orchestration coordinates assignments; Tasks retries and cancels |
| Agent | "an application" with job title, intent and scope, also a "digital teammate" | An identified actor that fills roles |
| Governance | An organizational model (centralized, federated, hybrid) plus controls | A service group |
| Control plane | MT: operational, management and orchestration mechanisms across tenants; OP: "capability registries ... task arbitration ... lifecycle and state tracking" | Not a WARM term |
| Memory | Short-term (conversation) plus long-term (insights) | Long-term only; short-term is Sessions |

## C. Google Cloud Architecture Center, agentic AI pages

**What it is.** A set of Architecture Center pages: two "choose" guides (components; design patterns), two generic reference architectures (multi-agent; single-agent), two infrastructure reference architectures (multi-tenant; private networking), and ten use-case architectures. The pages use the product names current on 2026-11-11 ("Gemini Enterprise Agent Platform", "Agent Runtime", "Agent Registry", "Agent Gateway", "Agent Identity", "Memory Bank").

**Pages found and read.** All fetched on 2026-11-11 with curl and converted to text by a delegated reader, which extracted a verbatim inventory; this mapper assigned from that inventory and checked the definitions it relied on. The page list comes from the Architecture Center navigation ("Agentic AI" subsection) and the overview index, which agree (17 pages). URLs are `https://cloud.google.com/architecture/<slug>`; dates are each page's "Last reviewed".

| Code | Page (slug) | Last reviewed | Read |
|---|---|---|---|
| CMP | Choose your agentic AI architecture components (`choose-agentic-ai-architecture-components`) | 2026-11-05 | full |
| DP | Choose a design pattern for your agentic AI system (`choose-design-pattern-agentic-ai-system`) | 2026-05-28 | full |
| MA | Multi-agent AI system in Google Cloud (`multiagent-ai-system`) | 2026-10-09 | full |
| SA | Single-agent AI system using ADK and Cloud Run (`single-agent-ai-system-adk-cloud-run`) | 2026-10-20 | core sections full; repeated boilerplate skimmed |
| OV | Agentic AI architecture guides, overview (`agentic-ai-overview`) | 2025-11-05 | full (index only) |
| MTN | Multi-tenant agentic AI system (`multi-tenant-agentic-ai-system`) | 2026-10-16 | agent sections full; network alternatives skimmed |
| PN | Multi-agent private networking patterns (`multi-agent-private-networking-patterns`) | 2026-11-09 | **partly**: first ~230 of 1,247 lines; the rest (network configuration) searched by keyword only |
| SOC | Orchestrate security operations workflows (`agentic-ai-orchestrate-security-ops-workflows`) | 2026-04-08 | full except duplicate deployment tabs |
| IL | Administer interactive learning (`agentic-ai-interactive-learning`) | 2026-10-14 | full |
| DS | Automate data science workflows (`agentic-ai-data-science`) | 2026-10-14 | full |
| XA | Implement agentic analytics for distributed data (`agentic-ai-cross-cloud-analytics`) | 2026-10-16 | architecture and use cases full |
| CM | Classify multimodal data (`agentic-ai-classify-multimodal-data`) | 2026-10-14 | architecture and flow full |
| GM | Build a trusted agentic system with Google Maps Platform (`agentic-ai-system-with-grounding-using-maps`) | 2026-10-21 | full |
| ST | Bidirectional multimodal streaming (`agentic-ai-bidirectional-multimodal-streaming`) | 2026-10-14 | architecture and flows full |
| LH | Cross-cloud open data lakehouse (`agentic-ai-build-multicloud-open-data-lakehouse`) | 2026-10-14 | components only |
| GR | Multimodal GraphRAG resource orchestration (`agentic-ai-multimodal-graph-rag-resource-orchestration`) | 2026-10-13 | architecture, flows, design considerations |
| DSY | Orchestrate access to disparate enterprise systems (`agenticai-orchestrate-access-disparate-systems`) | 2026-10-27 | full |
| — | Well-Architected AI and ML perspective: operational excellence; security (`framework/perspectives/ai-ml/...`) | 2026-10-29 | **not read** (ML operations, not agent architecture); keyword lines only |
| — | Generative AI overview (`genai-overview`) | 2026-11-02 | **not read** (non-agentic index) |

No page failed to open. There is no Architecture Center page dedicated to an agent registry, an agent catalog, MCP or A2A (guessed URLs redirect; none in the navigation or index). Every use-case page (SOC to DSY) repeats a four-line security block (human oversight, Agent Identity, Agent Gateway, Agent Registry); it is inventoried once, from MA.

### C.1 Inventory and assignment

| ID | Item | Definition (verbatim, short) | Page | Assignment | Fit | Reason |
|---|---|---|---|---|---|---|
| C001 | Agent (definition) | "An agent is an application that achieves a goal by processing input, performing reasoning with available tools, and taking actions based on its decisions" | CMP | Agent concept | S | An application, not an identified actor filling roles; no role or lifetime. |
| C002 | Agent development framework | "The frameworks and libraries that you use to build and structure your agent's logic" | CMP | Guidance (builder tooling) | G | Build-time. |
| C003 | Frontend framework (prototyping, production) | "A collection of prebuilt components, libraries, and tools that you use to build the user interface" | CMP | Guidance (builder tooling for Channels) | G | Build-time. |
| C004 | AG-UI | "An open, event-based protocol that enables backend AI agents to interact with your frontend framework" | CMP | Channels | C | Agent-to-user surface protocol. |
| C005 | A2UI | "lets backend agents stream declarative, structured UI components to the client application" | CMP | Channels | C | Same. |
| C006 | Agent security and governance (component) | "The controls and policies that secure agent identities, ingress and egress traffic, tools, and model interactions" | CMP | Span: Identity + Policy (+ Secrets) | Sp | WARM's Governance group without Approvals. |
| C007 | Agent Gateway (ingress and egress) | "authenticate callers, enforce authorization policies, and inspect inbound prompts in real time"; egress "enforcing default-deny access policies" | CMP | Span: Policy + Identity (+ routing of agent and tool calls) | Sp | An enforcement point on every call, inbound and outbound. |
| C008 | Agent Identity (with auth manager) | "manage the identities of your agents"; "centrally control OAuth tokens and API keys instead of embedding credentials in agent code or prompts" | CMP | Span: Identity + Secrets | Sp | Two services; the auth manager is WARM's Secrets almost word for word. |
| C009 | Agent Registry | "a centralized inventory and catalog for your organization's AI agents, MCP servers, agent skills, and tools and helps ensure that only verified tools and subagents are used" | CMP | Registry | C | Agents, tools and skills, as WARM's Registry; enforcement is by the Gateway ("combine it with Agent Gateway"). |
| C010 | IAM access policies, IAP, Principal Access Boundary | "enforce fine-grained, least-privilege authorization across agents, tools, and resources" | CMP | Policy | C | Authorization rules. |
| C011 | Model Armor | "protection ... against prompt injection, sensitive data leaks, and harmful content" | CMP | Policy | S | Content inspection, not action authorization. |
| C012 | Agent tools | "functions or APIs that are available to the AI model and that the agent uses to enhance output and allow for task automation" | CMP | Tools | C | Same. |
| C013 | Built-in tools | "common task like completing a web search, running a calculation, or executing code" | CMP | Tools | C | Kind of tool. |
| C014 | MCP (tool use pattern) | "a standardized interface for agents to access and use the necessary tools, data, and other services" | CMP | Tools | C | Mediation protocol. |
| C015 | Custom function tools | "integrate with a specific internal or third-party API that doesn't have an MCP server" | CMP | Tools | C | Kind of tool. |
| C016 | MCP server options (Google-managed, third-party remote, self-hosted) | "remote MCP servers that are fully-managed by Google" | CMP | Guidance (Tools, Providers) | G | Hosting choice. |
| C017 | API management: catalog and discovery | "API hub exposes an MCP server so that agents and developers can discover registered tools, and it synchronizes MCP metadata with Agent Registry" | CMP | Registry | C | Tool catalog. |
| C018 | API management: runtime policy enforcement | "authentication, fine-grained authorization, token and rate limiting, semantic caching, and monitoring for API endpoints and MCP servers" | CMP | Span: Identity + Policy + Scheduling (rate limits) + Observability | Sp | A gateway bundle; "semantic caching" has no WARM place. |
| C019 | API management: prebuilt connectors | "Application Integration and Integration Connectors or MCP Toolbox for Databases" | CMP | Tools | C | Connectors. |
| C020 | Agent-as-a-tool | "exposes one agent as a callable function that another agent can invoke" | CMP | Guidance (Orchestration through Tools) | G | Delegation carried by the tool interface rather than by Messaging. |
| C021 | Tool bloat mitigations (limit complexity, granular toolsets, search tool, multi-agent delegation) | "Tool bloat occurs when you provide too many tool definitions in the system prompt" | CMP | Guidance (Harness, Registry) | G | Practice. |
| C022 | Agent Skills and Skill Registry | "an open standard format that enables progressive discovery of instructions, scripts, and other resources"; "discover and load governed enterprise skills from Skill Registry" | CMP | Registry | C | Skills as versioned definitions loaded when needed, as WARM v0.11. |
| C023 | Agent memory (component) | "The system that your agent uses to store and recall information" | CMP | Span: Sessions + Memory | Sp | Two WARM services. |
| C024 | Short-term memory | "enables an agent to maintain context within a single, ongoing conversation" | CMP | Sessions | S | Conversation only. |
| C025 | Session | "the conversational thread between a user and the agent, from the initial interaction to the end of the dialogue" | CMP, SA | Sessions | S | WARM's session is any stretch of work, not only a dialogue. |
| C026 | State | "the data that the agent uses and collects within a specific session" | CMP, SA | Sessions | C | Session state. |
| C027 | External state management | "build a stateless agent application and manage the session state in an external storage service" | CMP | Guidance (Sessions) | G | Practice. |
| C028 | Long-term memory | "a persistent knowledge base that exists across all conversations for individual users" | CMP | Memory | C | Retained across sessions; scoped per user. |
| C029 | Agent design patterns (component) | "Common architectural approaches for structuring your agentic application" | CMP | Guidance | G | Google lists design patterns as a component of the architecture. |
| C030 | Graph-based workflows | "predictable execution paths with explicit state transitions, conditional routing, parallel branches, and human-in-the-loop checkpoints" | CMP | Span: Orchestration + Approvals | Sp | Fixed-step coordination with holds. |
| C031 | Dynamic workflows | "automatically checkpoint node executions so that workflows are durable and resumable" | CMP | Tasks | C | Durable execution. |
| C032 | Collaborative workflows | "Coordinate multiple specialized agents that delegate tasks and share context" | CMP | Orchestration | C | Coordination. |
| C033 | A2A | "enables AI agents to communicate and collaborate across different platforms and frameworks" | CMP, MA | Messaging | C | Delivery between agents. |
| C034 | Agent runtime (component) | "The compute environment where your agent's application logic runs"; "runs your application code, the business logic, and orchestration" | CMP | Span: Harness + Infrastructure | Sp | Compute plus loop. |
| C035 | Agent Runtime (managed product as runtime) | "an opinionated, managed runtime that includes integrations for memory, evaluation, identity, governance, and observability" | CMP | Span: Harness + Sessions + Memory + Evaluation + Identity + Observability | Sp | A harness-product bundle. |
| C036 | Container runtimes (Cloud Run, GKE) | "Cloud Run instances are stateless"; "GKE pods are ephemeral" | CMP | Infrastructure | C | Where it runs. |
| C037 | Code execution sandbox | "Gemini Enterprise Agent Platform Code Execution"; "GKE Sandbox" | CMP | Environments | C | Isolated place to act. |
| C038 | AI models | "The core reasoning engine that powers your agent's decision-making capabilities" | CMP | Providers layer | S | The model itself; the call goes through Models. |
| C039 | Model routing | "dynamically select the most appropriate model for each task based on the task's complexity, cost, or latency requirements" | CMP | Models | C | "choose the model for each task". |
| C040 | Thinking level and thought summaries | (model configuration options) | CMP | Models | S | Per-call configuration. |
| C041 | Model runtime | "The infrastructure that hosts and serves your AI model" | CMP | Infrastructure | C | Self-hosted model on infrastructure. |
| C042 | Context engineering | "isolating context for a specific agent, persisting information across multiple steps, or compressing large amounts of data" | DP | Harness | S | Defined as a process; its run-time part is the Harness. |
| C043 | Agent design pattern (definition) | "a distinct framework for organizing a system's components, integrating the model, and orchestrating a single agent or multiple agents" | DP | Guidance | G | Design-time. |
| C044 | Single-agent system | "uses an AI model, a defined set of tools, and a comprehensive system prompt to autonomously handle a user request" | DP | Guidance | G | Pattern. |
| C045 | Multi-agent system | "decompose a large objective into smaller sub-tasks and assign each sub-task to a dedicated agent with a specific skill" | DP | Guidance (Orchestration) | G | Pattern. |
| C046 | Sequential pattern | "executes a series of specialized agents in a predefined, linear order ... without having to consult an AI model for the orchestration" | DP | Guidance (Orchestration of fixed steps) | G | Pattern. |
| C047 | Parallel pattern | "multiple specialized subagents perform a task or sub-tasks independently at the same time" | DP | Guidance (Orchestration) | G | Pattern. |
| C048 | Loop pattern | "repeatedly executes a sequence of specialized subagents until a specific termination condition is met" | DP | Guidance (Orchestration) | G | Pattern. |
| C049 | Review and critique | "Critic can approve the content, reject it, or return it to the generator with feedback" | DP | Guidance (Evaluation by an agent) | G | Pattern. |
| C050 | Iterative refinement | "progressively improve an output over multiple cycles" | DP | Guidance (Evaluation, Sessions) | G | Pattern. |
| C051 | Coordinator pattern | "uses a central agent, the coordinator, to direct a workflow ... its use of an AI model to orchestrate and dynamically route tasks" | DP | Guidance (Orchestration) | G | Pattern. |
| C052 | Hierarchical task decomposition | "organizes agents into a multi-level hierarchy ... A top-level parent, or root, agent" | DP | Guidance (Orchestration) | G | Pattern. |
| C053 | Swarm pattern | "uses a dispatcher agent to route a user request to a collaborative group of specialized agents ... lacks a central supervisor" | DP | Guidance (Messaging) | G | Pattern. |
| C054 | ReAct pattern | "the agent operates in an iterative loop of thought, action, and observation" | DP | **Misfit** (out of scope) | M | Single-agent reasoning. |
| C055 | Human-in-the-loop pattern | "At a predefined checkpoint, the agent pauses its execution and calls an external system to wait for a person to review its work ... approve a decision, correct an error, or provide necessary input" | DP | Approvals | C | Hold until a person decides; Google adds "correct" and "provide input", which go beyond authorize. |
| C056 | Custom logic pattern | "implement specific orchestration logic that uses code" | DP | Guidance | G | Pattern. |
| C057 | Workflow agents (sequential, parallel, loop) | "a sequential workflow agent that operates on predefined logic without having to consult an AI model" | DP | Orchestration | S | Google calls a deterministic coordinator an "agent". |
| C058 | Coordinator and root agent roles | "the coordinator analyzes and decomposes a user's request into sub-tasks, and then it dispatches each sub-task" | DP, MA | Span: agent (coordinating role) + Orchestration | Sp | The agent does the decomposition and the coordination. |
| C059 | Subagent and worker agent | "Lowest level: a worker agent" | DP | Agent concept (task agent) | S | Lifetime not stated. |
| C060 | Dispatcher agent | "route a user request to a collaborative group of specialized agents"; "The dispatcher agent doesn't orchestrate" | DP, ST | **Misfit** | M | Intake routing (as A124, B199); Google explicitly separates it from orchestration. |
| C061 | Critic and quality evaluator agents | "reviews the output of the task-B subagent" | DP, MA | Evaluation (provided by an agent) | S | Evaluation in an agent role. |
| C062 | Pattern groupings and selection process | "Workflows that are deterministic ... require dynamic orchestration ... involve iteration ... have special requirements" | DP | Guidance | G | Selection method. |
| C063 | Multi-agent AI system (definition) | "segmenting them into discrete tasks that multiple specialized AI agents collaboratively execute" | MA | Guidance | G | Definition of a pattern. |
| C064 | Frontend | "Users interact with the multi-agent system through a frontend, such as a chat interface" | MA, SA | Channels | C | Surface for people. |
| C065 | Agents (coordinator plus subagents over A2A) | "A coordinator agent controls the agentic AI system ... invokes an appropriate subagent" | MA | Span: agent + Orchestration + Messaging | Sp | Component bundles three WARM parts. |
| C066 | AI model and model runtimes | "the agents ... use an AI model on Gemini Enterprise Agent Platform. ... Cloud Run and GKE as alternative runtimes" | MA | Span: Models + Infrastructure + Providers | Sp | Model, hosting and vendor. |
| C067 | MCP clients, servers, and tools | "For each agent-tool pair, an MCP client sends requests to an MCP server through which the agent accesses a tool" | MA, SA | Tools | C | Mediation. |
| C068 | Prompt enhancer and response generator subagents | "refine the prompt"; "generates a response, performs validation and grounding checks" | MA | Agent concept (roles) | S | Roles by processing step. |
| C069 | Use case: financial advisor (data retriever, financial analyzer, stock recommender, trade executor agents) | "Provide personalized stock trading recommendations and execute trades" | MA | Domains layer (an area of work implemented as agent roles) | S | An area of work defined only by its agents; no charter. |
| C070 | Use case: research assistant (planner, researcher, evaluator, report composer agents) | "The researcher agent repeats these tasks until the evaluator agent approves the research" | MA | Domains layer | S | As C069; the evaluator agent carries the acceptance criteria. |
| C071 | Use case: supply chain optimizer (warehouse manager, shipment tracker, supplier communicator agents) | "communicates with external suppliers on behalf of the other agents in the system" | MA | Domains layer | S | As C069; one agent holds the outward-communication responsibility for the others, as WARM's Communications domain does. |
| C072 | Agent design: business goal and per-agent task | "Clearly define the business goal of the agentic AI system and the task that each agent performs" | MA | Span: domain parts goals + roles | Sp | Goal per system, task per agent. |
| C073 | Human oversight (monitor, override, pause, approve or reject) | "let human supervisors monitor, override, and pause agents ... approve or reject the outputs" | MA | Span: Approvals + Observability + (pause: no WARM part) | Sp | "pause agents" is the run-time suspension of A93. |
| C074 | Workload-bound agent identity | "Provide each agent a workload-bound, SPIFFE-based identity by using Agent Identity" | MA | Identity | C | Same. |
| C075 | Per-agent least-privilege permissions | "Grant each agent only the permissions that it needs to perform its tasks and to communicate with tools and with other agents" | MA | Policy | C | Rules on actions. |
| C076 | Credential manager | "centrally control OAuth tokens and API keys instead of having to embed credentials within agent code or prompts" | MA | Secrets | C | WARM: "without placing it in an agent's context". |
| C077 | Ingress and egress traffic governance | "Route agent traffic through Agent Gateway to enforce runtime security policies at both the ingress and egress boundaries" | MA | Policy | C | Enforcement point (WARM Governance point 1). |
| C078 | Registered-target verification | "Verify that target agents and tools are registered in Agent Registry"; "agents only connect to inventoried, administrator-approved MCP endpoints" | MA | Span: Registry + Policy | Sp | Registration becomes a condition of permission. |
| C079 | Agent Card (A2A) | "Each agent advertises the authentication requirements in its Agent Card" | MA, ST | Span: Registry + Identity | Sp | Self-description plus auth needs. |
| C080 | Model use policy | "organization policies to limit the type and versions of AI models that can be used" | MA | Policy | S | A rule on Models. |
| C081 | Data loss prevention | "Cloud Data Loss Prevention API" for prompts, responses, logs | MA | Policy | C | Rule on data. |
| C082 | Continuous evaluation | "Regularly perform a qualitative evaluation of the output of the agents and the trajectory or steps taken" | MA, SA | Evaluation | C | Same. |
| C083 | Shared tool store (MCP Toolbox) | "a centralized location to store and update database tools. You can share the tools across agents and update the tools without redeploying agents" | MA, SA | Span: Tools + Registry + Releases | Sp | Tool definitions released apart from agents. |
| C084 | Tracing | "visibility into every action that an agent takes, including its reasoning process, tool selection, and execution paths" | MA | Observability | C | Evidence. |
| C085 | Prompt optimizer | "To rapidly improve and optimize prompt performance at scale" | MA | Improvement | C | Proposes changed prompts from evidence. |
| C086 | Simulate failures before production | "validate it by simulating a production environment" | MA | Evaluation | S | Pre-release test. |
| C087 | No-match handling | "Implement logic to handle no-match situations, such as when a prompt is off-topic" | MA | Guidance | G | Intake design advice. |
| C088 | Single agent (component) | "receives user requests, interprets user intent, selects the appropriate tools, and then it synthesizes information" | SA | Agent concept | S | Defined by its loop. |
| C089 | Observability (component) | "monitored by using Google Cloud Observability for logging, monitoring, and tracing" | SA | Observability | C | Same. |
| C090 | Decouple state from runtime (recover from outages) | "decouple state from runtime ... use an external datastore" | SA | Span: Sessions + Reliability | Sp | Recovery through externalized state. |
| C091 | Routing hub | "the central ingress point for the architecture" (load balancer, Cloud Armor, Model Armor, IAP) | MTN | Span: Channels + Policy + Identity | Sp | Ingress bundle. |
| C092 | Frontend portal (tenant router) | "acts as a routing engine to route requests to the appropriate isolated tenant project"; "Uses a dynamically maintained registry to identify the correct target tenant" | MTN | **Misfit** | M | Intake routing to a business unit by the user's identity; nearest WARM part is the Directory, which is consulted by agents and keyed on responsibilities. |
| C093 | Central governance and security hub | "centralized Identity and Access Management (IAM), logging, monitoring, and security for the entire platform" | MTN | Span: Identity + Policy + Observability | Sp | Governance plus Observability, shared by all tenants. |
| C094 | Tenant project per business unit | "a dedicated Google Cloud project for each business unit. Individual tenant projects are isolated environments" | MTN | Span: Domains layer (business unit) + Infrastructure (isolation) + Policy | Sp | The nearest thing to a WARM domain in any source: one business unit, its own agent, tools, rules and data. Bound to an isolation boundary, which WARM does not require. |
| C095 | Principal Access Boundary per business unit | "hard isolation between different business units" | MTN | Policy | C | Rule. |
| C096 | Business-unit agent runtime | "hosts the specific business unit agent and executes custom orchestration code" | MTN | Span: Harness + Infrastructure | Sp | Runtime per tenant. |
| C097 | Local (tenant-specific) MCP server | "provides agents access to datastores and tools that are specific to that business unit" | MTN | Domain part: domain tools | C | Connections this area of work needs. |
| C098 | Shared (global) MCP server | "provide access to tools and systems that are common across multiple tenants" (e.g. "expense reporting tools, human resources (HR) systems") | MTN | Tools | C | Platform tool access shared by all domains; matches WARM's platform/domain split for tools. |
| C099 | Tenant datastore | "stores specific business unit data ... only the tenant agents can access this data" | MTN | Domain part: domain knowledge | C | Knowledge of one area of work. |
| C100 | Per-business-unit cost attribution | "attribute costs to individual business units, use labels and Cloud Billing export data" | MTN | Observability | S | Cost attribution (WARM's Cost concern). |
| C101 | Tenant-level rate limiting | "Enforce quotas in the frontend portal for each tenant" | MTN | Scheduling | S | Limits on what runs, per tenant. |
| C102 | Persona-based access | "custom IAM roles to help ensure that a developer who builds an agent in one tenant can't access data in another tenant" | MTN | Policy | C | Rule on people. |
| C103 | Tenant onboarding with IaC | "establish a consistent baseline when you onboard new tenants" | MTN | Releases | S | Provisioning a domain's environment. |
| C104 | Hub-and-spoke network | "a central environment ... connects to multiple isolated environments" | MTN | Infrastructure | C | Network. |
| C105 | Root agent (custom agent) | "acts as a top-level workflow orchestrator ... The core of the AI system workflow and business logic resides in the root agent and in specialized subagents" | PN | Span: agent + Orchestration | Sp | Orchestration and business logic in one agent. |
| C106 | Gemini Enterprise app | "The frontend for users to access an in-app chat interface" | PN | Channels | C | Surface. |
| C107 | Subagents (triggered by root agent, A2A) | "Specialized agents that are triggered by the root agent workflow" | PN | Agent concept (task agent) | S | Lifetime not stated. |
| C108 | Tools (external to agents) | "Tools are external to agents, and agents connect and interact with tools by using the MCP specification" | PN | Tools | C | Mediation. |
| C109 | Agent discovery service (name to endpoint) | "When you register an agent, Gemini Enterprise maps the name of the agent to a specific target"; "the app looks up the agent in the registry to find the associated endpoint" | PN | Span: Registry + Directory (how to reach) | Sp | Reach information without responsibility. |
| C110 | Shared VPC personas | "a clear boundary between network and security administrator personas and AI app developer personas" | PN | Span: Infrastructure + People | Sp | Who controls what infrastructure. |
| C111 | Default-deny egress | "prevents AI agents from making any network connections that aren't explicitly authorized" | PN | Policy | C | Rule. |
| C112 | SOC manager (root, coordinator) | "dynamically directs subtasks to specialized subagents"; "evaluates the findings against the AI runbook requirements" | SOC | Span: agent + Orchestration + Evaluation | Sp | Coordinator that also judges. |
| C113 | SOC personas (Tier 1 analyst, CTI researcher, custom personas) | "you can deploy other SOC personas or create your own custom personas" | SOC | Domain part: roles | C | Roles of the security-operations area of work, filled by agents. |
| C114 | RAG knowledge database (incident response plans, AI runbooks as Agent Skills) | "AI runbooks are prescriptive workflows in the form of Agent Skills" | SOC | Span: Retrieval + Registry (skills) + domain workflow | Sp | Skills fetched by RAG. |
| C115 | Artifact service | "A managed service that stores investigation reports and evidence in Cloud Storage" | SOC | Artifacts | C | Work products stored. |
| C116 | Memory Bank (as memory component) | "lets agents maintain context about environmental and threat context across sessions"; "generates, refines, manages, and retrieves long-term memories" | SOC, IL | Memory | C | Same. |
| C117 | Sessions service | "A persistent storage service that saves and retrieves the history of interactions between a user and agents" | IL | Sessions | C | Same. |
| C118 | Third-party MCP servers | "A connector that third-party vendors manage" | SOC | Span: Tools + Providers | Sp | Supplied and operated outside. |
| C119 | Runbook evaluation criteria | "If the findings don't meet the evaluation criteria, the SOC manager repeats its analysis" | SOC | Domain part: acceptance criteria | C | Criteria supplied by the domain's runbooks. |
| C120 | Prompt caching | "cache static agent content, such as system instructions, personas, runbooks, and tool schema" | SOC | **Misfit** | M | Caching (as A109). |
| C121 | Per-role model selection | "Select different models in your agentic system based on the different agent roles and task requirements" | SOC | Models | C | Model choice per task. |
| C122 | Human-in-the-loop approval (capability) | "Implement human-in-the-loop approval." | SOC | Approvals | C | Same. |
| C123 | Agent scoping | "scope each agent's runbooks and system instructions" | SOC | Guidance | G | Practice. |
| C124 | Specialized agents by data source (analytics, AlloyDB, BigQuery, BigQuery ML agents) | "A specialized agent for interacting with data in BigQuery" | DS | Guidance (agent per system) | G | Agents split by tool, not by area of work. |
| C125 | Data Agent Kit | "lets agents access trusted data in Google Cloud by loading appropriate skills and connecting to remote MCP servers" | XA | Span: Registry (skills) + Tools | Sp | Skill pack plus tools. |
| C126 | External coding agents as clients (CLI agents) | "A CLI agent like Antigravity CLI, Claude Code, or Codex" | XA | Providers | S | Third-party agents calling the system's tools. |
| C127 | Knowledge Catalog (data catalog, context graph) | "extracts semantic metadata, and builds a context graph" | XA | Retrieval | S | Index over data; not an agent catalog. |
| C128 | Shared session state for subagents | "save resource paths in a shared session state. All of the subagents can access the shared session state" | CM | Sessions | C | Shared state of one stretch of work. |
| C129 | Observability pipeline and event viewer | "Agent events are logged in Cloud Logging and they're published to a Firestore database ... view the agents' thought flow and actions" | GM | Observability | C | Evidence. |
| C130 | Domain agents for trip planning (travel, CRM, schedule, logistics agents) | "A Schedule agent schedules meetings in the traveler's calendar" | GM | Agent concept (roles) | S | Roles by function; "schedule agent" is domain work, not WARM Scheduling. |
| C131 | Background streaming tool (continuous monitor) | "a streaming tool that runs in a continuous background loop to detect hazards" | ST | Span: Scheduling (continuous trigger) + Tools | Sp | A watcher that starts work. |
| C132 | Authenticated extended agent cards with OIDC | "Attach OpenID Connect (OIDC) identity tokens to requests" | ST | Identity | C | Who is calling. |
| C133 | BigQuery data agent (governed query agent) | "The agent enforces security and governance guardrails on the queries" | LH | Span: agent + Policy | Sp | An agent enforcing policy. |
| C134 | Secret Manager | "securely stores the Databricks service principal credentials" | LH | Secrets | C | Same. |
| C135 | Session versus Memory Bank rule | "Use session state for immediate conversation history and use Memory Bank for distilled facts across sessions. Inject memory context at the start of a session" | GR | Guidance (Sessions, Memory, Harness) | G | States WARM's cut. |
| C136 | User control over memories | "Let users clear or update stale memories if their preferences or roles change over time" | GR | **Misfit** | M | Subject control (as A66). |
| C137 | Search strategy selection (keyword, semantic, hybrid) | root agent chooses "keyword / semantic RAG / hybrid" | GR | Retrieval | C | Fetch method. |
| C138 | Interaction channels: custom frontend with HITL; Gemini Enterprise chat invoking the agent as a tool | "communicates with the agent over a secure REST API and supports human-in-the-loop processes" | DSY | Channels | C | Surfaces for people and applications. |
| C139 | Interaction channel: business events on Pub/Sub | "An external application that initiates system-to-system automation workflows by publishing business events to a Pub/Sub topic" | DSY | Span: Channels + Scheduling (event trigger) | Sp | An application starting work by event. |
| C140 | MCP servers as anti-corruption layer | "The MCP servers form an anti-corruption layer that isolates the agent from the backend systems" | DSY | Tools | C | Mediation (a DDD term applied to tools). |
| C141 | Backend systems layer | (layer name: "Backend systems") | DSY | Providers | S | Systems of record outside the platform. |
| C142 | Deployment automation across environments | "repeatable, auditable deployments across development, staging, and production" | DSY | Releases | C | Release with environments. |
| C143 | Governance templates (App Design Center) | "define templates that incorporate governance rules and best practices" | DSY | Span: Registry (templates) + Policy | Sp | Templates carrying rules. |
| C144 | Cross-cloud analytics layers (user and agentic actions; analytics workflows; trusted data stores) | (layer names) | XA | Guidance | G | Use-case layering. |


### C.2 Counts

| Inventory items | Clean | Strained | Spans | Guidance | Misfits |
|---|---|---|---|---|---|
| 144 | 56 | 25 | 32 | 26 | 5 |

The misfits are C054 (ReAct, out of scope), C060 (dispatcher agent), C092 (tenant-routing frontend portal), C120 (prompt caching) and C136 (user control over memories).

### C.3 Reverse direction: WARM against Google

Searched (delegated reader, `grep -i` over the 17 page bodies, then read in context): registry, catalog, discover, register, owner, ownership, accountab, approv, schedule, scheduler, cron, trigger, event, Pub/Sub, artifact, version, session, state, persist, ephemeral, long-running, lifecycle, evaluat, deploy, identity, secret, credential, policy, audit, observab, persona, role, business unit, tenant, domain. The instrument returned positives for most terms.

| WARM part | Google has it | Where |
|---|---|---|
| Harness | Partly | Agent runtime "runs your application code, the business logic, and orchestration" (C034); context engineering (C042). The loop is in the framework (ADK), not a named runtime responsibility. |
| Sessions | Fully | Session, state, Sessions service (C025, C026, C117, C128). |
| Tasks | Partly | Dynamic workflows "durable and resumable" (C031). No task-tracking component. |
| Environments | Fully | Code execution sandbox, GKE Sandbox (C037). |
| Scheduling | Partly | Only an event channel on Pub/Sub (C139), a background monitoring tool (C131), tenant quotas (C101) and "Cloud Scheduler and Pub/Sub" as allowed ingress sources (PN). No agent scheduler. |
| Memory | Fully | Long-term memory, Memory Bank (C028, C116). |
| Retrieval | Fully | RAG knowledge database, search strategies (C114, C137). |
| Artifacts | Partly | "Artifact service" in one use case (C115). Not in the components page. |
| Models | Fully | Model routing, per-role model selection, model use policy (C039, C121, C080). |
| Tools | Fully | Agent tools, MCP, API management, shared and tenant MCP servers (C012-C019, C097, C098). |
| Registry | Fully | Agent Registry of "AI agents, MCP servers, agent skills, and tools" (C009); Skill Registry (C022); API hub (C017). The closest match to WARM's Registry in any of the three sources. |
| Directory | Partly | Discovery service maps agent name to endpoint (C109); tenant router maps a user's business unit to a tenant (C092). Neither records accountability for a responsibility. |
| Messaging | Fully | A2A (C033). |
| Orchestration | Fully | Coordinator, workflow agents, collaborative workflows (C032, C057, C058). |
| Channels | Fully | Frontend, AG-UI, A2UI, interaction channels including application events (C004, C005, C064, C138, C139). |
| Identity | Fully | Agent Identity, SPIFFE identity, OIDC on agent cards (C008, C074, C132). |
| Secrets | Fully | Auth manager, Secret Manager (C076, C134). |
| Policy | Fully | IAM, PAB, Agent Gateway, default-deny (C007, C010, C077, C111). |
| Approvals | Fully | Human-in-the-loop pattern and capability (C055, C122); graph workflow checkpoints (C030). No approver role or queue is specified (delegated reader's note). |
| Observability | Fully | Tracing, observability pipeline (C084, C089, C129). |
| Evaluation | Fully | Continuous evaluation, critic and evaluator agents (C082, C061). |
| Improvement | Partly | Prompt optimizer (C085); "iterative development process that includes continuous monitoring" (GM). |
| Releases | Partly | Deployment automation across environments (C142), tool updates "without redeploying agents" (C083), tenant onboarding (C103). Agent versioning is not defined on any page; model versions appear only in organization policy (C080). |
| Reliability | Partly | Decouple state from runtime (C090); fault tolerance, simulate failures (MA). |
| People layer | Partly | Personas (C110), human supervisors (C073), teams per business unit (MTN). |
| Domains layer | Partly | Business units with their own tenant, agent, tools, rules and data (C094, C097, C099); use cases as areas of work (C069-C071). |
| Platform layer | Partly | "Gemini Enterprise Agent Platform ... build, scale, govern, and optimize" (MA); the central governance hub shared by tenants (C093). |
| Infrastructure layer | Fully | Runtimes, model runtime, networks (C036, C041, C104). |
| Providers layer | Partly | AI models (C038), third-party MCP servers (C118), backend systems (C141). |
| Goals | Partly | "Clearly define the business goal of the agentic AI system" (C072). |
| Roles | Partly | SOC personas (C113); "Establish strong governance with clear roles for each agent" (GM). |
| Workflow | Partly | AI runbooks as "prescriptive workflows" (C114); patterns. |
| Domain knowledge | Fully | Tenant datastore (C099); division-specific retrieval (MTN). |
| Domain tools | Fully | Tenant-specific MCP servers (C097). |
| Domain rules | Partly | Business units "follow specific operational rules" (MTN); runbooks. |
| Acceptance criteria | Partly | Runbook evaluation criteria (C119); evaluator approves research (C070). |
| Directory (as a whole) | Absent | No page records which area of work is accountable for a responsibility. |

### C.4 Findings

**(a) Misfits and spans**

| Item | Kind | What it suggests |
|---|---|---|
| C060 Dispatcher agent; C092 tenant-routing frontend portal | Misfit | Intake routing again, now in two forms: by intent (dispatcher) and by the requester's business unit (portal with "a dynamically maintained registry"). Google states the dispatcher "doesn't orchestrate", which separates routing from Orchestration explicitly. With A124 and B199, all three vendors have it. Strong evidence for a WARM responsibility: deciding which agent or domain receives an inbound request. |
| C136 User control over memories | Misfit | Subject control (with A66). Two sources. |
| C120 Prompt caching (and "semantic caching" inside C018) | Misfit | Caching (with A109). Three mentions across two sources; still an implementation optimization. |
| C054 ReAct | Misfit, out of scope | Nothing. |
| C073 Human oversight including "pause agents" | Span | Run-time suspension of an agent appears again (A93, B063). |
| C094 Tenant project per business unit | Span | A business unit with its own agent, tools, rules and data is close to a WARM domain, joined to an isolation boundary. Evidence for WARM's Domains layer, and evidence that practitioners implement a domain as a tenant. |
| C097/C098 Local versus shared MCP servers | Clean pair | Google draws WARM's line between domain tools and platform Tools: "specific to that business unit" versus "common across multiple tenants". |
| C114 Runbooks as Agent Skills in a RAG database | Span | Skills held in a retrieval store, not in a registry. Partly contradicts WARM v0.11 (Registry holds skills); C022 on the components page agrees with WARM (Skill Registry). Google holds both. |
| C078 Registered-target verification | Span | Registration is a precondition of permission: agents "only connect to inventoried, administrator-approved MCP endpoints". |
| C035 Agent Runtime product | Span | Harness-product bundle, as WARM predicts. |

**(b) Relations Google states that WARM does not, or that contradict WARM**

1. *Registry membership gates connection.* "When you register MCP servers and A2A agents in Agent Registry and combine it with Agent Gateway, you restrict agents to discovering and connecting only to approved endpoints instead of unmanaged or public URLs" (CMP). WARM says finding a destination grants nothing; Google uses the registry as the allow-list that Policy enforces. Compatible with WARM's separation (Policy enforces, Registry lists) but WARM does not state the relation "Policy may require registration".
2. *Dispatcher is not an orchestrator.* "The dispatcher agent doesn't orchestrate the agentic workflow, unlike the coordinator pattern. Instead, the dispatcher agent facilitates communication between the swarm subagents and the user" (DP). Separates routing from Orchestration, which WARM does not do.
3. *Delegation through tools.* "An agent-as-a-tool function exposes one agent as a callable function that another agent can invoke" (CMP); the data-science architecture invokes all specialized agents this way (DS). WARM routes handoffs through Orchestration and Messaging; Google also routes them through Tools. WARM should say that a handoff carried by a tool call is still an assignment that Orchestration tracks, or admit Tools as a carrier.
4. *Tools can change without releasing agents.* "update the tools without redeploying agents" (MA). Supports WARM's separate versioning of tools in the Registry and Releases.
5. *Sessions versus memory.* "Use session state for immediate conversation history and use Memory Bank for distilled facts across sessions" (GR). Matches WARM.
6. *Anti-corruption layer.* "The MCP servers form an anti-corruption layer that isolates the agent from the backend systems" (DSY). A Domain-Driven Design relation between Tools and outside systems that WARM does not state; consistent with WARM's Tools.
7. *Workflow agents that are not AI agents.* "a sequential workflow agent that operates on predefined logic without having to consult an AI model" (DP). WARM says Orchestration coordinates "agents, people and fixed steps" and that a platform service may be implemented by fixed code; Google calls that code an agent. Term difference, not a relation difference.

**(c) Domains, ownership, registries, persistence**

- *Business domains.* The multi-tenant architecture frames the problem in WARM's terms: "different business units require specialized AI agents that access unique tools, follow specific operational rules, and process sensitive data" (MTN). Its example: "to support an electronics division and a home goods division, you deploy an electronics agent and a home goods agent as two separate agents in separate tenant projects" and "the agent only retrieves context from its division-specific datastore. This targeted retrieval helps improve accuracy and helps prevent the agent from confusing the policies of different business units" (MTN). This is the closest any source comes to WARM's Step 4: a business unit has tools, rules, knowledge and an agent. It differs from WARM in three ways: one agent per business unit; isolation is the motive, not accountability; and the unit is an organizational division, not a responsibility at the hand-off grain. Elsewhere, "Each subagent is specialized in a particular domain" (CM) uses domain for a data modality (image, video, structured data).
- *Ownership and accountability.* No page defines an owner of an agent, tool or domain (delegated reader: owner, ownership, accountab, steward had no hits in agent context). Nearest: "Individual developer and operations teams manage tenant projects independently. This isolation provides autonomy for each business unit" versus "A centralized operations team manages the implementation" of shared MCP servers (MTN); personas that separate network administrators from AI app developers (PN); "You are responsible for properly configuring your services" (customer versus Google, MA).
- *Registries and their entries.* Agent Registry lists "AI agents, MCP servers, agent skills, and tools" (CMP); no entry schema is given. The discovery service maps "the name of the agent to a specific target, either the Agent Runtime resource URI or the A2A agent URL" (PN). The A2A Agent Card advertises "the authentication requirements" (MA). The tenant router's registry maps a user to a tenant (MTN). Entries are agents, tools and skills, plus reach information. No entry carries a responsibility or an accountable domain.
- *Long-lived versus per-task.* Not distinguished (delegated reader). Runtimes are stateless ("Cloud Run instances are stateless"; "GKE pods are ephemeral"), and persistence is in Sessions and Memory Bank. Subagents are "triggered by the root agent workflow" (PN) with no stated lifetime. WARM's persistent agent (identity, memory and channel across tasks) has no counterpart; continuity is per user, not per agent: long-term memory "exists across all conversations for individual users" (CMP).

**(d) Same word, different meaning**

| Term | Google | WARM |
|---|---|---|
| Agent | "an application"; also deterministic "workflow agents" with no model | An identified actor filling roles |
| Skill | Agent Skills: "progressive discovery of instructions, scripts, and other resources" (matches WARM); but "assign each sub-task to a dedicated agent with a specific skill" (an ability) | A packaged set of instructions |
| Session | "the conversational thread between a user and the agent" | Any stretch of an agent's work |
| Domain | A business unit (MTN), a data modality (CM) | An area of work with a charter |
| Registry | Agent Registry (agents, tools, skills); "registry" mapping users to tenants (MTN); discovery-service registry mapping names to endpoints (PN) | Versioned definitions of agents, tools and skills |
| Schedule agent | A domain agent that books meetings (GM) | Scheduling is a platform service |
| Catalog | Knowledge Catalog, a data catalog (XA) | Industry term for Registry |
| Artifact | Artifact service for reports and evidence (matches WARM); Artifact Registry/Analysis for container images | Work products |

## Across the three sources

### Misfits that recur

| Responsibility | Microsoft | AWS | Google |
|---|---|---|---|
| Routing an inbound request to an agent or a domain, by intent or by requester | A124 Classifier; A143 semantic router pattern | B199 routing workflow, classifier or router agent | C060 dispatcher agent; C092 tenant-routing portal |
| Suspending an agent or a class of agents at run time | A93 "pause/disable an agent class" | B063 "circuit breakers for abnormal behavior patterns"; B106 "restrict agent actions" | C073 "monitor, override, and pause agents" |
| A data subject's control over what is remembered | A66 | — | C136 |
| Caching | A109 semantic cache | — | C120 prompt caching; "semantic caching" in C018 |
| Tenancy | (memory scope by "tenant", MAP) | B104, and a whole guide | C092, C094 (tenant = business unit) |
| Model training and model catalog | (model oversight, GOV) | B007, B116, B147 | C080 (model version policy) |
| Metering and monetization | — | B117 | C100 (cost per business unit, as Observability) |

### Spans that recur

| Pattern | Evidence | Reading |
|---|---|---|
| Registry as a governance record | A11, A26, A118, A132; B006, B054; C078, C109 | Practitioners keep one record per asset with definition, reach, owner, permissions, approval status and metrics. WARM splits it across six services. |
| Gateways bundle mediation, discovery, policy and audit | A86, A135; B069, B071, B076, B078; C007, C018 | Predicted by WARM's statement that Governance covers an action only at an enforcement point. |
| One coordinating agent that also does the work | A07, A123, A126; B157; C058, C065, C105, C112 | WARM's Orchestration-versus-agent split is never drawn by the sources; a mapping must record the bundle. |
| Memory products holding sessions and memory | A41, A71; B051, B058, B152; C023 | WARM's cut by what is kept still applies; the sources name it the same way ("short-term" versus "long-term"). |
| Domain parts written for one agent | B088, B118; A08, A127; C072 | WARM's seven parts are recognizable in the sources, attached to agents. |
| Platform services provided by agents | B092 arbiter, B110 reflective agents; C061 critic agents; C133 governed query agent | Supports WARM's provisional statement on platform roles held by agents. |

## What WARM might change

Each candidate states the evidence, the sources that support it, and a confidence. Confidence is about whether the evidence shows a real gap or error in WARM, not about the proposed wording.

| # | Candidate change | Evidence | Sources | Confidence |
|---|---|---|---|---|
| 1 | **Name intake routing as a responsibility.** Deciding which agent or domain receives an inbound request (by intent, by requester, or by explicit mention) before any agent runs. Placement options: a sub-responsibility of Orchestration ("coordinate assignments, including the first one"), or a resolution function of the Directory (answer "who handles this request?"), or Channels routes as well as carries. Google says its dispatcher "doesn't orchestrate", which argues against folding it into Orchestration without saying so. | A124, A143; B199; C060, C092; also PN: "when the assistant decides to delegate, the app looks up the agent in the registry" | Microsoft, AWS, Google | High that the gap is real; medium on placement |
| 2 | **Add an owner to Registry entries**, distinct from Directory accountability: the person or team who answers for a definition of an agent, tool or skill and approves access to it and changes to it. WARM has accountable domains for responsibilities; the sources have owners of assets. Both relations exist. | "Metadata on ownership" and "authorization delegation to the tool or agent owners" (B054); `owners` in agent metadata (A26); "which team in the organization owns the agents" (BEH); "product owners" in the model catalog (B007). Google has no owner concept. | Microsoft, AWS | Medium |
| 3 | **State that registration is a gate.** Two relations: Policy may require a target to be registered before an agent may call it; and admission to the Registry is a release, which Evaluation and Approvals can gate. This does not change "finding a destination grants nothing"; it adds that not being registered can deny. | A27, A83, PAT#2 (evaluation before registration; "Only approved capabilities can be executed"); B008, B054 ("Approval status"); C078 ("agents only connect to inventoried, administrator-approved MCP endpoints") | Microsoft, AWS, Google | High |
| 4 | **Place run-time suspension of an agent.** Pausing, disabling or quarantining an agent or a class of agents without affecting the rest. Candidate home: Policy (a rule that denies every action of an actor, applied at every enforcement point), with Reliability for the restart. Also states what WARM's unresolved rule on platform-role agents needs: a way to stop an agent that does not pass through itself. | A93; B063, B106; C073 | Microsoft, AWS, Google | High that the gap is real; medium on placement |
| 5 | **Widen Policy's wording to content rules.** Policy now reads "whether an action is allowed, how long stored data is retained". All three vendors place content filtering of prompts, model outputs and tool payloads (injection, harmful content, sensitive data) in their governance components. Either Policy covers "rules on content entering and leaving models and tools", or WARM names a separate guardrail responsibility. The industry-terms column already lists "guardrails". | A88, A99; B060, B064, B072; C011, C062 | Microsoft, AWS, Google | High |
| 6 | **List tenancy as a concern that is not a group**, beside Security and Cost, and say which services carry a tenant scope (Identity, Policy, Sessions, Memory, Observability, Releases). Note that a domain may be implemented as a tenant (Google's business-unit tenant projects). v0.11 recorded tenancy from one platform and did not adopt it. | B104 (focus area and a whole guide); C092-C103; MAP memory scope by tenant | AWS, Google (Microsoft in passing) | Medium |
| 7 | **Develop the person-as-subject relation for stored data**: subject-initiated see, correct, delete and opt-out, as part of Policy's rules on stored data and Memory's duty to keep entries current. | A66 ("Users must be able to see, edit, and delete what the system remembers about them"); C136 | Microsoft, Google | Medium |
| 8 | **Say that a handoff may be carried by a tool call.** Agent-as-a-tool is common; WARM's handoff names Orchestration and Messaging only. State that an agent invoked as a tool is still an assignment Orchestration tracks, or admit Tools as a carrier of assignments. | C020, DS ("by using the agent as a tool feature"); A107 (agents exposed as tools); B173 (agent graph meta-tools) | Google, Microsoft, AWS | Medium |
| 9 | **Include models in what Releases versions and Improvement may propose**, and say where an approved-model list lives (Models or Policy). Fine-tuning and model approval are changes WARM does not place. | B007, B009, B116, B147; C080; GOV "Model oversight" | AWS, Google, Microsoft | Medium-low |
| 10 | **Draw the line between a skill and fetched material.** Google keeps skills in a Skill Registry (C022) and also stores "AI runbooks ... in the form of Agent Skills" in a RAG database (C114); Microsoft says a written procedure belongs "in a knowledge source or in a tool, not in memory". WARM puts skills in the Registry and fetched material in Retrieval, but does not say which a runbook is. | C022, C114; A46 | Google, Microsoft | Medium-low |
| 11 | **Say whether a release can restore memory.** Microsoft's rollback snapshots include "memory state"; WARM says memory persists through a change of definition. | A119; BEH ("memory snapshots") | Microsoft | Low |
| 12 | **Allow a domain's parts to be written for a single agent** when a domain has one agent, and say how that relates to the charter. All three attach goals, roles, rules and success criteria to agents. This is not evidence that WARM's separation is wrong; it is evidence that no source makes it. | B088, B118; A08; C072, C094 | AWS, Microsoft, Google | Low |
| 13 | **Keep caching and metering out**, recorded as implementation or commercial concerns. Recorded again here so that a later version does not re-derive them: caching in two sources, metering in two. | A109, C120, C018; B117, C100 | Microsoft, Google, AWS | Low (that WARM should change) |
| 14 | **Reconsider the phrase "acceptance criteria".** AWS argues for "behavioral guardrails" instead, on non-determinism, while still asking for "measurable success criteria". WARM's Evaluation already returns judgments. A wording question only. | B119 | AWS | Low |

## What WARM has that the sources do not

| WARM part or claim | Microsoft | AWS | Google |
|---|---|---|---|
| **Directory** (accountable domain per scoped responsibility, and how to reach a role) | Absent; `owners` tag and endpoints only | Absent; "ownership, and business purpose" fields on asset entries | Absent; name-to-endpoint discovery and user-to-tenant routing |
| **Domain as a charter separate from its agents** (seven parts) | Absent; domain = agent's expertise | Absent; parts written per agent (intent and scope, zones of intent) | Partly: business units with their own tools, rules, data and one agent (MTN); no charter |
| **Responsibility at the hand-off grain; exactly one accountable domain** | Absent | Absent | Absent |
| **Agent as an identified actor distinct from its definition**; a definition shared by several agents | Absent (agents are services) | Absent ("an application" with a job title) | Absent ("an application") |
| **Persistent agent versus task agent by lifetime** | Absent | Implicit only (personal assistant, autonomous team agent; worker agents) | Absent |
| **The platform test** ("works the same whatever the work is about") | Absent | Absent | Applied without being stated: shared versus tenant-specific MCP servers (C097, C098) |
| **Working versus cross-cutting groups** | Absent | Partly: "cross-layer concerns" (observability, security, discoverability) | Absent |
| **Improvement separate from Releases, with a person or release process deciding** | Improvement only as human practice | Improvement register and reflective agents; who decides is not stated | Prompt optimizer only |
| **Tasks as a contract every runtime meets** | Task IDs in async request-reply only | Step Functions checkpoints; worker retry | Durable, resumable workflows |
| **Artifacts as a versioned store of work products** | Absent | S3 for outputs, no versions | One use case (artifact service), no versions |
| **Scheduling as a platform service** | Two scheduled jobs | Events and an end-user scheduling interface | Events only |
| **Evaluation reports "unknown" when a check cannot run** | Absent | Absent | Absent |
| **Governance covers an action only at an enforcement point** (stated as a condition) | Embodied in the MCP policy check, not stated | Embodied in gateways and interceptors, not stated | Embodied in Agent Gateway ("default-deny"), not stated |

What the sources have and WARM leaves unstated, beyond the misfits: organizational governance models (centralized, federated, hybrid: B017-B019); maturity scales for agents and for versioning (A121, B089); use-case typologies that set governance rigor (B001-B005); release techniques (shadow agents, ring deployment, aliases: A116, A120, B158); memory engineering in depth (scoring, decay, tiers, promotion pipelines: A62-A73). These are guidance or implementation detail of existing WARM services and suggest no structural change.
