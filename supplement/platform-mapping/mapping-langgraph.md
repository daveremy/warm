---
title: "Mapping: LangGraph, LangSmith Deployment and LangSmith onto WARM v0.10"
date: 2026-11-11
type: platform-mapping
model: warm-model-v0.10.md
inventory: platform-mapping/inventory-langgraph.md (307 components)
status: draft
---

# Mapping: LangGraph, LangSmith Deployment and LangSmith onto WARM v0.10

The purpose is to test WARM, so a forced fit is the worst error. Where a fit needed more than one sentence it is marked strained, and where a fit and a misfit were both arguable the component is a misfit. Vendor documentation was read on 2026-11-11; `predictions.md` was not read.

## Summary

| Category | Count | Of which strained |
|---|---|---|
| (a) One WARM service | 183 | 46 |
| (b) A non-platform WARM layer (Infrastructure 19, Domains 2, Providers 1, People 0) | 22 | 14 |
| (c) Builder tooling (CLI, SDK, studio, consoles, test helpers, vendor documentation pages) | 55 | n/a |
| (d) Spans two or more services | 30 | n/a |
| (e) MISFIT | 17 | n/a |
| **Total** | **307** | **60 of 205 fits** |

Internal constructs assigned as a class, one class per group: graph-building constructs (32, 37 to 41, 44) to Orchestration; state constructs (34 to 36) to Sessions; persistence internals (6, 7, 11) to Sessions; Pregel execution internals (33, 61 to 63) to Orchestration, strained; streaming internals (22, 58) to Human channels, strained; trace data model (171 to 174, 177, 178, 193) to Observability; evaluation data model (237) to Evaluation.

Headline findings, explained in the last section:

1. **Sessions and Tasks are one mechanism here.** The checkpointer is the session store and the durable-execution log at once (entry 4). Eleven spans name both.
2. **LangGraph is not a harness.** The open-source library leaves the agent loop out on purpose ("does not prescribe prompts or agent architecture"). The Harness appears only in LangChain `create_agent` and Deep Agents, which the docs file outside LangGraph.
3. **Six misfit classes recur**: data protection, data retention, tenancy, outbound event notification, result caching, and the improvement machinery (Insights, Engine, Smithtune).
4. **No domain and no directory.** The platform's unit is the agent ("an agent is also the unit a workspace is organized around"). Nothing records responsibilities.
5. **Observability is the one truly cross-cutting service.** Identity and Policy are rebuilt separately by each product surface.

## Full assignment table

Confidence is given for fits (a and b) only. "s" marks a strained fit in the service lists below.

| # | Component | Assignment | Confidence | Reason |
|---|---|---|---|---|
| 1 | LangGraph overview | (d) spans: Tasks, Sessions, Orchestration, Approvals |  | The library calls itself an "orchestration framework and runtime" whose named features are durable execution, persistence, orchestration and human-in-the-loop. |
| 2 | Quickstart | (c) builder tooling (tutorial) |  | A tutorial for developers. |
| 3 | Persistence | (d) spans: Sessions, Memory |  | One layer gives "short-term memory through checkpointers and long-term memory through stores". |
| 4 | Checkpointers | (d) spans: Sessions, Tasks |  | One snapshot mechanism serves conversation state (Sessions) and "fault-tolerant execution" (Tasks). |
| 5 | Threads (LangGraph) | (a) service: Sessions | clear | A thread holds "the accumulated state of a sequence of runs". |
| 6 | Checkpoints and StateSnapshot | (a) service: Sessions | clear | Class: persistence internals. A checkpoint is the session state at one step. |
| 7 | Checkpoint namespace | (a) service: Sessions | clear | Class: persistence internals. |
| 8 | Get / update state | (a) service: Sessions | clear | Reads and edits session state. |
| 9 | Durability modes | (a) service: Tasks | strained | Sets how much of a run survives a crash, which is a recovery guarantee of Tasks, but it is configured as a write policy on Sessions storage. |
| 10 | Checkpointer libraries | (a) service: Sessions | clear | Storage backends for session state. |
| 11 | Serializer | (a) service: Sessions | clear | Class: persistence internals. |
| 12 | Checkpoint encryption | (e) MISFIT (data protection) |  | Encrypts persisted agent state; no WARM service protects stored data. |
| 13 | Checkpointer contract and conformance suite | (c) builder tooling (test helper) |  | A contract test for people who write backends. |
| 14 | Stores | (a) service: Memory | strained | Holds "facts that should survive beyond a single conversation", but has no provenance and does not keep entries current. |
| 15 | Store semantic search | (a) service: Memory | strained | Recall from Memory by meaning; WARM's Retrieval is for named sources, so this is Memory's recall, not Retrieval. |
| 16 | Retry policies | (a) service: Tasks | clear | Retry of a failed step. |
| 17 | Timeouts | (a) service: Tasks | clear | Bounds a node attempt. |
| 18 | Error handlers | (a) service: Tasks | clear | Recovery after retries are exhausted. |
| 19 | Graph defaults | (a) service: Tasks | clear | Graph-wide retry, timeout and error settings. |
| 20 | Graceful shutdown (RunControl) | (a) service: Tasks | clear | Cooperative cancellation with a resumable checkpoint. |
| 21 | Event streaming | (a) service: Human channels | strained | Carries partial results to the calling application, which may or may not be a person's channel. |
| 22 | Stream transformers, StreamChannel | (a) service: Human channels | strained | Class: streaming internals. |
| 23 | Stream modes | (a) service: Human channels | strained | Same as 21; the debug and checkpoint modes are closer to Observability. |
| 24 | Interrupts | (d) spans: Sessions, Approvals, Human channels |  | A general pause-for-input primitive: it saves session state and waits; approval is one use, asking a person a question is another. |
| 25 | Human-in-the-loop (concept) | (a) service: Approvals | clear | "The reviewer approves the call, edits its arguments, rejects it with feedback". |
| 26 | Time travel: replay and fork | (d) spans: Sessions, Tasks |  | Fork branches session history; replay re-runs a task from a checkpoint. |
| 27 | Memory (short-term and long-term) | (d) spans: Sessions, Memory, Harness |  | Thread-level history (Sessions), cross-thread store (Memory), and trimming and summarizing messages (Harness context management). |
| 28 | Subgraphs | (a) service: Orchestration | clear | Composes graphs as steps of another graph. |
| 29 | Workflows and agents (patterns) | (a) service: Orchestration | clear | Routing, orchestrator-worker, parallelization. |
| 30 | ToolNode | (a) service: Tools | strained | Executes the model's tool calls, which WARM splits between Harness (carry out) and Tools (mediate). |
| 31 | Graph API | (a) service: Orchestration | clear | Mixes "deterministic steps with LLM-driven steps" in one flow. |
| 32 | StateGraph and compiling | (a) service: Orchestration | clear | Class: graph-building constructs (32, 37, 38, 39, 40, 41, 44). |
| 33 | Super-steps | (a) service: Orchestration | strained | Class: Pregel execution internals (33, 61, 62, 63). The engine both orders steps (Orchestration) and executes them durably (Tasks). |
| 34 | State (schema) | (a) service: Sessions | clear | Class: state constructs (34, 35, 36). State is what a session keeps. |
| 35 | Reducers | (a) service: Sessions | clear | Class: state constructs. |
| 36 | MessagesState, add_messages | (a) service: Sessions | clear | Class: state constructs. |
| 37 | Nodes | (a) service: Orchestration | clear | Class: graph-building constructs. |
| 38 | START and END | (a) service: Orchestration | clear | Class: graph-building constructs. |
| 39 | Edges | (a) service: Orchestration | clear | Class: graph-building constructs. |
| 40 | Send | (a) service: Orchestration | clear | Class: graph-building constructs (fan-out). |
| 41 | Command | (a) service: Orchestration | clear | Class: graph-building constructs. |
| 42 | Configure nodes | (a) service: Tasks | clear | Retry, timeout and error settings per node. |
| 43 | Node caching (CachePolicy) | (e) MISFIT (result caching) |  | Reuses a step's result by input; WARM has no caching responsibility. |
| 44 | Runtime context | (a) service: Orchestration | clear | Class: graph-building constructs (dependency injection). |
| 45 | Recursion limit | (a) service: Tasks | strained | A hard bound on a run's steps; WARM's Policy evaluates rules, Tasks tracks runs, and neither names bounds. |
| 46 | Graph migrations | (d) spans: Releases, Sessions |  | Changing a graph is a release, and its safety depends on persisted session state. |
| 47 | Visualize your graph | (c) builder tooling |  | Debug view for developers. |
| 48 | Run a local server | (c) builder tooling |  | Local development. |
| 49 | Application structure, langgraph.json | (a) service: Releases | strained | The deployment manifest; packaging is part of releasing, but the file also declares graphs, auth and stores. |
| 50 | Test (unit testing patterns) | (c) builder tooling (test helper) |  | Unit-test patterns. |
| 51 | Backward compatibility | (d) spans: Releases, Sessions |  | "every change you ship is effectively a backward-compatible API change with respect to your existing checkpoints". |
| 52 | LangSmith Studio (pointer) | (c) builder tooling |  | IDE. |
| 53 | Agent Chat UI | (a) service: Human channels | strained | A chat front end for people, but shipped as a reference app with time-travel debugging for builders. |
| 54 | Deployment (pointer) | (b) layer: Infrastructure | strained | A pointer to hosting choices. |
| 55 | LangSmith Observability (pointer) | (a) service: Observability | clear | Pointer to tracing. |
| 56 | Frontend overview | (a) service: Human channels | strained | UI that shows a running pipeline to the user. |
| 57 | Graph execution cards | (a) service: Human channels | strained | UI component for the same. |
| 58 | Custom stream channels | (a) service: Human channels | strained | Class: streaming internals, published to the client. |
| 59 | Functional API (@entrypoint, @task) | (d) spans: Tasks, Sessions |  | Wraps functions with durable execution and persistence; a "task" is "a discrete unit of work". |
| 60 | LangGraph runtime (Pregel) | (d) spans: Tasks, Orchestration |  | The engine runs steps in order and persists them; ordering is Orchestration, durable execution is Tasks. |
| 61 | Actors (PregelNode) | (a) service: Orchestration | strained | Class: Pregel execution internals. |
| 62 | Channels | (a) service: Orchestration | strained | Class: Pregel execution internals. |
| 63 | DeltaChannel | (a) service: Orchestration | strained | Class: Pregel execution internals. |
| 64 | langgraph-supervisor | (a) service: Orchestration | clear | Supervisor multi-agent pattern. |
| 65 | Versioning and release policy | (c) builder tooling (vendor documentation) |  | The vendor's policy for its own library versions. |
| 66 | Changelog (OSS) | (c) builder tooling (vendor documentation) |  | Vendor release notes. |
| 67 | Errors reference | (c) builder tooling (vendor documentation) |  | Reference. |
| 68 | LangSmith Deployment | (d) spans: Tasks, Sessions, Releases, Reliability |  | "a workflow orchestration runtime" plus "managed infrastructure" and the deployment lifecycle. |
| 69 | Deploy to cloud quickstart | (c) builder tooling (tutorial) |  | Tutorial. |
| 70 | Agent Server | (d) spans: Tasks, Sessions, Memory, Scheduling, Messaging |  | "Handles execution, state management, and persistence"; also serves crons, store, A2A. |
| 71 | LangGraph CLI | (c) builder tooling (CLI) |  | CLI. |
| 72 | Studio | (c) builder tooling (studio) |  | IDE. |
| 73 | Deployment SDK | (c) builder tooling (SDK) |  | Client SDK. |
| 74 | RemoteGraph | (a) service: Orchestration | strained | Lets one graph call a deployed graph as a step; it is also agent-to-agent invocation (Messaging). |
| 75 | Control plane | (a) service: Releases | clear | "creating, updating, and managing Agent Server deployments". |
| 76 | Data plane | (b) layer: Infrastructure | strained | The runtime layer plus its databases: a topology term, not a responsibility. |
| 77 | Listener application | (a) service: Releases | clear | Reconciles deployments from the control plane. |
| 78 | langgraph dev / up | (c) builder tooling |  | Local servers for development and validation. |
| 79 | Deploy Google ADK agents | (c) builder tooling (SDK adapter) |  | Wrapper package so a foreign harness runs on Agent Server. |
| 80 | Deploy other frameworks | (c) builder tooling (guide) |  | Guide for wrapping other harnesses. |
| 81 | Full-stack web apps | (a) service: Human channels | strained | Embeds an agent in a web app that people use; mostly a build guide. |
| 82 | Agent Server API | (d) spans: Registry, Sessions, Tasks, Scheduling, Memory, Messaging |  | Endpoint groups: assistants, threads, runs, crons, store, A2A, MCP. |
| 83 | Control Plane API | (a) service: Releases | clear | Programmatic deployment management. |
| 84 | Agent Server changelog, release streams | (a) service: Releases | strained | Versions of the platform software itself ("Deployments use the newest stable version by default"), released by the vendor. |
| 85 | Application structure (deployment) | (a) service: Releases | strained | Same as 49. |
| 86 | Dependency setup | (c) builder tooling |  | Packaging how-to. |
| 87 | Custom Dockerfile | (c) builder tooling |  | Build customization. |
| 88 | Monorepo support | (c) builder tooling |  | Build customization. |
| 89 | Configure checkpointer backend | (a) service: Sessions | clear | Choose the session store. |
| 90 | TTLs | (e) MISFIT (data retention) |  | Deletes threads and store items after a time; WARM mentions a retention policy but gives no service the responsibility. |
| 91 | Semantic search on deployment store | (a) service: Memory | strained | Same as 15. |
| 92 | Assistants | (a) service: Registry | clear | An assistant is a versioned configuration (prompt, model, tools) over a graph: the nearest thing to an agent definition. |
| 93 | Threads (Agent Server) | (a) service: Sessions | clear | Stateful execution across runs. |
| 94 | Runs | (a) service: Tasks | clear | "A run is an invocation of an assistant." |
| 95 | Background runs | (a) service: Tasks | clear | Runs with no client waiting, "for long running jobs". |
| 96 | Multiple assistants on one thread | (a) service: Sessions | clear | A session handed from one agent to another. |
| 97 | Stateless runs | (a) service: Tasks | clear | A run with no session. |
| 98 | Cancel a run | (a) service: Tasks | clear | Cancellation. |
| 99 | Cron jobs | (a) service: Scheduling | clear | "run an assistant on a schedule". |
| 100 | Streaming API | (a) service: Human channels | strained | Same as 21, with resumable streams. |
| 101 | Human-in-the-loop (server API) | (a) service: Approvals | clear | Review, edit and approve tool calls. |
| 102 | Time travel (server API) | (d) spans: Sessions, Tasks |  | Same as 26. |
| 103 | Webhooks (Agent Server) | (e) MISFIT (outbound event notification) |  | Notifies external services of run events; WARM starts work on events but has no service that emits them. |
| 104 | Distributed tracing with Agent Server | (a) service: Observability | clear | Trace propagation. |
| 105 | MCP endpoint | (a) service: Messaging | strained | Exposes the agent to other agents and MCP clients as a callable tool, which is the reverse direction of WARM's Tools. |
| 106 | HITL over MCP (elicitation) | (d) spans: Approvals, Human channels |  | Routes an interrupt to whatever MCP client called the agent. |
| 107 | A2A endpoint | (a) service: Messaging | clear | "communicate with other A2A-compatible agents". |
| 108 | Double texting | (d) spans: Sessions, Tasks |  | A policy for a new message on a session while a run is in flight: enqueue, reject, interrupt or roll back. |
| 109 | Task queue | (a) service: Tasks | clear | Durable queue of runs. |
| 110 | Agent Server persistence | (d) spans: Sessions, Memory, Tasks |  | "core resource data, checkpoints, store". |
| 111 | Deployment modes | (b) layer: Infrastructure | strained | Runtime topology (single host, split, distributed). |
| 112 | Container architecture | (b) layer: Infrastructure | strained | API servers and queue workers. |
| 113 | Graph loading | (a) service: Harness | strained | Loads the agent's graph for each run, as WARM's Harness loads a definition, but LangGraph has no loop to load it into. |
| 114 | Collect user feedback for runs | (a) service: Evaluation | strained | End-user scores of a run; collection is a Human-channels act. |
| 115 | Generative UI | (a) service: Human channels | strained | The agent returns UI to the person, not only text. |
| 116 | CI/CD pipeline example | (a) service: Releases | strained | A pipeline that tests and deploys an agent; WARM files CI under the Software Factory domain. |
| 117 | Authentication and access control | (d) spans: Identity, Policy |  | "authentication and authorization system". |
| 118 | Custom auth handlers | (d) spans: Identity, Policy |  | @auth.authenticate (Identity) and authorization handlers (Policy). |
| 119 | Document API auth in OpenAPI | (c) builder tooling |  | Documentation config. |
| 120 | Agent Auth | (a) service: Secrets | strained | Holds OAuth tokens and releases them to the agent at use; it also acts on a user's behalf, which is Identity. |
| 121 | Server-side caching | (e) MISFIT (result caching) |  | Same class as 43. |
| 122 | IAM auth for data stores | (d) spans: Identity, Secrets |  | Workload identity generates short-lived database credentials. |
| 123 | Rebuild graph at runtime | (a) service: Harness | strained | Same as 113. |
| 124 | Encryption at rest | (e) MISFIT (data protection) |  | Same class as 12; per-tenant keys. |
| 125 | Custom store | (a) service: Memory | clear | Replace the Memory backend. |
| 126 | Custom checkpointer | (a) service: Sessions | clear | Replace the Sessions backend. |
| 127 | Custom routes | (c) builder tooling (server extension) |  | Adds HTTP routes to the server. |
| 128 | Custom middleware | (a) service: Policy | strained | A generic hook point used for "logging request metrics, injecting or checking headers, and enforcing security policies". |
| 129 | Custom lifespan events | (c) builder tooling (server extension) |  | Startup and shutdown hooks. |
| 130 | HTTP headers for runtime configuration | (c) builder tooling |  | Configuration passing. |
| 131 | HTTP headers in server logs | (a) service: Observability | clear | Log content setting. |
| 132 | Deploy to Cloud | (b) layer: Infrastructure | strained | A hosting arrangement: vendor operates every plane. |
| 133 | Serverless and Dedicated, sizes | (b) layer: Infrastructure | clear | Capacity and scaling options. |
| 134 | Cloud platform features | (b) layer: Infrastructure | clear | Regions, static IPs, payload limits. |
| 135 | Create a deployment | (a) service: Releases | clear | Deploy. |
| 136 | Revisions | (a) service: Releases | clear | "A revision deploys a version of your application". |
| 137 | Monitor a deployment | (a) service: Observability | clear | Build logs, server logs, runtime metrics. |
| 138 | Preview builds | (a) service: Releases | clear | Preview deployments per pull request. |
| 139 | Manage a deployment | (a) service: Releases | clear | Repo, branch, auto-update, delete. |
| 140 | Cloud environment variables | (c) builder tooling (reference) |  | Reference. |
| 141 | Self-hosted overview | (b) layer: Infrastructure | clear | Run on your own infrastructure. |
| 142 | Self-hosted with control plane | (b) layer: Infrastructure | strained | Hosting arrangement. |
| 143 | Hybrid | (b) layer: Infrastructure | strained | Hosting arrangement. |
| 144 | Standalone servers | (b) layer: Infrastructure | strained | Hosting arrangement. |
| 145 | Self-hosted platform features | (b) layer: Infrastructure | clear | Databases, listeners, resources. |
| 146 | Agent Server metrics (OpenTelemetry) | (a) service: Observability | clear | Platform metrics. |
| 147 | Configure Agent Server for scale | (a) service: Reliability | strained | Capacity tuning; WARM has no capacity responsibility, and Reliability is the nearest. |
| 148 | Restricted-network build machine | (b) layer: Infrastructure | clear | Network and package mirrors. |
| 149 | Troubleshooting self-hosted | (a) service: Reliability | strained | Diagnostics before contacting support. |
| 150 | Self-hosted env vars | (c) builder tooling (reference) |  | Reference. |
| 151 | Licensing and telemetry | (e) MISFIT (vendor commercial control) |  | License validation and billing telemetry to beacon.langchain.com: a control the vendor keeps inside a customer's platform. |
| 152 | Prompt & Context Hub | (d) spans: Registry, Releases |  | "store, version, review, and update the non-code parts of your agent so you can change behavior without a full deploy". |
| 153 | Prompts, templates, commits, tags | (a) service: Registry | strained | Versioned instructions; the versioning and environment tags are Releases. |
| 154 | Playground | (c) builder tooling |  | Prompt iteration UI. |
| 155 | Prompt canvas | (c) builder tooling |  | LLM-assisted prompt editing. |
| 156 | Model connections | (a) service: Models | clear | Connect model providers. |
| 157 | Context Hub (contexts, skills, agents) | (a) service: Registry | strained | Holds versioned agent definitions and the skills themselves; WARM keeps skills in Memory and only an index in Registry. |
| 158 | Context Hub commit webhooks | (e) MISFIT (outbound event notification) |  | Same class as 103. |
| 159 | Sync prompts with GitHub | (a) service: Releases | strained | Moves prompt versions into source control. |
| 160 | Sandboxes | (a) service: Environments | clear | "isolated environments that allow agents to safely execute potentially risky operations". |
| 161 | Sandbox snapshots | (a) service: Environments | clear | Reusable sandbox filesystem. |
| 162 | Sandbox service URLs | (a) service: Environments | clear | Reach a service in a sandbox. |
| 163 | Sandbox download links | (a) service: Artifacts | strained | Hands one produced file to an outside party; it is delivery from an Environment, not storage with versions. |
| 164 | Sandbox auth proxy | (a) service: Secrets | clear | "call external APIs ... without hardcoding credentials". |
| 165 | Sandbox mounts | (a) service: Environments | clear | Attach data to a sandbox. |
| 166 | Sandbox access permissions | (a) service: Policy | strained | Access rules on one resource; who-may rules on people are Identity plus Policy. |
| 167 | Sandbox CLI and SDK | (c) builder tooling (CLI, SDK) |  | CLI and SDK. |
| 168 | Harbor integrations | (a) service: Evaluation | clear | Run and compare agent evaluations. |
| 169 | LangSmith Observability | (a) service: Observability | clear | Tracing and metrics. |
| 170 | Tracing quickstart | (c) builder tooling (tutorial) |  | Tutorial. |
| 171 | Runs (spans) | (a) service: Observability | clear | Class: trace data model (171-174, 177, 178, 193). Note the name clash with Agent Server runs. |
| 172 | Traces | (a) service: Observability | clear | Class: trace data model. |
| 173 | Threads (observability) | (a) service: Observability | clear | Class: trace data model; a third meaning of "thread". |
| 174 | Trajectories | (a) service: Observability | clear | Class: trace data model. |
| 175 | Trace containers | (a) service: Observability | strained | Organizes records by organization, workspace, agent and environment, a tenancy hierarchy WARM lacks. |
| 176 | Feedback | (a) service: Evaluation | clear | Score a run against a criterion. |
| 177 | Tags | (a) service: Observability | clear | Class: trace data model. |
| 178 | Metadata | (a) service: Observability | clear | Class: trace data model. |
| 179 | Tracing integrations | (a) service: Observability | clear | Auto-instrumentation, including other harnesses (Claude Code, Codex). |
| 180 | Trace LangGraph agents | (a) service: Observability | clear | Integration. |
| 181 | Trace with OpenTelemetry | (a) service: Observability | clear | Integration. |
| 182 | Coding agent metadata contract | (a) service: Observability | strained | A trace schema for one kind of agent (coding), so domain meaning inside a platform service. |
| 183 | Manual instrumentation | (a) service: Observability | clear | @traceable, RunTree. |
| 184 | Trace with API | (a) service: Observability | clear | REST ingestion. |
| 185 | Cost tracking | (a) service: Observability | clear | Token use and cost. |
| 186 | Usage and billing (retention tiers, limits) | (e) MISFIT (data retention; vendor commercial terms) |  | Retention tiers decide how long evidence exists, and rate limits are commercial terms. |
| 187 | Log traces to an agent | (a) service: Observability | clear | Attributes traces to an agent and environment. |
| 188 | Replicas | (a) service: Observability | clear | Fan-out of traces. |
| 189 | Trace without env vars | (c) builder tooling |  | Configuration how-to. |
| 190 | Conditional tracing | (a) service: Observability | clear | Selective tracing. |
| 191 | Sampling rate | (a) service: Observability | clear | Sampling. |
| 192 | Distributed tracing | (a) service: Observability | clear | Cross-service traces. |
| 193 | Access the current span | (a) service: Observability | clear | Class: trace data model. |
| 194 | Serverless, multimodal, generator tracing | (a) service: Observability | clear | Tracing variants. |
| 195 | Add metadata and tags | (a) service: Observability | clear | Annotate traces. |
| 196 | Prevent logging of sensitive data | (e) MISFIT (data protection) |  | Masks inputs and outputs before they leave; WARM has no data-protection responsibility. |
| 197 | Redact secrets | (d) spans: Secrets, Observability |  | Keeps credential values out of the evidence record. |
| 198 | OpenTelemetry Gateway redaction | (e) MISFIT (data protection) |  | Same class as 196. |
| 199 | Troubleshooting guides | (c) builder tooling (vendor documentation) |  | Reference. |
| 200 | View traces | (a) service: Observability | clear | Trace UI. |
| 201 | Filter traces | (a) service: Observability | clear | Query. |
| 202 | Input and output preview | (c) builder tooling |  | UI setting. |
| 203 | Manage a trace | (a) service: Observability | clear | Share, view logs. |
| 204 | Query traces (SDK) | (a) service: Observability | clear | Query API. |
| 205 | Resolve an agent environment | (c) builder tooling |  | ID lookup. |
| 206 | Query threads (SDK) | (a) service: Observability | clear | Query API. |
| 207 | LangSmith Remote MCP | (c) builder tooling |  | Lets a builder's coding agent read traces. |
| 208 | LangSmith MCP Server (deprecated) | (c) builder tooling |  | Deprecated predecessor of 207. |
| 209 | Bulk export | (a) service: Observability | clear | Export evidence. |
| 210 | Trajectory view integrations | (a) service: Observability | clear | Rendering. |
| 211 | Data type reference | (c) builder tooling (reference) |  | Reference. |
| 212 | Dashboards | (a) service: Observability | clear | Trends and health. |
| 213 | Alerts | (a) service: Reliability | strained | Notifies people of critical issues; WARM's Observability only collects, and no service raises alarms. |
| 214 | Insights | (e) MISFIT (criteria-free analysis of behavior) |  | Discovers "usage patterns, common agent behaviors, and failure modes" without stated criteria, so it is neither Observability (collect) nor Evaluation (judge against criteria). |
| 215 | Custom Apps | (c) builder tooling |  | UIs that run inside LangSmith. |
| 216 | Online evaluators: LLM-as-a-judge | (a) service: Evaluation | clear | Online evaluation. |
| 217 | Online evaluators: decision model | (a) service: Evaluation | clear | Online evaluation. |
| 218 | Online evaluators: multi-turn | (a) service: Evaluation | clear | Conversation-level evaluation. |
| 219 | Tuned Evaluators | (a) service: Evaluation | clear | Vendor-maintained judges. |
| 220 | Online evaluators: code, composite | (a) service: Evaluation | clear | Online evaluation. |
| 221 | Automation rules | (d) spans: Observability, Evaluation, Scheduling |  | Filter and sample traces, then act (evaluate, queue, add to dataset, webhook): event-triggered work over evidence. |
| 222 | Webhook notifications for rules | (e) MISFIT (outbound event notification) |  | Same class as 103. |
| 223 | LangSmith Evaluation | (a) service: Evaluation | clear | Evaluation. |
| 224 | Offline evaluations | (a) service: Evaluation | clear | Pre-deployment tests. |
| 225 | Online evaluations | (a) service: Evaluation | clear | Production monitoring. |
| 226 | Datasets and examples | (a) service: Evaluation | clear | Stated criteria as examples. |
| 227 | Experiments | (a) service: Evaluation | clear | Results of one version on a dataset. |
| 228 | Evaluators | (a) service: Evaluation | clear | Scorers. |
| 229 | Run an evaluation | (a) service: Evaluation | clear | evaluate(). |
| 230 | Target functions | (a) service: Evaluation | clear | What is evaluated. |
| 231 | Multi-turn simulation | (a) service: Evaluation | clear | Simulated users for evaluation. |
| 232 | Trajectory evaluations | (a) service: Evaluation | clear | agentevals. |
| 233 | Scoring methods | (a) service: Evaluation | clear | Score types. |
| 234 | Experiment configuration | (a) service: Evaluation | clear | Repetitions, concurrency. |
| 235 | Multimodal evaluations | (a) service: Evaluation | clear | Attachments in examples. |
| 236 | Smithtune | (e) MISFIT (model adaptation from evidence) |  | Fine-tunes a model on recorded trajectories; WARM's Models mediates and chooses models but never changes one. |
| 237 | Dataset data types | (a) service: Evaluation | clear | Class: evaluation data model. |
| 238 | Custom output rendering | (c) builder tooling |  | UI rendering. |
| 239 | Manage evaluators | (a) service: Evaluation | clear | Bind evaluators to datasets. |
| 240 | Evaluator spend limits | (a) service: Policy | clear | A spend cap, WARM's own example of a rule. |
| 241 | LLM-as-a-judge evaluator | (a) service: Evaluation | clear | Evaluator type. |
| 242 | Decision model evaluator | (a) service: Evaluation | clear | Evaluator type. |
| 243 | Code evaluator | (a) service: Evaluation | clear | Evaluator type. |
| 244 | Composite evaluator | (a) service: Evaluation | clear | Evaluator type. |
| 245 | Summary evaluator | (a) service: Evaluation | clear | Experiment-level metric. |
| 246 | Pairwise evaluation | (a) service: Evaluation | clear | Compare experiments. |
| 247 | openevals and agentevals | (a) service: Evaluation | clear | Evaluator library. |
| 248 | pytest and Vitest/Jest integrations | (c) builder tooling (test helper) |  | Test framework plug-ins. |
| 249 | Improve evaluators | (a) service: Evaluation | clear | Align judges with human feedback. |
| 250 | Annotation queues | (d) spans: Evaluation, Human channels |  | A work queue that routes runs to people so they can score them. |
| 251 | Annotation queue custom views | (c) builder tooling |  | UI. |
| 252 | Assertions | (a) service: Evaluation | clear | "turn a reviewer's English-language standards into an automated check". |
| 253 | Feedback criteria, inline annotation | (a) service: Evaluation | clear | Criteria definitions. |
| 254 | User feedback (SDK, presigned) | (a) service: Evaluation | strained | End-user scores, collected through the application, so partly Human channels. |
| 255 | Test from the Playground | (a) service: Evaluation | clear | Run an evaluation over inputs. |
| 256 | Studio for testing | (c) builder tooling (studio) |  | IDE. |
| 257 | Deploy from Studio | (c) builder tooling (studio) |  | One-click deploy from the IDE. |
| 258 | LLM Gateway | (d) spans: Models, Identity, Policy, Observability |  | "authenticates the caller, selects an upstream route, applies governance policies, translates between API formats, and traces the result". |
| 259 | Gateway API formats | (a) service: Models | clear | Translate between provider APIs. |
| 260 | Gateway for coding agents | (a) service: Models | clear | Route other harnesses' model calls. |
| 261 | Gateway decision models | (a) service: Models | clear | Route to decision models. |
| 262 | Gateway Credits | (b) layer: Providers | strained | The vendor acts as a model provider and bills for it. |
| 263 | Custom model configurations (gateway) | (a) service: Models | clear | Custom endpoints. |
| 264 | Model fallbacks | (a) service: Models | clear | Retry against backup models. |
| 265 | Gateway and provider authentication | (d) spans: Identity, Secrets |  | Caller authentication (Identity) and provider keys held as workspace secrets (Secrets). |
| 266 | Gateway traces and spend monitoring | (a) service: Observability | clear | Cost by user, key, model. |
| 267 | Gateway governance policies | (a) service: Policy | clear | Spend, rate, model access, header, data policies. |
| 268 | Build an agent (no-code) | (c) builder tooling (studio) |  | An AI-assisted agent builder. |
| 269 | LangSmith Fleet | (d) spans: Harness, Registry, Tools, Memory, Orchestration, Approvals, Scheduling, Human channels, Identity, Environments |  | A no-code agent product bundling "tools, channels, memory, sub-agents, and approvals" with schedules, identity and computer use. |
| 270 | LangSmith Tool Server | (a) service: Tools | clear | Build and serve tools with auth. |
| 271 | LangSmith Engine | (e) MISFIT (vendor-supplied improvement agent) |  | An agent that diagnoses failures in traces, proposes code fixes and opens pull requests: judgment, so by WARM's test domain work, yet offered as a platform feature. |
| 272 | Engine fix validation | (a) service: Evaluation | clear | Replays traces to confirm a fix. |
| 273 | Engine Red Teaming | (a) service: Evaluation | clear | Synthetic adversarial requests, judged. |
| 274 | Agent Registry | (a) service: Registry | strained | An inventory of agents "to govern every agent"; it records no responsibilities and does not load definitions. |
| 275 | Agent environments | (a) service: Releases | strained | Production, Staging, Development, Local separate traces and deployments by stage; the word clashes with WARM's Environments. |
| 276 | Create agent, deploy to agent environment | (a) service: Releases | strained | Binds a deployment to an agent and a stage. |
| 277 | Account, API keys, profile | (a) service: Identity | strained | API keys identify callers; the rest is account setup. |
| 278 | Billing and usage | (c) builder tooling (console) |  | Vendor account console. |
| 279 | LangSmith Cloud | (b) layer: Infrastructure | strained | A hosting arrangement in which the vendor operates everything. |
| 280 | BYOC | (b) layer: Infrastructure | strained | Hosting arrangement: vendor operates in the customer's cloud. |
| 281 | Self-hosted LangSmith | (b) layer: Infrastructure | strained | Hosting arrangement; includes disaster recovery and upgrades. |
| 282 | SmithDB | (b) layer: Infrastructure | clear | A datastore for trace data. |
| 283 | LLM auth proxy | (a) service: Identity | clear | Validates signed JWTs. |
| 284 | Mission Control | (c) builder tooling (console) |  | In-cluster operator console. |
| 285 | Self-hosted observability | (a) service: Observability | clear | Observes the platform itself. |
| 286 | Admin scripts | (c) builder tooling |  | Operator scripts. |
| 287 | Release stages, deprecation policy | (c) builder tooling (vendor documentation) |  | Vendor policy. |
| 288 | Organizations, workspaces, workload isolation | (e) MISFIT (tenancy) |  | A hierarchy of organizations and workspaces that isolates resources; WARM has no tenancy and assumes one system with one owner. |
| 289 | Tunnels | (b) layer: Infrastructure | clear | Network reach into a private network. |
| 290 | Relays | (b) layer: Infrastructure | clear | Routes sandbox egress through your network. |
| 291 | Terraform and organization API | (c) builder tooling |  | Infrastructure-as-code for the platform. |
| 292 | Agent-based workspace migration | (c) builder tooling (vendor documentation) |  | Migration guide. |
| 293 | Resource tags | (c) builder tooling |  | Organize resources. |
| 294 | Model configurations | (a) service: Models | clear | Model and parameters per feature. |
| 295 | RBAC, ABAC, teams, SSO, SCIM | (d) spans: Identity, Policy |  | Who a person is (SSO, SCIM) and what they may do (RBAC, ABAC). |
| 296 | LangSmith Chat | (c) builder tooling |  | An assistant that helps builders analyze their data. |
| 297 | LangSmith CLI | (c) builder tooling (CLI) |  | CLI. |
| 298 | LangSmith skills | (c) builder tooling |  | Skills for a builder's coding agent. |
| 299 | Audit logs | (a) service: Observability | clear | Tamper-resistant record of admin actions. |
| 300 | Data and compliance | (e) MISFIT (data retention and purging) |  | Shared-responsibility model, data purging, retention: no WARM service owns the life of data. |
| 301 | LangSmith SDK | (c) builder tooling (SDK) |  | SDK. |
| 302 | LangSmith REST API | (c) builder tooling (API) |  | API over everything. |
| 303 | LangChain create_agent | (a) service: Harness | clear | "The harness is everything around the model loop". |
| 304 | Deep Agents | (d) spans: Harness, Orchestration, Memory, Environments |  | "planning, a virtual filesystem for context, subagent spawning, and long-term memory". |
| 305 | Managed Deep Agents | (d) spans: Harness, Sessions, Tasks, Releases |  | "LangSmith runs the harness and runtime." |
| 306 | OpenWiki | (b) layer: Domains | strained | Writes knowledge for coding agents: a Software Factory tool, not a platform mechanism. |
| 307 | Deep Agents Code (dcode) | (b) layer: Domains | strained | A coding agent, so an agent of the Software Factory domain. |

## The 22 services

"Direct" lists components assigned to the service alone ("s" = strained). "In spans" lists components that cover this service among others. Searches are recorded for every service with no direct clear match, and for services whose match covers only part of the responsibility.

| Group | Service | Direct | In spans | Verdict |
|---|---|---|---|---|
| Runtime | Harness | 113s, 123s, 303 | 27, 269, 304, 305 | **FOUND, but outside LangGraph.** LangGraph has no loop; `create_agent` (303) and Deep Agents (304) supply it. Inventory search: "harness" occurs only in 1.1, 303, 304, 305 and 4.1. |
| Runtime | Sessions | 5, 6, 7, 8, 10, 11, 34, 35, 36, 89, 93, 96, 126 | 1, 3, 4, 24, 26, 27, 46, 51, 59, 68, 70, 82, 102, 108, 110, 305 | FOUND. Clean match (threads), but shares its mechanism with Tasks. |
| Runtime | Tasks | 9s, 16, 17, 18, 19, 20, 42, 45s, 94, 95, 97, 98, 109 | 1, 4, 26, 59, 60, 68, 70, 82, 102, 108, 110, 305 | FOUND. Runs, task queue, retries, cancellation, durability. |
| Runtime | Environments | 160, 161, 162, 165 | 269, 304 | FOUND. LangSmith Sandboxes. |
| Runtime | Scheduling | 99 | 70, 82, 221, 269 | FOUND, server only. Cron jobs; Fleet channels start an agent on an event ("Channels define when your agent starts running", https://docs.langchain.com/langsmith/fleet/channels). Not in the open-source library. |
| Knowledge | Memory | 14s, 15s, 91s, 125 | 3, 27, 70, 82, 110, 269, 304 | **PARTIAL.** Stores hold facts across threads but record no provenance and do not keep entries current. Searches: "LangMem memory management background memory manager LangGraph long-term memory"; "LangSmith workspace secrets agent identity Fleet" (Fleet memory pages). LangMem's background manager "automatically extracts, consolidates, and updates agent knowledge" (https://langchain-ai.github.io/langmem/), and a Fleet schedule can do "Memory synthesis: Periodically review and consolidate the agent's memory files" (https://docs.langchain.com/langsmith/fleet/schedules). No provenance field found. LangMem is not in the inventory. |
| Knowledge | Retrieval | none | none | **PARTIAL (library only).** No component in the three products. Inventory search: "retriev" occurs only in tracing (184 "log retriever traces") and RAG evaluation. Web searches: "LangChain docs retrievers retrieval RAG LangGraph agentic retrieval"; "LangSmith knowledge base document loaders vector store retriever tool agent grounding". Found: LangChain's retriever interface, "an interface that returns documents given an unstructured query" (https://docs.langchain.com/oss/python/langchain/retrieval, https://docs.langchain.com/oss/python/integrations/retrievers) and a LangGraph RAG tutorial that wraps a retriever as a tool (https://docs.langchain.com/oss/python/langgraph/agentic-rag). This is code the developer assembles, not a platform service over named sources. No hosted knowledge base was found. |
| Knowledge | Artifacts | 163s | none | **PARTIAL.** Inventory search: "artifact" does not occur; "file" occurs in sandbox entries and 184 (upload files with traces). Web searches: "LangSmith artifacts files agent outputs storage Deep Agents filesystem backend"; "LangSmith attachments upload files with traces store agent generated files versions". Found: Deep Agents filesystem backends, where the Context Hub backend stores files as Hub commits with version history (https://docs.langchain.com/oss/python/deepagents/backends); sandbox `download_files()` for "generated code, build outputs, reports" (https://docs.langchain.com/oss/python/deepagents/sandboxes); trace attachments (https://docs.langchain.com/langsmith/upload-files-with-traces). No store for work products as such. |
| Capabilities | Models | 156, 259, 260, 261, 263, 264, 294 | 258 | FOUND. LLM Gateway (beta) and model configurations. |
| Capabilities | Tools | 30s, 270 | 269 | FOUND, thin. ToolNode and the Tool Server; tool integrations live in LangChain, outside scope. |
| Capabilities | Registry | 92, 153s, 157s, 274s | 82, 152, 269 | **PARTIAL.** Definitions: assistants (92) and Context Hub (157). Inventory of agents: Agent Registry (274, Cloud only). The **directory of responsibilities is ABSENT.** Searches: "LangGraph multi-agent handoffs router agent discovery which agent to call"; Agent Registry page read in full (https://docs.langchain.com/langsmith/agent-registry). Nearest: subagent discovery "via system prompt (listing available agents) or through progressive disclosure", with a `list_agents` tool for "Large or dynamic agent registries" (https://docs.langchain.com/oss/python/langchain/multi-agent/subagents). That is a list of agents, not of responsibilities. |
| Interaction | Messaging | 105s, 107 | 70, 82 | FOUND, server only. A2A endpoint; MCP endpoint. |
| Interaction | Orchestration | 28, 29, 31, 32, 33s, 37, 38, 39, 40, 41, 44, 61s, 62s, 63s, 64, 74s | 1, 60, 269, 304 | FOUND. The library's core. |
| Interaction | Human channels | 21s, 22s, 23s, 53s, 56s, 57s, 58s, 81s, 100s, 115s | 24, 106, 250, 269 | **PARTIAL.** Streaming and front-end kits carry results to an application the developer builds; Fleet adds real channels (Slack, Teams, Gmail). Every LangGraph match is strained. |
| Governance | Identity | 277s, 283 | 117, 118, 122, 258, 265, 269, 295 | FOUND, fragmented. Server auth, SSO/SCIM for people, Gateway auth, and Fleet agent identity ("Fixed credentials" or "User credentials", https://docs.langchain.com/langsmith/fleet/agent-identity) are separate mechanisms. |
| Governance | Secrets | 120s, 164 | 122, 197, 265 | FOUND. Sandbox auth proxy, Agent Auth (beta), workspace secrets (Fleet uses them for model and tool keys, https://docs.langchain.com/langsmith/fleet/setup). Searched: "LangSmith workspace secrets agent identity Fleet". |
| Governance | Policy | 128s, 166s, 240, 267 | 117, 118, 258, 295 | **PARTIAL.** Rules exist per surface (Gateway policies on model calls, evaluator spend caps, sandbox permissions, RBAC/ABAC on people, authorization handlers on server resources). No policy point over an agent's tool calls was found besides per-tool approval mode. |
| Governance | Approvals | 25, 101 | 1, 24, 106, 269 | FOUND. Interrupt-based human-in-the-loop; Fleet per-tool "Auto" or "Ask". |
| Operations | Observability | 39 components | 197, 221, 258 | FOUND. The deepest and most cross-cutting part of the platform. |
| Operations | Evaluation | 37 components | 221, 250 | FOUND. Offline and online, human and automated. No explicit "unknown" verdict when a check cannot run was found. |
| Operations | Releases | 49s, 75, 77, 83, 84s, 85s, 116s, 135, 136, 138, 139, 159s, 275s, 276s | 46, 51, 68, 152, 305 | FOUND. Rollback exists for prompts ("Rollback history" per environment) and assistants (`setLatest`), and the changelog mentions deployment rollbacks (https://docs.langchain.com/langsmith/manage-prompts, https://docs.langchain.com/langsmith/assistants, https://docs.langchain.com/langsmith/changelog). Searched: "LangSmith deployment rollback previous revision". Self-hosted "Downgrades are not officially supported" (https://docs.langchain.com/langsmith/self-host-upgrades). |
| Operations | Reliability | 147s, 149s, 213s | 68 | **PARTIAL.** Built into the server, not offered as a service: "any runs that were in progress will be picked up by an internal sweeper task" and "exactly-once semantics enforced through Postgres's MVCC model" (https://docs.langchain.com/langsmith/scalability-and-resilience). Disaster recovery is a self-hosted setup topic (entry 281). No component restores the agents' services as a whole. |

No service is ABSENT across the whole vendor documentation. Retrieval is absent from the three inventoried products and present only as library code. The directory, which WARM puts inside Registry, is absent.

## MISFIT list

| # | Component | Class | Quote and URL |
|---|---|---|---|
| 12 | Checkpoint encryption | Data protection | "Checkpointers can optionally encrypt all persisted state" (https://docs.langchain.com/oss/python/langgraph/checkpointers) |
| 124 | Encryption at rest | Data protection | "Use built-in AES encryption unless you need per-tenant keys or an external key management system." (https://docs.langchain.com/langsmith/encryption) |
| 196 | Prevent logging of sensitive data | Data protection | "LangSmith provides multiple approaches to protect your data before it's sent to the backend" (https://docs.langchain.com/langsmith/mask-inputs-outputs) |
| 198 | OpenTelemetry Gateway redaction | Data protection | "Use an OpenTelemetry collector to redact sensitive data" (https://docs.langchain.com/langsmith/otel-gateway-trace-redaction) |
| 90 | TTLs | Data retention | "configure Time-to-Live (TTL) policies in `langgraph.json` to manage the lifecycle of this data automatically" (https://docs.langchain.com/langsmith/configure-ttl) |
| 186 | Usage and billing (retention tiers, limits) | Data retention; vendor commercial terms | "two tiers of traces based on Data Retention": Base "14 days", Extended "180 days" (https://docs.langchain.com/langsmith/usage-and-billing) |
| 300 | Data and compliance | Data retention and purging | Data purging and shared-responsibility pages (https://docs.langchain.com/langsmith/data-purging-compliance, https://docs.langchain.com/langsmith/shared-responsibility-model) |
| 288 | Organizations, workspaces, workload isolation | Tenancy | "LangSmith uses a hierarchical structure to organize your work: organizations, workspaces, agents or applications, and resources." (https://docs.langchain.com/langsmith/workload-isolation) |
| 103 | Webhooks (Agent Server) | Outbound event notification | "Webhooks enable event-driven communication from your LangSmith application to external services." (https://docs.langchain.com/langsmith/use-webhooks) |
| 158 | Context Hub commit webhooks | Outbound event notification | "notify external services whenever an agent or skill commit is created" (https://docs.langchain.com/langsmith/context-hub-webhooks) |
| 222 | Webhook notifications for rules | Outbound event notification | "LangSmith makes a POST request to your webhook endpoint any time the rules you defined match" (https://docs.langchain.com/langsmith/webhooks) |
| 43 | Node caching | Result caching | "LangGraph can cache node (and task) results by input." (https://docs.langchain.com/oss/python/langgraph/graph-api) |
| 121 | Server-side caching | Result caching | "store those results server-side so subsequent runs read from memory instead of making redundant network calls" (https://docs.langchain.com/langsmith/caching) |
| 151 | Licensing and telemetry | Vendor commercial control | "Agent Server is automatically configured to perform license key validation." and "to report telemetry metadata for billing purposes" (https://docs.langchain.com/langsmith/data-plane) |
| 214 | Insights | Criteria-free analysis | "automatically analyzes your traces to detect usage patterns, common agent behaviors, and failure modes" (https://docs.langchain.com/langsmith/insights) |
| 271 | LangSmith Engine | Vendor-supplied improvement agent | "it surfaces recurring issues, diagnoses their root cause, and proposes fixes"; "Apply the proposed fix by opening a pull request" (https://docs.langchain.com/langsmith/engine) |
| 236 | Smithtune | Model adaptation from evidence | "fine-tuning models on trajectories recorded in LangSmith" (https://docs.langchain.com/langsmith/smithtune) |

Why each is a misfit and not a strained fit:

- **Data protection.** WARM's Secrets holds credentials; it does not encrypt agent state or mask content in records. WARM names Security as a concern that is not a group, so this is the predicted gap, but four components need a home and none exists.
- **Data retention.** Step 0 says the platform keeps records "for as long as the retention policy says", but no service holds that policy or deletes anything. Sessions keep, Observability collects, nothing expires.
- **Tenancy.** WARM describes one system. A vendor platform serves many organizations, each with workspaces, and isolation between them is a mechanism every resource depends on.
- **Outbound event notification.** Scheduling starts work on an event; no service emits events for others. Messaging is between agents; a webhook goes to any system.
- **Result caching.** A cache changes whether work runs at all. Tasks tracks runs; it does not skip them.
- **Vendor commercial control.** WARM assumes the platform belongs to the implementer. Here part of the platform answers to its supplier (license checks, billing telemetry, retention by price tier).
- **Insights.** Evaluation assesses "against stated criteria". Insights finds categories nobody stated. Observability "collects evidence"; Insights interprets it.
- **Engine.** It applies judgment, so by WARM's own test (Step 4) it is domain work. Yet it is a product feature of the platform, serves every customer's agents, and reaches into a code repository. WARM's provisional "platform agent" covers an agent that provides a service; Engine provides no WARM service.
- **Smithtune.** WARM's Models mediates and chooses. Training a model from the platform's own evidence is a change path WARM does not have.

## SPANS list

| # | Component | Services | Quote and URL |
|---|---|---|---|
| 1 | LangGraph overview | Tasks, Sessions, Orchestration, Approvals | "orchestration capabilities such as durable execution, streaming, and human-in-the-loop" (https://docs.langchain.com/oss/python/langgraph/overview) |
| 3 | Persistence | Sessions, Memory | "short-term memory through checkpointers and long-term memory through stores" (https://docs.langchain.com/oss/python/langgraph/persistence) |
| 4 | Checkpointers | Sessions, Tasks | "to enable human-in-the-loop workflows, time travel debugging, fault-tolerant execution, and conversational memory" (https://docs.langchain.com/oss/python/langgraph/checkpointers) |
| 24 | Interrupts | Sessions, Approvals, Human channels | "pause graph execution at specific points and wait for external input" (https://docs.langchain.com/oss/python/langgraph/interrupts) |
| 26 | Time travel | Sessions, Tasks | "Replay: Retry from a prior checkpoint. Fork: Branch from a prior checkpoint" (https://docs.langchain.com/oss/python/langgraph/use-time-travel) |
| 27 | Memory (short and long term) | Sessions, Memory, Harness | Covers thread persistence, cross-thread store, and "trimming, deleting, and summarizing messages" (https://docs.langchain.com/oss/python/langgraph/add-memory) |
| 46 | Graph migrations | Releases, Sessions | "What is safe depends on whether the thread has finished or is paused." (https://docs.langchain.com/oss/python/langgraph/graph-api) |
| 51 | Backward compatibility | Releases, Sessions | "every change you ship is effectively a backward-compatible API change with respect to your existing checkpoints" (https://docs.langchain.com/oss/python/langgraph/backward-compatibility) |
| 59 | Functional API | Tasks, Sessions | "wraps ordinary functions with LangGraph runtime features (persistence, memory, human-in-the-loop, and streaming)" (https://docs.langchain.com/oss/python/langgraph/functional-api) |
| 60 | Pregel runtime | Tasks, Orchestration | "`Pregel` implements LangGraph's runtime, managing the execution" (https://docs.langchain.com/oss/python/langgraph/pregel) |
| 68 | LangSmith Deployment | Tasks, Sessions, Releases, Reliability | "a workflow orchestration runtime purpose-built for agent workloads" (https://docs.langchain.com/langsmith/deployment) |
| 70 | Agent Server | Tasks, Sessions, Memory, Scheduling, Messaging | "Handles execution, state management, and persistence" (https://docs.langchain.com/langsmith/components) |
| 82 | Agent Server API | Registry, Sessions, Tasks, Scheduling, Memory, Messaging | Endpoint groups "Assistants, Threads, ... Thread Runs, Crons, Stateless Runs, Store, A2A, MCP" (https://docs.langchain.com/langsmith/server-api-ref) |
| 102 | Time travel (server) | Sessions, Tasks | "resuming past execution produces a new fork in the history" (https://docs.langchain.com/langsmith/human-in-the-loop-time-travel) |
| 106 | HITL over MCP | Approvals, Human channels | "Agent Server asks the MCP client for the answer with elicitation" (https://docs.langchain.com/langsmith/server-mcp-elicitation) |
| 108 | Double texting | Sessions, Tasks | "users may invoke the graph a second time before the first run has finished" (https://docs.langchain.com/langsmith/double-texting) |
| 110 | Agent Server persistence | Sessions, Memory, Tasks | "Agent Server persists three types of data" (https://docs.langchain.com/langsmith/agent-server) |
| 117 | Authentication and access control | Identity, Policy | "a flexible authentication and authorization system" (https://docs.langchain.com/langsmith/auth) |
| 118 | Custom auth handlers | Identity, Policy | `@auth.authenticate` plus authorization handlers (https://docs.langchain.com/langsmith/custom-auth) |
| 122 | IAM auth for data stores | Identity, Secrets | "use a cloud workload identity to generate short-lived PostgreSQL and Redis credentials" (https://docs.langchain.com/langsmith/configure-iam-auth) |
| 152 | Prompt & Context Hub | Registry, Releases | "store, version, review, and update the non-code parts of your agent so you can change behavior without a full deploy" (https://docs.langchain.com/langsmith/prompt-context-hub) |
| 197 | Redact secrets | Secrets, Observability | "mark individual credentials ... to detect common secret formats before upload" (https://docs.langchain.com/langsmith/redact-secrets) |
| 221 | Automation rules | Observability, Evaluation, Scheduling | "an item type, filter, sampling rate, and action" (https://docs.langchain.com/langsmith/rules) |
| 250 | Annotation queues | Evaluation, Human channels | "give human reviewers a focused workflow for attaching feedback" (https://docs.langchain.com/langsmith/annotation-queues) |
| 258 | LLM Gateway | Models, Identity, Policy, Observability | "authenticates the caller, selects an upstream route, applies governance policies, translates between API formats, and traces the result" (https://docs.langchain.com/langsmith/llm-gateway-how-it-works) |
| 265 | Gateway and provider authentication | Identity, Secrets | Caller auth plus "add provider keys as workspace secrets" (https://docs.langchain.com/langsmith/llm-gateway-provider-authentication) |
| 269 | LangSmith Fleet | Harness, Registry, Tools, Memory, Orchestration, Approvals, Scheduling, Human channels, Identity, Environments | "tools, channels, memory, sub-agents, and approvals" (https://docs.langchain.com/langsmith/fleet/essentials) |
| 295 | RBAC, ABAC, teams, SSO, SCIM | Identity, Policy | "Role-Based Access Control (RBAC) system" (https://docs.langchain.com/langsmith/rbac) |
| 304 | Deep Agents | Harness, Orchestration, Memory, Environments | "planning, a virtual filesystem for context, subagent spawning, and long-term memory" (https://docs.langchain.com/oss/python/deepagents/overview) |
| 305 | Managed Deep Agents | Harness, Sessions, Tasks, Releases | "LangSmith runs the harness and runtime" (https://docs.langchain.com/langsmith/python/managed-deep-agents-overview) |

Most spans are product bundles (68, 70, 258, 269, 304, 305), which WARM's "harness product" section anticipates. The ones that matter for the model are the mechanism-level spans: 4, 24, 26, 46, 51, 108 and 152, where one primitive does the work of two WARM services.

## Groupings compared

**The vendor groups by lifecycle phase, WARM groups by runtime question.** The docs' top level is "Build, Test, Deploy, Monitor" plus "Products and setup" and a "Govern" section (https://docs.langchain.com/llms.txt). The cut against WARM's six groups:

| Vendor group | WARM groups it covers |
|---|---|
| Build (LangGraph) | Runtime (Sessions, Tasks), Interaction (Orchestration, Human channels via streaming), Knowledge (Memory stores), Governance (Approvals via interrupts) |
| Deploy (LangSmith Deployment) | Runtime (Tasks, Sessions, Scheduling, Environments via Sandboxes), Interaction (A2A, MCP), Governance (auth), Capabilities (Prompt and Context Hub as Registry), Operations (Releases) |
| Test | Operations (Evaluation) only. This is the one clean match. |
| Monitor | Operations (Observability, online Evaluation, alerts), plus the misfits Insights and Engine |
| Products and setup | Capabilities (LLM Gateway as Models), a whole harness product (Fleet), Registry (Agent Registry), Infrastructure (hosting) |
| Govern | Tenancy, people's access control, audit logs, network reach. Governance here means governing the organization's use of LangSmith, not governing agent actions. |

Three observations:

1. **Evaluation and Observability are separate tabs (Test and Monitor) joined by online evaluation.** WARM puts them in one group, Operations. The vendor's split follows when you use them (before or after deployment), and online evaluators sit under Monitor. Neither split is wrong; WARM's is by responsibility, the vendor's by phase.
2. **Deploy is a grab bag.** It holds the runtime, the definition store (Context Hub), sandboxes and releases. This is because "Deploy" is the hosted product, and everything the hosted product does lands there.
3. **The library alone covers a narrow middle.**

**Cross-cutting.** Observability is cross-cutting in exactly WARM's sense, and wider: "Agent Server is automatically configured to send traces to LangSmith" (required on Cloud), every LLM Gateway call "becomes a LangSmith trace", and tracing integrations instrument other vendors' harnesses (Claude Code, Codex, CrewAI). Identity and Policy are not one cross-cutting layer. Each surface brings its own: Agent Server auth handlers, LangSmith RBAC and ABAC for people, Gateway authentication and policies for model calls, sandbox permissions, Fleet agent identity. Custom auth "does not apply to isolated usage of the LangGraph open source library" (https://docs.langchain.com/langsmith/custom-auth). Approvals is the exception: one mechanism (interrupts) serves every surface.

**Open-source library versus hosted products.**

| Coverage | Services |
|---|---|
| LangGraph library alone (MIT) | Sessions, Tasks, Orchestration, Approvals; Memory (partial: stores without provenance); Human channels (partial: streaming to an app); Tools (partial: ToolNode). About 4 full and 3 partial of 22. |
| Adding open-source LangChain and Deep Agents (same docs, outside scope) | Harness, Models (provider integrations, not routing), Retrieval (retriever interface), Tools, Artifacts (partial: filesystem backends). About 7 full and 4 partial. |
| Needs the hosted or licensed products (Agent Server is Elastic-2.0 and needs a license key in production) | Scheduling, Messaging, Identity, Secrets, Policy, Environments, Registry, Releases, Reliability, Observability backend, Evaluation backend, and model routing in Models (LLM Gateway). |

So Runtime's core and Interaction's Orchestration are open source, and Governance and Operations are almost entirely hosted. Double texting, crons and auth are explicitly server-only ("Double texting is a feature of LangSmith Deployment. It is not available in the LangGraph open source framework.", https://docs.langchain.com/langsmith/double-texting).

## Resemblances to WARM ideas

**A domain or area of work with roles.** Nothing found. The organizing unit is the agent: "In LangSmith, an agent is also the unit a workspace is organized around." (https://docs.langchain.com/langsmith/agent-registry). Workspaces group agents by organization, not by area of work. Fleet templates come closest: "Templates are pre-configured agents designed for specific use cases. Each template includes ... a *system prompt* ... that defines the agent's behavior, personality, and capabilities." (https://docs.langchain.com/langsmith/fleet/templates). A template is one role, with no area of work around it.

**A directory of who is responsible for what.** Not found. Two partial resemblances:
- Agent Registry: "one place to govern every agent your organization runs, wherever it is hosted", to which "Datasets, evaluators, deployments, traces, and alerts each attach" (https://docs.langchain.com/langsmith/agent-registry). It lists agents, not responsibilities.
- Subagent discovery: "Sub-agents can be discovered via system prompt (listing available agents) or through progressive disclosure"; "System prompt enumeration: Small, static agent lists"; "Tool-based discovery: Large or dynamic agent registries" (https://docs.langchain.com/oss/python/langchain/multi-agent/subagents). This matches WARM's "short form of the directory loaded into every agent" plus "query the Registry", but over agents within one application, and it is left to the developer.

**Persistent agents and short-lived task agents.** Present as mechanisms, not named as two kinds. A Fleet agent persists with long-term memory as "Persistent files in the agent workspace, such as `AGENTS.md`, ... `subagents/*`, and `skills/*`" and its sub-agents are "specialized helpers, each one handling a specific part of the job" (https://docs.langchain.com/langsmith/fleet/essentials). At the server level, threads persist and "if you don't need to persist the runs ... you can create stateless runs" (https://docs.langchain.com/langsmith/stateless-runs). Fleet's "Agent identity" split is about whose credentials an agent uses, "Fixed credentials ("Claws")" or "User credentials ("Assistants")" (https://docs.langchain.com/langsmith/fleet/agent-identity), which is a different axis from lifetime. Note that channels and schedules "require fixed credentials", so unattended work forces an agent identity of its own.

**Conversation versus scheduled or background work.** Present, and the vendor offers both the separated and the mixed form. Background runs: "kick off background runs for your agent. This can be useful for long running jobs." (https://docs.langchain.com/langsmith/background-run). Fleet: "Use schedules when your agent needs to do work proactively, not just in response to a message or event." (https://docs.langchain.com/langsmith/fleet/schedules). But a cron job can either "Create a new thread" each time or be a "Cron job on a thread" via `create_for_thread` (https://docs.langchain.com/langsmith/cron-jobs), which is the in-session pattern WARM's design guidance warns against. Double texting (enqueue, reject, interrupt, rollback) is the platform's answer to the collision WARM describes: a second message arriving while a run holds the thread.

**An improvement loop that turns evaluation into changes.** Present and productized, more than in WARM. LangSmith Engine "surfaces recurring issues, diagnoses their root cause, and proposes fixes"; "Apply the proposed fix by opening a pull request"; "Create ground truth dataset examples from production traces for offline evaluation, so you can verify a fix before it ships"; and "Engine learns from what you do with each issue" (https://docs.langchain.com/langsmith/engine, https://docs.langchain.com/langsmith/engine-issues). The evaluation concepts page describes "an iterative feedback loop" between offline and online evaluation (https://docs.langchain.com/langsmith/evaluation-concepts). Other paths that change the system from evidence: Smithtune (fine-tune on trajectories), Prompt and Context Hub ("change behavior without a full deploy"), and Fleet memory ("Agents remember important information from previous conversations and can update themselves to work better", with "approval before saving to the memories folder" by default).

## What this says about the model

**1. Sessions and Tasks may be one service with two views, or the boundary is in the wrong place.** LangGraph's checkpointer is the session history and the durable-execution log in one structure; the docs list "conversational memory" and "fault-tolerant execution" as uses of the same snapshot (entry 4). WARM even lists "checkpointing" under Tasks and "state" under Sessions. Replay, fork, double texting and graph migration all act on both at once. Either WARM should say that Sessions and Tasks share one store (and state the contract between them), or the split should be "state" versus "lifecycle" rather than "session" versus "task".

**2. The Harness is not where WARM puts the center.** WARM makes the Harness the loop that every agent runs and places it first in Runtime. LangGraph deliberately ships a durable workflow runtime without a loop, and the loop is a library on top (`create_agent`, Deep Agents). The platform's center is Tasks plus Orchestration, and an agent loop is one graph among others, mixed freely with "deterministic steps". WARM's statement that "the Harness loads [the definition]" has no counterpart: the server loads a graph (113). This suggests the Harness is better treated as a component a domain or builder chooses than as the hub of the platform.

**3. WARM lacks a data lifecycle and protection responsibility.** Seven misfits (encryption, masking, redaction, TTLs, retention tiers, purging) have no home. Step 0 already relies on "the retention policy", which no service owns. A candidate: a Governance service such as **Data protection** ("Decide how long each record is kept, protect it at rest and in records, and delete it when policy says"), or extend Secrets' responsibility from credentials to all sensitive content.

**4. WARM lacks tenancy.** The vendor's whole Govern section, its trace containers and its agent registry assume many organizations and workspaces on one platform. WARM models one system with one owner. A hosted platform needs isolation between tenants as a mechanism; at minimum WARM should state the one-owner assumption in its scope.

**5. The improvement loop is a platform feature here, which contradicts WARM's placement.** WARM says improvement is a domain stage that the platform supports with Evaluation and Releases. LangSmith ships Insights (find patterns without criteria), Engine (diagnose and open a pull request) and Smithtune (retrain a model). By WARM's own test, Engine applies judgment and so is domain work, yet it works the same way for every customer's agents, which is WARM's test for a mechanism. Either the test needs a third case (judgment that is domain-independent, about agents in general), or WARM is missing an Operations service between Evaluation and Releases, such as **Improvement** ("turn evidence into proposed changes"). Insights alone suggests Observability's boundary ("collect evidence") is too narrow, or that Evaluation should cover analysis without stated criteria.

**6. Identity and Policy are not one cross-cutting layer in practice.** WARM's Governance group assumes one Identity and one Policy that act on every call "without the cooperation of the agent". Here each product surface carries its own authentication and its own rules, and the open-source library has none. Approvals is the only governance mechanism shared across surfaces, and it works by the agent's cooperation (the graph must call `interrupt`). This does not refute WARM's model, but it shows the model describes a target, not common practice, and that "cross-cutting" for Governance needs an enforcement point that the platform owns (the LLM Gateway is the closest: it enforces policy on model calls without the agent's code).

**7. The Registry carries three things the vendor keeps apart, and the directory is missing entirely.** Assistants and Context Hub hold definitions; Context Hub also holds the skills themselves as versioned repos written by people, where WARM puts skills in Memory with only an index in Registry; Agent Registry is an inventory for governance. Nothing holds responsibilities. Skills that are authored, reviewed and versioned like code behave more like Releases-managed definitions than like learned memory, which questions WARM's "skills are procedural memory" placement.

**8. Missing or thin parts that the platform does not need.** Retrieval is not a platform service anywhere in the three products: it is library code the developer assembles into a tool. This supports reading Retrieval as "a kind of tool" rather than a Knowledge service, or at least shows a large platform does without it. Artifacts is likewise thin: work products live in sandbox filesystems, trace attachments or Hub commits, never in a store for products as such.

**9. Smaller boundary findings.**
- Releases has to know about Sessions: every graph change is "a backward-compatible API change with respect to your existing checkpoints". WARM's Releases contract should name persisted state.
- Interaction has no party for an **application**. Streaming, Generative UI and the SDKs serve an app that embeds the agent; WARM has only agents and people. All ten Human-channels matches were strained for this reason.
- Exposing an agent *as* a tool (MCP endpoint, 105) is the reverse of WARM's Tools; Messaging absorbs it only with strain.
- Outbound events (webhooks) have no service; Scheduling only consumes events.
- Capacity and scaling (147, 133) fit nowhere cleanly; Reliability "keeps services available" but WARM puts capacity nowhere.
- WARM says CI belongs to the Software Factory. LangSmith offers CI/CD for agents (116), preview builds per pull request (138) and environments by stage (275) as platform features. The platform treats "how agents are changed" as a mechanism, which supports making Releases broader than WARM's wording.
- The vendor's word "environment" means a release stage (Production, Staging, Development, Local); WARM's Environments means an isolated place to act. The word "thread" has three meanings in the vendor docs (LangGraph, Agent Server, observability). A mapping guide should flag both.

**What held up.** Evaluation, Observability, Environments, Scheduling, Approvals and Models matched cleanly, with dozens of clear fits and almost no strain. The Governance/Operations split into constrain versus observe matched the vendor's own placement of policies (Gateway) and evaluation (Test, Monitor). The harness-product idea ("a product bundles several services") described Fleet, Deep Agents and the LLM Gateway well.

## Sources searched for this mapping (2026-11-11)

Web searches (docs.langchain.com unless noted): "LangChain docs retrievers retrieval RAG LangGraph agentic retrieval"; "LangSmith knowledge base document loaders vector store retriever tool agent grounding"; "LangSmith artifacts files agent outputs storage Deep Agents filesystem backend"; "LangSmith attachments upload files with traces store agent generated files versions"; "LangMem memory management background memory manager LangGraph long-term memory" (also langchain-ai.github.io); "LangSmith workspace secrets agent identity Fleet"; "LangSmith deployment rollback previous revision"; "LangGraph multi-agent handoffs router agent discovery which agent to call". Pages read directly as Markdown: agent-registry, deployment-revisions, fleet/agent-identity, fleet/schedules, fleet/channels, fleet/essentials, fleet/templates, fleet/skills, scalability-and-resilience, agent-auth, insights, engine, engine-issues, background-run, cron-jobs, stateless-runs, managed-deep-agents-overview, oss/python/langchain/retrieval, oss/python/langchain/multi-agent/subagents.
