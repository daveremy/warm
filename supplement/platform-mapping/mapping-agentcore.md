---
title: "WARM v0.10 mapped onto Amazon Bedrock AgentCore"
date: 2026-11-11
author: research subagent (mapping)
inputs: warm-model-v0.10.md (Steps 1 to 4, Glossary); platform-mapping/inventory-agentcore.md (146 components, read 2026-11-11)
not-read: platform-mapping/predictions.md
---

# WARM v0.10 mapped onto Amazon Bedrock AgentCore

Purpose: test WARM against a platform it was not built from. The inventory was written by a researcher who had not seen WARM, in the vendor's own grouping. The rule used here: when a fit needed more than one sentence it is marked strained, and when in doubt between a fit and a misfit, the component is a misfit.

## Summary

| Class | Count | Clear | Strained |
|---|---|---|---|
| (a) one WARM service | 92 | 68 | 24 |
| (b) a non-platform layer (all Infrastructure) | 5 | 3 | 2 |
| (c) builder tooling | 10 | 9 | 1 |
| (d) SPANS two or more services | 28 | 18 | 10 |
| (e) MISFIT | 11 | 4 | 7 |
| **Total** | **146** | | |

- Fits (a + b + c): 107, of which **27 are strained** (25%).
- No component mapped to the People or Domains layer, and none to Providers. AgentCore has no concept of a domain.
- 6 of 22 services have no direct match: Scheduling, Artifacts, Messaging, Human channels, Approvals, Reliability. After searching the docs: Scheduling is ABSENT; the other five are PARTIAL. Tasks and Registry have matches but cover only part of their WARM responsibility.
- The 11 misfits fall into four clusters: the inbound invocation endpoint (5), payments (4), platform-generated changes (1) and a judgment-bearing connector (1).
- "Strained" on a MISFIT row means I am not sure it is a misfit; "clear" means I am sure no service holds it.

Two inventory slips, noted and not corrected: C71 cites "configuration bundles (C125)", which is C130; C13 cites "AgentCore Memory (C39)", which is C41.

## Full assignment table

| # | Component | Class | Assignment | Confidence | Reason |
|---|---|---|---|---|---|
| C1 | AgentCore CLI | (c) builder tooling | Builder tooling | clear | A local command-line tool for building, deploying and operating projects. |
| C2 | Agent Inspector (part of the CLI) | (c) builder tooling | Builder tooling | clear | A local developer UI for chatting with an agent and viewing traces during `agentcore dev`. |
| C3 | AgentCore Python SDK | (c) builder tooling | Builder tooling | clear | A library for writing agent code against the platform. |
| C4 | AgentCore TypeScript SDK | (c) builder tooling | Builder tooling | clear | A library for writing agent code against the platform. |
| C5 | AgentCore MCP Server | (c) builder tooling | Builder tooling | clear | Lets a coding assistant transform, deploy and test agents; it serves the builder, not the agent. |
| C6 | AWS SDK, AWS CLI, AgentCore console | (c) builder tooling | Builder tooling | clear | Generic API clients and console for builders and operators. |
| C7 | AWS CDK constructs | (c) builder tooling | Builder tooling | clear | Infrastructure templates. |
| C8 | AgentCore harness | (d) spans | Harness, Sessions, Environments, Memory, Tools, Observability | clear | A harness product: "AgentCore handles the environment, compute, memory, identity, networking, and observability" around a managed loop. |
| C9 | Harness: Models and instructions (managed defaults) | (d) spans | Harness, Models, Registry | strained | Holds the agent definition (model, system prompt, tools, limits) inside the harness resource and chooses the provider; WARM puts the definition in Registry and model choice in Models. |
| C10 | Harness: Tools (including built-in tools) | (d) spans | Tools, Environments, Orchestration, Harness, Retrieval | clear | Tool mediation plus built-ins that are other services: `shell`/`read`/`write` (Environments), `subagent` (Orchestration), `retrieve_context` (Harness context management), `web_fetch` (Retrieval). |
| C11 | Harness: Lifecycle hooks | (d) spans | Policy, Observability | clear | A Lambda hook returns allow or deny (Policy); SNS and EventBridge hooks only notify (Observability). |
| C12 | Harness: Skills | (d) spans | Harness, Registry, Memory | strained | Skills are files loaded from Git, S3 or a container as part of the agent's configuration; WARM splits skills across Memory (holds), Registry (indexes) and the definition (names), and AgentCore Memory holds none of them. |
| C13 | Harness: Memory | (d) spans | Sessions, Memory | clear | Persists conversation state in AgentCore Memory: session history and, with strategies, long-term memory. |
| C14 | Harness: Environment and filesystem | (a) service | Environments | clear | Every harness session runs in an isolated microVM with its own filesystem and shell. |
| C15 | Harness: Interactive shells (terminals) | (a) service | Environments | strained | Opens the agent's isolated environment to a person or program over WebSocket, outside the agent loop. |
| C16 | Harness: Observability and cost controls | (a) service | Observability | strained | Traces, logs and metrics fit; "cost controls" (execution limits) would be Policy, and the inventory does not describe them. |
| C17 | Harness: Versioning and endpoints | (a) service | Releases | clear | Automatic versions and endpoints that point at a version. |
| C18 | Harness: Export to code | (c) builder tooling | Builder tooling | clear | Generates editable source code for the developer. |
| C19 | Harness: Security | (a) service | Policy | strained | Access controls for the harness; the inventory gives only the page title, so the fit is a guess between Identity and Policy. |
| C20 | Step Functions integration with AgentCore harness | (a) service | Orchestration | clear | Embeds agent steps in a workflow of fixed steps. |
| C21 | AgentCore Runtime | (d) spans | Environments, Sessions, Tasks | clear | Hosts agent or tool code per session in an isolated microVM and manages session lifecycle. |
| C22 | Compute type: microVMs | (b) layer | Infrastructure | clear | A choice of compute the platform runs on. |
| C23 | Compute type: Instances (with capacity providers) | (b) layer | Infrastructure | clear | EC2 instances in the customer's account defined by a capacity provider. |
| C24 | Platform versions (V1, V2) | (b) layer | Infrastructure | strained | Controls how the runtime starts an agent (from a snapshot); an implementation variant of the hosting layer, not a responsibility. |
| C25 | Runtime service contract and protocols (HTTP, MCP, A2A, AG-UI) | (d) spans | Human channels, Messaging, Tools | clear | One contract covers AG-UI (to people), A2A (to agents) and MCP (as a tool server). |
| C26 | Direct code deployment | (a) service | Releases | clear | Deploys a new agent version from a zip. |
| C27 | Amazon Bedrock Managed Agents (with OpenAI) | (a) service | Harness | strained | Hosts another vendor's harness product (Codex) on the same platform; WARM's Harness service, but delivered as a whole second harness. |
| C28 | Isolated sessions, lifecycle settings, stop session | (d) spans | Environments, Sessions, Tasks | clear | A runtime "session" is a microVM lifetime (Environments) with lifecycle and stop controls (Tasks); its state is "ephemeral". |
| C29 | File system configurations | (a) service | Environments | strained | A workspace for the agent; managed session storage also persists state across stop and resume, which is Sessions' job. |
| C30 | Mount your own file systems (FUSE) | (a) service | Environments | clear | Mounts storage into the agent's workspace. |
| C31 | Asynchronous and long-running agents | (a) service | Tasks | clear | `add_async_task` and `complete_async_task` track background work after the agent has replied. |
| C32 | Stream agent responses | (e) MISFIT | (none: invocation endpoint) | strained | Part of the application-facing invocation interface, which WARM does not model (see MISFIT list). |
| C33 | Bidirectional streaming (WebSocket, WebRTC) | (e) MISFIT | (none: invocation endpoint) | strained | Same invocation interface, here for voice and real-time clients. |
| C34 | Pass custom headers | (e) MISFIT | (none: invocation endpoint) | strained | Passes context from the calling application to agent code; plumbing of the invocation interface. |
| C35 | Inbound Auth and Outbound Auth (Runtime) | (d) spans | Identity, Secrets | clear | Inbound auth establishes who calls; outbound auth releases credentials for third-party services. |
| C36 | Runtime versioning and endpoints | (a) service | Releases | clear | Automatic versions; "Control rollout by updating endpoints". |
| C37 | Invoke an agent | (e) MISFIT | (none: invocation endpoint) | clear | The API by which any caller (an app, a scheduler, a workflow, another agent) starts or continues a session; WARM has no service for an inbound endpoint. |
| C38 | Session endpoints | (e) MISFIT | (none: invocation endpoint) | strained | An authenticated URL to an application server running inside one session; ingress to a running environment. |
| C39 | Shell execution (one-shot and interactive) | (a) service | Environments | strained | Runs commands in the agent's environment directly, "without passing through the LLM". |
| C40 | Observe agents (Runtime) | (a) service | Observability | clear | Points to Observability. |
| C41 | AgentCore Memory | (d) spans | Sessions, Memory | clear | One product holds short-term events (Sessions) and long-term records (Memory). |
| C42 | Short-term memory (events) | (a) service | Sessions | clear | Raw interactions ... within a single session. |
| C43 | Long-term memory (memory records) | (a) service | Memory | clear | Persists across sessions. |
| C44 | Built-in strategy: Semantic | (a) service | Memory | clear | Semantic facts. |
| C45 | Built-in strategy: User preference | (a) service | Memory | clear | Facts about the user. |
| C46 | Built-in strategy: Summary | (a) service | Sessions | strained | Summaries of one session, stored as Memory records; close to Harness compaction. |
| C47 | Built-in strategy: Episodic (with reflections) | (a) service | Memory | clear | Episodic memory, named in WARM. |
| C48 | Built-in with overrides strategy | (a) service | Memory | clear | Custom extraction instructions and model. |
| C49 | Self-managed strategy | (a) service | Memory | clear | Developer-built extraction; AgentCore stores and retrieves. |
| C50 | Memory organization (actor, session, strategy, namespace) | (a) service | Memory | clear | How memories are partitioned. |
| C51 | Memory record streaming | (a) service | Memory | strained | Change notifications to Kinesis; used for replication and integration. |
| C52 | Cross-account memory access | (a) service | Memory | strained | Sharing a memory resource across accounts is an access rule as much as a memory feature. |
| C53 | Record time-to-live (TTL) | (a) service | Memory | clear | Retires records, part of keeping memory current. |
| C54 | Direct long-term memory ingestion (IngestData) | (a) service | Memory | clear | Writes content directly to long-term memory. |
| C55 | Long-term memory metadata (filtering) | (a) service | Memory | clear | Structured attributes on records. |
| C56 | Redrive failed ingestions | (a) service | Memory | strained | Memory's own retry queue; retry is Tasks' and restore is Reliability's in WARM. |
| C57 | Access Memory through a gateway (Memory connector) | (d) spans | Memory, Tools, Policy | clear | Puts Memory behind the tool gateway so Policy enforcement applies to memory access. |
| C58 | Memory encryption and memory replication | (d) spans | Secrets, Reliability | strained | Customer-managed keys (key custody) and cross-Region replication (recovery). |
| C59 | AgentCore Gateway | (d) spans | Tools, Models, Messaging, Policy, Identity | clear | Connecting agents to tools, to other agents, and to large language models, with auth and policy at the entry point. |
| C60 | MCP targets | (a) service | Tools | clear | Aggregates tool backends into one MCP server. |
| C61 | Built-in templates from integration providers | (a) service | Tools | clear | Connector templates for external services. |
| C62 | Built-in connector: Managed Knowledge Bases | (a) service | Retrieval | clear | Managed RAG exposed as a connector. |
| C63 | Built-in connector: Web Search Tool | (a) service | Retrieval | clear | Fetches web results; WARM names search as Retrieval. |
| C64 | Built-in connector: Web Answer | (e) MISFIT | (none: judgment sold as a platform service) | strained | Returns "a synthesized answer with citations"; by WARM's own test (applies judgment) that is domain work, yet it is offered as a platform connector. |
| C65 | Built-in connector: AWS Step Functions | (a) service | Tools | clear | Exposes workflow operations as tools. |
| C66 | HTTP targets: Runtime targets and HTTP passthrough | (d) spans | Tools, Messaging | clear | Fronts external APIs (Tools) and other agents, including A2A passthrough (Messaging). |
| C67 | Inference targets | (a) service | Models | clear | A unified LLM proxy layer routing by model. |
| C68 | Gateway authorizer and credential providers | (d) spans | Identity, Secrets | clear | Inbound authorization and outbound credential release. |
| C69 | Semantic search of tools | (a) service | Registry | clear | Finds tools by natural-language query when a task needs one. |
| C70 | MCP protocol features | (d) spans | Tools, Tasks, Sessions, Human channels | clear | MCP sessions (Sessions), tasks (Tasks), elicitation (to a person) on top of tool calls. |
| C71 | Gateway rules (routing, model fallback, session stickiness) | (d) spans | Models, Tools | clear | Model fallback chains and target routing overrides. |
| C72 | Fine-grained access control and Gateway interceptors | (a) service | Policy | strained | Access control fits; interceptors are arbitrary request and response code, wider than rule evaluation. |
| C73 | Rate limits | (a) service | Policy | strained | A limit enforced per caller, target or tool; could also be read as Reliability (protecting availability). |
| C74 | AWS WAF integration | (b) layer | Infrastructure | strained | Perimeter network security in front of the gateway. |
| C75 | Other Gateway features (debug, KMS, domains, headers, MCP Inspector, CloudTrail, VPC egress) | (d) spans | Observability, Secrets, Infrastructure | strained | A grab bag of logging, key custody, networking and builder tooling. |
| C76 | AgentCore Identity | (d) spans | Identity, Secrets | clear | An identity and credential management service: both who acts and what credentials they get. |
| C77 | Workload identities and the agent identity directory | (a) service | Identity | clear | Identities for agents; the "directory" lists identities, not responsibilities. |
| C78 | Token vault | (a) service | Secrets | clear | Stores tokens, client credentials and API keys. |
| C79 | Inbound JWT authorizer | (a) service | Identity | clear | Authenticates callers. |
| C80 | Credential providers (OAuth2 client, API key) | (a) service | Secrets | clear | Releases a credential to the component that needs it at the point of use. |
| C81 | Provider setup (built-in IdP configurations) | (a) service | Identity | clear | Configurations for external identity providers. |
| C82 | On-behalf-of token exchange | (a) service | Identity | clear | Establishes on whose behalf an agent acts. |
| C83 | Private Key JWT client authentication | (a) service | Identity | strained | How the platform authenticates itself to an IdP; touches Secrets (signing key). |
| C84 | Workload access token | (a) service | Identity | clear | A token combining user identity and agent workload identity. |
| C85 | Consent portal | (d) spans | Identity, Approvals | strained | Authenticates an end user and records their consent before delegated access; a grant, not a per-action approval. |
| C86 | Private identity providers | (a) service | Identity | clear | IdPs inside a VPC. |
| C87 | Identity data protection and tagging | (a) service | Secrets | strained | KMS key for the token vault; tagging is builder tooling. |
| C88 | AgentCore payments | (e) MISFIT | (none: payments) | clear | Pays for APIs, tools and content on the agent's behalf; WARM has no service for spending money. |
| C89 | PaymentManager | (e) MISFIT | (none: payments) | clear | Top-level resource that coordinates payment operations. |
| C90 | PaymentConnector | (e) MISFIT | (none: payments) | strained | Links the payment service to an external wallet provider; connector-like, but only meaningful inside the payments service. |
| C91 | Payment sessions and payment instruments | (d) spans | Policy, Secrets | strained | Per-session spending limits (Policy) and the user's payment credentials (Secrets). |
| C92 | Coinbase x402 Bazaar via Gateway | (a) service | Tools | strained | A catalog of paid MCP tools added as a gateway target; discovery is also Registry-like. |
| C93 | Payments Browser Tool integration and framework integrations | (e) MISFIT | (none: payments) | strained | The payment path through the browser and agent frameworks. |
| C94 | AgentCore Code Interpreter | (a) service | Environments | clear | A sandbox for running code. |
| C95 | AgentCore Browser | (a) service | Environments | clear | An isolated browser; WARM names browsers under Environments. |
| C96 | Browser: Live View | (d) spans | Observability, Human channels | strained | A person watches, and can take over, the agent's browser. |
| C97 | Browser: Session Recording and Replay | (a) service | Observability | clear | Captures interactions as evidence. |
| C98 | Browser: CloudWatch metrics | (a) service | Observability | clear | Metrics. |
| C99 | Browser: Web Bot Auth | (a) service | Identity | clear | Signs agent traffic so websites know who is acting. |
| C100 | Browser extensions | (a) service | Environments | clear | Configures the environment. |
| C101 | Browser profiles | (a) service | Environments | strained | Persists browser state across sessions, which is closer to Sessions or Memory for one tool. |
| C102 | Browser proxies | (a) service | Environments | strained | Routes the environment's traffic; could be Infrastructure. |
| C103 | Browser enterprise policies | (a) service | Policy | strained | Chromium rules enforced on the environment; Policy of a tool rather than of an agent action. |
| C104 | Root Certificate Authority (Browser and Code Interpreter) | (a) service | Environments | strained | Trust configuration for the sandbox, fetched from Secrets Manager. |
| C105 | Browser OS action (InvokeBrowser) | (a) service | Environments | clear | OS-level control of the browser environment. |
| C106 | AgentCore Web Search (InvokeWebSearch API) | (a) service | Retrieval | clear | Web search callable from code. |
| C107 | AgentCore Observability | (a) service | Observability | clear | Tracing, metrics and audit logging. |
| C108 | Cross-account monitoring | (a) service | Observability | clear | Observability across accounts. |
| C109 | Policy in AgentCore | (a) service | Policy | clear | Intercepts gateway traffic and evaluates each request. |
| C110 | Policy engine | (a) service | Policy | clear | Stores and evaluates Cedar policies. |
| C111 | Policy languages: Cedar and Dogwood | (a) service | Policy | clear | The rule language. |
| C112 | Policy authoring service (natural language) | (c) builder tooling | Builder tooling | strained | An authoring aid that turns requirements into Cedar; serves the people who write rules. |
| C113 | Guardrails in policies | (a) service | Policy | clear | Content-based policy decisions. |
| C114 | Temporal policies and policy sessions | (a) service | Policy | clear | Decisions that depend on the history within a session. |
| C115 | Policy enforcement modes | (a) service | Policy | clear | LOG_ONLY or ENFORCE. |
| C116 | Policy validation and analysis | (a) service | Policy | strained | Automated reasoning over the rules themselves; also Evaluation of a governance artifact, or builder tooling. |
| C117 | AgentCore Evaluations | (a) service | Evaluation | clear | Assesses agents against criteria. |
| C118 | Built-in evaluators | (a) service | Evaluation | clear | Predefined criteria. |
| C119 | Skill evaluators | (a) service | Evaluation | clear | Criteria for skill selection and use. |
| C120 | Insight evaluators and Failure analysis | (a) service | Evaluation | clear | Explains what went wrong. |
| C121 | Third-party evaluators | (a) service | Evaluation | clear | External evaluator libraries. |
| C122 | Custom evaluators | (a) service | Evaluation | clear | Developer-defined criteria. |
| C123 | Online evaluation | (a) service | Evaluation | clear | Continuous evaluation of live traffic. |
| C124 | On-demand evaluation (with ground truth) | (a) service | Evaluation | clear | Evaluates chosen spans. |
| C125 | Batch evaluation (with insights) | (a) service | Evaluation | clear | Evaluates many sessions in one job. |
| C126 | Dataset evaluation (dataset runners) | (a) service | Evaluation | clear | Invokes the agent on a dataset and evaluates. |
| C127 | Simulation (user simulation) | (a) service | Evaluation | clear | Generates simulated users to evaluate against. |
| C128 | Diagnose with AI assistant (Evaluation Diagnostic Skill) | (c) builder tooling | Builder tooling | clear | A markdown skill for the builder's coding assistant. |
| C129 | AgentCore optimization | (d) spans | Evaluation, Releases | strained | Recommendations, bundles and A/B tests: an improvement loop built on Evaluation and Releases, plus generation of changes, which no WARM service does. |
| C130 | Configuration bundles | (a) service | Releases | strained | A versioned, immutable snapshot of prompts, model IDs and tool descriptions; also a second home for the agent definition. |
| C131 | Recommendations (system prompt, tool description) | (e) MISFIT | (none: platform-generated changes) | clear | The platform writes new prompts and tool descriptions from traces; WARM gives that to the domain's improve stage. |
| C132 | A/B testing | (d) spans | Releases, Evaluation | clear | Splits live traffic between variants (Releases) and measures significance (Evaluation). |
| C133 | AgentCore insights (being retired) | (a) service | Evaluation | clear | Analysis reports, replaced by batch insights. |
| C134 | AWS Agent Registry | (a) service | Registry | clear | A centralized catalog of agents, tools, MCP servers and skills. |
| C135 | Registries and registry records | (a) service | Registry | clear | The catalog's resources. |
| C136 | Curation and approval workflow | (d) spans | Registry, Approvals | clear | A curator approves a record before it becomes active: an approval gate on the catalog. |
| C137 | Discovery: hybrid search, catalog browsing, Registry MCP endpoint | (a) service | Registry | clear | Finding entries. |
| C138 | Synchronize records from external sources | (a) service | Registry | clear | Keeps entries current. |
| C139 | AWS Organizations auto-detection | (a) service | Registry | clear | Auto-catalogs runtimes and gateways. |
| C140 | Cross-account sharing with AWS RAM | (a) service | Registry | strained | Sharing a registry is an access rule as much as a registry feature. |
| C141 | Notifications (Amazon EventBridge) | (a) service | Observability | strained | Events on record lifecycle and approval transitions; could be read as Approvals reaching a person. |
| C142 | Registry PrivateLink, CloudTrail, KMS, cross-region inference, service-linked roles | (d) spans | Infrastructure, Observability, Secrets | strained | A grab bag of networking, audit logging and key custody. |
| C143 | VPC and AWS PrivateLink | (b) layer | Infrastructure | clear | Private network connections. |
| C144 | Resource-based policies | (a) service | Policy | clear | Decides which principals can invoke or manage a resource. |
| C145 | Cross-region inference (Memory, Policy, Evaluations) | (a) service | Models | strained | Chooses where a platform service's own model calls are processed; Models for internal consumers, or Infrastructure. |
| C146 | IAM, managed policies, service-linked roles, condition keys, compliance, disaster recovery, tagging | (d) spans | Identity, Policy, Reliability, Infrastructure | strained | The cloud account's identity and permission system plus resilience and compliance docs. |

## The 22 services

"Direct" lists components assigned to that service alone. "In spans" lists components that cover it among others. For each service with no direct match, the queries are recorded and the verdict comes after them.

| Group | Service | Direct | In spans | Verdict |
|---|---|---|---|---|
| Runtime | Harness | C27 | C8, C9, C10, C12 | FOUND. The harness is a product that bundles the loop with environment, memory, identity and observability (C8), and a second harness product (Codex) runs on the same platform (C27). |
| Runtime | Sessions | C42, C46 | C8, C13, C21, C28, C41, C70 | FOUND, split. Session history is Memory short-term events (C42). The thing AgentCore calls a "session" is a microVM lifetime whose "state is ephemeral" (C28, section 4.3). |
| Runtime | Tasks | C31 | C21, C28, C70 | PARTIAL. Async tasks are tracked by `add_async_task` / `complete_async_task` and a `HealthyBusy` ping; sessions can be stopped (C28); MCP tasks return a task ID (C70). No retry, recovery or checkpoint coordination is documented. Queries: "AgentCore Runtime long-running task checkpoint resume retry cancellation site:docs.aws.amazon.com"; WebFetch of https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-long-run.html (only status tracking and the 15-minute idle rule). |
| Runtime | Environments | C14, C15, C29, C30, C39, C94, C95, C100, C101, C102, C104, C105 | C8, C10, C21, C28 | FOUND. The largest and cleanest match: microVM per session, code interpreter, browser. |
| Runtime | Scheduling | none | none | **ABSENT** from AgentCore. Queries: (1) "AgentCore schedule agent invocation EventBridge Scheduler cron site:docs.aws.amazon.com": no AgentCore page; community posts point EventBridge Scheduler (a separate AWS service) at `InvokeAgentRuntime`. (2) "bedrock-agentcore devguide trigger agent on a schedule or event": harness lifecycle hooks are output only ("EventBridge does not return a hook decision", https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-lifecycle-hooks.html); the Memory `TimeBasedTrigger` API is an idle-session trigger for memory extraction, not a scheduler. Starting work at a time or on an event is left to the surrounding cloud. |
| Knowledge | Memory | C43, C44, C45, C47 to C56 | C8, C12, C13, C41, C57 | FOUND for semantic and episodic memory, with extraction strategies, TTL and redrive. The inventory does not say whether records keep their source. Procedural memory (skills) is not in Memory (see C12). |
| Knowledge | Retrieval | C62, C63, C106 | C10 | FOUND. Delivered as Gateway connectors and a web search API, so the vendor files it under tools. |
| Knowledge | Artifacts | none | none | **PARTIAL.** Files persist through file system configurations (managed session storage, S3 Files, EFS, C29) and browser recordings go to S3 (C97), but there is no store of work products with versions. Queries: (1) "AgentCore harness artifacts output files store versions site:docs.aws.amazon.com": only harness versioning pages; the harness overview says the agent "can persist short-term and long-term memories and files across sessions". (2) "AgentCore store agent output files S3 session storage persist work products site:docs.aws.amazon.com bedrock-agentcore": harness guidance is "For state that needs to outlast a single session, mount S3-backed storage through AgentCore Runtime file system configurations" (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html). |
| Capabilities | Models | C67, C145 | C9, C59, C71 | FOUND. Gateway inference targets with routing by model and fallback chains. |
| Capabilities | Tools | C60, C61, C65, C92 | C8, C10, C25, C57, C59, C66, C70, C71 | FOUND. The Gateway is the tool mediator, and it also carries models, agents and memory. |
| Capabilities | Registry | C69, C134, C135, C137 to C140 | C9, C12, C136 | PARTIAL against WARM's responsibility. AWS Agent Registry catalogs agents, tools, MCP servers and skills. It does not hold the directory of responsibilities, and it does not hold the agent definition the harness loads (that lives in the harness configuration and configuration bundles). |
| Interaction | Messaging | none | C25, C59, C66 | **PARTIAL.** AgentCore hosts A2A servers and proxies requests to them ("Amazon Bedrock AgentCore acts as a proxy between clients and your A2A server", https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-a2a.html), and the Gateway can pass traffic to an A2A agent (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-http-passthrough.html). Delivery is a synchronous request; no queue, mailbox or delivery guarantee. Queries: "AgentCore agent-to-agent A2A messaging between agents site:docs.aws.amazon.com"; "AgentCore Gateway A2A target agent calls another agent asynchronous message queue site:docs.aws.amazon.com bedrock-agentcore". |
| Interaction | Orchestration | C20 | C10 | FOUND. The harness `subagent` tool and the Step Functions integration. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-tools.html |
| Interaction | Human channels | none | C25, C70, C96 | **PARTIAL.** AG-UI protocol hosting, streaming and WebRTC (C25, C32, C33), MCP elicitation (C70) and browser Live View (C96). No channel to where a person is (Slack, Teams, email); AWS's own Slack integration is built from API Gateway, Lambda, Secrets Manager and SQS around the runtime (https://aws.amazon.com/blogs/machine-learning/integrating-amazon-bedrock-agentcore-with-slack). Queries: "AgentCore agent Slack Microsoft Teams email channel deliver messages to users site:docs.aws.amazon.com bedrock-agentcore" (only an Identity page for Slack OAuth); the A2A query above, which also covers AG-UI. |
| Governance | Identity | C77, C79, C81 to C84, C86, C99 | C35, C59, C68, C76, C85, C146 | FOUND. Workload identities, on-behalf-of exchange, a token that combines user and agent identity. |
| Governance | Secrets | C78, C80, C87 | C35, C58, C68, C75, C76, C91, C142 | FOUND, inside the Identity product (token vault, credential providers). |
| Governance | Policy | C19, C72, C73, C103, C109 to C111, C113 to C116, C144 | C11, C57, C59, C91, C146 | FOUND. Enforced at the Gateway and through harness Lambda hooks. |
| Governance | Approvals | none | C85, C136 | **PARTIAL.** No service holds an agent action for a person and records the decision. The documented pattern is an inline function: "The harness pauses when the tool is called and returns the call to your code ... This is the pattern for human-in-the-loop approvals" (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-tools.html). The one native approval workflow is for Registry records (`ApprovalConfiguration`: "Configuration for the registry record approval workflow", https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ApprovalConfiguration.html). Queries: "AgentCore human in the loop approval tool call site:docs.aws.amazon.com"; "AgentCore approval workflow pause agent wait for human Step Functions callback elicitation site:docs.aws.amazon.com bedrock-agentcore" (Well-Architected points to Step Functions `.waitForTaskToken`). |
| Operations | Observability | C16, C40, C97, C98, C107, C108, C141 | C8, C11, C75, C96, C142 | FOUND. Service-provided telemetry for Runtime, Memory, Payments, Gateway, built-in tools, Identity and Policy. |
| Operations | Evaluation | C117 to C127, C133 | C129, C132 | FOUND, and richer than WARM's sentence: online, batch, dataset, simulated users, failure analysis. The inventory does not mention an "unknown" verdict for a check that could not run. |
| Operations | Releases | C17, C26, C36, C130 | C129, C132 | FOUND. Automatic versions, endpoints, immutable configuration bundles, A/B traffic split. |
| Operations | Reliability | none | C58, C146 | **PARTIAL.** Within a Region "AgentCore manages the infrastructure"; "Recovery across Regions is yours to design and operate" (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/disaster-recovery-resiliency.html). The DR pages are a build guide for the customer, and they say they do not cover Evaluations, payments, harness, optimization, Registry, Web Search or Web Answer. Queries: "AgentCore disaster recovery resiliency availability site:docs.aws.amazon.com bedrock-agentcore"; WebFetch of the resilience page. |

## MISFIT list

| # | Component | Why no service holds it | Inventory quote | URL |
|---|---|---|---|---|
| C37 | Invoke an agent | The inbound API through which any caller (an app, EventBridge, Step Functions, another agent) starts or resumes a session. Human channels is for people, Messaging for agents; WARM has no service for a generic agent endpoint. | nav item; `InvokeAgentRuntime`, `InvokeAgentRuntimeWithWebSocketStream`; "Use the same session ID for follow-up interactions to maintain context" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-invoke-agent.html |
| C32 | Stream agent responses | Same endpoint cluster: the response path of an invocation. | "shows how an AgentCore Runtime agent can stream a response back to a client." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/response-streaming.html |
| C33 | Bidirectional streaming (WebSocket, WebRTC) | Same cluster, for real-time and voice clients. | "AgentCore Runtime supports two protocols for bidirectional streaming: WebSocket ... WebRTC" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-bidirectional-streaming.html |
| C34 | Pass custom headers | Same cluster: caller-to-agent context. | "Custom headers let you pass contextual information from your application directly to your agent code" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-header-allowlist.html |
| C38 | Session endpoints | Same cluster: an addressable URL into one running session. | "A session endpoint is an authenticated HTTPS URL that addresses one runtime session." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-session-endpoints.html |
| C88 | AgentCore payments | Spending money on the agent's behalf. WARM treats cost as a concern spread over Models, Policy and Observability; it has no service that executes and settles payments. | "a fully managed service that enables microtransaction payments in AI agents to access paid APIs, MCP servers, and content." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments.html |
| C89 | PaymentManager | Same cluster. | "the top-level resource that coordinates payment operations for your AWS account." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-how-it-works.html |
| C90 | PaymentConnector | Same cluster; connector-like, but only inside payments. | "integrates your PaymentManager with an external payment provider such as Coinbase or Stripe (Privy)." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-how-it-works.html |
| C93 | Payments Browser Tool and framework integrations | Same cluster. | "There are two ways your agent can access x402 paid content: via the Browser Tool or via standard HTTP calls." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-browser.html |
| C131 | Recommendations | The platform writes changes to an agent's prompt and tool descriptions from traces. WARM's improve stage belongs to the domain, with Evaluation as evidence and Releases as rollout; no service generates the change. | "Recommendations use AI to generate optimized agent configurations from real session traces." "Review and test before applying them." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/optimization-recommendations.html |
| C64 | Web Answer connector | It synthesizes an answer, which by WARM's test ("If the provider applies its own knowledge or judgment, it is domain work") is not a platform service, yet the vendor ships it as one. It could be read as a Provider reached through Tools; I kept it a misfit because the vendor presents it as part of the platform. | "takes a natural-language question and returns a synthesized answer with citations to current web sources." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-web-answer-tool.html |

## SPANS list

| # | Component | Services | Inventory quote | URL |
|---|---|---|---|---|
| C8 | AgentCore harness | Harness, Sessions, Environments, Memory, Tools, Observability | "AgentCore handles the environment, compute, memory, identity, networking, and observability" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html |
| C9 | Harness: Models and instructions | Harness, Models, Registry | "Define a harness once with defaults for model, system prompt, tools, memory, and execution limits." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-models.html |
| C10 | Harness: Tools | Tools, Environments, Orchestration, Harness, Retrieval | built-ins "`shell`, `read`, `write`, `edit`, `file_operations`, `todo_write`, `retrieve_context`, `subagent`, `web_fetch`" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-tools.html |
| C11 | Harness: Lifecycle hooks | Policy, Observability | "send an event to an AWS Lambda function, Amazon SNS topic, or Amazon EventBridge event bus at a defined point in the harness agent loop" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-lifecycle-hooks.html |
| C12 | Harness: Skills | Harness, Registry, Memory | "bundles of markdown and scripts that give the agent domain knowledge on demand" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-skills.html |
| C13 | Harness: Memory | Sessions, Memory | "the harness persists conversation state in AgentCore Memory." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-memory.html |
| C21 | AgentCore Runtime | Environments, Sessions, Tasks | "a secure, serverless and purpose-built hosting environment for deploying and running AI agents or tools." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html |
| C25 | Runtime service contract and protocols | Human channels, Messaging, Tools | Protocols: HTTP, MCP, A2A, AG-UI | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-service-contract.html |
| C28 | Isolated sessions, lifecycle, stop session | Environments, Sessions, Tasks | "Each session in AgentCore Runtime receives its own dedicated microVM" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html |
| C35 | Inbound and Outbound Auth (Runtime) | Identity, Secrets | "Inbound Auth ... controls who can access and invoke your agents"; "Outbound Auth ... securely access third-party services" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html |
| C41 | AgentCore Memory | Sessions, Memory | short-term "within a single session"; long-term "persists across sessions" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html |
| C57 | Memory through a gateway | Memory, Tools, Policy | "move that enforcement out of your application code and into the infrastructure." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-gateway-connector.html |
| C58 | Memory encryption and replication | Secrets, Reliability | "the standby Region ... has none of your agent's memory unless you replicate it." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/disaster-recovery-memory.html |
| C59 | AgentCore Gateway | Tools, Models, Messaging, Policy, Identity | "connecting agents to tools, to other agents, and to large language models (LLMs)." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html |
| C66 | HTTP targets | Tools, Messaging | passthrough is "ideal for fronting agent URLs, external APIs, or any HTTP service" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-http-passthrough.html |
| C68 | Gateway authorizer and credential providers | Identity, Secrets | "Each gateway must have an inbound authorization configuration" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-core-concepts.html |
| C70 | MCP protocol features | Tools, Tasks, Sessions, Human channels | MCP sessions "Enable stateful interactions"; Tasks "return a task ID immediately"; elicitation | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-features.html |
| C71 | Gateway rules | Models, Tools | "With model fallback, you define an ordered chain of alternative destinations" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-rules.html |
| C75 | Other Gateway features | Observability, Secrets, Infrastructure | debugging, KMS, custom domains, CloudTrail, VPC egress | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-cloudtrail.html |
| C76 | AgentCore Identity | Identity, Secrets | "an identity and credential management service designed specifically for AI agents" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html |
| C85 | Consent portal | Identity, Approvals | "authenticates your end users ... and gathers their consent before your agent accesses a downstream resource on their behalf." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-consent-portal.html |
| C91 | Payment sessions and instruments | Policy, Secrets | "Each session has configurable payment limits"; instruments are "the end user's payment credentials" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-how-it-works.html |
| C96 | Browser: Live View | Observability, Human channels | "powered by AWS DCV. Each browser session launches a dedicated DCV server" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-dcv-integration.html |
| C129 | AgentCore optimization | Evaluation, Releases (plus change generation) | "builds on AgentCore Evaluations and introduces three capabilities: Recommendations ... Configuration bundles ... A/B testing" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/optimization.html |
| C132 | A/B testing | Releases, Evaluation | "splits live production traffic between two variants and continuously evaluates performance with statistical significance." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/ab-testing.html |
| C136 | Registry curation and approval | Registry, Approvals | "DRAFT → Submit → PENDING_APPROVAL → Approve → APPROVED" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-record-lifecycle.html |
| C142 | Registry PrivateLink, CloudTrail, KMS, etc. | Infrastructure, Observability, Secrets | nav items | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-data-protection.html |
| C146 | IAM, compliance, disaster recovery, tagging | Identity, Policy, Reliability, Infrastructure | nav items under Security | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security-iam.html |

## Step 3: the vendor's grouping against WARM's six groups

The vendor groups the platform two ways. The navigation has 13 product sections (Harness, Runtime, Memory, Gateway, Identity, Payments, Built-in tools, Web Search, Observability, Policy, Evaluations, Optimization, Registry) plus Interfaces and Security. The overview diagram groups them by lifecycle stage: **Build** (Browser, Code Interpreter, Gateway, Identity, Memory, Policy, Payments, Registry), **Deploy** (Runtime) and **Assess** (Observability, Evaluations, "Refinements": Recommendations and A/B tests).

| Vendor unit | WARM groups it covers | Where it cuts across WARM |
|---|---|---|
| Runtime | Runtime (Environments, Sessions, Tasks) and Infrastructure | Puts the compute choice (microVM, EC2 instances, platform version) in the same product as the agent's environment. |
| Harness | Runtime (Harness) plus pieces of all others | A bundle, as WARM's Step 3 predicts. |
| Memory | Runtime (Sessions) and Knowledge (Memory) | Short-term events are session history; WARM keeps them apart. |
| Gateway | Capabilities (Tools, Models), Interaction (Messaging), Governance (enforcement point) | The vendor's center of gravity: one traffic chokepoint for tools, models, agents and even memory (C57), on which Policy, rate limits and WAF hang. WARM spreads these over three groups. |
| Built-in tools, Web Search | Runtime (Environments) and Knowledge (Retrieval) | The vendor files sandboxes and search under "tools"; WARM files them under Runtime and Knowledge. |
| Identity | Governance (Identity and Secrets) | Identity and credentials are one product; WARM splits them. |
| Policy | Governance (Policy) | Clean fit. |
| Payments | none | No WARM group. |
| Observability | Operations (Observability) | Clean fit. |
| Evaluations, Optimization | Operations (Evaluation, Releases) plus change generation | Optimization adds a responsibility WARM does not have. |
| Registry | Capabilities (Registry) and a little Governance (curation approval) | A catalog, not a directory of responsibilities. |
| Interfaces | none (builder tooling) | WARM does not model the builder's interface. |
| Security | Governance and Infrastructure | IAM, VPC, compliance and DR in one section. |

Does the vendor treat identity, policy and observability as applying across everything else?

- **Observability: yes.** The service-provided data page covers Runtime, Memory, Payments, Gateway, built-in tools, Identity and Policy, and every harness invocation "automatically generates traces, logs, and metrics". The harness diagram draws observability as a layer under the harness, beside identity and evaluations.
- **Identity: yes in practice.** Workload identities are created "automatically by AgentCore Runtime and Gateway"; Runtime does inbound and outbound auth; payments sign with credentials "from AgentCore Identity"; the browser signs traffic (Web Bot Auth).
- **Policy: only at chokepoints.** "Policy in AgentCore intercepts all agent traffic through Amazon Bedrock AgentCore Gateways." Traffic that does not go through a gateway is not covered: the harness accepts a remote MCP URL with "No Gateway required for simple cases", and memory is under policy only if it is put behind a gateway (C57). Harness Lambda hooks are a second enforcement point inside the loop. WARM's claim that Policy acts on "every tool call, message and memory write ... without the cooperation of the agent" holds in AgentCore only for the traffic routed through those two points.
- The overview diagram puts Identity and Policy in **Build**, next to tools and memory, not in a cross-cutting band. The lifecycle grouping (build, deploy, assess) is a different axis from WARM's (what question a service answers); Assess lines up with WARM's Operations, minus Releases and Reliability.

## Step 4: WARM ideas in the platform

**A domain or area of work with roles.** Not found. `[no-record: domain, area of work, team or role concept searched=inventory-agentcore.md full text (grep team, department, owner, responsib, persona, role, organization)]`. "Role" appears only as an IAM execution role. The nearest concept is the organization in the Registry: "a centralized catalog for organizing, curating, and discovering resources across your organization" (C134). Memory partitions by "actor" and "namespace" (C50), which identify users, not areas of work.

**A directory of who is responsible for what.** Not found as such. Two things are named "directory" or catalog, and neither records responsibility:
- "The agent identity directory is a centralized collection of all workload identities within your AWS account." (C77)
- The Registry publishes "MCP servers, tools, agents, agent skills, and custom resources" with a custom metadata schema (C134, C135). A custom schema could hold a responsibility field; nothing in the docs says so. A2A Agent Cards "describe an A2A server's identity, capabilities, skills, service endpoint, and authentication requirements" (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-a2a.html): capabilities, not accountability.

**Persistent agents and short-lived task agents.** The task agent exists: the `subagent` tool "Lets the agent delegate a self-contained task to a fresh child agent and receive its result. The child is not a separately configured harness." (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-tools.html). A persistent agent is not a first-class thing. Sessions last up to 8 hours on microVMs and "persistent sessions of up to 14 days" on Instances (C23), and "Session state is ephemeral and should not be used for long-term durability (use AgentCore Memory for context durability)" (section 4.3). So persistence is something a developer assembles from session IDs plus Memory keyed by actor; the platform has deployed agents (runtimes, harnesses) and sessions, not agents that keep a role.

**Conversation separated from scheduled or background work.** The platform does the opposite of WARM's design guidance. Background work runs in the same session as the conversation: an agent can "Immediately respond to the user saying 'I've started working on this' / Continue processing in the background / Allow the user to check back later for results" (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-long-run.html). Scheduled work has no native home (Scheduling is ABSENT). The harness-versus-runtime split is about configuration versus code, not about conversation versus jobs. One partial separation exists: a microVM per session means a background run in its own session does not share a context window, but nothing in the docs recommends that pattern.

**An improvement loop that turns evaluation into changes.** Found, and more complete than WARM's. The optimization loop: "Recommendations: Analyze agent traces, Generate optimized prompts and tool descriptions" → "Configuration Bundles (optional): Version the change as an immutable snapshot" → "A/B Testing: Split traffic between control and treatment, Measure with statistical significance" → "Deploy Winner: Route 100% traffic to winning variant", with "Monitor traces, re-optimize as needed" (section 4.8, https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/optimization.html). The platform proposes the change, and a person is told to "Review and test before applying them."

## What this says about the model

Each item says which kind of problem it is: a missing service, a boundary in the wrong place, or a service this platform does not need.

1. **Missing service: the agent's inbound endpoint.** Five misfits (C32, C33, C34, C37, C38) are one thing: an addressable, authenticated, streaming API that starts or resumes a session for any caller. WARM's Interaction group assumes callers are either people (Human channels) or agents (Messaging). In AgentCore the main caller is an application, and schedulers, workflows and other agents use the same `InvokeAgentRuntime` call. WARM's "How work starts" table names three starts but no service that receives them. Either Human channels should be widened into a general "Endpoints" or "Ingress" service with people as one kind of caller, or WARM needs a 23rd service.

2. **Missing service: payments.** AgentCore treats spending as a mechanism any domain can use: wallets, per-session limits, signing, settlement (C88 to C93). WARM's "Concerns that are not groups" lists cost as touching Models, Policy and Observability; that covers measuring and limiting spend, not executing it. Pieces fit (limits are Policy, wallet credentials are Secrets, paid tools are Tools), but holding funds and settling a payment has no home. If agents are to act economically, WARM needs a service for it, probably in Capabilities, gated by Approvals.

3. **Boundary: the agent definition and skills.** WARM says the Registry holds the agent definition and an index of skills, and that skills are procedural memory kept in Memory. AgentCore keeps the definition (model, system prompt, tools, skills, limits) in the harness resource (C9) and in versioned configuration bundles (C130), and versions it with Releases. Skills are files loaded from Git, S3 or a container (C12); AgentCore Memory has semantic, preference, summary and episodic strategies, and no procedural one. The Registry is a separate, organization-wide catalog for discovery. This suggests WARM's Registry bundles three responsibilities (the directory, the definitions, the skill index) that a real platform separates, and that "skills are memory" is WARM's choice rather than industry practice. A boundary closer to the vendor's: definitions and skills are versioned configuration (Releases-managed), the catalog is for discovery, and Memory is what is learned.

4. **Boundary: Sessions.** AgentCore's "session" is an isolated microVM lifetime with ephemeral state (Environments plus Tasks), while the durable history of the session lives in Memory short-term events (C42), and a summary strategy writes session summaries as Memory records (C46). WARM's Sessions service ("keep the history and state ... so a long-running agent can pause, resume and hand off") is split across two vendor products. WARM survives this (it says services are responsibilities, not products), but the word "session" will mislead anyone mapping AgentCore, and the Sessions/Memory line is drawn in a different place.

5. **Boundary: judgment inside the platform.** Two vendor services do what WARM's test assigns to a domain. Recommendations (C131) writes new prompts and tool descriptions; Web Answer (C64) synthesizes cited answers. WARM's rule ("If the provider applies its own knowledge or judgment, it is domain work") would push both out of the platform. The vendor's view is that judgment applied the same way for every domain is a mechanism. WARM should either accept that a platform service may use a model to produce a result (and say how that differs from domain judgment), or place these explicitly as Providers reached through Tools. Its own "platform agent" provision (Step 4, provisional) already points this way.

6. **Missing or misplaced: the improvement step.** WARM gives "improve" to the domain, supported by Evaluation and Releases. AgentCore makes the loop a platform product (optimization: recommend, bundle, A/B test, deploy winner, re-optimize). A/B testing itself spans Releases and Evaluation (C132). If a platform can run the loop, WARM's Operations group may need an "Improvement" (or "Optimization") service, or Releases' responsibility should include controlled experiments.

7. **Boundary: Governance is cross-cutting only through chokepoints.** AgentCore enforces policy at the Gateway and in harness hooks; traffic that bypasses them is ungoverned (a harness can call a remote MCP URL directly), and memory is covered only when fronted by a gateway. WARM's claim that cross-cutting services act "without the cooperation of the agent" is true only where all traffic is forced through a mediator. WARM should state that requirement, and note that the Tools service is where the vendor puts the mediator.

8. **Boundary: Identity and Secrets.** The vendor ships them as one product (C76: "an identity and credential management service"), with the token vault, credential providers and on-behalf-of exchange inside Identity. The join is natural because the credential released depends on who is acting and for whom. This does not show WARM's split is wrong, but the mapping had to put 6 components in SPANS (Identity, Secrets).

9. **Services this platform does not provide, which may not be agent-platform services.** Scheduling is ABSENT and left to EventBridge Scheduler; Artifacts is plain file storage (S3, EFS) without versions; cross-Region Reliability is "yours to design and operate"; Messaging is a synchronous proxy with no queue; Approvals is a client-side pattern; Human channels stops at protocols (AG-UI, WebRTC) and leaves Slack or email to the customer. A cloud vendor can omit these because general cloud services cover them. That supports one of two readings: WARM is right and AgentCore has gaps that every customer fills, or several of WARM's 22 are general infrastructure that WARM has promoted into the agent platform. The mapping cannot decide which; a second non-cloud platform could.

10. **Not modeled: builder tooling.** Ten components (CLI, SDKs, MCP server, CDK, console, Agent Inspector, export to code, natural-language policy authoring, the diagnostic skill) are interfaces for the people who build and operate the platform. WARM's People layer directs and approves; it has no interface for building. This is probably correct for a reference model of the running system, but it should be stated as out of scope.

11. **Infrastructure inside the platform product.** Compute types (C22, C23), platform versions (C24), VPC, WAF and PrivateLink are configured through the agent product. WARM's line between Environments (a place to act) and Infrastructure (where everything runs) held, but only because the assignment treats configuration choices as Infrastructure; the vendor does not draw that line.

12. **Where WARM fit well.** Environments, Memory (for facts and episodes), Identity, Secrets, Policy, Observability, Evaluation and Releases mapped cleanly with many clear fits each. The cross-cutting status of Identity and Observability matches the vendor's own architecture. The harness-as-bundle caution in Step 3 matched exactly.
