---
title: "Re-rating version 2: reader A"
date: 2026-11-12
author: "reader A (subagent)"
status: "not yet checked by sagan"
---

# Values

Criteria applied: `rerate-criteria-v2.md` (frozen 12:25). "D:" marks a DISPUTABLE cell: the value given is the lower of two defensible values, and the higher one follows in brackets.

| Source | C1 | C2 | C3 | C4 | Directory (derived) |
|---|---|---|---|---|---|
| 1. AAM/5C (Goujon 2026) | part (D: yes) | part (D: yes) | part | part | part |
| 2. OperA (Dignum, Dignum, Meyer 2004) | part | part (D: yes) | part | part | part |
| 3. ASOC manifesto (Beheshti et al.) | part | part | part | part | part |
| 4. Microsoft Multi-Agent Reference Architecture (adbefc1) | part | part | part | part (D: yes) | part |
| 5. Horling and Lesser survey (rated: the paradigms the survey describes) | yes | part | part | yes | part |
| 6. FIPA SC00023K | no (D: part) | no | part | yes | part |
| 7. Electronic institutions (ISLANDER + AMELI) | part | part | part | part | part |
| 8. JaCaMo (Moise organization model + ORA4MAS) | yes | yes | part | part (D: yes) | part |

DISPUTABLE cells: 6.

# 1. AAM/5C

**Read:** the arXiv PDF (arXiv:2610.30221v1, 195 PDF pages, 120 manuscript pages), extracted to text with pypdf. Read in full: table of contents; §1.3.2 (A2A and MCP); §2.2.1 to §2.3.2 (five Capabilities, seven layers, R-AUT, agent typology, Tables 2 and 3); §4.2 (six entities, functional component, dependency); §4.5; §7.7.1 (agentic registry passage); §8.2 excerpt; §8.4 (AOM roles, RACI); Glossary G.1 to G.13; Appendix 3 §3.3 (Table 14, RACI); Appendix 4 Objection 9. Searched the full text for domain, registry, catalog, owner, RACI, directory, discover, routing. Not read: Chapters 3, 5, 6, most of 7, 9, 10, 11, Appendices 1, 2, 5.

**C1: part (D: yes).** Quote (§2.2.2, p. 27): "the Capabilities are instantiated in seven logical layers, on the principle of the OSI model: each layer has a single responsibility and communicates with its neighbors through standardized interfaces." And (§2.3, p. 31): "Agents specialize according to their place in the stack and fall into three groups, depending on their respective roles: Perception (L1–L2), Cognition (L3–L4–L5) and Governance (L6–L7)." Reason: the layers and agent groups are defined units, each holds more than one agent, and several exist side by side, which reads as yes; but they are the fixed technical tiers of one architecture stack rather than areas of work or organizational units the model lets a system divide its work into, so part is also defensible and is given.

**C2: part (D: yes).** Quote (Table 3, §2.3.2, p. 32): "Table 3 specifies, for each type of agent, its group, its layer and its role", e.g. "Governor agent | Governance · L6 | Checks each plan against the signed policies, renders the authorization decision and its proof, logs; issues no token." Reason: each layer has a stated responsibility (a) and agent types are assigned to it (b), which supports yes; but the "roles" are agent types tied one-to-one to layers (in effect each layer is one kind of agent), so responsibility is stated per agent type rather than as positions in a unit, and part is given.

**C3: part.** Quote (Appendix 3 §3.3, Table 14, p. 114): "R performs, A approves and is accountable, C is consulted, I is informed." and below the table: "Two As on the same row signal a dual signature". Reason: the RACI matrix is a named artifact that gives an accountable role per activity, but some rows carry two As, so accountability is not exactly one per entry; the agentic registry (G.10, "Inventory of the authorized agents and MCP servers, kept by the AOM") names no owner per capability.

**C4: part.** Quote (G.1, Definitions): "A2A (Agent2Agent) — Protocol for horizontal cooperation between peer agents: it conveys intents rather than function calls, and its Agent Cards describe the capabilities of each agent." And (§2.3.1): "an agent negotiates only with its direct dependencies (negotiation scope)." Reason: agents can see other agents' capabilities through Agent Cards, but the model describes no lookup from a kind of work to the agent that handles it; peers are found through the dependency graph, and the agentic registry is an admission inventory, not a lookup service.

# 2. OperA

**Read:** the full PDF from maxapress (28 pages), extracted to text. Read closely: §3 (OperA model), §3.1 to §3.4.3 (organizational, social, interaction models, methodology), §5 to §5.3 (knowledge market worked example: Tables 1 to 5, groups, dependencies, social and interaction contracts). Skimmed §1, §2, §4. Figures 3 to 9 are images and their text did not extract.

**C1: part.** Quote (§3.1, p. 154): "The OM specifies an agent society in terms of four structures: social, interaction, normative and communicative. The social structure specifies objectives of the society, its roles and the model that governs coordination." Reason: the defined unit is the society (the whole system) and the model defines no way to hold several; groups of roles ("groups of roles were identified and group norms formalized in the group description", §5.1.3) and the "Non-life department" stakeholder appear only in the worked example and are sets of roles, not defined units of the model.

**C2: part (D: yes).** Quote (§3.1, p. 154): "The OM specifies the global objectives of the society and the means to achieve those objectives. ... The global objectives of an organization are represented in terms of objectives of the roles that compose the organization." Reason: rating the society, the OM states society-level objectives (a) and defines roles independently of the agents that enact them (b), which supports yes; but the same passage says those objectives are represented as role objectives, which the version 2 ruling excludes from (a), so part is given.

**C3: part.** Quote (§3.2, p. 154): "Agent populations of the OM are described in the SM in terms of commitments regulating the enactment of roles by individual agents." Reason: social contracts (and the notary's "Register agreements", Table 1, worked example) are records of commitments agents take on while the system runs, which the ruling rates part; the dependency diagrams name a target role "that handles the objective" (§5.1.3), but they are an example artifact and uniqueness is not stated.

**C4: part.** Quote (Table 1, §5.1.2, p. 162): "Matchmaker | Register participants, skills and needs | Accept and distribute exchange requests | Obliged to distribute requests". Reason: the matchmaker would meet the intermediary ruling, but it appears only in the knowledge-market worked example ("the role of matchmaker is also added to the facilitation layer of the knowledge market"); the model itself (§3) defines facilitation roles generically with no lookup, so the example caps the value at part.

# 3. ASOC manifesto

**Read:** arXiv HTML of 2607.12619 (converted to text). Read in full: §II-A (Table I), §IV (definition, four core concepts, Table III, reference architecture, three lenses, Table IV), §V principles 2 and 6 passages, §VI-A, §VI-C. Skimmed §I, §III, §VII, §VIII. Not read: most of §VI-B, §VI-D, §VI-E.

**C1: part.** Quote (§IV-A): "Agentic Service Ecosystem: A governed, heterogeneous collection of agentic services and conventional services that can be discovered, composed, orchestrated, and managed under shared policies, trust frameworks, and interoperability standards." Reason: the only defined unit above the agent is the ecosystem, which is the whole system; organizations appear as delegators ("a human or organisation delegates a goal") but are not defined.

**C2: part.** Quote (§IV-A): "Delegation Contract: A formal specification of the scope, authority, constraints, duration, revocability, and accountability conditions under which a human or organisation delegates a goal to an agentic service." Reason: scope and accountability are specified per agentic service (a per-agent contract), and the ecosystem has only "shared policies"; no unit-level objectives or roles are given.

**C3: part.** Quote (§IV-A): "ASOC should produce a family of engineering artefacts ... agentic capability contracts, delegation contracts, agent harnesses, agent provenance graphs, agentic service registries, ..." Reason: delegation contracts are a record of obligations agents take on (part under the ruling); the registry is named as a future artifact with no stated content, and no record assigns one accountable owner per capability.

**C4: part.** Quote (§II-A): "In ASOC, discovery must work at the goal level: an orchestrating agent must find, assess, and bind to agentic services whose capabilities match a specified goal, not merely a typed interface." Reason: this is a lookup from a kind of work, but it is stated as a requirement ("must"), with "agent registry and marketplace" only listed as a realization mechanism (§V) and no mechanism described, so the rule caps it at part.

# 4. Microsoft Multi-Agent Reference Architecture

**Read:** repository at commit adbefc1 (the current HEAD, 2026-10-27) via `gh api`: Agent-Registry.md, Reference-Architecture.md, Patterns.md (patterns 1, 2, 5 to 9), Building-Blocks.md, Introduction.md; grepped Agents-Orchestration.md and Governance.md. Not read: memory, communication, versioning, evaluation, security, design-options pages.

**C1: part.** Quote (Reference-Architecture.md, Supervisor Agent, recommended practices): "Introduce agent supervisors as the architecture scales across domains—these components help manage and abstract groups of related agents. Use hierarchical organization (e.g., supervisor → agent group)". Reason: agent groups and domains are mentioned, but no group unit is defined; "domain" is defined per agent ("Each agent focuses on a particular domain (e.g., finance, healthcare, coding)"), which is the same thing as one agent.

**C2: part.** Quote (Introduction.md, Separation of Concerns): "In multi-agent systems, it's essential that each agent has a distinct and well-defined responsibility." Reason: responsibilities are specified per agent, not per unit, which the criterion rates part.

**C3: part.** Quote (Building-Blocks.md): "`Agents registry` serves as a centralized data service and source of truth for managing all specialized agents ... cataloging each agent's identity, capabilities, operational status, version, and metadata tags." Reason: the registry records capabilities per agent (and optional `owners` metadata "for human consumption", Agent-Registry.md), but accountability is not stated and a capability can map to several agents.

**C4: part (D: yes).** Quote (Agent-Registry.md): "The primary goal of an agent registry is to provide an information repository for the agents in the system to know how to communicate with one another. In most cases though, in an Orchestrator-based multi-agent architecture, the registry enables the Orchestrator Agent to query which agents are best to carry the immediate tasks at hand." Reason: the registry is a defined element answering from registered capabilities with endpoints ("Query-optimized schema for capability lookups", Reference-Architecture.md), and the first sentence opens it to all agents, which supports yes; but the architecture routes all lookups through the single orchestrator and classifier (Building-Blocks.md: "managing all specialized agents available in the system for the orchestrator"; "route all communication through the orchestrator"), which the ruling rates part.

# 5. Horling and Lesser survey

**Read:** the PDF from the posomas.isse.de link (36 pages, dated May 2005 on its title page), extracted to text. Read closely: §2 Hierarchies (intro, 2.1), §3 Holarchies (intro, 3.1), §7 Societies (intro and the passage on facilitation roles), §8 Federations (all), §10 Matrix organizations (intro, 10.1), §12 Other organizational topics (items 1 to 3). Not read: §4 to §6, §9, §11, §13 beyond the summary table row. Per the criteria, I rated the paradigms the survey itself describes and name the paradigm in each quote.

**C1: yes.** Quote (§3, Holarchies, p. 5): "The defining characteristic of a holarchy is the partially-autonomous holon. Each holon is composed of one or more subordinate entities, and can be a member of one or more superordinate holons." and "Enterprises, companies, divisions, working groups and individuals can each be viewed as a holons taking part in a larger holarchy." Reason: the holon is a defined unit with stated properties, holds several members, and nests within and beside other holons.

**C2: part.** Quote (§2, Hierarchies, p. 3): "Multi-divisional hierarchies further exploit localization by dividing the organization along product lines ... Each division has complete control over their product". Reason: unit-level scope is given (a division owns a product line; holons receive "capabilities ... instead of individual agents"), and the federation defines a delegate position per group, but no paradigm specifies both a unit's responsibility and the roles inside it.

**C3: part.** Quote (§8, Federations, p. 16): "Agents connecting to the system start by sending their capabilities to the local facilitator. ... Each facilitator provides a yellow pages function which supports this search." Reason: the facilitator holds a record of capabilities per agent, but it names providers, not one accountable owner; the matrix grid ("a check is used to denote where an authority relationship exists", §10) records several managers per agent.

**C4: yes.** Quote (§8, Federations, p. 15 to 16): "Typically, the intermediate accepts skill and need descriptions from the local agents, which it uses to match with requests from intermediaries representing other groups." and "Needs are similarly routed to the facilitator, which then attempts to find other facilitators that can service that need." Reason: the facilitator is a defined element of the federation paradigm, every member agent can send it needs, and it answers from registered capabilities and forwards the request, which meets the intermediary ruling; it is one per group, not a single system orchestrator.

# 6. FIPA Agent Management Specification SC00023K

**Read:** the provided text extraction of the 2015 Wayback capture (`scratchpad/src/fipa-SC00023K-text.txt`): §1, §2 (reference model), §3 (naming, name resolution), §4.1.1 to 4.1.3 (DF overview, functions, federation), §6.1.2 and §6.1.3 (df-agent-description, service-description). Searched the full text for domain, organisation, ownership, owner, group, role. Not read: §4.2 AMS detail, §5 lifecycle, §6.2 onward beyond the frames above.

**C1: no (D: part).** Searched for: domain, organisation/organization, group, department, role as a unit. Found only (§2): "An agent must have at least one owner, for example, based on organisational affiliation or human user ownership". The Agent Platform is defined, but as infrastructure ("The AP provides the physical infrastructure in which agents can be deployed"), not as an area of work. Reason: no unit of work or organization is in the model; "organisational affiliation" is a single passing mention, which could be read as an undefined mention (part), so the cell is DISPUTABLE.

**C2: no.** Searched for unit-level responsibility, objectives, roles or positions; none, since no unit exists (C1). The AID may carry "roles, etc." (§3), but that is per agent and undefined.

**C3: part.** Quote (§6.1.3, Service Description frame): "ownership | The owner of the service | Optional | string". Reason: the DF directory records an owner per registered service, but the field is optional, accountability is not stated, and §4.1.1 says "There is no intended future commitment or obligation on the part of the registering agent implied in the act of registering."

**C4: yes.** Quote (§2): "The DF provides yellow pages services to other agents. Agents may register their services with the DF or query the DF to find out what services are offered by other agents". Reason: the DF is a defined component that any authorized agent may search by service description, and it returns agent descriptions whose AIDs carry transport addresses (§3), so it answers from registered capabilities with how to reach the handler.

# 7. Electronic institutions: ISLANDER and AMELI

**Read:** Esteva et al., AMELI (AAMAS 2004), local PDF, all 8 pages extracted: §2 to §5.2 closely (scene and performative structure definitions, execution state, AMELI agents, Table 2). Huget et al., Model Checking Electronic Institutions, §1 and §2 in full (ISLANDER elements, BNF in Figure 1). The ISLANDER article (AAMAS 2002) could not be opened: the search found only the ACM DOI 10.1145/545056.545069 and Unpaywall lists no open copy.

**C1: part.** Quote (Huget et al., §2): "An electronic institution is composed of four elements: a dialogical framework, scenes, performatives structure and norms." Reason: the institution is the only defined unit and the texts define no way to have several; scenes are "agent group meetings" (activities), which the version 2 ruling excludes from areas of work.

**C2: part.** Quote (Huget et al., §2): "the dialogic framework defines which will be the participant roles in the institution and the relationships among them. Each role defines a pattern of behaviour within the institution". Reason: rating the institution, roles are defined independently of the agents (b), but the specification (`ins-def` in Figure 1: dialogic framework, performative structure, norms) states no objective or mission for the institution (a).

**C3: part.** Quote (AMELI §3): "Obl = {⟨ag, ι, s⟩ | ag ∈ Ag, ι ∈ CL(s), s ∈ S} is the set of pending obligations (where ⟨ag, ι, s⟩ stands for the obligation of agent ag to utter illocution ι at scene s)." Reason: the execution state keeps a record of obligations agents acquire at run time, which the ruling rates part; there is no record mapping a capability to one accountable owner.

**C4: part.** Quote (AMELI Table 2): "scenePlayers | Ask for agents in a scene" and "accesScenes | Ask for the scenes the agent can join from a transition". Reason: an agent can discover other agents (by scene) through its governor, but not from a kind of work; movement between scenes is routed by role inside the performative structure.

# 8. JaCaMo

**Read:** The Science of Computer Programming article could not be opened (sciencedirect.com returned HTTP 403). Read instead: the Moise specification source `doc/specification/moise-spec.tex` from github.com/moise-lang/moise (the TeX source of moise-spec.pdf; §1 Organisation Model (section title), all subsections through Organisation Entity (section title); section headings of §2 OML Semantics), `doc/ora4mas/readme.adoc` in full, and the class descriptions of the API pages for GroupBoard, SchemeBoard and OrgBoard. Not read: NormativeBoard page, §2 NOPL details, jacamo-lang.github.io.

**C1: yes.** Quote (moise-spec, Definition GI): "A Group Instance (GI) is defined by ... ⟨id, GS, players, subgroups, RS⟩ where ... players : R → 2^A is function that maps each available role in the corresponding GS to the set of agents that are playing that role; subgroups ... maps each groups specification to a set of group instances". Reason: the group is a defined element, holds several agents and roles, and nests subgroups, with several group instances per organization entity.

**C2: yes.** Quote (moise-spec, Definition GI): "RS : 2^SI is a set of schemes' identification the group is responsible for." and (Definition GS): "maxrp : R → Z: is a function that maps each role to the maximum number of players of that role in the group". Reason: at group level the model states what the group is responsible for (schemes, each with a root goal, Definition Scheme Specification) and the roles agents fill, defined apart from agents. Note: the responsibility is bound to group instances at run time ("Add responsible group" action), not in the group specification.

**C3: part.** Quote (SchemeBoard API page): "groups: a list of groups responsible for the scheme." and "commitment(ag,mission,sch): agent ag is committed to the mission in the scheme". Reason: the SchemeBoard and GroupBoard hold run-time records of responsibility and commitment, but a scheme carries a list of responsible groups and a mission maps to a set of agents ("commitments : M → 2^A"), so the record is not one owner per entry.

**C4: part (D: yes).** Quote (SchemeBoard API page): "goalState(schId, goal, list of committed agents, list of agents that performed the goal, state)". Reason: any agent focusing on the organizational artifacts can read, from a goal or mission, which agents are committed to it (and the GroupBoard's `play(ag,role,group)` maps roles to agents), which supports yes; but the source presents these as observable organizational state for coordination, not as a lookup service for sending work, and states no reach information beyond the agent name, so part is given.

# Disclosures and what I could not open

- I did not open any other file under `` beyond the two named inputs, and no file whose name starts with `rerate-v2-reader`. No search or grep printed content from such a file.
- In the scratchpad `src/` folder I listed the files (including `fipa01.*`, `fipa23.*`, `j3.html`, `j5.json`, `j6.json`, `oa.json`, `core.json`) but read only `fipa-SC00023K-text.txt`, `ameli.pdf` and `huget-model-checking-EI.pdf`.
- Could not open: the ISLANDER article (AAMAS 2002; no open copy found), and the JaCaMo article in Science of Computer Programming (HTTP 403). I rated JaCaMo from the Moise specification, the ORA4MAS readme and the API pages.
- The arXiv abstract page lists AAM/5C at 120 pages; the PDF has 195 pages. I read the sections listed above, not the whole book.
- PDF text was extracted with pypdf installed into a scratchpad virtual environment; figures (OperA Figures 3 to 9, AAM/5C figures) did not extract and were not rated.
- The Horling and Lesser PDF at the given link is dated May 2005 on its title page, not 2004.

# Addendum: JaCaMo re-checked against the 2013 article

**Read:** Boissier, Bordini, Hübner, Ricci and Santi, "Multi-agent oriented programming with JaCaMo", Science of Computer Programming 78 (2013) 747-761, both local PDFs read whole (printed pages 747 to 761): §1, §2, §3 (meta-model, synergies), §4 (platform, organisational artifacts, Building-a-House example), §5 (applications), §6. Same frozen criteria and isolation rules as above; the other seven rows are unchanged.

| | Before | After |
|---|---|---|
| C1 | yes | yes (stays) |
| C2 | yes | part (D: yes) (changes) |
| C3 | part | part (stays) |
| C4 | part (D: yes) | part (D: yes) (stays) |
| Directory (derived) | part | part (stays) |

**C1: stays yes.** Quote (§3.1, p. 751): "on the organisational side, on the basis of Moise, an organisation is described: (i) from a structural point of view, in terms of group and role entities". And (§4, p. 754): "GroupBoard artefacts, used to manage the life-cycle of specific groups of agents". Reason: the group is a named element of the programming meta-model that several agents and roles belong to, with one GroupBoard per group (and several groups side by side in the §5 applications, Fig. 7), so the earlier value holds.

**C2: changes from yes to part (D: yes).** Quote (§3.2, p. 753): "goals defined at the organisation dimension (those goals that are to be achieved by the organisation, i.e., the overall system) are mapped into individual agent goals". And (§3.1, p. 751): "norms which bind roles to missions, constraining an agent's behaviour as regards sets of goals that it will have to achieve when it chooses to enter a group and play a certain role in it." Reason: the article defines roles inside groups independently of agents (b), but states goals only for the organisation as a whole and responsibilities per role through norms; its text never says what a group is responsible for, which the version 2 ruling requires for (a), so the article supports part. The Moise specification read earlier ("RS ... a set of schemes' identification the group is responsible for") and the "Schemes" property on the GroupBoard in Fig. 3 (p. 753) still make yes defensible, so the cell is DISPUTABLE.

**C3: stays part.** Quote (§3.2, p. 753): "The state of goals from the organisation dimension (which agents should fulfil them and when) is maintained by an organisational artefact and is displayed as obligations for the agents". Reason: the SchemeBoard keeps a run-time record of obligations agents take on, which the ruling rates part; the article describes no record that names exactly one accountable owner per responsibility.

**C4: stays part (D: yes).** Quote (§4, p. 754): "the GroupBoard artefact has an observable property concerning the available roles in a group; therefore agents can find out which are the existing roles and then reason about them so as to autonomously decide whether to adopt a role or not." And (§4.1.1, p. 755): "the agent first joins the workspace, retrieves the unique identifier of the artefact with the specified name (lookupArtifact action)". Reason: the article shows discovery of roles and of artifacts by name, not a lookup from a kind of work to the agent that handles it, so on the article alone the value is part. The higher value still rests only on the SchemeBoard API page read earlier (`goalState(... list of committed agents ...)`), which the article does not describe; I keep the DISPUTABLE marking for that reason.

DISPUTABLE cells across the whole file after this addendum: 7 (was 6; JaCaMo C2 is added).

# Addendum 2: ISLANDER and AMELI re-checked against the 2002 ISLANDER article

**Read:** Esteva, de la Cruz and Sierra, "ISLANDER: an electronic institutions editor", AAMAS 2002, pp. 1045-1052, local PDF read whole (8 PDF pages): §1 to §8. Same frozen criteria and isolation rules as above; row 7 is still rated as one source (ISLANDER together with AMELI and Huget et al.), and the other rows are unchanged.

| | Before | After |
|---|---|---|
| C1 | part | part (stays) |
| C2 | part | part (stays) |
| C3 | part | part (stays) |
| C4 | part | part (stays) |
| Directory (derived) | part | part (stays) |

**C1: stays part.** Quote (§3, PDF page 3): "an electronic institution is specified by a dialogic framework which determines the valid illocutions and the participant roles, a performative structure which describes the activities within the institution, and a set of norms that govern the institution." Reason: the institution is the only unit the model defines, and the article gives no way for a system to hold several; scenes are "agent group meetings" for one "dialogic activity" (§2, PDF page 2), which the version 2 ruling excludes from areas of work, and organisations are mentioned only as a "broader context" (§2, PDF page 2), not defined.

**C2: stays part.** Quote (§2, PDF page 2): "the dialogic framework defines which will be the participant roles in the institution and the relationships among them. Each role defines a pattern of behaviour within the institution and any agent within an institution is required to adopt some of them." Reason: roles are defined at the institution level independently of the agents (b, including internal roles for "staff agents"), but neither the article's prose nor its `ins-def` grammar (Figure 1, PDF page 3) states what the institution as a whole is for or must achieve (a).

**C3: stays part.** Quote (§2, PDF page 3): "the institution does know the obligations that each agent has acquired and can thus detect when an agent does not fulfil its obligations and hence violates the norms." Reason: the institution keeps a run-time record of obligations agents acquire ("Both types of consequences will need to be kept by an institution for each agent on an individual basis", §2, PDF page 2), which the ruling rates part; there is no record that names one accountable owner per responsibility or capability.

**C4: stays part.** Quote (§2, PDF page 2): "Transitions can be seen as a type of routers in the context of a performative structure." And (§7, PDF page 7), on governors as planned future work: "the agent only communicates with its governor which is responsible to transmit its messages to the corresponding agents." Reason: the article routes agents between scenes by role and has governors forward messages, but it describes no lookup from a kind of work to the agent that handles it. On its own the article would support no rather than part, because it gives agents no way to discover other agents. The row keeps part because AMELI's `scenePlayers` information request ("Ask for agents in a scene", Table 2), read earlier, still lets an agent discover other agents. This does not change the value, so the cell is not marked DISPUTABLE.

DISPUTABLE cells across the whole file after this addendum: 7 (unchanged from Addendum 1).
