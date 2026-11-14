---
title: "Criteria for re-rating the boundary cases, version 2 (clarified)"
date: 2026-11-12
author: sagan
status: frozen at 12:25 before either reader started; do not edit after a reader has started. A change is a new file.
supersedes: "rerate-criteria.md for the sources listed in rerate-v2-sources.md only"
---

# Why a second version

Two readers applied version 1 to different groups of sources and did not read three points the same way: whether a unit that is the whole system counts as an area of work, whether a requirement or an example counts as a lookup, and whether a lookup made through an intermediary counts. Version 2 keeps the four criteria and their three values and adds a ruling on each point. Both readers rate every listed source on all four criteria.

# Rules for both readers

Each source gets one value for each of four criteria: **yes**, **part**, **no**, or **not assessed** (the material read does not let the rater decide). Every value needs one quoted passage from the source with its location (or, for **no**, a statement of what was searched and not found). A rater decides from what the source states. A rater does not infer what a source "probably" has. When two values are both defensible, the rater gives the lower one and marks the cell DISPUTABLE with the other value and the reason.

Rate what the source defines as part of its model, method, specification or architecture. An element that appears only in a worked example and is not defined in the model rates **part** at most. A stated requirement or goal with no described mechanism, record or element rates **part** at most. For a survey, rate the paradigm or element the survey itself describes, and say so.

## C1. An area of work exists in the model
The source's model has a named unit that stands for an area of work or an organizational unit (for example a domain, department, business unit, subdomain, group, organization or capability area), and the unit is distinct from a single agent.
- **yes**: the unit is a defined element of the model (it has a definition or stated properties), more than one agent or role can belong to it, and the model allows a system to contain more than one such unit (several units side by side, or units inside a larger unit).
- **part**: such units are mentioned or used, but the unit is not defined; or the unit is the same thing as one agent or one team of agents built for one task; or the only defined unit is the whole system (one organization, society, institution or governing body) and the model defines no way to have several.
- **no**: no such unit.

Ruling added in version 2: the criterion asks whether the model can divide a system's work into more than one area. A unit that models an activity or a conversation (for example a meeting, a protocol run or a task) is not an area of work.

## C2. The area is specified apart from who does the work
Rate the unit found under C1 (if C1 is **part** because the only unit is the whole system, rate that unit).
- **yes**: the source specifies, at the level of the unit and not per agent, at least (a) what the unit is responsible for and (b) roles or positions that agents or people fill.
- **part**: the source specifies some properties at the level of the unit (an owner, a scope, capabilities, rules) but not both (a) and (b); or it specifies responsibilities and roles per agent (an agent charter or contract) and not per unit.
- **no**: neither.

Ruling added in version 2: for (a), the source must state what the unit as a whole is for or must achieve (objectives, goals, a mission, a scope of work). Responsibilities stated only for each role do not meet (a). For (b), the roles must be defined independently of the agents that fill them.

## C3. A record of accountability
- **yes**: the source describes a record (registry, table, map, catalog) in which each responsibility or capability has one named accountable area or owner.
- **part**: a record names an owner, a provider or a responsible party per agent, asset or capability, but accountability is not stated, not unique, or not per responsibility or capability.
- **no**: no such record.

Ruling added in version 2: a record is a kept set of entries, either a named artifact of the method or state held by the running system. Rules or norms alone are not a record. "One named" means exactly one; a record that allows a list of responsible parties for one entry rates **part**. A record of commitments or obligations that agents take on while the system runs counts as a record and rates **part** unless it also meets the wording of **yes**.

## C4. Finding where to send work
- **yes**: at run time an agent can look up, from a kind of work or a capability, the agent or role that handles it and how to reach it.
- **part**: agents can discover other agents (a list, agent cards, a registry with endpoints), but the lookup is not from a kind of work; or routing exists only inside one orchestrator's own logic or prompt.
- **no**: neither.

Ruling added in version 2: a lookup made through an intermediary (a directory, facilitator, matchmaker, broker or registry service) rates **yes** when the source defines the intermediary as an element of the model, any agent may ask it, and it answers from registered capabilities or kinds of work, whether it returns the handler or forwards the request to it. An intermediary that is the system's single orchestrator and resolves handlers only for its own plans rates **part**.

## Derived, not rated
Directory (the service) = **yes** if C3 and C4 are both yes; **part** if either is yes or part; **no** if both are no.
