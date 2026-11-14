---
title: "Inventory: LangGraph, LangSmith Deployment, and LangSmith"
date: 2026-11-11
type: research-inventory
status: draft
sources: primary only (docs.langchain.com, github.com/langchain-ai, pypi.org and npmjs.com package metadata, langchain.com blog)
---

# Inventory: LangGraph, LangSmith Deployment, and LangSmith

**Date-stamped:** 2026-11-11. Every page was read on 2026-11-11 unless a line says otherwise.

**URL convention.** Paths that start with `/` are on `https://docs.langchain.com` (for example, `/langsmith/agent-server` means `https://docs.langchain.com/langsmith/agent-server`). Each page is also served as Markdown by adding `.md`. Other URLs are written in full.

**Staleness rule.** Anything dated before 2026-05-11 (more than six months before this file) carries the tag **[possibly stale]**.

**Scope.** The three products asked for: LangGraph (open-source library), the hosted product for it (now **LangSmith Deployment**, earlier **LangGraph Platform**, earlier **LangGraph Cloud**), and **LangSmith** (observability and evaluation, which the docs now present as a wider platform). The docs place several other LangChain products in the same navigation (LangChain, Deep Agents, Managed Deep Agents, Fleet, Engine, LLM Gateway, OpenWiki, Deep Agents Code). The ones the docs file under LangSmith are listed in Section 2 because the docs present them as LangSmith components. The open-source ones outside LangGraph are listed briefly in Section 2.D so nothing in the shared navigation is missing.

**How the docs are organized (the structure followed below).** The docs index says: "Documentation for LangSmith, Fleet, and our open source packages." (https://docs.langchain.com/llms.txt). The top-level navigation is an "AGENT DEVELOPMENT LIFECYCLE" with tabs **Build, Test, Deploy, Monitor**, plus "PRODUCTS AND SETUP" with **LangSmith setup, LLM Gateway, No-code agents, Engine, Deep Agents Code** (https://docs.langchain.com/llms.txt). LangGraph sits under Build. LangSmith Deployment sits under Deploy. LangSmith observability sits under Monitor and evaluation under Test.

---

## 1. What it is

### 1.1 Each product's own description

**The docs home page (umbrella statement).** "LangChain provides open source, model-agnostic harnesses for building agents. LangSmith is the framework-agnostic platform for testing, deploying, monitoring, and improving your agents across the agent development lifecycle. You control every layer of your agent system, and keep improving it with what you learn in production." (https://docs.langchain.com/, read 2026-11-11)

**LangGraph (open-source library).** "LangGraph is a low-level orchestration framework and runtime for long-running, stateful agents. You define workflows as graphs of shared state, nodes, and edges, and can mix deterministic steps with LLM-driven steps in the same graph. LangGraph focuses on orchestration capabilities such as durable execution, streaming, and human-in-the-loop. It does not prescribe prompts or agent architecture." (/oss/python/langgraph/overview, read 2026-11-11). The same page: "LangGraph works on its own." and "Docs examples often use LangChain for those integrations, but LangGraph does not require LangChain." The GitHub repository describes itself as "Build resilient agents." (https://github.com/langchain-ai/langgraph, read 2026-11-11, license MIT per GitHub API).

**LangSmith Deployment (hosted or self-hosted server product; formerly LangGraph Platform, formerly LangGraph Cloud).** "**LangSmith Deployment** is a workflow orchestration runtime purpose-built for agent workloads. It provides the managed infrastructure agents need to run reliably in production at scale, supporting the full lifecycle from local development to deployment. Deploy to Cloud, BYOC, or your own infrastructure." (/langsmith/deployment, read 2026-11-11). Its runtime is the **Agent Server** (formerly LangGraph Server): "LangSmith Deployment's **Agent Server** offers an API for creating and managing agent-based applications. It is built on the concept of assistants, which are agents configured for specific tasks, and includes built-in persistence and a task queue." (/langsmith/agent-server, read 2026-11-11)

**LangSmith (observability and evaluation product, now a wider platform).** Observability: "LangSmith Observability provides full visibility into your LLM application: from individual traces to production-wide performance metrics. Traces are the record of what your agents did in production. Use them to debug failures, monitor quality, and build the datasets you evaluate against." (/langsmith/observability, read 2026-11-11). Evaluation: "LangSmith's testing tools help you measure agent quality, iterate on prompts, and debug live in an interactive environment. Evaluation is the core of testing: it scores your agent's outputs against datasets and criteria so you can benchmark versions, catch regressions, and track quality over time." (/langsmith/evaluation, read 2026-11-11). The LangGraph overview positions it this way: "LangSmith is the platform for tracing, evaluation, prompts, and deployment across frameworks." (/oss/python/langgraph/overview)

### 1.2 Which part is which

| Part | Kind | Evidence |
|---|---|---|
| LangGraph library (`langgraph`, `langgraph-checkpoint*`, `langgraph-prebuilt`; JS `@langchain/langgraph`) | Open-source library (MIT) | Repo license MIT (https://github.com/langchain-ai/langgraph); "LangGraph works on its own." (/oss/python/langgraph/overview) |
| LangGraph CLI (`langgraph-cli`) and LangGraph / Deployment SDK (`langgraph-sdk`) | Open-source tools (MIT) that drive the server product | PyPI license metadata MIT for both (https://pypi.org/pypi/langgraph-cli/json, https://pypi.org/pypi/langgraph-sdk/json); SDK page: "(Formerly LangGraph Platform) ... The Deployment SDK (`langgraph-sdk`) provides Python clients for interacting with LangSmith deployments." (/langsmith/smith-deployments-sdk) |
| Agent Server (`langgraph-api`, `langgraph-runtime-inmem`) | Server runtime: vendor-hosted (Cloud) or self-hosted (Hybrid, self-hosted with control plane, standalone). Package license metadata is **Elastic-2.0**, not an OSI license | PyPI `license: Elastic-2.0` for `langgraph-api` and `langgraph-runtime-inmem` (https://pypi.org/pypi/langgraph-api/json); production self-hosting "Requires a license key for production use." (/langsmith/cli) |
| LangSmith Deployment control plane and data plane | Hosted or self-hosted server product | "Pick an environment based on where you want the control plane and data plane (Agent Servers and their databases) to run. All infrastructure types use the same Agent Server runtime." (/langsmith/deployment) |
| LangSmith (observability, evaluation, prompt engineering, plus Engine, Fleet, LLM Gateway, Sandboxes, Insights, Chat) | Observability and evaluation product; Cloud (SaaS), BYOC, or Self-hosted | "LangSmith offers Cloud, Bring Your Own Cloud (BYOC), and Self-hosted options." (/langsmith/platform-setup) |
| LangSmith SDK (`langsmith`, Python and JS) | Open-source client (MIT) | PyPI classifier "License :: OSI Approved :: MIT License" (https://pypi.org/pypi/langsmith/json). The old `langchain-ai/langsmith-sdk` repo says "This repo was archived on Oct 16, 2026. Python SDK moved to langchain-ai/langsmith-python and JS SDK to langchain-ai/langsmith-javascript." (https://github.com/langchain-ai/langsmith-sdk) |

### 1.3 Names over time

| Current name | Earlier names | Evidence and date |
|---|---|---|
| LangSmith Deployment | LangGraph Platform; before that LangGraph Cloud | "LangGraph Cloud, currently in closed beta, is infrastructure for deploying your LangGraph agents..." (https://www.langchain.com/blog/langgraph-cloud, published 2024-06-27) **[possibly stale]**. "expanding our LangGraph deployment options and rebranding our service as LangGraph Platform" (https://www.langchain.com/blog/langgraph-platform-announce, published 2024-10-31) **[possibly stale]**. LangSmith changelog entry under "October 13-17, 2025": "LangGraph Platform is now LangSmith Deployment and LangGraph Studio is now LangSmith Studio. LangSmith now spans three services: Observability, Evaluation, and Deployment. Existing deployments, APIs, workflows, pricing, and contracts are unchanged" (/langsmith/changelog) **[possibly stale]**. LangGraph Platform reached GA in the "May 12-16, 2025" entry (/langsmith/changelog) **[possibly stale]**. |
| Agent Server | LangGraph Server (the 2024 blog: "LangGraph Platform today includes LangGraph Server, LangGraph Studio, plus the CLI and SDK.", https://www.langchain.com/blog/langgraph-platform-announce) | Docs pull request "LangGraph Server --> Agent Server" merged 2025-11-05 (https://github.com/langchain-ai/docs/pull/1252) **[possibly stale]**. The old name survives in code and env vars, for example `LANGGRAPH_CLOUD_LICENSE_KEY` (/langsmith/deploy-standalone-server) and "`server_info` is `None` when the graph is not running on LangGraph Server" (/oss/python/langgraph/graph-api-nodes). |
| LangSmith Studio | LangGraph Studio | Same October 2025 changelog entry (/langsmith/changelog) **[possibly stale]**. |
| LangSmith Fleet | Agent Builder | "Agent Builder is now LangSmith Fleet." (/langsmith/fleet), changelog "March 16-20, 2026" (/langsmith/changelog) **[possibly stale]**. |
| LangSmith Chat | Polly | "**LangSmith Chat** (formerly Polly)" (/langsmith/chat). |
| Workspaces | Tenants | "Workspaces were formerly called Tenants." (found in the LangSmith admin pages; see /langsmith/administration-overview) |
| Prompt & Context Hub (Prompts) | `langchainhub` package (deprecated) | "Previously this functionality lived in the `langchainhub` package which is now deprecated." (/langsmith/manage-prompts-programmatically) |
| Deployment SDK (`langgraph-sdk`) | "LangGraph Platform" SDK | "(Formerly LangGraph Platform)" (/langsmith/smith-deployments-sdk) |

### 1.4 Current versions (checked 2026-11-11)

| Package | Version | Released | Source |
|---|---|---|---|
| `langgraph` (Python) | 1.2.20 | 2026-11-05 | https://pypi.org/project/langgraph/ ; GitHub release `1.2.20` 2026-11-05 (https://github.com/langchain-ai/langgraph/releases) |
| `langgraph-checkpoint` | 4.3.1 | 2026-10-26 | https://pypi.org/project/langgraph-checkpoint/ |
| `langgraph-checkpoint-postgres` | 3.2.0 | 2026-10-14 | https://pypi.org/project/langgraph-checkpoint-postgres/ |
| `langgraph-checkpoint-sqlite` | 3.1.3 | 2026-10-30 | https://pypi.org/project/langgraph-checkpoint-sqlite/ |
| `langgraph-prebuilt` | 1.1.1 | 2026-10-15 | https://pypi.org/project/langgraph-prebuilt/ |
| `langgraph-sdk` | 0.4.14 | 2026-11-06 | https://pypi.org/project/langgraph-sdk/ |
| `langgraph-cli` | 0.4.42 | 2026-11-06 | https://pypi.org/project/langgraph-cli/ |
| `langgraph-api` (Agent Server) | 0.17.1 stable; 0.18.0rc4 release candidate | 2026-11-03 (0.17.1) | https://pypi.org/project/langgraph-api/ ; "Latest version: `0.18.0rc4` ... This minor line is still a release candidate. The last stable release is `0.17.1`." (/langsmith/agent-server-changelog) |
| `langgraph-runtime-inmem` | 0.37.1 | 2026-11-03 | https://pypi.org/project/langgraph-runtime-inmem/ |
| `@langchain/langgraph` (JS) | 1.7.3 | 2026-11-10 | https://www.npmjs.com/package/@langchain/langgraph |
| `@langchain/langgraph-sdk` (JS) | 1.15.0 | 2026-11-07 | https://www.npmjs.com/package/@langchain/langgraph-sdk |
| `@langchain/langgraph-cli` (JS) | 1.7.1 | 2026-11-10 | https://www.npmjs.com/package/@langchain/langgraph-cli |
| `langsmith` (Python SDK) | 0.14.17 | 2026-11-02 | https://pypi.org/project/langsmith/ |
| `langsmith` (JS SDK) | 0.12.0 | 2026-11-10 | https://www.npmjs.com/package/langsmith |
| Self-hosted LangSmith Helm | `langsmith-0.18.0-rc.65` | 2026-11-09 | /langsmith/self-hosted-changelog |

Major-version anchors: LangGraph v1.0.0 is dated "Oct 20, 2025" in the OSS changelog (/oss/python/releases/changelog) **[possibly stale]**; `langgraph` v1.1.0 "Mar 10, 2026" **[possibly stale]**; `langgraph` v1.2.0 "May 12, 2026" **[possibly stale]** (/oss/python/releases/changelog).

### 1.5 Latest documentation change found

- Docs repository `langchain-ai/docs` (license MIT, "Unified LangChain documentation."): latest commit 2026-11-11T19:52:52Z, "oss: document gemini decisions support (#7632)" (https://github.com/langchain-ai/docs/commits/main).
- LangSmith Cloud changelog: newest entry "November 2-9, 2026" (/langsmith/changelog).
- LangSmith Fleet changelog: newest entry "November 2-9, 2026" (/langsmith/fleet/changelog).
- Self-hosted changelog: newest entry "2026-11-09" (/langsmith/self-hosted-changelog).
- OSS (Python) changelog: newest entry "Nov 11, 2026", `langchain` v1.5.0 (/oss/python/releases/changelog).

---

## 2. Components

Format for each entry: **Name.** What it does, with a quote and URL. *Runs:* who runs it. *Depends on:* what it needs. *Status:* release stage as the docs state it. "No stage stated" means the page carries no alpha or beta label; the docs say "smaller features may skip alpha or beta and launch directly as GA" (/langsmith/release-stages), so an unlabeled feature is not proven GA.

Release stage definitions, quoted from /langsmith/release-stages: Alpha is "Design partners only" with "Breaking changes expected; the feature may change significantly or never ship". Beta is "Public or a private group" where "Interface or behavior may still change; GA expected within a few months". GA is "Stable; breaking changes require a deprecation period". For the open-source packages: "APIs marked as `beta` are feature-complete but may undergo minor changes based on user feedback." (/oss/python/versioning)

### 2.A LangGraph (open-source library)

Docs navigation for LangGraph (Python and TypeScript are parallel): Overview; Get started; Capabilities; Patterns; Build with the Graph API; Deployment; Frontend; Advanced (https://docs.langchain.com/_llms/agent-development-lifecycle/build/python.txt and .../type-script.txt). *Runs* for every entry in 2.A is "the developer builds it in code and runs it in their own process" unless stated.

#### Overview and Get started

1. **LangGraph overview.** "Low-level orchestration framework and runtime for long-running, stateful agents" (/oss/python/langgraph/overview). *Runs:* developer, in code. *Depends on:* Python or JavaScript runtime; models and tools the developer supplies ("LangGraph does not require LangChain"). *Status:* v1 line; LangGraph v1 "keeps the core graph APIs and execution model unchanged" (/oss/python/releases/langgraph-v1).
2. **Quickstart.** "This quickstart demonstrates how to build a calculator agent with the LangGraph Graph API." (/oss/python/langgraph/quickstart). *Runs:* developer. *Depends on:* `langgraph`, a model provider. *Status:* no stage stated.

#### Capabilities

3. **Persistence.** "LangGraph's persistence layer gives agents short-term memory through checkpointers and long-term memory through stores." (/oss/python/langgraph/persistence). The page contrasts the two: a checkpointer persists "Graph state snapshots" scoped to "A single thread"; a store persists "Application-defined key-value data" "Across threads". *Runs:* developer. *Depends on:* a checkpointer and optionally a store. *Status:* no stage stated.
4. **Checkpointers.** "A checkpointer saves a snapshot of graph state at each super-step, organized into **threads**. Compile a graph with a checkpointer to enable human-in-the-loop workflows, time travel debugging, fault-tolerant execution, and conversational memory." (/oss/python/langgraph/checkpointers). *Runs:* developer (in OSS); injected by Agent Server when deployed. *Depends on:* a storage backend. *Status:* no stage stated.
5. **Threads (LangGraph).** "A thread is a unique ID or thread identifier assigned to each checkpoint saved by a checkpointer. It contains the accumulated state of a sequence of runs." and "you **must** specify a `thread_id`" (/oss/python/langgraph/checkpointers). *Runs:* developer supplies the ID. *Depends on:* checkpointer. *Status:* no stage stated.
6. **Checkpoints and StateSnapshot.** "The state of a thread at a particular point in time is called a checkpoint. A checkpoint is a snapshot of the graph state saved at each super-step and is represented by a `StateSnapshot` object" (/oss/python/langgraph/checkpointers). *Status:* no stage stated.
7. **Checkpoint namespace.** "Each checkpoint has a `checkpoint_ns` (checkpoint namespace) field that identifies which graph or subgraph it belongs to" (/oss/python/langgraph/checkpointers). *Status:* no stage stated.
8. **Get state / get state history / update state.** "You can edit the graph state using `update_state`. This creates a new checkpoint with the updated values... it does not modify the original checkpoint." (/oss/python/langgraph/checkpointers). *Status:* no stage stated.
9. **Durability modes.** "LangGraph supports three durability modes that let you balance performance and data consistency." The modes are `"exit"`, `"async"`, and `"sync"`; `"sync"`: "LangGraph persists changes synchronously before the next step starts." (/oss/python/langgraph/checkpointers). *Status:* no stage stated.
10. **Checkpointer libraries.** "LangGraph provides several checkpointer implementations, all implemented via standalone, installable libraries." Listed: `langgraph-checkpoint` (base interface and `InMemorySaver`, "LangGraph comes with `langgraph-checkpoint` included"), `langgraph-checkpoint-sqlite` ("Ideal for experimentation and local workflows"), `langgraph-checkpoint-postgres` ("used in LangSmith. Ideal for using in production"), `langgraph-checkpoint-mongodb` (/oss/python/langgraph/checkpointers). More providers: /oss/python/integrations/checkpointers. *Runs:* developer. *Depends on:* SQLite, Postgres, or MongoDB. *Status:* no stage stated.
11. **Serializer (`JsonPlusSerializer`, `SerializerProtocol`).** "When checkpointers save the graph state, they need to serialize the channel values in the state. This is done using serializer objects." (/oss/python/langgraph/checkpointers). *Status:* no stage stated.
12. **Checkpoint encryption (`EncryptedSerializer`).** "Checkpointers can optionally encrypt all persisted state. To enable this, pass an instance of `EncryptedSerializer` to the `serde` argument" (/oss/python/langgraph/checkpointers). *Depends on:* a key the developer supplies. *Status:* no stage stated.
13. **Custom checkpointer contract and conformance suite (`langgraph-checkpoint-conformance`).** The page documents the base contract (`put`, `put_writes`, `get_tuple`, `list`, `delete_thread`) and says "`langgraph-checkpoint-conformance` validates your implementation against the full contract, including delta channel history" (/oss/python/langgraph/checkpointers). *Runs:* developer builds. *Status:* no stage stated.
14. **Stores.** "Stores let agents persist information across threads, including user preferences, accumulated knowledge, and facts that should survive beyond a single conversation." (/oss/python/langgraph/stores). *Runs:* developer (OSS); Agent Server provides a Postgres store when deployed. *Status:* no stage stated.
15. **Store semantic search.** "the store also supports semantic search, allowing you to find memories based on meaning rather than exact matches. To enable this, configure the store with an embedding model" (/oss/python/langgraph/stores). *Depends on:* an embedding model. *Status:* no stage stated.
16. **Fault tolerance: retry policies.** "A retry policy automatically re-runs a failed node attempt based on exception type and backoff settings. Pass `retry_policy=` to `add_node`" (/oss/python/langgraph/fault-tolerance). *Status:* no stage stated.
17. **Fault tolerance: timeouts (run timeout, idle timeout, heartbeats, `NodeTimeoutError`).** "The `timeout=` parameter on `add_node` caps how long a single node attempt may run." Requires `langgraph>=1.2` (/oss/python/langgraph/fault-tolerance). *Status:* no stage stated; new in v1.2 ("May 12, 2026", /oss/python/releases/changelog).
18. **Fault tolerance: error handlers (`NodeError`).** "An error handler runs after a node fails and all retries are exhausted. It receives the current state and can update it or route to a different node using `Command`." Requires `langgraph>=1.2` (/oss/python/langgraph/fault-tolerance). *Status:* no stage stated.
19. **Graph defaults (`set_node_defaults`).** "use `set_node_defaults` to configure graph-w[ide defaults]" for `retry_policy`, `error_handler`, `timeout`, `cache_policy`. Requires `langgraph>=1.2` (/oss/python/langgraph/fault-tolerance). *Status:* no stage stated.
20. **Graceful shutdown (`RunControl`).** "Cooperative shutdown lets you stop an in-flight graph run after the current superstep completes and save a resumable checkpoint." Requires `langgraph>=1.2` (/oss/python/langgraph/fault-tolerance). *Status:* no stage stated.
21. **Event streaming.** "Event streaming is the recommended in-process streaming model for most LangGraph application code. It returns a run stream object that can be consumed in multiple ways at the same time." (/oss/python/langgraph/event-streaming). *Status:* no stage stated.
22. **Stream transformers and `StreamChannel` (incl. built-in `ToolCallTransformer`).** "Event streaming normalizes those events, runs them through stream transformers, and exposes typed projections." (/oss/python/langgraph/event-streaming). *Status:* no stage stated.
23. **Streaming (stream modes).** "This page covers LangGraph's stream-mode API. It exposes graph execution through stream modes such as `updates`, `values`, `messages`, `custom`, `checkpoints`, `tasks`, and `debug`." (/oss/python/langgraph/streaming). Includes a v2 output format ("Stream output format (v2)"). *Status:* no stage stated.
24. **Interrupts.** "Interrupts allow you to pause graph execution at specific points and wait for external input before continuing... When an interrupt is triggered, LangGraph saves the graph state using its persistence layer and waits indefinitely until you resume execution." (/oss/python/langgraph/interrupts). *Depends on:* a checkpointer. *Status:* no stage stated.
25. **Human-in-the-loop (concept).** "Human-in-the-loop (HITL) pauses an agent before a tool call runs so a person can review it. The reviewer approves the call, edits its arguments, rejects it with feedback, or answers in place of the tool." (/oss/python/concepts/human-in-the-loop). *Status:* no stage stated.
26. **Time travel: replay and fork.** "**Replay**: Retry from a prior checkpoint. **Fork**: Branch from a prior checkpoint with modified state to explore an alternative path." (/oss/python/langgraph/use-time-travel). *Depends on:* checkpointer. *Status:* no stage stated.
27. **Memory (short-term and long-term).** "**Short-term** memory (thread-level persistence) enables agents to track multi-turn conversations." and "Use long-term memory to store user-specific or application-specific data across conversations." (/oss/python/langgraph/add-memory). The page also covers trimming, deleting, and summarizing messages. Concept page: /oss/python/concepts/memory. *Status:* no stage stated.
28. **Subgraphs.** "A subgraph is a graph that is used as a node in another graph." Subgraph persistence is per-invocation (default), per-thread, or stateless (/oss/python/langgraph/use-subgraphs). *Status:* no stage stated.

#### Patterns

29. **Workflows and agents.** "This guide reviews common workflow and agent patterns." Sections: prompt chaining, parallelization, routing, orchestrator-worker, evaluator-optimizer, agents (/oss/python/langgraph/workflows-agents). *Status:* no stage stated.
30. **`ToolNode` (prebuilt).** "`ToolNode` is a prebuilt node that executes tools in LangGraph workflows. It handles parallel tool execution, error handling, and state injection automatically." (/oss/python/langgraph/workflows-agents). *Depends on:* `langgraph-prebuilt`. *Status:* no stage stated. Note: the `create_react_agent` prebuilt "has been deprecated in favor of LangChain's `create_agent`" (/oss/python/releases/langgraph-v1).

#### Build with the Graph API

31. **Graph API.** "The Graph API defines agent workflows as a graph of state, nodes, and edges. `Send` and `Command` control how the graph runs work" (/oss/python/langgraph/graph-api). Guide pages: "Thinking in the Graph API" (/oss/python/langgraph/thinking-in-graph-api) and "Build checklist for the Graph API" (/oss/python/langgraph/use-graph-api). *Status:* no stage stated.
32. **`StateGraph` and compiling.** "`StateGraph` is the main graph builder. Parameterize it with your state schema." "Compilation checks the graph structure... It is also where you attach runtime options such as checkpointers and breakpoints. You must compile the graph before you invoke or stream it." (/oss/python/langgraph/graph-api). *Status:* no stage stated.
33. **Super-steps.** "LangGraph runs graphs with message passing, in the style of Google's Pregel system. Execution advances in discrete **super-steps**" (/oss/python/langgraph/graph-api). *Status:* no stage stated.
34. **State (schema, multiple schemas, private state).** "State is the shared schema that nodes read and write." (/oss/python/langgraph/graph-api-state). *Status:* no stage stated.
35. **Reducers (default, custom, `Overwrite`).** "Reducers control how node updates merge into state. Each key has its own reducer. With no reducer, updates overwrite the previous value." (/oss/python/langgraph/graph-api). *Status:* no stage stated.
36. **`MessagesState` and `add_messages`.** "`MessagesState` is a prebuilt state with a single `messages` key that uses `add_messages`." (/oss/python/langgraph/graph-api). *Status:* no stage stated.
37. **Nodes.** "Nodes are sync or async functions that implement a step of the graph." A node can accept `state`, `config`, and `runtime` (/oss/python/langgraph/graph-api). *Status:* no stage stated.
38. **`START` and `END`.** "`START` is the virtual entry that delivers user input into the graph." "`END` marks a terminal edge." (/oss/python/langgraph/graph-api). *Status:* no stage stated.
39. **Edges (normal, conditional, entry point, conditional entry point).** "Edges decide where control goes next" and "Destinations on those edges run in parallel in the next super-step." (/oss/python/langgraph/graph-api). Control-flow guide: /oss/python/langgraph/graph-api-control-flow. *Status:* no stage stated.
40. **`Send`.** "Use `Send` when you need to run the same node once per item, each with its own input, and the number of items is only known at runtime." (/oss/python/langgraph/graph-api; guide /oss/python/langgraph/graph-api-send-command). *Status:* no stage stated.
41. **`Command`.** "Use `Command` when a single step must both update state and choose what runs next." Also used for `resume` after an interrupt (/oss/python/langgraph/graph-api). *Status:* no stage stated.
42. **Configure nodes (runtime configuration, retry, timeouts, error handling, defaults, caching).** "This page covers how to attach runtime configuration, retries, timeouts, error handlers, defaults, and caching when you add a node." (/oss/python/langgraph/graph-api-nodes). *Status:* no stage stated.
43. **Node caching (`CachePolicy`).** "LangGraph can cache node (and task) results by input. Pass a cache when you compile the graph, and attach a `CachePolicy` on the node." (/oss/python/langgraph/graph-api). *Status:* no stage stated.
44. **Runtime context.** "Runtime context passes dependencies into nodes without putting them in graph state (for example, model name or a database handle)." (/oss/python/langgraph/graph-api). *Status:* no stage stated.
45. **Recursion limit.** "The recursion limit caps how many super-steps one run may execute. When the limit is exceeded, LangGraph raises `GraphRecursionError`. Starting in version 1.1.4, the default is 10,007 super-steps." (/oss/python/langgraph/graph-api). *Status:* no stage stated.
46. **Graph migrations.** "You can change a graph's nodes, edges, and state schema even when a checkpointer already stores thread state. What is safe depends on whether the thread has finished or is paused." (/oss/python/langgraph/graph-api). *Status:* no stage stated.
47. **Visualize your graph.** "Render a compiled graph as Mermaid text or a PNG image to inspect topology and debug routing." (/oss/python/langgraph/graph-api-visualize). *Status:* no stage stated.

#### Deployment (as listed inside the LangGraph section)

48. **Run a local server.** "This guide shows you how to run a LangGraph agent locally." Steps: install the LangGraph CLI, create an agent, install dependencies, create `.env`, "Launch Agent server", test in Studio, test the API (/oss/python/langgraph/local-server). *Runs:* developer, locally. *Depends on:* LangGraph CLI, a LangSmith API key. *Status:* no stage stated.
49. **Application structure and `langgraph.json`.** "A LangGraph application consists of one or more graphs, a configuration file (`langgraph.json`), a file that specifies dependencies, and an optional `.env` file that specifies environment variables." (/oss/python/langgraph/application-structure). *Runs:* developer writes it. *Status:* no stage stated.
50. **Test.** "This guide covers some useful patterns you can use when writing unit tests." Sections: testing individual nodes and edges, partial execution (/oss/python/langgraph/test). *Status:* no stage stated.
51. **Backward compatibility.** "Because LangGraph runs the latest deployed graph against state that has been persisted for existing threads, every change you ship is effectively a backward-compatible API change with respect to your existing checkpoints." (/oss/python/langgraph/backward-compatibility). *Status:* no stage stated.
52. **LangSmith Studio (from the LangGraph section).** "**LangSmith Studio** is a free visual interface for developing and testing your LangChain agents from your local machine." (/oss/python/langgraph/studio). Full entry in 2.B. *Status:* no stage stated.
53. **Agent Chat UI.** "Agent Chat UI is a Next.js application that provides a conversational interface for interacting with any LangChain agent. It supports real-time chat, tool visualization, and advanced features like time-travel debugging and state forking." (/oss/python/langgraph/ui; repo https://github.com/langchain-ai/agent-chat-ui). *Runs:* developer deploys. *Depends on:* an Agent Server endpoint. *Status:* no stage stated.
54. **Deployment (from the LangGraph section).** "When you are ready to deploy your LangGraph agent to production, choose a hosting model that fits your stack. **LangSmith Cloud** provides fully managed infrastructure for stateful, long-running agents" (/oss/python/langgraph/deploy). *Status:* no stage stated.
55. **LangSmith Observability (from the LangGraph section).** "Traces are a series of steps that your agent takes to go from input to output. Each of these individual steps is represented by a run." (/oss/python/langgraph/observability). Full entries in 2.C. *Status:* no stage stated.

#### Frontend

56. **Frontend overview.** "Build frontends that visualize LangGraph pipelines in real time." (/oss/python/langgraph/frontend/overview). *Runs:* developer builds (JS packages such as `@langchain/react`). *Status:* no stage stated.
57. **Graph execution cards.** "Graph execution cards make this pipeline visible by rendering a card for each node, showing its status, streaming its content in real time" (/oss/python/langgraph/frontend/graph-execution). *Status:* no stage stated.
58. **Custom stream channels (`useExtension`, `useChannel`).** "A server-side **stream transformer** can inspect or rewrite the protocol as it flows to the client and publish its own structured data on a named **custom channel**." (/oss/python/langgraph/frontend/custom-stream-channels). *Status:* no stage stated.

#### Advanced

59. **Functional API (`@entrypoint`, `@task`).** "The **Functional API** wraps ordinary functions with LangGraph runtime features (persistence, memory, human-in-the-loop, and streaming). Use it when you already have existing code or are using a different framework and want to deploy it on LangSmith without rewriting" (/oss/python/langgraph/functional-api). "The `@entrypoint` decorator creates a workflow from a function." "A **task** is a discrete unit of work". *Status:* no stage stated.
60. **LangGraph runtime (Pregel).** "`Pregel` implements LangGraph's runtime, managing the execution of LangGraph applications." (/oss/python/langgraph/pregel). *Status:* no stage stated.
61. **Actors (`PregelNode`).** "An **actor** is a `PregelNode`. It subscribes to channels, reads data from them, and writes data to them." (/oss/python/langgraph/pregel). *Status:* no stage stated.
62. **Channels (`LastValue`, `Topic`, `BinaryOperatorAggregate`).** "Channels are used to communicate between actors (PregelNodes). Each channel has a value type, an update type, and an update function" (/oss/python/langgraph/pregel). *Status:* no stage stated.
63. **`DeltaChannel`.** "`DeltaChannel` stores only the incremental delta at each step rather than the full accumulate[d value]." (/oss/python/langgraph/pregel). *Status:* "currently in **beta**" and "requires `langgraph>=1.2`" (/oss/python/langgraph/pregel).

#### Other LangGraph packages and reference items

64. **`langgraph-supervisor` package.** "The `langgraph-supervisor` package is no longer actively maintained. Instead use the subagents pattern" (/oss/python/migrate/langgraph-supervisor). *Status:* no longer actively maintained.
65. **Versioning and release policy.** "Our OSS version numbers follow the format: `MAJOR.MINOR.PATCH`, as defined by Semantic Versioning." (/oss/python/versioning); "This page explains the LangChain and LangGraph release policies." (/oss/python/release-policy). *Status:* n/a.
66. **Changelog (OSS).** "Log of updates and improvements to our Python packages" (/oss/python/releases/changelog). *Status:* n/a.
67. **Errors reference.** Listed in navigation as "Errors" (/oss/python/common-errors). *Status:* n/a.

### 2.B LangSmith Deployment (hosted or self-hosted server product)

Docs navigation under the Deploy tab: Get started (LangSmith Deployment, Deploy your app to cloud, Deployment components, Develop and test, Frameworks and platforms, Reference); Agent Server (Develop your application, Capabilities, How to build, Auth and access control, Server customization); Deploy to Cloud; Deploy to Self-hosted; Prompt and Context Hub; Sandboxes (https://docs.langchain.com/_llms/agent-development-lifecycle/deploy.txt). The docs list seven "Deployment components": "Agent Server, LangGraph CLI, Studio, SDKs, RemoteGraph, control plane, and data plane" (/langsmith/components).

#### Get started and deployment components

68. **LangSmith Deployment.** "a workflow orchestration runtime purpose-built for agent workloads" that is "framework-agnostic" (/langsmith/deployment). *Runs:* vendor (Cloud) or developer (self-hosted). *Depends on:* LangSmith account; Cloud "Requires a Plus plan or above" (/langsmith/deployment). *Status:* GA per changelog "May 12-16, 2025" **[possibly stale]** (/langsmith/changelog).
69. **Deploy your app to cloud (quickstart).** "Deploy your first application to LangSmith Cloud in GCP using the LangGraph CLI." (/langsmith/deployment-quickstart). *Status:* "The `langgraph deploy` command is in **beta**" (/langsmith/deployment-quickstart).
70. **Agent Server.** "Defines an opinionated API and runtime for deploying graphs and agents. Handles execution, state management, and persistence so you can focus on building logic rather than server infrastructure." (/langsmith/components). *Runs:* vendor (Cloud) or developer (Hybrid, self-hosted, standalone). *Depends on:* PostgreSQL, Redis, the developer's graph(s). *Status:* no stage stated; releases follow `latest`, `rc`, `stable` streams (/langsmith/agent-server-changelog).
71. **LangGraph CLI.** "A command-line interface to build, package, and interact with graphs locally and prepare them for deployment." (/langsmith/components). Commands `langgraph dev`, `build`, `deploy`, `dockerfile`, `up` (/langsmith/cli). *Runs:* developer. *Depends on:* Python or Node; Docker for `build` and `up`. *Status:* no stage stated, except `langgraph deploy` is beta (/langsmith/deploy-to-cloud).
72. **Studio (LangSmith Studio).** "A specialized IDE for visualization, interaction, and debugging. Connects to a local Agent Server for developing and testing your graph." (/langsmith/components). *Runs:* vendor-hosted web UI connecting to the developer's server. *Depends on:* LangSmith, Agent Server, LangGraph CLI ("Prerequisites", /langsmith/studio). *Status:* no stage stated.
73. **Python/JS SDK (Deployment SDK, `langgraph-sdk`).** "The Python/JS SDK provides a programmatic way to interact with deployed graphs and agents from your applications." (/langsmith/components); "It includes clients for managing assistants, threads, runs, and cron jobs, as well as authentication utilities." (/langsmith/smith-deployments-sdk). *Runs:* developer, in client code. *Status:* no stage stated.
74. **RemoteGraph.** "Allows you to interact with a deployed graph as though it were running locally." (/langsmith/components); "It provides API parity with `CompiledGraph`" (/langsmith/use-remote-graph). *Runs:* developer, in client code. *Depends on:* a deployment URL. *Status:* no stage stated.
75. **Control plane.** "The UI and APIs for creating, updating, and managing Agent Server deployments." (/langsmith/components). *Runs:* vendor (Cloud, Hybrid) or developer (self-hosted with control plane). *Status:* no stage stated.
76. **Data plane.** "The runtime layer that executes your graphs, including Agent Servers, their backing services (PostgreSQL, Redis, etc.), and the listener that reconciles state from the control plane." (/langsmith/components). *Runs:* vendor (Cloud) or developer (Hybrid, self-hosted, standalone). *Status:* no stage stated.
77. **Listener application.** "The data plane listener application periodically calls control plane APIs to: Determine if new deployments should be created... updated... deleted." (/langsmith/data-plane). *Runs:* in the data plane. *Status:* no stage stated.
78. **Local development and testing (`langgraph dev`, `langgraph up`).** "`langgraph dev`: A lightweight development server for rapid iteration. `langgraph up`: A production-like testing environment for validation." `dev` keeps state "In-memory & pickled to local directory"; `up` uses "PostgreSQL" (/langsmith/local-dev-testing). *Runs:* developer, locally. *Status:* no stage stated.

#### Frameworks and platforms

79. **Deploy Google ADK agents (`deployments-wrap-sdk`).** "Deploy Google Agent Development Kit (ADK) agents to LangSmith Agent Server using the deployments-wrap-sdk package." (/langsmith/deploy-google-adk). *Status:* no stage stated.
80. **Deploy other frameworks.** "This guide is the how-to for deploying agents built outside LangGraph (Claude Agent SDK, Strands, CrewAI, AutoGen, and similar) to LangSmith Deployment... It walks through wrapping those agents with the Functional API" (/langsmith/deploy-other-frameworks). *Status:* no stage stated.
81. **Full-stack web apps (Vite, Next.js, SvelteKit, Nuxt, Cloudflare Workers, Deno Deploy).** "Ship a LangChain.js chat app: embed the agent in Next.js, SvelteKit, Nuxt, Cloudflare Workers, or Deno Deploy (no Agent Server required), or pair LangSmith Deployment with a Vite + React UI." (/langsmith/deployment; detail /langsmith/deploy-frameworks-and-platforms). *Runs:* developer on a third-party host, or LangSmith Deployment for the Vite case. *Status:* no stage stated.

#### Reference

82. **Agent Server API.** "The Agent Server API reference is available within each deployment at the `/docs` endpoint" (/langsmith/server-api-ref). Endpoint groups in the navigation: Assistants, Threads, Streaming (Protocol v2 Event Stream (SSE), Protocol v2 Command), Thread Runs, Crons, Stateless Runs, Store, A2A, MCP, System (Server Information, System Metrics, API Documentation, Health Check) (https://docs.langchain.com/_llms/agent-development-lifecycle/deploy/get-started.txt). *Runs:* served by Agent Server. *Status:* no stage stated.
83. **Control Plane API.** "With the control plane API, you can programmatically create, manage, and automate your Agent Server deployments" (/langsmith/api-ref-control-plane). Groups: Integrations (v1, v2, including "Forge" GitHub integrations), Deployments (v2), Listeners (v2), Auth Service (v2), Agent Connections (v2) (deploy/get-started index). *Runs:* vendor or self-hosted control plane. *Status:* no stage stated.
84. **Agent Server changelog and release streams.** "`langgraph-api` maintains three release streams: `latest`... `rc`... `stable`" and "Deployments use the newest `stable` version by default" (/langsmith/agent-server-changelog). *Status:* n/a.

#### Agent Server: develop your application

85. **Application structure (deployment).** "To deploy on LangSmith, an application must consist of one or more graphs, a configuration file (`langgraph.json`), a file that specifies dependencies, and an optional `.env` file" (/langsmith/application-structure). *Runs:* developer writes. *Status:* no stage stated.
86. **Dependency setup (`requirements.txt`, `pyproject.toml`, JavaScript).** Navigation items "How to set up an application with requirements.txt", "...with pyproject.toml", "How to set up a JavaScript application" (/langsmith/setup-app-requirements-txt, /langsmith/setup-pyproject, /langsmith/setup-javascript). *Status:* no stage stated.
87. **Custom Dockerfile.** Navigation item "How to customize the Dockerfile" (/langsmith/custom-docker); CLI `langgraph dockerfile` "Emits a Dockerfile derived from your config for custom builds." (/langsmith/cli). *Status:* no stage stated.
88. **Monorepo support.** Navigation item "Monorepo support" (/langsmith/monorepo-support). *Status:* no stage stated.
89. **Configure checkpointer backend.** "By default, LangSmith stores checkpoints in PostgreSQL alongside other server data. You can switch to MongoDB or provide a custom implementation." (/langsmith/configure-checkpointer). *Status:* no stage stated.
90. **TTLs.** "You can configure Time-to-Live (TTL) policies in `langgraph.json` to manage the lifecycle of this data automatically" (/langsmith/configure-ttl). *Status:* no stage stated.
91. **Semantic search on the deployment store.** "This guide shows you how to enable semantic search on your deployment's cross-thread store" (/langsmith/semantic-search). *Depends on:* an embedding model; pgvector (/langsmith/custom-store). *Status:* no stage stated.

#### Agent Server: capabilities

92. **Assistants.** "*Assistants* are an Agent Server concept that allow you to manage configurations (e.g., prompts, LLM selection, tools) separately from your graph's core logic." (/langsmith/assistants). Versions are managed through the API (/langsmith/assistants; manage: /langsmith/configuration-cloud). *Status:* no stage stated.
93. **Threads (Agent Server).** "Threads work with assistants to enable stateful execution of your deployed graphs." (/langsmith/use-threads). *Status:* no stage stated.
94. **Runs.** "A *run* is an invocation of an assistant." (/langsmith/runs). *Status:* no stage stated.
95. **Background runs.** "This guide covers how to kick off background runs for your agent. This can be useful for long running jobs." (/langsmith/background-run). *Status:* no stage stated.
96. **Multiple assistants on the same thread.** "In LangSmith Deployment, a thread is not explicitly associated with a particular assistant." (/langsmith/same-thread). *Status:* no stage stated.
97. **Stateless runs.** "if you don't need to persist the runs you don't need to use the built-in persistent state and can create stateless runs." (/langsmith/stateless-runs). *Status:* no stage stated.
98. **Cancel a run.** "You can cancel a single run by ID or cancel multiple runs by thread or status." with "interrupt and rollback actions" (/langsmith/cancel-run). *Status:* no stage stated.
99. **Cron jobs.** "There are many situations in which it is useful to run an assistant on a schedule." (/langsmith/cron-jobs). *Status:* no stage stated.
100. **Streaming API.** "The LangGraph SDK lets you stream outputs from the LangSmith Deployment API in multiple modes... Thread streaming also supports resumability: if a connection drops, reconnect with the last event ID to pick up where you left off." (/langsmith/streaming). *Status:* no stage stated.
101. **Human-in-the-loop using server API.** "To review, edit, and approve tool calls in an agent or workflow, use LangGraph's human-in-the-loop features." (/langsmith/add-human-in-the-loop). *Status:* no stage stated.
102. **Time travel using the server API.** "resuming past execution produces a new fork in the history." (/langsmith/human-in-the-loop-time-travel). *Status:* no stage stated.
103. **Webhooks (Agent Server).** "Webhooks enable event-driven communication from your LangSmith application to external services." (/langsmith/use-webhooks). *Status:* no stage stated.
104. **Distributed tracing with Agent Server.** "When you call a deployed Agent Server from another service, you can propagate trace context so that the entire request appears as a single unified trace in LangSmith." (/langsmith/agent-server-distributed-tracing). *Status:* no stage stated.
105. **MCP endpoint in Agent Server.** The page describes MCP as "an open protocol for describing tools and data sources in a model-agnostic format"; the API exposes "MCP Get", "MCP Post", "Terminate Session" "Implemented according to the Streamable HTTP Transport specification" (/langsmith/server-mcp; deploy/get-started index). *Status:* no stage stated.
106. **Human-in-the-loop over MCP (elicitation).** "When an agent exposed through the MCP endpoint calls `interrupt`, Agent Server asks the MCP client for the answer with elicitation. When the client answers, Agent Server resumes the agent." (/langsmith/server-mcp-elicitation). *Status:* no stage stated.
107. **A2A endpoint in Agent Server.** "LangSmith implements A2A support, allowing your agents to communicate with other A2A-compatible agents through a standardized protocol." (/langsmith/server-a2a). *Status:* no stage stated.
108. **Double texting (strategies: enqueue, reject, interrupt, rollback).** "users may invoke the graph a second time before the first run has finished. We call this 'double texting'." "Enqueue is the default double texting (multi-tasking) strategy" and "Double texting is a feature of LangSmith Deployment. It is not available in the LangGraph open source framework." (/langsmith/double-texting; strategy pages /langsmith/interrupt-concurrent, /langsmith/rollback-concurrent, /langsmith/reject-concurrent, /langsmith/enqueue-concurrent). *Status:* no stage stated.
109. **Task queue.** "When a client creates a run, the API server enqueues it and a queue worker picks it up for execution." and "Redis handles the signaling, cancellation, and streaming pub/sub between API servers and queue workers." (/langsmith/agent-server). *Runs:* inside Agent Server. *Status:* no stage stated.
110. **Agent Server persistence (core resource data, checkpoints, store).** "Agent Server persists three types of data, all backed by PostgreSQL by default" (/langsmith/agent-server). *Status:* no stage stated.
111. **Deployment modes (single host, split API and queue, distributed runtime).** "Agent Server supports three runtime configurations" (/langsmith/agent-server). *Status:* no stage stated.
112. **Container architecture (API servers, queue workers).** "**API servers** handle client requests... but do not execute agent code themselves. **Queue workers** are the execution engine." (/langsmith/agent-server). *Status:* no stage stated.
113. **Graph loading (compiled graph or factory function).** "**Compiled graph** (recommended)... **Factory function**: Export an agent factory function that the server invokes each time it needs the graph." (/langsmith/agent-server). *Status:* no stage stated.

#### Agent Server: how to build

114. **Collect user feedback for Agent Server runs.** "When creating a run, include the keys in the `feedback_keys` field of the request body. The response will return a pre-signed URL for each key" (/langsmith/agent-server-feedback). *Status:* no stage stated.
115. **Generative UI.** "Generative user interfaces (Generative UI) allows agents to go beyond text and generate rich user interfaces." (/langsmith/generative-ui-react). *Status:* no stage stated.
116. **CI/CD pipeline example.** "This guide demonstrates how to implement a comprehensive CI/CD pipeline for AI agent applications deployed in LangSmith Deployment." (/langsmith/cicd-pipeline-example). *Status:* no stage stated.

#### Agent Server: auth and access control

117. **Authentication and access control.** "LangSmith provides a flexible authentication and authorization system that can integrate with most authentication schemes." Defaults: on LangSmith it "Uses LangSmith API keys by default"; self-hosted has "No default authentication" (/langsmith/auth). *Status:* no stage stated.
118. **Custom authentication (`@auth.authenticate`, authorization handlers).** "This guide shows you how to add custom authentication to your LangSmith application... It does not apply to isolated usage of the LangGraph open source library in your own custom server." (/langsmith/custom-auth). Tutorial pages: /langsmith/set-up-custom-auth, /langsmith/resource-auth ("Make conversations private"), /langsmith/store-auth ("Isolate store data per user"), /langsmith/add-auth-server ("Connect an authentication provider"). *Runs:* developer writes handlers; server enforces. *Status:* no stage stated.
119. **Document API authentication in OpenAPI.** "This guide shows how to customize the OpenAPI security schema for your LangSmith API documentation." (/langsmith/openapi-security). *Status:* no stage stated.
120. **Agent Auth.** "Enable secure access from agents to any system using OAuth 2.0 credentials with Agent Auth." (/langsmith/agent-auth). *Status:* "Agent Auth is in **beta**" (/langsmith/agent-auth).

#### Agent Server: server customization

121. **Server-side caching.** "The built-in cache lets you store those results server-side so subsequent runs read from memory instead of making redundant network calls." (/langsmith/caching). *Status:* "currently in **beta**" (/langsmith/caching).
122. **IAM authentication for data stores.** "Agent Server can use a cloud workload identity to generate short-lived PostgreSQL and Redis credentials at runtime." (/langsmith/configure-iam-auth). *Status:* no stage stated.
123. **Rebuild graph at runtime (`ServerRuntime`).** "You might need to rebuild your graph with a different configuration for a new run... This guide shows how you can do this using `ServerRuntime`." (/langsmith/graph-rebuild). *Status:* no stage stated.
124. **Encryption at rest (built-in AES, custom handlers).** "Agent Server supports two approaches to application-level encryption at rest. Use built-in AES encryption unless you need per-tenant keys or an external key management system." (/langsmith/encryption; /langsmith/aes-encryption; /langsmith/custom-encryption). *Status:* no stage stated.
125. **Custom store.** "You can replace this with your own BaseStore implementation" (/langsmith/custom-store). *Status:* "Custom stores are in **alpha**." (/langsmith/custom-store).
126. **Custom checkpointer.** "You can replace this with your own BaseCheckpointSaver implementation to use a different storage backend." (/langsmith/custom-checkpointer). *Status:* "Custom checkpointers are in **alpha**." (/langsmith/custom-checkpointer).
127. **Custom routes.** "your server automatically exposes routes for creating runs and threads, interacting with the long-term memory store, managing configurable assistants" and you can add your own (/langsmith/custom-routes). *Status:* no stage stated.
128. **Custom middleware.** "you can add custom middleware to your server to handle concerns like logging request metrics, injecting or checking headers, and enforcing security policies" (/langsmith/custom-middleware). *Status:* no stage stated.
129. **Custom lifespan events.** "Lifespan events let you hook into your server's startup and shutdown sequence" (/langsmith/custom-lifespan). *Status:* no stage stated.
130. **HTTP headers for runtime configuration.** "you can pass this configuration in the request body (`config`) or specific request headers." (/langsmith/configurable-headers). *Status:* no stage stated.
131. **HTTP headers in server logs.** "By default, the Agent Server omits HTTP headers from server logs for privacy reasons." Opt in through `logging_headers` (/langsmith/configurable-logs). *Status:* no stage stated.

#### Deploy to Cloud

132. **Deploy to Cloud (LangSmith Cloud for agents).** "LangChain hosts and operates the control plane, data plane, Agent Server runtime, and supporting databases on AWS, Azure, and GCP." (/langsmith/deploy-to-cloud-overview). *Runs:* vendor. *Depends on:* GitHub repository, Plus plan or above. *Status:* no stage stated.
133. **Deployment types: Serverless and Dedicated; sizes Small, Medium, Large.** "**Serverless**: Scales to zero when idle." "**Dedicated**: Stays on and autoscales across replicas." (/langsmith/deploy-to-cloud-overview); "Each is available in three sizes: Small, Medium, and Large." (/langsmith/cloud-platform-features). *Status:* no stage stated.
134. **Cloud platform features (data region, static IPs, payload size, database provisioning, scaling).** "Cloud-only platform features for LangSmith Deployment, including data regions, static IP addresses, payload limits, and deployment types" (/langsmith/cloud-platform-features). *Status:* no stage stated.
135. **Create a deployment.** "Create a LangSmith Cloud deployment from the LangSmith UI or LangGraph CLI." (/langsmith/deploy-to-cloud). *Status:* `langgraph deploy` is beta (/langsmith/deploy-to-cloud).
136. **Revisions.** "A revision deploys a version of your application to an existing Cloud deployment." (/langsmith/deployment-revisions). *Status:* no stage stated.
137. **Monitor a deployment.** "Monitor a Cloud deployment with build logs, Agent Server logs, and runtime metrics." (/langsmith/monitor-deployment). *Status:* no stage stated.
138. **Preview builds.** "Preview builds create temporary **preview deployments** for pull requests." (/langsmith/preview-builds). *Status:* "Preview builds are in public beta and are available only on LangSmith Cloud for deployments created through the GitHub integration." (/langsmith/preview-builds).
139. **Manage a deployment.** "Configure the repository, branch, and automatic updates for a LangSmith Cloud deployment, or delete it." (/langsmith/manage-deployment). *Status:* no stage stated.
140. **Cloud Agent Server environment variables.** "Environment variables supported by the LangSmith Agent Server when deployed on Cloud." (/langsmith/env-var-cloud). *Status:* n/a.

#### Deploy to Self-hosted

141. **Deploy to self-hosted (overview).** "Run the LangSmith Deployment platform on your own infrastructure with full control over data, networking, and resources." (/langsmith/deploy-to-self-hosted-overview). *Runs:* developer. *Status:* no stage stated.
142. **Self-hosted with control plane.** "With a control plane, you build Docker images locally, push them to a registry that your Kubernetes cluster has access to, and deploy them" (/langsmith/deploy-with-control-plane). *Depends on:* self-hosted LangSmith, Kubernetes, "the Enterprise plan with LangSmith Deployment enabled" (/langsmith/deployment). *Status:* no stage stated.
143. **Hybrid.** "A LangSmith Deployment setup where you self-host Agent Servers in your infrastructure and send traces to LangSmith Cloud or a self-hosted LangSmith instance." (/langsmith/hybrid). A legacy variant exists: "Legacy hybrid deployment model with a LangChain-managed control plane and a self-managed data plane" (/langsmith/hybrid-legacy). *Runs:* vendor control plane, developer data plane. *Status:* no stage stated; one variant labeled "legacy".
144. **Standalone servers.** "Deploy standalone Agent Servers using Docker, Docker Compose, or Kubernetes without the LangSmith control plane." (/langsmith/deploy-standalone-server). *Depends on:* "Bring your own PostgreSQL, Redis, and LangSmith license" (/langsmith/deployment). *Status:* no stage stated.
145. **Self-hosted platform features (custom databases, listeners, resource customization).** (/langsmith/self-hosted-platform-features). *Status:* no stage stated.
146. **Agent Server metrics (OpenTelemetry).** "Reference for Agent Server OpenTelemetry metrics on self-hosted deployments" (/langsmith/self-hosted-agent-server-metrics). *Status:* no stage stated.
147. **Configure Agent Server for scale.** The navigation description begins "Tune the Agent Server for self-hosted deployments" and covers write load, read load, and example Helm configurations (/langsmith/agent-server-scale). *Status:* no stage stated.
148. **Restricted-network build machine.** "Configure pip, uv, Python, and the LangGraph CLI to pull every package, interpreter, and image from an..." internal source (/langsmith/self-host-restricted-network-build). *Status:* no stage stated.
149. **Troubleshooting for self-hosted deployments.** "Diagnostic steps for troubleshooting self-hosted LangSmith Deployment issues before contacting support." (/langsmith/diagnostics-self-hosted). *Status:* n/a.
150. **Self-hosted Agent Server environment variables.** (/langsmith/env-var-self-hosted). *Status:* n/a.
151. **Licensing and telemetry (data plane features).** "Agent Server is automatically configured to perform license key validation." and "Agent Server is automatically configured to report telemetry metadata for billing purposes." (/langsmith/data-plane). *Status:* no stage stated.

#### Prompt & Context Hub (filed under the Deploy tab)

152. **Prompt & Context Hub.** "Use the Prompt & Context Hub to store, version, review, and update the non-code parts of your agent so you can change behavior without a full deploy" (/langsmith/prompt-context-hub). *Runs:* vendor-hosted (LangSmith). *Status:* no stage stated.
153. **Prompts, prompt templates, commits, tags.** "**Prompts** refer to the messages that are passed into the language model. **Prompt templates** allow you to create reusable p[rompts]" (/langsmith/prompt-engineering-concepts). Versioning uses "Commits" and "Tags" (same page). Management pages: /langsmith/create-a-prompt, /langsmith/manage-prompts ("Manage prompt versions, environments, and access controls"), /langsmith/manage-prompts-programmatically, /langsmith/prompt-template-format, /langsmith/use-tools, /langsmith/multimodal-content. *Status:* no stage stated.
154. **Playground.** "The Playground provides an interface for iterating on and testing prompts." (/langsmith/prompt-engineering-concepts). Model providers and prompt settings: /langsmith/playground-model-providers, /langsmith/managing-model-configurations. *Status:* no stage stated.
155. **Prompt canvas ("Write your prompt with AI").** "The prompt canvas makes it easy to edit a prompt with the help of an LLM." (/langsmith/write-prompt-with-ai). *Status:* no stage stated.
156. **Model connections (OpenAI-compliant provider, decision model provider, custom model).** Navigation: "Connect to an OpenAI compliant model provider/proxy", "Connect to a compatible decision model provider", "Connect to a custom model" (/langsmith/custom-openai-compliant-model, /langsmith/compatible-decision-model-provider, /langsmith/custom-endpoint). *Status:* no stage stated.
157. **Context Hub (contexts, skills, agents).** "The **Context Hub** gives your team version-controlled, environment-aware management of the instructions and tools your agents use in production. A *context* is a versioned bundle of agent instructions and tools, either a skill or a full agent" (/langsmith/use-the-context-hub). "A *skill* is a versioned repo in the Context Hub that packages a reusable capability an agent can invoke." (/langsmith/context-engineering-concepts). SDK: /langsmith/manage-contexts-sdk. *Status:* no stage stated.
158. **Context Hub commit webhooks.** "Context Hub commit webhooks notify external services whenever an agent or skill commit is created in your workspace." (/langsmith/context-hub-webhooks). *Status:* no stage stated.
159. **Sync prompts with GitHub (prompt commit webhooks).** "LangSmith provides a collaborative interface to create, test, and iterate on prompts." (/langsmith/prompt-commit). *Status:* no stage stated.

#### Sandboxes (filed under the Deploy tab)

160. **LangSmith Sandboxes.** "Sandboxes are isolated environments that allow agents to safely execute potentially risky operations, like running arbitrary code or interacting with the filesystem, without affecting your main infrastructure." (/langsmith/sandboxes). *Runs:* vendor (Cloud) or developer (self-hosted, which uses microVMs per /langsmith/self-host-sandbox-architecture). *Status:* "Sandboxes are generally available in all LangSmith Cloud regions" (/langsmith/sandboxes).
161. **Sandbox snapshots.** "A **snapshot** is a reusable sandbox filesystem." (/langsmith/sandbox-snapshots). *Status:* no stage stated.
162. **Sandbox service URLs.** "Service URLs let you access an HTTP service running inside a sandbox... without tunnels, port forwarding, or CLI tools." (/langsmith/sandbox-service-urls). *Status:* no stage stated.
163. **Sandbox download links.** "A download link hands one sandbox file to something that cannot carry a LangSmith credential" (/langsmith/sandbox-download-links). *Status:* no stage stated.
164. **Sandbox auth proxy.** "The auth proxy lets sandbox code call external APIs (OpenAI, Anthropic, GitHub, etc.) without hardcoding credentials." (/langsmith/sandbox-auth-proxy). *Status:* no stage stated.
165. **Sandbox mounts.** "Sandbox mounts attach external data sources to a sandbox filesystem when the sandbox is created." (/langsmith/sandbox-mounts). *Status:* no stage stated.
166. **Sandbox access permissions.** "By default, only the creator can run commands, read or write files, open tunnels, or reach service URLs on that sandbox." (/langsmith/sandbox-permissions). *Status:* no stage stated.
167. **Sandbox CLI and SDK.** "The LangSmith CLI includes sandbox commands for creating snapshots, booting sandboxes, running commands, opening interactive shells, and tunneling TCP connections into a sandbox." (/langsmith/sandbox-cli); "The LangSmith SDK provides a programmatic interface to create and interact with sandboxes." (/langsmith/sandbox-sdk). *Status:* no stage stated.
168. **Harbor integrations.** "Use LangSmith to run, trace, compare, and cost agent evaluations from one place, with Harbor as the execution layer." (/langsmith/harbor-integrations). *Status:* no stage stated.

### 2.C LangSmith (observability, evaluation, and the wider platform)

#### Monitor tab: Trace

169. **LangSmith Observability.** Quoted in 1.1 (/langsmith/observability). *Runs:* vendor (Cloud), vendor-operated in customer cloud (BYOC), or developer (Self-hosted). *Status:* no stage stated.
170. **Tracing quickstart.** "LangSmith gives you end-to-end visibility into your agent by capturing *traces*" (/langsmith/observability-quickstart). *Status:* no stage stated.
171. **Runs.** "A *run* represents a single unit of work executed by an agent, such as calling an LLM, formatting a prompt, or retrieving documents... you can think of a run as a span." (/langsmith/observability-concepts). *Status:* n/a (concept).
172. **Traces.** "A *trace* is a collection of runs for a single operation." (/langsmith/observability-concepts). *Status:* n/a.
173. **Threads (LangSmith observability).** "A *thread* is a sequence of traces representing a single multi-turn session." (/langsmith/observability-concepts); configuration: /langsmith/threads. *Status:* n/a.
174. **Trajectories.** "A *trajectory* is a flat, ordered list of messages that shows the path an agent took from start to finish." (/langsmith/observability-concepts). *Status:* n/a.
175. **Trace containers (organization, workspace, agent, environment).** "An organization contains workspaces. Each workspace contains agents, and each agent has environments that separate its traces." (/langsmith/observability-concepts). *Status:* n/a.
176. **Feedback.** "*Feedback* allows you to score an individual run based on certain criteria. Each feedback entry consists of a tag and a score" (/langsmith/observability-concepts). *Status:* n/a.
177. **Tags.** "*Tags* are strings you can attach to runs to categorize, filter, and group them" (/langsmith/observability-concepts). *Status:* n/a.
178. **Metadata.** "*Metadata* is a collection of key-value pairs you can attach to runs." (/langsmith/observability-concepts). *Status:* n/a.
179. **Tracing integrations.** "LangSmith *integrations* provide automatic tracing for popular LLM providers and agent frameworks (the equivalent of auto-instrumentation in general observability)." (/langsmith/observability-concepts). The navigation lists LLM providers (Anthropic, Amazon Bedrock, DeepSeek, Google Gemini, LiteLLM, Mistral, OpenAI, OpenAI-compatible), agent frameworks (AutoGen, Claude Agent SDK, Claude Managed Agents, CrewAI, Deep Agents, Google ADK, LangChain, LangGraph, Mastra, Microsoft Agent Framework, OpenAI Agents SDK, OpenTelemetry, PydanticAI, Semantic Kernel, Strands, Vercel AI SDK), voice frameworks (OpenAI Realtime, Gemini Live, LiveKit, Pipecat), developer tools (Claude Code, OpenAI Codex, OpenCode, Cursor, Pi, Instructor, n8n, Temporal, VS Code Copilot Chat), and productivity (Claude Cowork) (https://docs.langchain.com/_llms/agent-development-lifecycle/monitor.txt). *Status:* OpenAI Realtime and Gemini Live: "This integration is in beta, so its API may change." (/langsmith/trace-openai-realtime, /langsmith/trace-gemini-live); others no stage stated.
180. **Trace LangGraph agents.** Navigation item "Trace LangGraph agents" (/langsmith/trace-with-langgraph). *Status:* no stage stated.
181. **Trace with OpenTelemetry.** "Configure OpenTelemetry tracing in LangSmith, including LANGSMITH_OTEL_ENABLED and OTEL fanout" (/langsmith/trace-with-opentelemetry). *Status:* no stage stated.
182. **Coding agent metadata contract.** "The metadata schema that standardizes what trace metadata coding agents must emit" (/langsmith/coding-agent-metadata-contract). *Status:* no stage stated.
183. **Manual instrumentation (`@traceable`, `trace`, `RunTree`).** "LangSmith provides three mechanisms: `@traceable` / `traceable`: a decorator to trace any function; `trace` context manager (Python): wrap specific code blocks; `RunTree` API: low-level, explicit tr[acing]" (/langsmith/observability-concepts; /langsmith/annotate-code). *Runs:* developer, in code. *Status:* no stage stated.
184. **Trace with API (REST).** "Learn how to trace LLM applications using the LangSmith REST API directly." (/langsmith/trace-with-api). Related: log LLM calls (/langsmith/log-llm-trace), log retriever traces (/langsmith/log-retriever-trace), metadata parameters reference (/langsmith/ls-metadata-parameters), upload files with traces (/langsmith/upload-files-with-traces). *Status:* no stage stated.
185. **Cost tracking.** "LangSmith automatically records LLM token usage and costs for major providers, and also allows you to submit custom cost data for any additional components." (/langsmith/cost-tracking). *Status:* no stage stated.
186. **Usage and billing (retention tiers, rate limits, usage limits).** "LangSmith has two tiers of traces based on Data Retention": Base "14 days", Extended "180 days" (/langsmith/usage-and-billing). *Status:* n/a.
187. **Log traces to an agent.** "Each trace belongs to an agent and one of its environments within a workspace. Configure the agent identifier and environment in your code or environment variables." (/langsmith/log-traces-to-agent). *Status:* no stage stated.
188. **Replicas.** "Replicas let you send every trace to multiple agent environments or workspaces at the same time." (/langsmith/trace-replicas). *Status:* no stage stated.
189. **Trace without environment variables.** Navigation item (/langsmith/trace-without-env-vars). *Status:* no stage stated.
190. **Conditional tracing.** "This guide shows you how to disable or customize tracing selectively for specific requests." (/langsmith/conditional-tracing). *Status:* no stage stated.
191. **Sampling rate.** "Sampling rates allow you to control what percentage of traces are logged" (/langsmith/sample-traces). *Status:* no stage stated.
192. **Distributed tracing.** "Sometimes, you need to trace a request across multiple services." (/langsmith/distributed-tracing). *Status:* no stage stated.
193. **Access the current run (span).** Navigation item (/langsmith/access-current-span). *Status:* no stage stated.
194. **Serverless JS tracing, multimodal traces, generator functions.** Navigation items "Trace JS functions in serverless environments", "Log multimodal traces", "Trace generator functions" (/langsmith/serverless-environments, /langsmith/log-multimodal-traces, /langsmith/trace-generator-functions). *Status:* no stage stated.
195. **Add metadata and tags to traces.** "LangSmith supports sending arbitrary metadata and tags along with traces." (/langsmith/add-metadata-tags). *Status:* no stage stated.
196. **Prevent logging of sensitive data (masking).** "LangSmith provides multiple approaches to protect your data before it's sent to the backend" (/langsmith/mask-inputs-outputs). *Status:* no stage stated.
197. **Redact secrets (`LangSmithSecret`, SDK anonymizer).** "Use `LangSmithSecret` (Python only) to mark individual credentials, or the SDK's built-in anonymizer to detect common secret formats before upload." (/langsmith/redact-secrets). *Status:* no stage stated.
198. **OpenTelemetry Gateway redaction.** "Use an OpenTelemetry collector to redact sensitive data fro[m traces]" (/langsmith/otel-gateway-trace-redaction). *Status:* no stage stated.
199. **Troubleshooting guides (trace nesting, variable caching).** (/langsmith/nest-traces, /langsmith/troubleshooting-variable-caching). *Status:* n/a.

#### Monitor tab: Debug

200. **View traces (Trajectory view, Details view).** "From a tracing project, use the **Threads**, **Traces**, or **Runs** tabs to change what appears in the table." (/langsmith/view-traces). *Status:* no stage stated.
201. **Filter traces and trace query syntax.** "Find specific threads, traces, and runs in a LangSmith tracing project by writing filter queries in the search bar." (/langsmith/filter-traces; /langsmith/trace-query-syntax; ClickHouse variant /langsmith/filter-traces-in-application). *Status:* the AI search suggestion is "marked Beta" (/langsmith/filter-traces); otherwise no stage stated.
202. **Run input and output preview configuration.** "Customize what appears in the Input and Output columns of the Runs table" (/langsmith/configure-input-output-preview). *Status:* no stage stated.
203. **Manage a trace (share publicly, view server logs).** "You can share a trace publicly, and view the server logs associated with a trace execution." (/langsmith/manage-trace). *Status:* no stage stated.
204. **Query traces using the SDK (`runs.query`).** "The recommended way to query runs... is to use the `runs.query` method in the SDK or the `POST /api/v2/runs/query` endpoint" (/langsmith/export-traces). *Status:* the older `list_runs` and `read_run` "are deprecated" (/langsmith/export-traces).
205. **Resolve an agent environment.** "Resolve an agent environment, experiment, or workspace evaluator traces to the session ID required by query..." (/langsmith/resolve-an-agent). *Status:* no stage stated.
206. **Query threads using the SDK.** "LangSmith automatically groups your runs into *threads*." (/langsmith/query-threads). *Status:* older methods "are deprecated" (/langsmith/query-threads).
207. **LangSmith Remote MCP.** "The LangSmith Remote MCP is a Model Context Protocol (MCP) server hosted by LangSmith." (/langsmith/langsmith-remote-mcp). *Runs:* vendor. *Status:* no stage stated.
208. **LangSmith MCP Server (standalone).** "It lets MCP-compatible clients (for example, AI coding assistants) read conversation history..." (/langsmith/langsmith-mcp-server). *Status:* "**Deprecated** ... use the LangSmith Remote MCP" (/langsmith/langsmith-mcp-server).
209. **Bulk export trace data.** "LangSmith's bulk data export lets you export trace data from a specific project and date range to an S3-compatible bucket in Parquet format" (/langsmith/data-export). Related: destinations, monitoring, importing, BigQuery (/langsmith/data-export-destinations, /langsmith/data-export-monitor, /langsmith/data-export-downstream, /langsmith/big-query-bulk-export). *Status:* no stage stated.
210. **Trajectory view integrations.** "The Trajectory view renders the traces of a thread as a trajectory" (/langsmith/trajectory-view-integrations). *Status:* no stage stated.
211. **Data type reference (run format, feedback format).** (/langsmith/run-data-format, /langsmith/feedback-data-format). *Status:* n/a.

#### Monitor tab: Observe

212. **Dashboards.** "Dashboards give you high-level insights into your trace data, helping you spot trends and monitor the health of your applications." (/langsmith/dashboards). *Status:* no stage stated.
213. **Alerts.** "LangSmith's alerts feature helps identify critical issues" (/langsmith/alerts). *Status:* no stage stated.
214. **Insights.** "Insights automatically analyzes your traces to detect usage patterns, common agent behaviors, and failure modes, so you do not need to review thousands of traces manually." (/langsmith/insights). *Status:* no stage stated.
215. **Custom Apps.** "A custom app is a UI you build that runs inside LangSmith and calls the LangSmith API." (/langsmith/custom-apps). *Status:* no stage stated.
216. **Online evaluators: LLM-as-a-judge.** "Online evaluations provide real-time feedback on your production traces." (/langsmith/online-evaluations-llm-as-judge). *Status:* no stage stated.
217. **Online evaluators: decision model.** "Evaluate production traces in LangSmith with a decision model as the judge" (/langsmith/online-evaluations-decision-models). *Status:* no stage stated.
218. **Online evaluators: multi-turn.** "Multi-turn online evaluators allow you to evaluate entire conversations between a human and an agent" (/langsmith/online-evaluations-multi-turn). *Status:* no stage stated.
219. **LangChain Tuned Evaluators.** "Each evaluator uses a specialized judge trained for a specific evaluation task. LangChain writes, tests, versions, and maintains the prompt and judge model" (/langsmith/tuned-evaluators). *Runs:* vendor. *Status:* "in **beta**" (/langsmith/tuned-evaluators).
220. **Online evaluators: code and composite.** (/langsmith/online-evaluations-code, /langsmith/online-evaluations-composite). *Status:* no stage stated.
221. **Automation rules.** "You define an automation by an **item type**, **filter**, **sampling rate**, and **action**." (/langsmith/rules). *Status:* no stage stated.
222. **Webhook notifications for rules.** "LangSmith makes a POST request to your webhook endpoint any time the rules you defined match any new runs or threads." (/langsmith/webhooks). *Status:* no stage stated.

#### Test tab: Evaluation

223. **LangSmith Evaluation.** Quoted in 1.1 (/langsmith/evaluation). *Runs:* vendor-hosted platform plus developer code (SDK). *Status:* no stage stated.
224. **Offline evaluations.** "Use offline evaluations for **pre-deployment testing**" (benchmarking, regression testing, unit testing, backtesting) (/langsmith/evaluation-concepts). *Status:* n/a.
225. **Online evaluations.** "Use online evaluations for **production monitoring**" (/langsmith/evaluation-concepts). *Status:* n/a.
226. **Datasets and examples.** "A dataset is a *collection of examples* used for evaluating an application. An example is a test input, reference output pair." (/langsmith/evaluation-concepts). Management: /langsmith/manage-datasets, /langsmith/manage-datasets-in-application, /langsmith/manage-datasets-programmatically. *Status:* no stage stated.
227. **Experiments.** "An *experiment* represents the results of evaluating a specific application version on a dataset." (/langsmith/evaluation-concepts). Analysis: /langsmith/analyze-an-experiment, /langsmith/compare-experiment-results, /langsmith/filter-experiments-ui, /langsmith/fetch-perf-metrics-experiment, /langsmith/upload-existing-experiments. *Status:* no stage stated.
228. **Evaluators (workspace-level).** "*Evaluators* are workspace-level resources that score application performance." Techniques: "Human", "Code", "LLM-as-judge", "Decision model", "Pairwise" (/langsmith/evaluation-concepts). *Status:* no stage stated.
229. **Run an evaluation (SDK `evaluate`, OpenTelemetry, REST API).** "This guide shows you how to run an evaluation on an agent using the LangSmith SDK." (/langsmith/evaluate-llm-application; /langsmith/evaluate-with-opentelemetry; /langsmith/run-evals-api-only). *Status:* no stage stated.
230. **Target functions (including intermediate steps, runnables, graphs).** "There are three main pieces need to run an evaluation: 1. A dataset... 2. A target function... 3. Evaluators" (/langsmith/define-target-function; /langsmith/evaluate-on-intermediate-steps; /langsmith/langchain-runnable; /langsmith/evaluate-graph). *Status:* no stage stated.
231. **Multi-turn simulation.** "AI applications with conversational interfaces... operate over multiple interactions with a user, also called conversation *turns*." (/langsmith/multi-turn-simulation). *Status:* no stage stated.
232. **Trajectory evaluations (`agentevals`).** "LangChain's `agentevals` package provides evaluators specifically designed for testing agent trajectories with live models." (/langsmith/trajectory-evals). *Status:* no stage stated.
233. **Scoring methods (multiple scores, categorical vs numerical).** (/langsmith/multiple-scores, /langsmith/metric-type). *Status:* no stage stated.
234. **Experiment configuration (async, repetitions, rate limits, add evaluators to existing experiment, local runs, read local results, retry failed runs).** Navigation group "Experiment configuration" (/langsmith/experiment-configuration and linked pages; several are "Python only"). *Status:* no stage stated.
235. **Multimodal evaluations.** "Learn how to create dataset examples with file attachments and use them in prompts and evaluators" (/langsmith/evaluate-with-attachments). *Status:* no stage stated.
236. **Smithtune.** "Smithtune is a command-line tool for fine-tuning models on trajectories recorded in LangSmith. It trains a model with Fireworks or Baseten and compares the base and tuned models in a LangSmith experiment" (/langsmith/smithtune). *Depends on:* Fireworks or Baseten. *Status:* "Smithtune is in **beta**" (/langsmith/smithtune).
237. **Dataset data types (example format, prebuilt JSON schema types, transformations).** "LangSmith allows you to attach transformations to fields in your dataset's schema" (/langsmith/dataset-transformations; /langsmith/example-data-format; /langsmith/dataset-json-types). *Status:* no stage stated.
238. **Custom output rendering.** (/langsmith/custom-output-rendering). *Status:* "Custom output rendering for annotation queues will be deprecated." (/langsmith/custom-output-rendering).
239. **Manage evaluators (UI and SDK), auto-run on experiments.** "You can attach a single evaluator to multiple trace containers and datasets" (/langsmith/evaluators; /langsmith/manage-evaluators-sdk; /langsmith/bind-evaluator-to-dataset). *Status:* no stage stated.
240. **Evaluator spend limits.** "Cap weekly LLM spend per evaluator to prevent a single evaluator from exceeding your budget." (/langsmith/evaluator-spend). *Status:* no stage stated.
241. **LLM-as-a-judge evaluator (UI and SDK).** "LLM applications can be challenging to evaluate since they often generate conversational text with no single correct answer." (/langsmith/llm-as-judge; /langsmith/llm-as-judge-sdk). *Status:* no stage stated.
242. **Decision model evaluator.** "A decision model evaluator uses a decision model as the judge. Each question you define returns a typed answer" (/langsmith/decision-model-evaluator). *Status:* no stage stated.
243. **Code evaluator (UI and SDK).** "Code evaluators in the LangSmith UI allow you to write custom evaluation logic using Python or TypeScript code directly in the interface." (/langsmith/code-evaluator-ui; /langsmith/code-evaluator-sdk). *Status:* no stage stated.
244. **Composite evaluator.** "*Composite evaluators* are a way to combine multiple evaluator scores into a single score." (/langsmith/composite-evaluators-ui; /langsmith/composite-evaluators-sdk). *Status:* no stage stated.
245. **Summary evaluator.** "Some metrics can only be defined on the entire experiment level... These are called summary evaluators." (/langsmith/summary). *Status:* no stage stated.
246. **Pairwise evaluation.** "you can score the output from multiple experiments against each other." (/langsmith/evaluate-pairwise). *Status:* no stage stated.
247. **openevals and agentevals packages.** "LangSmith integrates with the open-source `openevals` package to provide a suite of evaluation utilities and prompts" (/langsmith/openevals). *Runs:* developer, open source. *Status:* no stage stated.
248. **pytest and Vitest/Jest integrations.** "The LangSmith pytest plugin lets Python developers define their datasets and evaluations as pytest test cases." (/langsmith/pytest; /langsmith/vitest-jest). *Status:* no stage stated.
249. **Improve evaluators (human feedback alignment, few-shot, audit scores).** (/langsmith/improve-judge-evaluator-feedback, /langsmith/create-few-shot-evaluators, /langsmith/audit-evaluator-scores). *Status:* no stage stated.
250. **Annotation queues.** "*Annotation queues* give human reviewers a focused workflow for attaching feedback to specific runs or threads." (/langsmith/annotation-queues; SDK /langsmith/annotation-queues-sdk). *Status:* no stage stated.
251. **Annotation queue custom views.** "Build a custom view with LangSmith Chat to control how runs and threads appear to reviewers in an annotation queue." (/langsmith/annotation-queue-custom-views). *Status:* no stage stated.
252. **Assertions.** "Assertions turn a reviewer's English-language standards into an automated check." (/langsmith/assertions). *Status:* no stage stated.
253. **Feedback criteria and inline annotation.** "Feedback criteria are represented in the application as feedback tags." (/langsmith/set-up-feedback-criteria; /langsmith/annotate-traces-inline). *Status:* no stage stated.
254. **User feedback via SDK and presigned URLs.** "Presigned feedback tokens let you collect feedback from client-side applications... without exposing your LangSmith API key." (/langsmith/attach-user-feedback; /langsmith/presigned-feedback-tokens). *Status:* no stage stated.
255. **Test from the Playground.** "Test a prompt or model configuration over a series of inputs to see how well it scores... without writing any code." (/langsmith/test-from-playground; /langsmith/run-evaluation-from-playground). *Status:* no stage stated.
256. **Studio for testing (graph mode, chat mode).** "Studio is a specialized agent IDE that enables visualization, interaction, and debugging of agentic systems that implement the Agent Server API protocol." Graph mode "exposes the full feature-set"; Chat mode "is a simpler UI for iterating on and testing chat-specific agents" (/langsmith/studio; /langsmith/quick-start-studio; /langsmith/use-studio; /langsmith/observability-studio). *Status:* no stage stated.
257. **Deploy from Studio.** "Go from testing graphs locally in Studio to deploying them on Langsmith Cloud in 1 Click, directly from Studio." (/langsmith/studio). *Status:* no stage stated.

#### Products and setup: LLM Gateway

258. **LLM Gateway.** "The LLM Gateway is the control layer between the agents and applications you run and the model providers your workspace has configured. Because the gateway is part of LangSmith, each call it routes becomes a LangSmith trace" (/langsmith/llm-gateway). "It authenticates the caller, selects an upstream route, applies governance policies, translates between API formats, and traces the result." (/langsmith/llm-gateway-how-it-works). *Runs:* vendor (Cloud) or developer (self-hosted `agent-gateway` service, /langsmith/llm-gateway-self-hosted). *Status:* "The LLM Gateway is in **beta**" (/langsmith/llm-gateway).
259. **Gateway API formats and direct model access.** "Use OpenAI Chat Completions, Anthropic Messages, or OpenAI Responses requests to call models across providers" (/langsmith/llm-gateway-api-formats; /langsmith/llm-gateway-direct-model-access). *Status:* beta.
260. **Gateway for coding agents.** "Configure Claude Code, Codex, Gemini CLI, and Deep Agents Code to route LLM calls through the LLM Gateway." (/langsmith/llm-gateway-coding-agents). *Status:* beta.
261. **Gateway decision models.** "Call TypeSafe and OpenAI decision models through the LangSmith LLM Gateway" (/langsmith/llm-gateway-decision-models). *Status:* beta.
262. **Gateway Credits.** "**Gateway Credits** let you call LangChain-hosted models through the standard LLM Gateway API without setting up a provider account or key." (/langsmith/llm-gateway-credits). *Status:* beta.
263. **Custom model configurations (gateway).** "Call saved model configurations through the LLM Gateway to reach custom endpoints" (/langsmith/llm-gateway-model-configurations). *Status:* beta.
264. **Model fallbacks.** "Model fallbacks in the LLM Gateway allow you to retry a request against one or more backup models when the primary model returns a configured error" (/langsmith/llm-gateway-fallbacks). *Status:* beta.
265. **Gateway authentication and provider authentication.** (/langsmith/llm-gateway-authentication, /langsmith/llm-gateway-provider-authentication). *Status:* beta.
266. **Gateway traces and spend monitoring.** "Find LLM Gateway traces, read their policy and cost metadata, triage policy violations in LangSmith Engine" and "View and analyze LLM Gateway costs by user, API key, model, provider, and request header." (/langsmith/llm-gateway-traces; /langsmith/llm-gateway-monitoring). *Status:* beta.
267. **Governance policies: spend, rate limit, model access, header-based, data.** "A spend policy defines a cost cap for a specific scope (organization, workspace, user, or API key) over a time window" (/langsmith/llm-gateway-spend-policies); "A data policy controls what happens to the content of requests that pass through the LLM Gateway" (/langsmith/llm-gateway-data-policy); also /langsmith/llm-gateway-rate-limit-policies, /langsmith/llm-gateway-model-access-policies, /langsmith/llm-gateway-header-policies. *Status:* beta.

#### Products and setup: No-code agents

268. **Build an agent with LangSmith Studio (no-code).** "LangSmith Studio builds a no-code agent from a description. You describe what the agent should do, LangSmith Chat drafts its configuration, and you review each step before you save." (/langsmith/build-an-agent). *Runs:* vendor. *Status:* no stage stated.
269. **LangSmith Fleet.** "LangSmith Fleet is a no-code platform for creating and managing AI agents. It allows you to create agents from templates, connect your accounts, and let the agent handle routine work while you stay in control." (/langsmith/fleet). Sub-features in its navigation: Quickstart, Essentials ("tools, channels, memory, sub-agents, and approvals", /langsmith/fleet/essentials), Templates, Agent platform comparison, Workspace administration, Agent identity, Agent settings, Computer use ("access to an isolated virtual computer", /langsmith/fleet/computer-use), Tool integrations, Channels, Schedules, Skills, Slack app, Microsoft Teams app, Remote MCP servers, Arcade integration, Salesforce integration, Use Fleet agents in code ("Invoke Fleet agents via the LangGraph SDK or REST API", /langsmith/fleet/code), Fleet webhooks, Auth-aware tool responses, Access and oversight, changelog (products-and-setup index). *Runs:* vendor (Cloud) or developer (self-hosted). *Status:* "Self-hosting for Fleet is available in **beta**" (/langsmith/fleet); Cloud no stage stated.
270. **LangSmith Tool Server.** "The LangSmith Tool Server is a standalone MCP framework for building and deploying tools with built-in authentication and authorization." (/langsmith/fleet/mcp-framework). *Status:* no stage stated.

#### Products and setup: Engine

271. **LangSmith Engine.** "LangSmith Engine is the LangSmith agent for agent engineering. Working from your production traces, it surfaces recurring issues, diagnoses their root cause, and proposes fixes" (/langsmith/engine). Sub-pages: set up, issues ("open pull requests with its proposed fixes, and turn failing traces into dataset examples", /langsmith/engine-issues), repositories, notifications, security, self-hosted and BYOC. *Runs:* vendor (Cloud), or on self-hosted and BYOC (/langsmith/engine-self-hosted). *Depends on:* tracing project; optional GitHub or GitLab repository. *Status:* no stage stated for the core.
272. **Engine fix validation.** "Confirm that a LangSmith Engine issue reproduces on your deployment, and that Engine's fix resolves it, by replaying the issue's traces." (/langsmith/engine-fix-validation). *Status:* "Fix validation is in private beta" (/langsmith/engine-fix-validation).
273. **Engine Red Teaming.** "Red Teaming tests a deployed agent by sending it new, synthetic requests and judging how it responds." (/langsmith/engine-red-teaming). *Status:* "Red Teaming is in private beta" (/langsmith/engine-red-teaming).

#### LangSmith setup: agent-based workspaces

274. **Agent Registry.** "LangSmith Agent Registry offers a centralized location for registering an agent, providing one place to govern every agent your organization runs, wherever it is hosted. Agent Registry is available on LangSmith Cloud." (/langsmith/agent-registry). *Runs:* vendor. *Status:* no stage stated; Cloud only.
275. **Agent environments.** "Every trace an agent records lands in exactly one of its environments, which are drawn from a fixed set of four." The four are Production, Staging, Development, Local; "custom names are not supported" (/langsmith/agent-environments). *Status:* "Agent-based workspaces are available on LangSmith Cloud. They are not available on self-hosted LangSmith." (/langsmith/agent-environments).
276. **Create an agent, navigate agents, deploy to an agent environment.** "Deploying to an agent environment binds a deployment to one agent and one of that agent's environments. Two flags carry the binding, and the LangGraph CLI and the `mda` CLI both accept them." (/langsmith/deploy-to-agent-environment; /langsmith/create-an-agent; /langsmith/navigate-agents). *Status:* no stage stated.

#### LangSmith setup: account, hosting, and operations

277. **Account, API keys, profile configuration.** "Set up your LangSmith account, including API keys, profile configuration, integrations, and pricing tiers." (/langsmith/admin; /langsmith/create-account-api-key; /langsmith/profile-configuration). *Status:* n/a.
278. **Billing and usage (view usage, granular billable usage).** (/langsmith/billing, /langsmith/view-usage, /langsmith/granular-usage). *Status:* n/a.
279. **LangSmith Cloud (SaaS).** "The **Cloud** hosting option is a fully managed model where LangChain hosts and operates all LangSmith infrastructure and services" (/langsmith/cloud). *Runs:* vendor. *Status:* no stage stated.
280. **Bring Your Own Cloud (BYOC).** "Bring Your Own Cloud (BYOC) lets you deploy LangSmith services and store data in your own cloud environment, while LangChain operates, scales, and upgrades the infrastructure." (/langsmith/byoc). Sub-pages per AWS, Azure, GCP (onboarding, architecture, operations, billing, cost estimates, BYO VPC, BYO IAM). *Runs:* vendor operates in the customer's cloud account. *Status:* "BYOC is generally available (GA) on AWS"; "BYOC on GCP and Azure is available in beta" (/langsmith/byoc).
281. **Self-hosted LangSmith.** "Self-hosted LangSmith runs the LangSmith platform in your own infrastructure so that trace and operational data stay in your environment." "Self-hosted LangSmith is an add-on to the Enterprise plan" (/langsmith/self-hosted). Sub-areas: per-cloud guides, Terraform modules, Kubernetes Helm install, additional features (Fleet, LLM Gateway, LangSmith Deployment, Sandboxes), configuration, external services (blob storage, ClickHouse, PostgreSQL, Redis or Valkey, Slack), platform auth (basic auth, SSO, user management, TLS), upgrades, disaster recovery (products-and-setup/lang-smith-setup index). *Runs:* developer. *Status:* base no stage stated; table shows some add-ons "Optional (beta)" (/langsmith/self-hosted).
282. **SmithDB.** "SmithDB is a columnar datastore built for agent trace data: deeply nested spans, multi-modal content, and spans that stay open for hours." (/langsmith/self-host-smithdb). "In May 2026, we released SmithDB" (/langsmith/smithdb-sdk-migration). *Runs:* vendor (Cloud, BYOC) or developer (self-hosted, alongside ClickHouse). *Status:* no stage stated; some features need it, for example "Thread annotation-queue and webhook automations now require SmithDB queries." (changelog "August 10-17, 2026", /langsmith/changelog).
283. **LLM auth proxy (self-hosted).** "Deploy an Envoy-based auth proxy that validates LangSmith-signed JWTs and routes..." (/langsmith/llm-auth-proxy-self-hosted). *Status:* no stage stated.
284. **Mission Control.** "Mission Control is an in-cluster console for monitoring, configuring, and operating LangSmith on Kubernetes." (/langsmith/self-hosted-mission-control). *Runs:* developer, in cluster. *Status:* no stage stated.
285. **Self-hosted observability (telemetry export, collector, dashboards, observability stack).** (/langsmith/export-backend, /langsmith/langsmith-collector, /langsmith/self-host-observability-dashboards, /langsmith/observability-stack). *Status:* "**Deprecated**: The LangSmith Observability Helm chart is deprecated." (/langsmith/observability-stack).
286. **Admin scripts (delete workspaces, organizations, traces; ClickHouse and query stats; support queries).** Navigation group "Scripts" (for example /langsmith/script-delete-traces). *Status:* n/a.
287. **Release stages, deprecation policy, self-hosted release policy.** (/langsmith/release-stages, /langsmith/endpoint-deprecation, /langsmith/release-versions). *Status:* n/a.

#### Govern

288. **Organizations, workspaces, resource hierarchy, workload isolation.** "LangSmith uses a hierarchical structure to organize your work: organizations, workspaces, agents or applications, and resources." (/langsmith/workload-isolation; /langsmith/administration-overview; /langsmith/set-up-hierarchy). *Status:* no stage stated.
289. **Tunnels.** "A tunnel lets LangSmith reach a service that runs on your private network, such as a model endpoint or an MCP server, without opening that service to the internet." (/langsmith/tunnels). *Status:* "Tunnels are in alpha" (/langsmith/tunnels).
290. **Relays.** "A relay sends some of a sandbox's outbound connections through your own network." (/langsmith/relays). *Status:* "Relays are in alpha" (/langsmith/relays).
291. **Manage the organization by API and with Terraform.** "Use the official LangSmith Terraform provider to manage workspaces, access contr[ol]..." (/langsmith/manage-with-terraform; /langsmith/manage-organization-by-api). *Status:* no stage stated.
292. **Agent-based workspaces (migration).** "What changes when a workspace moves from organizing traces by trac[ing projects]..." (/langsmith/migrate-to-agent-based-workspaces). *Status:* Cloud only (/langsmith/agent-environments).
293. **Resource tags.** "Create and manage resource tags to organize projects, datasets, prompts, and other resources" (/langsmith/set-up-resource-tags). *Status:* no stage stated.
294. **Model configurations (workspace library).** "Model configurations define the model and parameters that LangSmith features use when calling an AI provider." (/langsmith/model-configurations). *Status:* no stage stated.
295. **User management: RBAC, ABAC, teams, SSO, SCIM.** "This reference explains LangSmith's Role-Based Access Control (RBAC) system" (/langsmith/rbac); "Attribute-based access control (ABAC) lets organization administrators grant or restrict access to LangSmith resources based on the resources' attributes." (/langsmith/abac); "A team is a group of organization members." (/langsmith/teams); also /langsmith/user-management, /langsmith/authentication-methods, /langsmith/jit-invite-sso. *Status:* no stage stated.
296. **LangSmith Chat.** "**LangSmith Chat** (formerly Polly) is built directly into your LangSmith workspace to help you analyze and understand your application data." (/langsmith/chat). *Runs:* vendor (and self-hosted, "enabled by default", /langsmith/self-hosted). *Status:* no stage stated.
297. **LangSmith CLI.** "The LangSmith CLI is a command-line tool for querying and managing your LangSmith data. It's designed for both developers and AI coding agents" (/langsmith/langsmith-cli). *Runs:* developer. *Status:* no stage stated.
298. **LangSmith skills (Agent Skills).** "This page summarizes the LangSmith-oriented skills you can add to a compatible coding agent to query traces, generate datasets, and define evaluators." (/langsmith/skills). *Status:* no stage stated.
299. **Audit logs.** "LangSmith audit logs provide a tamper-resistant record of administrative and configuration actions taken within your organization." (/langsmith/audit-logs). *Status:* no stage stated.
300. **Data and compliance (shared responsibility, data storage and privacy, data purging, scalability and resilience).** (/langsmith/shared-responsibility-model, /langsmith/data-storage-and-privacy, /langsmith/data-purging-compliance, /langsmith/scalability-and-resilience). *Status:* n/a.
301. **LangSmith SDK (Python and JS).** "The LangSmith SDK provides a programmatic interface to create and interact with sandboxes." is one use (/langsmith/sandbox-sdk); the SDK is also the tracing and evaluation client (`@traceable`, `evaluate`, `runs.query`) (/langsmith/observability-concepts; /langsmith/evaluate-llm-application; /langsmith/export-traces). Repos: https://github.com/langchain-ai/langsmith-python and https://github.com/langchain-ai/langsmith-javascript (per the archived repo's note). *Runs:* developer, in code. *Status:* no stage stated.
302. **LangSmith REST API.** Groups: "System, Tracing, Administration, Datasets, Evaluation, Feedback & Annotation, Monitoring, Prompts & Playground, Integrations & Tools, Prompt Hub, LLM Gateway, Issues, teams, Threads, Sandboxes" (https://docs.langchain.com/llms.txt). *Runs:* vendor or self-hosted LangSmith. *Status:* no stage stated.

### 2.D Other products in the same docs navigation (not part of the requested scope; listed so the shared navigation is complete)

303. **LangChain (`create_agent`, middleware).** "LangChain provides `create_agent`: a minimal, highly configurable harness. The harness is everything around the model loop: the prompt, the tools, and any middleware that shapes behavior." (/oss/python/langchain/overview). "While LangChain is built on top of LangGraph, you don't need to know LangGraph to use LangChain." (/oss/python/concepts/products). *Runs:* developer. *Status:* v1 line; `langchain` 1.5.0 released 2026-11-11 (https://pypi.org/project/langchain/).
304. **Deep Agents (SDK).** "Deep Agents is the agent harness for complex, multi-step work. It adds planning, a virtual filesystem for context, subagent spawning, and long-term memory on top of LangChain and LangGraph." (/oss/python/deepagents/overview). *Runs:* developer. *Status:* `deepagents` 0.7.35 (https://pypi.org/project/deepagents/).
305. **Managed Deep Agents.** "Build your agent as a directory of files while LangSmith runs the harness and runtime." Uses the `mda` CLI (/langsmith/python/managed-deep-agents-overview). *Runs:* vendor (Cloud, BYOC). *Status:* "Managed Deep Agents is in **public beta**" (/langsmith/python/managed-deep-agents-overview).
306. **OpenWiki.** "CLI that writes and maintains agent wikis so coding agents work faster" (/oss/openwiki/overview). *Runs:* developer. *Status:* no stage stated.
307. **Deep Agents Code (`dcode`).** "Terminal coding agent built on the Deep Agents SDK" (/oss/deepagents/code/overview). *Runs:* developer. *Status:* no stage stated.

**Component count:** 307 numbered entries (2.A: 67, 2.B: 101, 2.C: 134, 2.D: 5). Several entries group closely related navigation pages (for example, the four double-texting strategy pages are one entry); the grouping follows the docs' own navigation groups.

---

## 3. What the developer must bring

1. **The agent logic itself (graph, nodes, prompts, architecture).** LangGraph "does not prescribe prompts or agent architecture." (/oss/python/langgraph/overview); "LangGraph provides the runtime primitives for stateful, long-running workflows. It does not abstract prompts or force a fixed agent architecture." (same page).
2. **Models and tools.** "Before you start, learn the building blocks agents use, especially models and tools." and "LangGraph does not require LangChain." (/oss/python/langgraph/overview). Model provider credentials go in `.env` for local runs (/oss/python/langgraph/local-server).
3. **A checkpointer and a `thread_id` (OSS).** "Compile a graph with a checkpointer to enable human-in-the-loop workflows, time travel debugging, fault-tolerant execution, and conversational memory." and "you **must** specify a `thread_id`" (/oss/python/langgraph/checkpointers). On Agent Server the opposite holds: "the server automatically injects the checkpointer and memory store configured for that deployment at runtime. **Do not configure these in your graph code**" (/langsmith/agent-server).
4. **A storage backend for OSS persistence.** Postgres, SQLite, or MongoDB checkpointer libraries "Needs to be installed separately." (/oss/python/langgraph/checkpointers).
5. **An embedding model for semantic search.** "To enable this, configure the store with an embedding model" (/oss/python/langgraph/stores).
6. **Idempotent side effects.** "side effects called before `interrupt` should (ideally) be idempotent." (/oss/python/langgraph/interrupts); retries need an idempotency key: "Protect side effects with an idempotency key" (/oss/python/langgraph/fault-tolerance).
7. **Backward-compatible graph changes.** "every change you ship is effectively a backward-compatible API change with respect to your existing checkpoints." (/oss/python/langgraph/backward-compatibility).
8. **Application structure for deployment.** "an application must consist of one or more graphs, a configuration file (`langgraph.json`), a file that specifies dependencies, and an optional `.env` file" (/langsmith/application-structure).
9. **A LangSmith account and API key.** Local server prerequisite: "An API key for LangSmith" (/oss/python/langgraph/local-server). Cloud deploy prerequisite: "A GitHub account" and "A LangSmith account" (/oss/python/langgraph/deploy).
10. **A GitHub repository (Cloud).** "Your application's code must reside in a GitHub repository to be deployed on LangSmith." (/oss/python/langgraph/deploy).
11. **A paid plan.** Cloud deployments "Requires a Plus plan or above"; self-hosted with control plane "Requires the Enterprise plan with LangSmith Deployment enabled" (/langsmith/deployment); "Self-hosted and BYOC are available on the Enterprise plan." (/langsmith/platform-setup).
12. **Docker (for `langgraph up` and `build`).** "`langgraph up` ... Requires Docker running; LangSmith API key for local dev; license for production." (/langsmith/cli).
13. **For standalone servers: PostgreSQL, Redis, license key, egress.** "Bring your own PostgreSQL, Redis, and LangSmith license; no control plane." (/langsmith/deployment); env vars `REDIS_URI`, `DATABASE_URI`, `LANGSMITH_API_KEY`, `LANGGRAPH_CLOUD_LICENSE_KEY` and "Egress to `https://beacon.langchain.com` from your network. This is required for license verification and usage reporting if not running in air-gapped mode." (/langsmith/deploy-standalone-server).
14. **For non-Kubernetes self-hosting: operational gaps.** "Non-Kubernetes deployments have known gaps that you must implement and maintain yourself": independent queue autoscaling, graceful run draining, split-mode wiring, reference scaling configuration, version upgrades (/langsmith/deploy-standalone-server).
15. **For self-hosted LangSmith: the Kubernetes cluster and its databases.** "If you're deploying on your own infrastructure, you'll need to set it up yourself." (/langsmith/agent-server); self-hosted runs "in your own Kubernetes cluster" with external services such as ClickHouse, PostgreSQL, Redis or Valkey, blob storage (/langsmith/self-hosted; products-and-setup/lang-smith-setup index).
16. **Authentication for self-hosted Agent Servers.** Self-hosted has "No default authentication" and "You control all aspects of authentication and authorization" (/langsmith/auth). The developer supplies an identity provider: "Examples: Auth0, Supabase Auth, Okta, or your own auth server" (/langsmith/auth).
17. **Custom auth handlers and authorization rules.** "The values you return in `@auth.authenticate` are added to the run context" (/langsmith/auth).
18. **For non-LangGraph frameworks: a wrapper.** Agents built elsewhere are deployed "using the LangGraph Functional API or the `deployments-wrap-sdk` package." (/langsmith/agent-server).
19. **Tracing setup and thread metadata.** "To group traces into a thread, pass a `thread_id` metadata key with a unique value." (/langsmith/observability-concepts); "you must set the thread metadata (`session_id` or `thread_id`) on **all runs**, including child runs within a trace." (/langsmith/threads). In agent-based workspaces, "create an agent once before sending traces" (/oss/python/langgraph/local-server).
20. **Manual instrumentation where no integration exists.** "Use it when you're not using a supported integration or when you need granular control over what gets traced." (/langsmith/observability-concepts).
21. **Evaluation inputs: dataset, target function, evaluators.** "There are three main pieces need to run an evaluation: 1. A dataset of test inputs and expected outputs. 2. A target function which is what you're evaluating. 3. Evaluators that score your target function's outputs." (/langsmith/define-target-function).
22. **Provider keys for Playground, LLM-as-judge, and the LLM Gateway.** "Configure model providers for the LangSmith Playground and LLM-as-a-judge evaluators." (/langsmith/playground-model-providers); gateway "Choose how the LLM Gateway authenticates to each model provider, add provider keys as workspac[e secrets]" (/langsmith/llm-gateway-provider-authentication). Exception: "Gateway Credits let you call LangChain-hosted models ... without setting up a provider account or key." (/langsmith/llm-gateway-credits).
23. **Fine-tuning provider for Smithtune.** "It trains a model with Fireworks or Baseten" (/langsmith/smithtune).
24. **Frontend.** The docs provide Agent Chat UI and frontend patterns, but the developer builds or deploys the UI: "Build frontends that visualize LangGraph pipelines in real time." (/oss/python/langgraph/frontend/overview).

---

## 4. How the pieces connect (the documentation's own account)

### 4.1 Product stack

"Deep Agents is an agent harness: planning, subagents, filesystem tools, and context management on top of LangGraph. LangChain is the agent framework: abstractions and integrations for models, tools, and agent loops. LangGraph is the orchestration runtime: durable execution, streaming, human-in-the-loop, and persistence. LangSmith is the platform for tracing, evaluation, prompts, and deployment across frameworks. LangSmith Engine detects issues in LangGraph agent traces and proposes fixes... LangSmith Fleet is the no-code agent builder" (/oss/python/langgraph/overview).

### 4.2 Inside LangGraph: one run

1. Build: "Build a graph by defining state, adding nodes and edges, then compiling." (/oss/python/langgraph/graph-api).
2. Execute in super-steps: "Nodes that run in parallel share one super-step. Nodes that run in sequence use separate super-steps. A node becomes active when it receives input on an incoming edge." (/oss/python/langgraph/graph-api). The engine is Pregel: actors subscribe to channels and write to them (/oss/python/langgraph/pregel).
3. Persist: "A checkpointer saves a snapshot of graph state at each super-step, organized into threads." (/oss/python/langgraph/checkpointers), at a frequency set by the durability mode (same page).
4. Stream: "**Streaming** emits raw graph execution events from the Pregel engine. **Event streaming** normalizes those events, runs them through stream transformers, and exposes typed projections." (/oss/python/langgraph/event-streaming).
5. Pause and resume: "When an interrupt is triggered, LangGraph saves the graph state using its persistence layer and waits indefinitely until you resume execution." (/oss/python/langgraph/interrupts). Resume replays from a checkpoint boundary: "Execution returns to a checkpoint boundary and **replays** forward until it hits the pause again." (/oss/python/langgraph/functional-api).

### 4.3 Development to deployment

"Develop `langgraph dev` → Test Locally `langgraph dev` → Validate `langgraph up` → Deploy via UI or API" (flowchart, /langsmith/local-dev-testing). Component diagram: "LangGraph CLI -->|creates| Agent Server deployment", which connects to "Studio", "SDKs", and "RemoteGraph" (/langsmith/components). The control plane manages deployments and the data plane listener "periodically calls control plane APIs" to create, update, or delete them (/langsmith/data-plane).

### 4.4 One run on Agent Server

"When you invoke a run, the request flows through several components:
1. A client sends a request to an API server, which creates a pending run in the durable task queue.
2. A queue worker picks up the run, acquires a lease on it, loads the appropriate graph, and begins execution. The queue enforces that at most 1 run can be executed for a given thread at one time.
3. As the graph executes, the worker writes checkpoints to the persistence layer (the frequency depends on the durability mode) and broadcasts streaming events over the configured pubsub provider.
4. If the client opened a `/stream` connection, the API server subscribes to the pubsub channel and forwards events to the client via server-sent events in real time.
5. When execution completes, the worker updates the run status and releases its slot for the next run." (/langsmith/agent-server)

The page's diagram labels the same flow: "User -->|request| API", "API -->|create run| DB", "API -->|notify| Redis", "Redis -->|wake| QueueLoop", "QueueLoop -->|claim next run| DB", workers "save checkpoints / update status" to Postgres and "publish events" to Redis, "Redis -->|stream events| API", "API -->|SSE response| User" (/langsmith/agent-server). The execution model is "**assistants** for configuration, **threads** for state, and **runs** for workloads" (/langsmith/deployment).

### 4.5 Auth path for a deployed agent

Three components: an "Authentication Provider (Identity Provider/IdP)" that "Issues tokens", the "Agent Server (Resource Server)" that "Validates tokens with the auth provider" and "Enforces access control", and the "Client Application (Frontend)" that "Includes these tokens in requests to the Agent Server" (/langsmith/auth). "After authentication, the platform creates a special configuration object that is passed to your graph and all nodes via the configurable context." (/langsmith/auth).

### 4.6 From runs to traces to evaluation and fixes

- Agent Server sends traces automatically: "Agent Server is automatically configured to send traces to LangSmith." Tracing is "Required" on Cloud and "Optional" on Hybrid and Self-hosted (/langsmith/data-plane).
- Outside Agent Server, traces arrive through integrations or manual instrumentation: "There are two ways to send trace data to LangSmith." (/langsmith/observability-concepts).
- Calls across services can join one trace: "you can propagate trace context so that the entire request appears as a single unified trace in LangSmith." (/langsmith/agent-server-distributed-tracing).
- Model calls routed through the LLM Gateway become traces: "each call it routes becomes a LangSmith trace that records the routing and policy decisions made for it." (/langsmith/llm-gateway).
- Evaluation lifecycle: "During development and testing, offline evaluations validate functionality against curated datasets. After deployment, online evaluations monitor production behavior on live traffic. As applications mature, both evaluation types work together in an iterative feedba[ck loop]" (/langsmith/evaluation-concepts). Traces feed datasets: traces are used "to debug failures, monitor quality, and build the datasets you evaluate against." (/langsmith/observability).
- Automation rules act on traces ("item type, filter, sampling rate, and action", /langsmith/rules); Insights analyzes them (/langsmith/insights); Engine turns them into "tracked issues, fixes, and datasets" and "You can open a pull request with the proposed fix from the Engine tab." (/langsmith/engine; /oss/python/langgraph/overview).
- Feedback from end users links to traces: "When creating a run, include the keys in the `feedback_keys` field... The response will return a pre-signed URL for each key" (/langsmith/agent-server-feedback).
- Prompts and contexts can change behavior without redeploying: "Manage the prompts and versioned contexts your deployed agents pull at runtime, so you can change behavior without a full deploy." (/langsmith/deployment).
- A CI/CD example ties the three together: "you'll use the LangGraph open source framework for orchestrating and building the agent, LangSmith for observability and evaluations" (/langsmith/cicd-pipeline-example).

### 4.7 Hosting topologies (who runs which plane)

| Setup | Control plane | Data plane | Source |
|---|---|---|---|
| Cloud | LangChain | LangChain | "LangChain hosts the control plane, data plane, and databases." (/langsmith/deployment) |
| Hybrid | LangChain | Customer | "LangChain hosts the control plane; you host Agent Servers and their data plane." (/langsmith/deployment) |
| Self-hosted with control plane | Customer | Customer | "You host the control plane and Agent Servers in your own infrastructure alongside self-hosted LangSmith." (/langsmith/deployment) |
| Standalone server | none | Customer | "Run Agent Server containers with Docker or Kubernetes without a control plane" (/langsmith/deployment) |
| LangSmith BYOC (platform) | LangChain | Customer cloud | "LangChain runs the control plane, you run your data planes" (/langsmith/platform-setup) |

---

## 5. Limits and gaps the documentation itself states

**LangGraph library**
- Fault tolerance: "**Timeouts are async-only**: sync nodes with a `timeout` are rejected at compile time." "**One handler per node**". "**Handler failures bubble up**". "**`set_node_defaults` is not inherited by subgraphs**" (/oss/python/langgraph/fault-tolerance).
- Durability: in `"exit"` mode "intermediate state is not saved, so you cannot recover from system failures (like process crashes) mid-execution"; in `"async"` mode "there is a small risk that LangGraph does not write checkpoints if the process crashes during execution." (/oss/python/langgraph/checkpointers).
- Interrupt rules: "Do not wrap `interrupt` calls in try/except", "Do not reorder `interrupt` calls within a node", "Do not return complex values in `interrupt` calls", "Side effects called before `interrupt` must be idempotent" (/oss/python/langgraph/interrupts).
- Replay re-runs side effects: "Nodes after the checkpoint re-execute, including any LLM calls, API requests, or interrupts" and these are "always re-triggered during replay" (/oss/python/langgraph/checkpointers).
- Functional API: "Resume does **not** continue from the exact line where execution stopped." (/oss/python/langgraph/functional-api); the page lists "Common pitfalls" for side effects and "Non-deterministic control flow".
- Recursion limit: default "10,007 super-steps", after which LangGraph "raises `GraphRecursionError`" (/oss/python/langgraph/graph-api).
- Graph migrations on interrupted threads: "you can change edges and add nodes. Do not rename or remo[ve nodes]" (/oss/python/langgraph/graph-api).
- Troubleshooting entries name known failure modes: "PostgresSaver: `thread_id` too long", "`MemorySaver` does not persist between restarts", "Checkpoints growing unboundedly" (/oss/python/langgraph/persistence).
- `DeltaChannel` is beta, and the Deep Agents changelog warns: "**Rolling back from v0.6.0 is not supported once threads have persisted.**" because of the new checkpoint format (/oss/python/releases/changelog, entry "May 12, 2026") **[possibly stale]**.
- Chat mode in Studio "is only supported for graph's whose state includes or extends `MessagesState`" (/langsmith/studio).

**LangSmith Deployment / Agent Server**
- One run per thread at a time: "The queue enforces that at most 1 run can be executed for a given thread at one time." (/langsmith/agent-server).
- Per-worker concurrency: "Each worker executes up to `N_JOBS_PER_WORKER` runs concurrently (default: 10)" (/langsmith/agent-server).
- Double texting exists only on the server: "It is not available in the LangGraph open source framework." (/langsmith/double-texting).
- Custom auth does not apply to the OSS library alone: "It does not apply to isolated usage of the LangGraph open source library in your own custom server." (/langsmith/custom-auth).
- RemoteGraph: "Do not use `RemoteGraph` to call itself or another graph on the same deployment, as this can lead to deadlocks and resource exhaustion." (/langsmith/use-remote-graph).
- Semantic search: "Changing the embedding model or dimensions requires re-embedding all existing data. There is no automated migration tooling for this." (/langsmith/semantic-search).
- Distributed tracing headers: "**Only accept distributed-tracing headers from trusted services.**" (/langsmith/distributed-tracing).
- Cloud payload: "The maximum payload size for all requests sent to Cloud deployments is 25 MB." (/langsmith/cloud-platform-features).
- Serverless scaling: "Serverless deployments scale between zero and one replica." (/langsmith/data-plane).
- Standalone: "Do not run standalone servers in serverless environments. Scale-to-zero may cause task loss and scaling up will not work reliably." and "LangChain does not regularly test other orchestrators." (/langsmith/deploy-standalone-server).
- Factory functions cost time: "Factory functions add overhead on every invocation; compiled graphs do not." (/langsmith/agent-server).
- Alpha and beta pieces: custom store and custom checkpointer are alpha; server-side caching, Agent Auth, `langgraph deploy`, and preview builds are beta (entries 69, 120, 121, 125, 126, 135, 138).
- Preview builds "are available only on LangSmith Cloud for deployments created through the GitHub integration." (/langsmith/preview-builds).

**LangSmith**
- Runs per trace: "Each trace is limited to a maximum of 25,000 runs. Once the trace reaches this limit, LangSmith will reject any additional runs that you send for that trace." (/langsmith/usage-and-billing).
- Retention: "LangSmith (SaaS) retains trace data for 180 days from ingestion. After that, traces are permanently deleted" (/langsmith/observability-concepts); Base tier is 14 days (/langsmith/usage-and-billing).
- Rate limits: "LangSmith will respond with HTTP Status Code 429 indicating that rate or usage limits have been exceeded" (/langsmith/usage-and-billing), with named limits for load balancer throughput, hourly trace events, hourly ingest, monthly unique traces, run query and run stats endpoints (same page).
- Agent-based workspaces and Agent Registry are Cloud only; "They are not available on self-hosted LangSmith." (/langsmith/agent-environments; /langsmith/agent-registry).
- SmithDB: a page titled "SmithDB feature availability" lists "LangSmith features that are unavailable on self-hosted installations that quer[y]..." without SmithDB (/langsmith/self-host-smithdb-features); "Thread annotation-queue and webhook automations now require SmithDB queries." (/langsmith/changelog, "August 10-17, 2026").
- Deprecations: standalone LangSmith MCP Server (use Remote MCP); `list_runs`/`read_run` and `list_threads`/`read_thread`; custom output rendering for annotation queues; the LangSmith Observability Helm chart (entries 204, 206, 208, 238, 285).
- Beta or alpha pieces: LLM Gateway (beta), Smithtune (beta), Tuned Evaluators (beta), Engine fix validation and Red Teaming (private beta), Managed Deep Agents (public beta), BYOC on GCP and Azure (beta), Fleet self-hosting (beta), Tunnels and Relays (alpha), OpenAI Realtime and Gemini Live tracing (beta).
- Release-stage caveat: beta means "Interface or behavior may still change before the feature reaches GA" and alpha "may never ship as GA" (/langsmith/release-stages).

---

## 6. Not found

- **Exact rename date of LangGraph Cloud to LangGraph Platform.** The October 31, 2024 blog post describes "rebranding our service as LangGraph Platform" (https://www.langchain.com/blog/langgraph-platform-announce). I found no single dated rename notice in the docs. Search run: WebSearch "LangChain blog LangGraph Cloud renamed LangGraph Platform" (allowed domains langchain.com, blog.langchain.com, changelog.langchain.com).
- **An official announcement of the LangGraph Server to Agent Server rename.** Only the docs pull request "LangGraph Server --> Agent Server" (merged 2025-11-05, https://github.com/langchain-ai/docs/pull/1252) was found. Searches: WebSearch `"LangGraph Server" renamed "Agent Server" LangSmith`; grep for "LangGraph Server" across 520 downloaded docs pages.
- **Explicit GA statements for most unlabeled features.** For features with no stage label (for example Assistants, Threads, Insights, Agent Registry, Context Hub, Engine core), the docs do not say "GA". The release-stages page allows features to skip labels, so these are reported as "no stage stated". Search: grep for "beta|alpha|generally available|GA" in the first 60 lines of each downloaded page.
- **A dedicated "durable execution" page in the current LangGraph navigation.** The overview links "durable execution" to the Persistence page (/oss/python/langgraph/overview), and the navigation lists no separate page (https://docs.langchain.com/_llms/agent-development-lifecycle/build/python.txt). Earlier docs had one; I did not confirm whether it still exists at a hidden URL.
- **The JavaScript LangGraph SDK reference page.** `https://docs.langchain.com/langsmith/langgraph-js-sdk` returned "Page Not Found" on 2026-11-11. The npm package `@langchain/langgraph-sdk` 1.15.0 exists (https://www.npmjs.com/package/@langchain/langgraph-sdk).
- **The license of Agent Server stated in the docs.** The docs describe license keys but I found no docs sentence naming the source license. The Elastic-2.0 value comes only from PyPI package metadata for `langgraph-api` (https://pypi.org/pypi/langgraph-api/json). Search: grep "license" across downloaded deployment pages.
- **Per-page "last updated" dates.** The Markdown docs pages carry no visible last-modified date, so per-component documentation dates come from changelogs and the docs repository commit log instead.
- **Pages not read in full.** About 520 pages were downloaded and indexed; most entries rely on each page's title, description line, and opening paragraph, plus targeted section reads for LangGraph core, Agent Server, Deployment, observability and evaluation concepts, auth, and limits. The 596 REST API endpoint pages and the BYOC, Terraform, and self-host-SmithDB sub-pages were inventoried from the navigation index only (https://docs.langchain.com/llms.txt and the products-and-setup index).

---

*Sources index files used for navigation structure (read 2026-11-11):* https://docs.langchain.com/llms.txt ; https://docs.langchain.com/_llms/agent-development-lifecycle.txt ; .../build/python.txt ; .../build/type-script.txt ; .../deploy.txt ; .../deploy/get-started.txt ; .../monitor.txt ; https://docs.langchain.com/_llms/products-and-setup.txt ; .../products-and-setup/lang-smith-setup.txt
