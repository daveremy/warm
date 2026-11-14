---
title: "Organizational models of multi-agent systems, and five recent sources, read against the WARM description"
date: 2026-11-12
author: "sagan (subagent)"
status: "not yet checked by sagan"
---

# Organizational models of multi-agent systems: what each source states

Scope: sources A to H from the brief, plus two additions from the older literature (OperA, and the Horling and Lesser survey). All sources were read on 2026-11-12. Quotations are exact except for line breaks and hyphenation from PDF text extraction. Page numbers are the source's printed page numbers where the extracted text carries them; otherwise they are PDF page numbers and are labeled "PDF p.". Ratings apply C1 to C4 from `prior-work/rerate-criteria.md` as written. Other than that file, the only file read under `papers/warm/` was `prior-work/search.md`, for the URLs of E and F; while extracting those two rows, a grep also printed three summary lines of search.md that mention E and F, and these ratings do not use them.

The WARM description used for item 4 is the one in the brief: people direct the work; domains are areas of work, each defined by a written charter (goals, responsibilities, roles filled by agents and people, workflow, knowledge, tools, rules, acceptance criteria, and what the domain offers other domains); agents are identified actors that fill roles; a shared platform serves agents in every domain; a directory records which domain is accountable for each responsibility and how to reach it.

---

## A. AGR (Agent/Group/Role)

**1. Citation and reading.** Jacques Ferber, Olivier Gutknecht, Fabien Michel. "From Agents to Organizations: An Organizational View of Multi-agent Systems." In P. Giorgini, J.P. Müller, J. Odell (eds.), *Agent-Oriented Software Engineering IV (AOSE 2003)*, LNCS 2935, pp. 214-230, Springer, 2004. Copy read: https://www.lirmm.fr/~fmichel/publi/pdfs/ferber04ocmas.pdf (the author copy with the Springer page header). Read: the whole paper, pp. 214-230, including references. Date read: 2026-11-12.

**2. What the source states.**
- *Organizational unit: the group.* "Group: a group is a set of agents sharing some common characteristic. A group is used as a context for a pattern of activities, and is used for partitioning organizations." (p. 220). Groups are instances of a *group structure*: "A role structure is defined, for each group, by a set of roles and their relationships." (p. 218). The paper names department as one kind of partition: organizations "are structured as aggregates of several partitions which may overlap, sometimes called groups or communities, contexts, department, services, etc." (p. 217). Groups are boundaries: "Whereas the structure of a group A may be known by all agents belonging to A, it is hidden to all agents that do not belong to A." (p. 219).
- *Role, and where it belongs.* Roles belong to the group, not to the agent: "Role: the role is the abstract representation of a functional position of an agent in a group. [...] Roles are local to groups, and a role must be requested by an agent." (p. 220). Axiom e: "A role is defined in a group structure" (p. 221). Role content: "A role describes the constraints (obligations, requirements, skills) that an agent will have to satisfy to obtain a role, the benefits (abilities, authorization, profits) that an agent will receive in playing that role, and the responsibilities associated to that role." (p. 218).
- *Occupants.* "A role may be played by several agents." "An agent may hold multiple roles, and may be member of several groups." (p. 220). Agents may be of any kind, including people: "an agent may be as reactive as an ant, or as clever as a human." (p. 220). The paper's example has people-like roles (program chair, PC member, author, reviewer; pp. 226-227) but does not say whether the occupants are humans or programs.
- *Responsibilities.* Attached to roles (quotation above, p. 218). No separate assignment mechanism is described. Roles "may be described as in Gaïa [15] by attributes such as its cardinality" (p. 221), and the methodology says "one could use the Gaia [15] methodology to fill the roles" (p. 226).
- *Workflow.* Interactions are protocols between roles: "Interaction diagrams [...] are used to describe communication protocols between roles." (p. 223). Organizational dynamics (creating groups, entering, taking roles) are drawn as "organizational sequence diagram[s]" (p. 223). The conference example names protocols such as "distribute papers to review" and "notification of acceptance" (p. 227).
- *Authority, permissions, norms.* Two structural constraints between roles: correspondence and dependence, e.g. "Role('director','Lab') requires Role('researcher','Lab')" (p. 221). Entry to a group requires authorization through a gatekeeper pattern: "We will assume that an agent is permitted to enter a group only if it provides the right authorization." (p. 224). Norms are deferred: "describing norms (obligations, permissions, interdictions) that are related to groups and roles (this latter feature will be presented in a forthcoming paper)" (p. 229); "functional views, deontic aspects (concepts of norms and institutions) [...] have been left over" (p. 229).
- *Communication rule.* Axiom b: "Two agents may communicate only if they are members of the same group" (p. 220). Principle 1: "The organizational level describes the 'what' and not the 'how'." (p. 219).
- *Shared platform.* No service layer is part of the model. The paper names the MadKit platform as an implementation: "The MadKit platform [8] that we have designed is built around the AGR model." (p. 229).
- *Registry or directory.* None in the model. The FIPA Directory Facilitator appears only as an example of a role: "the FIPA agents called the Directory Facilitator (DF) and the Message Transport Service (MTS) would be represented as agents playing the DF and MTS roles respectively." (p. 225). The paper criticizes the FIPA assumption that "An agent provides a set of services, which are available to every other agent in the system." (p. 215).
- *How one unit asks another for work.* Through agents that belong to both groups. A correspondence constraint lets "delegates of smaller groups [...] automatically [be] members of another group where they act as representative" (p. 221); hierarchies of groups are represented by "some 'delegate' agents in one group [...] seen as 'representative' agents in another group" (p. 226).

**3. Ratings.**
| Criterion | Value | Quotation or search |
|---|---|---|
| C1 | yes | "a group is a set of agents sharing some common characteristic. A group is used as a context for a pattern of activities, and is used for partitioning organizations." (p. 220) |
| C2 | part, DISPUTABLE (yes) | Roles are specified per group structure ("A role structure is defined, for each group, by a set of roles", p. 218), but responsibilities are stated per role ("the responsibilities associated to that role", p. 218), not per group. Yes is defensible because every role, with its responsibilities, is defined inside a group structure. |
| C3 | no | Searched the whole text for a registry, table or map of responsibilities to owners. None. The DF is mentioned only as a role in an example (p. 225). |
| C4 | no | Searched for lookup or discovery. None in the model; communication is limited to members of the same group (axiom b, p. 220). |

**4. Comparison with the WARM description.**
- AGR has and the description lacks: a formal axiom set (membership, communication only within a shared group, roles defined in group structures); group boundaries that hide a group's structure from non-members; role constraints (correspondence, dependence); an explicit split between organizational structure and concrete organization (p. 218); group entry through an entrance group and gatekeeper (p. 224).
- The description has and AGR lacks: a written charter per unit with goals, workflow, knowledge, tools, acceptance criteria and an offer to other units; a shared platform as part of the model; a directory of accountability and reachability; people directing the work. AGR's group has no stated goal or responsibility of its own.

**5. LLM agents?** No (2003). The agent is "an active, communicating entity playing roles within groups" with "no constraints [...] placed upon the architecture of an agent or about its mental capabilities" (p. 220). Principle 2 forbids agent descriptions at the organizational level: "Thus, reactive agents as well as intentional agents may act in an organization." (p. 219). The organizational model does not depend on the kind of agent; that independence is a stated design principle.

---

## B. Gaia (extended version)

**1. Citation and reading.** Franco Zambonelli, Nicholas R. Jennings, Michael Wooldridge. "Developing Multiagent Systems: The Gaia Methodology." *ACM Transactions on Software Engineering and Methodology* 12(3):317-370, July 2003. Copy read: https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/tosem2003.pdf. Read: sections 1-4 in full (pp. 317-364), section 5.1-5.2 (pp. 364-367), section 6 (pp. 367-368). Not read closely: section 3.2 (example applications) and the parts of 4.2.1-4.2.2 on organizational efficiency and patterns. Figures 9 and 10 (the role schema template and the REVIEWER schema) did not survive text extraction, so the role schema fields below come from the prose only. Date read: 2026-11-12.

**2. What the source states.**
- *Organizational unit: the organization and suborganization.* "as soon as the complexity increases, modularity and encapsulation principles suggest dividing the system into different suborganizations [...], with a subset of the agents being possibly involved in multiple organizations." (p. 325). Criteria for finding them: "such suborganizations can be found when there are portions of the overall system that (i) exhibit a behavior specifically oriented towards the achievement of a given subgoal, (ii) interact loosely with other portions of the system, or (iii) require competences that are not needed in other parts of the system." (p. 338). Example: "the organization responsible for the review process. This is in charge of assigning submitted papers to reviewers, of collecting and ranking the reviews, and defining the technical programme." (p. 338). Analysis produces models "for each of the (suborganizations) composing the overall system." (p. 338).
- *Role, and where it belongs.* "The role of an agent defines what it is expected to do in the organization [...]. our notion of a role is much more precise; it gives an agent a well-defined position in the organization, with an associated set of expected behaviors" (p. 329). Roles are specified before agents: "the notion of roles, at this stage, is abstract from any mapping into agents." (p. 335). A role has two attribute classes, "(i) permissions and (ii) responsibilities." (p. 342). "A roles model is comprised of a set of role schema, one for each role in the system." (p. 346).
- *Occupants.* An agent "is an active software entity playing a set of agent roles" (p. 361); "a designer can choose to package a number of closely related and strongly interacting roles in the same agent class" (p. 361); class cardinality annotations allow "no less than m and no more than n instances" (p. 361). On people: "Depending on the actual organizational structures, different actors (e.g., the PC Chair, the PC Members or external reviewers) will be called to play such roles." (p. 342). "any member of an organization, whether a human being, a hardware component, or a software agent, exhibits bounded rationality" (p. 352). Humans in the environment are to be modeled as agents: components such as "humans in-the-loop [...] should not be treated as part of the environment but, instead, they should be agentified." (p. 341).
- *Responsibilities.* Per role, as liveness and safety properties: "Responsibilities. These attributes determine the expected behavior of a role and, as such, are perhaps the key attribute associated with a role." (p. 344). Liveness is written as a regular-expression "life-cycle" of activities and protocols (pp. 344-345); safety as invariants (p. 346). At the level of the organization: "organizational rules are considered as responsibilities of the organization as a whole." (p. 349).
- *Workflow.* Liveness expressions per role (p. 344) and an interaction model with "one protocol definition for each type of inter role interaction" (p. 346). A protocol definition has "Protocol Name", "Initiator", "Partner", "Inputs", "Outputs", "Description" (p. 347). A services model gives each service "inputs, outputs, preconditions and postconditions" (pp. 362-363).
- *Authority, permissions, norms.* Permissions per role say "what can be spent while carrying out the role" and "what can't be spent" (p. 342). Organizational rules are global constraints, e.g. "an agent should be prevented from playing both the role of author and reviewer of the same paper" (p. 331), written in the same formalism (p. 349). Organizational structure states relations between roles, e.g. "a control relationship may identify an authority relationship of one role over another" (p. 357); example "PC CHAIR control→ REVIEWCATCHER[i]" (p. 358).
- *Shared infrastructure.* The environment is a first-class abstraction separate from the organization: "identifying and modeling the environment involves determining all the entities and resources that the MAS can exploit, control or consume" (p. 328). The environmental model is "a list of resources; each associated with a symbolic name, characterized by the type of actions that the agents can perform on it" (p. 339). It is a resource model, not a set of services.
- *Registry or directory.* None in the methodology. Directories appear only in a general remark that components "interact in more flexible ways (e.g., by making use of external directory, lookup, and security services)" (p. 323). The agent model is a design-time table: "a simple diagram (or table) specifying, for each agent class, which roles will map to it." (p. 361).
- *How one unit asks another for work.* Interactions between organizations are described only in general terms ("the interactions between organizations are loose and scheduled at specific intervals of time", pp. 338-339), and in the pipeline example a role may be added "to coordinate with the electric plant (better, the agent organization of the electric plant)" (p. 342). No inter-organization request mechanism is specified.
- *Use by outside parties.* "assuming that the developers of the existing MAS have made all the Gaia models publicly available, an agent developer will be able to check whether their agent can enter the system and, if so, what rules and procedures it needs to conform to." (p. 364).

**3. Ratings.**
| Criterion | Value | Quotation or search |
|---|---|---|
| C1 | yes | "such suborganizations can be found when there are portions of the overall system that (i) exhibit a behavior specifically oriented towards the achievement of a given subgoal, (ii) interact loosely [...], or (iii) require competences that are not needed in other parts of the system." (p. 338) |
| C2 | yes | Per suborganization, analysis yields "an environmental model, preliminary role and interaction models, and a set of organizational rules" (p. 338); the organization has goals ("the organization responsible for the review process. This is in charge of assigning submitted papers to reviewers [...]", p. 338) and roles "abstract from any mapping into agents" (p. 335). |
| C3 | no, DISPUTABLE (part) | No registry of accountability. Part is defensible because the agent model is "a simple diagram (or table) specifying, for each agent class, which roles will map to it" (p. 361), a design-time record per agent class, without accountability per responsibility. |
| C4 | no | Searched for lookup, discovery, directory. Only the general remark about "external directory, lookup, and security services" (p. 323); protocols fix initiator and partner roles at design time (p. 347). |

**4. Comparison with the WARM description.**
- Gaia has and the description lacks: a stepwise method (analysis, architectural design, detailed design); explicit criteria for splitting a system into suborganizations (p. 338); formal role responsibilities as liveness and safety properties; organizational rules as constraints on the whole organization; an explicit choice of organizational structure (topology and control regime) as a design decision separate from the roles; an environment model of resources with per-role permissions.
- The description has and Gaia lacks: a named charter per area that also lists knowledge, tools, acceptance criteria and an offer to other areas; a shared platform of services; a run-time directory of accountability; people directing the work (Gaia's humans are either role occupants or "agentified" environment components).

**5. LLM agents?** No (2003). Agents are software entities with autonomy, situatedness and proactivity (p. 320); "the real advantages of agent-based computing" do not require "AI techniques" (p. 322). Gaia "does not directly deal with implementation issues" and its output "should be easily implemented using an appropriate agent-programming framework (e.g., a FIPA-compliant agent system) or by using a modern object/component-based framework" (p. 337). One part of the model depends on the agent kind: the agent model assumes "static assignment of roles to agent classes, in which the implementation of the agent class is assumed to hardwire the code to implement one or more roles"; with agents that "dynamically assume roles [...] the Gaia agent model would no longer be of use." (p. 362).

---

## C. MOISE+

**1. Citation and reading.** Jomi Fred Hübner, Jaime Simão Sichman, Olivier Boissier. "A Model for the Structural, Functional, and Deontic Specification of Organizations in Multiagent Systems." SBIA 2002 (Brazilian Symposium on Artificial Intelligence). Copy read: https://moise.sourceforge.net/doc/publications/Hubner-sbia2002.pdf (author copy, 10 PDF pages, no printed page numbers or volume data). Read: the whole paper. Part of PDF pp. 5-6 (the scope of compatibilities and the soccer group specification beside Fig. 2) was garbled in extraction. Date read: 2026-11-12.

**2. What the source states.**
- *Organizational unit: the group (and the organization).* An organization has an Organizational Specification (OS) and an Organizational Entity (OE): "An OE is a population of agents functioning under an OS." (PDF p. 3). The OS has three parts: "An MOISE+ OS is formed by a Structural Specification (SS), a Functional Specification (FS), and a Deontic Specification (DS)." (PDF p. 3). The group: "a group must be created from a group specification represented by the tuple gt = ⟨R, SG, Lintra, Linter, Cintra, Cinter, np, ng⟩ where R is the set of not abstract roles that may be played in groups created from gt." (PDF p. 4). Groups have sub-groups, intra- and inter-group links, compatibilities, and cardinalities of roles and sub-groups (PDF pp. 4-6).
- *Role, and where it belongs.* "A role means a set of constraints that an agent ought to follow when it accepts to enter a group playing that role." (PDF p. 3). "Roles can only be played in the collective level, i.e., in a group already created in an OE." (PDF p. 4). But a role is not owned by one group: "notice that a role may belong to several group specifications (e.g., the leader)." (PDF p. 6). Roles have inheritance and abstract roles (PDF pp. 3-4).
- *Occupants.* Cardinality per role in a group, e.g. "one or two agents playing the coach role, one agent playing the leader role" (PDF p. 6). Agents choose to join: "there is not a 'new Role()' command to create an agent for a role. [...] the agents of a MAS are autonomous and decide to 'follow' the rules stated by the OS." (PDF p. 9). People are not discussed.
- *Responsibilities.* Expressed as goals grouped into missions, in the functional specification: "a Social Scheme (SCH) which is essentially a goal decomposition tree where the root is the SCH goal and where the responsibilities for the sub-goals are distributed in missions" (PDF p. 6). "a mission is a set of coherent goals that an agent can commit to." (PDF p. 7). Missions are linked to roles by the deontic specification (below).
- *Workflow.* The social scheme with plan operators sequence, choice and parallelism (PDF p. 6), a success rate per plan (PDF p. 7), a well-formedness condition on the number of agents committed to each mission (PDF p. 7), and mission preferences (PDF p. 8). "the FS is a set of several SCHs and mission preferences which describes how a MAS usually achieves its global goals" and it can be stored by agents "as an enterprise does through its 'procedures manual'" (PDF p. 8).
- *Authority, permissions, obligations.* Links between roles: "link(ρs, ρd, t) where [...] t ∈ {acq, com, aut}" for acquaintance, communication and authority; "In a authority link (t = aut), the ρs agents are allowed to have authority on ρd agents, i.e., to control them." (PDF p. 4). Deontic relations: "A permission per(ρ, m, tc) states that an agent playing the role ρ is allowed to commit to the mission m, and tc is a time constraint"; "an obligation obl(ρ, m, tc) states that an agent playing ρ ought to commit to m in the periods listed in tc." (PDF p. 8). "The DS is thus a set of obligations and permissions for the agents, through roles, on SCH, through missions." (PDF p. 9).
- *Separation of structure and function.* "The objective is an organization centered model where the first two dimensions can be specified almost independently of each other and after properly linked by the deontic dimension." (PDF p. 3). "we can change, for instance, the functioning dimension without changing the structure, only the deontic dimension needs to be adjusted." (PDF p. 10).
- *Shared infrastructure.* None in this paper.
- *Registry or directory.* None. The DS is a specification, not a run-time lookup.
- *How one unit asks another for work.* An agent whose role is permitted the root mission can start a scheme and so obligate others: "If an agent starts a SCH [...] it can force, by the DS, other agents to commit to this SCH missions." (PDF p. 9). Inter-group links allow communication or authority across groups (PDF p. 5). No request protocol between groups is specified.

**3. Ratings.**
| Criterion | Value | Quotation or search |
|---|---|---|
| C1 | yes | The group specification tuple "gt = ⟨R, SG, Lintra, Linter, Cintra, Cinter, np, ng⟩ where R is the set of not abstract roles that may be played in groups created from gt" (PDF p. 4). |
| C2 | part, DISPUTABLE (yes) | Roles are specified per group (the tuple above). Responsibilities (missions) are specified per role, not per group: "an obligation obl(ρ, m, tc) states that an agent playing ρ ought to commit to m" (PDF p. 8). Yes is defensible because the OS as a whole specifies both responsibilities and roles apart from the agents, and roles are attached to group specifications. |
| C3 | part | The DS records, per mission, which roles are obliged or permitted: "The DS is thus a set of obligations and permissions for the agents, through roles, on SCH, through missions." (PDF p. 9). The owner is a role, not an area, and uniqueness is not required. |
| C4 | no | Searched for lookup, discovery, directory. None. Acquaintance links grant only permission "to have a representation of the agents playing the destination role" (PDF p. 4). |

**4. Comparison with the WARM description.**
- MOISE+ has and the description lacks: a formal, separable functional specification (goal trees, plans, missions with agent cardinalities); a deontic layer that binds roles to missions with time constraints; typed links between roles (acquaintance, communication, authority) with inheritance rules; role compatibility and cardinality constraints; well-formedness conditions; the stated aim of changing the functioning without changing the structure.
- The description has and MOISE+ lacks: a unit that owns its goals and responsibilities (in MOISE+ missions attach to roles, and a role can appear in several groups); knowledge, tools and acceptance criteria per unit; an offer to other units; a shared platform; a directory; people.

**5. LLM agents?** No (2002). The paper assumes autonomous agents that may or may not follow the organization: "this paper does not cover how an agent will (or won't) follow the organizational norms." (PDF p. 9). Goals are "collective goals and not social goals", because "it is not possible to concept the social goal which depends on the agents internal mental state" (PDF p. 6, footnote 2). The organizational model does not depend on a kind of agent.

---

## D. Microsoft Cloud Adoption Framework: AI agent adoption guidance

**1. Citation and reading.** Microsoft, *Cloud Adoption Framework for Azure*, "AI agents" section, learn.microsoft.com. Pages read (in the published source repository MicrosoftDocs/cloud-adoption-framework, folder `docs/ai-agents/`, commit d9d5da6 of 2026-11-09, which is the source of the learn.microsoft.com pages):
- "Process to build agents across your organization" (`build-secure-process.md`, ms.date 2025-12-01), https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/build-secure-process ; read in full. This is the page with "Define the agent charter".
- "Governance and security across the organization" (`governance-security-across-organization.md`, ms.date 2026-04-09), https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization ; the control-plane section read.
- "Organizational readiness" (`organization-people-readiness-plan.md`, ms.date 2025-12-01); the responsibilities section read.
- "Single agent or multiple agents" (`single-agent-multiple-agents.md`, ms.date 2025-12-01); the multi-agent sections read.
The other pages were searched with grep for charter, registry, inventory, owner, department, business unit. The live learn.microsoft.com pages were not rendered directly; the text comes from the Markdown source. Date read: 2026-11-12.

**2. What the source states.**
- *The agent charter.* "Define the agent charter. Create governance artifacts that document agent boundaries and business alignment. The charter serves as the authoritative reference for what the agent system accomplishes and what it must avoid. This documentation prevents scope creep, ensures compliance teams understand system boundaries, and provides clear accountability when issues arise. Include system responsibilities that map to specific business objectives, agent roles that prevent functional overlap, and prohibited actions that establish compliance guardrails." (build-secure-process, section 1). The charter is per agent system. Agent instructions are specified separately per agent: "Identity and tone", "Scope and boundaries", "Tool mandates", "Citation rules" (same page, "Agent instructions").
- *Organizational unit.* Business units and teams appear as the organization's existing structure, not as elements of an agent model: "Workload teams operate within business units and own the end-to-end lifecycle of specific agents. They define business requirements, curate domain-specific data, design conversation flows, and integrate agents into business processes." (organization-people-readiness-plan). Multi-agent design is recommended "when distinct teams manage separate knowledge areas. [...] teams maintain domain-specific agents. [...] This alignment mirrors organizational structure" (single-agent-multiple-agents, criterion 2).
- *Role.* "agent roles that prevent functional overlap" (charter, above). Roles are roles of agents within one agent system.
- *Occupants.* Not specified beyond agents and human approval steps: "mandate human-in-the-loop confirmation for high-impact actions" (build-secure-process, "Agent tools").
- *Workflow.* Approved orchestration patterns and deterministic workflows: "Enforce the use of deterministic workflows for critical business logic." (build-secure-process). Workflow capabilities include "Branching logic | Routes requests to appropriate agents based on conditions, enabling escalation from chatbots to specialized agents or human support" (single-agent-multiple-agents).
- *Authority, permissions, rules.* Charter "prohibited actions"; least privilege for tools ("ensuring the agent holds only the permissions necessary for the specific task", build-secure-process); "Require each agent to operate under a distinct agent identity" (governance page, item 3); policies applied "consistently across first-party agents, custom agents, and third-party agents" (item 4).
- *Shared platform, distinct from units.* "The platform team manages the technical foundation and governance guardrails. [...] Workload teams [...] inherit the security controls of the platform" (organization-people-readiness-plan). Also an AI Center of Excellence as "a centralized advisory body" (same page).
- *Registry.* "Maintain an agent registry. [...] Require every AI agent to be recorded in a single organizational inventory. Track ownership, purpose, platform, and access scope. Treat agents as managed organizational resources. Agent 365 provides an Agent Registry when adopted." (governance page, item 2). Accountability for governance as a whole: "Assign ownership for agent governance to the same leaders responsible for cloud governance, security, and compliance." (item 1).
- *How one unit asks another for work.* Not described for teams or business units. Between agents, through workflows (above) and an "A2A tool" listed under Microsoft facilitation (build-secure-process).

**3. Ratings.**
| Criterion | Value | Quotation or search |
|---|---|---|
| C1 | part | Business units and teams are used, not defined in the model: "Workload teams operate within business units and own the end-to-end lifecycle of specific agents." |
| C2 | part | The charter specifies responsibilities and roles per agent system, not per area: "Include system responsibilities that map to specific business objectives, agent roles that prevent functional overlap, and prohibited actions" |
| C3 | part | The registry names an owner per agent, not per responsibility: "Require every AI agent to be recorded in a single organizational inventory. Track ownership, purpose, platform, and access scope." |
| C4 | part | Routing exists inside workflows: "Branching logic: Routes requests to appropriate agents based on conditions". No lookup from a kind of work in the registry is described. |

**4. Comparison with the WARM description.**
- CAF has and the description lacks: a concrete adoption sequence (plan, govern and secure, build, manage); a named organizational split between a platform team, workload teams and an AI Center of Excellence; per-agent identity, cost tracking per department; deterministic workflows for critical logic; registry fields (ownership, purpose, platform, access scope).
- The description has and CAF lacks: a charter per area of work rather than per agent system; roles that people as well as agents fill; an offer of one area to others; a directory that records accountability per responsibility and how to reach the accountable area.

**5.** Not applicable (D is not one of A to C).

---

## E. Beyond the Agent Harness

**1. Citation and reading.** Lei Hua. "Beyond the Agent Harness: Boundary Criteria for Software-Factory Orchestration. A Single-Operator Case Study." arXiv:2611.06946v1 [cs.SE], 3 November 2026. https://arxiv.org/abs/2611.06946 (URL from search.md entry 12; PDF read from https://arxiv.org/pdf/2611.06946). Read: abstract, sections 1, 2 (related work, in part), 3 (framework, in full), 4 (case), and the appendix rows on registries. Not read: sections 5-10 in detail. Date read: 2026-11-12.

**2. What the source states.**
- *Layers.* "From top to bottom: the Domain layer holds industry rules, cases, evaluation sets and compliance boundaries, and is pluggable; the Factory Harness orchestrates runs, keeps state, verifies externally, classifies failures, enforces budgets and locks, and runs preflight; the Agent Harness provides tools, context, permissions, sandbox and the loop for one run of one agent; the Foundation Model reasons and generates; the Plant provides machines, runners, network, caches and credential stores." (section 3.2, p. 4).
- *The domain.* Defined by a change test: "C3 If it must change when the application domain changes (an industry, or a functional domain such as payments), it belongs to the Domain layer." (section 3.3, p. 6). "The domain sits above the factory as an input, not inside it as configuration" (p. 4). In the case: "Domain differences between projects appear as plug-in and configuration fields, for example a validation-scope declaration and a named reviewer for SQL configuration in a medical project, while engine code stays shared" (section 4, p. 9). "C3 precedes C2 because a domain rule remains a domain rule when the factory enforces it" (p. 7).
- *Shared layer serving all projects.* The factory harness: "the layer between the agent harness and the domain layer that organises the runs of one or more agents into a production process that is verifiable, recoverable and continuously deliverable. It is responsible for scheduling and resource locks, persistent state across runs, verification that the agent cannot reach, failure classification and repair budgets, environment preflight, and human intervention points." (section 3.1, p. 4). The case pipeline "serves six business projects (P1-P6)" (p. 8).
- *Role, occupants.* Not part of the model. Roles appear only in related work: "Role-based multi-agent frameworks such as MetaGPT encode standard operating procedures as agent roles within one workflow" (p. 3). Human role in the case: "the operator reviews only intent and acceptance evidence" (p. 9).
- *Workflow.* Not specified per domain. The paper's loop is a failure-to-rule feedback loop: a failure "is classified by layer, sedimented either as a factory-structure fix or as a domain rule or evaluation, and enforced as a gate in later runs." (section 3.4, p. 8).
- *Authority, rules.* Domain rules and evaluation sets; protected test files ("the mechanism belongs to the Factory and the path list to the Domain", Fig. 2 caption, p. 9).
- *Registry or directory.* None in the model. An appendix row classifies a "Claim-boundary registry / prohibited-wording guard" as a factory mechanism; the related-work table records "skills registry" for Uber's factory (Table 1). Neither is a directory of accountability.
- *How one unit asks another for work.* Not discussed.

**3. Ratings.**
| Criterion | Value | Quotation or search |
|---|---|---|
| C1 | part | A domain is a defined layer ("the Domain layer holds industry rules, cases, evaluation sets and compliance boundaries, and is pluggable", p. 4), but nothing states that agents or roles belong to it; it is a layer of rules and evaluations, not a unit of actors. |
| C2 | part | Some properties at the level of the domain (rules, cases, evaluation sets, compliance boundaries; "a named reviewer for SQL configuration in a medical project", p. 9); no statement of the domain's responsibilities, no roles. |
| C3 | no | Searched for registry, directory, owner, accountable. Only the "Claim-boundary registry / prohibited-wording guard" (appendix) and "skills registry" in a related-work row, neither of which records an accountable owner per responsibility. |
| C4 | no | Searched for routing or lookup between projects or agents. None; each project selects one of three harnesses by configuration (p. 8). |

**4. Comparison with the WARM description.**
- The source has and the description lacks: an operational definition of a run and three boundary tests (C1 run-scoped, C2 cross-run, C3 domain-changing) with residual tests for plant and model; a three-field incident coding (defect origin, control gap, fix layer); a separate infrastructure ("Plant") layer under the model; a reliability check of the criteria with two coders; a feedback loop that turns failures into factory fixes or domain rules.
- The description has and the source lacks: domains as units that agents and people belong to, with goals, responsibilities, roles, workflow, tools and an offer to other domains; identified agents filling roles; a directory. The source's scope is coding pipelines run by one operator.

**5.** Not applicable.

---

## F. WorkMate

**1. Citation and reading.** Guowen Li, Zhongbo Jing, Zhidong Liu, Jiayao He, Qi Xu, Zhen Lei, Xuanning Zhang, Gong Shen, Hao Qiu, Zirui Xu. "WorkMate: A Human-AI Collaborative Agent Infrastructure for Enterprise Organizational Governance." Preprint, Zenodo, 2026-06-11. DOI 10.5281/zenodo.20644795. https://zenodo.org/records/20644795 (from search.md entry 33). Read: the PDF from the Zenodo record (28 PDF pages): abstract, introduction, sections 2.3-2.4 in part, 3 (architecture), 4 (execution and SubAgents), 6.1-6.2. Not read: section 5 (memory) beyond its opening, section 7 onward. Date read: 2026-11-12.

**2. What the source states.**
- *Organizational unit: department (mapped, not defined).* "WorkMate maps enterprise departments, positions, and responsibilities to permissions, skill accessibility, and contextual boundaries within the agent system." (section 3.2, PDF p. 12). "Every agent node within the system is explicitly mapped to enterprise roles, departments, and organizational positions." (section 6.1, PDF p. 16).
- *Role.* Institutional roles taken from the company, contrasted with roles in other LLM work: "the concept of 'roles' in existing multi-agent research primarily refers to logical roles rather than institutional roles grounded in real enterprise organizations." (section 2, PDF p. 8).
- *Occupants.* An agent stands for an employee or a business module: "SubAgents correspond to specific business modules or employee roles and execute concrete skill-oriented operations." (section 4.2, PDF p. 13). "AI systems do not possess independent permissions; rather, they function as digital extensions of employee execution capabilities." (PDF p. 16).
- *Responsibilities.* Assigned through the organizational mapping above and through skills: "enterprise workflows are decomposed into executable skills, where each skill encapsulates task execution logic, permission constraints, and institutional rules." (section 4.1, PDF p. 13).
- *Workflow.* Skills, scheduled by a skill orchestration layer, and a master agent: "The master agent is responsible for task scheduling, workflow monitoring, and global strategy management" (section 4.2, PDF p. 13).
- *Authority, permissions, rules.* "Permission Homology, whereby an agent's execution permissions are strictly inherited from the organizational permissions of its corresponding employee." (section 6.1, PDF p. 16). Approval: "Tasks involving sensitive data access, financial operations, contract approval, or external information dissemination automatically trigger approval workflows that require explicit human authorization before continuation." (section 3.3, PDF p. 12).
- *Shared infrastructure.* "a five-layer design paradigm that spans user interaction, governance control, skill orchestration, agent execution, and infrastructure support. [...] the infrastructure layer provides tools, databases, language models, and runtime environments" (section 3.1, PDF p. 11).
- *Registry or directory.* No registry is described in the sections read. The organizational mapping is stated but its form (table, store) is not. Audit logs record "execution traces, operator identities, timestamps, data states, approval histories, and exception-handling procedures" (PDF p. 12).
- *How one unit asks another for work.* Through the master agent; "cross-employee coordination" is supported (PDF p. 13), with "strict context isolation to ensure that sensitive data and operational permissions do not propagate across organizational boundaries" (PDF p. 13).

**3. Ratings.**
| Criterion | Value | Quotation or search |
|---|---|---|
| C1 | part | Departments are used but not defined in the model: "WorkMate maps enterprise departments, positions, and responsibilities to permissions, skill accessibility, and contextual boundaries within the agent system." (PDF p. 12) |
| C2 | part | Properties (permissions, skill access) are set per role and per agent through the mapping; no area-level statement of responsibilities and roles: "Every agent node within the system is explicitly mapped to enterprise roles, departments, and organizational positions." (PDF p. 16) |
| C3 | part | The mapping names a role and department per agent node, not an accountable owner per responsibility; the mapping's form is not described (same quotation, PDF p. 16). |
| C4 | part | Routing is inside one orchestrator: "The master agent is responsible for task scheduling, workflow monitoring, and global strategy management, whereas SubAgents correspond to specific business modules or employee roles" (PDF p. 13). |

**4. Comparison with the WARM description.**
- WorkMate has and the description lacks: permissions inherited from the employee an agent stands for; approval-driven execution for named classes of risky operation; a skill lifecycle with approval (PDF p. 14); context isolation between SubAgents.
- The description has and WorkMate lacks: a written charter per area of work; areas that are defined units rather than a mapping from the company's org chart; an offer from one area to others; a directory of accountability and reachability; agents as identified actors in their own right (WorkMate's agents are extensions of employees).

**5.** Not applicable.

---

## G. Kandogan et al., blueprint architecture for compound AI

**1. Citation and reading.** Eser Kandogan, Nikita Bhutani, Dan Zhang, Rafael Li Chen, Sairam Gurajada, Estevam Hruschka (Megagon Labs). "Orchestrating Agents and Data for Enterprise: A Blueprint Architecture for Compound AI." arXiv:2504.08148v1, 10 April 2025. https://arxiv.org/abs/2504.08148. Read: the full paper (10 PDF pages), with sections IV and V (architecture and components) read closely. Date read: 2026-11-12.

**2. What the source states.**
- *Organizational unit.* None. The HR company is an example setting: "While we present an HR scenario, the proposed architecture is not specific to any industry" (section II). The nearest scoping construct is the session: "A 'session' defines the context and scope for agents' collaborative work." (section V.E).
- *Agent.* "An agent, broadly defined as a 'compute' entity responsible for executing tasks [...] encompasses any computational entity that processes input data and generates output. For instance, an LLM-based model, a task-specific CRF model, a search interface, or any API can serve as an agent" (section V.B).
- *Role, occupants, responsibilities.* Not modeled. Agents are named by function (PROFILER, JOB MATCHER, PRESENTER).
- *Workflow.* "A task planner interprets user requests and devises a task plan that available agents can execute"; it "formulates a task plan structured as directed acyclic graphs (DAGs) connecting agent input and outputs" (section V.F). A task coordinator "coordinates and monitors execution of an agentic workflow, keeping track of the budget" (section IV).
- *Authority, permissions.* Not part of the architecture; listed as open: "How to ensure data-governance and support data privacy in agentic workflows, with potentially agents with different privileges?" (section VII).
- *Shared infrastructure.* Streams: "a 'stream' is the central 'orchestration' concept" (section V.A); a streams database "manages the flow of data and control messages among these components" (section IV); also a budget, an optimizer and a data planner.
- *Registry.* "An agent registry stores and organizes metadata about agents, including their descriptions, input and output parameters, stream inclusion/exclusion rules, deployment information such as docker images, deployment configurations, along with other properties." (section V.C). "Agent registry can be queried and searched by any agent. Searches can utilize keywords or vector-based techniques using learned representations derived from metadata and logs." (section V.C). A data registry holds data-source metadata "at various levels of granularity" (section V.D). No owner field is mentioned.
- *How work is requested.* Through the planner and the registry: "The task planner utilizes metadata sourced from the agent registry to identify suitable agents for each sub-task." (section V.F), and through tagged streams that agents listen to (section V.E).

**3. Ratings.**
| Criterion | Value | Quotation or search |
|---|---|---|
| C1 | no | Searched for department, team, domain, group, organization as model elements. None; "domain" occurs only as "the HR domain" example, and the session is a context for one piece of collaborative work. |
| C2 | no | No area exists to specify. |
| C3 | no, DISPUTABLE (part) | The agent registry stores "descriptions, input and output parameters, stream inclusion/exclusion rules, deployment information" (section V.C), with no owner or accountable party. Part is defensible if a registry entry is read as naming the provider of a capability. |
| C4 | yes | "The task planner utilizes metadata sourced from the agent registry to identify suitable agents for each sub-task." and "Agent registry can be queried and searched by any agent." (sections V.F, V.C); entries include deployment information. |

**4. Comparison with the WARM description.**
- The source has and the description lacks: streams as the coordination medium; a data registry beside the agent registry; QoS budgets and a multi-objective optimizer over task and data plans; vector search over registry metadata and usage logs.
- The description has and the source lacks: areas of work, charters, roles, people directing the work, accountability. The registry lists agents by function and deployment, not by accountable area.

**5.** Not applicable.

---

## H. EDDOps

**1. Citation and reading.** Boming Xia, Qinghua Lu, Liming Zhu, Zhenchang Xing, Dehai Zhao, Hao Zhang. "Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture." arXiv:2411.13768v3, 17 November 2025. https://arxiv.org/abs/2411.13768. Read: abstract, section 1, section 5.1 (Step 1, evaluation plan), section 6 (reference architecture) in full; other sections searched with grep for registry, owner, role, team, domain, governance. Date read: 2026-11-12.

**2. What the source states.**
- *Organizational unit.* None. "domain" means application domain, e.g. "domain sensitivity (e.g., healthcare versus general use)" (section 5.1).
- *Layers.* "an Evaluation Backbone and Control Loop that causally links evidence to both development-time and operation-time changes [...] across the Supply Chain, Agent, and Operation layers" (section 6).
- *Role, occupants, responsibilities.* Not modeled for agents. The architecture's own responsibilities are listed as drivers D1 to D6 (section 6). Humans appear as evaluators and approvers: "Hybrid evaluation policies determine when automation suffices and when escalation to human review is required." (section 6.3.1).
- *Workflow.* The agent module has "Reasoning & Planning" and "Workflow Execution" components that emit traces (section 6.2). The paper's process model is the evaluation process (four steps, section 5).
- *Acceptance criteria and rules.* "Carry regulatory and policy constraints into acceptance criteria, evaluator policies, and logging or retention choices" (section 5.1, step 2). "Understand User Goals: Translate high level goals into structured, testable scenarios with expected interactions, conditions, success criteria, and failure tolerance" (step 1). These are per agent system.
- *Shared infrastructure.* "The AgentOps Infrastructure is the operational environment where evaluation becomes actionable" with release controls, error analysis and a feedback pipeline (section 6.3.2).
- *Registry or directory.* None for agents. Evidence stores: "Versioned Evaluation Results, Test Cases, and Safety Cases form the knowledge base that both paths rely on." (section 6.3.1); a "Versioned Test Catalog" (section 5.2).
- *How work is requested between units.* Not discussed. "other agents (coordination)" are listed as an external environment (section 6.2).

**3. Ratings.**
| Criterion | Value | Quotation or search |
|---|---|---|
| C1 | no | Searched for department, team, domain, group, organization as model elements. None; "domain" is the application domain. |
| C2 | no | No area. Acceptance criteria and goals are per agent system: "Carry regulatory and policy constraints into acceptance criteria" (section 5.1). |
| C3 | no | Searched for registry, owner, accountable. Only evidence stores (evaluation results, test cases, safety cases), which name no owner. |
| C4 | no | Searched for routing, discovery, registry. None; other agents appear only as an external environment "(coordination)" (section 6.2). |

**4. Comparison with the WARM description.**
- The source has and the description lacks: evaluation as a governing control loop with offline and online paths; versioned evidence stores linking each change to its evidence; release controls (shadow evaluation, canary rollout, kill switches); a multivocal literature review as empirical basis.
- The description has and the source lacks: areas of work, roles, a shared platform serving several areas, a directory. The source's acceptance criteria are per agent system; the description's are per domain.

**5.** Not applicable.

---

## Additions from the older literature

I added two works. Electronic Institutions (ISLANDER/AMELI) were considered and not added; see the note after the second addition.

### Addition 1. OperA

**Why added.** OperA separates an organizational model (objectives, roles, norms, interactions) written by the organization's owners from the agents that later enact the roles, and it names facilitation roles that serve the whole society, including a matchmaker that registers skills and distributes requests. These are closer to "a written specification of an area apart from who does the work", "a shared service" and "finding where to send work" than anything in A to C.

**1. Citation and reading.** Virginia Dignum, Frank Dignum, John-Jules Meyer. "An agent-mediated approach to the support of knowledge sharing in organizations." *The Knowledge Engineering Review* 19(2):147-174, 2004. doi:10.1017/S0269888904000244. Copy read: https://www.maxapress.com/data/article/ker/preview/pdf/S0269888904000244.pdf (publisher layout, 28 pages). Read: sections 2.2, 3 (the OperA model, pp. 150-157), 5.1-5.2 (the knowledge-market design, pp. 161-167). Not read: sections 4 and 5.3-5.4 in detail. Dignum's 2004 thesis, the full source of OperA, was not read. Date read: 2026-11-12.

**2. What the source states.**
- *Organizational unit: the society (organization).* "The organizational structure of the society, as intended by the organizational stakeholders, is described in the organizational model (OM)." (p. 153). "The OM specifies an agent society in terms of four structures: social, interaction, normative and communicative. The social structure specifies objectives of the society, its roles and the model that governs coordination." (p. 154). Separation from occupants: "The model separates the description of the structure and global behavior of the domain from the specification of the individual entities that populate the domain." (p. 152). Groups are mentioned only as a target of norms ("whether a norm refers to a role, a scene, a transition, or a group", p. 164).
- *Role, and where it belongs.* Roles belong to the society's OM: "The global objectives of an organization are represented in terms of objectives of the roles that compose the organization. Roles are tightly coupled to norms" (p. 154). The design yields "role descriptions for all society roles, as well as their objectives, norms and dependencies" (p. 157). The example's role table has the columns "Role | Relation to society | Role objectives | Role dependencies" (Table 3, p. 163).
- *Occupants.* "Agents are actors that perform role(s) described by the society design. The agent's own capabilities and aims determine the specific way an agent enacts its role(s)." (p. 152). The social model lists "role-enacting agents (REAs)" and "several populations are possible for each OM" (p. 154). People act through agents: "People seeking collaboration through the knowledge market will initiate a personal agent that acts as their avatar in the system." (p. 166).
- *Responsibilities and their assignment.* Through social contracts: "when an agent applies, and is accepted, for a role, it will commit itself to the realization of the role goals [...]. These commitments are specified as social contracts that can be compared to labor contracts between employees and companies." (pp. 154-155). "Negotiation of social contracts is carried out between the applicant agent and the gatekeeper agent" (p. 166).
- *Workflow.* "roles interact with other roles according to interaction scripts that describe a 'unit' of activity in terms of landmarks. The interaction structure gives a partial ordering of the scene scripts" (p. 154). At run time, "interaction contracts" instantiate scene scripts (p. 155).
- *Norms.* "Society norms and regulations are specified in the normative structure, expressed in terms of role and interaction norms." (p. 154). "The society can sanction undesirable (wrong) behavior" (p. 155).
- *Shared services: facilitation roles.* "We distinguish between social, or facilitation roles, that is, roles needed in order to keep the society going, and operational roles, which will provide the actual objectives of the society. Facilitation roles are usually played by mutually trusted agents" (pp. 155-156; the source's dashes replaced by commas). In the example, facilitation roles are Gatekeeper, Notary, Monitor and Matchmaker (Table 1, p. 162), and "external agents cannot apply to a facilitation role" (p. 166).
- *Registry and finding where to send work.* Table 1 (p. 162): "Matchmaker | Register participants, skills and needs; Accept and distribute exchange requests | Obliged to distribute requests; Obliged to give distribution requests back to requester". "Notary | Register agreements; Assign monitors | Obliged to register exchanges". The role table lists "Knowledge seeker | [...] | Request knowledge | Matchmaker" (Table 3).
- *How one unit asks another.* OperA models one society; requests between roles go through scene scripts and, in the example, through the matchmaker.

**3. Ratings.**
| Criterion | Value | Quotation or search |
|---|---|---|
| C1 | yes | "The OM specifies an agent society in terms of four structures: social, interaction, normative and communicative." (p. 154). The unit is the whole society, not one of several areas. |
| C2 | yes | "The social structure specifies objectives of the society, its roles and the model that governs coordination." (p. 154), specified apart from agents: "The model separates the description of the structure and global behavior of the domain from the specification of the individual entities that populate the domain." (p. 152) |
| C3 | part | The role table names a role per objective ("Role | Relation to society | Role objectives | Role dependencies", Table 3, p. 163); accountability is not stated and the owner is a role, not an area. |
| C4 | part, DISPUTABLE (yes) | "Matchmaker: Register participants, skills and needs; Accept and distribute exchange requests" (Table 1, p. 162). Yes is defensible because requests are routed from a need to a registered capability at run time; part is given because the lookup is done by an intermediary role defined for one example society, not as a general part of the model. |

**4. Comparison with the WARM description.**
- OperA has and the description lacks: a social contract per role enactment, negotiated with a gatekeeper; interaction contracts that instantiate scene scripts; sanctions; a formal semantics (the LCR deontic temporal logic, p. 153); the explicit distinction between facilitation roles and operational roles; a stakeholder table.
- The description has and OperA lacks: several areas of work inside one organization, each with its own charter and an offer to the others (OperA specifies one society); tools and acceptance criteria per area; a shared platform as a layer rather than as roles played by trusted agents; a directory of accountability per responsibility.

**5. LLM agents?** No (2004). Agents are "autonomous communicative entities that will perform the society's role(s) according to their own internal aims and architecture" (p. 154); "The design of the agents themselves is outside the scope of an OperA model." (p. 157). The paper notes one dependence on agent capability: social-contract negotiation "can be very simple [...]. More sophisticated versions will require that agents are able to reason about goals, norms and objectives." (p. 166).

### Addition 2. Horling and Lesser, survey of organizational paradigms

**Why added.** It is a survey of organizational forms for multi-agent systems, and it describes federations in which an intermediary holds a "yellow pages" of member capabilities and routes needs to providers, and societies whose services ("directories" among them) are run by agents in facilitation roles. These are the closest older material to a directory and a shared platform.

**1. Citation and reading.** Bryan Horling, Victor Lesser. "A Survey of Multi-Agent Organizational Paradigms." *The Knowledge Engineering Review* 19(4):281-316, 2004. doi:10.1017/S0269888905000317. Copy read: the authors' May 2005 version hosted at https://posomas.isse.de/PosoMAS-Scrum/aose.practice.tech.agent_organisation_design.base/guidances/whitepapers/resources/Bryan%20Horling%20and%20Victor%20Lesser%20-%20A%20Survey%20of%20Multi-Agent%20Organizational%20Paradigms.pdf (36 PDF pages; page numbers below are this copy's printed numbers, not the journal's). Read: abstract and introduction (pp. 1-2), section 7 Societies (pp. 14-15), section 8 Federations (pp. 15-17), section 10 Matrix organizations (pp. 20-21), and the team-formation passage on matchmakers (p. 9). Not read: hierarchies, holarchies, coalitions, teams (except the passage), congregations, markets, compound organizations, and the comparison tables. Date read: 2026-11-12.

**2. What the source states.**
- *Scope.* "we present a survey of the major organizational paradigms used in multi-agent systems. These include hierarchies, holarchies, coalitions, teams, congregations, societies, federations, markets, and matrix organizations." (abstract). "It is generally agreed that there is no single type of organization that is suitable for all situations" (p. 1).
- *Unit: federate.* "All share the common characteristic of a group of agents which have ceded some amount of autonomy to a single delegate which represents the group" (p. 15). "Group members interact only with this agent, which acts as an intermediary between the group and the outside world" (p. 15).
- *Directory and routing in federations.* "Typically, the intermediate accepts skill and need descriptions from the local agents, which it uses to match with requests from intermediaries representing other groups. In this way the group is provided with a single, consistent interface." (pp. 15-16). Describing Genesereth's federated systems: "Agents connecting to the system start by sending their capabilities to the local facilitator. [...] Needs are similarly routed to the facilitator, which then attempts to find other facilitators that can service that need. Each facilitator provides a yellow pages function which supports this search." (p. 16). Brokering: "An intermediary which accepts task requests and allocates those tasks among its members is known as a broker or a facilitator." (p. 16).
- *Societies: specification and shared services.* "If the society is to be an open and flexible system, its structure must be formally encoded so that potential members may analyze it and determine compatibility. This description can be as simple as a set of common interfaces that must be implemented, or a complex description of permissible roles, high-level objectives and social laws." (p. 14). "Sophisticated legal systems, communication bridges, ontologies, exception handling services, directories may all be part of the society model [...]. Some or all of these may be directly instantiated by trusted agents taking on so-called facilitation roles (differentiated from the operational roles taken on by worker agents)." (p. 15). Joining: "a social contract, or an explicit agreement made between the agent and the society indicating the conditions under which the agent may join that society" (p. 15).
- *Authority.* Matrix organizations "relax the one-agent, one-manager restriction, by permitting many managers or peers to influence the activities of an agent" (p. 20).
- *Role and occupants.* Discussed per paradigm, not as one model; the survey compares people and agents: matrix organizations are "in some sense a closer approximation to how humans exist" (p. 20).

**3. Ratings.** (The survey reports other authors' models; ratings apply to what the survey states.)
| Criterion | Value | Quotation or search |
|---|---|---|
| C1 | yes | Federation: "a group of agents which have ceded some amount of autonomy to a single delegate which represents the group" (p. 15); the survey defines several such units (federates, societies, matrix groups). |
| C2 | part, DISPUTABLE (yes) | The survey reports that a society's structure can be "a complex description of permissible roles, high-level objectives and social laws" (p. 14), but gives this as one option among several and not as a defined specification. |
| C3 | part | The federation intermediary "accepts skill and need descriptions from the local agents" (p. 15): a record of capabilities per agent, with no statement of accountability. |
| C4 | yes | "Needs are similarly routed to the facilitator, which then attempts to find other facilitators that can service that need. Each facilitator provides a yellow pages function which supports this search." (p. 16). This describes cited work (Genesereth 1997; Singh et al. 1995), reported by the survey. |

**4. Comparison with the WARM description.**
- The survey has and the description lacks: a catalog of organizational forms with their tradeoffs; intermediaries per group that both register capabilities and route requests between groups; matrix authority (several managers per agent); societies with entry by social contract.
- The description has and the survey lacks: a single model combining all of these; written charters per area; accountability recorded per responsibility. The survey's yellow pages record capabilities, not accountability.

**5. LLM agents?** No (2004/2005). The survey assumes agents of varied sophistication, and notes that using society services needs capable agents: "agents acting in the society must have a certain level of sophistication to know how and when to use such services." (p. 15). The federation paradigm is described as useful precisely because "individual normal agents do not require a common language as they never directly interact" (p. 16), that is, it does not depend on a kind of agent.

### Considered and not added

Electronic Institutions (ISLANDER/AMELI; Esteva et al. 2001). I read only a secondary description, in the OperA paper (KER 19(2), p. 151, URL above): "This formalism views an agent-based institution as a dialogical system [...] structured through agent group meetings called scenes that follow well-defined protocols", with "governors that regulate agent actions" (pp. 151-152). That is secondary, so I do not describe it further. Its governors could matter for WARM's shared platform; a primary reading would be needed.

---

## Comparison table

C1 to C4 as rated above. "D(x)" marks a DISPUTABLE cell whose alternative value is x.

| Source | Organizational unit | Role | Occupant | Responsibility | Workflow | Authority | Shared platform | Directory | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A. AGR (2003) | Group, instance of a group structure; partitions organization | Belongs to the group structure ("local to groups") | One or more agents; any agent kind, "as clever as a human" | Per role | Interaction protocols between roles; organizational sequence diagrams | Role constraints (correspondence, dependence); gatekeeper for entry; norms deferred | None in model (MadKit implements it) | None | yes | part D(yes) | no | no |
| B. Gaia (2003) | Organization and suborganization, with criteria for splitting | Position in the organization; role schema | Agent classes with cardinality; human actors may play roles; humans in-the-loop "agentified" | Per role (liveness, safety); organizational rules for the whole | Liveness expressions; protocol definitions; services model | Permissions per role; control, peer, dependency relations; organizational rules | Environment model of resources | None (agent model table at design time) | yes | yes | no D(part) | no |
| C. MOISE+ (2002) | Group specification (tuple); organizational specification | Defined in SS; can belong to several group specifications | Agents with cardinality per role | Missions (goal sets) in social schemes | Social schemes: goal trees with sequence, choice, parallelism | Links (acq, com, aut); obligations and permissions role to mission | None | None | yes | part D(yes) | part | no |
| OperA (2004) | Society (organizational model) | Defined in the OM with objectives, norms, dependencies | Role-enacting agents via social contracts; people via personal agents | Role objectives; social contracts | Scene scripts with landmarks; interaction contracts | Normative structure; sanctions; gatekeeper | Facilitation roles (gatekeeper, notary, monitor, matchmaker) | Matchmaker registers skills and needs (example) | yes | yes | part | part D(yes) |
| Horling & Lesser (2004) | Paradigms: federate, society, matrix, etc. | Per paradigm | Per paradigm | Per paradigm | Per paradigm | Hierarchy, matrix (many managers) | Society services run by facilitation roles | Facilitator yellow pages (federations) | yes | part D(yes) | part | yes |
| D. Microsoft CAF | Business units and teams (used, not modeled) | Agent roles inside one agent system's charter | Agents; human approval steps | Charter per agent system | Approved orchestration patterns; deterministic workflows | Charter prohibited actions; least privilege; agent identity | Platform team and platform controls; AI CoE | Agent registry (ownership, purpose, platform, access scope) | part | part | part | part |
| E. Beyond the Agent Harness | Domain layer (rules, cases, evals, compliance) | Not modeled | Operator reviews intent and acceptance evidence | Not per domain | Failure-to-rule feedback loop | Domain rules; protected files | Factory harness and Plant layer | None | part | part | no | no |
| F. WorkMate | Departments (mapped from the company) | Institutional (employee) roles | SubAgent per employee role or business module | Through the org mapping and skills | Skills; master agent schedules SubAgents | Permission homology; approval-driven execution | Infrastructure layer; governance control layer | None found in sections read | part | part | part | part |
| G. Kandogan et al. | None (session as scope of one piece of work) | Not modeled | Agents = any compute entity | Not modeled | Task planner DAGs; task coordinator; streams | Open question | Streams, budget, optimizer, data planner | Agent registry and data registry (no owner) | no | no | no D(part) | yes |
| H. EDDOps | None | Not modeled | Agents; human reviewers | Not modeled (evaluation drivers D1-D6) | Evaluation process (4 steps) | Governance requirements into acceptance criteria | AgentOps infrastructure | None (evidence stores) | no | no | no | no |

---

## What the older organizational literature establishes

Read on their own terms, A to C and the two additions establish, before any LLM work, that a multi-agent system can be specified as an organization whose units (groups, suborganizations, societies) and roles are defined independently of the agents that later fill them (AGR Principle 2, Gaia's roles "abstract from any mapping into agents", OperA's separation of organizational and social models). They establish that roles belong to organizational units rather than to agents, that one agent may hold several roles and one role may have several agents, and that roles carry responsibilities, permissions and obligations (AGR, Gaia, MOISE+). They give separate specifications for structure, function (goal decomposition, missions, protocols) and norms, with an explicit deontic link between roles and work (MOISE+), and rules that apply to a whole organization rather than to one role (Gaia). They treat entry to a unit as a governed act, by gatekeeper or social contract (AGR, OperA, the survey). OperA and the survey also describe services that keep an organization running, played by trusted agents in facilitation roles, including matchmakers and facilitators that register capabilities and route requests. None of these sources has a per-unit written charter that lists tools, knowledge, acceptance criteria and an offer to other units, and none records accountability per responsibility in a directory; the closest are MOISE+'s deontic specification (obligations per role per mission) and the federation facilitator's yellow pages (capabilities per agent). A paper about organizing LLM agents that uses the terms domain, role, charter, shared services or directory would be expected to cite this literature for the parts it shares with it, chiefly the separation of organizational specification from agents, roles owned by units, the deontic link between roles and work, and facilitation services.

---

## Recent LLM-agent work that builds on AGR, Gaia or MOISE

None found in the searches I ran that builds a model on AGR, Gaia or MOISE. One 2024 position paper cites them as background and argues for the approach:

- Önder Gürcan. "Modélisation à base d'Agents Augmentés par LLM pour les Simulations Sociales: Défis et Opportunités." arXiv:2409.00100v1, 27 August 2024 (French; social simulation). It cites Ferber, Gutknecht and Michel 2003, Hübner, Sichman and Boissier (MOISE+), and Dignum, Vázquez-Salceda and Dignum (OMNI) among "méthodologies orientées vers l'organisation" (PDF p. 3, refs [14], [17], [22]) and concludes: "nous affirmons qu'un outil ABM efficace augmenté par LLM devrait soutenir la base conceptuelle orientée vers l'organisation." It does not define an organizational model of its own in the part read.

None of E, F, G or H cites AGR, Gaia, MOISE, OperA, Electronic Institutions or Horling and Lesser (checked by grep of each full text for Ferber, Gaia, Moise, Hübner, Wooldridge, Jennings, Zambonelli, Dignum, Aalaadin, "electronic institution", Horling). WorkMate contrasts its roles with "logical roles" in LLM frameworks such as CAMEL and MetaGPT, not with the MAS organizational literature. arXiv:2607.25446 ("Toward an Organizational Science of Multi-Agent LLM Systems", Chen et al., 2026), found in search, was checked by the same grep and does not cite them.

Searches run (web search, 2026-11-12): "LLM agents organizational model MOISE JaCaMo large language model multi-agent organisation 2024 2025"; "'Agent/Group/Role' OR AGR model LLM-based multi-agent system organization arXiv"; "Gaia methodology LLM-based multi-agent systems roles agent-oriented software engineering arXiv 2024"; "arxiv LLM agents 'Moise' organisation specification roles missions norms language model agents". These four searches are a small sample, not a systematic review; a citation search (papers citing AGR, Gaia or MOISE+ since 2023 in Semantic Scholar or OpenAlex) was not run and would be the stronger test.

---

## What I could not open or verify

- MOISE+: the author copy carries no volume or page numbers, so quotations cite PDF pages. Part of PDF pp. 5-6 was garbled in extraction.
- Gaia: Figures 9 and 10 (role schema template and example) did not extract; the role schema fields are taken from prose only.
- Microsoft CAF: read from the Markdown source in the MicrosoftDocs/cloud-adoption-framework GitHub repository (commit d9d5da6, 2026-11-09), not from the rendered learn.microsoft.com pages. Linked Agent 365 registry documentation was not read.
- WorkMate: sections 5 (memory, beyond its opening) and 7 onward were not read; the form of the organizational mapping (whether a table or store exists) is not stated in the sections read.
- Beyond the Agent Harness: sections 5 to 10 were not read in detail.
- EDDOps: sections 2-4 and 7 were searched, not read.
- OperA: only the KER 2004 paper was read, not Dignum's 2004 thesis or the 2009 book, which define OperA in full.
- Horling and Lesser: the authors' May 2005 copy was read, not the journal version; several paradigm sections were not read.
- Electronic Institutions: no primary source was read; mentioned only from a secondary description.
