---
log_id: "2026-11-10-0807-37-warm-v0-8-figure-library-concept-register-and-full"
title: "WARM: the Working Agents Reference Model, v0.10"
date: 2026-11-11
author: sagan
issue: lifeos#3502
status: v0.10 applies the author's notes from listening to the narrated deck (2026-11-10) and his decisions of 2026-11-11: an agent belongs to a domain and runs on the platform; how work starts (conversation, job, backlog); domains have responsibilities and hand work to the domain responsible; CI is a Software Factory practice; Finance as a second mapped domain; limits corrected
---

# WARM: the Working Agents Reference Model (v0.10)

WARM is explained in six steps, then two examples. Each step states one idea and builds on the step before. The steps are an order of explanation; they are not layers of the system. A glossary at the end defines every term in one place.

## Step 0. Scope

**Idea: WARM names the parts of a system in which agents do sustained work, and how the parts relate.**

An **agent** fills a role in a domain. Its **agent definition** (role, instructions, skills) is written by the domain, and it is what makes this agent different from another. An agent **runs on** the platform. The **harness**, a platform service, runs its loop: it sends context to a model and carries out the tool calls the model asks for. The model comes from a provider and is called through the platform, and the platform may choose a different model for different requests.

So an agent belongs to a domain and runs on the layers below it, as a domain runs on the platform. A test shows which part is the agent. Replace the harness product or the model, and it is the same agent doing the same work. Replace the definition, and it is a different agent.

Agents are of two kinds, by how long they last.

| Kind | What it is | What it keeps | Example |
|---|---|---|---|
| **Persistent agent** | Holds a role across many sessions and tasks. | An identity, its session history, what it has learned, and a channel on which people and other agents reach it. | A finance agent that a person consults, and that remembers the accounts and last month's decisions. |
| **Task agent** | Holds a role for one task: it is started for the task and ended when the task ends. Another agent starts it (a subagent), or a schedule or an event does (a job). | No continuing role and no memory of its own after the task. It returns a result and work products, and acts on behalf of whoever started it. | A developer agent started for one issue, which delivers a pull request and ends. |

Both kinds belong to a domain and run on the same platform services. The two kinds match how work starts (Step 4): a persistent agent is the one that people talk to, and task agents do the work that a schedule, an event or a backlog starts. The difference is what continues: a persistent agent keeps its role, its session history and its memory from one task to the next, and a task agent does not. The end of a task agent is not the deletion of its records. The platform retains the identity under which it acted, its transcript and its results for as long as the retention policy says, so that a past action can be attributed and investigated, and it can checkpoint and resume a task agent while its task is still running.

WARM describes the system around agents: who directs them, what work they do, and what they run on. It does not describe how a single agent reasons (planning, reflection); research papers already model that.

WARM names no vendor and no product. It is abstract. A real system that fills in one of its parts is an **implementation** of that part (Step 5).

## Step 1. The layers

**Idea: people direct domains; domains run on a platform; the platform runs on infrastructure and calls providers.**

| Layer | What it is | Examples |
|---|---|---|
| **People** | Those who direct and approve the work. | A developer; a team lead |
| **Domains** | Areas of work, and the agents that carry them out. | Software Factory, Finance, Health |
| **Platform** | Reusable mechanisms that agents in any domain can use. | Sessions, memory, scheduling |
| **Infrastructure** | Where everything runs. | Machines, CI runners, storage, network |
| **Providers** | What the platform calls from outside. | Models, external services |

Infrastructure and Providers sit side by side beneath the platform. Neither runs on the other: the platform runs *on* infrastructure and *calls* providers.

The platform holds what every domain reuses, and a domain holds what is specific to one area of work. Stated as a rule: **the platform supplies mechanisms; a domain supplies meaning.** The wording follows the separation of mechanism and policy in operating-system design (citation to verify: the Hydra system, 1975); WARM says "meaning" because Policy is the name of one of its services. A mechanism works the same way whatever the work is about. Meaning is the goals, rules and knowledge of one area of work, together with any logic that makes sense only for that area.

Example: holding an action until a person approves it is a mechanism, so it is a platform service. The rule "every payment needs approval" is meaning, so it belongs to the Finance domain. The domain supplies the rule, and the platform's mechanism applies it.

A domain can also supply executable logic: a connector to one bank, a calculation, the tests of one codebase. That logic is meaning in this sense, because it is useful only in its own area. The domain supplies it through a platform service (Tools for the connector, Evaluation for the tests), and the platform mediates it without knowing what it is about.

The rule is a design choice and not a finding. A mechanism discovered inside a domain is treated as a gap in the platform, so no observation can refute the rule. What can be tested is its usefulness: whether a service stays meaningful, unchanged, when a second and a third domain use it.

A platform service does not have to be used by every domain. A system with one agent needs no agent messaging; messaging is still a platform service, because it does not depend on what the messages are about.

## Step 2. The platform is six groups of services

**Idea: the platform answers six questions about agents.**

| Group | The question it answers |
|---|---|
| **Runtime** | How, where and when do agents run? |
| **Knowledge** | What do agents know and keep? |
| **Capabilities** | What can agents use? |
| **Interaction** | Who do agents work with? |
| **Governance** | What are agents allowed to do? |
| **Operations** | How do we see it, judge it and keep it running? |

### How the groups relate

The six groups are of two kinds, by the main scope of their services. Four are **working groups**: an agent mostly uses their services to do its work. Two are **cross-cutting groups**: their services mostly apply to what happens in every other group.

| Group | Kind | Relation to the other groups | The services that make it so |
|---|---|---|---|
| **Runtime** | working | The center. Work happens in a session or a task, and the other working groups are used from there. | Harness, Sessions, Tasks |
| **Capabilities** | working | **Used by** Runtime. | The Harness sends context to Models, carries out calls through Tools, and finds agent definitions, tools and skills through the Registry. |
| **Knowledge** | working | **Used by** Runtime. | The Harness reads Memory and Retrieval into the context window, including the skills a task needs, and writes back what was learned. A task stores its work products in Artifacts. |
| **Interaction** | working | **Connects** Runtime to other agents and to people, in both directions. | An agent sends through Messaging, Orchestration and Human channels. A message, a handoff or a person's request starts or resumes a session or a task. |
| **Governance** | cross-cutting | **Constrains** the other five. | Identity establishes who is acting on every tool call, message and memory write. Secrets releases what that actor may use without showing it. Policy decides whether the action may proceed. Approvals holds it for a person. |
| **Operations** | cross-cutting | **Observes and changes** the other five. | Observability records what they did, Evaluation judges it, Releases changes them, and Reliability restores them. |

Three points follow.

1. **The two cross-cutting groups apply to each other.** A release can require an approval, so Governance constrains Operations. An approval decision is recorded, so Operations observes Governance.
2. **A cross-cutting group still uses working services.** Approvals reaches the person through Human channels. Observability stores its records somewhere. Cross-cutting describes what a group applies to, not what it is built from.
3. **The relations are not a layering.** No group sits on another, and a system that lacks a service lacks the relations that service carries.

The kind describes the main scope of a group and does not sort every service cleanly. A working service is mostly called for its result. A cross-cutting service mostly applies to actions whose purpose lies elsewhere, and it has to be able to act on an action without the cooperation of the agent that performs it. Some cross-cutting services are also called directly: an agent asks Evaluation for a verdict, Releases for a deployment, or Secrets for the use of a credential. Some working services apply without being called: Environments isolates whatever an agent does. The stated overlaps are part of the model.

These relations are stated between groups and are derived from the responsibilities of the services in Step 3. The dependencies between individual services are part of each service's contract, which the paper for each group specifies.

### Concerns that are not groups

The groups are also a way to find things, and some concerns touch several of them without being a group. Security touches Governance, Runtime and Capabilities. Cost touches Models (which model is used), Policy (spending limits) and Observability (what was spent).

### Group, service and module

A **group** is a set of services that answer one question; it is a classification with stated relations, and it is not a unit that is built or replaced. A **service** is the unit with one responsibility and a boundary. A **module** is a unit of an implementation. WARM does not use "module" for anything in the model, because one service may be implemented by several modules and one module may implement parts of several services.

## Step 3. Twenty-two services

**Idea: each group holds a few services, and each service has one responsibility.**

| Group | Service | Its one responsibility | Industry terms |
|---|---|---|---|
| Runtime | **Harness** | Run the agent loop: decide what goes into the context window, send it to the model, and carry out the tool calls the model asks for. | harness, agent loop, context management, compaction |
| Runtime | **Sessions** | Keep the history and state of an agent's work so a long-running agent can pause, resume and hand off. | session, thread, state |
| Runtime | **Tasks** | Track each unit of work (a task or run) from start to finish, and coordinate its retry, recovery and cancellation. | runs, jobs, task lifecycle, durable execution, checkpointing |
| Runtime | **Environments** | Give each agent a place to act, isolated from the others, on the infrastructure: sandboxes, workspaces, browsers. | sandbox, runtime, workspace, computer use |
| Runtime | **Scheduling** | Start work at a time or on an event. | cron jobs, scheduled tasks, triggers |
| Knowledge | **Memory** | Retain what agents learn across sessions, with where it came from, and keep it current. Memory holds three kinds: semantic (facts), episodic (events) and procedural (skills: how to do a kind of task). | memory, memory bank, dreaming, skills, procedural memory |
| Knowledge | **Retrieval** | Fetch material from named sources: documents, data, notes. | retrieval, knowledge base, grounding, RAG |
| Knowledge | **Artifacts** | Store what agents produce (reports, files, pages) and its versions. | artifacts, outputs, store |
| Capabilities | **Models** | Mediate requests to models and choose the model for each task, across more than one model or vendor. | models, model routing, multi-model |
| Capabilities | **Tools** | Mediate calls to tools, local or external. | tools, MCP, gateway, connectors |
| Capabilities | **Registry** | Hold the directory (the responsibilities, the domain that holds each, and which agent to reach), the definitions of agents and tools, and an index of the skills kept in Memory, so that each can be found and loaded when a task needs it. | registry, catalog, discovery |
| Interaction | **Messaging** | Deliver messages between agents. | agent-to-agent, A2A |
| Interaction | **Orchestration** | Divide work among agents (including subagents an agent starts itself), people and fixed steps, and collect the results. | orchestration, subagents, handoffs, workflows |
| Interaction | **Human channels** | Carry requests and results between people and agents, on the channel the person is using. | channels, surface, agent interface |
| Governance | **Identity** | Establish who is acting: each agent, person and service, and on whose behalf. | identity, agent identity, authentication |
| Governance | **Secrets** | Hold every value that platform components and agents must not know directly (API keys, passwords, tokens, signing keys, and other sensitive values such as account numbers), and release each one only to the component that needs it, at the point of use, without placing it in an agent's context. | secrets, secret manager, vault, credentials |
| Governance | **Policy** | Evaluate rules that decide automatically whether an action is allowed, and enforce the decision. Domains and the platform's operator supply the rules; a spending limit is a rule a finance domain supplies. | policy, guardrails, permissions, hooks |
| Governance | **Approvals** | Hold chosen actions until a person authorizes them, and record the decision. | human in the loop, tool approval |
| Operations | **Observability** | Collect evidence of what agents and the platform did. | observability, tracing, audit log |
| Operations | **Evaluation** | Assess behavior and work products against stated criteria, and report "unknown" when a check could not run. | evaluation, evals |
| Operations | **Releases** | Version and release changes to agents, the platform and the infrastructure the system manages, with a way back. | deployment, versioning, rollback, change management |
| Operations | **Reliability** | Keep services available and restore them after a failure. | operations, recovery |

These names are responsibilities, not products. One product may cover several responsibilities, one responsibility may be shared by several products, and a system does not need all twenty-two.

WARM names each service and its responsibility. The word "job" is kept for scheduled work: a task that a schedule or an event starts. Whether a retried task repeats an effect is an example of what a responsibility leaves open: it depends on the contract between Tasks, Tools and the outside system. WARM does not yet specify each service's contract (what it guarantees on failure, cancellation or delegation). Those contracts are the subject of the papers that cover each group.

### The Harness service and harness products

The Harness is listed as one service of twenty-two, and it is also the part of every agent that runs the loop. Both statements hold, because the word names two things. The Harness *service* is the loop: it assembles the context, calls the model, and carries out tool calls. A harness *product* usually bundles the loop with several other services, such as sessions, tool mediation, subagents and permission checks. A mapping of a real system records the bundle: which of the twenty-two responsibilities the product provides, and which are built around it. From the loop, an agent calls the working services, and the cross-cutting services act on those calls.

### Where memory lives

"Memory" is one service, but what an agent remembers is spread across five services, by how long it lasts and who wrote it.

| What is remembered | Service |
|---|---|
| What is in the context window now (working memory) | Harness, which decides what goes into context |
| The history of one stretch of work | Sessions |
| What agents learn and keep across sessions: facts (semantic), events (episodic) and skills (procedural) | Memory |
| Material that is looked up when needed, not learned | Retrieval |
| What agents produce | Artifacts |

Memory also keeps its entries current: it records where each came from, and it revises or retires entries that later evidence contradicts.

The five services are responsibilities and not five bins that each piece of content fits exactly once. One report can be stored by Artifacts, fetched by Retrieval, placed in the context window by the Harness, recorded in a session, and used to write a Memory entry. A skill can be written by a person before any agent has learned from experience; Memory then records that source.

## Step 4. A domain supplies meaning

**Idea: a domain tells the platform's mechanisms what the work is.**

| A domain defines | What it is | The platform service that carries it |
|---|---|---|
| **Goals** | What the work is for, and who is accountable. | (set by people) |
| **Roles** | The positions in the domain and their duties, filled by agents and people. Each role that an agent fills is written as an agent definition. | Registry (for roles an agent fills) |
| **Workflow** | How work starts, and how it moves from request to result. | Tasks, Scheduling, Orchestration |
| **Domain knowledge** | What must be known to do this work. | Memory, Retrieval |
| **Domain tools** | Connections this work needs. | Tools |
| **Domain rules** | Limits and approvals this work needs. | Policy, Approvals |
| **Acceptance criteria** | How to tell that a work product is good. | Evaluation |

People set the goals, and a platform service carries each of the other six. Under WARM's rule a domain adds no mechanisms of its own: if a domain needs a mechanism the platform lacks, that is a gap in the platform. A new domain can still require new work, such as a connector to a system no other domain uses. The domain supplies that logic, and Tools carries it.

### How work starts

Work in a domain starts in three ways, and each needs a different place to run.

| Work starts when | Example | Where it runs |
|---|---|---|
| A person asks | A conversation with the finance agent | The persistent agent's own session |
| A time or an event arrives | A nightly sync; a scan for alerts | A job: a task agent with no conversation, started by Scheduling |
| A backlog needs working | A sprint | A separate team: a coordinating agent and task agents, tracked by Tasks |

Unattended work that runs inside a conversation session interrupts the conversation and fills its context, and the conversation delays the work. The reference implementation met this twice: first with periodic checks that ran inside each agent's session, and then with sprints that ran inside the session of the agent that planned them. Both times the remedy was to move execution out of the session and to leave the persistent agent as the one that people talk to. This is an observation from one system. WARM offers it as design guidance and not as a rule of the model.

A second question follows: where judgment happens. A scheduled job can be a plain script, and then anything that needs judgment waits for a conversation. It can also be a task agent, which judges and escalates what it cannot decide.

Not every domain needs the third row. It fits a domain that has a backlog which outlasts a conversation, and acceptance criteria that can be checked without a person. This test is reasoning from the reference implementation and has not been measured.

### How agents fit

Domains differ from one another in everything the table lists: no two have the same goals, knowledge or rules. What they have in common is the set of services through which that meaning reaches the platform. For each role an agent fills, a domain writes an **agent definition**, which names the role, the instructions and the skills the role needs. The Registry holds the definition. The Harness loads it, and from then on the agent is doing the domain's work on the platform's services. The definition is not the only route: the domain's rules reach Policy and Approvals, its criteria reach Evaluation, and its knowledge reaches Memory and Retrieval, each through its own service.

WARM sets no number of agents per domain. A domain may have one persistent agent that holds its main role, several persistent agents with different roles, or none, with task agents started when work arrives. One persistent agent may also hold roles in more than one domain. A persistent agent commonly starts task agents for parts of its work, so a domain with one persistent agent still runs many agents over time. A task agent, a schedule or an event can start a task agent as well.

**Provisional.** A component that provides a platform service may itself be an agent: a router that delivers messages, a reviewer that evaluates work. Such an agent is part of the platform. Its definition comes from whoever operates the service and not from a domain, so it is the one exception to the statement that an agent belongs to a domain. A platform agent still uses the platform like any other agent, and it has to meet the same service boundary as any other implementation of that service. One consequence needs a rule that WARM does not yet state: an agent that provides Messaging or Reliability cannot rely on its own service to recover, so it needs a way to start and be repaired that does not pass through itself.

### Domains have responsibilities

A domain does not act. It is a definition: its goals, roles, workflow, knowledge, tools, rules and acceptance criteria. The agents and people who fill its roles act. A domain resembles a department's charter more than a department's staff.

Each domain holds a cohesive set of responsibilities: the things its roles are accountable for. Finance is responsible for tracking spending, paying bills, managing investments and watching subscriptions. Communications is responsible for the inbox and for messages sent in a person's name. The responsibilities of one domain belong together because they draw on the same knowledge, tools and rules and serve the same goals. A responsibility that shares none of these with the rest is a sign that it belongs in another domain, or in a new one. Each responsibility belongs to exactly one domain. People set this division, as part of directing the domains.

The division is recorded in one place, the **directory**: a list of the responsibilities, the domain that holds each, and which agent to reach. It works as a company directory does, for responsibilities. The Registry holds it.

An agent learns the division in three ways. It can look a responsibility up in the directory. The Harness loads a short form of that directory into every agent when it starts, so that an agent knows where work belongs without looking it up. An agent that is unsure can query the Registry, or send the work to an agent whose role is to route it.

When an agent meets work that falls under another domain's responsibility, it hands the work to an agent of that domain and gets a result back. The request and the result travel through Messaging. The work is an ordinary task in the responsible domain, requested by an agent and not by a person.

Example: a finance agent needs an email sent. Delivering a message works the same way whatever the message says, so delivery is a platform service. Deciding what to say, to whom, and whether it is approved takes knowledge of the contacts, the person's voice and the rules for outbound messages. That is the communications domain's responsibility, so the finance agent hands the email to the communications agent.

A second example: research. In the reference implementation a person converses with the research agent directly, and the agents of other domains also hand it questions. Fetching a page or running a search works the same way whatever the question is, so fetching is a platform service (Retrieval). Deciding what to look for, checking one source against another and saying how far the evidence goes takes judgment, so research is a domain. The specialized research tools are that domain's tools, which is a second reason the work goes there: the responsibilities, the tools and the knowledge of how to verify a claim sit together. Communications receives work because of rules (who may send in a person's name). Research receives it because of skill and tools.

Domains depend on one another as the departments of an organization do. One asks another for work in ordinary language, the other uses its judgment, and the two sort out what was unclear. Nothing about the exchange is specified in advance beyond who is responsible for what. This kind of dependence suits agents, whose strengths are language and judgment and whose output varies from one run to the next. Platform services are the opposite case: small, clearly bounded and expected to behave the same way every time. So the two layers differ in kind as well as in content. The platform is where a system needs sameness, and the domains are where it needs judgment.

One test separates domain work from a platform service. If the provider applies its own knowledge or judgment, it is domain work. If it adds none, it is a platform service that sits in the wrong place.

The division is also a diagnostic. A responsibility with no domain is a gap, one that two domains both hold is an overlap, and work done outside the domain responsible for it is misplaced. A map of the reference implementation found all three.

Work in many domains passes through the same six stages, which WARM offers as a template, not a requirement: **intake → plan → execute → verify → report → improve**. In the last stage a domain changes its own way of working from evidence; the platform supports that with Evaluation (the evidence) and Releases (the rollout).

## Step 5. Every part has implementations

**Idea: WARM is abstract; a real system implements one of its parts.**

"Implementation" is one relation, and it applies at every layer.

| Part of WARM (abstract) | An implementation (real) |
|---|---|
| A domain: the Software Factory | **Agent Scrum**: named roles, a sprint backlog, reviews, a wrap |
| The platform | A harness plus what is built around it. In the reference implementation: Claude Code and the LifeOS tooling |
| Infrastructure | A server, its CI runners, backups and network. In the reference implementation: a remote Linux server |
| Providers | The model vendors and external services a system uses |
| The agents of a domain | In the reference implementation: one persistent agent for each of six domains, several for the Software Factory, and task agents started by all of them |

A domain can have more than one implementation (Scrum and Kanban both implement software development), and an implementation's ideas can be reused in another domain.

The mapping between services and components is many to many. One boundary for each service is an experiment of the reference implementation and not a rule of the model.

A full system is described by mapping its parts to WARM. For each platform service the mapping records which component provides it, who supplies that component (the harness vendor, the implementer, a third party) and who operates it. One service can have more than one provider.

Providers of a service change over time. Harness vendors now supply services that implementers used to build (sessions, memory, scheduling and messaging are recent examples). An implementer who keeps each service behind a clear interface can change its provider with less rework.

Uses of the model:

- **Describe a system:** map each part to a layer, a service or a domain. A part that fits nowhere is a finding: the model lacks something, or the part mixes two responsibilities.
- **Place new work:** mechanism or meaning (Step 1)? If mechanism, which question does it answer (Step 2)?
- **Compare systems:** list, per service, who provides it.
- **Structure a body of writing or code:** one unit per part.

## Example: the Software Factory

The Software Factory is the domain that builds software. Agent Scrum is one implementation of it. It is the most developed domain in the reference implementation, and the seven rows of Step 4 were drawn largely from it. The example therefore illustrates Steps 4 and 5 and is not an independent test of them.

| Step 4 asks for | In Agent Scrum |
|---|---|
| Goals | Working software, merged and released |
| Roles | Scrum master, developers, reviewers; a person as product owner |
| Workflow | Sprint backlog, tasks, reviews, wrap |
| Domain knowledge | The codebase, its conventions, past decisions |
| Domain tools | Source control, CI, issue tracker |
| Domain rules | Who may merge what; which changes need a second reviewer |
| Acceptance criteria | Tests pass; reviewers approve |

CI is a practice of software development, so it belongs to the Software Factory: it is part of that domain's workflow, tools and acceptance criteria. Like any domain work it uses platform services (Environments gives a build an isolated place to run) and runs on Infrastructure (the CI runners). No other domain uses CI, so it is not a platform service.

One property is prominent in this domain. Its work products are software, and the platform is software. So the Software Factory can build and change the platform it runs on, and the tools the other domains use. Other domains change the system too (a security domain changes policies; every domain improves its own way of working, and any domain may produce software). In the reference implementation the Software Factory owns changes to platform software.

When the work is building the platform or changing the infrastructure, the same services still apply: Policy and Approvals gate those changes, Evaluation judges them, and Releases versions them and keeps a way back. The model states that the services apply. It does not show that an implementation enforces them. That requires a control that an agent cannot change by itself, such as an approval or deployment authority outside the agent's reach.

For this reason the reference implementation got the platform and the Software Factory working first: the two improve each other, and every other domain benefits. A team that starts from a managed platform or from another domain may choose a different order.

## Second example: Finance

Finance is the second domain mapped to the seven rows. The entries are generic and come from the reference implementation's finance agent.

| Step 4 asks for | In the reference implementation |
|---|---|
| Goals | The household's money is tracked, bills are paid, and spending follows the plan |
| Roles | A financial advisor agent; a person who decides |
| Workflow | Conversations with the person; scheduled syncs, scans and summaries. No backlog |
| Domain knowledge | The accounts, the plan, and past decisions on how to categorize spending |
| Domain tools | Connections to banks and to a budgeting service |
| Domain rules | Every payment and every trade needs the person's approval; no scheduled job may move money |
| Acceptance criteria | The books reconcile; most other decisions are the person's judgment |

How work starts: a person asks, or a time arrives. There is no backlog, and most acceptance criteria are a person's judgment, so by the test in Step 4 this domain needs no separate team. Its scheduled jobs are plain scripts, so work that needs judgment waits for a conversation.

The seven rows fit this domain without strain. Like the first example, the map was made by the model's author and is not an independent test.

## Glossary

| Term | Meaning |
|---|---|
| **Agent** | Fills a role in a domain. Its definition comes from the domain, and it runs on the platform: the Harness service runs its loop with a model from a provider. |
| **Agent definition** | The role, instructions and skills that make one agent different from another. A domain writes one for each role an agent fills; the Registry holds it. (Provisional: the operator of a platform service writes one for an agent that provides the service.) |
| **Artifact** | Something an agent produces and stores: a report, a file, a page. |
| **Directory** | The list of responsibilities, the domain that holds each, and which agent to reach. People set it, the Registry holds it, and every agent starts with a short form of it. |
| **Domain** | An area of work, such as building software or managing money, defined by its goals, roles, workflow, knowledge, tools, rules and acceptance criteria. A domain does not act; the agents and people in its roles do. It holds a cohesive set of responsibilities. |
| **Persistent agent** | An agent that holds a role across many sessions and tasks. The platform keeps its identity, session history and memory between tasks. |
| **Harness** | The service that runs the agent loop: it manages the context window, calls the model and carries out tool calls. A harness product usually bundles this service with others. |
| **Implementation** | A real system that fills in one part of WARM: Agent Scrum implements the Software Factory; a harness and its tooling implement the platform. |
| **Infrastructure** | Where everything runs: machines, CI runners, storage, network. |
| **Person** | Someone who sets goals, makes decisions and approves actions. |
| **Provider** | An outside source the platform calls: a model vendor or an external service. |
| **Role** | A position in a domain with stated duties, filled by an agent or a person. |
| **Responsibility** | What a part is accountable for. Each platform service has one. Each domain holds a cohesive set of them, and each responsibility belongs to exactly one domain. |
| **Service** | Something the platform provides to agents in any domain, which works the same way whatever the work is about. Only the platform has services; a domain does work. |
| **Session** | The history and state of one stretch of an agent's work. |
| **Skill** | Procedural memory: a packaged set of instructions for a kind of task, learned and refined from experience and kept in Memory. The Registry indexes skills so an agent can load the right one when a task needs it. |
| **Subagent** | A task agent started by another agent to do part of its task. |
| **Task** | One unit of work with a start, an end and a result. Also called a run. A task that a schedule or an event starts is a job. |
| **Task agent** | Also called a worker agent. An agent started for one task and ended with it, with no continuing role or memory of its own. The platform retains its records. A subagent is a task agent started by another agent; a schedule or an event can also start one. |
| **Work product** | What a task produces: software, a report, a decision, a message. |

Relations: a person **directs** a domain. A domain **defines** roles, and **writes** an agent definition for each role an agent fills. An agent **fills** a role and **belongs to** that domain. A domain **holds** a cohesive set of responsibilities, and an agent **hands** work to the domain responsible for it. A persistent agent **starts** task agents. An agent **works on** tasks, in sessions. A task **produces** work products. Agents **run on** the platform and **use** its services. Within the platform, Runtime **uses** Capabilities and Knowledge, Interaction **connects** Runtime to other agents and people, Governance **constrains** every group, and Operations **observes and changes** every group. The platform **runs on** infrastructure and **calls** providers. A real system **implements** a part of the model.

## What WARM adds, and its limits

Most agent platforms grow, and few are designed up front. A team starts with a harness (a model, a loop and some tools) and adds to it one problem at a time: memory, scheduled jobs, approvals, subagents, a second agent. Each addition solves a real problem, and the result is hard to describe, compare or change. The reference implementation grew this way, in part from the goals of the open-source project OpenClaw, which its author tried first.

WARM offers four things:

1. **An anatomy of an agent platform.** Names for its parts (five layers, six groups, 22 services) and for what sits on it (domains and agents).
2. **Organizing principles.** What belongs in the platform and what belongs in a domain; an agent belongs to a domain and runs on the platform; a domain holds a cohesive set of responsibilities, recorded in a directory; unattended work is kept out of conversation sessions; Governance and Operations apply across the other groups.
3. **A map for a harness that is growing.** It shows the whole that the additions are heading toward, so that a team can see what it has, what is missing and what is tangled.
4. **A starting place to build, assess and compare.** A checklist for building, a frame for comparing platforms service by service, and a target for a refactor.

A survey of 34 sources on 2026-11-09 found no adopted, vendor-neutral reference model for an agent platform. Vendors decompose the platform into services and agree on a core (runtime, sessions, memory, tools, identity, observability, sandboxed execution). Software-factory products describe one way of working. The survey found no source that puts domains of work in the same model as the platform. WARM joins them.

Limits, stated as plainly as the author can:

1. **Source.** WARM is built from an industry survey and one implementation. The survey supplies vocabulary and no proof of completeness, and some of its quotes were not re-checked against the primary page. The implementation is a small company's system, on one harness product.
2. **Domains.** That implementation runs seven domains (software, finance, health, communications, research, marketing and customer support). That is some evidence that the platform services are reusable. But the seven are the domains its owner needed, each built as far as was useful, so other kinds of domain, and deeper ones, may not fit the domain half of the model. The author made every map.
3. **Platforms.** WARM has not been mapped to another agent platform, service by service, by the author or by anyone else.
4. **Interfaces.** WARM names what each service is responsible for and does not specify interfaces. An implementation does that.
5. **Evidence.** There is no evidence yet that organizing a system this way improves it. The refactoring of the reference implementation is the first test.

Two further cautions: the boundary rule is a design choice that cannot be refuted, and the two kinds of group describe scope and do not sort every service.

## Changes from v0.9 (The author's notes on the narrated deck, 2026-11-10, and his decisions of 2026-11-11)

| Change | Why |
|---|---|
| An agent belongs to a domain and runs on the platform. The "three parts from three layers" description is withdrawn | The author noted that an agent, at least a persistent one, is defined at the domain level although it runs on the harness and the infrastructure. Both kinds are placed in a domain (his decision, 2026-11-11). Test: change the harness or the model and it is the same agent; change the definition and it is not |
| Examples for the two kinds: a finance agent and a developer agent | The author asked for an example of a persistent agent and of a task agent |
| "How work starts" added to the Workflow part: a person asks, a time or event arrives, a backlog is worked; unattended work is kept out of conversation sessions; where judgment happens | The author's account of three attempts at heartbeats and of sprints inside the CTO agent's session. Stated as design guidance from one system |
| "Domains have responsibilities" added: each domain is accountable for an area of work, the Registry holds the division, and an agent hands work to the domain responsible for it. "Service" now means a platform service only. (This replaces "domains serve other domains", written earlier the same day) | The domain maps found domains doing work for others. The author, 2026-11-11: a domain service was too close to a mechanism; domains have responsibilities within the whole scheme, and other domains know which domain holds which. |
| A domain holds a cohesive set of responsibilities, not one. Cohesion means shared knowledge, tools, rules and goals; each responsibility belongs to exactly one domain | The author, 2026-11-11: a domain holds a cohesive set of responsibilities, as Finance does, and not a single one |
| "What WARM offers" restated as four: an anatomy, organizing principles, a map for a growing harness, a starting place to build, assess and compare | The author, 2026-11-11: this statement matters and was weak; many engineers of AI applications are growing their harness toward this point without noticing; and LifeOS grew from the goals of OpenClaw |
| Limits restated as five: source (a survey and one small company's system), domains (seven, the ones needed, limited depth and width), platforms (not mapped to another), interfaces (not specified), evidence (none yet) | The author, 2026-11-11: state the limits deliberately, and do not call it one person's system, since it is also a company |
| "Worked example" becomes "example" everywhere | The author, 2026-11-11: the phrase read oddly; it is an example |
| Research added as a second example of a domain that others hand work to | The author, 2026-11-11 13:28: he talks with the Research agent directly, and other agents regularly use it for research, so it is a second example beside Communications. |
| Domains depend on one another as departments do, in language and with judgment; platform services are small, bounded and behave the same way every time | The author, 2026-11-11: domains depend on each other as departments of people do, which suits what agents built on language models do well, whereas platform services are clear-cut and granular |
| The directory is named as a first-class part: the list of responsibilities and the domain that holds each, held by the Registry and loaded into every agent | The author, 2026-11-11: it is first class in the model, like a corporate directory of responsibilities. |
| "Mechanism" is credited to the operating-system principle and no longer leads the statement | The author had not heard "mechanism" used for something a platform provides. |
| CI restated as a Software Factory practice | The author: CI belongs to the Software domain |
| Finance added as a second mapped domain | The author: map each domain; the public material shows one more than software |
| Limits corrected: one implementation runs several domains; two are mapped in detail | The author: LifeOS has more than one domain, so the text should not say the model was applied only to Software |
| "Worker agent" recorded as another name for a task agent (glossary only; figures and deck unchanged) | The author, 2026-11-11, listening to the v0.10 recording: a task agent could also be called a worker agent. It matches the reference implementation's dev-worker and the orchestrator-workers pattern in the literature |
| The boundary rule is unchanged in the model. The deck no longer gives it a slide of its own in the talk | The author: the rule was emphasized more than it needed |

## Changes from v0.8 (two reviews of the deck, 2026-11-10; the author accepted the recommendations)

Both reviewers (gpt-6-astra and a fresh Opus reviewer) read the deck, this document and the twelve figures. The reviews are `deck/review-astra.md` and `deck/review-opus.md`.

| Change | Finding it answers |
|---|---|
| "Durable agent" renamed **persistent agent** (The author, 2026-11-10 09:37) | It is the term of the published Persistent Agents paper, and "durable" already means execution that survives a crash (durable execution), which is a property of Tasks and Sessions and not of an agent's lifetime. |
| The boundary test is stated as a design rule that cannot be refuted; a domain may supply executable logic through a platform service | Both: the test was true by definition, and "a domain adds no new mechanisms" was presented as a finding |
| Policy evaluates and enforces rules that domains supply; "Spending limits are policies" removed | Opus: the Policy row contained domain meaning |
| The two kinds of group describe the main scope; direct calls to Evaluation, Releases and Secrets are stated overlaps | Both: the test put several services in both kinds |
| A task agent has no continuing role or memory; the platform retains its identity, records and results | astra: the end of an agent was confused with the deletion of its records |
| Tasks coordinates retry, recovery and cancellation; the promise "without repeating its effects" is removed | astra: an effect guarantee was promised while contracts are deferred |
| Releases also covers the infrastructure the system manages; the example separates "the services apply" from "an implementation enforces them"; adoption order is the reference implementation's choice | Both: the improvement loop overclaimed its governance |
| "The Harness service and harness products" added | Opus: the Harness is both a peer service and the engine of every agent |
| People set the goals and services carry the other six parts; the agent definition is one route among several | Both: "each thing is carried by a platform service" contradicted the Goals row |
| Platform agents are marked provisional, with two sources of definition and an open bootstrap rule | Both: the v0.8 addition contradicted "the definition comes from a domain" |
| Mapping is many to many; one boundary per service is the reference implementation's experiment | Both: the deck alternated between the two |
| The five memory services are responsibilities and not exclusive bins | astra |
| "Job" removed from the Tasks row; a Role is a position with duties | Opus: both words still had two senses |

## Changes from v0.7 (The author's decisions, 2026-11-10 07:52)

| Change | Decision |
|---|---|
| "How agents fit" added to Step 4; the three parts of an agent are traced to a domain, the platform and a provider in Step 0 | The author: the domain figure was missing the agent definition and how agents fit. The agent definition is the common form in which a domain's meaning reaches the platform, although the domains themselves differ. |
| **Persistent agent** and **task agent** added (Step 0, glossary, relations) | The author asked whether each domain goes one to one with a persistent agent. That holds for most domains of the reference implementation and is not a rule of the model: the Software Factory has several persistent agents, and every persistent agent starts task agents. |
| A platform service may be provided by an agent (Step 4) | Sagan's addition, kept as provisional by the author on 2026-11-10 after the reviews: two persistent agents of the reference implementation route messages and watch reliability, which are platform services and not domains. |
| What a service does is its **responsibility**; "job" now means only scheduled work | The author, 2026-11-10 08:19: calling the service names jobs collided with jobs as scheduled things. Each service has one responsibility, which also matches the single-responsibility principle the architecture follows. |
| The six-stage workflow keeps its sentence and loses its figure | The author: drop figure 5b. The stages are a template, and domains differ most in their workflow. |

## Changes from v0.6 (The author's decisions, 2026-11-10 07:04)

| Change | Decision |
|---|---|
| **Secrets** added to Governance (22 services); Identity narrowed to who is acting | The author: secrets is the general term for what the platform's components should not know directly. Identity and secrets fail differently: a wrong identity loses track of who acted; a leaked secret lets someone else act. "Secrets" is also the product word (Google Secret Manager, AWS Secrets Manager). |
| "Where memory lives" added after Step 3 | Memory is spread across Harness, Sessions, Memory, Retrieval and Artifacts; the table keeps a reader from concluding that the model lacks it. |

## Changes from v0.5 (The author's decision, 2026-11-10 06:59)

| Change | Decision |
|---|---|
| Skills are **procedural memory** and are kept in Memory (Knowledge), which now holds three kinds: semantic, episodic and procedural | A skill is know-how learned and refined from experience, and most continuous improvement lands as a changed skill. The memory work had already classified skills this way (CoALA's procedural memory). |
| The Registry **indexes** skills; it no longer holds them | Finding and loading the right skill is a capability; keeping the skill current is a knowledge responsibility. |

## Changes from v0.4 (The author's decision, 2026-11-10)

| Change | Decision |
|---|---|
| Relations between the six groups added to Step 2: four working groups and two cross-cutting groups | v0.4 defined relations between layers but none between groups. The author asked whether groups relate and approved adding the relations. |
| "Group" kept; "module" reserved for implementations | A group is not a unit that is built or replaced. A service is. "Module" already names a unit of the LifeOS implementation. |
| The implementation is written "LifeOS" | The author, 2026-11-10: the name in documentation is LifeOS. |

## Changes from v0.3 (The author's decisions, 2026-11-09)

| Change | Decision |
|---|---|
| Foundation split into **Infrastructure** and **Providers**, side by side beneath the platform | The physical side (machines, CI runners, builds) needed its own place. The two sit at the same level because neither runs on the other. |
| **Implementation** is the relation at every layer; the word "method" is dropped | Agent Scrum is an implementation of the Software Factory, as LifeOS is an implementation of the platform. |
| Old Steps 5 and 6 merged into "Every part has implementations" | One idea now, not two. |
| A domain's "Method" row became **Workflow** | It names how work moves, without using "method" as a level. |
| Environments reworded to sit on Infrastructure; CI added to the example | Shows how one familiar thing divides across the layers. |
| CI restated as a practice of the Software Factory domain that uses Environments and runs on runners (2026-11-10) | The author: CI belongs to the Software domain. The earlier wording said the layers divide CI in three, which overstated a plain uses relation. |
| "Capabilities" kept | Decided against "Access" and "Resources". |

Earlier changes and the review points not adopted are in `warm-model-v0.2.md` and `warm-model-v0.3.md`.
