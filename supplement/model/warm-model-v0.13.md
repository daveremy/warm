---
title: "WARM: the Working Agents Reference Model, v0.13"
date: 2026-11-11
author: sagan
issue: lifeos#3502
status: draft for the owner to read. v0.13 splits the model into a core and an appendix, adds pre-approval and three kinds of human decision, redefines a domain, adds the domain's published skill and the domain pattern, and narrows the claims that Domain-Driven Design, Team Topologies and Data Mesh qualify. Input - v0.13-spec.md (the owner's decisions of 2026-11-11). Not yet reviewed by a second reader.
---

# WARM: the Working Agents Reference Model (v0.13)

WARM names the parts of a system in which agents do sustained work, and how the parts relate. It is written for systems in which agents finish work end to end: people direct the work and set the rules in advance, and agents act within them. It is also written for systems that improve themselves continuously.

The model in four sentences: people direct the work. Domains define it. Agents carry it out. The platform provides the services they share.

WARM comes from three sources: published work (an industry survey, a documented search, and a part-by-part comparison with fourteen published models); the experience of building and running one system; and a mapping of the model to three existing agent platforms. Each source changed the model.

The model was made with the system it describes. The work ran in the first version of the reference implementation: the agents of its Research domain did the reading, the mappings and the second ratings, the agents of its Software domain built the map of the code's modules, checked the plan for changing the system and filed its issues, and a person directed the work and decided each change of substance.

This document has two parts. The **Core** is the model, and it reads alone. The **Appendix** has three sections: A, notes that qualify the core; B, the questions that each service's contract has to settle; and C, the evidence (examples, the three platforms, the fourteen models, how the model was derived, the glossary, the limits and the change log).

# Core

## A request to follow

One request is used throughout. A person asks their finance agent: "There is a duplicate charge from the gym this month. Dispute it."

The finance agent can find the charge. It may not write to the merchant: messages sent in the person's name are the responsibility of another area of work, Communications, and need the person's approval. So the request crosses two areas of work, uses sixteen platform services, and stops once for a person. The appendix traces it step by step.

## Step 0. Scope

**Idea: WARM describes the system around agents: who directs them, what work they do, and what they run on.**

An **agent** is an identified actor that carries out one or more assigned roles. In the request, the finance agent is one agent and the communications agent is another. The agent is the identity, not a running copy of it: an **instance** of an agent can be restarted or moved, and it is not the agent. Every agent identity traces to a person who is accountable for it.

An **agent definition** describes a role: its instructions and the skills it refers to. A skill is a packaged set of instructions for a kind of task. A definition is not the agent. Several agents can use one definition, and a definition can be revised while the agent stays the same agent. An agent's identity, memory and history persist through a change of definition, harness or model. Each such change can alter how the agent behaves, so each is versioned and evaluated.

An agent **runs on** the platform. The **Harness**, a platform service, runs each agent's loop: it sends context to a model and carries out the tool calls the model asks for.

An agent may hold more than one role. For each task that is a domain's work, one role is active and one domain is accountable for the result.

Agents are of two kinds, by lifetime.

| Kind | What it is | What persists | Example |
|---|---|---|---|
| **Persistent agent** | Holds its roles across many sessions and tasks. | Its identity, its session history, what it has learned, and a channel on which people and other agents reach it. | A finance agent that a person consults, and that remembers the accounts and last month's decisions. |
| **Task agent** | Holds a role for one task: it is started for the task and ended when the task ends. Another agent starts it, or a schedule or an event does. | No continuing role and no memory of its own. It returns a result and work products. The platform retains its records. | A developer agent started for one issue, which delivers a pull request and ends. |

The difference between the kinds is lifetime and nothing else. A persistent agent can work unattended, and a task agent can ask a person a question. One definition can serve both kinds: a persistent agent that a person talks to, and a task agent that another agent starts from the same definition for one question. They are two agents with one role. The role a task agent fills determines the domain accountable for its work; who started it is a separate fact. A task agent acts under an identity of its own, and the record says on whose behalf it acts.

**The aim is that agents finish work end to end.** An agent carries a piece of work from request to result without a person approving each action. People keep control in three ways: they direct the work, they set the rules in advance, and they decide the cases that the rules reserve for them. Step 2 names the three kinds of decision this leaves to people.

**The system improves itself continuously.** This is the second aim. The people and agents of each domain change its way of working from evidence, and the agents of the Software domain can change the platform itself. Observability collects the evidence, Evaluation judges it, Improvement proposes a change and Releases makes it. Each change is governed like any other action.

WARM does not describe how a single agent reasons (planning, reflection); research papers already model that. No part of the model is tied to a vendor or a product. A real system that fills in one of its parts is an **implementation** of that part (Step 5).

## Step 1. The layers

**Idea: people direct domains; the work of a domain runs on a platform; the platform runs on infrastructure and calls providers.**

| Layer | What it is | Examples |
|---|---|---|
| **People** | Those who direct and approve the work. | A developer; a team lead; the person who owns the accounts |
| **Domains** | Areas of work. A charter defines each one; agents and people fill its roles and do the work. | Software, Finance, Communications |
| **Platform** | Services that agents in any domain can use. | Sessions, memory, scheduling |
| **Infrastructure** | Where everything runs. | Machines, CI runners, storage, network |
| **Providers** | What the platform calls and does not operate. | Model vendors, external services |

The layers are logical categories, relative to the boundary of one system. They are not a deployment diagram. Agents are not a layer: agents and people fill the roles of domains, and agents run on the platform.

### What belongs in the platform

One test places a responsibility. **A responsibility belongs to the platform if it works the same whatever the work is about. It is domain work if what it does depends on the subject of the work.**

In the request, holding an action until a person approves it works the same for an email, a payment or a merge, so Approvals is a platform service. The rule "every message in this person's name needs approval" is about one area of work, so it is part of the Communications charter, and the platform applies it.

The test classifies the responsibility, not how it is built. A platform service may use a model or an agent inside it, and domain work may be a fixed script.

## Step 2. The platform is six groups of services

**Idea: the platform answers six questions about agents.**

Four groups are **working groups**: an agent mostly uses their services to do its work. Two are **cross-cutting groups**: their services mostly apply to what happens in every other group.

| Group | The question it answers | Kind | Relation to the other groups |
|---|---|---|---|
| **Runtime** | How, where and when do agents run? | working | The center. Work happens in a session or a task, and the other working groups are used from there. |
| **Knowledge** | What do agents know and keep? | working | **Used by** Runtime. |
| **Capabilities** | What can agents use? | working | **Used by** Runtime. |
| **Interaction** | Who do agents work with? | working | **Connects** Runtime to other agents, to people and to applications, in both directions. |
| **Governance** | What are agents allowed to do? | cross-cutting | **Constrains** the other five. |
| **Operations** | How do we see it, judge it, improve it and keep it running? | cross-cutting | **Observes and changes** the other five. |

Governance follows three rules.

1. **Governance covers an action only if the action passes an enforcement point.** An enforcement point is a place where a call is checked against the rules and can be blocked. A call that reaches a tool, a model or a store without passing one is not governed, whatever the rules say.
2. **A positive decision is issued as a grant:** authority for one action or one task.
3. **Whoever proposes or performs an action does not approve it.** An agent cannot grant itself authority.

### Human decisions and pre-approval

For each class of action, people choose one of three kinds of decision.

1. **Reserved for people.** An agent may prepare the step and may not carry it out.
2. **Pre-approved under conditions.** A person authorizes a class of actions in advance and states the conditions: for example, two independent reviewers agree, the checks pass, and the action can be undone and is reported afterward. At run time Policy checks the conditions and issues the grant. No person is asked.
3. **Held for a person.** When the rules allow an action but no pre-approval applies, or a pre-approval's conditions are not met, the action waits for a person's decision. This is the fallback.

**All authority traces to a person.** An agent has a role or a rule because a person decided it. Changing a role or a rule is itself an action, so it too is reserved, pre-approved or held. A system that improves itself continuously changes its own roles and rules, and it can do that only if some of those changes are pre-approved.

**Principle: design for agents to finish work end to end. Prefer a pre-approval to holding each action.**

Two rules apply to every pre-approval.

- **It states its term.** A pre-approval names an end date or a condition that ends it, or it says explicitly that it does not expire. A person can revoke it at any time.
- **An action that cannot be undone must be named.** A pre-approval covers such an action only if it says so explicitly and names the kind of action. Whether a system pre-approves such actions at all, and what more it requires, is a choice for the people who direct it. The notes list the options.

An agent that merges reviewed work acts under a pre-approval: Policy enforces it, and Evaluation supplies the reviewers' verdicts. In the request, no pre-approval covers a message in the person's name, so the send is held.

Pre-approval is not WARM's idea. Six of the fourteen published models compared state it in full and six in part, and two state it more completely than WARM does: Charterion and AAM/5C, which calls it a "pre-authorized capability envelope". The sources disagree on actions that cannot be undone: AAM/5C requires a person for each one, and Charterion allows autonomy where a compensating step exists. Six of the models grade autonomy or decision authority in levels or classes (AAM/5C, Charterion, CEAD, ASOC, AOS and Zhu). WARM defines no levels: its kinds of decision apply to classes of action.

## Step 3. Twenty-five services

**Idea: each group holds a few services, and each service has one responsibility.**

| Group | Service | Its one responsibility | Industry terms |
|---|---|---|---|
| Runtime | **Harness** | Run the agent loop: decide what goes into the context window, send it to the model, and carry out the tool calls the model asks for. | harness, agent loop, context management, compaction |
| Runtime | **Sessions** | Keep the history and state of a stretch of an agent's work, so that the agent can pause, resume and hand off, and so that the record remains after the work ends. | session, thread, state, checkpoint |
| Runtime | **Tasks** | Track each unit of work (a task or run) from start to finish, coordinate its retry, recovery and cancellation, and keep the original request. | runs, jobs, task lifecycle, durable execution |
| Runtime | **Environments** | Give each agent a place to act, isolated from the others: sandboxes, workspaces, browsers. | sandbox, runtime, workspace, computer use |
| Runtime | **Scheduling** | Decide when work starts: at a time, on an event, and within the limits on how much may run at once. | cron jobs, triggers, queues, concurrency limits, rate limits |
| Runtime | **Lifecycle** | Create, suspend, resume and end agents, and keep the list of which agents exist. | agent lifecycle, provisioning, decommissioning, orphaned agents, sprawl |
| Knowledge | **Memory** | Retain what agents learn across sessions (facts and events), with where each entry came from, and keep it current. | memory, memory bank, dreaming |
| Knowledge | **Retrieval** | Fetch material from named sources: documents, data, notes. | retrieval, knowledge base, grounding, RAG |
| Knowledge | **Artifacts** | Store what agents produce (reports, files, pages) and its versions. | artifacts, outputs, store |
| Capabilities | **Models** | Mediate requests to models and choose the model for each task, across more than one model or vendor. | models, model routing, multi-model |
| Capabilities | **Tools** | Mediate calls to tools, local or external. | tools, MCP, gateway, connectors |
| Capabilities | **Registry** | Hold the versioned definitions of agents, tools and skills, so that each can be found and loaded when a task needs it. | registry, catalog, discovery, skills, hub |
| Interaction | **Directory** | Record which domain is accountable for each responsibility, and how to reach a role of that domain. | (none found) |
| Interaction | **Messaging** | Deliver messages between agents, and events to their subscribers. | agent-to-agent, A2A |
| Interaction | **Orchestration** | Coordinate assignments among agents, people and fixed steps: who does what, what depends on what, and the results that come back. | orchestration, subagents, handoffs, workflows |
| Interaction | **Channels** | Carry requests and results between agents and the people and applications that use them, on the channel each one uses. | channels, surface, agent interface, invoke API, endpoints |
| Governance | **Identity** | Establish who is acting (each agent, person and service, and on whose behalf), record the person accountable for each agent identity, and revoke an identity. | identity, agent identity, authentication |
| Governance | **Secrets** | Hold values that agents must not see, and release each one only at the point of use. | secrets, secret manager, vault, credentials |
| Governance | **Policy** | Decide by rule whether an action may proceed, what content may enter and leave, and what stored data is kept; issue a grant when an action is allowed. | policy, guardrails, content filters, permissions, hooks, retention, TTL |
| Governance | **Approvals** | Obtain and record people's authorizations: approvals given in advance for a class of actions under stated conditions, and decisions on single actions that are held. | human in the loop, tool approval, standing approval |
| Operations | **Observability** | Collect evidence of what agents and the platform did. | observability, tracing, audit log |
| Operations | **Evaluation** | Assess behavior and work products against stated criteria, and report "unknown" when a check could not run. | evaluation, evals |
| Operations | **Improvement** | Turn evidence (traces, evaluations, reviews) into proposed changes to agents, skills and the platform. | recommendations, insights, optimization, self-improvement |
| Operations | **Releases** | Version and release changes to agents, skills, rules, the platform and the infrastructure the system manages, with a way back. | deployment, versioning, rollback, change management |
| Operations | **Reliability** | Keep services available and restore them after a failure. | operations, recovery |

These names are responsibilities, not products. One product may cover several responsibilities, one responsibility may be shared by several products, and a system does not need all twenty-five. Tasks, for example, names a responsibility and does not require its own store.

WARM names each service and its responsibility. It does not state each service's contract: what the service guarantees on failure, cancellation, delegation, stale state and recovery. The appendix lists the questions those contracts have to settle.

## Step 4. A domain is an area of work

**Idea: a domain says what the work is. Agents and people do the work, on the platform's services.**

**A domain is an area of work: a body of specialized knowledge, a set of responsibilities that belong together, and one or more patterns for carrying them out. Its charter writes these down.**

"Domain" here has its organizational sense, as in Team Topologies and Data Mesh. It is not the domain of Domain-Driven Design, which is the subject area that a piece of software models.

A domain does not act. The agents and people who fill its roles act. A domain resembles a department's charter more than a department's staff.

| The charter states | What it is | Platform services that commonly carry it |
|---|---|---|
| **Goals** | What the work is for, and who is accountable. | (set by people) |
| **Responsibilities** | What the domain is accountable for. | Directory |
| **Roles** | The positions in the domain and their duties, filled by agents and people. Each role that an agent fills has an agent definition. | Registry (definitions); Directory (how to reach a role) |
| **Workflow** | How work starts, and how it moves from request to result. | Tasks, Scheduling, Orchestration |
| **Domain knowledge** | What must be known to do this work, including its skills. | Memory, Retrieval, Registry (skills) |
| **Domain tools** | Connections this work needs. | Tools |
| **Domain rules** | Limits, pre-approvals, required approvals and preferences. | Policy, Approvals |
| **Acceptance criteria** | How to tell that a work product is good. | Evaluation |
| **Published skill** | What the domain offers other domains, and how to ask for it. | Registry (holds it); Directory (points to it) |

People set the goals and approve the charter. The third column lists common carriers and is not complete. A domain needs no platform service of its own: if its work needs a reusable responsibility that the platform lacks, that is a gap in the platform.

### Responsibilities and the Directory

Each domain holds a set of responsibilities that belong together, because they draw on the same knowledge, tools and rules and serve the same goals. Finance is responsible for tracking spending, watching subscriptions and reporting where the money goes. Communications is responsible for the inbox and for messages sent in a person's name.

A responsibility is stated at the size at which an agent of another domain would hand work over. "Messages sent in a person's name" is a responsibility. One checking account is not: it is knowledge and a tool inside Finance. At that size, exactly one domain is **accountable** for each responsibility. Other domains may contribute to the work or carry out part of it. People set this division.

The division is recorded in the **Directory**. An entry holds a responsibility, the domain accountable for it, and how to reach a role of that domain: an agent that exists, or how to start one. Finding a destination grants nothing: whether the request may be made, and whether the work may be done, are still questions for Identity, Policy and Approvals.

### What a domain offers other domains

An agent in one domain needs to know when to ask another domain, how to ask, and what comes back. Each domain states this in a **published skill**: the part of its charter that is written for the agents of other domains. The skill says what the domain offers, when to use it, how to ask and what comes back.

The skill belongs to the domain. The Registry holds it, and the Directory's entries point to it. An agent of another domain loads it when it needs it. Loading the skill grants nothing: Policy still decides. The precedents are the Team API of Team Topologies and the data product of Data Mesh.

### Handing work over

When an agent meets work that another domain is accountable for, it hands the work over and gets a result back. In the request, the finance agent learns from the Directory that messages in the person's name belong to Communications, and from the Communications skill how to ask. Messaging carries the request to an agent that exists; if the accountable domain has no agent running, the platform starts one. Orchestration tracks the assignment and the result. Delivery alone establishes neither that the work was accepted nor that it was done.

Agents in different domains ask each other in ordinary language and use judgment, as the departments of an organization do. Who is accountable, who may authorize what, what result is expected and when to escalate are agreed in advance. An agent reaches a platform service differently: through a defined interface, with stated guarantees.

### How work starts

| Trigger | Example | The service it arrives through |
|---|---|---|
| A person or an application asks | A conversation with the finance agent | Channels |
| Another agent asks | The finance agent hands over an email | Orchestration, Messaging |
| A time or an event arrives | A nightly sync; a new message in the inbox | Scheduling |

A trigger may start work at once or add it to a backlog. A script, one agent, or a coordinating agent with several task agents may carry the work out.

### Subdomains

A domain's responsibilities often fall into groups that are carried out in different ways. A **subdomain** is a named group of a domain's responsibilities that has its own workflow. It may also have its own roles, knowledge, tools and acceptance criteria. It keeps the domain's goals and rules, and the domain remains accountable for its work.

In the reference implementation the Software domain has two kinds of work: building and changing software, and running the product in production. They arrive differently, are carried out by different roles and are judged done differently, and both answer to the same goals and rules. Running the product is a subdomain of Software.

A subdomain is internal to its domain. The Directory records domains and not subdomains: another domain asks the accountable domain, in the way its published skill says, and how that domain divides the work is its own business. A subdomain is optional, and a small domain has none. WARM names one level and states no rule for when a group of responsibilities should become a subdomain or a domain of its own.

### Domain patterns

A **domain pattern** is a recurring way of carrying out a group of a domain's responsibilities. It answers four questions: how the work arrives, who carries it out, who judges it done, and when a person is involved. A pattern attaches to a group of responsibilities (a subdomain, where the domain names one) and not to a whole domain. A domain usually mixes several.

One example is the factory pattern. Work waits in a backlog. A coordinating agent hands items to task agents. Each item passes through fixed stages, and each result is checked against stated criteria and by reviewers before it is accepted. People set the rules in advance and are told afterward. In the reference implementation the Software domain carries out its main work this way.

A domain pattern is not an orchestration pattern, which is the industry's term for how several agents coordinate on one task. WARM names the idea and gives one example. Which patterns recur across domains is an area of study, and we expect to find more.

### How agents fit

For each role an agent fills, the charter includes an agent definition. The Registry holds it, and the Harness loads it. The definition is not the only route from the charter to the platform. The domain's rules on what is allowed reach Policy and Approvals. Its criteria reach Evaluation, and its knowledge reaches Memory and Retrieval.

WARM sets no number of agents per domain. A domain may have one persistent agent that holds its main role, several persistent agents with different roles, or none, with task agents started when work arrives. One persistent agent may hold roles in more than one domain.

**A platform service may be implemented by an agent, and it need not be.** One example from the reference implementation, measured 2026-11-12: a persistent agent routed signals between the other agents. Of 1,895 signals it received between 2026-10-07 and 2026-11-12, it forwarded 1,756 (92.7%) unchanged to the recipient the sender had named. In four of the 78 forwards whose text changed, read by hand, the change was a lost apostrophe. One reader and one script produced these counts, and 92 of the remaining rows were not read by hand. The routing is a platform service that a program without a model could implement, and the owner has asked for that (lifeos#3873). The question the example suggests for any component: what share of its outputs needed a judgment? This is one example and not a rule of the model.

**One area of work can hold a platform service and a domain.** A second example from the reference implementation, measured the same day: the communications agent made 40 successful sends (email and text) between 2026-10-07 and 2026-11-12. It drafted 21 itself. In 16 it sent text that another agent had supplied, as supplied. The person dictated one, and two were a test or not traced. On the 16 it asked the person to approve again and checked the recipient; it raised no concern about the wording of any. The test of Step 1 separates the two kinds of work. Delivering a message, and the approval that releases it, work the same whatever the message is about, so they are platform services (Channels, Approvals). Triage, drafting, follow-up and contacts depend on the subject, so they are the communications domain. What a particular message says is accountable to the domain of its subject. The owner adopted this split on 2026-11-12. One reader and one script produced the counts.

**Proposed, not adopted: a domain reviews outgoing content from other domains.** The communications domain would review another domain's outgoing message for risk, and the marketing domain another domain's proposed public post. In WARM's terms the domain supplies criteria and Evaluation applies them before Approvals asks the person. The reference implementation does not do this today, and no sent message with a content problem was found in the 16 relays. The owner's trigger for building it: the first sent message he regrets or has to correct.

## Step 5. Every part has implementations

**Idea: WARM is abstract; a real system implements one of its parts.**

"Implementation" is one relation, and it applies at every layer.

| Part of WARM (abstract) | An implementation (real) |
|---|---|
| A domain: Software | **Agent Scrum**, which carries out the domain's main work in the factory pattern |
| The platform | A harness plus what is built around it. In the reference implementation: Claude Code and the LifeOS tooling. Also: each of the three platforms mapped in the appendix |
| Infrastructure | A server, its CI runners, backups and network |
| Providers | The model vendors and external services a system uses |
| The agents of a domain | In the reference implementation: one persistent agent for each of six domains, several for Software, and task agents started by all of them |

A domain can have more than one implementation, and the mapping between services and components is many to many.

Uses of the model:

- **Describe a system:** map each part to a layer, a service or a domain. A part that fits nowhere is a question: the model may lack something, the part may mix two responsibilities, or it may be outside the model's scope.
- **Place new work:** does it work the same whatever the work is about (Step 1)? If so, which question does it answer (Step 2)?
- **Compare systems:** list, for each service, who supplies it, what it guarantees, and what is unresolved. Two services with the same name are not thereby equivalent.
- **Decide what agents may finish alone:** for each class of action, choose reserved, pre-approved or held (Step 2), and write each pre-approval with its conditions and its term.
- **Structure a body of writing or code:** one unit per part.

# Appendix A. Notes

Each note qualifies a statement in the core and is filed under the step it qualifies. Most of this text is carried from v0.12.

## Notes on Step 0 (scope)

**Records of a task agent.** The end of a task agent is not the deletion of its records. The platform retains the identity under which it acted, its transcript and its results for as long as the rules on stored data say (Policy), so that a past action can be attributed and investigated. The platform can also checkpoint and resume a task agent while its task is running.

**Other names.** A task agent is also called a worker agent. A task agent that another agent starts is a subagent.

**Roles and domains.** A role that does the work of a domain belongs to that domain (Step 4).

**The model call.** The model is called through the platform, which may choose a different model for different requests.

**One definition, two kinds.** In the reference implementation a person converses with a persistent agent, and another agent can start a task agent from the same definition to answer one question. The task agent has the role and the domain's knowledge. It does not have the persistent agent's session history, and it acts under its own identity.

**Autonomy as an aim.** The published models do not agree that autonomy is a goal. Several treat it as one (AAM/5C, Salesforce, EAAF and AWS among them), and two say it is not: Zhu, and CEAD ("the objective is not autonomous completion at any cost"). WARM states the aim as its scope and does not claim it as a distinction (see "What WARM adds, and its limits").

## Notes on Step 1 (the layers)

**Deployment.** The platform executes on infrastructure and calls providers. A model that the system hosts itself runs on its infrastructure; the Models service still mediates the call.

**Clients and outside systems.** A system that agents act on is reached through Tools, and it is a Provider when this system does not operate it. An application that calls an agent comes in through Channels. It is a client of the system and sits in none of the five layers.

**People's other relations.** People appear in the layer table as those who direct and approve. People also fill roles, request or receive results (a customer), and are the subject of the work (the person whose health or money it is). These relations do not carry the same authority. WARM has not developed them in detail. One is stated: when a person is the subject of stored data, Policy's rules on what is kept include that person's right to see, correct and delete it.

**What the platform test classifies.** The test classifies the responsibility and its stated guarantees, not how it is built:

- A platform service may use a model or an agent inside it. An evaluator that judges a work product against criteria it is given is still providing a platform service.
- Domain work may be a fixed script. A calculation, a connector to one bank and the tests of one codebase are domain logic, although nothing in them decides anything.
- One component can implement both. A mapping records the split, or leaves the placement open.
- Who uses a service today does not place it. A system with one agent needs no agent messaging; Messaging is still a platform service.

**Precedents for the test.** The test is not new. Data Mesh states it as a design rule for a data platform: "to not include any domain specific concepts or business logic, keeping it domain agnostic" (Dehghani, 2019). Domain-Driven Design states it for code inside one design: of generic subdomains, "Leave no trace of your specialties in them" (Evans, Domain-Driven Design Reference, 2015, p. 41). An older statement is that the platform supplies mechanisms and the work supplies meaning, after the separation of policy and mechanism in operating-system design (Levin, Cohen, Corwin, Pollack and Wulf, "Policy/Mechanism Separation in Hydra", Proceedings of the 5th Symposium on Operating Systems Principles, 1975, pp. 132-140). Data Mesh also states the move that follows from the test, taking a capability that domains duplicate into the platform: "Harvesting and extracting domain agnostic infrastructure capabilities into a data infrastructure platform solves the need for duplicating the effort".

**A design choice, not a finding.** A reusable responsibility discovered inside a domain is treated as a gap in the platform, so no observation can refute the test. What can be checked is its usefulness: whether a service stays meaningful, unchanged, when a second and a third domain use it.

**When the Domain layer matters.** The Domain layer matters once a system has several areas of work on one platform. A system built for one purpose has one domain and may never name it. The three platforms mapped to WARM are of this kind, or leave domains to the customer: none has a domain layer.

## Notes on Step 2 (the six groups)

**The services that carry each relation.**

| Group | The services that make the relation so |
|---|---|
| **Runtime** | Harness, Sessions, Tasks; Lifecycle keeps the list of which agents exist |
| **Capabilities** | The Harness sends context to Models, carries out calls through Tools, and finds the definitions of agents, tools and skills in the Registry. |
| **Knowledge** | The Harness reads Memory and Retrieval into the context window and writes back what was learned. A task stores its work products in Artifacts. |
| **Interaction** | An agent finds who is responsible in the Directory and reaches them through Messaging and Orchestration. People and applications reach agents through Channels. A message, an assignment or a request starts or resumes a session or a task. |
| **Governance** | Identity establishes who is acting on every tool call, message and memory write, and can revoke an identity. Secrets releases what that actor may use without showing it. Policy decides whether the action may proceed, issues a grant when it may, and decides what happens to stored data. Approvals obtains and records people's authorizations. |
| **Operations** | Observability records what they did, Evaluation judges it, Improvement proposes changes from the evidence, Releases makes the changes, and Reliability restores what fails. |

**Enforcement points in practice.** Two of the three platforms mapped enforce policy only at certain gateways or separately per product. "Constrains the other five" states what the group is for. An implementation has to show where each kind of call is checked. A reminder shown to an agent is not an enforcement point: in the reference implementation an agent was shown a count of unprocessed items on every turn for 17 days and did not act on it, while the scheduled jobs that gathered the items reported success.

**The two cross-cutting groups apply to each other.** A release can require an approval, so Governance constrains Operations. An approval decision is recorded, so Operations observes Governance.

**A cross-cutting group still uses working services.** Approvals reaches the person through Channels. Observability stores its records somewhere. Cross-cutting describes what a group applies to, not what it is built from.

**The relations are not a layering.** No group sits on another, and a system that lacks a service lacks the relations that service carries.

**The kind does not sort every service.** A working service is mostly called for its result. A cross-cutting service mostly applies to actions whose purpose lies elsewhere, and it has to be able to act on an action without the cooperation of the agent that performs it. Some cross-cutting services are also called directly: an agent asks Evaluation for a verdict, Releases for a deployment, or Secrets for the use of a credential. Some working services apply without being called: Environments isolates whatever an agent does. The stated overlaps are part of the model.

**Where the relations come from.** The relations are stated between groups and are derived from the responsibilities of the services in Step 3. The dependencies between individual services belong to each service's contract.

**Concerns that are not groups.** Some concerns touch several groups without being one. Security touches Governance, Runtime and Capabilities. Cost touches Models (which model is used), Policy (spending limits), Scheduling (how much may run at once) and Observability (what was spent). A budget is carried in a grant, enforced by Scheduling's limits and metered by Observability. Tenancy, several organizations or users on one platform, touches Identity, Policy, Environments and the services that store data.

**Group, service and module.** A **group** is a set of services that answer one question; it is a classification with stated relations, and it is not a unit that is built or replaced. A **service** is the unit with one responsibility and a boundary. A **module** is a unit of an implementation. WARM does not use "module" for anything in the model, because one service may be implemented by several modules and one module may implement parts of several services.

**Governance across domains.** WARM's Governance is a group of services. The rules come from domain charters and from the platform's operator, and people approve them. WARM names no body that sets rules for all domains. Data Mesh has one, its federated computational governance, with the split "what shall be standardized globally, implemented and enforced by the platform for all domains ... and what shall be left to the domains to decide" (Dehghani, 2020).

### Notes on human decisions and pre-approval

**Precedent for the kinds.** Charterion separates steps reserved for people, actions held for approval and the granting of authority most precisely; AEON and CEAD make the same separation in part.

**Where each kind is carried.** A step reserved for people is a domain rule. In the Finance example the person places every order himself. A pre-approval is recorded by Approvals and enforced by Policy. A held action is held by Approvals, which reaches the person through Channels. A change to a role or a rule is an action of one of the three kinds; Releases makes the change.

**Options for changes to roles and rules.** An implementation may reserve every such change for a person, hold each one, or pre-approve some classes of change. The reference implementation pre-approves an agent's edits to agent definitions and to the shared rules: each edit is a marked commit with a working revert, and it is reported afterward. It reserves any change that weakens a check on an action that cannot be undone. A mapping of the reference implementation on 2026-11-12 found this practice, which an earlier wording of the model ("only a person gives an agent its authority") did not allow.

**Examples from the reference implementation.** Three pre-approvals are in use. A change is merged after independent reviews agree and the checks pass, and the person is told afterward. An agent may edit an agent definition without asking, if each edit is a marked commit with a working revert and is reported afterward. Arithmetic that follows from a decision the person already approved is not approved again.

**An agent that signs off on another agent's work** acts under a pre-approval. It is not a fifth kind of decision: people wrote the rule, Policy enforces it, and the review it relies on is Evaluation.

**What the sources add.** Six of the fourteen models state pre-approval in full: Charterion, AAM/5C, Zhu, AOS, EAAF and Yu et al. (in a worked example). Six state part of it, AEON among them (it does not say that the second authority is a person). Microsoft and Google do not state it as a whole (`prior-work/autonomy-check.md`). Statements that WARM has not adopted:

- **Charterion** (El Hassani): thresholds that permit, escalate or deny; an authorization with a validity interval and a review date; a named, reachable person who watches an agent at the autonomous level, with a cap on how many agents one person watches; a fourth outcome for a decision whose evidence is too weak.
- **AAM/5C** (Goujon): the advance authorization is short-lived and revocable by event; each act under it is audited and attributed to the people who co-signed the policy; a self-declared attribute can only add a restriction.
- **Zhu**: the authorization is a lease that ends at completion, timeout, a broken budget or a halt; an agent reviewer, not a person, decides a middle class of change.
- **AOS**: delegated scope can only narrow; the unavailability of a person is a failure mode with stated responses.

**Where the sources disagree.** On an action that cannot be undone: AAM/5C requires a person ("irreversible acts, whatever their criticality, require human validation"); Charterion allows autonomy where a compensating step exists; Zhu accepts a second key from a reviewer, a deterministic control or a person. WARM takes neither side. The model states one requirement: a pre-approval covers an action that cannot be undone only if it says so explicitly and names the kind of action. The rest is an implementation's choice. The sources also disagree on whether another agent can stand in for the person, and on what happens when no person is available.

**Options for an action that cannot be undone.** An implementation chooses among these, and may combine them: never pre-approve such an action, and hold each one for a person (AAM/5C); require a compensating step (Charterion); make the action undoable, by moving a file to a trash folder, marking a record deleted or delaying the effect; require a stronger confirmation when the pre-approval is given, such as typing the name of the action; require a second, independent reviewer (Zhu); give the pre-approval a short term; report each such action to the person afterward. The reference implementation's choice is its owner's: such an action may be pre-approved with an explicit authorization, and the system makes it undoable where it can.

**No levels of autonomy.** Six models grade autonomy in levels: AAM/5C (0 to 4), Charterion (read, propose, commit, autonomous), CEAD (L0 to L4), ASOC (L0 to L4), AOS (four levels) and Zhu (four classes of decision by risk). The six do not grade the same thing: some grade a system, some an agent's contract, and Zhu a class of decision. WARM has no levels. Its kinds of decision apply to a class of action, and one agent commonly acts under different kinds for different classes: it merges reviewed changes under a pre-approval and has every outbound message held.

**The term.** The owner's rule, 2026-11-11: "a preapproval should expire or, if not, explicitly not expire".

## Notes on Step 3 (the services)

**Secrets.** The values are those that platform components and agents must not know directly: API keys, passwords, tokens, account numbers. Secrets releases each one only to the component that needs it, without placing it in an agent's context, and rotates or revokes it.

**Policy.** The rules come from domain charters and from the platform's operator. They cover three things: what may be done, what may be said (what content may enter and leave models and tools), and what is kept (how long stored data is retained, when it is purged, how it is protected, and what the person it is about may see, correct and delete). WARM names no separate guardrail service.

**Evaluation.** Evaluation may assess before, during or after an action. Policy may use an assessment, such as a risk score, as an input to its decision.

**A service's results vary.** A platform service has an explicit boundary and stated guarantees. Its implementation may be fixed code or an agent, and its results vary with its inputs and its state: Approvals returns approved, denied or still pending; Retrieval returns whatever the source now holds. Predictable guarantees are the aim. Identical results are not.

**Job.** The word "job" is kept for scheduled work: a task that a schedule or an event starts. A script or an agent may carry it out.

**Sessions, Tasks and Memory.** The cut between the three is by what is kept: the history of a stretch of work (Sessions), the lifecycle of a unit of work (Tasks), and what was learned (Memory). One store may serve more than one of them.

**The Harness service and harness products.** The word "harness" names two things. The Harness *service* runs each agent's loop: it assembles the context, calls the model, and carries out tool calls. A harness *product* usually bundles the loop with several other services, such as sessions, tool mediation, subagents and permission checks. A mapping of a real system records the bundle: which of the twenty-five responsibilities the product provides, and which are built around it. One of the mapped platforms can replace the loop while it "keeps ownership of channels, sessions, policy, and state", which is the same boundary.

**Where what an agent knows is kept.** What an agent knows and remembers is spread across six services, by how long it lasts and who wrote it.

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

## Notes on Step 4 (domains)

**Relation to Domain-Driven Design, Team Topologies and Data Mesh.** Three bodies of work outside agent systems describe areas of work, shared platforms or both. They were read against v0.12 on 2026-11-11 (`prior-work/ddd-teamtopologies-datamesh.md`; one reader; Evans's 2015 Reference, the Team Topologies site and two articles by Dehghani; the three books were not read).

| What WARM states | Who states it already | What differs in WARM |
|---|---|---|
| Domains of work and a shared platform in one model | Data Mesh (domains, a self-serve platform, federated governance); Team Topologies (stream-aligned teams and platform teams) | WARM applies the shape to agent systems, and adds agents as the actors |
| A test for what belongs in the platform | Data Mesh ("domain agnostic"); Domain-Driven Design (generic subdomains, cohesive mechanisms) | Stated as a test of one responsibility |
| One accountable owner | Data Mesh, for data: "The accountability of data quality shifts upstream as close to the source of the data as possible" | For every responsibility, at the size at which work is handed over |
| A record of who is responsible for what | Partial: the context map of Domain-Driven Design; the Team API; the Data Mesh catalog of data products "with their meta information such as their owners" | None of the three records which domain is accountable for which responsibility |
| What an area offers other areas | The data product (Data Mesh); the Team API (Team Topologies): "a description and specification that a team can define that tells others how to interact with that team" | The published skill is loaded by an agent when it needs it |
| How areas relate | The context-map relationships of Domain-Driven Design; the three interaction modes of Team Topologies | WARM names one relation, the handoff, and adopts neither typology |
| Reaching the platform through a defined interface | Team Topologies' X-as-a-Service; Data Mesh's self-serve platform | The same relation |
| Rules set by domains and applied by the platform | Data Mesh: rules "defined by the global federated governance team, and automated by the platform" | WARM's rules come from each charter and from the operator; it names no governance body |

What WARM does that none of the three does in full: it defines an area of work by a charter, apart from the people and agents who fill its roles. In Team Topologies the area and the team are one. In Data Mesh a domain is the teams and systems that manage something. Domain-Driven Design comes nearest. It bounds a model, and a team is only one of the ways to set the boundary: a bounded context is "A description of a boundary (typically a subsystem, or the work of a particular team) within which a particular model is defined and applicable" (Evans, 2015). WARM's domain is not a bounded context, although inside a domain terms and rules do have one meaning.

What WARM cites and does not adopt: the context-map relationships and the interaction modes. Both sources recommend a defined protocol or a published language between areas, where WARM has agents ask in ordinary language. What WARM leaves out: a part shared deliberately by two areas (the shared kernel of Domain-Driven Design). In WARM two domains accountable for the same responsibility is an overlap to resolve. Also absent from WARM: translation between areas, priority among domains, temporary helper roles, and the platform run as a product with its own measures.

A search of arXiv and the web on 2026-11-11 found no source that organizes a system of agents with all three. The Team Topologies authors map team boundaries and cognitive load to agents and keep the boundary with a human team. Writing on Domain-Driven Design mostly sets one agent for each bounded context. Work on Data Mesh mostly treats agents as consumers or builders of data products. One book that appears to apply mesh ideas to agents as the nodes, "Agentic Mesh" (Broda and Broda, 2026), could not be opened and has not been read.

**Words with other meanings.** "Domain" and "service" have established meanings elsewhere. In Domain-Driven Design a domain is a subject area and a domain service is an operation in a model. In Team Topologies any team may provide something "as a service". In WARM only the platform has services, and a domain is an area of work.

**How large a domain should be.** WARM has no rule. Team Topologies sizes a team by cognitive load: "Explicitly thinking about cognitive load can be a powerful tool for deciding on team size, assigning responsibilities, and establishing boundaries with other teams". The Team Topologies site applies the same idea to agents: "this human cognitive boundary directly maps to an AI agent's context window" (2026). The reference implementation's nearest evidence is about context too: unattended work run inside a conversation filled the conversation's context (see "Where the work runs"). This is guidance, not a part of the model.

**Scoped responsibilities.** Where a system serves several products, projects or accounts, a responsibility is scoped by them: publishing for one product and publishing for a personal account can have different accountable domains.

**Contributing is not owning.** The Software domain builds the Finance domain's bank connector, and Finance remains accountable for the books.

**Using the Directory.** An agent may be given a summary of the Directory when it starts, and it consults the Directory itself when it is unsure or when the summary may be out of date. It works as a company directory does, for responsibilities.

**The published skill in the reference implementation.** The reference implementation does not have published skills yet. The when and how of asking another domain is copied into each agent's definition: the research agent's definition carries the rule that outbound email goes through Communications, with the steps. A check on 2026-11-11 found a routing line in one definition that contradicts the directory. The published skill is the owner's decision of 2026-11-11 ("i lean towards a domain publishing a skill"), and it is untested.

**Handoffs.** A handoff can also be carried as a tool call, when the other agent is exposed as a tool; Orchestration still tracks the assignment. The work is an ordinary task in the accountable domain, requested by an agent and not by a person. How much structure an exchange has (a free request, a brief with fixed fields, a required result format) is a choice of the workflow. In the reference implementation, a message in a person's name is sent only on that person's approval, whoever asked for it.

**Questions the division raises.** A responsibility with no accountable domain is a gap. Two domains accountable for the same scoped responsibility is an overlap. Work carried out by another domain is not by itself misplaced: delegation, consultation and shared inputs are normal. A map of the reference implementation raised candidates of each kind. They have not been verified.

**A second example: research.** In the reference implementation a person converses with the research agent directly, and the agents of other domains hand it questions. Fetching a page or running a search works the same whatever the question is, so fetching is a platform service (Retrieval). Deciding what to look for, checking one source against another and saying how far the evidence goes is an area of work with its own knowledge, tools and criteria, so research is a domain. Communications receives work because of rules (who may send in a person's name). Research receives it because of skill and tools.

**Rules that are not Policy's.** Rules that authorize or forbid an action go to Policy and Approvals. Other rules go to the service that applies them: a preference for a model goes to Models, and the order in which sources are trusted goes to Retrieval or stays in the domain's own logic. A mapping records the carriers a system actually uses.

**New work for a new domain.** A new domain can require new work, such as a connector to a system no other domain uses. That logic is part of the domain, and Tools carries it.

**Where the work runs.** Where the work runs is a separate choice from how it starts. The reference implementation ran unattended work inside its persistent agents' conversation sessions twice: first periodic checks, then sprints run inside the session of the agent that planned them. Both times the work filled the conversation's context and each delayed the other, and both times the remedy was to move execution out of the conversation, into scheduled jobs and task agents. One of the mapped platforms, OpenClaw, moved its periodic checks into ordinary scheduled jobs between July and October 2026, independently. This is guidance from experience and not a rule of the model. Other arrangements can work, and separate execution does not remove all interference: workers still share tools, rate limits and stored state.

**One worker or a team.** A durable backlog is one reason to give a group of responsibilities a team (a coordinating agent and task agents). The choice between one worker and a team depends on volume, how much can run at once, the cost of coordinating, and whether the stages are independent. Execution can pause for a person's decision.

**Subdomains: the evidence and the word.** The subdomain is the owner's decision of 2026-11-12, and its support is thin. It rests on one decided case: on that day the owner placed "running the product in production" inside the Software domain, as a named group of responsibilities, where the system's files had listed it as a domain of its own with no agent. The inventory below found 45 groups of responsibilities in nine areas, which shows that domains divide and does not show that each group is a subdomain. What a subdomain carries (its own workflow; optionally roles, knowledge, tools and criteria) is a first statement and is untested. Among the published models, AEON has subdomains that provide capabilities. In Domain-Driven Design a subdomain is a part of the subject area that software models (core, supporting or generic), which is a different thing; WARM's subdomain is a part of an area of work.

**Domain patterns: the evidence.** An inventory of the reference implementation on 2026-11-11 (`domain-pattern-inventory.md`; one reader) listed 45 groups of responsibilities in nine areas: the seven domains, and two areas (operations and coordination) whose agents also provide platform services. It recorded, for each group, how work arrives, who carries it out, who judges it done and when a person is involved.

- Eight shapes recur, such as conversation with the person; a scheduled script with a mechanical check and no person; a persistent agent that judges gathered items and tells the person afterward; and a request handed over, with each action approved by the person.
- Eighteen of the 45 groups fit none of the eight, among them five of the six Software groups and all four Marketing groups.
- Every area mixes shapes, which is why a pattern attaches to a group of responsibilities and not to a domain.
- Conversation with the person occurs in six of the nine areas, so it is not the pattern of some domains.
- The factory pattern has one instance. It is a worked example and not yet a pattern that recurs.
- Two of the eight shapes involve no agent: a script does the work.

The author's earlier proposal of three patterns (expert, operator, factory) did not survive the inventory. One system does not establish a catalog.

**A pattern with an unobserved step.** In the shape where a persistent agent judges gathered items, the gathering jobs were observed and the judging was not. The jobs reported success for 17 days while the judging had stopped. A pattern should say which step shows that the work was done, not only that it was started.

**A template for workflow.** Work in many domains passes through the same six stages, which WARM offers as a template, not a requirement: **intake → plan → execute → verify → report → improve**. In the last stage the people and agents of a domain change its way of working from evidence. The platform supports that with Evaluation (the evidence), Improvement (the proposed change) and Releases (the rollout).

**Persistent agents and task agents.** A persistent agent commonly starts task agents for parts of its work, so a domain with one persistent agent still has many agents over time.

**Provisional: an agent that provides a platform service.** A component that provides a platform service may itself be an agent: a router that delivers messages, a reviewer that evaluates work. Such a role belongs to the platform. Its definition comes from whoever operates the service and not from a domain's charter. An agent in such a role still uses the platform like any other agent, and it has to meet the same service boundary as any other implementation of that service. One consequence needs a rule that WARM does not yet state: an agent that provides Messaging or Reliability cannot rely on its own service to recover, so it needs a way to start and be repaired that does not pass through itself. In the reference implementation two persistent agents do some work of this kind along with domain work. Their responsibilities are classified one by one, and several are unresolved.

## Notes on Step 5 (implementations)

**More than one implementation.** Scrum and Kanban both implement software development, and an implementation's ideas can be reused in another domain.

**One boundary per service is not a rule.** The mapping between services and components is many to many. One boundary for each service is an experiment of the reference implementation and not a rule of the model.

**What a mapping records.** A full system is described by mapping its parts to WARM. For each platform service the mapping records which component implements it, who supplies that component (the harness vendor, the builder of the system, a third party), who operates it, what it guarantees, and what evidence the entry rests on. One service can have more than one implementation. An entry may be left unresolved. A component that implements no platform service is not a fault; it may be domain logic.

**A component that spans parts.** In the reference implementation the persistent agents run in a terminal multiplexer on a remote server, and a person reaches them from another machine. The multiplexer maps to three parts and to no single one: the pane a person types into is a channel (Channels); with the script that starts, stops and lists the panes it implements Lifecycle for persistent agents; and it keeps each harness process running, which is Infrastructure. Remote access splits the same way: the network path is Infrastructure, the applications a person uses to reach an agent are channels, and establishing who the person is belongs to Identity.

**Suppliers change.** Suppliers of a service change over time. Harness vendors now supply services that builders used to write themselves (sessions, memory, scheduling and messaging are recent examples). A builder who keeps each service behind a clear interface can change its supplier with less rework. Domain-Driven Design states the same aim for code in its pluggable component framework: "diverse implementations of those interfaces to be freely substituted".

# Appendix B. Contract questions

A service's **contract** is the set of guarantees it states: what it does on failure, cancellation, delegation, stale state and recovery. WARM uses the word in this one sense. The core names each service and its responsibility and states no contract. This section lists what the papers on each group have to settle. Most of these questions come from published models with no named adopter, which is why they are questions and not parts of the core.

Four questions cut across groups. Whether a retried task repeats an effect depends on the contract between Tasks, Tools and the outside system. How an action's effects outside the system are undone is owned by no service yet. Whether the configuration that runs is the one that was reviewed is open. Which rule takes precedence when rules from different sources conflict is open.

## Governance

**Pre-approvals.** How conditions are written so that Policy can check them. How a term is recorded and what happens when it ends while work is in flight. Who may revoke a pre-approval, and what happens to actions already granted. What counts as an action that cannot be undone, and which step keeps one undoable. Whether each act under a pre-approval is audited and attributed to the person who gave it (AAM/5C). Whether an agent at full autonomy needs a named, reachable person (Charterion).

**Grants.** When Policy allows an action, the authority to carry it out is a grant: scoped to that action or that task, limited in time and revocable. The grant is checked again when the action runs, not only when it is requested, because a deferred or delegated action may run long after the decision. A grant passed to another agent can only be narrower than the one it came from, in scope, in time and in budget. AAM/5C gives deciding, issuing and enforcing to separate components; WARM keeps all three in Policy and leaves the split to an implementation. The request already follows this order: the mail credential is released only after the person approves. To settle: scope, time limit, recheck at run time, narrowing on delegation, and whether the three steps are separate components.

**Outcomes of a decision.** A Policy decision may allow, deny, hold the action for a person, narrow it, or be unknown. To settle: what each outcome guarantees to the caller.

**Separation of duties.** Whoever writes a rule does not approve it. Agents started by the same agent do not count as independent of each other. To settle: which reviewers count as independent.

**Checking the enforcement point.** The condition in Step 2 can be checked: compare a record kept at the resource, of what the tool, model or store received, with what the enforcement point admitted; an action in the first and not in the second did not pass the enforcement point. AAM/5C (Goujon) states the check and its blind spot: actions taken under a person's or a script's identity.

**The person.** Who decides when the named person is unavailable, and how much one person can be asked to decide.

**Registration as a gate.** Policy may require that an agent, tool or skill be registered before it is used, and adding an entry is a release, which Evaluation and Approvals can gate. Not being registered can deny an action; finding a destination still grants nothing. Each Registry entry names its owner, the person or team who answers for the definition. The owner of an entry is separate from the Directory's accountable domain, which answers for a responsibility.

## Runtime

**The stop path.** A system needs a way to stop an agent that does not pass through the agent or through a service the agent provides. Tasks cancels a unit of work, Lifecycle suspends or ends a running agent, and Identity revokes its identity. This generalizes the provisional rule about agents that provide Messaging or Reliability, from repair to stopping.

**Lifecycle's scope.** Whether Lifecycle covers task agents as fully as persistent agents, and who stops every agent built from one definition (raised by the second rater).

**Retries.** Whether a retry repeats an effect.

## Capabilities

**Side effects.** A tool's definition in the Registry declares its side effects, whether they can be undone and whether a retry is safe. That declaration is what lets Tasks decide whether to retry. To settle: who owns undoing.

**Published skills.** What a domain's published skill must state (what is offered, when to use it, how to ask, what comes back), how a change to it is released, and how an agent learns that the copy it loaded is out of date.

## Interaction

**Intake routing.** An inbound request that names no agent still has to reach one. Channels delivers by address: a conversation with the finance agent reaches the finance agent. When the address does not settle it, the request is routed by what it is about, using the Directory. The component that classifies the request may be an agent providing this platform service. All three vendor architectures compared have such a router (Microsoft's Classifier, AWS's routing workflow, Google's dispatcher agent). That the gap is real is well supported; where routing belongs (Channels, the Directory or Orchestration) is less certain.

**Handoffs.** What accepting a handoff guarantees, and how the requester learns that work was denied, is pending or is done.

## Operations

**Assessment at run time.** Whether assessment before and during an action belongs to Evaluation or to a service of its own. Whether a standing trust score for an actor is Evaluation's (raised by the second rater).

**Patterns.** Which step of a domain pattern shows that the work was done, and which service observes it.

**The reviewed configuration.** Whether the configuration that runs is the one that was reviewed.

## Knowledge

No question from the comparison is specific to this group. Retention, purging and the rights of the person the data is about are Policy's rules (see the notes on Step 3).

# Appendix C. Evidence

## Example: one request across two domains

"There is a duplicate charge from the gym this month. Dispute it." This is one illustrative path. Another workflow may omit, reorder or add steps, and decisions that belong to a domain enter at every step.

| Step | What happens | Domain | Platform services |
|---|---|---|---|
| 1 | The request reaches the finance agent in the conversation the person is using. | Finance | Channels, Identity, Sessions |
| 2 | The finance agent finds the two charges and checks them against past decisions. | Finance: its bank connector, its knowledge of the accounts | Harness, Models, Tools, Memory, Retrieval; Policy checks each call |
| 3 | A dispute needs a message to the merchant. The finance agent sees that messages in the person's name belong to Communications, and loads the Communications skill to see how to ask. | Finance | Directory, Registry |
| 4 | It hands the work over: the facts, what is wanted, what counts as done. | Finance → Communications | Orchestration, Messaging, Tasks |
| 5 | The communications agent drafts the message, using the contact and the person's voice. | Communications: its knowledge, and its rule that every such message needs approval | Harness, Models, Retrieval |
| 6 | The proposed send is checked. No pre-approval covers a message in the person's name, so the action is held and the person is asked. | Communications | Policy, Approvals, Channels |
| 7 | The person approves. Only then is the mail credential released and the message sent. | Communications | Approvals, Secrets, Tools |
| 8 | The result goes back. The finance agent records that the dispute message was sent and tells the person. | Finance | Messaging, Orchestration, Memory, Channels |

Step 6 has three other outcomes: the person denies the send, changes the draft, or does not answer. In each case nothing is sent, and the finance agent is told that the work is denied or still pending.

Throughout, Tasks tracks each unit of work, Observability records each step, and Evaluation can check each result against the criteria of the domain accountable for it. A scheduled scan could have found the duplicate and started the same work with no conversation; step 1 would then be a job started by Scheduling.

The request stops for a person because this class of action is held. Had the person pre-approved dispute messages to merchants under stated conditions (a duplicate charge, an amount under a limit, a fixed wording), step 6 would check the conditions and issue the grant, and the person would be told afterward.

The steps follow the reference implementation's rules for email. They are an illustration of the model and not a record of one run. Step 3's skill does not exist in the reference implementation yet (see the notes on Step 4).

## Example: Software

Software is the domain that builds and changes software. It is the most developed domain in the reference implementation, and the rows of the charter were drawn largely from it. The example therefore illustrates Steps 4 and 5 and is not an independent test of them. It has three parts: the domain, the pattern and the implementation.

**The domain.**

| The charter states | In the reference implementation |
|---|---|
| Goals | Working software, merged and released |
| Responsibilities | Building and changing software for every domain, including the platform's own software |
| Roles | A coordinator, developers, reviewers; a person as product owner |
| Workflow | A backlog, tasks, reviews, a wrap |
| Domain knowledge | The codebase, its conventions, past decisions |
| Domain tools | Source control, CI, issue tracker |
| Domain rules | Who may merge what; which changes need a second reviewer; which classes of change are held for the person |
| Acceptance criteria | Tests pass; reviewers approve |
| Published skill | Not written yet. How to ask for software work is stated in a shared instruction file and repeated in agents' definitions |

**The pattern.** The domain's main work, building a planned set of changes, follows the factory pattern. Work arrives from a backlog that the person ranks. A coordinating agent and task agents carry it out. Stated criteria and reviewer agents judge each result. The person sets the rules in advance, including the pre-approval to merge reviewed work, and is told afterward. Not all of the domain's work follows this pattern: ranking the backlog is a conversation with the person, and scheduled engineering jobs are scripts.

**The implementation.** The reference implementation carries out the main work in this pattern in sprints. Another implementation of the same pattern could use a continuous flow.

Continuous integration (CI) belongs to the Software domain. It does not work the same whatever the work is about: what is integrated, which checks run and what passing means are all about code. So CI is part of this domain's workflow, tools and acceptance criteria. The general parts beneath it are platform services: Environments gives a build an isolated place to run, Scheduling starts it on an event, Tasks tracks the run, and Evaluation reports the verdict. The runners are Infrastructure.

One property is prominent in this domain. Its work products are software, and the platform is software. So the agents of the Software domain can build and change the platform they run on, and the tools the other domains use. Other domains change the system too (a security domain changes policies; every domain improves its own way of working, and any domain may produce software). In the reference implementation the Software domain is accountable for changes to platform software.

When the work is building the platform or changing the infrastructure, the same services still apply: Policy and Approvals gate those changes, Evaluation judges them, and Releases versions them and keeps a way back. The model states that the services apply. It does not show that an implementation enforces them. That requires a control that an agent cannot change by itself, such as an approval or deployment authority outside the agent's reach.

For this reason the reference implementation got the platform and the Software domain working first: the two improve each other, and every other domain benefits. A team that starts from a managed platform or from another domain may choose a different order.

## Example: Finance

Finance is a second domain set against the charter's rows. The entries are simplified from the declared configuration of the reference implementation's finance agent.

| The charter states | In the reference implementation |
|---|---|
| Goals | Know where the money goes, and track spending against the plan |
| Responsibilities | Tracking spending, watching subscriptions, and reporting where the money goes |
| Roles | A financial advisor agent, which gathers and analyzes. A person, who decides, approves every order and places it himself |
| Workflow | Conversations with the person. Scheduled jobs gather data, scan for alerts and write summaries. No standing backlog was found |
| Domain knowledge | The accounts, the plan, and past decisions on how to categorize spending |
| Domain tools | Connections to banks, a budgeting service and a brokerage |
| Domain rules | The agent never moves money or changes a position; no scheduled job or task agent trades; bulk changes and deletions need the person's confirmation |
| Acceptance criteria | A balance carries its time and names any stale source; categorization follows the recorded decisions; most other judgments are the person's |
| Published skill | Not written yet |

The rules show all three kinds of human decision. Placing an order is reserved for the person. Bulk changes and deletions are held for the person. Categorizing a transaction by a decision the person already recorded is pre-approved.

The rules are declared in the agent's definition, a hook and a script. They are candidates for enforcement by Policy and Approvals. How much of them those services actually enforce has not been verified, and one rule (the thresholds for an alert) lives in a script that Policy does not read.

Work here starts from a person's request or from a schedule. The scheduled jobs are scripts, and anything they find that needs judgment waits for the agent to read it in a conversation. That is how this implementation is built today and not a property of the domain: a job could start a task agent that judges and escalates.

The charter's rows describe this domain, with two strains the model does not yet resolve: the person is the subject of the work as well as its director, and the person carries out some of the work himself. The map was made by the model's author and is not an independent test.

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
| Tasks is not a separate store | All three | Tasks restated as a responsibility that does not require its own store; the cut between Sessions, Tasks and Memory stated |
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

This section is carried from v0.12. Where it names "How the groups relate", a numbered point or "Three kinds of human decision", it refers to v0.12's text; "How the model was derived" below says where that text is now.

On 2026-11-11 WARM was compared, part by part, with fourteen published reference models and architectures, in two rounds. The first round compared v0.11 with six:

- Yu, Rabhi, Zhu and Lu, "A Reference Architecture for Integrating Agentic AI into Enterprise Software" (arXiv:2610.14818, October 2026);
- Zhu, "Fluid Structure, Rigid Record" (arXiv:2608.08516, August 2026);
- Goujon, "Agentic Architecture of Information Systems. The AAM/5C Model: A Reference Model for Distributed Autonomy" (arXiv:2610.30221, October 2026), all 120 pages;
- Microsoft's Multi-Agent Reference Architecture (the GitHub repository, every chapter);
- AWS Prescriptive Guidance on agentic AI (six guides);
- the agentic AI pages of Google Cloud's Architecture Center (17 pages).

The second round compared v0.11, with the first round's changes treated as planned, with eight more. They are the most complete of the sources that the documented search newly found:

- El Hassani, Charterion v2.0 (Zenodo 10.5281/zenodo.22829848, September 2026), read in full: the first mapping read about 110 of its 290 pages, and the rest were read afterward with no change to a verdict (`prior-work/charterion-full.md`);
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
| Charterion v2.0 (counts from the first, partial reading) | 112 | 9 | 33 | 24 | 6 | 12 | 28 |
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

## How the model was derived

The two subsections below are carried from v0.12 with small corrections. They record how the mapping to three platforms and the comparison with published models changed the list of services. "Point 2", "point 3" and "point 4" refer to the seven points of v0.12's "How the groups relate". v0.13 keeps three of the seven in Step 2 (the enforcement point, the grant, separation of duties) and moves the others to the notes on Step 2 and to the contract questions. v0.12's three kinds of human decision are restated in Step 2: pre-approval is a kind, and the granting of authority is a principle.

### Six services the mapping changed

The mapping to three platforms changed this list in six places.

**Directory is new, and no mapped platform has it.** Each platform has a registry, which is a catalog: it answers "what agents, tools and skills exist". None records which area of work is accountable for what. v0.10 put the directory inside the Registry, which then carried three responsibilities. It is now a service of its own, in Interaction, because it answers "who do agents work with". Step 4 describes its entries.

**Improvement is new.** All three platforms run a loop that turns evidence from past work into changes: recommendations from traces and comparisons of versions on two of them, and on the third a loop that revises learned skills and promotes entries into memory. The reference implementation has one too (a retrospective at the end of each sprint; a nightly pass over its documents and memory). v0.10 had no place for it. In WARM, Improvement proposes, a person or a release process decides, and Releases makes the change. That separation is a choice of the model: one platform applies such changes by default with no approval, keeping a version to go back to.

**Skills are definitions, not memory.** v0.10 kept skills in Memory as procedural memory. Two platforms and the reference implementation keep them as versioned files that are loaded when needed and released like other changes; the third revises skills from experience and saves a version before each change. So the Registry holds skills, Releases changes them, and Memory keeps what agents learn: facts and events. A lesson that should change how a kind of task is done starts as a Memory entry or as evidence, and becomes a changed skill through Improvement and Releases.

**Channels serves applications as well as people.** All three platforms give a program a way to call an agent: an invoke interface, a streaming endpoint, an endpoint compatible with a model API. v0.10 had only Human channels. The service is renamed Channels and carries both.

**Tasks names a responsibility and does not require its own store.** No mapped platform keeps a separate store of tasks. One uses the same checkpoints as its session history and its run log. One built a shared registry of tasks in March 2026 and removed it in September 2026, giving duplicated state as the reason. WARM keeps Tasks as a responsibility that every runtime has to meet: track a unit of work, retry it, cancel it. The cut between three services is by what is kept: the history of a stretch of work (Sessions), the lifecycle of a unit of work (Tasks), and what was learned (Memory). One store may serve more than one of them.

**Scheduling and Policy each gained a part of their responsibility.** Deciding what may run next when capacity is limited (queues, lanes, limits on concurrent work) is part of deciding when work starts, so it is in Scheduling. Rules on stored data (retention, purging, protection) are part of Policy; the notes on Step 0 rely on them.

**Artifacts is unchanged, and no mapped platform provides it.** Each has only a partial counterpart to a versioned store for work products. WARM keeps the service, because sustained work produces reports, files and pages that outlast a session and need versions. An adopter should expect to build it.

### What the published models changed

The comparison with published models ("Compared with published models") ran in two rounds. The first, with six models, changed no service: it added to the responsibilities of five services and to the Registry's text, and it added three points to how the groups relate. The second, with eight more models, made eleven further changes, one of which adds a service, Lifecycle, and brings the count to 25. This subsection describes the larger changes of both rounds; the rest are listed in "Compared with published models".

**Grants, and the split of deciding, issuing and enforcing.** Yu et al., Zhu and AAM/5C each have a step that v0.11 lacked: authority scoped to one task or action, limited in time, issued only on a positive decision, checked again when the action runs, and revocable. WARM calls it a grant and puts it in Policy (point 2 of "How the groups relate"). AAM/5C gives proposal, decision, issuing, enforcement and execution to five different holders, with separate signing keys, so that no one component can authorize itself. WARM keeps deciding, issuing and enforcing in one service and leaves that split to an implementation.

**Separation of duties.** The same three sources state that whoever proposes or performs an action does not approve it. Yu et al. state it for people (the approver "is not the submitter"), Zhu for agents ("No agent controls the full chain"), and AAM/5C for the people who write and audit rules. v0.11 had no such rule. It is now point 3.

**Stopping an agent.** Five of the six sources have a way to pause, suspend or stop an agent at run time: Microsoft's "pause/disable an agent class", AWS's "circuit breakers for abnormal behavior patterns", Google's "monitor, override, and pause agents", Zhu's stop path that does not pass through the data plane, and AAM/5C's emergency stop "independent of the authorization chain". v0.11 had no place for it. The first round gave suspension to Identity. With Lifecycle (below), a running agent is suspended or ended by Lifecycle, its identity is revoked by Identity, a unit of work is still canceled by Tasks, and point 4 requires that the stop not pass through the agent.

**Registration as a gate, and owners on entries.** In all three vendor architectures a registry is a governance record, and registration is a precondition for use: Google's agents "only connect to inventoried, administrator-approved MCP endpoints". The Registry keeps its one responsibility, and two relations are added. Policy may require that an agent, tool or skill be registered before it is used, and adding an entry is a release, which Evaluation and Approvals can gate. Not being registered can deny an action; finding a destination still grants nothing. Each entry also names its owner, the person or team who answers for the definition. The owner of an entry is separate from the Directory's accountable domain, which answers for a responsibility. The second round added one statement from AOS and from Steinder and Franke: a tool's definition in the Registry declares its side effects, whether they can be undone and whether a retry is safe. That declaration is what lets Tasks decide whether to retry, and it gives the open question on undoing a concrete input.

**Policy and content.** Microsoft, AWS and Google place the filtering of prompts, model outputs and tool payloads (injection, harmful content, sensitive data) in their governance components. v0.11 worded Policy for actions and stored data. Policy now covers what may be said as well, and "content filters" joins its industry terms. WARM names no separate guardrail service.

**Events.** Yu et al. have a responsibility for asynchronous and event infrastructure that carries events between components, and one of the three platforms mapped earlier had outbound events. In v0.11 Messaging delivered only between agents, and no service distributed events. Messaging now delivers events to their subscribers as well. Scheduling still starts work on an event.

**Lifecycle, the 25th service.** Nothing in WARM owned which agents exist. Three of the four platform-like models of the second round make the lifecycle of a running agent a top-level component: AOS's "Agent lifecycle", whose representative failure is an "Orphaned agent"; Steinder and Franke's first primitive, "Agent lifecycle"; and EAAF's Agent Lifecycle Manager, which "manages the complete creation, maintenance, and retirement of agents". The platform mapping had recorded agent provisioning in OpenClaw as a misfit; AAGMM, a governance maturity model that the search found, is about agent sprawl; and Microsoft, AWS and Google can pause or disable an agent at run time. Before this round the pieces were spread over Identity, Sessions, Tasks and Orchestration, and no service could say which agents are running or who started one. Lifecycle creates, suspends, resumes and ends agents, and keeps the list of which agents exist. It is the first Runtime service that concerns an agent as a whole: Sessions concerns a stretch of an agent's work, and Tasks a unit of work. Its failure case is an orphan, an agent that nobody owns or lists. In the reference implementation it is the launcher that starts, stops and lists the persistent agents, and the board that lists running task agents. That the gap is real is well supported. Making it a service, and not a widening of Identity and Tasks, was the author's call; the owner accepted it on 2026-11-11.

**Assessment before and during an action.** All four platform-like models of the second round assess risk, confidence or trust at run time and use the result to decide whether an action proceeds; WARM's Evaluation judged only finished work. Evaluation now assesses before, during or after an action, and Policy may use an assessment as an input. That the gap is real is well supported; its placement in Evaluation, and not in a new service, is less certain.

## Glossary

| Term | Meaning |
|---|---|
| **Agent** | An identified actor that carries out one or more assigned roles. It runs on the platform: the Harness service runs its loop with a model. Its identity, memory and history persist through changes to its definition, harness or model. |
| **Agent definition** | The description of a role: its instructions and the skills it refers to. A charter includes one for each role an agent fills; the Registry holds it. Several agents may use one definition, and it may be revised. (Provisional: the operator of a platform service writes one for an agent that provides the service.) |
| **Artifact** | Something an agent produces and stores: a report, a file, a page. |
| **Charter** | The written definition of a domain: its goals, responsibilities, roles, workflow, knowledge, tools, rules, acceptance criteria and published skill. People approve it. |
| **Contract** | The guarantees a service states: what it does on failure, cancellation, delegation, stale state and recovery. WARM does not yet state any service's contract. |
| **Directory** | The platform service that records each scoped responsibility, the domain accountable for it, and how to reach a role of that domain. People set its content. |
| **Domain** | An area of work: a body of specialized knowledge, a set of responsibilities that belong together, and one or more patterns for carrying them out. Its charter writes these down. A domain does not act; the agents and people in its roles do. |
| **Domain pattern** | A recurring way of carrying out a group of a domain's responsibilities: how the work arrives, who carries it out, who judges it done, and when a person is involved. The factory pattern is one example; which patterns recur is an area of study. |
| **Grant** | Authority to carry out one action or task, issued on a positive Policy decision, limited in time and revocable. |
| **Harness** | The service that runs each agent's loop: it manages the context window, calls the model and carries out tool calls. A harness product usually bundles this service with others. |
| **Implementation** | A real system that fills in one part of WARM: a team's sprint process implements the main work of the Software domain; a harness and its tooling implement the platform. |
| **Infrastructure** | Where everything runs: machines, CI runners, storage, network. |
| **Instance** | A running copy of an agent. It can be restarted or moved; the agent is the identity, not the instance. |
| **Job** | Work that a schedule or an event starts. A script or an agent may carry it out. |
| **Persistent agent** | An agent that holds its roles across many sessions and tasks. The platform keeps its identity, session history and memory between tasks. |
| **Person** | Someone who directs or approves work. People also fill roles, request or receive results, and are subjects of the work. |
| **Pre-approval** | A person's authorization, given in advance, for a class of actions under stated conditions. It states its term (an end date or condition, or that it does not expire) and can be revoked. Approvals records it; Policy checks its conditions and issues the grant. |
| **Provider** | An outside source the platform calls and does not operate: a model vendor or an external service. |
| **Published skill** | The part of a domain's charter written for the agents of other domains: what the domain offers, when to use it, how to ask and what comes back. The Registry holds it and the Directory points to it. Loading it grants nothing. |
| **Responsibility** | What a part is accountable for. Each platform service has one. Each domain holds a set that belong together; at the size at which work is handed between domains, exactly one domain is accountable for each. |
| **Role** | A position with stated duties, filled by an agent or a person. A role that does a domain's work belongs to that domain. |
| **Service** | Something the platform provides to agents in any domain, which works the same whatever the work is about. Only the platform has services; a domain is an area of work. |
| **Subdomain** | A named group of a domain's responsibilities that has its own workflow, and may have its own roles, knowledge, tools and acceptance criteria. It keeps the domain's goals and rules, and the domain remains accountable. Not the subdomain of Domain-Driven Design. |
| **Session** | The history and state of one stretch of an agent's work. |
| **Skill** | A packaged set of instructions for a kind of task. A person may write it, and experience may revise it. The Registry holds its versions and Releases makes each change. |
| **Subagent** | A task agent started by another agent to do part of its task. |
| **Task** | One unit of work with a start, an end and a result. Also called a run. |
| **Task agent** | Also called a worker agent. An agent started for one task and ended with it, with no continuing role or memory of its own. The platform retains its records. |
| **Work product** | What a task produces: software, a report, a decision, a message. |

Relations: a person **directs** a domain, **approves** its charter, and **pre-approves** classes of action. A charter **defines** roles and **includes** an agent definition for each role an agent fills. An agent **fills** one or more roles. A domain **is accountable for** a set of responsibilities, and the Directory **records** them. A domain **offers** work to other domains through its published skill. An agent **hands** work to a role of the domain accountable for it. A persistent agent **starts** task agents. An agent **works on** tasks, in sessions. A task **produces** work products. Agents **run on** the platform and **use** its services. Within the platform, Runtime **uses** Capabilities and Knowledge, Interaction **connects** Runtime to other agents, people and applications, Governance **constrains** every group, and Operations **observes and changes** every group. The platform **runs on** infrastructure and **calls** providers. A real system **implements** a part of the model.

## What WARM adds, and its limits

Most agent platforms grow, and few are designed up front. A team starts with a harness (a model, a loop and some tools) and adds to it one problem at a time: memory, scheduled jobs, approvals, subagents, a second agent. Each addition solves a real problem, and the result is hard to describe, compare or change. The reference implementation grew this way, in part from the goals of the open-source project OpenClaw, which its author tried first. This is the history of one system and of the projects its author followed; a team can also start from a managed platform or a workflow engine.

What WARM contributes is the whole in one picture, for agent systems. The published models of agent systems have good parts: lists of platform services, a charter for one agent, registries of capabilities, careful accounts of authority and of pre-approval. WARM puts the platform, the domains of work and the agents in one model, with a directory that records which domain is accountable for what, and it has been set against three platforms and fourteen published models. Outside agent systems the shape is established: Data Mesh puts domains, a self-serve platform and federated governance in one model, and Team Topologies puts stream-aligned teams and platform teams in one.

WARM offers four things:

1. **An anatomy of an agent system and its platform.** Names for the parts (five layers, six groups, 25 services) and for what sits on the platform (domains and agents). It is a proposed vocabulary and not a proof that the list is complete.
2. **Organizing principles.** A responsibility belongs to the platform if it works the same whatever the work is about. An agent is an identified actor that fills roles, and a domain's roles belong to the domain. A domain holds a set of responsibilities that belong together, recorded in a directory. Design for agents to finish work end to end, and prefer a pre-approval to holding each action. Design for a system that improves itself continuously: a change to a role or a rule is an action that can be pre-approved. Governance and Operations apply across the other groups. One piece of guidance from experience: keep unattended work out of conversation sessions.
3. **A map for a harness that is growing.** A team can set what it has built against the list and ask what is missing and what is mixed. The three platforms mapped have grown most of the same parts, which is some evidence that the list describes where a growing harness tends to go. A system does not need every part, and a missing part may be deliberate.
4. **A starting place to build, assess and compare.** A checklist for building, a frame for comparing platforms service by service, and a candidate target for a refactor. A match of names does not make two services equivalent; a comparison has to record what each guarantees.

A survey of 34 sources on 2026-11-09 found no adopted, vendor-neutral reference model for an agent platform. Vendors decompose the platform into services and agree on a core (runtime, sessions, memory, tools, identity, observability, sandboxed execution). Software-factory products describe one way of working. The survey found no model of an agent system that puts domains of work in the same model as the platform. WARM joins them for agent systems.

The survey was a search for vocabulary and not a systematic review. A second reading on 2026-11-11 covered what it had left out: Domain-Driven Design applied to agents, Microsoft's multi-agent reference architecture, and further frameworks and papers from the AI community (`research/reports/2026-11-11-warm-prior-work-reading.md`). That reading, the documented search, the two rounds of comparison with fourteen published models, a check of how those models treat autonomy, and a reading of Domain-Driven Design, Team Topologies and Data Mesh qualify the claim in nine ways. The verdicts and their evidence for points 1 to 6 are in "Compared with published models".

1. **Vendor-neutral reference models have been proposed; none was found to be adopted.** Microsoft's Multi-Agent Reference Architecture calls its approaches "agnostic", and names Microsoft products. Yu, Rabhi, Zhu and Lu (arXiv:2610.14818, October 2026) present "a technology-neutral reference architecture" of ten responsibilities. Goujon (arXiv:2610.30221, October 2026) presents a "prescriptive reference model" in seven layers. The reading found no named adopter of any of them, and the two papers had no citations as of 2026-11-11. What is widely adopted is frameworks and guidance for building one agent application (AutoGen, the OpenAI Agents SDK, 12-factor agents), not reference models. So "no adopted model" holds as of this date. "No vendor-neutral model" would be false. A documented search on 2026-11-11 found 48 further sources that meet its rule for a general model of an agent system, and none of them has more than 51 citations. None of the fourteen models compared has a named adopter that the readers could find; the most-cited has 19 citations.
2. **Separating an area of work from the agents in it has partial precedents.** In Domain-Driven Design a bounded context is "A description of a boundary (typically a subsystem, or the work of a particular team) within which a particular model is defined and applicable" (Evans, Domain-Driven Design Reference, 2015). It bounds a model, and one way to set the boundary is by team. Dubrov, applying it to agents, paraphrases it as "a part of the system where business terms and rules have one agreed meaning" and writes that a bounded context "is not automatically a microservice, repository, agent, or team". Atlan gives a domain a named human owner, with agents assigned to it. Zhu (arXiv:2608.08516, August 2026) keeps a persistent specialization apart from the temporary workers that fill it. Zhu's resident entry is a dormant template that is activated to lead one task's team, so it is not a persistent agent in WARM's sense, and Zhu rejects long-lived agents by design. The frameworks read (Microsoft's architecture, OpenAI's guide, 12-factor agents) assign a domain to an agent or to a group of agents. AEON's subdomains and Charterion's business scopes are areas of work apart from agents, so "no model separates an area of work from its agents" would be false. No source read gives a domain a charter with roles that several agents and people fill, its own workflow and acceptance criteria. The nearest cases are AWS, which writes a domain's parts as a charter for each agent; Google's multi-tenant architecture, which gives a business unit its own agent, tools, rules and data; CEAD, which defines a business capability and its owner before the agent, inside one agent's contract; and Microsoft's Cloud Adoption Framework, which has teams write an "agent charter" for an agent system, with its responsibilities, agent roles that do not overlap and prohibited actions. The word "charter" and much of the idea are therefore not WARM's. A full reading of Goujon found no entity for an area of work. Outside agent systems, neither Team Topologies nor Data Mesh separates an area of work from the team that does it.
3. **No source read has a directory of which domain is accountable for which responsibility, and AEON comes nearest.** AEON's capability registry records, for each capability, the subdomain that provides it and the principals allowed to invoke it, and agents find one another through it. It records a provider, not who is accountable. Charterion's registers let one compute which agent covers a step and which person answers for the agent; they are not presented as a lookup for handing work over. Other near cases are optional owner tags in a registry of agents (Microsoft) and a matrix that assigns governance activities to governance roles (Goujon). EAAF has agents negotiate their responsibilities, the opposite of a directory that people set. Outside agent systems the near cases are the context map of Domain-Driven Design (a named record of every context and how they relate), the Team API of Team Topologies (for each team: its focus, the software it owns, the services it provides and how to contact it) and the Data Mesh catalog of data products and their owners. None of them records accountability for each responsibility.
4. **An agent as an identified actor is not new, and WARM withdraws that claim.** Charterion defines an agent as "a non-human principal" with an identity that "may be instantiated many times", and credits the idea to security and standards guidance published since 2025, from the Cloud Security Alliance, NIST and OWASP among others. AOS separates "a persistent agent identity" from "a transient runtime instance". What remains different is narrow. In Charterion every running instance of an agent, a subagent included, acts under the one identity of the chartered agent; WARM gives each task agent an identity of its own.
5. **The split between persistent and task agents has partial precedents.** Charterion has one kind of agent, long-lived, whose running instances share its identity; Salesforce has only agents started for one task; EAAF's "Task Agents" are a type of job and not a lifetime, and Zhu rejects long-lived agents. The claim that none separates the two kinds by lifetime as WARM does stands, narrowed.
6. **Artifacts has no full counterpart in any system mapped.** None of the three platforms and none of the published models whose scope could include one has a full counterpart to a versioned store of work products, and Steinder and Franke argue that a file system is enough: "POSIX file systems still store agent-produced artifacts". The owner decided on 2026-11-11 to keep Artifacts and to state the gap.
7. **Pre-approval and autonomy do not set WARM apart.** Six of the fourteen models state pre-approval in full and six in part, and Charterion and AAM/5C state it more completely than WARM (`prior-work/autonomy-check.md`; one reader). Several of the fourteen treat autonomy as a goal, and two say it is not one. WARM's emphasis on agents finishing work end to end is its owner's design aim, stated as scope. It is not a claim to be distinct.
8. **The published skill, the domain pattern and the subdomain are proposals with thin support.** The published skill has precedents outside agent systems (the Team API, the data product) and no implementation in the reference system. The domain pattern rests on an inventory of one system, in which the factory pattern occurs once. The subdomain rests on one decided case in the same system.
9. **Defining an area of work and its roles apart from the agents that fill them is established in the organizational multi-agent literature of 2002 to 2004.** The documented search admitted only work on LLM agents from 2023 onward and missed it; a reviewer of the paper's first draft named it on 2026-11-12. Gaia (Zambonelli, Jennings and Wooldridge, 2003) and OperA (Dignum, Dignum and Meyer, 2004) specify an organization, its roles and their responsibilities and permissions before any agent is assigned; AGR (Ferber, Gutknecht and Michel, 2003) and MOISE+ (Hübner, Sichman and Boissier, 2002) do so in part or in full, depending on the reading; OperA and a survey (Horling and Lesser, 2004) also describe facilitation roles such as a matchmaker that routes requests (`prior-work/organizational-mas.md`; one reader). WARM's domain layer therefore restates an older idea for agents built on language models. An independent rating of the seventeen sources under four frozen criteria (`prior-work/rerate-criteria.md`, `prior-work/rerate-four-columns.md`) found two with an area of work as a defined part (Charterion, AEON), and, under the stricter reading of the disputed cells, none that fully specifies it apart from who does the work and none with a full record of accountability; twenty of the 68 cells are disputable, and on the other defensible reading two sources would meet the first and three the second. Across all 27 sources read, none received an undisputed full rating for a record that names one accountable area for each responsibility. Two readers rated the two groups of sources and did not apply the criteria identically, so the difference between the older and the recent sources is not yet a finding about the literature (`paper/astra-review-d3.md`). Four web searches found no recent model of an LLM-agent system that builds on the older literature; a citation search was not run.

Not read: AWS's guides on security and on a semantic layer, most of its serverless and multi-tenant guides, and its Well-Architected Agentic AI Lens; one AWS guide (an enterprise multi-account architecture) that could not be opened; most of one Google page (private networking patterns) and two Google pages outside agent architecture; one Microsoft page that is empty. Forty of the 48 sources the documented search newly found have not been mapped, and eight more could not be opened, among them the Cloud Security Alliance's reference architecture. Of the eight mapped, Salesforce's page was read as text with two of its seven figures, and ASOC's layer contents exist only as figure labels. The books on Domain-Driven Design (Evans, 2003; Vernon, 2013), Team Topologies (Skelton and Pais, 2019) and Data Mesh (Dehghani, 2022) were not read; the reading used Evans's 2015 Reference, the Team Topologies site and two articles by Dehghani. "Agentic Mesh" (Broda and Broda, 2026) could not be opened. Failing to find a model does not show that none exists.

Limits, stated as plainly as the author can:

1. **Source.** WARM is built from published work (an industry survey, a documented search and a comparison with fourteen published models), one implementation, and a mapping to three platforms. The survey supplies vocabulary and no proof of completeness, and some of its quotes were not re-checked against the primary page. The implementation is a small company's system, on one harness product, with one owner who is also its operator.
2. **Domains.** That implementation has seven areas of work configured (software, finance, health, communications, research, marketing and customer support). The author mapped their declared roles, tools and rules. The author did not check in the code which service carries each part, and did not measure whether any service is reused unchanged across domains. The maps contain unresolved placements. The seven are the domains the owner needed, each built as far as was useful, so other kinds of domain, and deeper ones, may not fit. The domain pattern and the published skill come from this one system: the inventory behind the pattern had one reader, and no domain has a published skill yet.
3. **Platforms.** WARM has been mapped to three platforms from their documentation, by the author's team, with one mapper per platform and a second rater on a sample of 36 assignments. The comparison with fourteen published models had one reader per group of sources and a second rater on a sample of 126 assignments, and forty of the sources the search newly found are unmapped. No one outside has mapped a system to it, and no running system other than the reference implementation has been inspected.
4. **Contracts.** WARM names responsibilities and some relations. It does not state what each service must guarantee (on failure, cancellation, delegation, stale state) or how to tell that a system conforms. Implementations define concrete interfaces. Later papers on each group are intended to propose contracts; whether any becomes part of the model is open.
5. **Evidence.** There is no evidence yet that organizing a system this way improves it. The refactoring of the reference implementation is the first test, and its measures have to be set before it starts.
6. **Pre-approval.** The three kinds of human decision and the two rules on pre-approval come from the owner's experience of one system and from his decisions of 2026-11-11. The reference implementation uses pre-approvals; it has not been checked that each one states its term.

Two further cautions: the platform test is a design choice that cannot be refuted, and the two kinds of group describe scope and do not sort every service.

## Changes from v0.12

Sources: the owner's decisions of 2026-11-11, recorded in `v0.13-spec.md` (quotations are his); `simplicity-pass-plan.md` (the map of where each v0.12 passage went); `prior-work/autonomy-check.md`; `prior-work/ddd-teamtopologies-datamesh.md` (F numbers are its section F); `domain-pattern-inventory.md`; the review of the talk, `deck/review-core-merged-v0.12.md`.

| Change | Source |
|---|---|
| The document is a core and an appendix. The core is Steps 0 to 5 at about half of v0.12's length. The appendix holds Notes, Contract questions and Evidence. v0.12's statements are moved and not deleted, except where this table says one changed | "i like having the core and the appendix"; "stay simple and understandable but keep the correctness and comprehensive coverage" |
| The scope sentence and the aim: WARM is written for systems in which agents finish work end to end. A principle is added: prefer a pre-approval to holding each action. The model is not renamed | "highly emphasize autonomy" |
| Continuous self-improvement is stated in Step 0 as the second aim and listed among the organizing principles | The owner, 2026-11-12 06:12: "we are building a continous self improving system so we have to have this type of appraoch"; "that is a core principle" |
| The three kinds of human decision are restated for a class of action: reserved for people, pre-approved under conditions, held for a person. The granting of authority is now a principle (all authority traces to a person), and a change to a role or a rule is an action of one of the three kinds. The Approvals service obtains and records both pre-approvals and decisions on held actions | The owner, 2026-11-11 19:54 (pre-approval as a kind); 2026-11-12 06:11 (the principle, after the mapping of the reference implementation found agents editing their own definitions under a standing permission): "we need to stay nimble and agile and pragmatic"; "we are building a continous self improving system so we have to have this type of appraoch" |
| A pre-approval states its term and can be revoked | "a preapproval should expire or, if not, explicitly not expire" |
| A pre-approval covers an action that cannot be undone only if it says so explicitly and names the kind of action. That is the model's one requirement; whether to allow it and what more to require are options for an implementation, listed in the notes with the reference implementation's choice | "irrevisible options can be preapproved. we may need extra clear approval (type DELETE) and we may want to take some insulating action where possible ... (like put into a trash folder rather than deleting)"; 2026-11-12: "we need to think about what is at the reference model level and what options an reference implementation has" |
| Charterion and AAM/5C are credited for pre-approval; the sources' disagreement on actions that cannot be undone is stated; WARM defines no levels of autonomy, and the six models that do are named | `prior-work/autonomy-check.md` |
| A domain is redefined: an area of work with a body of specialized knowledge, a set of responsibilities that belong together, and one or more patterns for carrying them out. "Domain" is said to have its organizational sense | The owner chose this wording |
| The charter table has nine rows: Responsibilities and Published skill are added to the seven. The owner confirmed it on 2026-11-12 | Follows from "Its charter writes these down" |
| The published skill: each domain states what it offers other domains, when to use it, how to ask and what comes back; the Registry holds it and the Directory points to it; loading it grants nothing | "i wonder if a domain ends up being a skill for other domains. so they know when and how to use it"; "i lean towards a domain publishing a skill" |
| The domain pattern is added as a term, with the factory pattern as one worked example and the catalog stated as open work. It is distinguished from an orchestration pattern | The owner chose "domain pattern"; `domain-pattern-inventory.md` |
| The domain is Software. "Software Factory" is no longer a domain name; factory is a domain pattern, and the reference implementation's process is an implementation. The example is rewritten as domain, pattern, implementation | The owner, 2026-11-11 |
| The reference implementation's products are each named once in the core, as implementations | "tread lightly with lifeos and agent scrum in this paper ... not a product. and definitely not a product pitch" |
| One definition can serve a persistent agent and a task agent; they are two agents with one role | The owner, 2026-11-11 22:26; confirmed 2026-11-12 |
| A note maps a terminal multiplexer and remote access to the model, as an example of a component that spans parts | The owner's question, 2026-11-11 22:26 |
| Wording: a domain does not "run", "supply" or "write". The work of a domain runs on the platform; a charter states or includes; people and agents act | `deck/review-core-merged-v0.12.md` (the independent reviewer) |
| "Grain" is "size", and "a cohesive set" is "a set that belong together" | Same review |
| "Contract" has one meaning, the guarantees a service states. Tasks "names a responsibility and does not require its own store" replaces "Tasks is a contract" | Same review |
| The Secrets and Policy rows are one sentence each; their detail is in the notes on Step 3. Evaluation's row loses "before, during or after an action", which is in the notes | `simplicity-pass-plan.md` |
| Four of the seven points of "How the groups relate" leave the core: the stop path, grant detail and the enforcement-point check go to Contract questions; points 5 to 7 go to Notes. The enforcement point, the grant and separation of duties stay, one or two sentences each | `simplicity-pass-plan.md` |
| The platform test cites Data Mesh (2019) and Domain-Driven Design's generic subdomains as nearer precedents than the Hydra paper, which is kept | F1, F2 |
| The sentence on bounded contexts is removed from Step 4. Evans's definition is quoted, and the earlier paraphrase is attributed to Dubrov | F3, F4 |
| "No source puts domains of work in the same model as the platform" is narrowed to models of agent systems; Data Mesh and Team Topologies are cited as the general precedent | F5, F6 |
| The context map, the Team API and the Data Mesh catalog are added as near cases for the Directory | F7 |
| Notes cite the typologies of how areas relate, the platform reached through a defined interface, single accountability, rules applied by the platform, governance across domains and replaceable implementations; a note says that "domain" and "service" have other meanings elsewhere | F8 to F14 |
| A shared kernel is not adopted; cognitive load is cited as sizing guidance | The owner, 2026-11-11 22:05 |
| Two points are added to "What WARM adds, and its limits" (pre-approval and autonomy are not WARM's; the published skill and the domain pattern have thin support), and one limit (pre-approval) | `prior-work/autonomy-check.md`; the inventory |
| Charterion is recorded as read in full; no verdict changed | `prior-work/charterion-full.md` |
| After an independent review of this draft (`review-v0.13-astra.md`, 15 findings, all applied): accountability is stated for a domain's tasks; a held action is one the rules allow; "skill" and "enforcement point" are defined at first use; the grant's time limit moved to the contract questions; the six graded schemes are no longer all called levels of autonomy; two claims about Domain-Driven Design and about the search were narrowed; the two older change tables are replaced by a pointer | `review-v0.13-astra.md` |
| The inventory's count of groups that fit no recurring shape is 18 of 45, not the 20 recorded in the working notes | `domain-pattern-inventory.md`, section B |
| The subdomain is added to Step 4, the glossary, the notes on Step 4 and the limits: a named group of a domain's responsibilities with its own workflow; the domain remains accountable; a subdomain is internal to its domain and does not appear in the Directory (the owner, 07:59) | The owner, 2026-11-12 07:26 and 07:57; product operations placed inside Software, 2026-11-12 07:20 |
| The opening says that the model was made in the reference implementation, by its Research and Software domains | The owner, 2026-11-12 07:57 |
| A ninth qualification is added to "What WARM adds, and its limits": the organizational multi-agent literature of 2002 to 2004 already defines an area of work and its roles apart from agents; the four contribution-bearing columns were re-rated independently under frozen criteria | `paper/astra-review-d1.md`; `prior-work/organizational-mas.md`; `prior-work/rerate-four-columns.md` |

## Earlier changes

The changes from v0.11 to v0.12 and from v0.10 to v0.11 are in `warm-model-v0.12.md`. Those tables use the names of their time: "Software Factory" for the Software domain, and "Tasks is a contract" for the statement that Tasks does not require its own store.
