---
title: "WARM platform mapping: second-rater spot-check"
date: 2026-11-11
type: platform-mapping-audit
model: warm-model-v0.10.md
inputs: inventory-*.md, mapping-*.md, mapping.md; OpenClaw and AgentCore live docs and the openclaw/openclaw GitHub repository, read 2026-11-11
---

# WARM platform mapping: second-rater spot-check

I am the second rater. I read the WARM v0.10 service definitions (Step 3), assigned each sampled component myself from its inventory entry, and only then compared with the mapper's row. Where an inventory entry was thin I read the platform's page.

## Summary

| Platform | Agree | Disagree | Unclear | Sampled |
|---|---|---|---|---|
| AgentCore | 9 | 2 | 1 | 12 |
| LangGraph / LangSmith | 10 | 1 | 1 | 12 |
| OpenClaw | 10 | 1 | 1 | 12 |
| **Total** | **29** | **4** | **3** | **36** |

| Category (mapper's label) | Agree | Disagree | Unclear |
|---|---|---|---|
| Clean one-service fit | 12 of 12 | 0 | 0 |
| Strained fit or span | 7 of 12 | 3 | 2 |
| Misfit, other layer, builder tooling | 10 of 12 | 1 | 1 |

The clean fits hold. The disagreements sit in strained fits and spans, where the mapper's own confidence was lowest: one generic hook point called Policy, one change feed called Memory, one routing span whose members I would change, and one misfit (AgentCore payments) that I would call a span.

Part 2: OpenClaw's self-learning, Skill Workshop and dreaming each turn evidence from past sessions into applied changes: the first two change learned skills, dreaming changes durable memory (`MEMORY.md`). By default no person approves the change first. Self-learning and Skill Workshop have an opt-in `propose` mode that saves drafts for review, and every skill change can be undone. None of the three pages says the loop edits the agent definition (`AGENTS.md`, `SOUL.md`). The mapper put all three under Memory, marked clear.

Part 3: (a) CONTRADICTED on the start date: the ledger was merged 2026-03-29, and 2026-03-31 is the date of the TaskFlow (ClawFlow) control surface. The removal date and reason are confirmed. (b) CONFIRMED in substance, with each end of the range one day off (2026-07-22 to 2026-10-22). (c) CONFIRMED: AgentCore has no general scheduling component. Two internal timers exist, and neither starts agent work.

## Part 1. Spot-check

### How I picked

For each platform I extracted every row of the mapper's assignment table into a list, in table order (AgentCore C1 to C146; LangGraph 1 to 307; OpenClaw's 373 individual rows, section 1.1; class rows excluded). I split the list by the mapper's label and took evenly spaced rows at positions round(n·k/(m+1)) for k = 1..m, so the first row of a list is never chosen:

- clean fit: (a) one service, confidence "clear", m = 4
- strained or span: (a) one service with confidence "strained", m = 2, plus SPANS, m = 2
- misfit or other: MISFIT, m = 2, plus non-platform layer, m = 1, plus builder tooling, m = 1

The rule picked two LangGraph misfits from the same class (data protection). I kept them so the method stays fixed.

### AgentCore (inventory-agentcore.md, mapping-agentcore.md)

| # | Component | Mapper | Mine | Verdict | Reason |
|---|---|---|---|---|---|
| C48 | Built-in with overrides strategy | Memory (clear) | Memory | agree | Custom instructions and model for memory extraction; this is how Memory keeps what agents learn. |
| C77 | Workload identities and agent identity directory | Identity (clear) | Identity | agree | "the digital identity of your agents"; the directory is a list of identities, not of responsibilities. |
| C105 | Browser OS action (InvokeBrowser) | Environments (clear) | Environments | agree | OS-level control of the agent's browser session is part of the place the agent acts in. |
| C120 | Insight evaluators and failure analysis | Evaluation (clear) | Evaluation | agree | Built-in evaluators that judge sessions; the explanation goes beyond a score but is still assessment. |
| C51 | Memory record streaming | Memory (strained) | Misfit (outbound event feed), or Observability | disagree | It sends create/update/delete notifications to a Kinesis stream for other systems. That is outbound event notification, which the LangGraph mapper treated as a misfit class; nothing in it retains or updates what agents learn. |
| C101 | Browser profiles | Environments (strained) | Environments (strained) | agree | Persisted cookies and logins are state of the agent's browser environment; "strained" is right because the state outlives a session. |
| C28 | Isolated sessions, lifecycle settings, stop session | Spans: Environments, Sessions, Tasks | Spans: Environments, Sessions, Tasks | agree | A microVM per session (Environments), session lifetime (Sessions), and stop/terminate (Tasks cancellation). |
| C75 | Other Gateway features (debug, KMS, custom domains, header propagation, MCP Inspector, CloudTrail, VPC egress) | Spans: Observability, Secrets, Infrastructure | Spans: Observability, Tools, Infrastructure, plus data protection | unclear | The span is right but the members differ: header propagation is tool mediation, and customer-managed KMS encryption of stored data is data protection, which WARM's Secrets (release values at point of use) does not clearly cover. The row is a grab-bag of seven features. |
| C37 | Invoke an agent | Misfit (invocation endpoint) | Misfit | agree | A program calling the agent is neither a person (Human channels) nor agent-to-agent delivery (Messaging); WARM has no place for it. |
| C88 | AgentCore payments | Misfit (payments) | Spans: Tools, Policy, Secrets | disagree | Each part has a WARM home: paying for an API or tool call is part of mediating that call (Tools), payment limits are Policy, wallet credentials are Secrets. The mapper's own C91 already spans Policy and Secrets. An argument for misfit remains: no service is responsible for moving money. |
| C24 | Platform versions (V1, V2) | Infrastructure (strained) | Infrastructure | agree | How the runtime starts the agent (V2 from a snapshot) is a hosting detail beneath Environments. |
| C5 | AgentCore MCP Server | Builder tooling | Builder tooling | agree | It helps a coding assistant "transform, deploy, and test" agents; the agent never uses it. |

### LangGraph, LangSmith Deployment, LangSmith (inventory-langgraph.md, mapping-langgraph.md)

| # | Component | Mapper | Mine | Verdict | Reason |
|---|---|---|---|---|---|
| 55 | LangSmith Observability (pointer) | Observability (clear) | Observability | agree | A pointer to tracing; "Traces are a series of steps that your agent takes". |
| 160 | Sandboxes | Environments (clear) | Environments | agree | "isolated environments that allow agents to safely execute potentially risky operations". |
| 195 | Add metadata and tags to traces | Observability (clear) | Observability | agree | Annotating collected evidence. |
| 239 | Manage evaluators | Evaluation (clear) | Evaluation | agree | Binding evaluators to datasets and trace containers configures assessment. |
| 61 | Actors (PregelNode) | Orchestration (strained) | Orchestration (strained) | agree | A node is a fixed step in a graph; an internal construct of the engine that divides work, so "strained" fits. |
| 128 | Custom middleware | Policy (strained) | Spans: Policy, Observability (or builder extension point) | disagree | The page names "logging request metrics, injecting or checking headers, and enforcing security policies": a generic hook, not a policy evaluator. The AgentCore mapper put the equivalent (C11 lifecycle hooks) as a Policy + Observability span. |
| 60 | LangGraph runtime (Pregel) | Spans: Tasks, Orchestration | Spans: Tasks, Orchestration | agree | It orders steps (Orchestration) and persists each step for durable execution (Tasks). |
| 122 | IAM auth for data stores | Spans: Identity, Secrets | Spans: Identity, Secrets | agree | A workload identity (Identity) yields short-lived database credentials (Secrets). |
| 124 | Encryption at rest | Misfit (data protection) | Misfit | agree | Encrypting stored state with per-tenant keys is protection of stored data; Secrets covers releasing values to components, not encrypting stores. |
| 198 | OpenTelemetry Gateway redaction | Misfit (data protection) | Observability (strained), or misfit | unclear | Redacting sensitive data from traces before they are stored can be read as part of how Observability collects evidence; it can also be read as data protection, which WARM lacks. |
| 144 | Standalone servers | Infrastructure (strained) | Infrastructure | agree | A hosting arrangement (Docker, Kubernetes) without the control plane. |
| 167 | Sandbox CLI and SDK | Builder tooling | Builder tooling | agree | Client tools and libraries; the SDK is how agent code reaches Environments, but the library is not the service. |

### OpenClaw (inventory-openclaw.md, mapping-openclaw.md)

| Component | Mapper | Mine | Verdict | Reason |
|---|---|---|---|---|
| Memory provenance and deletion | Memory (clear) | Memory | agree | Records "source-session lineage" and removes entries; WARM's Memory holds provenance and keeps entries current. |
| Plugin permission requests | Approvals (clear) | Approvals | agree | "pause a tool call ... until a user approves or denies it". |
| Browser (OpenClaw-managed) | Environments (clear) | Environments | agree | A dedicated browser profile "the agent controls", "isolated from your personal browser". |
| Tool and agent permissions | Policy (clear) | Policy | agree | Per-agent access profiles for sensitive tools. |
| Session Share plugin | Sessions (strained) | Observability, or Sessions | unclear | It lets teammates "read selected sessions" read-only in the Control UI. That is people reading what agents did, closer to Observability than to pausing, resuming or handing off work. |
| Authentication (model providers) | Secrets (strained) | Secrets (strained) | agree | API keys, OAuth and CLI-credential reuse for model providers; credential storage is Secrets, and access to providers touches Models. |
| Multi-agent routing | Spans: Human channels, Registry (strained) | Spans: Environments, Sessions, Human channels | disagree | The page is mostly about running "multiple isolated agents ... each with its own workspace, state directory ... and SQLite-backed session history" (Environments, Sessions). The routing is by channel account and binding, which is Human channels; the mapper names Registry only to say it does not fit. |
| Background exec and process tool | Spans: Tools, Tasks (clear) | Spans: Tools (or Environments), Tasks | agree | The exec tool runs commands (Tools, in an Environment); durable processes "retain ownership across Gateway restarts" (Tasks recovery). |
| Standing intents | Misfit | Misfit | agree | An event-conditioned instruction checked "before eligible interactive replies": it does not start work (not Scheduling) and is not a fact, event or skill (Memory's three kinds). |
| MCP Relay | Misfit | Misfit | agree | ChatGPT, Codex and Claude connect into the Gateway as MCP clients; an inbound interface for outside agents and programs, which WARM lacks. |
| Deep Research | Domains layer (strained) | Domains layer | agree | Under WARM Step 4's own research example, finding and weighing sources is domain judgment; fetching is Retrieval. |
| Configuration - browser, UI, and desktop | Builder tooling | Builder tooling | agree | A configuration reference for operators. |

One observation outside the sample counts: the OpenClaw mapper's "Why" column is templated for many clear rows (for example, every Memory row reads "Durable learned memory, its backends, provenance or consolidation."). The template did not cause an error in my sample, but it means the reason column does not show that each row was judged on its own.

## Part 2. OpenClaw self-learning, dreaming and Skill Workshop

Sources: inventory-openclaw.md lines 952-954 (Dreaming), 1404-1417 (Skill Workshop, Self-learning); mapping-openclaw.md rows at lines 141, 214, 216 and section 6.5; the three docs pages, read 2026-11-11.

| | Self-learning | Skill Workshop | Dreaming |
|---|---|---|---|
| Page | https://docs.openclaw.ai/tools/self-learning | https://docs.openclaw.ai/tools/skill-workshop | https://docs.openclaw.ai/concepts/dreaming |
| What it does (quoted) | "Self-learning turns corrections and hard-won procedures into learned skills that future sessions load. It is on by default." | "Skill Workshop holds the skills an agent writes for itself, called **learned skills**. The agent saves a procedure after hard multi-step work and fixes a learned skill that misled it; skills nobody uses for 30 days are archived." | "Dreaming is the background memory consolidation system in `memory-core`. It moves strong short-term signals into durable memory while keeping the process explainable and reviewable." |
| Evidence from past runs | Yes. The review reads "a recent excerpt through the finished turn" and looks for "a correction to the agent's method", "a non-obvious method that worked after trial and error", or "a learned skill with a wrong, missing, or outdated step". It runs "When a session reaches 10" model iterations since its last review. Cron, heartbeat, hook, subagent and Incognito sessions do not count. | Yes. "After hard multi-step work you are likely to repeat, it saves the working procedure"; "when a learned skill the agent used turns out wrong or incomplete, it views the skill and patches the misleading step". Usage history drives archiving (30 days unused) and the skill diet ("one oversized learned skill is shrunk without changing its rules"). | Yes. It "Reads recent short-term recall state, daily memory files, and session transcripts when available". "Only interactive sessions are eligible." |
| What it changes | Learned skills; the reviewer makes "at most one change". | Learned skills: save, patch, archive, shrink. Facts are routed to memory, not to skills. | Durable memory: "Long-term promotion still writes only to `MEMORY.md`"; a human-readable diary in `DREAMS.md`. |
| Proposed or applied | Applied: "Every change applies immediately and can be undone." In `propose` mode reviews "save their changes as drafts" instead. | Applied: "Every change applies immediately, saves the previous version first, and can be undone." In `propose` mode "Background reviews then change no skills"; "Drafts are not announced and never load as skills." | Applied automatically on a schedule: "Dreaming is enabled by default"; `memory-core` "auto-manages one cron job", default `0 3 * * *`. |
| Does a person approve | Not by default. Approval only in the opt-in `propose` mode (`/learn drafts`). Undo through a button, "undo" in chat, or `/learn undo <id>`. | Not by default. Same opt-in `propose` mode; versions saved before every change; `openclaw skills workshop restore <name>`. | Not for scheduled promotion. The page offers review in two places: grounded backfill can be inspected "before deciding whether grounded candidates deserve promotion", and manual promotion is preview-first (`openclaw memory promote --apply`). |
| Changes the agent definition (`AGENTS.md`, `SOUL.md`) | The page does not mention either file. [no-record: self-learning editing AGENTS.md or SOUL.md searched=docs.openclaw.ai/tools/self-learning] | The page says codebase knowledge belongs in "that repository's docs or `AGENTS.md`", so it is not saved as a skill; it does not say Skill Workshop edits that file. [no-record: Skill Workshop editing AGENTS.md or SOUL.md searched=docs.openclaw.ai/tools/skill-workshop] | The page does not mention either file. [no-record: dreaming editing AGENTS.md or SOUL.md searched=docs.openclaw.ai/concepts/dreaming] |
| Mapper's assignment | Memory (clear) | Memory (clear); the plugin class row also Memory | Memory (clear) |

Related facts the mapper records: an "Advisor" plugin corrects only the current run, and "Job promotion" offers to turn a repeated request into a schedule (mapping-openclaw.md section 6.5). The v2026.8.1 release index says Skill Workshop now holds "proposals, checks, decisions, and applied history" (https://docs.openclaw.ai/releases/2026.8.1). In its section 7, item 10, the mapper notes that these loops "change memory directly with an undo, without passing through Evaluation and Releases".

## Part 3. Claims in mapping.md

### (a) OpenClaw built a shared Tasks ledger on 2026-03-31 and removed it on 2026-09-27 as duplicate state

**CONTRADICTED on the build date; CONFIRMED on the removal.**

- The durable task registry was merged on 2026-03-29: PR #52518, "Gateway: track background task lifecycle" (opened 2026-03-22, merged 2026-03-29T10:48Z), whose body says it "adds a durable task registry". PR #57324, "refactor(tasks): unify the shared task run registry", merged 2026-03-29, and #57361, "feat(tasks): move task ledger to sqlite and add audit CLI", followed on 2026-03-30.
- 2026-03-31 is PR #58227, "ClawFlow: add linear flow control surface" (merged 2026-03-31T08:08Z). Its test list already includes `src/tasks/task-executor.ts` and `src/tasks/flow-registry.ts`, so the ledger existed before it. ClawFlow became TaskFlow. mapping-openclaw.md section 6.4 dates TaskFlow correctly. mapping.md attaches that date to the ledger.
- Removal: PR #159179, "refactor: remove Tasks and TaskFlow runtime", merged 2026-09-27T17:40Z. The reason, quoted by the mapper from the PR, is "The Tasks ledger duplicated execution and completion state already owned elsewhere." The PR body I fetched says the removal follows "after Cron, follow-up results, native execution and generated-media completion have their own existing owners". The docs say: "The shared Tasks ledger, TaskFlow orchestration API, and TaskFlow Webhooks plugin have been removed." (https://docs.openclaw.ai/automation, inventory line 52).

### (b) OpenClaw moved heartbeats to ordinary scheduled jobs between 2026-07-23 and 2026-10-21, shipped in v2026.8.1 on 2026-08-31

**CONFIRMED in substance; each end of the range is one day off, and the last steps shipped after v2026.8.1.**

- Start: PR #112585, "feat(cron): system-owned heartbeat monitor jobs replace the dedicated interval scheduler", merged 2026-07-22. #113165 (heartbeat `tasks:` entries become cron jobs, "Stage 4 of the 'everything is a cron' program") and #113135 merged 2026-07-23; #113131 (remove the `HEARTBEAT.md` runtime fallback) merged 2026-07-24.
- #129862, "refactor(cron): unify heartbeat automations under cron ownership", merged 2026-08-26. Its merge commit is an ancestor of tag v2026.8.1 (GitHub compare: behind_by 0).
- v2026.8.1 ("OpenClaw 2026.8.1") was published on GitHub 2026-08-31T03:30Z. Its docs page https://docs.openclaw.ai/releases/2026.8.1/automations-and-scheduling says: "Heartbeat schedules are now managed as Automations ... Existing installations using `HEARTBEAT.md` must run `openclaw doctor --fix` to migrate valid work because OpenClaw no longer reads that file at runtime." The page lists #112585, #113131, #113135, #113165 and #129862. The GitHub release body and CHANGELOG.md do not carry that sentence; the release's index page on the docs site does not either.
- End: #179387, "feat(automations): migrate heartbeat jobs through Doctor" ("slice 3 of 4"), merged 2026-10-21. Slice 4 landed the next day: #180192, "refactor(automations): retire heartbeat executor and response tool", merged 2026-10-22, with clean-up PRs #179747 (2026-10-21), #180563 and #180915 (2026-10-22). These shipped after v2026.8.1.
- mapping.md's own wording ("2026-07-23 entries became cron jobs; 2026-08-26 schedules unified under cron, shipped in v2026.8.1 on 2026-08-31; 2026-10-21 monitors migrated") is accurate for the steps it names. A full range is 2026-07-22 to 2026-10-22.

### (c) AgentCore has no scheduling component

**CONFIRMED.**

- The AgentCore Developer Guide navigation (`toc-contents.json`, downloaded 2026-11-11) has no page title or path containing "schedul" or "cron". Titles matching "trigger", "event", "recurring" or "periodic" are: Memory short-term events (create/get/list/delete an event), Gateway event types and CloudTrail data events, Registry notifications through EventBridge (outbound), and "Recurring report".
- "Recurring report" (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/insights-recurring-report.html) is a clustering schedule (`DAILY`, `WEEKLY`, `MONTHLY`) for insight analysis jobs. It starts no agent work, and the page says creation of new recurring insights ended 2026-10-16 and existing ones stopped generating reports after 2026-10-30.
- The mapper also found the Memory `TimeBasedTrigger`, an idle-session trigger for memory extraction. It is not a scheduler for agent work.
- A web search restricted to docs.aws.amazon.com and aws.amazon.com found no AgentCore scheduling feature. AWS's own examples schedule agents with a separate service: EventBridge Scheduler calling `InvokeAgentRuntime` directly or through a Lambda, or a customer-built scheduler queuing jobs to SQS ([Nova Act synthetic monitoring](https://aws.amazon.com/blogs/machine-learning/implementing-synthetic-monitoring-using-amazon-nova-act/), [ambient agents on AgentCore](https://aws.amazon.com/blogs/machine-learning/building-ambient-agents-with-amazon-bedrock-agentcore-from-event-driven-signals-to-human-in-the-loop-workflows/), [Reactiv](https://aws.amazon.com/blogs/machine-learning/how-reactiv-automates-mobile-commerce-80-faster-with-amazon-bedrock-agentcore/)).
- [no-record: AgentCore-native scheduler for agent work searched=Developer Guide navigation (toc-contents.json, all titles and hrefs), docs.aws.amazon.com and aws.amazon.com via web search; instrument check: the same TOC search found "Recurring report", so it can return a positive]. I did not full-text search the body of every Developer Guide page.

## What I could not check

- I did not read every Developer Guide page body for AgentCore (only the navigation, two pages and a web search), so a scheduling sentence buried in a page body would have been missed.
- For the OpenClaw sample I relied on inventory entries plus my own reading; I fetched live pages only for Part 2 and Part 3. MCP Relay, Session Share and Standing intents were judged from the inventory's quotes.
- The three docs-page summaries in Part 2 came through a fetch tool that summarizes pages; the quotes match the inventory and the mapper where they overlap, but I did not read the raw HTML of those three pages.
- I did not confirm which OpenClaw release first shipped the Tasks removal (#159179); the mapper did not either.
- The sample is 36 of 1,301 components; it says little about any single service's row count.
