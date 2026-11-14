---
title: "Re-rating version 2, reader B"
date: 2026-11-12
author: "reader B (subagent)"
status: "not yet checked by sagan"
---

# Values

Criteria applied: `rerate-criteria-v2.md` (frozen 12:25). "D:" marks a DISPUTABLE cell: the value given is the lower one, and the value after "D:" is the defensible higher one (the reason is in the source section). Directory is derived by the rule in the criteria (yes if C3 and C4 are both yes; part if either is yes or part; no if both are no).

| Source | C1 | C2 | C3 | C4 | Directory (derived) |
|---|---|---|---|---|---|
| 1. AAM/5C (Goujon) | part (D: yes) | yes | part (D: yes) | part | part |
| 2. OperA (Dignum, Dignum, Meyer 2004) | part | part (D: yes) | part | part | part |
| 3. ASOC manifesto (Beheshti et al.) | no (D: part) | no (D: part) | part | part | part |
| 4. Microsoft Multi-Agent Reference Architecture | part | no (D: part) | part | part (D: yes) | part |
| 5. Horling and Lesser survey | part (D: yes) | part | part | yes | part |
| 6. FIPA SC00023K | no | no | part | yes | part |
| 7. Electronic institutions (ISLANDER + AMELI) | part | part | part | part | part |
| 8. JaCaMo (Moise / ORA4MAS material) | yes | part (D: yes) | part | part (D: yes) | part |

DISPUTABLE cells: 10.

# 1. AAM/5C

**Read.** arXiv PDF of 2610.30221 (V7.83-EN, 120 manuscript pages), extracted to text. Read in full: Executive Summary; §1.3.2 (A2A and MCP); §2.2 (five Capabilities, seven layers, Table 2); §2.3 (agents, Table 3); §4.2 (six fundamental entities); §4.5 to §4.7; §6.4 (L3); §7.7.1 (threats, agentic registry); §8.2 (EU AI Act alignment, agentic registry); §8.4 (Agentic Operating Model); Definitions G.1, G.2, G.10, G.11; Appendix 3 §3.3 (Table 14, RACI). Searched the whole text for domain, registry, catalog, agent card, discover, owner, business unit, RACI, accountab, route, find. Not read closely: Chapters 3, 5, 7.2 to 7.8 other than 7.7.1, 8.6 to 8.7, 9 to 11, Appendices 1, 2, 4, 5.

**C1 = part (D: yes).** "To move from concept to implementation, the Capabilities are instantiated in seven logical layers, on the principle of the OSI model: each layer has a single responsibility and communicates with its neighbors through standardized interfaces." (§2.2.2, p. 27). The layers are defined units with several agent types each and seven side by side, so yes is defensible; part because a layer is a fixed tier of one technical stack (L1 Channels to L7 Infrastructure), not an area of work or organizational unit that a system can add or divide, and the source defines no other such unit (the AOM is one operating model for the whole system).

**C2 = yes** (rating the layer). (a) per layer: "L5 — Security and Compliance: the layer of cognitive Zero Trust, which continuously evaluates agent behavior ... and passes its evaluation to L6" (§2.2.2, p. 28); (b) Table 3 assigns agent types (roles) to layers: "Table 3 specifies, for each type of agent, its group, its layer and its role" (§2.3.2, p. 31–32). Each layer has a stated responsibility and a set of agent types defined independently of the agents that instantiate them.

**C3 = part (D: yes).** "R performs, A approves and is accountable, C is consulted, I is informed." and, under Table 14: "Two As on the same row signal a dual signature" (Appendix 3, §3.3, p. 113–114). The RACI matrix is a named artifact that names an accountable role for each of 14 activities, which supports yes; part because at least one row ("Putting a policy into production after dual signature") has two As, so the record does not name exactly one accountable party per entry.

**C4 = part.** "Agent Cards describe each agent's capabilities there, and execution remains opaque" (§1.3.2, p. 22–23), and "G.10. Agentic registry — Inventory of the authorized agents and MCP servers, kept by the AOM; only registered servers, with their digests, are admitted" (Definitions, p. 92). Agents can be described and listed, but the model defines no run-time lookup from a kind of work to a handler: the registry serves admission control, negotiation is limited to "direct dependencies (negotiation scope)" (§2.3.1), and routing is fixed by the layer stack.

# 2. OperA

**Read.** The maxapress PDF link returned a captcha page ("Your access frequency is too high"). I read the Utrecht University Repository copy instead (hdl.handle.net/1874/10587, 29 pages, the published KER 19(2):147–174 text with journal pagination). Read in full: Abstract; §1; §3 (OperA model) including §3.1 to §3.4.3; §5 (knowledge market) §5.1 to §5.4. Skimmed: §2 (related work), §4 (knowledge-sharing scenario). Not read: §6 conclusions beyond the first lines. Figures 3 to 9 (role, group, scene and contract definitions) are images and did not come through as text.

**C1 = part.** "Furthermore, groups of roles were identified and group norms formalized in the group description. In particular, the following groups are relevant for the knowledge market: participant, ... partner, ... browser" (§5.1.3, p. 164–165). Groups appear only in the worked example and are sets of roles sharing norms, not areas of work; the defined unit of the model is the whole society ("The OM specifies the global objectives of the society and the means to achieve those objectives", §3.1, p. 154), and the model defines no way to have several societies or areas inside one.

**C2 = part (D: yes)** (rating the society). "The social structure specifies objectives of the society, its roles and the model that governs coordination. The global objectives of an organization are represented in terms of objectives of the roles that compose the organization." (§3.1, p. 154). Roles are defined independently of agents ((b) holds: "Agents are actors that perform role(s) described by the society design", §3, p. 152), and society objectives are specified, which supports yes; part because the same passage says the society's objectives are represented through the roles' objectives, and the version 2 ruling says responsibilities stated only per role do not meet (a).

**C3 = part.** Table 3 "Role table for knowledge market" lists "Role | Relation to society | Role objectives | Role dependencies", with "Exchange knowledge" under both Knowledge seeker and Knowledge owner (§5.1.2, p. 163); the social model records per-agent "social contracts that make explicit the commitments regulating the enactment of roles by individual agents" (§3, p. 153). The role table and the social contracts are kept records naming the role or agent per objective, but an objective can belong to more than one role and the contracts are commitment records, so not one accountable owner per responsibility.

**C4 = part.** "because the domain requires support for users to find suitable partners, the role of matchmaker is also added to the facilitation layer of the knowledge market" and Table 1: "Matchmaker | Register participants, skills and needs | Obliged to distribute requests" (§5.1.1, p. 162). A matchmaker that registers skills and distributes requests would meet the intermediary ruling, but it is added for this case study, not defined in the model (§3 defines only generic facilitation roles), so it rates part at most.

# 3. ASOC

**Read.** arXiv HTML of 2607.12619v1, converted to text. Read in full: §IV (Defining ASOC: IV-A formal definition, IV-B reference architecture, IV-C three lenses, IV-D, IV-E) and §V (six principles). Searched the rest for department, business unit, domain, group, team, registr, owner, responsible party. Not read closely: §I to §III, §VI agenda (only the registry passages), §VII, §VIII.

**C1 = no (D: part).** The defined units are "Agentic Service: A service entity that accepts goals, constraints, and context ..." and "Agentic Service Ecosystem: A governed, heterogeneous collection of agentic services and conventional services that can be discovered, composed, orchestrated, and managed under shared policies, trust frameworks, and interoperability standards" (§IV-A). Searched for department, business unit, domain, group, team, organization unit: "domain" appears only as use-case domains and regulated domains, "group" only as "vulnerable groups". No unit stands for an area of work; part is defensible if the ecosystem is read as the whole-system unit.

**C2 = no (D: part).** With no C1 unit there is nothing to rate; if the ecosystem is taken as the whole-system unit, it has only unit-level policies ("managed under shared policies, trust frameworks, and interoperability standards", §IV-A) and no objectives or roles, which would rate part.

**C3 = part.** "Delegation Contract: A formal specification of the scope, authority, constraints, duration, revocability, and accountability conditions under which a human or organisation delegates a goal to an agentic service." (§IV-A). This is a defined record of a delegation that carries accountability conditions per delegated goal, a record of obligations taken on while the system runs; it is not a registry naming one accountable owner per responsibility.

**C4 = part.** "Agentic services must expose precisely described capability interfaces supporting automated discovery, selection, and assembly." with realization mechanisms "Capability description language, delegation contract, agent registry and marketplace" (§V-B), and "Capability descriptions for agentic services must draw on context-aware service modelling traditions to support automated discovery, goal-level matching, and contractual accountability" (§IV-C). Goal-level matching would be a lookup from a kind of work, but it is a stated requirement with mechanisms named and not described, so it rates part at most.

# 4. Microsoft Multi-Agent Reference Architecture

**Read.** Repository at commit adbefc1874820d3d61a10cbd0776986c33c4205e (the current HEAD, the same commit as the earlier reading): `docs/agent-registry/Agent-Registry.md`, `docs/reference-architecture/Reference-Architecture.md`, `docs/reference-architecture/Patterns.md` (patterns 1 to 4 in full; the rest skimmed). Fetched but not used: `Building-Blocks.md`, `Governance.md`, `Agents-Orchestration.md`, `Introduction.md` (not read closely). Not read: memory, security, versioning, evaluation, observability docs.

**C1 = part.** "Introduce agent supervisors as the architecture scales across domains—these components help manage and abstract groups of related agents." and "Use hierarchical organization (e.g., supervisor → agent group) to maintain clarity, scalability, and ease of intent resolution." (Reference-Architecture.md, Supervisor Agent, Recommended practices). Agent groups and domains are mentioned as practice advice, but no group or domain unit is defined; the domain belongs to a single agent ("Each agent focuses on a particular domain (e.g., finance, healthcare, coding)").

**C2 = no (D: part).** Agent information holds "`name`: the name of the agent that should convey an idea of the purpose of the agent" and "`description`: A detailed description of what the bot can do." (Agent-Registry.md, For Agent Consumption). Searched for responsibilities, objectives, roles or owners stated for a group or domain and found none; part is defensible if the per-agent name and description are read as a per-agent charter.

**C3 = part.** Registry Storage "Stores comprehensive information about each agent, including capabilities, endpoints, security credentials, performance metrics, and version history." (Reference-Architecture.md, Registry Storage), with optional "`tags` or `owners` in the metadata" for human consumption (Agent-Registry.md). The registry records which agent provides which capability, but accountability is not stated and an owner is optional and per agent.

**C4 = part (D: yes).** "Dynamic Agent Registry (Service Mesh for Agents) — Agent discovery based on capabilities and metadata. Agents register with descriptors (capabilities, tags, embeddings). Registry supports runtime resolution by orchestrator." (Patterns.md §2), and the sequence "Class->>AgReg: 7. Get matching agents" (Reference-Architecture.md). The registry answers from registered capabilities and stores `url` and `authentication`, and its stated goal is "for the agents in the system to know how to communicate with one another", which supports yes; part because every described flow has the orchestrator or its classifier ask the registry for its own plans ("the registry enables the Orchestrator Agent to query which agents are best to carry the immediate tasks at hand"), which the ruling rates part.

# 5. Horling and Lesser

**Read.** The posomas.isse.de PDF (36 pages, May 2005 version), extracted to text. Rated as a survey: what the survey itself describes. Read in full: §1 Introduction; §2 Hierarchies (opening and §2.1); §3 Holarchies (opening); §7 Societies (opening); §8 Federations (all); §9 Markets (opening); §10 Matrix organizations (all); §11 Compound organizations (opening); §12 Other topics (items 1 to 4). Not read: §4 to §6 (coalitions, teams, congregations), §2.2, §3.1 to §3.2, §7.1 to §7.2, §9.1 to §9.2, §11.2, §13.

**C1 = part (D: yes).** "Multi-divisional hierarchies further exploit localization by dividing the organization along product lines, where products might represent different physical artifacts, services, or high-level goals. Each division has complete control over their product" (§2, p. 3); and federations: "each grouping is a federate, and the white agent situated at the edge of each federate is the delegated intermediary" (§8, p. 15). Divisions and federates are areas or groups with several agents side by side, which supports yes; part because the survey describes them in passing (divisions in one sentence citing Fox 1979) and gives no definition of the unit as an element of a model.

**C2 = part** (rating the division / federate). (a) "Each division has complete control over their product" (§2, p. 3); (b) positions at group level appear only as the federate's intermediary: "The delegate is a distinguished agent member of the group, sometimes called a facilitator, mediator or broker" (§8, p. 15). The survey gives some unit-level properties (a scope for a division, a delegate position for a federate) but not both an objective and a set of roles for the same unit.

**C3 = part.** "Agents connecting to the system start by sending their capabilities to the local facilitator. ... Each facilitator provides a yellow pages function which supports this search." (§8.2, p. 16). The facilitator keeps capability entries naming which agent provides what, but accountability is not stated (registering only implies "the agent is willing to use those capabilities").

**C4 = yes.** "Typically, the intermediate accepts skill and need descriptions from the local agents, which it uses to match with requests from intermediaries representing other groups." (§8, p. 15–16) and "Needs are similarly routed to the facilitator, which then attempts to find other facilitators that can service that need." (§8.2, p. 16). The federation paradigm defines the intermediary as part of the organization, every member may send it needs, and it answers or forwards from registered capabilities, which the version 2 ruling rates yes.

# 6. FIPA Agent Management Specification SC00023K

**Read.** The local text extraction of the 2015 Wayback capture (`.../scratchpad/src/fipa-SC00023K-text.txt`), as directed. Read: §2 Agent Management Reference Model; §3 opening; §4.1 Directory Facilitator (§4.1.1 to §4.1.3); §6.1.2 DF agent description and the service-description and AMS-description tables. Searched for group, organisation, department, domain, community, owner, ownership, search. Not read: §4.2 AMS detail, §5 (agent platform lifecycle), most of §6 (ontology), annexes. The extraction carries tracked-change residue and some broken section numbers.

**C1 = no.** Searched for group, organisation, department, domain, community and team: the only organizational reference is the owner of an agent ("An agent must have at least one owner, for example, based on organisational affiliation or human user ownership", §2). The Agent Platform holds many agents but is "the physical infrastructure in which agents can be deployed" (§2), not an area of work.

**C2 = no.** No C1 unit; searched for unit-level responsibilities or roles and found none.

**C3 = part.** The service description registered with the DF has "ownership | The owner of the service | Optional | string" (§6.1.2 / service-description table), and §4.1.1 says "There is no intended future commitment or obligation on the part of the registering agent implied in the act of registering." The DF directory is a kept record naming an owner per service, but the field is optional and accountability is explicitly disclaimed.

**C4 = yes.** "The DF provides yellow pages services to other agents. Agents may register their services with the DF or query the DF to find out what services are offered by other agents" (§2), and the DF is "the trusted, benign custodian of the agent directory ... it must provide the most current information about agents in its directory on a non-discriminatory basis to all authorised agents" (§4.1.1). The DF is a defined element of the reference model, any authorized agent may search it by service description, and it returns agent identifiers whose AIDs carry transport addresses.

# 7. Electronic institutions (ISLANDER and AMELI)

**Read.** AMELI (AAMAS 2004), local PDF: §1, §2, §3.1, §3.2 (execution state, Table 1 operations), §4 (architecture, the four AMELI agent types), §5.1 (agent mediation, Table 2), §5.2.1 opening. Not read: §5.2.2 onward, §5.3 example, §6. Huget et al., "Model Checking Electronic Institutions", local PDF: §1 and §2 in full (ISLANDER, Figure 1 BNF). Not read: §3 onward. The ISLANDER AAMAS 2002 article itself: no open copy found (the IIIA link the search returned, iiia-2002-595.pdf, is the same Huget paper).

**C1 = part.** "An electronic institution is composed of four elements: a dialogical framework, scenes, performatives structure and norms." (Huget §2, p. 1). The only unit is the institution as a whole; scenes are "agent group meetings" that model an activity ("For each activity, interactions between agents are articulated through agent group meetings, the so-called scenes", AMELI §2, p. 2), which the version 2 ruling excludes, and the optional `social-structure` slot in the BNF (Huget Figure 1) is not defined.

**C2 = part** (rating the institution). "The internal roles can only be played by what we call staff agents ... Never an external agent can play an internal role." and "Each role defines a pattern of behaviour within the institution and any agent within an institution is required to adopt some of them." (Huget §2, p. 2–3). Roles are specified at the institution level independently of agents ((b)), but the sources state no objective or mission for the institution beyond its rules ((a) not met).

**C3 = part.** "Obl = {⟨ag, ι, s⟩ | ...} is the set of pending obligations (where ⟨ag, ι, s⟩ stands for the obligation of agent ag to utter illocution ι at scene s)" (AMELI §3.2, p. 3), kept by the governors ("Governors are also in charge of managing norms controlling its associated agent pending obligations", §5.1, p. 5). This is a run-time record of obligations agents take on, which the version 2 ruling rates part.

**C4 = part.** Table 2 "Actions from agent to governor" includes "scenePlayers | Ask for agents in a scene" and "accesScenes | Ask for the scenes the agent can join from a transition" (AMELI §5.1, p. 6). An agent can discover the agents present in a scene through its governor, but there is no lookup from a kind of work or capability to a handler; all interaction is mediated and routed by the performative structure.

# 8. JaCaMo

**Read.** The Science of Computer Programming article could not be opened: the HAL copy (emse-00680402) returned a bot-check page and the publisher was already known to refuse this machine. I rated from the project's own material: ORA4MAS reference (`doc/ora4mas/readme.adoc`, in full); the Moise specification (I read `doc/specification/moise-spec.tex`, the LaTeX source of `moise-spec.pdf` in the same directory, §Organisation Model in full: OS, SS, Link, Group Specification, FS, Scheme, Goal, Plan, Norm, OE, GI, SI; §NOPL for Groups facts); API pages for OrgBoard, GroupBoard and SchemeBoard (class descriptions; NormativeBoard fetched but not used). Not read: jacamo-lang.github.io site pages, the NOPL translation sections in detail.

**C1 = yes.** "A Group Specification (GS) is defined by the elements of the following tuple: ⟨id, compat, maxrp, minrp, maxsg, minsg⟩" with "maxrp : R → Z: is a function that maps each role to the maximum number of players of that role in the group" and "maxsg ... the maximum number of subgroups of the group" (moise-spec, Structural Specification). The group is a defined element distinct from any agent, several agents play roles in it, and a system can hold several groups and subgroups.

**C2 = part (D: yes)** (rating the group). (b) is met at group level (role cardinalities and compatibilities per group specification, roles defined in the SS independently of agents). For (a): "RS : 2^SI is a set of schemes' identification the group is responsible for" (Definition GI) and "responsible(g,s): the group instance g is responsible for the missions of scheme instance s" (NOPL for Groups, Facts). Yes is defensible because a group is made responsible for schemes whose root goal states what must be achieved; part because the group specification itself carries no objective, and responsibility is bound only to group instances at run time.

**C3 = part.** SchemeBoard observable properties: "commitment(ag,mission,sch): agent ag is committed to the mission in the scheme" and "groups: a list of groups responsible for the scheme. e.g. groups([g1])" (SchemeBoard API); the SI definition: "commitments : M → 2^A is a function that maps each mission ... to the set of agents that are committed to that mission". These are kept records of responsibility, but they map a mission to a set of agents and a scheme to a list of groups, so not exactly one accountable party, and they are commitment records.

**C4 = part (D: yes).** "goalState(schId, goal, list of committed agents, list of agents that performed the goal, state)" and "play(ag,role,group): agent ag is playing the role in the group" (SchemeBoard and GroupBoard API; also listed as agent beliefs in the ORA4MAS readme, "Organisational perception"). Any agent focusing on the organizational artifacts can find, from a goal or mission, the agents committed to it, which supports yes; part because the material defines this as perception of commitments in one scheme instance, not a lookup from a kind of work or capability, and states nothing about how to reach the agent beyond its name.

# Disclosures and sources not opened

- I opened no file under `` other than the two named input files and this output file. I checked that this output file did not exist (`test -e`) before writing it; no search or grep printed content from any other file in that folder.
- OperA: the listed maxapress URL returned a captcha page; rated from the Utrecht repository copy of the same published article. The OperA figures (role, group and contract definitions) are images and were not read.
- JaCaMo: the 2013 article was not opened (HAL bot check; publisher refusal). Rated from the Moise specification source, the ORA4MAS readme and the ORA4MAS API pages. I read the `.tex` source of the Moise specification, not the PDF.
- ISLANDER AAMAS 2002 article: no open copy found; rated from AMELI and Huget et al. §2.
- FIPA: rated from the provided text extraction of the 2015 Wayback capture, not from fipa.org.
- AAM/5C has no arXiv HTML version ("No HTML for '2610.30221'"); read from the arXiv PDF. Page numbers are the manuscript's own (x / 120).
- PDFs were converted to text with `pypdf` in a scratchpad virtual environment, because the Read tool needs `pdftoppm` for multi-page PDFs and it is not installed.

# Addendum: JaCaMo re-checked against the 2013 article

**Read.** Boissier, Bordini, Hübner, Ricci, Santi, "Multi-agent oriented programming with JaCaMo", Science of Computer Programming 78 (2013) 747–761, from the two local PDFs (`.../scratchpad/jacamo-article/p1-8.pdf`, printed pp. 747–754, and `p9-15.pdf`, printed pp. 755–761), each read whole with the Read tool. I read all of it: §1 to §6, Figs. 1 to 8 (captions and labels as rendered), and the reference list. Same frozen criteria, same isolation rules: I opened no other file under `papers/warm/` except this one, to append. The original table and sections above are unchanged.

| | Before | After | Change |
|---|---|---|---|
| C1 | yes | yes | stays |
| C2 | part (D: yes) | part (D: yes) | stays |
| C3 | part | part | stays |
| C4 | part (D: yes) | part (D: yes) | stays |
| Directory (derived) | part | part | stays |

**C1 stays yes.** "Finally, on the organisational side, on the basis of Moise, an organisation is described: (i) from a structural point of view, in terms of group and role entities" (§3.1, p. 751). The article's meta-model (Fig. 2, p. 751) has Group as an element with a self-association, and its applications show several groups side by side: "RoomManagement Group", "<EventKind>Group" and "SchedulingGroup" under "BuildingGroup" (Fig. 7, p. 758). The article cites the Moise specification for the group's full definition; together with that specification, the group is a defined unit that several agents belong to, with several per system.

**C2 stays part (D: yes).** "goals defined at the organisation dimension (those goals that are to be achieved by the organisation, i.e., the overall system) are mapped into individual agent goals" (§3.2, p. 753). The article states goals for the organisation as a whole and roles per group, but no objective for a group; in the example, agents become responsible by role ("Companies that won the auction will join the organisation playing specific roles and, by doing so, become responsible for some goals", §4.1.2, p. 756). The GroupBoard's "Schemes" property (Fig. 3, p. 753) agrees with the Moise material's "schemes the group is responsible for", which keeps yes defensible; the article itself adds nothing that settles (a) at group level.

**C3 stays part.** "The state of goals from the organisation dimension (which agents should fulfil them and when) is maintained by an organisational artefact and is displayed as obligations for the agents (e.g., agent a is obliged to fulfil goal x in one week)." (§3.2, p. 753). This is a run-time record of obligations per agent, which the version 2 ruling rates part; the role-to-mission norm table (Fig. 5, p. 756) appears only in the worked example and does not state accountability.

**C4 stays part (D: yes).** "the GroupBoard artefact has an observable property concerning the available roles in a group; therefore agents can find out which are the existing roles and then reason about them so as to autonomously decide whether to adopt a role or not." (§4, p. 754). Agents can discover roles, and artefacts by name ("retrieves the unique identifier of the artefact with the specified name (lookupArtifact action)", §4.1.1, p. 755), but the article describes no lookup from a kind of work or capability to the agent that handles it; in the example Giacomo learns who to contact from the auction artefacts he created and sends to them directly (Fig. 6, p. 756). The higher value (yes) rests on the `goalState` and `commitment` properties in the ORA4MAS API material, not on the article.

# Addendum 2: ISLANDER and AMELI re-checked against the 2002 ISLANDER article

**Read.** Esteva, de la Cruz, Sierra, "ISLANDER: an electronic institutions editor", AAMAS 2002, pp. 1045–1052, from `.../scratchpad/islander-article/islander-aamas-2002.pdf` (8 PDF pages), read whole with the Read tool: §1 to §8, Figures 1 to 4, references. Same frozen criteria and isolation rules: I opened no other file under `papers/warm/` except this one, to append. Nothing above this section is changed. PDF page n carries printed page 1044+n.

| | Before | After | Change |
|---|---|---|---|
| C1 | part | part | stays |
| C2 | part | part | stays |
| C3 | part | part | stays |
| C4 | part | part | stays |
| Directory (derived) | part | part | stays |

**C1 stays part.** "We identify four basic elements of an electronic institution: dialogic framework, scenes, performative structure and norms." (§2, PDF p. 1). The only unit is the institution as a whole. Scenes are activities ("For each activity, interactions between agents are articulated through agent group meetings, which we call scenes", §2, PDF p. 2), which the version 2 ruling excludes. The `[social-structure = (social-structure-def)]` slot in the BNF (Figure 1, PDF p. 3) is left undefined, and the article defines no way to have several institutions or areas inside one.

**C2 stays part.** "Moreover, the dialogic framework defines which will be the participant roles in the institution and the relationships among them. Each role defines a pattern of behaviour within the institution and any agent within an institution is required to adopt some of them." (§2, PDF p. 2). The article defines roles at institution level, independently of agents, which meets (b). It states no objective or mission for the institution beyond its rules ("Institutions represent the rules of the game in a society", §1, PDF p. 1), so (a) is not met.

**C3 stays part.** "Both types of consequences will need to be kept by an institution for each agent on an individual basis." (§2, PDF p. 2) and "the institution does know the obligations that each agent has acquired and can thus detect when an agent does not fulfil its obligations" (§2, PDF p. 3). This is a record of the obligations agents take on while the system runs, which the version 2 ruling rates part. There is no registry that names one accountable owner per responsibility.

**C4 stays part.** "Thus, the agent only communicates with its governor which is responsible to transmit its messages to the corresponding agents." (§7, PDF p. 7). Also: "The communication language allows to express that an illocution is addressed to an agent, to all the agents playing a role or to all the agents in the scene." (§3, PDF p. 3). Addressing by role works only inside a scene the agent has already joined, and governors are planned future work in this article. Neither gives a lookup from a kind of work or a capability to the agent that handles it.
