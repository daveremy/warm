---
title: "Protocol for mapping vendor products to the WARM platform services (version 1)"
date: 2026-11-12
author: sagan
status: frozen at 12:58 before any reader started; do not edit after a reader has started. A change is a new file.
---

# Purpose

Record, for one vendor product, which of 25 platform services the product itself supplies today, from the vendor's own current pages. Nine products are mapped, each by one reader: four harnesses on which a builder assembles a system (Claude Code, Codex CLI, Grok Build, Google Antigravity) and five finished personal agents (Claude Duet, OpenAI Dots, xAI Grok Bot, Google Gemini Spark, Meta Muse). A second reader later re-rates a sample.

# Sources

- These products change every few weeks. Do not rate from what you remember. Every value rests on a page you opened today.
- A cell cites the vendor's own material: documentation, changelog or release notes, help center, official blog or launch post, the product's public repository, or (for a product installed on this machine) its own help output.
- News coverage, reviews and third-party guides may be used only to find vendor pages. A cell that rests on such a source alone is marked "secondary only" and rates **part** at most.
- Record the date you read each page, and the product version or the date of the newest changelog entry you saw.

# Values

Each service gets **yes**, **part**, **no** or **not assessed**, with one exact quote and its URL (or, for **no**, what you searched and did not find).

- **yes**: the vendor's pages describe a feature of the product that carries out the responsibility in the service's definition, and a user of the product can use it today (say whether it is generally available, beta or preview).
- **part**: the product covers some of the definition; or it supplies only a mechanism on which the user must still build the responsibility (an extension point, a hook, a plugin interface); or the feature is announced and not available; or the evidence is secondary only.
- **no**: not found in the vendor pages you searched.
- **not assessed**: the product is closed or its pages do not let you decide.

When two values are both defensible, give the lower and mark the cell DISPUTABLE with the other value and the reason. Decide from what the pages state. Do not infer what the product "probably" does.

# The 25 services

| Group | Service | Responsibility |
|---|---|---|
| Runtime | Harness | Run the agent loop: decide what goes into the context window, send it to the model, and carry out the tool calls the model asks for. |
| Runtime | Sessions | Keep the history and state of a stretch of an agent's work, so that the agent can pause, resume and hand off, and so that the record remains after the work ends. |
| Runtime | Tasks | Track each unit of work from start to finish, coordinate its retry, recovery and cancellation, and keep the original request. |
| Runtime | Environments | Give each agent a place to act, isolated from the others: sandboxes, workspaces, browsers. |
| Runtime | Scheduling | Decide when work starts: at a time, on an event, and within the limits on how much may run at once. |
| Runtime | Lifecycle | Create, suspend, resume and end agents, and keep the list of which agents exist. |
| Knowledge | Memory | Retain what agents learn across sessions (facts and events), with where each entry came from, and keep it current. |
| Knowledge | Retrieval | Fetch material from named sources: documents, data, notes. |
| Knowledge | Artifacts | Store what agents produce (reports, files, pages) and its versions. |
| Capabilities | Models | Mediate requests to models and choose the model for each task, across more than one model or vendor. |
| Capabilities | Tools | Mediate calls to tools, local or external. |
| Capabilities | Registry | Hold the versioned definitions of agents, tools and skills, so that each can be found and loaded when a task needs it. |
| Interaction | Directory | Record which domain is accountable for each responsibility, and how to reach a role of that domain. |
| Interaction | Messaging | Deliver messages between agents, and events to their subscribers. |
| Interaction | Orchestration | Coordinate assignments among agents, people and fixed steps: who does what, what depends on what, and the results that come back. |
| Interaction | Channels | Carry requests and results between agents and the people and applications that use them, on the channel each one uses. |
| Governance | Identity | Establish who is acting (each agent, person and service, and on whose behalf), record the person accountable for each agent identity, and revoke an identity. |
| Governance | Secrets | Hold values that agents must not see, and release each one only at the point of use. |
| Governance | Policy | Decide by rule whether an action may proceed, what content may enter and leave, and what stored data is kept; issue a grant when an action is allowed. |
| Governance | Approvals | Obtain and record people's authorizations: approvals given in advance for a class of actions under stated conditions, and decisions on single actions that are held. |
| Operations | Observability | Collect evidence of what agents and the platform did. |
| Operations | Evaluation | Assess behavior and work products against stated criteria, and report "unknown" when a check could not run. |
| Operations | Improvement | Turn evidence (traces, evaluations, reviews) into proposed changes to agents, skills and the platform. |
| Operations | Releases | Version and release changes to agents, skills, rules, the platform and the infrastructure the system manages, with a way back. |
| Operations | Reliability | Keep services available and restore them after a failure. |

A domain, in this model, is an area of work (for example finance, communications or software) with a written statement of what it is responsible for and the roles that agents or people fill.

# Four further questions, answered after the table

1. **Areas of work.** Rate the product on C1 to C4 of `prior-work/rerate-criteria-v2.md` (read that file; apply it as written), with a quote for each value.
2. **Supplied agents for an area of work.** Does the vendor supply ready-made agents, roles or skills for a named area of work? List each with a quote and URL, or write "none found" and what you searched.
3. **What fits nowhere.** List features of the product that carry a responsibility none of the 25 services covers, each with a quote and URL, or write "none found".
4. **Where it runs and what the user supplies.** State, with quotes: where the agent runs (the user's machine, the vendor's cloud, both), whether an agent keeps running when the user is away, and what a user must supply or build to use the product for sustained work.

# Output

One file, `prior-work/vendors/<product>.md`: YAML frontmatter (title, date, author, product, product version or newest changelog date seen, status "not yet checked by sagan"); the 25-row table (service, value, quote, URL, availability); the four further answers; a list of every page opened with the date; disclosures and anything that could not be opened. American English spelling outside quotations.
