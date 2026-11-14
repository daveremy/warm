---
title: "WARM: the Working Agents Reference Model, v0.12"
date: 2026-11-11
author: sagan
issue: lifeos#3502
status: v0.12 applies a documented search and a part-by-part comparison with fourteen published reference models in two rounds (prior-work/synthesis.md, prior-work/synthesis-round2.md). The owner accepted the changes as a whole on 2026-11-11, including a 25th service, Lifecycle. A second rater and a full read of one source are in progress.
---

# WARM: the Working Agents Reference Model (v0.12)

WARM names the parts of a system in which agents do sustained work, and how the parts relate. It comes from three sources, in this order: published work (a survey of how the industry describes agent platforms, a documented search, and a part-by-part comparison with fourteen published models); the experience of building and running one system; and a detailed mapping of the model to three existing agent platforms. Each source changed the model.

The model is explained in six steps, then three examples, then the mapping. The steps are an order of explanation; they are not layers of the system. A glossary near the end defines every term in one place.

## A request to follow

One request is used throughout. A person asks their finance agent: "There is a duplicate charge from the gym this month. Dispute it."

The finance agent can find the charge. It may not write to the merchant: messages sent in the person's name are the responsibility of another area of work, Communications, and need the person's approval. So the request crosses two areas of work, uses a dozen platform services, and stops once for a person. The full trace is in "Example: one request across two domains". Each step below names the part of the request it explains.

## Step 0. Scope

**Idea: WARM describes the system around agents: who directs them, what work they do, and what they run on.**

An **agent** is an identified actor that carries out one or more assigned roles. In the request, the finance agent is one agent and the communications agent is another. The agent is the identity, not a running copy of it: an **instance** of an agent can be restarted or moved, and it is not the agent. Every agent identity traces to a person who is accountable for it. WARM did not originate the idea of an agent as an identified principal: Charterion and AOS state it, and Charterion credits security guidance published since 2025.

An **agent definition** describes a role: its instructions and the skills it refers to. A definition is not the agent. Several agents can use one definition (two developer agents working two issues), and a definition can be revised while the agent stays the same agent. An agent's identity, memory and history persist through a change of definition, harness or model. Any of those changes can alter how the agent behaves, so each is versioned and evaluated (Releases and Evaluation, Step 3).

An agent **runs on** the platform. The **Harness**, a platform service, runs each agent's loop: it sends context to a model and carries out the tool calls the model asks for. The model is called through the platform, which may choose a different model for different requests.

A role that does the work of a domain belongs to that domain (Step 4). An agent may hold more than one role. For each task one role is active, and one domain is accountable for the result.

Agents are of two kinds, by what persists.

| Kind | What it is | What persists | Example |
|---|---|---|---|
| **Persistent agent** | Holds its roles across many sessions and tasks. | Its identity, its session history, what it has learned, and a channel on which people and other agents reach it. | A finance agent that a person consults, and that remembers the accounts and last month's decisions. |
| **Task agent** | Holds a role for one task: it is started for the task and ended when the task ends. Another agent starts it (a subagent), or a schedule or an event does. | No continuing role and no memory of its own. It returns a result and work products. The platform retains its records. | A developer agent started for one issue, which delivers a pull request and ends. |

A task agent is also called a worker agent. The difference between the kinds is lifetime and nothing else. A persistent agent can work unattended, and a task agent can ask a person a question. The role a task agent fills determines the domain accountable for its work; who started it is a separate fact (a finance agent may start a research worker). A task agent acts under an identity of its own, and the record says on whose behalf it acts.

The end of a task agent is not the deletion of its records. The platform retains the identity under which it acted, its transcript and its results for as long as the rules on stored data say (Policy, Step 3), so that a past action can be attributed and investigated. The platform can also checkpoint and resume a task agent while its task is running.

WARM does not describe how a single agent reasons (planning, reflection); research papers already model that. WARM names no vendor and no product. A real system that fills in one of its parts is an **implementation** of that part (Step 5).

## Step 1. The layers

**Idea: people direct domains; the work of a domain runs on a platform; the platform runs on infrastructure and calls providers.**

| Layer | What it is | Examples |
|---|---|---|
| **People** | Those who direct and approve the work. | A developer; a team lead; the person who owns the accounts |
| **Domains** | Areas of work. Each is defined by a charter; agents and people fill its roles and do the work. | Software Factory, Finance, Communications |
| **Platform** | Services that agents in any domain can use. | Sessions, memory, scheduling |
| **Infrastructure** | Where everything runs. | Machines, CI runners, storage, network |
| **Providers** | What the platform calls and does not operate. | Model vendors, external services |

These are logical categories, relative to the boundary of one system. They are not a deployment diagram. The platform executes on infrastructure and calls providers. A model that the system hosts itself runs on its infrastructure; the Models service still mediates the call.

A system that agents act on is reached through Tools, and it is a Provider when this system does not operate it. An application that calls an agent comes in through Channels. It is a client of the system and sits in none of the five layers.

"A domain runs on the platform" is shorthand: the work of the agents that fill the domain's roles runs there.

People appear in the figure as those who direct and approve. People also fill roles, request or receive results (a customer), and are the subject of the work (the person whose health or money it is). These relations do not carry the same authority. WARM has not developed them in detail. One is stated: when a person is the subject of stored data, Policy's rules on what is kept include that person's right to see, correct and delete it.

### What belongs in the platform

One test places a responsibility. **A responsibility belongs to the platform if it works the same whatever the work is about. It is domain work if what it does depends on the subject of the work.**

In the request, holding an action until a person approves it works the same for an email, a payment or a merge, so Approvals is a platform service. The rule "every message in this person's name needs approval" is about one area of work, so the Communications domain supplies it, and the platform applies it.

The test classifies the responsibility and its contract, not how it is built:

- A platform service may use a model or an agent inside it. An evaluator that judges a work product against criteria it is given is still providing a platform service.
- Domain work may be a fixed script. A calculation, a connector to one bank and the tests of one codebase are domain logic, although nothing in them decides anything.
- One component can implement both. A mapping records the split, or leaves the placement open.
- Who uses a service today does not place it. A system with one agent needs no agent messaging; Messaging is still a platform service.

An older statement of the same idea is that the platform supplies mechanisms and a domain supplies meaning. The wording follows the separation of policy and mechanism in operating-system design (Levin, Cohen, Corwin, Pollack and Wulf, "Policy/Mechanism Separation in Hydra", Proceedings of the 5th Symposium on Operating Systems Principles, 1975, pp. 132-140).

The test is a design choice and not a finding. A reusable responsibility discovered inside a domain is treated as a gap in the platform, so no observation can refute the test. What can be checked is its usefulness: whether a service stays meaningful, unchanged, when a second and a third domain use it.

### When the Domain layer matters

The Domain layer matters once a system has several areas of work on one platform. A system built for one purpose has one domain and may never name it. The three platforms mapped to WARM are of this kind, or leave domains to the customer: none has a domain layer.

## Step 2. The platform is six groups of services

**Idea: the platform answers six questions about agents.**

| Group | The question it answers |
|---|---|
| **Runtime** | How, where and when do agents run? |
| **Knowledge** | What do agents know and keep? |
| **Capabilities** | What can agents use? |
| **Interaction** | Who do agents work with? |
| **Governance** | What are agents allowed to do? |
| **Operations** | How do we see it, judge it, improve it and keep it running? |

### How the groups relate

The six groups are of two kinds, by the main scope of their services. Four are **working groups**: an agent mostly uses their services to do its work. Two are **cross-cutting groups**: their services mostly apply to what happens in every other group.

| Group | Kind | Relation to the other groups | The services that make it so |
|---|---|---|---|
| **Runtime** | working | The center. Work happens in a session or a task, and the other working groups are used from there. | Harness, Sessions, Tasks; Lifecycle keeps the list of which agents exist |
| **Capabilities** | working | **Used by** Runtime. | The Harness sends context to Models, carries out calls through Tools, and finds the definitions of agents, tools and skills in the Registry. |
| **Knowledge** | working | **Used by** Runtime. | The Harness reads Memory and Retrieval into the context window and writes back what was learned. A task stores its work products in Artifacts. |
| **Interaction** | working | **Connects** Runtime to other agents, to people and to applications, in both directions. | An agent finds who is responsible in the Directory and reaches them through Messaging and Orchestration. People and applications reach agents through Channels. A message, an assignment or a request starts or resumes a session or a task. |
| **Governance** | cross-cutting | **Constrains** the other five. | Identity establishes who is acting on every tool call, message and memory write, and can revoke an identity. Secrets releases what that actor may use without showing it. Policy decides whether the action may proceed, issues a grant when it may, and decides what happens to stored data. Approvals holds an action for a person. |
| **Operations** | cross-cutting | **Observes and changes** the other five. | Observability records what they did, Evaluation judges it, Improvement proposes changes from the evidence, Releases makes the changes, and Reliability restores what fails. |

Seven points follow.

1. **Governance covers an action only if the action passes an enforcement point.** A call that reaches a tool, a model or a store without passing one is not governed, whatever the rules say. Two of the three platforms mapped enforce policy only at certain gateways or separately per product. "Constrains the other five" states what the group is for. An implementation has to show where each kind of call is checked. The condition can be checked: compare a record kept at the resource, of what the tool, model or store received, with what the enforcement point admitted; an action in the first and not in the second did not pass the enforcement point. AAM/5C (Goujon) states the check and its blind spot: actions taken under a person's or a script's identity.
2. **A positive decision is issued as a grant.** When Policy allows an action, the authority to carry it out is a grant: scoped to that action or that task, limited in time and revocable. The grant is checked again when the action runs, not only when it is requested, because a deferred or delegated action may run long after the decision. AAM/5C gives deciding, issuing and enforcing to separate components; WARM keeps all three in Policy and leaves the split to an implementation. The request already follows this order: the mail credential is released only after the person approves. A grant passed to another agent can only be narrower than the one it came from, in scope, in time and in budget.
3. **The actor that proposes or performs an action does not approve it.** An agent cannot grant itself authority, and whoever writes a rule does not approve it. In the reference implementation one agent writes a change and another reviews it, and a person approves a message sent in their name. Agents started by the same agent do not count as independent of each other for separation of duties.
4. **A system needs a way to stop an agent that does not pass through the agent or through a service the agent provides.** Tasks cancels a unit of work, Lifecycle suspends or ends a running agent, and Identity revokes its identity. This generalizes the provisional rule in Step 4 about agents that provide Messaging or Reliability, from repair to stopping.
5. **The two cross-cutting groups apply to each other.** A release can require an approval, so Governance constrains Operations. An approval decision is recorded, so Operations observes Governance.
6. **A cross-cutting group still uses working services.** Approvals reaches the person through Channels. Observability stores its records somewhere. Cross-cutting describes what a group applies to, not what it is built from.
7. **The relations are not a layering.** No group sits on another, and a system that lacks a service lacks the relations that service carries.

The kind describes the main scope of a group and does not sort every service cleanly. A working service is mostly called for its result. A cross-cutting service mostly applies to actions whose purpose lies elsewhere, and it has to be able to act on an action without the cooperation of the agent that performs it. Some cross-cutting services are also called directly: an agent asks Evaluation for a verdict, Releases for a deployment, or Secrets for the use of a credential. Some working services apply without being called: Environments isolates whatever an agent does. The stated overlaps are part of the model.

These relations are stated between groups and are derived from the responsibilities of the services in Step 3. The dependencies between individual services are part of each service's contract, which WARM does not yet specify.

### Three kinds of human decision

People take three kinds of decision in a system, and Approvals covers only the second.

1. **Steps reserved for people.** An agent may not carry them out at all, although it may prepare them. This is a domain rule. In the Finance example the person places every order himself.
2. **Actions held until a person approves them.** The agent proposes the action, and it runs only after a person agrees. This is Approvals.
3. **The granting of authority itself.** Only a person gives an agent its authority: the roles and rules under which Policy then issues grants for single actions. With point 3 above, an agent cannot grant itself authority.

Charterion separates the three most precisely; AEON and CEAD make the same separation in part.

An agent that signs off on another agent's work is none of the three. It acts under a rule that people wrote, so it is Policy, and the review it relies on is Evaluation. In the reference implementation one agent merges changes that another agent has reviewed.

### Concerns that are not groups

Some concerns touch several groups without being one. Security touches Governance, Runtime and Capabilities. Cost touches Models (which model is used), Policy (spending limits), Scheduling (how much may run at once) and Observability (what was spent). A budget is carried in a grant, enforced by Scheduling's limits and metered by Observability. Tenancy, several organizations or users on one platform, touches Identity, Policy, Environments and the services that store data.

### Group, service and module

A **group** is a set of services that answer one question; it is a classification with stated relations, and it is not a unit that is built or replaced. A **service** is the unit with one responsibility and a boundary. A **module** is a unit of an implementation. WARM does not use "module" for anything in the model, because one service may be implemented by several modules and one module may implement parts of several services.

## Step 3. Twenty-five services

**Idea: each group holds a few services, and each service has one responsibility.**

| Group | Service | Its one responsibility | Industry terms |
|---|---|---|---|
| Runtime | **Harness** | Run the agent loop: decide what goes into the context window, send it to the model, and carry out the tool calls the model asks for. | harness, agent loop, context management, compaction |
| Runtime | **Sessions** | Keep the history and state of a stretch of an agent's work, so that the agent can pause, resume and hand off, and so that the record remains after the work ends. | session, thread, state, checkpoint |
| Runtime | **Tasks** | Track each unit of work (a task or run) from start to finish, and coordinate its retry, recovery and cancellation. It keeps the original request: its objective, its constraints and what counts as done. | runs, jobs, task lifecycle, durable execution |
| Runtime | **Environments** | Give each agent a place to act, isolated from the others, on the infrastructure: sandboxes, workspaces, browsers. | sandbox, runtime, workspace, computer use |
| Runtime | **Scheduling** | Decide when work starts: at a time, on an event, and within the limits on how much may run at once. | cron jobs, triggers, queues, concurrency limits, rate limits |
| Runtime | **Lifecycle** | Create, suspend, resume and end agents, and keep the list of which agents exist. | agent lifecycle, provisioning, decommissioning, orphaned agents, sprawl |
| Knowledge | **Memory** | Retain what agents learn across sessions (facts and events), with where each entry came from, and keep it current. | memory, memory bank, dreaming |
| Knowledge | **Retrieval** | Fetch material from named sources: documents, data, notes. | retrieval, knowledge base, grounding, RAG |
| Knowledge | **Artifacts** | Store what agents produce (reports, files, pages) and its versions. | artifacts, outputs, store |
| Capabilities | **Models** | Mediate requests to models and choose the model for each task, across more than one model or vendor. | models, model routing, multi-model |
| Capabilities | **Tools** | Mediate calls to tools, local or external. | tools, MCP, gateway, connectors |
| Capabilities | **Registry** | Hold the versioned definitions of agents, tools and skills, so that each can be found and loaded when a task needs it. | registry, catalog, discovery, skills, hub |
| Interaction | **Directory** | Record which domain is accountable for each responsibility, and how to reach a role of that domain. | (none found; see below) |
| Interaction | **Messaging** | Deliver messages between agents, and events to their subscribers. | agent-to-agent, A2A |
| Interaction | **Orchestration** | Coordinate assignments among agents, people and fixed steps: who does what, what depends on what, and the results that come back. | orchestration, subagents, handoffs, workflows |
| Interaction | **Channels** | Carry requests and results between agents and the people and applications that use them, on the channel each one uses. | channels, surface, agent interface, invoke API, endpoints |
| Governance | **Identity** | Establish who is acting: each agent, person and service, and on whose behalf; record the person accountable for each agent identity; and revoke an identity. | identity, agent identity, authentication |
| Governance | **Secrets** | Hold every value that platform components and agents must not know directly (API keys, passwords, tokens, account numbers), and release each one only to the component that needs it, at the point of use, without placing it in an agent's context; and rotate or revoke it. | secrets, secret manager, vault, credentials |
| Governance | **Policy** | Evaluate and enforce rules on what may be done, what may be said and what is kept: whether an action is allowed (a positive decision is issued as a grant), what content may enter and leave models and tools, and how long stored data is retained, when it is purged, how it is protected and what the person it is about may see, correct and delete. Domains and the platform's operator supply the rules. A decision may allow, deny, hold the action for a person, narrow it, or be unknown. | policy, guardrails, content filters, permissions, hooks, retention, TTL |
| Governance | **Approvals** | Hold chosen actions until a person authorizes them, and record the decision. | human in the loop, tool approval |
| Operations | **Observability** | Collect evidence of what agents and the platform did. | observability, tracing, audit log |
| Operations | **Evaluation** | Assess behavior and work products against stated criteria, before, during or after an action, and report "unknown" when a check could not run. Policy may use an assessment, such as a risk score, as an input to its decision. | evaluation, evals |
| Operations | **Improvement** | Turn evidence (traces, evaluations, reviews) into proposed changes to agents, skills and the platform. | recommendations, insights, optimization, self-improvement |
| Operations | **Releases** | Version and release changes to agents, skills, rules, the platform and the infrastructure the system manages, with a way back. | deployment, versioning, rollback, change management |
| Operations | **Reliability** | Keep services available and restore them after a failure. | operations, recovery |

These names are responsibilities, not products. One product may cover several responsibilities, one responsibility may be shared by several products, and a system does not need all twenty-five.

WARM names each service and its responsibility. It does not yet specify each service's contract: what it guarantees on failure, cancellation, delegation, stale state and recovery. Whether a retried task repeats an effect is an example: it depends on the contract between Tasks, Tools and the outside system. A contract also has to settle how an action's effects outside the system are undone; no service owns undoing yet. Three further questions are open: who decides an approval when the named person is unavailable, and how much one person can be asked to approve; whether the configuration that runs is the one that was reviewed; and which rule takes precedence when rules from different sources conflict.

A platform service has an explicit boundary and stated guarantees. Its implementation may be fixed code or an agent, and its results vary with its inputs and its state: Approvals returns approved, denied or still pending; Retrieval returns whatever the source now holds. A predictable contract is the aim. Identical results are not.

The word "job" is kept for scheduled work: a task that a schedule or an event starts. A script or an agent may carry it out.

### Six services the mapping changed

The mapping to three platforms changed this list in six places.

**Directory is new, and no mapped platform has it.** Each platform has a registry, which is a catalog: it answers "what agents, tools and skills exist". None records which area of work is accountable for what. v0.10 put the directory inside the Registry, which then carried three responsibilities. It is now a service of its own, in Interaction, because it answers "who do agents work with". Step 4 describes its entries.

**Improvement is new.** All three platforms run a loop that turns evidence from past work into changes: recommendations from traces and comparisons of versions on two of them, and on the third a loop that revises learned skills and promotes entries into memory. The reference implementation has one too (a retrospective at the end of each sprint; a nightly pass over its documents and memory). v0.10 had no place for it. In WARM, Improvement proposes, a person or a release process decides, and Releases makes the change. That separation is a choice of the model: one platform applies such changes by default with no approval, keeping a version to go back to.

**Skills are definitions, not memory.** v0.10 kept skills in Memory as procedural memory. Two platforms and the reference implementation keep them as versioned files that are loaded when needed and released like other changes; the third revises skills from experience and saves a version before each change. So the Registry holds skills, Releases changes them, and Memory keeps what agents learn: facts and events. A lesson that should change how a kind of task is done starts as a Memory entry or as evidence, and becomes a changed skill through Improvement and Releases.

**Channels serves applications as well as people.** All three platforms give a program a way to call an agent: an invoke interface, a streaming endpoint, an endpoint compatible with a model API. v0.10 had only Human channels. The service is renamed Channels and carries both.

**Tasks is a contract, not necessarily a store.** No mapped platform keeps a separate store of tasks. One uses the same checkpoints as its session history and its run log. One built a shared registry of tasks in March 2026 and removed it in September 2026, giving duplicated state as the reason. WARM keeps Tasks as a responsibility that every runtime has to meet: track a unit of work, retry it, cancel it. The cut between three services is by what is kept: the history of a stretch of work (Sessions), the lifecycle of a unit of work (Tasks), and what was learned (Memory). One store may serve more than one of them.

**Scheduling and Policy each gained a part of their responsibility.** Deciding what may run next when capacity is limited (queues, lanes, limits on concurrent work) is part of deciding when work starts, so it is in Scheduling. Rules on stored data (retention, purging, protection) are part of Policy; Step 0 already relied on them.

**Artifacts is unchanged, and no mapped platform provides it.** Each has only a partial counterpart to a versioned store for work products. WARM keeps the service, because sustained work produces reports, files and pages that outlast a session and need versions. An adopter should expect to build it.

### What the published models changed

The comparison with published models ("Compared with published models") ran in two rounds. The first, with six models, changed no service: it added to the responsibilities of five services and to the Registry's text, and it added three points to how the groups relate. The second, with eight more models, made eleven further changes, one of which adds a service, Lifecycle, and brings the count to 25. This subsection describes the larger changes of both rounds; the rest are listed in "Compared with published models".

**Grants, and the split of deciding, issuing and enforcing.** Yu et al., Zhu and AAM/5C each have a step that v0.11 lacked: authority scoped to one task or action, limited in time, issued only on a positive decision, checked again when the action runs, and revocable. WARM calls it a grant and puts it in Policy (point 2 of "How the groups relate"). AAM/5C gives proposal, decision, issuing, enforcement and execution to five different holders, with separate signing keys, so that no one component can authorize itself. WARM keeps deciding, issuing and enforcing in one service and leaves that split to an implementation.

**Separation of duties.** The same three sources state that whoever proposes or performs an action does not approve it. Yu et al. state it for people (the approver "is not the submitter"), Zhu for agents ("No agent controls the full chain"), and AAM/5C for the people who write and audit rules. v0.11 had no such rule. It is now point 3.

**Stopping an agent.** Five of the six sources have a way to pause, suspend or stop an agent at run time: Microsoft's "pause/disable an agent class", AWS's "circuit breakers for abnormal behavior patterns", Google's "monitor, override, and pause agents", Zhu's stop path that does not pass through the data plane, and AAM/5C's emergency stop "independent of the authorization chain". v0.11 had no place for it. The first round gave suspension to Identity. With Lifecycle (below), a running agent is suspended or ended by Lifecycle, its identity is revoked by Identity, a unit of work is still canceled by Tasks, and point 4 requires that the stop not pass through the agent.

**Registration as a gate, and owners on entries.** In all three vendor architectures a registry is a governance record, and registration is a precondition for use: Google's agents "only connect to inventoried, administrator-approved MCP endpoints". The Registry keeps its one responsibility, and two relations are added. Policy may require that an agent, tool or skill be registered before it is used, and adding an entry is a release, which Evaluation and Approvals can gate. Not being registered can deny an action; finding a destination still grants nothing. Each entry also names its owner, the person or team who answers for the definition. The owner of an entry is separate from the Directory's accountable domain, which answers for a responsibility. The second round added one statement from AOS and from Steinder and Franke: a tool's definition in the Registry declares its side effects, whether they can be undone and whether a retry is safe. That declaration is what lets Tasks decide whether to retry, and it gives the open question on undoing a concrete input.

**Policy and content.** Microsoft, AWS and Google place the filtering of prompts, model outputs and tool payloads (injection, harmful content, sensitive data) in their governance components. v0.11 worded Policy for actions and stored data. Policy now covers what may be said as well, and "content filters" joins its industry terms. WARM names no separate guardrail service.

**Events.** Yu et al. have a responsibility for asynchronous and event infrastructure that carries events between components, and one of the three platforms mapped earlier had outbound events. In v0.11 Messaging delivered only between agents, and no service distributed events. Messaging now delivers events to their subscribers as well. Scheduling still starts work on an event.

**Lifecycle, the 25th service.** Nothing in WARM owned which agents exist. Three of the four platform-like models of the second round make the lifecycle of a running agent a top-level component: AOS's "Agent lifecycle", whose representative failure is an "Orphaned agent"; Steinder and Franke's first primitive, "Agent lifecycle"; and EAAF's Agent Lifecycle Manager, which "manages the complete creation, maintenance, and retirement of agents". The platform mapping had recorded agent provisioning in OpenClaw as a misfit; AAGMM, a governance maturity model that the search found, is about agent sprawl; and Microsoft, AWS and Google can pause or disable an agent at run time. Before this round the pieces were spread over Identity, Sessions, Tasks and Orchestration, and no service could say which agents are running or who started one. Lifecycle creates, suspends, resumes and ends agents, and keeps the list of which agents exist. It is the first Runtime service that concerns an agent as a whole: Sessions concerns a stretch of an agent's work, and Tasks a unit of work. Its failure case is an orphan, an agent that nobody owns or lists. In the reference implementation it is the launcher that starts, stops and lists the persistent agents, and the board that lists running task agents. That the gap is real is well supported. Making it a service, and not a widening of Identity and Tasks, is the author's call, and the owner decides it.

**Assessment before and during an action.** All four platform-like models of the second round assess risk, confidence or trust at run time and use the result to decide whether an action proceeds; WARM's Evaluation judged only finished work. Evaluation now assesses before, during or after an action, and Policy may use an assessment as an input. That the gap is real is well supported; its placement in Evaluation, and not in a new service, is less certain.

### The Harness service and harness products

The word "harness" names two things. The Harness *service* runs each agent's loop: it assembles the context, calls the model, and carries out tool calls. A harness *product* usually bundles the loop with several other services, such as sessions, tool mediation, subagents and permission checks. A mapping of a real system records the bundle: which of the twenty-five responsibilities the product provides, and which are built around it. One of the mapped platforms can replace the loop while it "keeps ownership of channels, sessions, policy, and state", which is the same boundary.

### Where what an agent knows is kept

What an agent knows and remembers is spread across six services, by how long it lasts and who wrote it.

| What is kept | Service |
|---|---|
| What is in the context window now (working memory) | Harness, which decides what goes into context |
| The history of one stretch of work | Sessions |
| What agents learn and keep across sessions: facts and events | Memory |
| How to do a kind of task: skills, written by a person or revised from experience | Registry (with Releases for each change) |
| Material that is fetched when needed | Retrieval |
| What agents produce | Artifacts |

Memory keeps its entries current: it records where each came from, and it revises or retires entries that later evidence contradicts.

The six are responsibilities and not six bins that each piece of content fits exactly once. One report can be stored by Artifacts, fetched by Retrieval, placed in the context window by the Harness, recorded in a session, and used to write a Memory entry. Retrieval fetches material whoever wrote it. Sessions keeps a record after the work ends, for as long as the rules on stored data say.

## Step 4. A domain is a charter for an area of work

**Idea: a domain says what the work is, and the platform's services carry it.**

A domain does not act. It is a definition: its goals, roles, workflow, knowledge, tools, rules and acceptance criteria. The agents and people who fill its roles act. A domain resembles a department's charter more than a department's staff.

| A domain defines | What it is | Platform services that commonly carry it |
|---|---|---|
| **Goals** | What the work is for, and who is accountable. | (set by people) |
| **Roles** | The positions in the domain and their duties, filled by agents and people. Each role that an agent fills is written as an agent definition. | Registry (definitions); Directory (how to reach a role) |
| **Workflow** | How work starts, and how it moves from request to result. | Tasks, Scheduling, Orchestration |
| **Domain knowledge** | What must be known to do this work, including its skills. | Memory, Retrieval, Registry (skills) |
| **Domain tools** | Connections this work needs. | Tools |
| **Domain rules** | Limits, approvals and preferences this work needs. | Policy, Approvals; other services for other rules |
| **Acceptance criteria** | How to tell that a work product is good. | Evaluation |

People set the goals. The third column lists common carriers. It is not exclusive or complete. Rules that authorize or forbid an action go to Policy and Approvals. Other rules go to the service that applies them: a preference for a model goes to Models, the order in which sources are trusted goes to Retrieval or stays in the domain's own logic. A mapping records the carriers a system actually uses.

A domain needs no platform service of its own. If it needs a reusable responsibility the platform lacks, that is a gap in the platform. A new domain can still require new work, such as a connector to a system no other domain uses. The domain supplies that logic, and Tools carries it.

### Domains have responsibilities

Each domain holds a cohesive set of responsibilities: the things its roles are accountable for. (The idea of a boundary around an area of work, inside which terms and rules have one meaning, is the bounded context of Domain-Driven Design.) Finance is responsible for tracking spending, watching subscriptions and reporting where the money goes. Communications is responsible for the inbox and for messages sent in a person's name. The responsibilities of one domain belong together because they draw on the same knowledge, tools and rules and serve the same goals.

A responsibility is stated at the grain at which an agent of another domain would hand work over. "Messages sent in a person's name" is a responsibility. One checking account is not: it is knowledge and a tool inside Finance. At that grain, exactly one domain is **accountable** for each responsibility. Other domains may contribute to the work or carry out part of it. The software domain builds the finance domain's bank connector, and Finance remains accountable for the books. Where a system serves several products, projects or accounts, a responsibility is scoped by them: publishing for one product and publishing for a personal account can have different accountable domains. People set this division, as part of directing the domains.

The division is recorded in the **Directory**. An entry holds a scoped responsibility, the domain accountable for it, and how to reach a role of that domain: an agent that exists, or how to start one. It works as a company directory does, for responsibilities. An agent may be given a summary of the directory when it starts, and it consults the Directory itself when it is unsure or when the summary may be out of date. Finding a destination grants nothing: whether the request may be made, and whether the work may be done, are still questions for Identity, Policy and Approvals.

**Intake routing.** An inbound request that names no agent still has to reach one. Channels delivers by address: a conversation with the finance agent reaches the finance agent. When the address does not settle it, the request is routed by what it is about, using the Directory. The component that classifies the request may be an agent providing this platform service. All three vendor architectures compared have such a router (Microsoft's Classifier, AWS's routing workflow, Google's dispatcher agent). That the gap is real is well supported; where routing belongs (Channels, the Directory or Orchestration) is less certain.

In the request, the finance agent knows from the directory that messages in the person's name belong to Communications, and how to reach its agent.

When an agent meets work that another domain is accountable for, it hands the work over and gets a result back. Orchestration tracks the assignment and the result. Messaging carries the request to an agent that exists; if the responsible domain has no agent running, the platform starts one. A handoff can also be carried as a tool call, when the other agent is exposed as a tool; Orchestration still tracks the assignment. Delivery alone establishes neither that the work was accepted nor that it was done. The work is an ordinary task in the responsible domain, requested by an agent and not by a person.

A second example is research. In the reference implementation a person converses with the research agent directly, and the agents of other domains hand it questions. Fetching a page or running a search works the same whatever the question is, so fetching is a platform service (Retrieval). Deciding what to look for, checking one source against another and saying how far the evidence goes is an area of work with its own knowledge, tools and criteria, so research is a domain. Communications receives work because of rules (who may send in a person's name). Research receives it because of skill and tools.

### How domains depend on one another

Domains depend on one another as the departments of an organization do. An agent in one asks an agent in another in ordinary language, the other uses its judgment, and the two sort out what was unclear. This suits agents, whose strengths are language and judgment.

Ordinary language does not mean nothing is agreed. Who is accountable, who may authorize what, what result is expected and when to escalate are agreed in advance, as they are between departments. In the reference implementation, a message in a person's name is sent only on that person's approval, whoever asked for it. How much structure an exchange has (a free request, a brief with fixed fields, a required result format) is a choice of the workflow.

An agent reaches a platform service differently: through a defined interface, with stated guarantees.

The division of responsibilities is also a source of questions about a system. A responsibility with no accountable domain is a gap. Two domains accountable for the same scoped responsibility is an overlap. Work carried out by another domain is not by itself misplaced: delegation, consultation and shared inputs are normal. A map of the reference implementation raised candidates of each kind. They have not been verified.

### How work starts

Work in a domain starts from a trigger:

| Trigger | Example | The service it arrives through |
|---|---|---|
| A person or an application asks | A conversation with the finance agent | Channels |
| Another agent asks | The finance agent hands over an email | Orchestration, Messaging |
| A time or an event arrives | A nightly sync; a new message in the inbox | Scheduling |

A trigger may start work at once or add it to a backlog. Pending work can be carried out by a script, by one agent, or by a coordinating agent and several task agents. A job is work that a schedule or an event starts; whatever carries it out need not be an agent.

Where the work runs is a separate choice. The reference implementation ran unattended work inside its persistent agents' conversation sessions twice: first periodic checks, then sprints run inside the session of the agent that planned them. Both times the work filled the conversation's context and each delayed the other, and both times the remedy was to move execution out of the conversation, into scheduled jobs and task agents. One of the mapped platforms, OpenClaw, moved its periodic checks into ordinary scheduled jobs between July and October 2026, independently. This is guidance from experience and not a rule of the model. Other arrangements can work, and separate execution does not remove all interference: workers still share tools, rate limits and stored state.

A durable backlog is one reason to give a domain a separate team (a coordinating agent and task agents). The choice between one worker and a team depends on volume, how much can run at once, the cost of coordinating, and whether the stages are independent. Execution can pause for a person's approval.

### How agents fit

For each role an agent fills, a domain writes an agent definition. The Registry holds it. The Harness loads it, and from then on the agent is doing the domain's work on the platform's services. The definition is not the only route: the domain's rules reach Policy and Approvals, its criteria reach Evaluation, and its knowledge reaches Memory and Retrieval, each through its own service.

WARM sets no number of agents per domain. A domain may have one persistent agent that holds its main role, several persistent agents with different roles, or none, with task agents started when work arrives. One persistent agent may hold roles in more than one domain. A persistent agent commonly starts task agents for parts of its work, so a domain with one persistent agent still runs many agents over time.

**Provisional.** A component that provides a platform service may itself be an agent: a router that delivers messages, a reviewer that evaluates work. Such a role belongs to the platform. Its definition comes from whoever operates the service and not from a domain. An agent in such a role still uses the platform like any other agent, and it has to meet the same service boundary as any other implementation of that service. One consequence needs a rule that WARM does not yet state: an agent that provides Messaging or Reliability cannot rely on its own service to recover, so it needs a way to start and be repaired that does not pass through itself. In the reference implementation two persistent agents do some work of this kind along with domain work. Their responsibilities are classified one by one, and several are unresolved.

### A template for workflow

Work in many domains passes through the same six stages, which WARM offers as a template, not a requirement: **intake → plan → execute → verify → report → improve**. In the last stage a domain changes its own way of working from evidence. The platform supports that with Evaluation (the evidence), Improvement (the proposed change) and Releases (the rollout).

## Step 5. Every part has implementations

**Idea: WARM is abstract; a real system implements one of its parts.**

"Implementation" is one relation, and it applies at every layer.

| Part of WARM (abstract) | An implementation (real) |
|---|---|
| A domain: the Software Factory | **Agent Scrum**: named roles, a sprint backlog, reviews, a wrap |
| The platform | A harness plus what is built around it. In the reference implementation: Claude Code and the LifeOS tooling. Also: each of the three platforms mapped below |
| Infrastructure | A server, its CI runners, backups and network. In the reference implementation: a remote Linux server |
| Providers | The model vendors and external services a system uses |
| The agents of a domain | In the reference implementation: one persistent agent for each of six domains, several for the Software Factory, and task agents started by all of them |

A domain can have more than one implementation (Scrum and Kanban both implement software development), and an implementation's ideas can be reused in another domain.

The mapping between services and components is many to many. One boundary for each service is an experiment of the reference implementation and not a rule of the model.

A full system is described by mapping its parts to WARM. For each platform service the mapping records which component implements it, who supplies that component (the harness vendor, the builder of the system, a third party), who operates it, what it guarantees, and what evidence the entry rests on. One service can have more than one implementation. An entry may be left unresolved.

Suppliers of a service change over time. Harness vendors now supply services that builders used to write themselves (sessions, memory, scheduling and messaging are recent examples). A builder who keeps each service behind a clear interface can change its supplier with less rework.

Uses of the model:

- **Describe a system:** map each part to a layer, a service or a domain. A part that fits nowhere is a question: the model may lack something, the part may mix two responsibilities, or it may be outside the model's scope. A component that implements no platform service is not a fault; it may be domain logic.
- **Place new work:** does it work the same whatever the work is about (Step 1)? If so, which question does it answer (Step 2)?
- **Compare systems:** list, per service, who supplies it, what it guarantees, and what is unresolved. Two services with the same name are not thereby equivalent.
- **Structure a body of writing or code:** one unit per part.

## Example: one request across two domains

"There is a duplicate charge from the gym this month. Dispute it." This is one illustrative path. Another workflow may omit, reorder or add steps, and decisions that belong to a domain enter at every step.

| Step | What happens | Domain | Platform services |
|---|---|---|---|
| 1 | The request reaches the finance agent in the conversation the person is using. | Finance | Channels, Identity, Sessions |
| 2 | The finance agent finds the two charges and checks them against past decisions. | Finance: its bank connector, its knowledge of the accounts | Harness, Models, Tools, Memory, Retrieval; Policy checks each call |
| 3 | A dispute needs a message to the merchant. The finance agent sees that messages in the person's name belong to Communications. | Finance | Directory |
| 4 | It hands the work over: the facts, what is wanted, what counts as done. | Finance → Communications | Orchestration, Messaging, Tasks |
| 5 | The communications agent drafts the message, using the contact and the person's voice. | Communications: its knowledge and its rule that every such message needs approval | Harness, Models, Retrieval |
| 6 | The proposed send is checked. The rule requires a person, so the action is held and the person is asked. | Communications | Policy, Approvals, Channels |
| 7 | The person approves. Only then is the mail credential released and the message sent. | Communications | Approvals, Secrets, Tools |
| 8 | The result goes back. The finance agent records the dispute and tells the person. | Finance | Messaging, Orchestration, Memory, Channels |

Step 6 has three other outcomes: the person denies the send, changes the draft, or does not answer. In each case nothing is sent, and the finance agent is told that the work is denied or still pending.

Throughout, Tasks tracks each unit of work, Observability records each step, and Evaluation can check each result against the criteria of the domain accountable for it. A scheduled scan could have found the duplicate and started the same work with no conversation; step 1 would then be a job started by Scheduling.

The steps follow the reference implementation's rules for email. They are an illustration of the model and not a record of one run.

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

Continuous integration (CI) belongs to the Software Factory. It does not work the same whatever the work is about: what is integrated, which checks run and what passing means are all about code. So CI is part of this domain's workflow, tools and acceptance criteria. The general parts beneath it are platform services: Environments gives a build an isolated place to run, Scheduling starts it on an event, Tasks tracks the run, and Evaluation reports the verdict. The runners are Infrastructure.

One property is prominent in this domain. Its work products are software, and the platform is software. So the Software Factory can build and change the platform it runs on, and the tools the other domains use. Other domains change the system too (a security domain changes policies; every domain improves its own way of working, and any domain may produce software). In the reference implementation the Software Factory is accountable for changes to platform software.

When the work is building the platform or changing the infrastructure, the same services still apply: Policy and Approvals gate those changes, Evaluation judges them, and Releases versions them and keeps a way back. The model states that the services apply. It does not show that an implementation enforces them. That requires a control that an agent cannot change by itself, such as an approval or deployment authority outside the agent's reach.

For this reason the reference implementation got the platform and the Software Factory working first: the two improve each other, and every other domain benefits. A team that starts from a managed platform or from another domain may choose a different order.

## Example: Finance

Finance is a second domain set against the seven rows. The entries are simplified from the declared configuration of the reference implementation's finance agent.

| Step 4 asks for | In the reference implementation |
|---|---|
| Goals | Know where the money goes, and track spending against the plan |
| Roles | A financial advisor agent, which gathers and analyzes. A person, who decides, approves every order and places it himself |
| Workflow | Conversations with the person. Scheduled jobs gather data, scan for alerts and write summaries. No standing backlog was found |
| Domain knowledge | The accounts, the plan, and past decisions on how to categorize spending |
| Domain tools | Connections to banks, a budgeting service and a brokerage |
| Domain rules | The agent never moves money or changes a position; no scheduled job or task agent trades; bulk changes and deletions need the person's confirmation |
| Acceptance criteria | A balance carries its time and names any stale source; categorization follows the recorded decisions; most other judgments are the person's |

The rules are declared in the agent's definition, a hook and a script. They are candidates for enforcement by Policy and Approvals. How much of them those services actually enforce has not been verified, and one rule (the thresholds for an alert) lives in a script that Policy does not read.

Work here starts from a person's request or from a schedule. The scheduled jobs are scripts, and anything they find that needs judgment waits for the agent to read it in a conversation. That is how this implementation is built today and not a property of the domain: a job could start a task agent that judges and escalates.

The seven rows describe this domain, with two strains the model does not yet resolve: the person is the subject of the work as well as its director, and the person carries out some of the work himself. The map was made by the model's author and is not an independent test.

## Tested against three platforms

On 2026-11-11 WARM v0.10 was mapped to three agent platforms that its author did not build: Amazon Bedrock AgentCore; LangGraph with LangSmith and LangSmith Deployment; and OpenClaw. The mapping is the model's third source. It tested v0.10, and it changed the model.

**Method.** Three researchers each listed one platform's components from the platform's own documentation, without being shown WARM. The author wrote predictions before any list existed. Three mappers, one per platform and not shown the predictions, assigned every component to one WARM service, to another layer, to builder tooling, to a span of several services, or to "misfit". A doubtful fit was to be called a misfit. A service could be called absent only after a recorded search.

| Platform | Components | One service | Other layer | Builder tooling | Spans | Misfit |
|---|---|---|---|---|---|---|
| Amazon Bedrock AgentCore | 146 | 92 | 5 | 10 | 28 | 11 |
| LangGraph, LangSmith Deployment, LangSmith | 307 | 183 | 22 | 55 | 30 | 17 |
| OpenClaw | 848 | 329 | 212 | 256 | 38 | 13 |

**Predictions.** Of eight predictions, one was confirmed, three were partly right and four were wrong. The author predicted that 90% of components would map to one service or layer; 64% to 67% did. The author predicted that each platform would lack several services; AgentCore lacks one (Scheduling) and the other two lack none, though each has services only in part. The errors ran one way: the platforms cover more of WARM's list than expected, and they have more that WARM lacked. The prediction confirmed on all three: no platform has domains, or a directory of responsibilities.

**What fit.** Each platform's own top-level names overlap WARM's. AgentCore's include Harness, Memory, Identity, Policy, Observability, Registry and Evaluations. OpenClaw separates persistent agents from task agents, and can replace the agent loop while keeping the services around it.

**What did not fit, and what changed.**

| Finding | Platforms | Change in v0.11 |
|---|---|---|
| A program has no place to call an agent | All three | Human channels widened to Channels |
| The platform runs an improvement loop | All three | Improvement added to Operations |
| Tasks is not a separate store | All three | Tasks restated as a contract; the cut between Sessions, Tasks and Memory stated |
| Skills are versioned definitions | AgentCore, LangSmith | Skills moved from Memory to the Registry |
| The registry is a catalog; nothing records who is accountable for what | All three | Directory made a service of its own |
| Governance is enforced at certain points, or per product | AgentCore, LangSmith | The condition on Governance stated |
| Retention, purging and protection of stored data | LangGraph | Added to Policy |
| Queues, lanes and limits on what runs next | OpenClaw, LangGraph | Added to Scheduling |
| No versioned store for work products | All three | Artifacts kept; the gap stated |
| No domain layer | All three | "When the Domain layer matters" added |
| A platform service may use a model | AgentCore, LangSmith | The judgment test replaced |

Recorded and not adopted, each from one platform: payments, tenancy, agent provisioning, governance of a marketplace of plugins, outbound events, caching.

**Second rater.** A second rater sampled 36 assignments, 12 per platform, and assigned each independently. It agreed on 29, disagreed on 4 and found 3 unclear. All 12 assignments that the mappers had marked as clean fits were confirmed; every disagreement was in a row the mapper had marked strained, a span or a misfit. The second rater also found that the third platform's improvement loop had been filed under Memory, and corrected one date.

**Threats to validity.** The mappers and the second rater knew WARM, and all worked for the author. The sample is 36 of about 1,300 assignments. The evidence is documentation as of 2026-11-11 and not running systems. The author read the mappers' reports and not every row. The author changed the plan (mappers did the assignment, not the author) after the lists arrived, because they held about 1,300 components.

## Compared with published models

On 2026-11-11 WARM was compared, part by part, with fourteen published reference models and architectures, in two rounds. The first round compared v0.11 with six:

- Yu, Rabhi, Zhu and Lu, "A Reference Architecture for Integrating Agentic AI into Enterprise Software" (arXiv:2610.14818, October 2026);
- Zhu, "Fluid Structure, Rigid Record" (arXiv:2608.08516, August 2026);
- Goujon, "Agentic Architecture of Information Systems. The AAM/5C Model: A Reference Model for Distributed Autonomy" (arXiv:2610.30221, October 2026), all 120 pages;
- Microsoft's Multi-Agent Reference Architecture (the GitHub repository, every chapter);
- AWS Prescriptive Guidance on agentic AI (six guides);
- the agentic AI pages of Google Cloud's Architecture Center (17 pages).

The second round compared v0.11, with the first round's changes treated as planned, with eight more. They are the most complete of the sources that the documented search newly found:

- El Hassani, Charterion v2.0 (Zenodo 10.5281/zenodo.22829848, September 2026), read in part: about 110 of its 290 pages;
- Longmire and Longmire, AEON (Zenodo record 20349596, May 2026);
- deVadoss, CEAD (arXiv:2605.08258, May 2026);
- Salesforce Architects, "The Agentic Enterprise - The IT Architecture for the AI-Powered Future" (an undated page);
- Sharma and Shah, AOS-0001 (arXiv:2608.03214, August 2026), with its precursor AOS-0000 (arXiv:2606.01508);
- Steinder and Franke, "Towards an Agent Operating System - Lessons from Classical and Cloud OS" (arXiv:2607.25076, July 2026);
- Beheshti et al., the ASOC manifesto (arXiv:2607.12619, July 2026);
- Venkiteela, EAAF (Scientific Journal of Computer Science 2(1), 2026).

The comparison is part of the model's first source, published work. The first round changed the model in fifteen places (`prior-work/synthesis.md`, V1 to V15). The second made eleven further changes, one of them a new service (`prior-work/synthesis-round2.md`, A1 and A3 to A12), and it withdrew or narrowed WARM's claims to be distinct (A2).

**The documented search.** A separate reader ran a documented search with a written protocol (`prior-work/search.md`) in arXiv, OpenAlex, general web search, vendor and standards sites, and GitHub. Only the first page of results of each query was screened.

| Stage | Records |
|---|---|
| Screened, within the page caps | 1,634 |
| After de-duplication | 1,314 |
| Passed title screening | 258 |
| Met the inclusion rule | 61 |
| of which already known, the six of the first round among them | 13 |
| of which new | 48 |

Eight sources could not be opened, among them a ten-layer reference architecture from the Cloud Security Alliance, whose download is behind a form. The second round mapped eight of the 48 new sources. Forty are unmapped.

**Method, round 1.** The author wrote eight predictions before any mapping (`prior-work/predictions.md`). Three mappers, not shown the predictions, read the primary text of their sources, listed every named component with a verbatim definition, and assigned each to one WARM v0.11 part, to a span of several parts, to design-time guidance, or to "misfit". A doubtful fit was to be called a misfit. For every WARM part they also recorded, after a search, whether the source has it.

| Source | Items | Clean fit | Strained fit | Spans | Guidance | Misfits |
|---|---|---|---|---|---|---|
| Yu et al. | 97 | 33 | 8 | 42 | 9 | 5 |
| Zhu | 78 | 13 | 15 | 37 | 9 | 4 |
| Goujon, AAM/5C | 153 | 20 | 45 | 36 | 34 | 18 |
| Microsoft | 153 | 48 | 17 | 36 | 47 | 5 |
| AWS, reference-architecture guide | 87 | 24 | 18 | 30 | 15 | 0 |
| AWS, all six guides | 385 | 73 | 46 | 72 | 149 | 45 (40 are single-agent reasoning, out of WARM's scope) |
| Google Cloud | 144 | 56 | 25 | 32 | 26 | 5 |

A clean or strained fit is an item that maps to one WARM part. The counts do not compare across sources: the granularity differs, and groupings and interactions span by their nature. They do not compare directly with the platform mapping either.

**Method, round 2.** Two mappers, one for each group of four sources (the charter-like models Charterion, AEON, CEAD and Salesforce; the platform-like models AOS, Steinder and Franke, ASOC and EAAF), listed every named item and assigned it, as in the first round, to one WARM part, a span, design-time guidance or a misfit, or to a change the first round had already planned (V1 to V15). Each also recorded whether a source has an area of work apart from agents, a record of who is accountable for what, and agents that persist. The author wrote five predictions (S1 to S5) before the mapping, having read only the search's one-line summaries of the sources (`prior-work/mapping-round2-charters.md`, `prior-work/mapping-round2-platforms.md`).

| Source | Items | Clean fit | Strained fit | Spans | Guidance | Already planned | Misfits |
|---|---|---|---|---|---|---|---|
| Charterion v2.0 (read in part) | 112 | 9 | 33 | 24 | 6 | 12 | 28 |
| AEON | 58 | 13 | 16 | 15 | 5 | 6 | 3 |
| CEAD | 47 | 6 | 11 | 7 | 20 | 2 | 1 |
| Salesforce | 114 | 25 | 30 | 15 | 19 | 3 | 22 |
| AOS-0001 and AOS-0000 | 69 | 10 | 5 | 22 | 24 | 3 | 5 |
| Steinder and Franke | 37 | 14 | 0 | 15 | 6 | 0 | 2 |
| ASOC manifesto | 60 | 13 | 12 | 12 | 9 | 4 | 10 |
| EAAF | 43 | 10 | 4 | 13 | 11 | 0 | 5 |

**Predictions, round 1.** Of eight predictions, four were confirmed, two were partly right and two were wrong.

| # | Prediction | Result |
|---|---|---|
| R1 | 80% of each source's components map to one WARM part | Wrong on all six: 36% to 56% (clean plus strained), counting AWS by its reference-architecture guide; 31% across all six AWS guides. Reference models are made of groupings and interactions, which span |
| R2 | No source has a directory of which area of work is accountable for what | Confirmed on all six |
| R3 | No source gives an area of work a charter with its own workflow and acceptance criteria | Confirmed, with one near case: AWS writes the same parts as a charter for each agent ("intent and scope") |
| R4 | Misfits concentrate in events, the client layer and business design | Partly: events and calling applications, yes. The larger group of misfits was in governance mechanics, which the author did not predict |
| R5 | Two sources have a part WARM lacks; guesses: context management, guardrails, cost, oversight roles | Partly: content guardrails, yes. The real gaps were a grant step, a stop path and intake routing |
| R6 | A source splits a WARM service in a way that looks right | Confirmed: AAM/5C splits Policy into deciding, issuing a grant and enforcing |
| R7 | No source contradicts the two cross-cutting groups; one makes observability or security a layer | Confirmed: Yu et al. make evaluation, observability and improvement one responsibility (L9), and AAM/5C has a Security and Compliance layer (L5) |
| R8 | The review changes the model in 2 to 5 places | Wrong: 15 |

As with the platform mapping, the errors ran one way: the published models have more that WARM lacked than the author expected.

**Predictions, round 2.** Of five predictions, one was confirmed, three were partly or half right and one was wrong.

| # | Prediction | Result |
|---|---|---|
| S1 | Charterion's charter and AEON's subdomain each bound one agent or one capability, not an area of work | Half right: Charterion's charter binds one agent. AEON's nine subdomains exist apart from agents; they are IT functions with contracts, without roles, a workflow or acceptance criteria |
| S2 | None of the eight has a directory of which area of work is accountable for what | Confirmed, narrowly: AEON's capability registry records the subdomain that provides each capability, and agents discover each other through it. It records a provider, not who is accountable |
| S3 | AOS's persistent identity versus transient instance matches WARM's agent versus definition, not persistent versus task agents | Partly: it is a third distinction, identity versus running instance, and WARM had no word for the instance |
| S4 | CEAD is the closest precedent for "a domain defines roles, agents fill them" | Partly: CEAD says to "define the business capability and owner before defining the agent role or prompt", and records them inside one agent's contract |
| S5 | At most three further changes; cost becomes a named concern | Wrong: eleven further changes, one of them a new service; cost was already a concern and stays one |

As in the first round, the prediction that failed outright underestimated how much the published models had that WARM lacked.

**What fit.** Yu et al.'s ten responsibilities line up with WARM's parts closely enough to print side by side. Two decompositions made independently arrive at nearly the same cut, which is evidence for the cut.

| Yu et al. responsibility | WARM parts |
|---|---|
| L0 Business and solution design | People, and a domain's goals, rules and acceptance criteria |
| L1 Client and experience | Channels |
| L2 Access, identity and safety control | Identity, Secrets and Policy (Governance without Approvals), with access audit from Observability |
| L3 Agent and workflow orchestration | Harness, Sessions, Tasks, Orchestration |
| L4 Model access and inference | Models |
| L5 Enterprise context and knowledge | Memory, Retrieval |
| L6 Tool and action runtime | Tools, Registry, Environments, with Governance at the point of action |
| L7 Async and event infrastructure | Scheduling, Tasks, Messaging |
| L8 Platform and delivery infrastructure | Infrastructure, Releases, Reliability |
| L9 Evaluation, observability and improvement | Observability, Evaluation, Improvement |

Yu et al. have no Domains layer, no Directory, no agent kinds and no Artifacts store. In the vendor architectures, gateways bundle mediation, discovery, policy and audit, as WARM's condition on enforcement points predicts, and memory products separate short-term from long-term memory, as WARM separates Sessions from Memory. Each vendor has platform services carried out by agents (an arbiter, critic agents), which supports WARM's provisional statement on platform roles held by agents. In the second round no source showed the six groups cut in the wrong place. Three of the platform-like models split deciding from executing, which is a different axis, and ASOC's two cross-cutting planes, "Governance and Observability" and "Security and Trust", match WARM's two cross-cutting groups.

**What the two rounds do to WARM's claims.** This table replaces the first round's list of what no source has.

| Claim | Verdict | Deciding evidence |
|---|---|---|
| No published model treats an agent as an identified actor distinct from its definition | Refuted. Withdrawn | Charterion (Def. 2.1): an agent is "a non-human principal" with an identity that "may be instantiated many times"; Charterion credits the idea to security and standards bodies since 2025, the Cloud Security Alliance, NIST and OWASP among them. AOS separates "a persistent agent identity" from "a transient runtime instance". What differs: in Charterion every running instance of an agent, a subagent included, acts under the one identity of the chartered agent ("holds no charter of its own", Def. 8.9); WARM gives each task agent an identity of its own. Steinder and Franke take the opposite view: an agent's identity "must be a function of" its Cloud-OS identity and properties such as its goal, skills and model |
| No published model has a directory of which domain is accountable for what | Stands, narrowed. AEON is cited | AEON's capability registry records, for each capability, "the subdomain that provides it" and "the principals authorized to invoke it". Charterion's Charter Register and Staffing Table let one compute which agent covers a step and which person answers for the agent. Neither records one accountable area of work per responsibility as a lookup for handing work over. EAAF has "agents negotiate responsibilities", the opposite of a directory that people set |
| No published model has a domain as a charter separate from its agents | Stands as worded only. "No model separates an area of work from its agents" would be false | AEON's subdomains and Charterion's business scopes are areas of work apart from agents. Neither has roles that several agents and people fill, a workflow and acceptance criteria. AWS writes a charter for each agent. CEAD defines the capability and its owner before the agent. Microsoft's Cloud Adoption Framework (December 2025) has teams "define the agent charter" for an agent system: "system responsibilities that map to specific business objectives, agent roles that prevent functional overlap, and prohibited actions". That is a charter for a system of agents with responsibilities, roles and rules, so the word and much of the idea are not WARM's. It has no workflow, knowledge, tools or acceptance criteria in the charter, no roles filled by people, and no record across charters of who is accountable for what |
| No published model distinguishes persistent agents from task agents | Stands, narrowed | Charterion has one kind of agent, long-lived and with memory between actions, whose instances share its identity. Salesforce has only agents "instantiated for specific tasks", which are "decommissioned afterwards". EAAF's "Task Agents" are a type of job, not a lifetime. Zhu rejects long-lived agents |
| WARM's six groups are cut in a reasonable place | Stands | Three sources split deciding from executing, which is a different axis. ASOC's two cross-cutting planes match WARM's two cross-cutting groups. Yu et al.'s ten responsibilities line up with WARM's parts |
| The service list is complete enough | One responsibility was missing | Nothing in WARM owned which agents exist. Lifecycle is added (A1) |

Two smaller items on the first round's list, the platform test stated as a test and Evaluation reporting "unknown", were not among the claims the second round tested. None of this is evidence that WARM's distinct parts are needed.

**What did not fit, and what changed.** In the first round WARM was thinnest in Governance. Three or more sources agree on each of these findings, and v0.11 stated none of them.

| Finding | Sources | Change in v0.12 |
|---|---|---|
| A grant step: authority scoped to one task or action, time-limited, issued only on a positive decision, checked again when the action runs, revocable | Yu et al., Zhu, AAM/5C | Grants stated in Policy and in "How the groups relate" (V1) |
| Separation of duties: whoever proposes or performs an action does not approve it; an agent cannot grant itself authority; whoever writes a rule does not approve it | Yu et al., Zhu, AAM/5C | A new point in "How the groups relate" (V2) |
| A way to stop or suspend an agent at run time that does not depend on the agent or on the path it would stop | Zhu, AAM/5C, Microsoft, AWS, Google Cloud | Identity suspends or revokes an actor; a new point on stopping (V3). The second round moved suspension of a running agent to Lifecycle (A1) |
| A check that makes "every call passes an enforcement point" testable | AAM/5C (the vendors' gateways embody it) | The check added to the condition on Governance (V4) |
| Policy covers what may be said (content rules), not only what may be done | Microsoft, AWS, Google Cloud | Policy widened to content (V5) |
| Registration is a gate: a tool or agent must be registered to be used, and admission is a release | Microsoft, AWS, Google Cloud | Registration as a gate; entries name an owner (V6) |

Other findings changed the model in smaller ways:

| Finding | Sources | Change in v0.12 |
|---|---|---|
| Rules are released and rolled back like other changes | AAM/5C | Releases covers rules (V7) |
| Credentials are rotated and revoked | AAM/5C | Secrets rotates or revokes a value (V8) |
| An inbound request is routed to an agent by what it is about, before any agent runs | Microsoft, AWS, Google Cloud | "Intake routing" added to Step 4 (V9) |
| An agent exposed as a tool receives work by a tool call | Microsoft, AWS, Google Cloud | A handoff may be a tool call (V10) |
| Events are distributed between components | Yu et al.; the platform mapping | Messaging delivers events to subscribers (V11) |
| Several organizations or users share one platform | AWS, Google Cloud, Yu et al.; LangGraph | Tenancy listed as a concern that is not a group (V12) |
| The person the data is about can see, correct and delete it | Microsoft, Google Cloud | Added to Policy and to the People paragraph (V13) |
| An action's outside effects may have to be undone | AAM/5C, Zhu | Undoing named as an open question for contracts (V14) |
| Applications that call agents, and systems agents act on, have no stated place | Yu et al., AAM/5C | One sentence in Step 1 (V15) |

The second round changed the model in eleven places, one of them a new service. The claims it withdrew or narrowed are in the table above (A2).

| Finding | Sources | Change in v0.12 |
|---|---|---|
| No service owns which agents exist; an orphaned agent has no home | AOS, Steinder and Franke, EAAF; OpenClaw (a misfit in the platform mapping); AAGMM (sprawl); run-time suspension in Microsoft, AWS and Google Cloud | Lifecycle added to Runtime, the 25th service; suspension of a running agent moves from Identity to Lifecycle (A1) |
| An agent's identity is distinct from a running instance of it | AOS, Charterion | The instance named in Step 0, with credit for agents as identified principals (A3) |
| Every agent identity traces to an accountable person | Charterion, CEAD | Step 0 and the Identity row (A4) |
| Steps reserved for people, actions held for approval and the granting of authority are three different decisions | Charterion, AEON, CEAD | "Three kinds of human decision" added to Step 2 (A5) |
| Delegated authority only narrows; agents started by one agent are not independent | AOS, ASOC, Charterion | Added to the points on grants and on separation of duties (A6) |
| Risk, confidence or trust assessed at run time is an input to the decision | AOS, ASOC, EAAF, Steinder and Franke | Evaluation assesses before, during or after an action; Policy may use the assessment (A7) |
| Budgets are carried and narrowed with authority | AOS, Steinder and Franke | Cost: a budget rides in a grant, Scheduling enforces it, Observability meters it (A8) |
| A tool declares its side effects, whether they can be undone and whether a retry is safe | AOS, Steinder and Franke | Added to the Registry's text (A9) |
| A task keeps the request as it was received | AOS, ASOC | Tasks keeps the objective, the constraints and what counts as done (A10) |
| A policy decision has more outcomes than allow and deny | AEON, Charterion | Allow, deny, hold for a person, narrow, or unknown (A11) |
| A task agent's identity is not stated | Charterion, Salesforce | A task agent acts under an identity of its own, and the record says on whose behalf (A12) |
| Who decides when the named approver is unavailable; whether the running configuration is the reviewed one; precedence between rule sources | Charterion, AOS | Added to the open questions for contracts in Step 3 |

Recorded and not adopted in the first round:

| Item | Sources | Why not |
|---|---|---|
| Caching (semantic cache, prompt cache) | Yu et al., Microsoft, Google Cloud, LangGraph | An optimization inside Models or Retrieval; no responsibility of its own |
| Metering, pricing, marketplace | AWS, OpenClaw | Commercial concerns of a platform vendor |
| Model training and fine-tuning | AWS | Outside a system that calls models |
| Approvals by a designated role or by several approvers | Zhu, AAM/5C | WARM's Approvals is a person's decision by design. In the reference implementation an agent merges changes that another agent has reviewed. The owner decided on 2026-11-11 that this is Policy and not a second kind of approval: the agent acts under a rule that people wrote, the review is Evaluation, and people granted the authority |
| Role Group: a fixed authority profile across domains | Zhu | One source |
| A single kernel that commits every state change; peer consensus before an act; context integrity proofs | Zhu, AAM/5C | Implementation designs, one source each |
| The Harness "requests" tool calls and Tools "executes" them | Yu et al. | A wording refinement; it would change two figures |
| Applicability conditions for each service (when a system needs it) | Yu et al. | Worth doing in the papers on each group |
| Single-agent reasoning (planning, reflection, beliefs and intentions) | AWS, AAM/5C, Yu et al., Microsoft, Google Cloud | Out of scope by Step 0 |

Recorded and not adopted in the second round:

| Item | Sources | Why not |
|---|---|---|
| Artifacts has no full counterpart in any of the seven systems that could have one; Steinder and Franke argue that a file system is enough | All four platform-like models; the three platforms | The owner decided on 2026-11-11 to keep Artifacts and state the gap. The statement of the gap is strengthened, and the question stays open |
| Trust and reputation as a standing score of an actor; consent records; appeal of a decision; billing; responsibility across suppliers | AOS, ASOC | Systems of several organizations; WARM describes one system |
| AEON's consume, promise and guarantee form for a contract | AEON | A good template for the papers on each group |
| Autonomy levels as a vocabulary; exclusions ("must not do") on roles; accepted exceptions with an expiry; where shared context for a long workflow lives | CEAD, Charterion, Salesforce | One or two sources each; low confidence |
| Scheduling decides where work runs as well as when; "authorized" and "done" as separate records; an identity that attests the current definition, model and harness | AOS, EAAF, Steinder and Franke | Low confidence |
| Planning, reflection and uncertainty estimation inside one agent | AOS, ASOC, EAAF, Steinder and Franke | Out of scope by Step 0 |

The comparison also corrected two statements in v0.11's prior work: Yu et al. define ten "responsibilities", not layers, and Zhu's resident entry is a dormant template activated to lead one task's team, not a persistent agent.

**Second rater.** A second rater sampled 126 assignments, nine from each of the fourteen sources, and assigned each independently against v0.12. It agreed on 107, disagreed on 8 and found 3 unclear; 8 more differed only because v0.12 had added a part. That is 107 of 118, or 91%. Unlike the platform mapping, not every clean fit held (39 of 42). It also checked four pieces of evidence in the primaries. Charterion's and AEON's passages say what the claims table reports. AOS's split between a persistent identity and a transient instance is WARM's agent and instance, not its two kinds of agent. And the three lifecycle parts that led to the Lifecycle service are different cuts: all three create and end agents, only AOS suspends and resumes them, and the duty to keep a list of which agents exist rests mainly on AOS. Charterion was then read in full, which changed no verdict (`prior-work/charterion-full.md`).

**Threats to validity, round 1.** Each source had one mapper, and the mappers knew WARM and worked for the author. Two vendor inventories (three of the AWS guides, and the Google pages) were extracted by delegated readers; 22 of their quotes were checked against the page text, and all matched. Some AWS and Google pages were not read, and one AWS guide could not be opened (listed in "What WARM adds, and its limits"). Figures that are images were read by caption only. Goujon was read in an AI-assisted English translation; the French original was not consulted. Yu et al.'s 44 capabilities were taken from the authors' replication package, because the paper does not list them. The counts depend on the granularity each mapper chose. Vendor documentation is evidence of what a vendor describes, not of what its products do. The 48 sources the search newly found were not part of the first round. The changes were the author’s recommendations; the owner accepted them as a whole on 2026-11-11.

**Threats to validity, round 2.** One mapper for each group of four sources; the mappers and the second rater knew WARM and worked for the author. The second rater's sample is 126 of about 1,550 assignments. Salesforce's page was read as text, with two of its seven figures. ASOC's layer contents exist only as figure labels, so its assignments are the least certain. EAAF reports results without a method. Forty of the 48 sources the search newly found have not been mapped, and eight could not be opened. None of the fourteen models has a named adopter that the readers could find; the most-cited, EAAF, has 19 citations. The changes were the author’s recommendations; the owner accepted them as a whole on 2026-11-11.

## Glossary

| Term | Meaning |
|---|---|
| **Agent** | An identified actor that carries out one or more assigned roles. It runs on the platform: the Harness service runs its loop with a model. Its identity, memory and history persist through changes to its definition, harness or model. |
| **Agent definition** | The description of a role: its instructions and the skills it refers to. A domain writes one for each role an agent fills; the Registry holds it. Several agents may use one definition, and it may be revised. (Provisional: the operator of a platform service writes one for an agent that provides the service.) |
| **Artifact** | Something an agent produces and stores: a report, a file, a page. |
| **Directory** | The platform service that records each scoped responsibility, the domain accountable for it, and how to reach a role of that domain. People set its content. |
| **Domain** | An area of work, such as building software or managing money, defined by its goals, roles, workflow, knowledge, tools, rules and acceptance criteria. A domain does not act; the agents and people in its roles do. It holds a cohesive set of responsibilities. |
| **Grant** | Authority to carry out one action or task, issued on a positive Policy decision, limited in time and revocable. |
| **Harness** | The service that runs each agent's loop: it manages the context window, calls the model and carries out tool calls. A harness product usually bundles this service with others. |
| **Implementation** | A real system that fills in one part of WARM: Agent Scrum implements the Software Factory; a harness and its tooling implement the platform. |
| **Infrastructure** | Where everything runs: machines, CI runners, storage, network. |
| **Instance** | A running copy of an agent. It can be restarted or moved; the agent is the identity, not the instance. |
| **Job** | Work that a schedule or an event starts. A script or an agent may carry it out. |
| **Persistent agent** | An agent that holds its roles across many sessions and tasks. The platform keeps its identity, session history and memory between tasks. |
| **Person** | Someone who directs or approves work. People also fill roles, request or receive results, and are subjects of the work. |
| **Provider** | An outside source the platform calls and does not operate: a model vendor or an external service. |
| **Responsibility** | What a part is accountable for. Each platform service has one. Each domain holds a cohesive set of them; at the grain at which work is handed between domains, exactly one domain is accountable for each. |
| **Role** | A position with stated duties, filled by an agent or a person. A role that does a domain's work belongs to that domain. |
| **Service** | Something the platform provides to agents in any domain, which works the same whatever the work is about. Only the platform has services; a domain does work. |
| **Session** | The history and state of one stretch of an agent's work. |
| **Skill** | A packaged set of instructions for a kind of task. A person may write it, and experience may revise it. The Registry holds its versions and Releases makes each change. |
| **Subagent** | A task agent started by another agent to do part of its task. |
| **Task** | One unit of work with a start, an end and a result. Also called a run. |
| **Task agent** | Also called a worker agent. An agent started for one task and ended with it, with no continuing role or memory of its own. The platform retains its records. |
| **Work product** | What a task produces: software, a report, a decision, a message. |

Relations: a person **directs** a domain. A domain **defines** roles, and **writes** an agent definition for each role an agent fills. An agent **fills** one or more roles. A domain **is accountable for** a cohesive set of responsibilities, and the Directory **records** them. An agent **hands** work to a role of the domain accountable for it. A persistent agent **starts** task agents. An agent **works on** tasks, in sessions. A task **produces** work products. Agents **run on** the platform and **use** its services. Within the platform, Runtime **uses** Capabilities and Knowledge, Interaction **connects** Runtime to other agents, people and applications, Governance **constrains** every group, and Operations **observes and changes** every group. The platform **runs on** infrastructure and **calls** providers. A real system **implements** a part of the model.

## What WARM adds, and its limits

Most agent platforms grow, and few are designed up front. A team starts with a harness (a model, a loop and some tools) and adds to it one problem at a time: memory, scheduled jobs, approvals, subagents, a second agent. Each addition solves a real problem, and the result is hard to describe, compare or change. The reference implementation grew this way, in part from the goals of the open-source project OpenClaw, which its author tried first. This is the history of one system and of the projects its author followed; a team can also start from a managed platform or a workflow engine.

What WARM contributes is the whole in one picture. The published models have good parts: lists of platform services, a charter for one agent, registries of capabilities, careful accounts of authority. WARM puts the platform, the domains of work and the agents in one model, with a directory that records which domain is accountable for what, and it has been set against three platforms and fourteen published models.

WARM offers four things:

1. **An anatomy of an agent system and its platform.** Names for the parts (five layers, six groups, 25 services) and for what sits on the platform (domains and agents). It is a proposed vocabulary and not a proof that the list is complete.
2. **Organizing principles.** A responsibility belongs to the platform if it works the same whatever the work is about. An agent is an identified actor that fills roles, and a domain's roles belong to the domain. A domain holds a cohesive set of responsibilities, recorded in a directory. Governance and Operations apply across the other groups. One piece of guidance from experience: keep unattended work out of conversation sessions.
3. **A map for a harness that is growing.** A team can set what it has built against the list and ask what is missing and what is mixed. The three platforms mapped have grown most of the same parts, which is some evidence that the list describes where a growing harness tends to go. A system does not need every part, and a missing part may be deliberate.
4. **A starting place to build, assess and compare.** A checklist for building, a frame for comparing platforms service by service, and a candidate target for a refactor. A match of names does not make two services equivalent; a comparison has to record what each guarantees.

A survey of 34 sources on 2026-11-09 found no adopted, vendor-neutral reference model for an agent platform. Vendors decompose the platform into services and agree on a core (runtime, sessions, memory, tools, identity, observability, sandboxed execution). Software-factory products describe one way of working. The survey found no source that puts domains of work in the same model as the platform. WARM joins them.

The survey was a search for vocabulary and not a systematic review. A second reading on 2026-11-11 covered what it had left out: Domain-Driven Design applied to agents, Microsoft's multi-agent reference architecture, and further frameworks and papers from the AI community (`research/reports/2026-11-11-warm-prior-work-reading.md`). That reading, the documented search and the two rounds of comparison with fourteen published models qualify the claim in six ways. The verdicts and their evidence are in "Compared with published models".

1. **Vendor-neutral reference models have been proposed; none was found to be adopted.** Microsoft's Multi-Agent Reference Architecture calls its approaches "agnostic", and names Microsoft products. Yu, Rabhi, Zhu and Lu (arXiv:2610.14818, October 2026) present "a technology-neutral reference architecture" of ten responsibilities. Goujon (arXiv:2610.30221, October 2026) presents a "prescriptive reference model" in seven layers. The reading found no named adopter of any of them, and the two papers had no citations as of 2026-11-11. What is widely adopted is frameworks and guidance for building one agent application (AutoGen, the OpenAI Agents SDK, 12-factor agents), not reference models. So "no adopted model" holds as of this date. "No vendor-neutral model" would be false. A documented search on 2026-11-11 found 48 further sources that meet its rule for a general model of an agent system, and none of them has more than 51 citations. None of the fourteen models compared has a named adopter that the readers could find; the most-cited has 19 citations.
2. **Separating an area of work from the agents in it has partial precedents.** In Domain-Driven Design a bounded context is a part of a system in which terms and rules have one agreed meaning (Evans, 2003). Dubrov, applying it to agents, writes that a bounded context "is not automatically a microservice, repository, agent, or team". Atlan gives a domain a named human owner, with agents assigned to it. Zhu (arXiv:2608.08516, August 2026) keeps a persistent specialization apart from the temporary workers that fill it. Zhu's resident entry is a dormant template that is activated to lead one task's team, so it is not a persistent agent in WARM's sense, and Zhu rejects long-lived agents by design. The frameworks read (Microsoft's architecture, OpenAI's guide, 12-factor agents) assign a domain to an agent or to a group of agents. AEON's subdomains and Charterion's business scopes are areas of work apart from agents, so "no model separates an area of work from its agents" would be false. No source read gives a domain a charter with roles that several agents and people fill, its own workflow and acceptance criteria. The nearest cases are AWS, which writes a domain's parts as a charter for each agent; Google's multi-tenant architecture, which gives a business unit its own agent, tools, rules and data; CEAD, which defines a business capability and its owner before the agent, inside one agent's contract; and Microsoft's Cloud Adoption Framework, which has teams write an "agent charter" for an agent system, with its responsibilities, agent roles that do not overlap and prohibited actions. The word "charter" and much of the idea are therefore not WARM's. A full reading of Goujon found no entity for an area of work.
3. **No source read has a directory of which domain is accountable for which responsibility, and AEON comes nearest.** AEON's capability registry records, for each capability, the subdomain that provides it and the principals allowed to invoke it, and agents find one another through it. It records a provider, not who is accountable. Charterion's registers let one compute which agent covers a step and which person answers for the agent; they are not presented as a lookup for handing work over. Other near cases are optional owner tags in a registry of agents (Microsoft) and a matrix that assigns governance activities to governance roles (Goujon). EAAF has agents negotiate their responsibilities, the opposite of a directory that people set.
4. **An agent as an identified actor is not new, and WARM withdraws that claim.** Charterion defines an agent as "a non-human principal" with an identity that "may be instantiated many times", and credits the idea to security and standards guidance published since 2025, from the Cloud Security Alliance, NIST and OWASP among others. AOS separates "a persistent agent identity" from "a transient runtime instance". What remains different is narrow. In Charterion every running instance of an agent, a subagent included, acts under the one identity of the chartered agent; WARM gives each task agent an identity of its own.
5. **The split between persistent and task agents has partial precedents.** Charterion has one kind of agent, long-lived, whose running instances share its identity; Salesforce has only agents started for one task; EAAF's "Task Agents" are a type of job and not a lifetime, and Zhu rejects long-lived agents. The claim that none separates the two kinds by lifetime as WARM does stands, narrowed.
6. **Artifacts has no full counterpart in any system mapped.** None of the three platforms and none of the published models whose scope could include one has a full counterpart to a versioned store of work products, and Steinder and Franke argue that a file system is enough: "POSIX file systems still store agent-produced artifacts". The owner decided on 2026-11-11 to keep Artifacts and to state the gap.

Not read: AWS's guides on security and on a semantic layer, most of its serverless and multi-tenant guides, and its Well-Architected Agentic AI Lens; one AWS guide (an enterprise multi-account architecture) that could not be opened; most of one Google page (private networking patterns) and two Google pages outside agent architecture; one Microsoft page that is empty. Forty of the 48 sources the documented search newly found have not been mapped, and eight more could not be opened, among them the Cloud Security Alliance's reference architecture. Of the eight mapped, Charterion was read in part (about 110 of its 290 pages), Salesforce's page was read as text with two of its seven figures, and ASOC's layer contents exist only as figure labels. Failing to find a model does not show that none exists.

Limits, stated as plainly as the author can:

1. **Source.** WARM is built from published work (an industry survey, a documented search and a comparison with fourteen published models), one implementation, and a mapping to three platforms. The survey supplies vocabulary and no proof of completeness, and some of its quotes were not re-checked against the primary page. The implementation is a small company's system, on one harness product, with one owner who is also its operator.
2. **Domains.** That implementation has seven areas of work configured (software, finance, health, communications, research, marketing and customer support). The author mapped their declared roles, tools and rules. The author did not check in the code which service carries each part, and did not measure whether any service is reused unchanged across domains. The maps contain unresolved placements. The seven are the domains the owner needed, each built as far as was useful, so other kinds of domain, and deeper ones, may not fit.
3. **Platforms.** WARM has been mapped to three platforms from their documentation, by the author's team, with one mapper per platform and a second rater on a sample of 36 assignments. The comparison with fourteen published models had one reader per group of sources and a second rater on a sample of 126 assignments, and forty of the sources the search newly found are unmapped. No one outside has mapped a system to it, and no running system other than the reference implementation has been inspected.
4. **Contracts.** WARM names responsibilities and some relations. It does not specify what each service must guarantee (on failure, cancellation, delegation, stale state) or how to tell that a system conforms. Implementations define concrete interfaces. Later papers on each group are intended to propose contracts; whether any becomes part of the model is open.
5. **Evidence.** There is no evidence yet that organizing a system this way improves it. The refactoring of the reference implementation is the first test, and its measures have to be set before it starts.

Two further cautions: the platform test is a design choice that cannot be refuted, and the two kinds of group describe scope and do not sort every service.

## Changes from v0.11

Sources: the first round of the comparison with published models, `prior-work/synthesis.md` (V numbers), and its three mappings `prior-work/mapping-yu-zhu.md`, `prior-work/mapping-aam5c.md` and `prior-work/mapping-vendors.md`; the second round, `prior-work/synthesis-round2.md` (A numbers), and its two mappings `prior-work/mapping-round2-charters.md` and `prior-work/mapping-round2-platforms.md`. Every change is the author's recommendation and awaits the owner's decision.

| Change | Source |
|---|---|
| A positive Policy decision is issued as a grant: scoped to the action or the task, limited in time, revocable, and checked when the action runs. Deciding, issuing and enforcing stay in Policy; the split is left to an implementation. Grant added to the glossary | V1. Yu et al., Zhu, AAM/5C |
| Separation of duties: the actor that proposes or performs an action does not approve it; an agent cannot grant itself authority; whoever writes a rule does not approve it | V2. Yu et al., Zhu, AAM/5C |
| Identity can suspend or revoke an actor. A system needs a way to stop an agent that does not pass through the agent or a service it provides | V3. Zhu, AAM/5C, Microsoft, AWS, Google Cloud |
| The condition on Governance can be checked against a record kept at the resource; actions under a person's or a script's identity are its blind spot | V4. AAM/5C |
| Policy covers what may be said as well as what may be done and what is kept; "content filters" added to its industry terms | V5. Microsoft, AWS, Google Cloud |
| Registration can be a gate, adding a Registry entry is a release, and each entry names its owner, separate from the Directory's accountable domain | V6. Microsoft, AWS, Google Cloud |
| Releases covers rules | V7. AAM/5C |
| Secrets rotates or revokes a value | V8. AAM/5C |
| "Intake routing" added to Step 4: a request that names no agent is routed by what it is about, using the Directory | V9. Microsoft, AWS, Google Cloud |
| A handoff can be carried as a tool call; Orchestration still tracks the assignment | V10. Microsoft, AWS, Google Cloud |
| Messaging delivers events to their subscribers as well as messages between agents | V11. Yu et al.; the platform mapping |
| Tenancy listed as a concern that is not a group | V12. AWS, Google Cloud, Yu et al.; LangGraph |
| The person the data is about can see, correct and delete it, under Policy's rules on what is kept; stated in the People paragraph | V13. Microsoft, Google Cloud |
| Undoing an action's outside effects added to what a contract has to settle; no service owns it yet | V14. AAM/5C, Zhu |
| Step 1 says where calling applications and systems acted on sit | V15. Yu et al., AAM/5C |
| "What the published models changed" added to Step 3 | V1, V2, V3, V5, V6, V11 |
| "Compared with published models" added, with a documented search; prior-work points, the "Not read" paragraph and limits 1 and 3 updated | `prior-work/synthesis.md`, `prior-work/search.md` |
| Yu et al. define ten "responsibilities", not layers (corrected in the v0.11 text during the comparison, and kept) | `prior-work/mapping-yu-zhu.md` |
| Zhu's resident entry is a dormant template activated to lead one task's team, not a persistent agent; Zhu rejects long-lived agents (corrected in the v0.11 text during the comparison, and kept) | `prior-work/mapping-yu-zhu.md` |
| The first round left Tasks, Directory, Improvement, Channels and the count of 24 services unchanged; the second round adds Lifecycle (A1) | `prior-work/synthesis.md`: "The service count stays 24"; `prior-work/synthesis-round2.md` |
| Lifecycle added to Runtime as the 25th service: create, suspend, resume and end agents, and keep the list of which agents exist. Suspending a running agent moves from Identity (V3) to Lifecycle; Identity revokes the identity. Every count of services becomes 25, and Runtime has six. A paragraph in "What the published models changed" | A1. AOS, Steinder and Franke, EAAF, OpenClaw, AAGMM; run-time suspension in Microsoft, AWS and Google Cloud |
| The claims are withdrawn or narrowed: an agent as an identified actor is withdrawn, with credit to Charterion, AOS and the security guidance they cite; the directory claim cites AEON; the charter and persistent-agent claims are narrowed; Artifacts has no full counterpart in any system mapped. "Compared with published models" covers two rounds and fourteen models, with the search flow, the round-2 counts and predictions, and a table of claims that replaces "What no source has". "What WARM adds", the "Not read" paragraph and limits 1 and 3 updated | A2. Charterion, AEON, AOS |
| Step 0 names the instance: a running copy of an agent, which can be restarted or moved and is not the agent. Instance added to the glossary | A3. AOS, Charterion |
| Every agent identity traces to a person accountable for it (Step 0 and the Identity row) | A4. Charterion, CEAD |
| "Three kinds of human decision" added to Step 2: steps reserved for people, actions held for approval, and the granting of authority | A5. Charterion, AEON, CEAD |
| A grant passed to another agent can only be narrower; agents started by the same agent are not independent for separation of duties | A6. AOS, ASOC, Charterion |
| Evaluation assesses before, during or after an action, and Policy may use an assessment as an input | A7. AOS, ASOC, EAAF, Steinder and Franke |
| Cost: a budget is carried in a grant, enforced by Scheduling's limits and metered by Observability | A8. AOS, Steinder and Franke |
| A tool's definition in the Registry declares its side effects, whether they can be undone and whether a retry is safe | A9. AOS, Steinder and Franke |
| Tasks keeps the original request: its objective, its constraints and what counts as done | A10. AOS, ASOC |
| A Policy decision may allow, deny, hold for a person, narrow the action, or be unknown | A11. AEON, Charterion |
| A task agent acts under an identity of its own, and the record says on whose behalf | A12. Charterion, Salesforce |
| Three open contract questions added in Step 3: an unavailable approver and the load on one approver; whether the running configuration is the reviewed one; precedence between rule sources | `prior-work/synthesis-round2.md` |

## Changes from v0.10

Sources: the independent review `deck/review-astra-v0.10.md` (F numbers), the platform mapping `platform-mapping/mapping.md` (M numbers), and the author's decisions of 2026-11-11.

| Change | Source |
|---|---|
| An agent is an identified actor that carries out assigned roles. The definition describes a role, may be shared and may be revised. "Change the definition: a different agent" is withdrawn | F01 (blocker). The author picked this wording |
| Domain membership is stated per role. One role is active and one domain accountable for each task. Who started a task agent is separate from which domain is accountable | F02 |
| The platform test is "works the same whatever the work is about". It classifies the responsibility, not the implementation. The "knowledge or judgment" test is withdrawn | F03 (blocker), M1. The author picked this wording |
| One domain is accountable for each responsibility, at the grain at which work is handed between domains. Finer items are knowledge or tools inside a domain. Other domains may contribute. Responsibilities may be scoped by product, project or account | F04, F26. The author: it is a question of granularity; Finance makes sense as a domain and a checking account probably does not. |
| Directory is a service of its own, in Interaction. An entry names a scoped responsibility, the accountable domain and how to reach a role (an agent, or how to start one). Finding a destination grants no authority | F05, M10. The author chose: its own service |
| CI stays in the Software Factory because it does not work the same whatever the work is about; the general parts beneath it are platform services. "No other domain uses CI" is withdrawn as the reason | F06. The author: it belongs to the Software domain. |
| The table of carriers lists common carriers, not all of them | F07 |
| Domains ask each other in ordinary language and use judgment; accountability, authority, expected results and escalation are agreed in advance. "Nothing about the exchange is specified in advance" is withdrawn | F08 (blocker). The author picked this wording |
| A platform service has a boundary and stated guarantees; its results vary. "The same way every time" and "sameness versus judgment" are withdrawn | F09 |
| The two kinds of agent are defined by what persists. Keeping unattended work out of conversations is guidance | F10. The author chose: define by lifetime |
| "How work starts" lists triggers (a person or application, another agent, a time or event). A backlog is pending work, not a trigger. A job need not be an agent | F11 |
| The test for a separate team is replaced by considerations (volume, concurrency, coordination cost, independent stages) | F12 |
| Limit 2 states what the domain maps did and did not verify, and the single owner | F13 |
| Limit 4 is about contracts and conformance, not only interfaces | F14 |
| The four offers are kept and calibrated | F15 |
| The why paragraph keeps both claims and adds what a second reading of prior work found: proposed vendor-neutral models with no adopter found, partial precedents for a domain separate from its agents, and no directory of responsibilities | F16. The author chose: keep, add a caveat |
| One request runs through the document, with a directory lookup, a handoff and an approval before the action | F17, F24. The author chose: worked example first for the talk |
| Messaging carries; Orchestration tracks the assignment and the result; delivery is not acceptance | F19 |
| The Finance example follows the declared configuration; enforcement is stated as unverified | F20 |
| Retrieval fetches material whoever wrote it; Sessions keeps a record after work ends; a skill may be written or revised | F21 |
| Terms: a domain is a charter (the layer row no longer includes its agents); "provider" is kept for the outside layer; a job is work, not an agent | F22 |
| People have more relations to the work than directing it; stated as not yet developed | F26 |
| Layers are logical categories relative to a system boundary; a self-hosted model is placed | F27 |
| The Hydra citation is verified and given in full | F28 |
| Improvement added to Operations | M2. The author chose: add the service |
| Skills are versioned definitions in the Registry, changed through Releases. Memory holds facts and events | M3. The author chose: Registry + Releases. This reverses the v0.6 decision that skills are procedural memory |
| Human channels renamed Channels, for people and applications | M4. The author chose: widen to Channels |
| Tasks is a contract every runtime meets and need not be a store; the cut between Sessions, Tasks and Memory is stated | M5. The author chose: contract, not a store |
| Governance covers an action only if it passes an enforcement point | M6 |
| Rules on stored data added to Policy | M7 |
| Admission and capacity added to Scheduling | M8 |
| Artifacts kept; the absence of a counterpart on the platforms is stated | M9. The author chose: keep, note the gap |
| "When the Domain layer matters" added | M11 |
| The model's sources are stated as three: survey, experience, mapping. "Tested against three platforms" added | The author: the process was an industry survey, our own experience, and then a detailed mapping to existing agent frameworks, and the mapping influenced the model |
| 22 services become 24 | Directory and Improvement |

Deck-only findings (F18 timing, F23 appendix notes, F25 concept-to-code slide) are applied in the deck. Earlier changes are in `warm-model-v0.10.md`.
