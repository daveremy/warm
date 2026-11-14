---
title: Amazon Bedrock AgentCore component inventory
date: 2026-11-11
read-on: 2026-11-11
author: research subagent
sources: primary only (docs.aws.amazon.com, aws.amazon.com product page, AWS What's New, AWS blogs)
---

# Amazon Bedrock AgentCore: component inventory (as of 2026-11-11)

Method: I downloaded the Developer Guide navigation (`toc-contents.json`, 597 pages) and every page in it on 2026-11-11, then read the pages for each component. Quotes are verbatim from those pages. The entries follow the Developer Guide's left navigation order and its own names. All Developer Guide URLs share the prefix `https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/`; every URL below is written in full anyway.

Staleness rule: any release date before 2026-05-11 (more than six months before this file) is marked **(over six months old, possibly stale)**. The pages themselves were read today, so a quote from a page is current as of 2026-11-11 even when the feature it describes is older.

---

## 1. What it is

**Self-description (Developer Guide overview, read 2026-11-11):**

> "Amazon Bedrock AgentCore is an agentic platform for building, deploying, and operating highly effective agents securely at scale using any framework and foundation model. With AgentCore, you can enable agents to take actions across tools and data with the right permissions and governance, run agents securely at scale, and monitor agent performance and quality in production - all without any infrastructure management. AgentCore services work together or independently with any open-source framework such as CrewAI, LangGraph, LlamaIndex, and Strands Agents and with any foundation model, so you don't have to choose between open-source flexibility and enterprise-grade security and reliability."

URL: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html (read 2026-11-11)

The same page says the services are "modular services and capabilities that you can use together or independently", and lists 13 in its "Core services" table: Harness, Runtime, Memory, Gateway, Identity, Code Interpreter, Browser, Observability, Payments, Evaluations, Optimization, Policy, Registry. The navigation also has top-level sections that are not in that table: AgentCore Web Search, AgentCore MCP Server, AgentCore CLI, the Python and TypeScript SDK references, and Security.

**Product page (https://aws.amazon.com/bedrock/agentcore/, read 2026-11-11):** headline "The platform for production AI agents. Any framework. Any model. Secure at scale." The page carries no preview or GA labels.

**Release status:**
- Platform GA: "Amazon Bedrock AgentCore is now generally available across nine AWS Regions" (release notes, October 2025 entry). https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html. What's New post dated October 13, 2025: https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available. **(over six months old, possibly stale as a region count; the current region table has 22 Regions, see section 5.)**
- Initial preview: release notes "July 2025: Initial release (preview)". **(over six months old)**
- Today, most components are GA; several named features are still labeled preview (marked per entry below).

**Latest documentation change found:** the release notes' newest section is "November 2026" (entries: Harness Strands-powered managed defaults; Web Search API `InvokeWebSearch`; Gateway Web Answer connector; Runtime MCP protocol 2026-07-28; Runtime V2 in five more Regions; 250 concurrent connections for V2; `OverheadLatency` metric). The HTTP `Last-Modified` header on the release notes page was `Wed, 11 Nov 2026 10:46:16 GMT`. The release notes give months, not days. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html

---

## 2. Components

Legend for "Who runs it": **Vendor hosts** = AWS operates it as a managed service. **Developer deploys** = the developer supplies an artifact that AWS hosts. **Developer builds** = the developer writes and runs it.

### 2.0 Interfaces (navigation: "Get started", "Understand the available interfaces", "Customize the CDK code", "AgentCore CLI", "AgentCore MCP Server", SDK references)

**C1. AgentCore CLI**
- What: "The AgentCore CLI is a command-line tool for building, deploying, and operating agents and Amazon Bedrock AgentCore resources." Project commands are "create, add, remove, dev, build, deploy, status, invoke, logs, traces, and export"; resource commands are "eval, gateway, harness, identity, memory, payment, and runtime." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-cli-way-to-interact.html
- Who runs it: developer runs it locally. "It requires Node.js 20.12 or later. Install the AgentCore CLI globally with npm: npm install -g @aws/agentcore" https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/develop-agents.html
- Depends on: Node.js, AWS credentials, AWS CDK (projects "include a small CDK app built on the @aws/agentcore-cdk constructs", release notes October 2026).
- Status: GA. Release notes March 2026 "AgentCore CLI is now Generally Available" (over six months old, possibly stale); October 2026 "AgentCore CLI: Version 1.0 is now available". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html

**C2. Agent Inspector (part of the CLI)**
- What: "Developers running agentcore dev now get a browser-based UI for chatting with agents, inspecting token usage and tool calls, viewing execution traces on a timeline, and browsing deployed AgentCore Memory." (release notes, April 2026) https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html
- Who runs it: developer, locally.
- Status: shipped April 2026 (over six months old, possibly stale); no preview label.

**C3. AgentCore Python SDK**
- What: "The simplest approach is to use the AgentCore Python SDK to create your agent code and use the AgentCore CLI to deploy your agent." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/develop-agents.html. Reference sections: Runtime, Identity, Gateway, Evaluation, Payments; "Auto-generated from bedrock-agentcore v1.18.1". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-python-sdk-reference.html
- Who runs it: developer builds with it (library inside agent code).
- Status: library released; some classes carry "This feature is in preview and might change in future releases." (ActorProfile, BatchEvaluation*, SimulationConfig, SimulatedScenario and related evaluation classes). Same URL.

**C4. AgentCore TypeScript SDK**
- What: reference covers Runtime, Identity, Code Interpreter; "Auto-generated from bedrock-agentcore v0.4.1". `BedrockAgentCoreApp` "Hosts agents on Amazon Bedrock AgentCore runtime." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-typescript-sdk-reference.html
- Who runs it: developer builds with it. Status: no label.

**C5. AgentCore MCP Server**
- What: "helps you transform, deploy, and test Amazon Bedrock AgentCore-compatible agents directly from your preferred development environment." Works with "Kiro, Cursor, Claude Code, and Amazon Q CLI". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/mcp-getting-started.html
- Who runs it: developer runs it locally in a coding assistant. Release notes April 2026: it "covers Runtime, Memory, Browser, and Code Interpreter, and authenticates through your default AWS credential chain." (over six months old, possibly stale)
- Status: no label.

**C6. AWS SDK, AWS CLI, AgentCore console**
- What: "To call the full set of AgentCore operations, use the AWS SDK." The interfaces page also lists "Amazon Bedrock AgentCore console" and "AWS Command Line Interface". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/develop-agents.html
- Who runs it: vendor hosts the APIs and console; developer calls them.

**C7. AWS CDK constructs**
- What: "The AgentCore CLI manages your project's AWS resources with AWS CDK constructs from the @aws/agentcore-cdk package." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/customize-project-cdk-code.html. Release notes May 2026: "The aws-bedrockagentcore L2 constructs have graduated from alpha to stable in aws-cdk-lib ... The Policy submodule remains in alpha."
- Who runs it: developer.
- Status: stable, except the Policy submodule (alpha).

### 2.1 AgentCore harness (navigation: "AgentCore harness")

**C8. AgentCore harness**
- What: "A managed agent loop that lets you define and invoke AI agents with a single API call. Specify a model, system prompt, and tools inline." (overview table) https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html. "You declare what your agent does (model, tools, skills, instructions); AgentCore handles the environment, compute, memory, identity, networking, and observability". "The harness is powered by Strands Agents, the open-source agent framework from AWS. There is no separate harness charge." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html
- Who runs it: vendor hosts. "The harness is a managed abstraction that runs inside Runtime". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-vs-runtime.html
- Depends on: AgentCore Runtime (microVM per session); optionally Memory, Gateway, Browser, Code Interpreter, Observability, Identity. Requires an IAM execution role.
- Status: GA. Page: "AgentCore harness is available in GA across all regions shown here." What's New posted Jun 17, 2026: https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available. (The Developer Guide release notes file this under "July 2026"; the What's New date is June 17, 2026.) Public preview: April 2026.

**C9. Harness: Models and instructions (managed defaults)**
- What: "Define a harness once with defaults for model, system prompt, tools, memory, and execution limits. Override any of those on a single invocation". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-models.html. Default model: "In commercial AWS Regions, the current default is Anthropic Claude Opus 5 on Amazon Bedrock". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-get-started.html. Providers: "Amazon Bedrock, OpenAI, Google Gemini, or any LiteLLM-compatible provider". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html
- Who runs it: vendor hosts; developer configures. Status: GA with harness; "Managed defaults can evolve." (release notes November 2026).

**C10. Harness: Tools (including built-in tools)**
- What: "Tools are declarative. You list what the agent can call; AgentCore handles invocation, credentials, and results. The harness supports five tool types and managed built-in tools." Types: MCP servers, AgentCore Gateway, AgentCore Browser, AgentCore Code Interpreter, inline functions. Built-in selectors: `shell`, `read`, `write`, `edit`, `file_operations`, `todo_write`, `retrieve_context`, `subagent`, `web_fetch`. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-tools.html
- Inline functions: "Tool schemas that execute on the client side, not on the harness VM." (developer builds these). Same URL.
- Status: GA with harness.

**C11. Harness: Lifecycle hooks**
- What: "Lifecycle hooks send an event to an AWS Lambda function, Amazon SNS topic, or Amazon EventBridge event bus at a defined point in the harness agent loop." "A harness supports up to 20 hooks". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-lifecycle-hooks.html
- Who runs it: vendor emits; developer builds the Lambda/SNS/EventBridge target. Released September 2026.

**C12. Harness: Skills**
- What: "Agent Skills are bundles of markdown and scripts that give the agent domain knowledge on demand. Each skill follows the open AgentSkills.io standard". Sources include "AWS Skills", "Git (HTTPS)", S3, and container-baked. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-skills.html
- Who runs it: AWS curates AWS Skills; developer may build its own. Status: GA with harness.

**C13. Harness: Memory**
- What: "When memory is enabled, the harness persists conversation state in AgentCore Memory." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-memory.html. Depends on AgentCore Memory (C39).

**C14. Harness: Environment and filesystem**
- What: "Every harness session runs in an isolated microVM with its own filesystem and shell." Covers "default or custom container", direct commands, environment variables, persistent filesystems. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-environment.html
- Developer may bring a container image.

**C15. Harness: Interactive shells (terminals)**
- What: "The InvokeAgentRuntimeCommandShell operation opens a persistent, interactive terminal inside a running AgentCore harness session over WebSocket." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-command-shell.html. Released September 2026.

**C16. Harness: Observability and cost controls**
- What: "Every harness invocation automatically generates traces, logs, and metrics through AgentCore Observability in CloudWatch." "Before you see traces, enable Transaction Search in CloudWatch (one-time per account)." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-operations.html

**C17. Harness: Versioning and endpoints**
- What: "Amazon Bedrock AgentCore implements automatic versioning for AgentCore harnesses and lets you manage different configurations using endpoints." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-versioning.html

**C18. Harness: Export to code**
- What: "Export harness to code takes a managed harness configuration and generates a runtime agent from it as editable Python source code using the Strands framework." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-export.html
- Who runs it: output is code the developer owns and deploys to Runtime.

**C19. Harness: Security** (navigation item "Security", page harness-security.html; access controls for the harness). https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-security.html

**C20. Step Functions integration with AgentCore harness**
- What: "AWS Step Functions now integrates natively with AgentCore harness, enabling teams to embed agent reasoning steps directly into production workflows." (release notes, July 2026). The harness page names "the AgentCore InvokeHarness state in AWS Step Functions". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html
- Who runs it: vendor hosts both services; developer builds the state machine.

### 2.2 AgentCore Runtime (navigation: "AgentCore Runtime: Host agent or tools")

**C21. AgentCore Runtime**
- What: "Amazon Bedrock AgentCore Runtime provides a secure, serverless and purpose-built hosting environment for deploying and running AI agents or tools." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html. "An AgentCore Runtime is the foundational component that hosts your AI agent or tool code." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html
- Who runs it: vendor hosts; developer deploys a container or zip.
- Depends on: Amazon ECR (container path), IAM execution role, optionally Identity for auth.
- Status: GA since October 2025 (over six months old, possibly stale as a date; still GA per current pages).

**C22. Compute type: microVMs**
- What: "Choose microVMs for fully managed, serverless sessions that start instantly and scale on demand, where you pay only for what you use." Sessions "run for up to 8 hours on microVMs". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html. Harness diagram labels it "Firecracker microVM". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html
- Who runs it: vendor hosts. Available in all 22 listed Regions.

**C23. Compute type: Instances (with capacity providers)**
- What: "Amazon Bedrock AgentCore Runtime runs your agent on Amazon EC2 managed instances that it provisions and operates inside your own AWS account". "A capacity provider defines the infrastructure those instances use". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-instances-how-it-works.html. "Instances support persistent sessions of up to 14 days and GPU-accelerated instance types." (release notes, August 2026)
- Who runs it: vendor operates EC2 in the developer's account; developer defines the capacity provider.
- Status: released August 2026; 9 Regions.

**C24. Platform versions (V1, V2)**
- What: "A platform version controls how AgentCore Runtime starts your agent. You set it with the platformVersion field (V1 or V2) on each agent runtime. V1 is the default." "V2 starts your agent from a snapshot". V2 is in 10 Regions. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html. Companion page "Optimize your agent": https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-v2-optimize.html

**C25. Runtime service contract and protocols (HTTP, MCP, A2A, AG-UI)**
- What: "The AgentCore Runtime service contract defines the standardized communication protocol that your agent application must implement". Protocols: HTTP (port 8080, `/invocations`, `/ws`), MCP (8000, `/mcp`), A2A (9000, `/`), AG-UI (8080). https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-service-contract.html. HTTP contract: "Platform: ARM64 container". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-http-protocol-contract.html
- Sub-pages, each its own nav item: Deploy MCP servers (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html), Stateful MCP features (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/mcp-stateful-features.html), Deploy A2A servers (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-a2a.html), Deploy AG-UI servers (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-agui.html), Configure serving port and invocation path (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-configure-invocation.html).
- Who: developer builds the server that honors the contract; vendor hosts it.

**C26. Direct code deployment**
- What: "With direct code deployment, you package your agent code and its dependencies in a .zip file archive and deploy it to AgentCore Runtime." Python and Node.js. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-code-deploy.html. Released November 2025 (over six months old, possibly stale).

**C27. Amazon Bedrock Managed Agents (with OpenAI)**
- What: "Amazon Bedrock Managed Agents runs the OpenAI Codex harness on AWS." "For other workloads, Bedrock Managed Agents invokes an AgentCore Runtime in your account." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-bma.html
- Status: **Preview**: "Amazon Bedrock Managed Agents (with OpenAI) is in preview. Features and APIs may change before general availability." Same URL.

**C28. Isolated sessions, lifecycle settings, stop session**
- What: "Each session in AgentCore Runtime receives its own dedicated microVM with isolated compute, memory, and filesystem resources." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html. "The LifecycleConfiguration input parameter to CreateAgentRuntime lets you manage the lifecycle of runtime sessions". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-lifecycle-settings.html. "The StopRuntimeSession operation lets you immediately terminate active agent AgentCore Runtime sessions". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-stop-session.html

**C29. File system configurations (managed session storage, capacity provider volumes, bring-your-own S3 Files/EFS)**
- What: "AgentCore Runtime supports persistent file systems through the filesystemConfigurations parameter." Managed types: "Session storage (Preview)", described as "Per-session storage on microVM runtimes that persists across stop/resume cycles", and "Capacity provider volumes", described as "Amazon EBS volumes on Instances runtimes". Bring-your-own: Amazon S3 Files and Amazon EFS (release notes May 2026). https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html
- Status: session storage **Preview** (same URL); BYO filesystem released May 2026.

**C30. Mount your own file systems (FUSE)**
- What: "your container can mount file systems itself at runtime: run a FUSE client over the FUSE (Filesystem in Userspace) device (/dev/fuse)". "available only for agent runtimes on platform version V2." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-fuse-mounts.html. Released October 2026.

**C31. Asynchronous and long-running agents**
- What: "Asynchronous tasks allow your agent to continue processing after responding to the client and handle long-running operations without blocking responses." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-long-run.html

**C32. Stream agent responses**
- What: example "shows how an AgentCore Runtime agent can stream a response back to a client." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/response-streaming.html

**C33. Bidirectional streaming (WebSocket, WebRTC)**
- What: "AgentCore Runtime supports two protocols for bidirectional streaming: WebSocket ... WebRTC". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-bidirectional-streaming.html. WebRTC "requires: VPC network mode". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-webrtc.html. Bidirectional streaming released December 2025 (over six months old, possibly stale).

**C34. Pass custom headers**
- What: "Custom headers let you pass contextual information from your application directly to your agent code". "Up to 20 headers can be configured per runtime". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-header-allowlist.html

**C35. Inbound Auth and Outbound Auth (Runtime)**
- What: "Inbound Auth, powered by AgentCore Identity, controls who can access and invoke your agents or tools". "Outbound Auth ... lets your agents hosted on AgentCore Runtime securely access third-party services". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html
- Depends on: AgentCore Identity; an external IdP for OAuth.

**C36. Runtime versioning and endpoints**
- What: "Each AgentCore Runtime in Amazon Bedrock AgentCore is automatically versioned". "The DEFAULT endpoint automatically points to the latest version". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agent-runtime-versioning.html

**C37. Invoke an agent** (nav item; `InvokeAgentRuntime`, `InvokeAgentRuntimeWithWebSocketStream`). https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-invoke-agent.html

**C38. Session endpoints**
- What: "With session endpoints, you can connect to application servers running inside an Amazon Bedrock AgentCore Runtime session. A session endpoint is an authenticated HTTPS URL that addresses one runtime session." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-session-endpoints.html. Released October 2026.

**C39. Shell execution (one-shot and interactive)**
- What: "One-shot command execution - InvokeAgentRuntimeCommand Runs a single command" and "Interactive shells (terminals) - InvokeAgentRuntimeCommandShell Opens a persistent terminal session over WebSocket". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-shell-execution.html

**C40. Observe agents (Runtime)**: points to Observability. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-observability.html

### 2.3 AgentCore Memory (navigation: "AgentCore Memory: Add memory to your agent")

**C41. AgentCore Memory**
- What: "AgentCore Memory is a fully managed service that gives your AI agents the ability to remember past interactions". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html
- Who runs it: vendor hosts. Developer calls APIs from agent code (Runtime path) or enables it in config (harness path).
- Status: GA since October 2025 (over six months old as a date). 16 Regions.

**C42. Short-term memory (events)**
- What: "Short-term memory stores raw interactions that help the agent maintain context within a single session." Captured "as an event using the CreateEvent operation". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html

**C43. Long-term memory (memory records)**
- What: long-term memory "persists across sessions" (overview table). Strategies "determine what types of information to extract from raw conversations". "If no strategies are specified, long-term memory records will not be extracted". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-strategies.html

**C44. Built-in strategy: Semantic**: "designed to identify and extract key pieces of factual information and contextual knowledge from conversational data." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/semantic-memory-strategy.html

**C45. Built-in strategy: User preference**: "designed to automatically identify and extract user preferences, choices, and styles from conversational data." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/user-preference-memory-strategy.html

**C46. Built-in strategy: Summary**: "responsible for generating condensed, real-time summaries of conversations within a single session." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/summary-strategy.html

**C47. Built-in strategy: Episodic (with reflections)**: "Episodic memory captures meaningful slices of user and system interactions". "Reflections build on episodic records by analyzing past episodes". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/episodic-memory-strategy.html. Released December 2025 (over six months old, possibly stale).

**C48. Built-in with overrides strategy (custom strategy)**: "let you override the default behavior of the built-in strategies by providing your own instructions and selecting a specific foundation model". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-custom-strategy.html. Requires a `memoryExecutionRoleArn`; Bedrock usage "consumes your allocated capacity". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/bedrock-capacity.html

**C49. Self-managed strategy**: "gives you complete control over your memory extraction and consolidation pipelines". Developer builds the pipeline; AgentCore stores and retrieves. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-self-managed-strategies.html

**C50. Memory organization (actor, session, strategy, namespace)**: "This lets you isolate memories by session and by actor. For long-term memory, you can also set a namespace". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html. "Flexible Namespaces" released August 2026.

**C51. Memory record streaming**: "delivers real-time notifications when memory records are created, updated, or deleted" to "a Kinesis Data Stream in your account". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-record-streaming.html. Released March 2026 (over six months old, possibly stale).

**C52. Cross-account memory access**: "supports cross-account access, enabling you to build multi-account architectures". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-cross-account-access.html

**C53. Record time-to-live (TTL)**: "By default, long-term memory records do not expire. You can optionally set a time-to-live (TTL)". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-record-ttl.html. Released October 2026.

**C54. Direct long-term memory ingestion (IngestData)**: "Use IngestData to submit content directly for long-term memory extraction, without persisting it as a short-term memory event." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-ingest-data.html. Released August 2026.

**C55. Long-term memory metadata (filtering)**: "lets you add structured attributes to your long-term memory records." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-memory-metadata.html

**C56. Redrive failed ingestions**: "failed jobs are moved to a dedicated queue for your memory resource." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-redrive.html

**C57. Access Memory through a gateway (Memory connector)**: "With an AgentCore Gateway in front of AgentCore Memory, you can move that enforcement out of your application code and into the infrastructure." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-gateway-connector.html. Depends on Gateway. No status label found.

**C58. Memory encryption and memory replication**: customer-managed KMS key option (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html); "AgentCore Memory keeps its data in one AWS Region, so the standby Region ... has none of your agent's memory unless you replicate it." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/disaster-recovery-memory.html. Replication is developer-built.

### 2.4 AgentCore Gateway (navigation: "AgentCore Gateway")

**C59. AgentCore Gateway**
- What: "a fully managed AI gateway that provides a single, secure entry point for agentic traffic", "connecting agents to tools, to other agents, and to large language models (LLMs)." Key capabilities named: "Security Guard", "Translation", "Composition", "Secure Credential Exchange", "Semantic Tool Selection", "Infrastructure Manager". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Who runs it: vendor hosts. Status: GA (part of October 2025 GA; over six months old as a date). 22 Regions.

**C60. MCP targets: Lambda, API Gateway stages, OpenAPI, Smithy, MCP servers**
- What: "MCP targets operate in aggregation mode": "the gateway acts as an MCP server whose capabilities combine those of all its MCP targets." Types listed: "AWS Lambda function targets", "Amazon API Gateway REST API stages as targets", "OpenAPI schema targets", "Smithy model targets", "MCP servers targets". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-targets-mcp.html
- Who: developer builds/owns the backend; vendor hosts the gateway.

**C61. Built-in templates from integration providers**: templates for "Amazon, Asana, BambooHR, Brave, Coinbase x402 Bazaar, Confluence, Jira, Microsoft, PagerDuty, Salesforce, ServiceNow, Slack, Smartsheet, Tavily, Zendesk, Zoom". "Set up hosting for the server yourself." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-integrations.html

**C62. Built-in connector: Amazon Bedrock Managed Knowledge Bases**
- What: "Amazon Bedrock Managed Knowledge Bases provides fully managed retrieval-augmented generation (RAG)". AgentCore "exposes a managed knowledge base as a native Gateway connector". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-managed-kb.html
- Who runs it: vendor hosts; developer supplies data sources. Creation is documented in the Amazon Bedrock User Guide.
- Status: GA, release notes July 2026 "Amazon Bedrock Managed Knowledge Base is now Generally Available".

**C63. Built-in connector: Web Search Tool**
- What: "a fully managed tool that lets agents ground responses in current, accurate web knowledge while keeping data residency within your secured AWS environment with zero data egress." "exposed as a built-in connector target on AgentCore Gateway using the Model Context Protocol (MCP)." (release notes July 2026). Page: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-web-search-tool.html
- Status: GA ("Web Search Tool is now Generally Available", July 2026). 7 Regions.

**C64. Built-in connector: Web Answer**
- What: "takes a natural-language question and returns a synthesized answer with citations to current web sources. It is a managed connector that you add as a target to your AgentCore Gateway." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-web-answer-tool.html
- Status: GA in us-east-1 only (release notes November 2026).

**C65. Built-in connector: AWS Step Functions**
- What: "Amazon Bedrock AgentCore Gateway includes a built-in Step Functions connector. You create a gateway target that uses the connector and choose which Step Functions operations to expose as tools." "available in all AWS Regions where Amazon Bedrock AgentCore Gateway is available." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-step-functions.html. Released October 2026.
- Also: "Connector versions" nav item (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-versions.html).

**C66. HTTP targets: AgentCore Runtime targets and HTTP passthrough**
- What: "For HTTP targets, the gateway sends traffic directly to the target without aggregation or protocol translation." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-targets-http.html. Passthrough is "ideal for fronting agent URLs, external APIs, or any HTTP service". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-http-passthrough.html. Runtime targets: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-http-runtime.html
- Status: "Gateway: AgentCore Runtime targets are now generally available" and "HTTP passthrough targets" (release notes July 2026).

**C67. Inference targets (connector, provider, InvokeModel format)**
- What: "The gateway acts as a unified LLM proxy layer, allowing clients to connect to a single endpoint and route requests to the correct model provider based on the model specified in the request." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-targets-inference.html. Connector targets "provide preconfigured setup for supported model providers" (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-inference-connector.html); provider targets "give you explicit control over the endpoint, model mappings, and operations" (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-inference-provider.html); InvokeModel wire format support (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-inference-invokemodel.html).
- Depends on: model provider accounts and credentials the developer holds. Released July 2026; InvokeModel support October 2026.

**C68. Gateway authorizer (inbound authorization) and credential providers (outbound)**
- What: "Each gateway must have an inbound authorization configuration". Types: "OAuth (JWT)", "IAM (AWS Signature Version 4)", "authenticate only", "no authorization". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-core-concepts.html. Setup pages: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-inbound-auth.html, https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-outbound-auth.html

**C69. Semantic search of tools**: "call the x_amz_bedrock_agentcore_search tool to search for tools in your gateway with a natural language query." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using-mcp-semantic-search.html

**C70. MCP protocol features: prompts, resources, elicitation, sampling, progress and logging notifications, tasks, MCP sessions, response streaming**
- What (features table): MCP sessions "Enable stateful interactions between clients and your gateway"; response streaming "Receive real-time Server-Sent Events (SSE)"; elicitation, sampling; Tasks "Let long-running tool calls return a task ID immediately". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-features.html. Tasks: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-mcp-tasks.html. Sessions/streaming/elicitation/sampling released May 2026; tasks October 2026.

**C71. Gateway rules (including model routing and fallback, session stickiness)**
- What: "Gateway rules let you control traffic routing and override target configurations on your gateway without redeploying targets." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-rules.html. "With model fallback, you define an ordered chain of alternative destinations". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-rules-fallback.html. Session stickiness: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-rules-session-stickiness.html
- Depends on: configuration bundles (C125) for overrides.

**C72. Fine-grained access control and Gateway interceptors**
- What: "You can implement access control through gateway interceptors for custom logic, or use resource-based policies". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-fine-grained-access-control.html. "Configuring interceptors on your gateway allows you to run custom code during each invocation of your gateway." Two types: REQUEST and RESPONSE. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-interceptors.html
- Who: developer builds the interceptor Lambda.

**C73. Rate limits**: "With rate limits, you control how much traffic individual callers, targets, or tools can consume on your gateway." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-rate-limits.html. Released August 2026.

**C74. AWS WAF integration**: "You can use AWS WAF with Amazon Bedrock AgentCore Gateway to protect your gateway from web exploits, bot traffic, and volumetric attacks." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-waf.html

**C75. Other Gateway features (nav "Advanced topics" and "Debug")**: debugging messages (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-debug-messages.html), customer-managed KMS encryption (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-encryption.html), custom domain names via CloudFront (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-custom-domains.html), header and query parameter propagation (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-headers.html), MCP Inspector, CloudTrail logging (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-cloudtrail.html), VPC egress (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-vpc-egress.html), performance optimization.

### 2.5 AgentCore Identity (navigation: "AgentCore Identity")

**C76. AgentCore Identity**
- What: "an identity and credential management service designed specifically for AI agents and automated workloads." "Agent identities are implemented as workload identities with specialized attributes". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html
- Who runs it: vendor hosts. Status: GA (October 2025 GA; over six months old as a date). 22 Regions.

**C77. Workload identities and the agent identity directory**
- What: "Workload identities represent the digital identity of your agents within the AWS environment." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/understanding-agent-identities.html. "The agent identity directory is a centralized collection of all workload identities within your AWS account." Identities are created "automatically by AgentCore Runtime and Gateway or manually". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agent-identity-directory.html

**C78. Token vault (secure credential storage)**: "The token vault provides security for storing OAuth 2.0 tokens, OAuth client credentials, and API keys". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html

**C79. Inbound JWT authorizer**: "authenticates and authorizes incoming OAuth 2.0 API requests to AgentCore Runtime and AgentCore Gateway." "IdP agnostic". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/inbound-jwt-authorizer.html

**C80. Credential providers (OAuth2 client, API key)**: "A resource credential provider stores the endpoint configuration and credentials that AgentCore Identity uses to get tokens or API keys for a resource server." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/resource-providers.html. Supports "OAuth 2.0 client credentials grant (machine-to-machine) and OAuth 2.0 authorization code grant (user-delegated access)". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html. Release notes July 2026: "Reference Existing Secrets in AWS Secrets Manager".

**C81. Provider setup (built-in IdP/provider configurations)**: nav lists: Amazon Cognito, Auth0 by Okta, Atlassian, CyberArk, Dropbox, Facebook, FusionAuth, GitHub, Google, HubSpot, LinkedIn, Microsoft, Notion, Okta, OneLogin, Ping Identity, Reddit, Salesforce, Slack, Spotify, Twitch, X, Yandex, Zoom. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idps.html. Developer brings the accounts/apps at each provider.

**C82. On-behalf-of (OBO) token exchange**: lets agents and MCP servers "exchange an inbound user access token for a new, scoped access token that targets a downstream resource server". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/on-behalf-of-token-exchange.html. Released April 2026 (over six months old, possibly stale).

**C83. Private Key JWT client authentication**: "AgentCore Identity authenticates to a downstream identity provider's token endpoint using a signed JWT client assertion ... instead of a client secret." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/private-key-jwt.html. Released July 2026.

**C84. Workload access token**: "an AWS-signed opaque access token that enables agents to access first-party AgentCore services, such as outbound credential providers." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/get-workload-access-token.html

**C85. Consent portal**: "a hosted, AWS-managed portal that authenticates your end users to an OpenID Connect (OIDC) identity provider (IdP) and gathers their consent before your agent accesses a downstream resource on their behalf." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-consent-portal.html. Released September 2026.

**C86. Private identity providers**: "supports connecting to OAuth 2.0 identity providers (IdPs) hosted inside your AWS VPC". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-private-idp.html

**C87. Identity data protection and tagging**: KMS key for Token Vault; tagging. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-tagging.html

### 2.6 AgentCore payments (navigation: "AgentCore payments")

**C88. AgentCore payments**
- What: "a fully managed service that enables microtransaction payments in AI agents to access paid APIs, MCP servers, and content." Uses "the x402 protocol and the Machine Payments Protocol (MPP)". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-how-it-works.html
- Who runs it: vendor hosts orchestration; external wallet providers (Coinbase CDP, Stripe/Privy) hold funds.
- Depends on: AgentCore Identity (credential storage), a wallet provider account; for Coinbase, an AWS Marketplace subscription: "you must subscribe to the Coinbase Wallets for AgentCore Payments listing in AWS Marketplace." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-marketplace-subscription.html
- Status: **GA** per What's New "Posted on: Aug 18, 2026" (https://aws.amazon.com/about-aws/whats-new/2026/08/bedrock-agentcore-payments-ga/). Preview announced April 2026 (What's New https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview; Developer Guide release notes list the preview under May 2026). The Developer Guide release notes have **no** payments GA entry, and the payments pages carry no preview or GA label. 12 Regions.

**C89. PaymentManager**: "the top-level resource that coordinates payment operations for your AWS account." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-how-it-works.html

**C90. PaymentConnector**: "integrates your PaymentManager with an external payment provider such as Coinbase or Stripe (Privy)." Types "CoinbaseCDP" and "StripePrivy". Same URL.

**C91. Payment sessions and payment instruments**: "Payment sessions represent individual payment contexts between an agent and an end user. Each session has configurable payment limits". "Payment instruments represent the end user's payment credentials, such as a crypto wallet address." Same URL.

**C92. Coinbase x402 Bazaar via Gateway**: "You can add the Coinbase x402 Bazaar MCP server as a target in a Gateway to discover 10,000+ existing paid MCP tools". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-connect-bazaar.html

**C93. Payments Browser Tool integration and framework integrations**: "There are two ways your agent can access x402 paid content: via the Browser Tool or via standard HTTP calls." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-browser.html; framework integrations: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-framework-integrations.html

### 2.7 Built-in tools: Code Interpreter, Browser, Web Search (the region table groups Code Interpreter and Browser as "AgentCore Built-in Tools")

**C94. AgentCore Code Interpreter**
- What: "enables AI agents to write and execute code securely in sandbox environments". "For inline upload, the file size can be up to 100 MB. And for uploading to Amazon S3 through terminal commands, the file size can be as large as 5 GB." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html. Languages/runtimes: Python (`python`), JavaScript and TypeScript (`nodejs`, `deno`). https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-runtime-selection.html. Pre-installed libraries (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-preinstalled-libraries.html); S3 access via an execution role (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-s3-integration.html); file system configurations; root CA.
- Who runs it: vendor hosts. Status: GA (October 2025; over six months old as a date). 22 Regions.

**C95. AgentCore Browser**
- What: "provides a secure, isolated browser environment for your agents to interact with web applications." Choose "the AWS managed Browser (aws.browser.v1)" or "a custom browser". Sessions "default: 15 minutes, maximum: 8 hours". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html
- Who runs it: vendor hosts; developer drives it with Playwright, Nova Act, Strands or browser-use. Status: GA. 22 Regions.

**C96. Browser: Live View**: "powered by AWS DCV. Each browser session launches a dedicated DCV server". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-dcv-integration.html

**C97. Browser: Session Recording and Replay**: "automatically captures browser interactions and stores them in your specified Amazon S3 bucket". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-session-recording.html

**C98. Browser: CloudWatch metrics** (nav item). https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-metrics.html

**C99. Browser: CAPTCHA reduction with Web Bot Auth**: "reduces CAPTCHA challenges through Web Bot Auth, a draft IETF protocol". Status **Preview**: "Amazon Bedrock AgentCore Browser Web Bot Auth (Preview) is based on the draft IETF Web Bot Auth protocol". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-web-bot-auth.html

**C100. Browser extensions**: "allow you to install custom extensions into browser sessions at session creation time." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-extensions.html

**C101. Browser profiles**: "enable you to persist and reuse browser profile data across multiple browser sessions." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-profiles.html

**C102. Browser proxies**: "supports routing browser traffic through your own external proxy servers." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-proxies.html

**C103. Browser enterprise policies**: "control browser behavior using the Chromium enterprise policy mechanism." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-enterprise-policies.html

**C104. Root Certificate Authority (Browser and Code Interpreter)**: "you must provide your custom root CA certificates when starting a session", retrieved "from AWS Secrets Manager". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-root-ca-certificates.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-root-ca-certificates.html

**C105. Browser OS action (InvokeBrowser)**: "provides direct operating system-level control over Amazon Bedrock AgentCore Browser sessions". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-invoke.html. Released April 2026 (over six months old, possibly stale).

**C106. AgentCore Web Search (InvokeWebSearch API)**
- What: "lets you search the web from your own code with the InvokeWebSearch API." "You don't create or manage any resources to use it." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/web-search-api.html. PrivateLink supported: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/web-search-api-privatelink.html
- Who runs it: vendor hosts; developer calls it from own code. Released November 2026; 6 Regions. No preview label on the page.

### 2.8 Observability (navigation: "Observe, trace, and audit agents")

**C107. AgentCore Observability**
- What: "trace and audit your agents in production across three pillars: tracing and telemetry, metrics and monitoring, and audit logging." "AgentCore emits telemetry data in a standardized OpenTelemetry (OTEL)-compatible format". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html. Concepts: sessions, traces, spans. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html. Service-provided data per component: Runtime, Memory, Payments, Gateway, Built-in tools, Identity, Policy. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html
- Who runs it: vendor emits to Amazon CloudWatch; developer instruments agent code: "you need to instrument your code using the AWS Distro for Open Telemetry (ADOT) SDK." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html
- Status: GA. 22 Regions.

**C108. Cross-account monitoring**: "use Amazon CloudWatch cross-account observability to monitor Amazon Bedrock AgentCore resources across multiple AWS accounts from a single monitoring account." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-cross-account.html. Released April 2026 (over six months old, possibly stale).

### 2.9 Policy in AgentCore (navigation: "Policy in AgentCore: Control Agent Interactions")

**C109. Policy in AgentCore**
- What: "enables developers to define and enforce security controls for AI agent interactions with tools by creating a protective boundary around agent operations." "Policy in AgentCore intercepts all agent traffic through Amazon Bedrock AgentCore Gateways and evaluates each request against defined policies in the policy engine". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html
- Who runs it: vendor hosts; developer writes policies. Depends on: AgentCore Gateway.
- Status: GA, release notes March 2026 "AgentCore Policy is now Generally Available" (over six months old, possibly stale as a date). 22 Regions.

**C110. Policy engine**: "the core component of Policy in AgentCore that stores and evaluates Cedar policies." "The engine enforces default-deny and forbid-wins semantics automatically." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-core-concepts.html

**C111. Policy languages: Cedar and Dogwood**: "Dogwood is an open-source policy language on the Dogwood Policy website that is compatible with Cedar: every valid Cedar policy is also a valid Dogwood policy". The docs' advice: "Write Dogwood." Same URL. (Prior knowledge of AgentCore Policy described Cedar only; the page now adds Dogwood. The page wins.)

**C112. Policy authoring service (natural-language policies)**: "automatically converts natural language authorization requirements into Cedar policies." Same URL; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-natural-language.html

**C113. Guardrails in policies**: "a policy's decision depends on whether request or response content holds unsafe material ... Today guardrails are backed by Amazon Bedrock Guardrails." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-guardrails-in-policies.html. Released July 2026.

**C114. Temporal policies and policy sessions**: "policies whose decisions depend on the history of an agent's actions within a session". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-temporal.html. "A policy session is a sequence of related Gateway invocations grouped under one session ID". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-core-concepts.html

**C115. Policy enforcement modes (LOG_ONLY, ENFORCE)**: "In LOG_ONLY mode, the policy engine evaluates and logs ... without enforcing the decision". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-enforcement-modes.html

**C116. Policy validation and analysis (automated reasoning)**: "Semantic validation uses automated reasoning to detect potential security and logic issues". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-validation-overview.html

### 2.10 AgentCore Evaluations (navigation: "AgentCore Evaluations")

**C117. AgentCore Evaluations**
- What: "provides automated assessment tools to measure how well your agent or tools perform specific tasks". "traces from these agents are converted to a unified format and scored using LLM-as-a-Judge techniques". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html. Can evaluate agents "hosted under AgentCore Runtime as well as AI agents hosted outside of AgentCore." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/how-it-works-evaluations.html. Supported frameworks nav: Strands Agents, LangGraph, OpenAI Agents, Vercel AI SDK, LlamaIndex, Google ADK, Claude Agent SDK, generic.
- Who runs it: vendor hosts. Depends on: Observability traces with Transaction Search.
- Status: GA, release notes March 2026 (over six months old, possibly stale as a date). 22 Regions.

**C118. Built-in evaluators**: "pre-configured evaluators ... use predefined evaluator models and prompt templates". IDs like "Builtin.Helpfulness". "cannot be modified". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/built-in-evaluators-overview.html

**C119. Skill evaluators**: "two built-in evaluators for agents that use skills" (Builtin.SkillSelectionAccuracy and skill instruction following). https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/skill-evaluators.html. Released August 2026.

**C120. Insight evaluators and Failure analysis**: "Insight evaluators are built-in evaluators that explain agent behavior instead of only scoring it." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/insight-evaluators.html. "The failure analysis evaluator (Builtin.FailureAnalysis) tells you what went wrong in your agent sessions". "Currently, only the batch evaluation APIs support it." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/builtin-failure-analysis.html. Status: release notes July 2026 "Failure Insights is now in Public Preview"; October 2026 "Failure analysis insights for batch evaluations". The pages carry no preview label.

**C121. Third-party evaluators**: "offers evaluators from the DeepEval and AutoEval open source libraries." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/third-party-evaluators.html. Released August 2026.

**C122. Custom evaluators (LLM-as-a-judge, multi-dimension, code-based)**: "allow you to define your own evaluator model, evaluation instruction and scoring schemas." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/custom-evaluators.html. Multi-dimension "rates one target on several named dimensions in a single judge call." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/multi-dimension-evaluators.html. Code-based: "use your own AWS Lambda function". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-based-evaluators.html. Developer builds these.

**C123. Online evaluation**: "continuously monitors the quality of deployed agents using live production traffic." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-types.html

**C124. On-demand evaluation (with ground truth)**: "evaluate specific agent interactions by directly analyzing a chosen set of spans." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/on-demand-evaluations.html. Ground truth: "you provide reference inputs alongside your session spans when calling the Evaluate API." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/ground-truth-evaluations.html

**C125. Batch evaluation (with insights)**: "runs evaluators against multiple agent sessions in a single job with server-side orchestration." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/batch-evaluations.html. Insights in batch: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/batch-evaluations-insights.html. Status: GA ("Batch Evaluations is now Generally Available", July 2026).

**C126. Dataset evaluation (dataset runners)**: "a dataset runner orchestrates the entire lifecycle in a single call: invoke the agent, wait for telemetry ingestion, and evaluate." Status **Preview**: "Dataset evaluation is in public preview." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/dataset-evaluations.html

**C127. Simulation (user simulation)**: "Simulation lets you evaluate your agent against dynamic, multi-turn conversations generated by LLM-backed actors." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/simulation.html. "User simulation invokes Amazon Bedrock models on the SDK side". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/user-simulation.html. No label on the page; the Python SDK marks `SimulationConfig` as preview.

**C128. Diagnose with AI assistant (Evaluation Diagnostic Skill)**: "The skill is a markdown file that works with any AI coding assistant." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/diagnose-evaluation-issues.html

### 2.11 AgentCore optimization (navigation: "AgentCore optimization")

**C129. AgentCore optimization**
- What: "provides tools to continuously improve your agent's performance through data-driven configuration changes." "builds on AgentCore Evaluations and introduces three capabilities: Recommendations ... Configuration bundles ... A/B testing". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/optimization.html
- Who runs it: vendor hosts. Status: public preview April 2026; Recommendations and A/B Testing GA July 2026. 21 Regions (not GovCloud).

**C130. Configuration bundles**: "a versioned, immutable snapshot of your agent's dynamic configuration", covering system prompts, model IDs, tool descriptions and "any other key-value pairs your agent reads at runtime". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/configuration-bundles.html. Runtime use "requires bedrock-agentcore-sdk-python version 1.8 or later." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/configuration-bundles-runtime.html. No separate GA statement found.

**C131. Recommendations (system prompt, tool description)**: "Recommendations use AI to generate optimized agent configurations from real session traces." "Recommendations are generated by LLMs. Review and test before applying them." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/optimization-recommendations.html. GA July 2026.

**C132. A/B testing (target-based, configuration bundle, external agents)**: "A/B testing splits live production traffic between two variants and continuously evaluates performance with statistical significance. The AgentCore Gateway handles traffic routing". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/ab-testing.html. External agents: "You can A/B test an agent hosted outside AgentCore Runtime, for example on AWS Lambda, Amazon EKS, or Amazon ECS." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/ab-testing-3p-agents.html. GA July 2026.

**C133. AgentCore insights (being retired)**: Status **Preview, being shut down**: "AgentCore insights is in public preview." and "Beginning October 16, 2026, Amazon Bedrock AgentCore insights no longer supports creating new batch or recurring insights. ... Beginning October 31, existing recurring insights will also stop generating reports." Replacement is Insights in batch evaluation (C125). https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/insights.html

### 2.12 AWS Agent Registry (navigation: "AWS Agent Registry: Centrally catalog and discover AI Resources")

**C134. AWS Agent Registry**
- What: "a fully managed discovery service that provides a centralized catalog for organizing, curating, and discovering resources across your organization." Publish "MCP servers, tools, agents, agent skills, and custom resources". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html
- Who runs it: vendor hosts; publishers and curators are the developer's organization. Registered resources may run "on AWS, On-Prem or on any other Cloud environment" (overview table).
- Status: GA, release notes August 2026 "AWS Agent Registry is now generally available". Public preview April 2026. Namespace change: "Support for the public preview bedrock-agentcore namespace will be discontinued on October 30, 2026." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-key-capabilities.html. 10 Regions.

**C135. Registries and registry records (with record types and custom metadata schema)**: "AWS Agent Registry is organized around two core resources: Registries ... Registry records". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html. MCP and A2A records are validated "against the MCP and A2A protocol schemas". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-key-capabilities.html

**C136. Curation and approval workflow (record lifecycle, review, deprecation, notifications)**: lifecycle "DRAFT → Submit → PENDING_APPROVAL → Approve → APPROVED" (doc's arrows). https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-record-lifecycle.html. "As a curator, you review records in Pending Approval status". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-reviewing-records.html

**C137. Discovery: hybrid search, catalog browsing, Registry MCP endpoint**: search via "the SearchDiscoverableRegistryRecords data-plane API" (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-search-records.html). "Each registry exposes an MCP-compatible endpoint following the 2025-11-25 specification". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-mcp-endpoint.html

**C138. Synchronize records from external sources**: "can automatically synchronize record metadata from external sources by connecting to the provided URL with outbound credentials." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-sync-records.html

**C139. AWS Organizations auto-detection**: AgentCore Runtimes and Gateways "in your organization's member accounts are automatically cataloged as registry records". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-organizations.html

**C140. Cross-account sharing with AWS RAM**: "You can share an AWS Agent Registry registry with other AWS accounts using AWS Resource Access Manager (RAM)." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-cross-account-sharing.html

**C141. Notifications (Amazon EventBridge)**: "emits Amazon EventBridge events for registry-record approval-workflow transitions and for registry provisioning and lifecycle transitions." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-eventbridge.html

**C142. Registry PrivateLink, CloudTrail, KMS encryption, cross-region inference, service-linked roles** (nav items). https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-privatelink.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-data-protection.html

### 2.13 Security (navigation: "Security"), cross-cutting

**C143. VPC and AWS PrivateLink**: "You can use Amazon Virtual Private Cloud (Amazon VPC) and AWS PrivateLink to create private connections between your VPC and Amazon Bedrock AgentCore." Covers interface endpoints, Gateway VPC egress, VPC Lattice, Runtime and tools VPC config, condition keys. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html

**C144. Resource-based policies**: "control which principals ... can invoke and manage your Amazon Bedrock AgentCore resources (supported for Runtime, Gateway and Memory)." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/resource-based-policies.html

**C145. Cross-region inference (Memory, Policy, Evaluations)**: these services "will automatically select the optimal region ... to process your inference request". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/cross-region-inference.html

**C146. IAM integration, managed policies, service-linked roles, condition keys, confused deputy prevention, compliance validation, disaster recovery, tagging** (nav items under Security and "Tagging resources"). https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security-iam.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/disaster-recovery-resiliency.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/tagging.html. Release notes: SOC compliance (July 2026), ISO and CSA STAR (February 2026, over six months old).

---

## 3. What the developer must bring

| Item | Quote | URL |
|---|---|---|
| Agent code and framework (Runtime path) | "You bring agent code - written in any framework or no framework - wrap it with the AgentCore SDK's BedrockAgentCoreApp entrypoint, package it into an ARM64 container, push it to Amazon ECR, and deploy. The orchestration loop is yours." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-vs-runtime.html |
| Configuration (harness path) | "You declare what the agent is (model, system prompt, tools, memory, limits) as configuration, and AgentCore runs the loop." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-vs-runtime.html |
| A server that meets the service contract | "the standardized communication protocol that your agent application must implement" ; "Platform: ARM64 container" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-service-contract.html ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-http-protocol-contract.html |
| Container image or zip, and ECR | "Build and push a container image to Amazon ECR directly or via the AgentCore SDK" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html |
| Model choice and provider credentials | Runtime "works with any Large Language Model"; examples pass an OpenAI "api_key" and "GOOGLE_API_KEY" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/using-any-model.html |
| System prompt and tools | harness: "Specify a model, system prompt, and tools inline." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html |
| Client-side tool code | inline functions: "The harness pauses when the tool is called and returns the call to your code" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-tools.html |
| Session IDs | "Generate a unique session ID for each user conversation" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html |
| Identity provider for inbound OAuth | "End users authenticate with your identity provider (Amazon Cognito, Okta, Microsoft Entra ID)" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html |
| OAuth clients / API keys for third-party services | credential provider "stores the endpoint configuration and credentials" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/resource-providers.html |
| IAM execution roles | harness SDK prerequisite: "an IAM execution role the harness can assume" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-get-started.html |
| Gateway targets and auth | "Set up inbound authorization ... Set up at least one target for your gateway. Set up outbound authorization" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-prerequisites.html |
| Hosting for integration templates | "Set up hosting for the server yourself." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-integrations.html |
| Interceptor code | interceptors "run custom code during each invocation of your gateway" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-interceptors.html |
| Observability instrumentation | "you need to instrument your code using the AWS Distro for Open Telemetry (ADOT) SDK" ; enable "Transaction Search in CloudWatch (one-time per account)" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-operations.html |
| Evaluation prerequisites | "An agent built with a supported framework and instrumentation library" ; "Amazon Bedrock access with model invocation permissions (required when using a custom evaluator)" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-prerequisites.html |
| Custom evaluator logic | code-based evaluators: "use your own AWS Lambda function" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-based-evaluators.html |
| Policies | "developers can create policy engines, create and store deterministic policies in them and associate policy engines with gateways" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html |
| Memory strategy pipeline (self-managed) | "build custom memory processing workflows while leveraging Amazon Bedrock AgentCore for storage and retrieval" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-self-managed-strategies.html |
| Bedrock capacity for custom memory strategies | "it consumes your allocated capacity and is subject to your Bedrock service quotas" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/bedrock-capacity.html |
| Wallet provider and Marketplace subscription (payments) | "you must subscribe to the Coinbase Wallets for AgentCore Payments listing in AWS Marketplace" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-marketplace-subscription.html |
| S3 buckets for browser extensions, recordings, enterprise policies | "You provide a list of browser extension ZIP files stored in your own Amazon S3 buckets" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-extensions.html |
| Capacity provider (Instances) | "You define the compute with a capacity provider, which specifies the operating system, allowed instance types, networking, and storage." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html (August 2026) |
| Cross-Region memory replication | "Memory keeps its data in one AWS Region ... unless you replicate it." | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/disaster-recovery-memory.html |
| Knowledge base data sources | Managed KB connectors ingest from "Amazon S3, SharePoint, Confluence, Google Drive, OneDrive, and Web Crawler" | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html (July 2026) |

---

## 4. How the pieces connect

**4.1 Overview diagram** (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/agentcore_all_components_final.png, on the overview page). Labels, transcribed:
- Title: "Amazon Bedrock AgentCore. Fully modular, secure and serverless agentic AI platform"
- Top box "Agents and tools": "Any framework", "Any model", "All popular protocols". Tab: "AgentCore native resources".
- **Build**: "Built-in tool: Browser. Interact with the web and internal domains using secure headless browsers." / "Built-in tool: Code interpreter. Execute code securely across multiple languages in sandbox environments." / "Gateway. Connect agents to tools and data using API, Lambda and MCP targets." / "Identity. Manage agent access across AWS and 3P resources." / "Memory. Maintain context across interactions." (chips: Short-term, Long-term, Semantic memory strategy, User preference memory strategy, Summary strategy) / "Policy. Establish cross-organization governance policies." (chips: Policy engine, Deterministic tool policies) / "Payments. Automate agent micro-transactions to pay for APIs and MCPs." / "Registry. Centralized way to discover and manage AI resources." (chips: Agents, MCP Servers, Tools, Skills, Custom resources)
- **Deploy**: "Runtime. Host agents and tools using any framework and any model on secure, serverless infrastructure." (chips: Isolated sessions, Serverless endpoints, Embedded identity, MCP & A2A Compatible, Low cold start, Rapid deployment, Long-running async execution)
- **Assess**: "Observability" (Sessions, Traces, Spans, Errors, Latency) / "Evaluations" (Batch evaluations, Online evaluation configurations, Custom evaluators) / "Refinements. Improve your agentic application" (Recommendations, A/B tests)
- Note: the diagram does not show Harness, Web Search, Web Answer, or Managed Knowledge Bases.

**4.2 Harness architecture diagram** (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html). Top: "AgentCore harness: CreateHarness, InvokeHarness", with arrows down to four boxes: "Models" (Bedrock, direct APIs to Anthropic, OpenAI, Gemini, LiteLLM), "Tools" (MCP server, AgentCore gateway and policy, AgentCore browser, AgentCore code interpreter, Web search, Inline functions), "Memory" (Short and long-term, Managed by default, Bring you own memory [sic]), "Skills" (AWS skills, Git source, S3 source, Container-baked). Layers below: "AgentCore runtime" (Firecracker microVM; Filesystem: managed session storage or bring your own (S3 Files, EFS); Default environment or bring your own container; Shell commands), "AgentCore identity" (Inbound/Outbound authentication; OAuth; API keys), "AgentCore observability" (CloudWatch traces, Logs, Metrics, Unified harness view), "AgentCore evaluations & optimization" (Built-in & custom evaluators, A/B testing, Recommendations, Versioning & endpoints).

**4.3 Runtime request flow** (implementation overview, https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html), quoted steps: "Define your agent logic using any AI framework or custom code"; "Build and push a container image to Amazon ECR"; "Create an AgentCore Runtime using the container image"; "The initial version (V1) and DEFAULT endpoint are created automatically"; "Generate a unique session ID for each user conversation"; "Call the InvokeAgentRuntime or InvokeAgentRuntimeWithWebSocketStream operation with your agent's ARN and session ID"; "Use the same session ID for follow-up interactions to maintain context"; "Control rollout by updating endpoints to point to new versions". Each session "Runs in a dedicated microVM" and "Session state is ephemeral and should not be used for long-term durability (use AgentCore Memory for context durability)".

**4.4 Inbound auth to workload token to outbound credentials** (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/get-workload-access-token.html): "Runtime validates the inbound identity provider OAuth token (issuer, signature)"; "Runtime extracts issuer and sub claims"; "Runtime fetches the associated workload identity of the agent"; "Runtime invokes GetWorkloadAccessTokenForJWT with both user identity and agent workload identity"; "Runtime passes the workload access token to agent code as part of the invocation payload header". The agent then uses that token with an outbound credential provider; "AgentCore Identity manages these credentials securely, preventing credential exposure in your agent code or logs." (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html)

**4.5 Gateway request path, with WAF, interceptors and Policy.**
- WAF first: "A client sends a request to your gateway endpoint. AWS WAF evaluates the request ... If the request is allowed, the gateway routes it to the appropriate target." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-waf.html
- Inbound authorizer (OAuth JWT, IAM SigV4, authenticate only, none). https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-core-concepts.html
- "The REQUEST interceptor gets invoked before gateway makes a call to the target". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-interceptors-types.html
- Policy: "The Gateway extracts information from both sources [JWT token and MCP tool call] and constructs a Cedar authorization request" with principal, action, resource, context. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-authorization-flow.html. "For every tool invocation, the policy engine evaluates all applicable policies". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-core-concepts.html
- Target dispatch by category: MCP targets aggregated into "a single unified virtual MCP server"; HTTP targets forwarded "without aggregation or protocol translation"; inference targets routed by "the model field in the request". Outbound credentials come from the execution role (Smithy, Lambda) or an AgentCore credential provider (OpenAPI, MCP server). https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-core-concepts.html

**4.6 Memory flow** (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html, https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-strategies.html): agent writes events with `CreateEvent` (short-term); configured strategies "are automatically executed on raw conversation events associated with that memory resource to extract long-term memories"; built-in strategy steps are "Extraction", "Consolidation", "Reflection" (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/built-in-strategies.html); the agent retrieves with `RetrieveMemoryRecords`. Memory overview diagram labels: "Agents without memory" vs "Agents with memory enabled"; "User, Interact with, Agent, Write, Memory, Read, Response with contextual awareness". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html

**4.7 Payment flow** (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-how-it-works.html), steps named: "Tool invocation" (through Gateway or direct), "Payment required" (HTTP 402), "Payment limit check", "Payment signing" ("retrieves wallet credentials from AgentCore Identity"), "Retry with payment" (`X-PAYMENT` header), "Verification and settlement" (on-chain), "State update". MPP variant uses "WWW-Authenticate: Payment" and the "Authorization header".

**4.8 Optimization loop** (diagram on https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/optimization.html): "Recommendations: Analyze agent traces, Generate optimized prompts and tool descriptions" → "Configuration Bundles (optional): Version the change as an immutable snapshot" → "A/B Testing: Split traffic between control and treatment, Measure with statistical significance" → "Deploy Winner: Route 100% traffic to winning variant", with a return arrow "Monitor traces, re-optimize as needed". Text: "Point the Recommendations API at agent traces in CloudWatch Logs and specify the evaluator you want to optimize for." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/optimization-how-it-works.html. Bundles reach agent code because "The gateway and runtime pass the bundle reference through W3C baggage headers". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/configuration-bundles-runtime.html

**4.9 Evaluation data path**: "traces from these agents are converted to a unified format and scored using LLM-as-a-Judge techniques". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html. Online evaluation reads live traffic through Observability; batch evaluation "handles session discovery, span collection, and scoring entirely on the service side". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/batch-evaluations.html

**4.10 Browser session flow** (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html): "Create a Browser Tool" → "Start a browser session" → "Interact with the browser" via "WebSocket-based streaming APIs" (Automation endpoint; Live View endpoint) → "Monitor and record sessions". Diagram alt text: "Architecture showing the built-in tools offering and Browser and CI tools." (image not transcribed).

**4.11 Harness vs Runtime responsibility split** (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-vs-runtime.html): "Harness - configuration, no code. Runtime - you write code, usually with the AgentCore SDK plus your framework." Grid entries where the harness says "No": "Choice of agent framework", "Bidirectional streaming", "Non-agent-loop patterns (graph, workflow style)".

---

## 5. Limits and gaps the documentation itself states

**Regions** (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html, 22 Regions in the table including AWS GovCloud (US-West)):
- All 22: Runtime microVMs, Gateway, Identity, Built-in Tools, Observability, Policy, Evaluations.
- Harness and Memory: 16 (not N. California, Milan, Spain, Malaysia, Hyderabad, Thailand).
- Optimization: 21 (not GovCloud).
- Payments: 12 (not N. California, Malaysia, Mumbai, Hyderabad, Thailand, Tokyo, Seoul, Canada Central, São Paulo, GovCloud).
- AWS Agent Registry: 10.
- Runtime Instances: 9.
- Web Search Tool: 7. Web Search API: 6. Web Answer: 1 (US East N. Virginia).
- Runtime platform V2: 10 Regions (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html).

**Quotas** (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/bedrock-agentcore-limits.html), selected:
- Harness: "harness invocations are bound by the same service quotas that apply to AgentCore Runtime."
- Runtime: max hardware per session "2vCPU/8GB" (not adjustable); Docker image "2 GB"; request timeout "15 minutes"; payload "100 MB"; streaming max duration "60 mins"; async job max "8 hours (microVMs), 14 days (Instances)"; idle session timeout 15 minutes; max session 8 hours; session storage "1 GB"; active session workloads "5,000 in US East (N. Virginia) and US West (Oregon), and 2,500 in other AWS Regions"; new session creation "25 TPS"; env vars "4 KB"; agents per account 1,000.
- Memory: 150 memory resources per Region; 6 strategies per memory; long-term extraction 150,000 tokens per minute; event expiration 7 to 365 days.
- Identity: 11,000 workload identities; 50 OAuth2, 50 API key, 50 payment credential providers.
- Gateway: 1000 gateways; 100 targets per gateway; 1000 tools per target; invocation timeout 15 minutes; tool-call rate 200 TPS; search-based tool-call "25 transactions per minute"; Web Search Tool and Web Answer "10 transactions per second".
- Browser: 1000 concurrent sessions; "1vCPU/4GB" per session; 10 GB disk; 1 automation stream and 1 live view stream per session.
- Code Interpreter: 1000 concurrent sessions; "2vCPU/8GB"; 10 GB disk; 15 min synchronous timeout.
- Evaluations: "Evaluators per on-demand evaluation | 1"; 25 evaluators per online configuration; batch: 5 active, 500 sessions per job, 10 evaluators per job.
- A/B testing: "Maximum AB tests per gateway | 1"; "Treatments per AB test | 2" (control and one treatment).
- Recommendations: 20 sessions sampled per recommendation; prompt size 20,000 characters.
- Policy: 1,000 policies per engine; "Temporal policies per policy engine | 20"; max temporal window "24 hours"; Cedar schema "400 KB".

**Things the docs say it does not do, or that the developer must handle:**
- Runtime session state: "Session state is ephemeral and should not be used for long-term durability (use AgentCore Memory for context durability)". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html
- Harness does not support choice of framework, bidirectional streaming, or graph/workflow-style patterns (grid, https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-vs-runtime.html).
- Memory is single-Region: "keeps its data in one AWS Region". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/disaster-recovery-memory.html
- Memory without strategies extracts nothing: "If no strategies are specified, long-term memory records will not be extracted". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-strategies.html
- Built-in evaluators "cannot be modified". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/built-in-evaluators-overview.html
- Failure analysis: "Currently, only the batch evaluation APIs support it." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/builtin-failure-analysis.html
- Multi-dimension evaluators "aren't supported in A/B tests or recommendations" (release notes October 2026).
- HTTP gateway targets "do not support capability synchronization or semantic tool search". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-targets-http.html
- Integration templates: AgentCore "supports a subset of APIs that the provider supports" and the developer must host the server. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-integrations.html
- Gateway synchronous tool calls limited by "the 15-minute gateway invocation timeout" without MCP tasks. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-mcp-tasks.html
- Policy LOG_ONLY risk: "every tool call succeeds regardless of forbid policies", and "No separate action or condition key protects the mode field beyond bedrock-agentcore:UpdateGateway". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-enforcement-modes.html
- Policy natural-language authoring may process prompts outside the originating Region within the geography. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-natural-language.html
- Recommendations: "Review and test before applying them." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/optimization-recommendations.html
- Web Bot Auth: "Not all websites will recognize or allow signed agent traffic". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-web-bot-auth.html
- Registry MCP endpoint "returns record metadata as publishers provide it" and must be validated before acting. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-mcp-endpoint.html
- Stateful MCP guide applies "to MCP protocol version 2025-11-25 and earlier"; version 2026-07-28 "removes" server-initiated elicitation and sampling. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/mcp-stateful-features.html
- FUSE mounts: "available only for agent runtimes on platform version V2." https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-fuse-mounts.html
- WebRTC "requires: VPC network mode". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-webrtc.html
- V2 create/update "run for several minutes", and the container "must report healthy within 120 seconds". https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html
- Deprecations: AgentCore insights job creation ended October 16, 2026, reports stop October 31, 2026 (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/insights.html); the Registry preview namespace `bedrock-agentcore` discontinued October 30, 2026 (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-key-capabilities.html).

**Features still labeled preview on their pages (as of 2026-11-11):** Amazon Bedrock Managed Agents (with OpenAI); Runtime managed session storage; Browser Web Bot Auth; Dataset evaluation; AgentCore insights (and being retired); some Python SDK evaluation and simulation classes.

---

## 6. Not found, or could not confirm

- **Payments GA in the Developer Guide.** The What's New post (Aug 18, 2026) says GA; the Developer Guide release notes have no payments GA entry, and the payments pages carry no label. Searched: full text of `release-notes.html` for "payments"; WebSearch `"AgentCore payments" generally available site:aws.amazon.com`.
- **Exact harness GA date.** What's New says Jun 17, 2026; the release notes file it under "July 2026". Not reconciled.
- **Payments preview date.** What's New URL path is `/2026/04/`; the release notes list it under May 2026. Not reconciled.
- **Day-level date of the latest doc change.** The release notes give months only; the RSS feed URL I tried (`bedrock-agentcore-release-notes.rss`) returned an HTML stub, not a feed. I used the HTTP `Last-Modified` header (11 Nov 2026), which may reflect a site rebuild rather than a content edit.
- **Status of configuration bundles, Gateway rules, Memory gateway connector, Web Search API, Simulation as separate GA statements.** No GA or preview label on these pages and no specific GA release note. [no-record: separate GA statement searched=597 Developer Guide pages (grep "preview", "generally available"), release-notes.html]
- **Managed Knowledge Bases region list.** Not in the AgentCore region table; creation is documented in the Amazon Bedrock User Guide, which I did not read.
- **Diagram content for Browser, Payments personas, and Browser proxy flow.** I transcribed the overview, harness, optimization and memory diagrams only; other images are listed by alt text.
- **Pricing details.** Out of scope; the overview points to https://aws.amazon.com/bedrock/agentcore/pricing/ (not read).
- **Prior-knowledge disagreements:** my prior knowledge did not include Harness, Payments, Optimization, Registry, Web Search/Web Answer, Instances, platform V2, or Dogwood; the pages describe all of them, so the pages win. My prior knowledge described Policy as Cedar-only; the page now recommends Dogwood.
