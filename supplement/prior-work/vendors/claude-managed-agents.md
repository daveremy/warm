---
title: "Claude Managed Agents, self-hosted: mapping to the 25 WARM platform services"
date: 2026-11-12
author: "independent reader (Claude agent, model claude-fable-5-2)"
product: "Claude Managed Agents, self-hosted (Anthropic)"
product_version: "No version number is published on the vendor's pages (it is in the release archive's name, which is not public). Newest release-notes entry seen: November 12, 2026, the launch of self-hosted Claude Managed Agents."
protocol: "prior-work/vendors/protocol-v2.md; C1 to C4 from prior-work/rerate-criteria-v2.md"
status: "not yet checked by sagan"
---

# What was rated

The product is the form of Claude Managed Agents that a customer runs on its own infrastructure: the server (`cma-server`), its PostgreSQL database, workers and sandboxes, the console on the server, and the admin CLI. The hosted service that Anthropic runs is not rated. Each row's reason says where the two differ.

Availability, for every row unless the row says otherwise: access on request ("To request access to self-hosted Claude Managed Agents, contact your Anthropic account team."), launched November 12, 2026, and Managed Agents as a whole "is in beta". The vendor's pages do not use the words "private beta".

How the general pages were used: the self-hosted overview says "Both have the same API, so the SDK and the `ant` CLI work with your server, and the rest of the Managed Agents documentation applies." and names the differences page as the list of exceptions. A row that quotes a general Managed Agents page was checked against the differences page first.

All pages were read on 2026-11-12. Base URL for the short page names below: `https://platform.claude.com/docs/en/managed-agents/`.

# The 25 services

| Service | Value | Quote | URL | Availability | Reason, and difference from the hosted service |
|---|---|---|---|---|---|
| Harness | yes | "**Server (`cma-server`):** Serves the API, runs the agent loop, and stores agents, sessions, and each session’s history." | https://platform.claude.com/docs/en/managed-agents/self-hosted | on request; beta | The customer's server runs the loop and compaction; workers run the shell and file tools. Hosted: Anthropic runs the loop. |
| Sessions | yes | "Sessions and their history stay in your database until you delete them." | https://platform.claude.com/docs/en/managed-agents/self-hosted-data-and-access | on request; beta | Sessions pause (`idle`), resume on the next `user.message`, archive and delete. History is in the customer's PostgreSQL; with no database a restart erases it. Hosted: Anthropic stores history and checkpoints the sandbox for 30 days. Here the Compose sandbox and its files go about a minute after a turn; on Kubernetes the `/workspace` volume stays. |
| Tasks | part. DISPUTABLE (yes) | "The session acts as a state machine that tracks progress, and events drive the actual execution." | https://platform.claude.com/docs/en/managed-agents/sessions | on request; beta | The session has statuses, the server retries failed model calls, a turn continues in a new sandbox, `user.interrupt` and a work-item stop cancel, and the request stays in the event history. There is no task record apart from the session, which can hold many requests. Yes is defensible because an outcome (`user.define_outcome`) has an ID, a kept description and result states. Difference: "The session’s status stays `running` between attempts", so the `rescheduling` status never shows. |
| Environments | yes | "The Docker Compose stack and the `cma-sandboxes` Helm chart start each session’s worker in a container or pod of its own." | https://platform.claude.com/docs/en/managed-agents/self-hosted | on request; beta | One sandbox per session (gVisor on Kubernetes, three egress modes). Agents in one multiagent session share the sandbox. No browser. The customer supplies the cluster and secures it. Hosted: Anthropic's cloud sandboxes; here "Only `self_hosted` environments exist." |
| Scheduling | part | "Start sessions from your own scheduler, such as a cron job." | https://platform.claude.com/docs/en/managed-agents/self-hosted/differences | on request; beta | The server limits how much runs at once (`scheduler.max_concurrent_turns`, a work queue per environment, `limits.max_live_subagent_threads`). It starts nothing at a time or on an event. Hosted: scheduled deployments (cron) and webhooks; here "The server has no routes for them." and "The server sends no webhooks". |
| Lifecycle | yes | "In it, you create agents, run sessions, and manage environments, credential vaults, memory stores, and skills, with no SDK or CLI." | https://platform.claude.com/docs/en/managed-agents/self-hosted/console | on request; beta | Agents are created, updated, archived and listed; sessions are created, interrupted, resumed, archived, deleted and listed, through the API, the `ant` CLI or the console. Same API as hosted. |
| Memory | yes | "Every change to a memory creates an immutable **memory version**, giving you an audit trail and point-in-time recovery for everything the agent writes." | https://platform.claude.com/docs/en/managed-agents/memory | on request; beta | Memory stores carry text across sessions; writes produce versions "attributed to the session". On the customer's server "The API is complete. The worker, not the server, copies each attached store into the sandbox and writes changes back." Hosted adds dreams, which rebuild a store from transcripts; here "Dreams have no replacement." |
| Retrieval | yes | "Pre-load a store with reference material before any agent runs:" | https://platform.claude.com/docs/en/managed-agents/memory | on request; beta | Named sources an agent can read: memory stores (read-only or read-write), Git repositories as session resources once the host is on `git.allowed_hostnames`, and MCP servers on `mcp.allowed_hostnames`. Hosted also has file resources and the Files API; here "The server rejects `file` resources, and `/v1/files` doesn’t exist." Web tools are off until a server setting turns them on. |
| Artifacts | part | "Data reaches a session and leaves it through the worker’s working directory." | https://platform.claude.com/docs/en/managed-agents/self-hosted/call-the-api | on request; beta | No output store. On Kubernetes each session keeps a `/workspace` volume; on Compose "Anything a session must keep has to leave through a tool call, such as an upload or a `git push`". Versions exist only for memory-store documents and for branches the agent pushes. Hosted: a session's output files are listed and downloaded through the Files API. |
| Models | part. DISPUTABLE (yes) | "Agents name models by their Claude API IDs, such as `claude-opus-5-5`. The server translates the ID, so an agent definition works unchanged under any provider that serves that model." | https://platform.claude.com/docs/en/managed-agents/self-hosted/inference-provider | on request; beta | The server mediates every model call and sends it to one of five provider settings (Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry, a model gateway). The builder names the model per agent, per session override or per listed subagent; the server does not choose a model for a task, except the refusal fallback under the Claude API. One provider per deployment; Claude models only. Yes is defensible because mediation covers several models and several providers. Hosted: Anthropic inference only; provider choice is a self-hosted-only feature. |
| Tools | yes | "A policy determines whether a tool’s calls run automatically, wait for your approval, or go to the server, which evaluates each call." | https://platform.claude.com/docs/en/managed-agents/permission-policies | on request; beta | The server mediates MCP calls and web tools; workers run `bash` and the file tools; the client answers custom tools. Differences: "The server connects only to the MCP hosts that you list in its settings." and the web tools are off by default and depend on the provider. |
| Registry | yes | "An agent is a reusable, versioned configuration that defines persona and capabilities." | https://platform.claude.com/docs/en/managed-agents/agent-setup | on request; beta | Agents and uploaded skills are stored with versions, listed, and loaded by ID or pinned version; a tool definition is part of an agent version. Difference: the prebuilt `docx`, `pdf`, `pptx` and `xlsx` skills are absent ("Only skills you upload exist."), and skills in a repository's `.claude/skills` are not discovered. |
| Directory | part (derived) | derived from C3 = part and C4 = part; see the answers after the table | n/a | n/a | derived |
| Messaging | part | "The server sends no webhooks, so a worker that starts on a webhook never starts." | https://platform.claude.com/docs/en/managed-agents/self-hosted/differences | on request; beta | Messages pass only between a coordinator and its listed subagents inside one session (`agent.thread_message_sent`, `agent.thread_message_received`). A client receives events only on a stream it opens or by listing them. Hosted: webhooks deliver events to subscribers. |
| Orchestration | part | "An agent can delegate only to subagents that you list. Dynamic workflows, the advisor, and subagents that the agent defines itself aren’t available." | https://platform.claude.com/docs/en/managed-agents/self-hosted/differences | on request; beta | One agent delegates one level down to 1 to 20 listed agents and reads their reports; people enter only through tool confirmations. No fixed steps and no dependencies between assignments. Hosted: dynamic workflows (a program that runs agents in phases) and an advisor model. |
| Channels | part. DISPUTABLE (yes) | "Your code calls it with the official SDK, cURL, or the `ant` CLI." | https://platform.claude.com/docs/en/managed-agents/self-hosted/call-the-api | on request; beta | Requests and results travel over the API, a terminal chat (`ant beta:sessions connect`) and the console web page on the server. No adapter to chat, email or other channels people already use, and no webhooks; the customer builds those on the API. Yes is defensible because applications (API) and people (console, terminal) each have a channel. Hosted: the Claude Console at platform.claude.com, which "doesn’t show what is on your server." |
| Identity | part. DISPUTABLE (yes) | "Your server can sign a short-lived JSON Web Token (JWT) that names an agent, and send it with that agent’s MCP calls." | https://platform.claude.com/docs/en/managed-agents/self-hosted/agent-identity | on request; beta | Single sign-on gives each person or service an identity and a role; an agent token carries `agent_id` and, for a tool call, the session creator in `actor_sub`; archiving the agent stops its tokens. The pages record a creator ("the server records it as part of the creator of each resource"), not an accountable person; a session made with the shared server API key names no person; agent tokens are optional and cover MCP calls only. Yes is defensible if the recorded creator counts as the accountable person. Both features exist only on the customer's server ("Features that only your server has"). |
| Secrets | yes | "With an [environment variable credential](https://platform.claude.com/docs/en/managed-agents/vaults#add-a-credential), an agent’s commands can call a service while the sandbox holds only a placeholder for the secret." | https://platform.claude.com/docs/en/managed-agents/self-hosted/agent-identity | on request; beta | Vault credentials are write-only and injected at the point of use (MCP call, Git request, egress gateway). The secret can live in the customer's secret manager. Differences: `mcp_oauth` credentials are rejected; `environment_variable` credentials need the egress gateway turned on; an external secret manager is a self-hosted-only feature. |
| Policy | part. DISPUTABLE (yes) | "Hosts match exactly, with no wildcards and no subdomains, and the list is empty by default." | https://platform.claude.com/docs/en/managed-agents/self-hosted/differences | on request; beta | Rules decide tool calls (`always_allow`, `always_ask`, `auto`), which MCP, Git and web hosts and which push branches are allowed, what sandboxes can reach, and what each role sees. For stored data the only rule is a retention period for sandbox volumes (`dispatcher.retentionDays`); "The server doesn’t delete a session because of its age". No grant is issued; the decision is recorded as `evaluated_permission` on the event. Yes is defensible on the action and content rules. The self-hosted pages speak of "a call that a policy denies" but do not name the `auto` policy. |
| Approvals | part. DISPUTABLE (yes) | "If a tool call waits for you, its card shows **Approve** and **Deny**." | https://platform.claude.com/docs/en/managed-agents/self-hosted/console | on request; beta | A held call waits for a person's `user.tool_confirmation` (allow or deny, with a message), which is kept in the session's events. Approval in advance exists only as the `always_allow` policy on a tool: no stated conditions and no record of who approved. Yes is defensible if a per-tool policy counts as approval of a class of actions. Same as hosted, except that no webhook announces a waiting call. |
| Observability | yes | "The server records no traces or metrics until you turn them on with the standard OpenTelemetry environment variables." | https://platform.claude.com/docs/en/managed-agents/self-hosted-data-and-access | on request; beta | Every session's events are kept and can be listed or streamed; the server logs to standard error, including the caller of each request; traces and metrics go to an OpenTelemetry collector or a Prometheus endpoint when turned on; the console shows sessions. Hosted: the Claude Console session viewer and Usage pages, which do not show the customer's server. |
| Evaluation | part. DISPUTABLE (yes) | "When you define an outcome, the harness automatically provisions a *grader* to evaluate the artifact against a rubric." | https://platform.claude.com/docs/en/managed-agents/define-outcomes | on request; beta | A grader scores a work product against a rubric and reports `satisfied`, `needs_revision`, `max_iterations_reached`, `failed` or `interrupted`. No result is described as "unknown" for a check that could not run, and the review of agent behavior is a cookbook job the customer runs. Yes is defensible because `failed` ("when the rubric does not apply to the deliverables") and `interrupted` are not verdicts on the work. Difference: "Send the rubric as text. The Files API isn’t available". |
| Improvement | no | Not found. Searched every downloaded page for "improv", "propos", "feedback", "dream", "learn". The only feature of this kind is dreams, about which the differences page says "The server has no routes for them." | https://platform.claude.com/docs/en/managed-agents/self-hosted/differences | n/a | Nothing turns traces or evaluations into proposed changes. Hosted: dreams (research preview) produce a reorganized memory store from past transcripts; that changes memory, not agents or skills. |
| Releases | part. DISPUTABLE (yes) | "This page shows how to upgrade a deployment on Kubernetes or Docker Compose, and how to roll back." | https://platform.claude.com/docs/en/managed-agents/self-hosted/upgrade | on request; beta | Agents and skills have versions and a session can pin one ("stage rollouts of new versions independently"). A platform release is an archive with a `CHANGELOG.md`; the operator installs it and rolls it back with Helm or Compose and a database backup. The server's settings file is not versioned by the product. Yes is defensible because versions and a way back exist for agents, skills and the platform. Hosted: Anthropic releases the service. |
| Reliability | part | "With self-hosted Managed Agents, you run and secure a server, its database, and your sandboxes, and you install each release yourself." | https://platform.claude.com/docs/en/managed-agents/self-hosted | on request; beta | The product supplies mechanisms: the server chart "runs two servers behind a Service", readiness and health endpoints, retried model calls, a turn that continues in a new sandbox, and a documented backup and restore. Keeping the service, the database and the workers available is the customer's work. Hosted: Anthropic operates the service. |

# Four further questions

## 1. Areas of work (C1 to C4)

**C1. An area of work exists in the model: part.**
Quote: "Each deployment serves one tenant at one trust level." (https://platform.claude.com/docs/en/managed-agents/self-hosted-data-and-access#multitenancy)
The model's units are the agent, the environment, the session, the vault and the memory store. None stands for an area of work. The only unit that stands for an organization is the deployment, which is the whole system; to have several, the customer runs separate deployments ("Give each tenant its own deployment, with its own database, server API key, and workers."). The other grouping is one agent with its listed subagents, which is one team of agents ("List 1 to 20 agents in `agents`"). Both cases are named under **part** in the criteria. The hosted service's workspace does not exist on the customer's server.

**C2. The area is specified apart from who does the work: part.**
Quote: "`roles` maps a group to `admin`, `developer`, or `user`. The highest matching role wins." (https://platform.claude.com/docs/en/managed-agents/self-hosted/configure)
Rated on the deployment. It has roles that people fill, defined apart from the people (a group maps to a role), which meets (b) for people only. No page states what a deployment as a whole is for, so (a) is not met. What an agent does is stated per agent (the `description` field: "A description of what the agent does."), not per unit.

**C3. A record of accountability: part.**
Quote: "`name` labels the issuer in log lines, and the server records it as part of the creator of each resource." (https://platform.claude.com/docs/en/managed-agents/self-hosted/configure)
The server keeps, for each agent, session, vault, memory store and skill, who created it, and uses that to decide who sees it. The record names a creator per asset. It does not state accountability and is not per responsibility or capability. A resource created with the server API key has no person as creator.

**C4. Finding where to send work: part.**
Quote: "An agent can delegate only to subagents that you list." (https://platform.claude.com/docs/en/managed-agents/self-hosted/differences)
A coordinating agent knows only the 1 to 20 agents the builder lists in its own definition and decides in its own turn which to call ("You decide which of these the agent can use, and the agent determines when to use them."). No agent can look up a handler from a kind of work, and no directory or broker is defined. Routing exists only inside one orchestrator's logic.

**Directory (derived): part.** C3 and C4 are both part.

## 2. Supplied agents for an area of work

None found for the self-hosted product.

- Prebuilt skills (`docx`, `pdf`, `pptx`, `xlsx`) exist on the hosted service only: "The server rejects an agent that declares them. Only skills you upload exist." The page tells the customer to "Download their sources from the [skills repository](https://github.com/anthropics/skills) and upload them as custom skills." (https://platform.claude.com/docs/en/managed-agents/self-hosted/differences)
- The console offers starting points when an agent is created ("Select a starting point, such as **Blank agent**, and enter a name."), but the page names only the blank one. (https://platform.claude.com/docs/en/managed-agents/self-hosted/console)
- The hosted quickstart links three sample applications (a research analyst, a spreadsheet analyst, a personal finance assistant) in the `anthropics/claude-quickstarts` repository. They are sample code for the hosted service, not agents shipped with the server. (https://platform.claude.com/docs/en/managed-agents/quickstart)

Searched: the 13 self-hosted pages, and the skills, agent setup, onboarding and quickstart pages, for "template", "starting point", "prebuilt" and "pre-built".

## 3. What fits nowhere

- **Session budgets and cost metering.** "A session budget is an optional hard spend ceiling you set when you [create a session](https://platform.claude.com/docs/en/managed-agents/sessions)." (https://platform.claude.com/docs/en/managed-agents/budgets) The session's `usage` reports tokens, active time and list cost. None of the 25 services covers a spending limit; Scheduling covers how much runs at once, not how much it costs. The self-hosted pages neither confirm nor exclude budgets on the customer's server.
- **Usage attribution to the vendor.** "With these headers, Anthropic can attribute usage to a session, an agent, or an environment. No setting turns them off." (https://platform.claude.com/docs/en/managed-agents/self-hosted-data-and-access) This is metering by the vendor of a product the customer hosts, when the Claude API is the inference provider.
- **Tenant separation by deployment.** "Each deployment serves one tenant at one trust level. Environments in one deployment don’t keep trust levels apart." (same page) This is closest to Policy and Identity, but the mechanism is a separate installation, which no service names.

## 4. Where it runs and what the user supplies

**Where the agent runs.** On the customer's infrastructure, with the model elsewhere unless a gateway keeps it in the network: "Self-hosted Claude Managed Agents is Managed Agents on your own infrastructure, which can be a cloud account or an on-premise data center. You host the service and the sandboxes. The model runs at Anthropic or at a provider that you choose." (https://platform.claude.com/docs/en/managed-agents/self-hosted) "Anthropic has no remote access to the server or its log." (https://platform.claude.com/docs/en/managed-agents/self-hosted-data-and-access)

**Whether an agent keeps running when the user is away.** A session runs on the server, not in the client: "To leave the chat, press Ctrl+C in its terminal. The session keeps running." (https://platform.claude.com/docs/en/managed-agents/self-hosted/quickstart) It stops for input it needs: "A paused session waits indefinitely, so an unattended session needs a client that answers paused calls or interrupts the session." (https://platform.claude.com/docs/en/managed-agents/secure-deployment) Nothing starts a session on its own: "Start sessions from your own scheduler, such as a cron job." (https://platform.claude.com/docs/en/managed-agents/self-hosted/differences) A sandbox lasts about an hour: "A container also exits about an hour after it starts, even in the middle of a turn. No setting changes that. The turn continues in a new container". (https://platform.claude.com/docs/en/managed-agents/self-hosted/call-the-api)

**What the user must supply or build for sustained work.**
- The release archive, by request, and the installation: "With self-hosted Managed Agents, you run and secure a server, its database, and your sandboxes, and you install each release yourself." (https://platform.claude.com/docs/en/managed-agents/self-hosted)
- A database: "PostgreSQL 16 or later. Without a database, the server keeps its data in memory, and a restart erases it." (same page)
- For production, a Kubernetes cluster ("Kubernetes 1.30 or later"), a sandboxed runtime, an image registry, and TLS in front of the server. (https://platform.claude.com/docs/en/managed-agents/self-hosted/kubernetes)
- An inference credential (a Claude API key or a cloud provider's credential), and an identity provider if people use the console or sign in ("The console needs single sign-on.").
- Workers that keep polling: "Keep your workers running so that they can poll." (https://platform.claude.com/docs/en/managed-agents/self-hosted/differences)
- Its own scheduler, its own client code to follow event streams and answer tool calls, and its own way to get files in and out of the working directory.
- The agents, skills, memory stores and vault credentials themselves: "Nothing is copied from the hosted service, session history included. Create your agents, skills, vault credentials, and memory stores again on your server." (same page)

# Pages opened (all on 2026-11-12)

All were fetched as Markdown with `curl` (the URL plus `.md`). Code samples were skipped.

Index and changelog:
- https://platform.claude.com/llms.txt (used to list the 53 Managed Agents pages)
- https://platform.claude.com/docs/en/release-notes/overview (searched for "self-hosted"; read the November 12, 2026 entry and the Managed Agents entries it returned)

Self-hosted pages, read in full:
- https://platform.claude.com/docs/en/managed-agents/self-hosted
- https://platform.claude.com/docs/en/managed-agents/self-hosted/differences
- https://platform.claude.com/docs/en/managed-agents/self-hosted-data-and-access
- https://platform.claude.com/docs/en/managed-agents/self-hosted/quickstart
- https://platform.claude.com/docs/en/managed-agents/self-hosted/kubernetes
- https://platform.claude.com/docs/en/managed-agents/self-hosted/call-the-api
- https://platform.claude.com/docs/en/managed-agents/self-hosted/configure (single sign-on)
- https://platform.claude.com/docs/en/managed-agents/self-hosted/console
- https://platform.claude.com/docs/en/managed-agents/self-hosted/agent-identity
- https://platform.claude.com/docs/en/managed-agents/self-hosted/inference-provider
- https://platform.claude.com/docs/en/managed-agents/self-hosted/configuration-reference
- https://platform.claude.com/docs/en/managed-agents/self-hosted/upgrade

General Managed Agents pages, read in full:
- overview, sessions, session-operations, permission-policies, define-outcomes, skills, agent-setup, session-observability, secure-deployment-monitoring, onboarding, self-hosted-sandboxes-security, self-hosted-sandboxes-operations

General pages, read in part (the opening sections, to the length noted):
- memory (about three quarters), multiagent-orchestration (about half, plus the section on the `coordinator` type), session-threads (first half), events-and-streaming (most), tools (most), vaults (first half), reference (event types and rate limits), self-hosted-sandboxes (most), github (most), mcp-connector (first half), budgets (first quarter), secure-deployment (four sections), secure-deployment-risks (most), self-hosted-sandboxes-workers (two sections), self-hosted-sandboxes-memory (opening), quickstart (two sections), dreams (opening), scheduled-deployments (opening), workflow-runs (opening)

General pages, headings and keyword search only:
- self-hosted-sandboxes-reference, self-hosted-sandboxes-custom-tools, choosing-an-environment, migration, files, tools-web-restrictions

Downloaded and not read (features the differences page says are absent on the customer's server, or stream rendering):
- environments (cloud), cloud-sandboxes-reference, webhooks, event-deltas

# Disclosures and what could not be opened

- **The release archive is not public.** I could not open its `operator-guide.md`, `CHANGELOG.md`, `cma-server.example.yaml` or the Helm charts' `values.yaml`, so I saw no product version number and no per-release changelog. The Kubernetes page's `TAG=1.2.3` is an example value.
- **No launch post found.** A web search for a vendor blog or news post on the November 12 launch returned only third-party pages about the May 2026 launch of self-hosted sandboxes (a different, earlier feature). I opened none of them and no cell rests on them. The launch is confirmed by the vendor's release notes.
- **"Private beta" is the brief's wording.** The vendor's pages say access is by request to the account team and that Managed Agents is in beta.
- **General pages describe the hosted service.** Where the differences page is silent (session budgets, the `auto` permission policy, the 30-day retention of memory versions), I took the general page as applying, as the self-hosted overview states, and said so in the row. Outcomes are confirmed for the customer's server by the call-the-API page.
- **Nothing was run.** I did not sign in, did not download the product and did not call its API. Every value rests on documentation, not on observed behavior.
- **Other files in this directory tree.** I opened only `protocol-v2.md` and `rerate-criteria-v2.md`. One command tested whether this output file existed and printed "ABSENT"; no other file's content was printed.
- **Reader and vendor.** The reader is a Claude model, made by the vendor of the product rated.
