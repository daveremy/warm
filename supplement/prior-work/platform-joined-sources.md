---
log_id: "2026-11-12-1221-56-warm-paper-jacamo-islander-ameli-and-fipa-director"
title: "JaCaMo, ISLANDER/AMELI and FIPA's Directory Facilitator, read against the paper's prior-work claims"
date: 2026-11-12
author: sagan
status: "sagan's reading; the same three works were then rated by two independent readers (rerate-v2-comparison.md). Updated 12:39 after the author supplied the JaCaMo article"
---

# Result

The three works change one claim of the paper and leave the others standing.

1. **Section 2.4, "the reading did not find in them a platform of services of the kind in Section 4.6", must be withdrawn for the literature as a whole.** It is true of the five sources that section cites. It is false for the period. FIPA (2002 to 2004) standardizes an agent platform as a set of services. AMELI (2004) is a domain-independent middleware that mediates every interaction and enforces an institution's rules. JaCaMo (2013) puts an organization model, an agent runtime and a shared environment in one development platform and holds the organization's state in infrastructure that agents observe.
2. **"Joining" is not a difference from prior work.** Section 6 says the model "joins" the organizational idea "to a list of platform services". JaCaMo and ISLANDER with AMELI each joined an organizational specification to execution infrastructure. What remains is narrower: none of the three gives each area one accountable owner per responsibility, and none lists platform services for agents built on language models.
3. **The C3 result holds.** None of the three has a record that names one accountable area for each responsibility. All three rate "part". FIPA states the opposite of accountability for its directory entries.
4. **C4 gains one full rating.** FIPA's Directory Facilitator is a lookup from a kind of service to the agent that offers it and its address. It is the direct precedent for the model's Directory lookup and the paper does not cite it.
5. **JaCaMo claims the join itself.** Its authors call it "the first successful combination" of agent, organization and environment programming in one platform (p. 749).
6. **One lead not read** bears on C3: an extension of Moise "with exception and accountability" (Baldoni, Baroglio, Micalizio and Tedeschi), named on the JaCaMo site's front page.

# What was read

| Work | Read | Not read |
|---|---|---|
| AMELI | Esteva, Rosell, Rodríguez-Aguilar and Arcos, "AMELI: An Agent-based Middleware for Electronic Institutions", AAMAS 2004, pp. 236-243. Full text, 8 pages. https://www.iiia.csic.es/media/filer_public/b8/a0/b8a0f2a8-6ab7-49af-a6b8-597b95af9c18/iiia-2004-896.pdf | |
| ISLANDER | Section 2 of Huget, Esteva, Phelps, Sierra and Wooldridge, "Model Checking Electronic Institutions" (IIIA report 2002-595), which describes the ISLANDER framework and gives its grammar; two of its authors wrote ISLANDER. Also Section 2 of the AMELI paper. https://www.iiia.csic.es/media/filer_public/67/71/6771e721-f0a8-4aa4-a4e8-32da6a0ba389/iiia-2002-595.pdf | Added 12:40: Esteva, de la Cruz and Sierra, "ISLANDER: an electronic institutions editor", AAMAS 2002, pp. 1045-1052 is now read (The author downloaded it). Its text layer is glyph-coded; I decoded it and searched it for roles, structure, obligations, infrastructure and directories, and did not read it page by page. Spaces in the quotes below are restored by hand. |
| FIPA | FIPA Agent Management Specification SC00023K, sections 2, 4.1, 4.2, 6.1.2, 6.1.3, 6.2.4.1. Wayback Machine capture of 2015 of http://www.fipa.org/specs/fipa00023/SC00023K.html (fipa.org refuses automated requests). The capture shows tracked changes from version J; one sentence on whether a DF is mandatory appears in both forms, and I quote only the reference-model wording. | FIPA Abstract Architecture SC00001L (downloaded, not read). |
| JaCaMo | Added 12:39: Boissier, Bordini, Hübner, Ricci and Santi, "Multi-agent oriented programming with JaCaMo", Science of Computer Programming 78(6), 747-761, 2013, pp. 748-754 and 759-760 (The author downloaded the publisher's open copy; not read: pp. 747, 755-758, 761). Before that: the project site (https://jacamo-lang.github.io/), the ORA4MAS reference in the Moise repository (`doc/ora4mas/readme.adoc`, github.com/moise-lang/moise), and the API descriptions of GroupBoard, SchemeBoard, OrgBoard and NormativeBoard (https://moise-lang.github.io/doc/api/ora4mas/nopl/). All are by the JaCaMo authors. | Hübner, Boissier, Kitio and Ricci, JAAMAS 2010 (ORA4MAS). The publisher's copy of the 2013 article refuses automated requests (curl and WebFetch 403, browser gate denies the domain); HAL and the Bologna repository hold no file. |

[no-record: an open copy of the JaCaMo SCP 2013 article; searched=HAL emse-00680402, cris.unibo.it 11585/129893, OpenAlex locations, Semantic Scholar, Unpaywall, Wayback; instrument=curl and WebSearch, which did return the AMELI PDF]

# What each source states

## FIPA Agent Management (SC00023K)

- The platform is defined as services: "The entities contained in the reference model (see Figure 1) are logical capability sets (that is, services) and do not imply any physical configuration." (section 2)
- "An Agent Platform (AP) provides the physical infrastructure in which agents can be deployed. The AP consists of the machine(s), operating system, agent support software, FIPA agent management components (DF, AMS and MTS) and agents." (section 2)
- Directory by service: "The DF provides yellow pages services to other agents. Agents may register their services with the DF or query the DF to find out what services are offered by other agents". (section 2)
- Identity and lifecycle: "The AMS exerts supervisory control over access to and use of the AP. Only one AMS will exist in a single AP. The AMS maintains a directory of AIDs which contain transport addresses (amongst other things) for agents registered with the AP. The AMS offers white pages services to other agents." (section 2). The AMS "is responsible for managing the operation of an AP, such as the creation of agents, the deletion of agents" and "has the authority to forcibly enforce the function if such a request is ignored." (section 4.2.1)
- The record: `df-agent-description` has `name` ("The identifier of the agent"), `services` ("A list of services supported by this agent"), protocols, ontologies, languages, lease-time and scope (6.1.2). `service-description` has `name`, `type`, and `ownership` ("The owner of the service", optional string) (6.1.3).
- No accountability: "There is no intended future commitment or obligation on the part of the registering agent implied in the act of registering. For example, an agent can refuse a request for a service which is advertised through a DF." (4.1.1)
- Lookup: search takes "an object template"; a registered object matches if "Each parameter of the object template is matched by a parameter of the object description." (6.2.4.1). Federation: "The DF encompasses a search mechanism that searches first locally and then extends the search to other DFs, if allowed." (4.1.3)
- Organizational unit: none. The only mention is that "An agent must have at least one owner, for example, based on organisational affiliation or human user ownership". (section 2)

Ratings: C1 **no**. C2 **no**. C3 **part** (an owner per service per agent; the spec says registering implies no obligation). C4 **yes** (from a service type or name to the agent's identifier, which carries its transport addresses). Directory (derived): part.

Platform services it has, in the paper's terms: Lifecycle (AMS), Identity (agent identifiers), Registry and Directory (AMS white pages, DF yellow pages), Messaging (Message Transport Service).

## ISLANDER and AMELI

- The specification: "An electronic institution is composed of four elements: a dialogical framework, scenes, performatives structure and norms." (Huget et al., PDF p. 1). The dialogic framework "defines which will be the participant roles in the institution and the relationships among them. Each role defines a pattern of behaviour within the institution" (PDF pp. 2-3).
- Roles apart from agents: "We consider the protocol of each scene to model the possible dialogic interactions between roles instead of agents." (Huget et al., PDF p. 3)
- Staff: "The internal roles can only be played by what we call staff agents, that is the agents that pertain to the institution. We can see them as the electronic version of the workers in human institutions." (Huget et al., PDF p. 3)
- The platform: AMELI is "an infrastructure that mediates agents' interactions while enforcing institutional rules. An innovative feature of AMELI is that it is of general purpose (it can interpret any institution specification), and therefore it can be regarded as domain-independent." (AMELI, abstract)
- Three layers: "External agent layer", "Social layer (AMELI). Implementation of the control functionality of the institution infrastructure", and "Communication layer. In charge of providing a reliable and orderly transport service." (AMELI, PDF pp. 4-5)
- Mediation and enforcement: "participating agents in the institution do not interact directly; they have their interactions mediated by AMELI"; AMELI guarantees "the correct evolution of each scene execution (preventing errors made by the participating agents by filtering erroneous illocutions, thus protecting the institution)". (AMELI, PDF p. 5)
- Entry as a governed act, at run time: the Institution Manager "is in charge of starting an EI, authorising agents to enter the institution"; "Scene managers are also in charge of authorising agents to join [operation join] or leave [operation leave] scene executions." (AMELI, PDF pp. 5-6)
- The record: the execution state includes "Obl = {⟨ag, ι, s⟩ ...} the set of pending obligations (where ⟨ag, ι, s⟩ stands for the obligation of agent ag to utter illocution ι at scene s)" (AMELI, PDF p. 3); "Governors continuously keep the pending obligations of their assigned agents" (PDF p. 7).
- What an agent can ask: Table 2 lists "agentObligations: Ask for pending obligations", "scenePlayers: Ask for agents in a scene", "accesScenes: Ask for the scenes the agent can join from a transition" (AMELI, PDF p. 6).
- The authors' own claim in 2004: "although further agent research has focused on the introduction of social concepts such as organisations or institutions (e.g. [8],[3],[10]), there is no infrastructure supporting their computational realisation." (AMELI, PDF p. 8; [3] is Dignum's OperA thesis)

From the 2002 ISLANDER article (added after the first reading):

- "We distinguish between two types of roles, the internal and external roles. The internal roles can only be played by what we call staff agents which are the agents that pertain to the institution." (PDF p. 2)
- The record is per agent: "Both types of consequences will need to be kept by an institution for each agent on an individual basis." (PDF p. 2)
- Obligations are known, not forced: "the institutions cannot force agents to fulfil their obligations. However, the institution does know the obligations that each agent has acquired and can thus detect when an agent does not fulfil its obligations" (PDF p. 3).
- Mediation was planned in 2002: "Each participating agent is connected to a governor who mediates between it and the rest of the agents." (PDF p. 7)
- A search of the article found no directory, no unit inside an institution other than scenes, and no statement of what an institution is responsible for.

Under criteria version 2 both independent readers rate C1 **part**, because the institution is the whole system; my **yes** below was given under version 1.

Ratings: C1 **yes** (the institution is a defined unit with roles that many agents play; its inner units, scenes, are activities and not areas of work). C2 **part** (roles are specified for the institution and each scene; what the institution or a scene is responsible for is not stated, and obligations arise per agent from norms). C3 **part** (a record of pending obligations per agent, not of one accountable area per responsibility). C4 **part** (an agent can ask who is in a scene and which scenes it can join; the lookup is not from a kind of work). Directory (derived): part.

Platform services it has, in the paper's terms: Policy enforcement at each agent's boundary (one governor per agent), admission, Messaging, Orchestration of movement between activities (transition managers), and monitoring (Figure 4).

## JaCaMo

From the 2013 article (printed page numbers):

- The system: "A JaCaMo multi-agent system (i.e., a software system programmed in JaCaMo) is given by an agent organisation programmed in Moise, organising autonomous agents programmed in Jason, working in shared distributed artefact-based environments programmed in CArtAgO" (p. 750).
- The authors' own claim: "to the best of our knowledge, JaCaMo is the first approach aimed at explicitly investigating the integration of all these dimensions from a design and programming point of view: existing approaches consider either only the agent–organisation dimensions or the agent–environment dimensions." (p. 749)
- Against modelling services as agents: in other platforms "typically low-level workarounds are used (such as modelling everything as an agent, even environment or organisational abstractions)" (p. 749).
- The organization: "an organisation is described: (i) from a structural point of view, in terms of group and role entities; (ii) from a functional point of view, in terms of social scheme, mission, and goal entities [...] and (iii) from a normative point of view, in terms of norms which bind roles to missions" (p. 751).
- Infrastructure services: predefined actions "refer to the basic functionalities provided by the overall infrastructure, including the environment and organisation dimensions. This makes it possible in particular to avoid the introduction of ad hoc specific mechanisms for exploiting infrastructure services concerning organisation and coordination, for instance to adopt a role or to interact with a tuple space." (p. 752)
- Organization state held outside the agents: "the different concrete computational entities aimed at managing, outside the agents, the current state of the organisation in terms of groups, social schemes, and normative state are reified in the environment by means of organisational artefacts" (p. 752).
- The record of who must do what: "The state of goals from the organisation dimension (which agents should fulfil them and when) is maintained by an organisational artefact and is displayed as obligations for the agents (e.g., agent a is obliged to fulfil goal x in one week)." The goals are "those goals that are to be achieved by the organisation, i.e., the overall system". (p. 753)
- Autonomy kept: "besides being free to adopt or not the goals from the organisation, the agent is also free to decide which courses of action should be used to achieve each goal" (p. 753).
- Lookup: "the GroupBoard artefact has an observable property concerning the available roles in a group; therefore agents can find out which are the existing roles and then reason about them so as to autonomously decide whether to adopt a role or not." (p. 754)
- Three levels in Figure 3: conceptual, execution and platform; "each infrastructure node integrates the Jason, CArtAgO, and Moise platforms" (pp. 753-754).

The article does not change the four ratings below. It ties the organization's goals to "the overall system" and binds roles to missions by norms, which supports C2 part with yes as the alternative. It has no directory by kind of work.

From the project's documentation (read before the article arrived):

- "The JaCaMo project aims to promote the Multi-Agent Oriented Programming (MAOP) approach by providing a development platform that integrates tools and languages for programming the following dimensions of Multi-Agent Systems: agents, environment, and organisation." (jacamo-lang.github.io)
- Organization management as infrastructure, not as an agent: the current approach implements the "OMI (Organisation Management Infrastructure): based on a normative language and artifacts." The earlier S-MOISE "adds an organisational layer on top of the communication layer" and was "centralised due a component called OrgManager". (ORA4MAS reference)
- GroupBoard: "Artifact to manage a group instance." Operations: adoptRole, leaveRole, addScheme, removeScheme. Observable properties: "play(ag,role,group): agent ag is playing the role in the group"; "schemes: a list of schemes identification the group is responsible for"; "subgroups"; "formationStatus: whether the group is well-formed". (GroupBoard API)
- SchemeBoard: "Artifact to manage a scheme instance." Observable properties: "commitment(ag,mission,sch): agent ag is committed to the mission in the scheme"; "groups: a list of groups responsible for the scheme"; "goalState(schId, goal, list of committed agents, list of agents that performed the goal, state)"; "obligation(ag,reason,goal,deadline): current active obligations". (SchemeBoard API)
- OrgBoard: "Artifact that manages an organizational entity (its groups, schemes, ....)". (OrgBoard API)
- Agents read this state: "Observable properties of the artifacts (which are Java objects) are mapped to the beliefs inside agents by Cartago-Jason bridge." (ORA4MAS reference)

Ratings: C1 **yes** (group, with subgroups and roles). C2 **part**, DISPUTABLE (**yes**): roles belong to the group specification, and a group instance is "responsible for" schemes, but the documentation read shows that link made at run time (addScheme) and I did not read how it is specified. C3 **part** (the scheme artifact records the groups responsible for a scheme and the agents obligated to each goal; it is "a list of groups", so not one accountable area). C4 **part**, DISPUTABLE (**yes**): an agent can look up, from a goal in a running scheme, the agents committed to it, and from a role, who plays it; the lookup is from a goal instance and not from a kind of work in general. Directory (derived): part.

This is the nearest prior record to the model's directory found so far: a record held by the platform, readable by every agent at run time, of which group is responsible for which work and which agent is obligated to which goal.

# Effect on the paper (draft 4)

| Place | Draft 4 says | Change |
|---|---|---|
| 2.4, after the five sources | "Their facilitation services are roles played by agents, and the reading did not find in them a platform of services of the kind in Section 4.6." | Keep the first half for those five. Replace the second half: the same literature has platforms. Cite FIPA's agent platform (lifecycle, naming, white and yellow pages, message transport), AMELI (a domain-independent middleware that mediates and enforces) and JaCaMo (organization, agents and environment in one platform, with the organization's state in infrastructure). |
| 2.3, last sentence | "WARM differs from these sources mainly in joining the platform, the domains of work and the agents in one model." | True of the seventeen sources of 2.3. Add that the join itself is older (2.4). |
| 5.3 | Counts across 27 sources: C1 7, C2 2, C4 6, C3 none undisputed. | With these three, across 30: C1 9, C2 2, C4 7, C3 still none. With every higher alternative: C1 13, C2 8, C3 3, C4 12. (Single reader; confirm at the re-rate.) |
| 5.3, "The nearest are records of an owner for each agent or asset, a provider for each capability, or obligations for each role." | | Add JaCaMo's scheme artifact (groups responsible for a scheme, agents obligated to each goal) and note that FIPA's directory disclaims any obligation. |
| 4.6 Directory, and Table of precedents | No citation of FIPA. | Cite the Directory Facilitator as the precedent for lookup by kind of service, and the AMS for the registry of agents. |
| 6, "joins it to a list of platform services" | | Narrow: the join has precedents in JaCaMo and in ISLANDER with AMELI; what the model adds is the list of services for agents built on language models and one accountable area per responsibility. |
| 6, "entry to a unit as a governed act" | Listed as material not yet used. | AMELI enforces it at run time (the institution manager and scene managers authorize entry). Cite. |
| 7, Work not done | "Three works ... were not read." | Replace with: read from the sources listed above by one reader; the JaCaMo and ISLANDER articles themselves were not opened; the accountability extension of Moise was not read. |
| 8 | "the platform side of WARM is mostly a consolidation of parts that are widely named" | Stands, and is stronger: the platform as a set of services is in FIPA. |

# Limits of this reading

- One reader, who knows the paper's claims. The four criteria were applied as frozen in `rerate-criteria.md`; no second rater has seen these three sources.
- JaCaMo was first rated from documentation and API descriptions; the 2013 article was read afterward (pp. 748-754, 759-760) and did not change the ratings. The 2020 book was not read.
- ISLANDER was first rated from two papers by its authors that summarize it; the 2002 article was searched afterward and changed nothing.
- I did not search for other work of this kind (for example THOMAS, S-MOISE+ or the JADE platform).
