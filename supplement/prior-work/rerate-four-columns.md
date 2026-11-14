---
title: "Independent re-rating of 17 sources on four criteria (C1 to C4)"
date: 2026-11-12
author: "independent rater (subagent)"
status: "not yet checked by sagan"
---

# Independent re-rating of 17 sources on four criteria

Criteria applied: `prior-work/rerate-criteria.md` (frozen 07:45, read in full, applied as written). I did not open any excluded file (`source-by-part-grid.md`, `directory-column-rule.md`, `coverage-matrix.md`, `synthesis.md`, `synthesis-round2.md`, `second-rater.md`, `autonomy-check.md`, `platform-mapping/mapping.md`, `platform-mapping/spot-check.md`, `paper/`, `PROGRESS.md`, any `warm-model-*.md`). One disclosure: a keyword grep over `prior-work/charterion-full.md` printed lines 18 and 19 of its Summary table, which state that earlier reader's verdicts on Charterion. I did not use them, and every Charterion cell below rests on the Charterion PDF or on item rows from that file's §1.

Rule followed throughout: where two values were defensible, the cell carries the LOWER value and is marked DISPUTABLE with the higher one.

## 1. Values

| # | Source | C1 area exists | C2 area specified | C3 accountability record | C4 finding where to send work | Directory (derived) |
|---|---|---|---|---|---|---|
| 1 | Yu, Rabhi, Zhu, Lu | no | no | no | part | part |
| 2 | Zhu, Fluid Structure | part | part | no (D: part) | part | part |
| 3 | Goujon, AAM/5C | part (D: yes) | part (D: yes) | part (D: yes) | part | part |
| 4 | Microsoft MARA | part | part | part | yes | part |
| 5 | AWS Prescriptive Guidance | part | part | part | part (D: yes) | part |
| 6 | Google Cloud Arch. Center | part (D: yes) | part | no | part | part |
| 7 | Charterion v2.0 | yes | part (D: yes) | part | no (D: part) | part |
| 8 | AEON | yes | part | part (D: yes) | yes | part |
| 9 | CEAD | part (D: yes) | part | part (D: yes) | part | part |
| 10 | Salesforce, Agentic Enterprise | part | no | part | part (D: yes) | part |
| 11 | AOS-0001 / AOS-0000 | no (D: part) | no (D: part) | part | yes | part |
| 12 | Steinder and Franke (IBM) | no | no (D: part) | no | no (D: part) | no |
| 13 | ASOC manifesto | no | part | no | part (D: yes) | part |
| 14 | EAAF | part | no (D: part) | no | part | part |
| 15 | Amazon Bedrock AgentCore | no | no | no (D: part) | yes | part |
| 16 | LangGraph + LangSmith (+ Deployment) | part (D: yes) | part | no | part | part |
| 17 | OpenClaw | part | part | part | part | part |

"D: x" means DISPUTABLE, higher value x. Directory is derived from the values given (lower values), per the criteria file.

## 2. Evidence per source

Location key: "primary" means I read the passage in the source itself (arXiv HTML or PDF text, Zenodo PDF, vendor page, or repository file) on 2026-11-12. "notes" means a quotation taken from an earlier reading note and checked against that note by script (section 7). For PDFs, page numbers are PDF page numbers of the file I extracted.

### 1. Yu, Rabhi, Zhu and Lu, arXiv:2610.14818 (primary: full arXiv HTML text, keyword search plus §IV and Table II read)

- **C1 no.** Searched the full text for domain, department, business unit, subdomain, organization, group, team, capability area. The only organizational use of "domain" is about the case study: "It covers one domain and one existing system" (§VII, limitations). The ten responsibilities L0 to L9 group capabilities by architectural purpose, not areas of work. Primary.
- **C2 no.** Ownership is a design-time concern of L0, not a property of an area: L0 "establishes ownership, accountability, risk, and regulatory requirements that constrain decisions elsewhere, rather than acting as a runtime step" (§IV-B). Primary.
- **C3 no.** Same search plus owner, registry, catalog. No record assigns an owner to a responsibility or capability; "ownership" in the paper means which architectural responsibility owns a decision (for example "L3 owns execution coordination", §IV-A). Primary.
- **C4 part.** Agent discovery is a conditional capability: when there are "Multiple collaborating agents", "Enable L3 agent collaboration, discovery, and coordination interactions", realized by "Agent registry; A2A or direct calls" (Table II). No lookup from a kind of work is described. Primary.

### 2. Zhu, "Fluid Structure, Rigid Record", arXiv:2608.08516 (primary: full arXiv HTML text, keyword search plus §3.2, §3.4, §4)

- **C1 part.** The groupings are a temporary Task Group (a team built for one task) and three Role Groups that are authority profiles, explicitly not areas of work: "the domain does not confer the power. The three groups are fixed constitutional categories even though every Task Group is temporary." (§4). Primary.
- **C2 part.** Specification is per resident agent specification: "A resident entry is a reusable specification, not a permanently busy digital employee." (§3.2), which then binds a domain specialization, tools, skills and default P&P templates. Role Groups carry authority profiles but no area responsibilities. Primary.
- **C3 no. DISPUTABLE: part.** The Log records "accepted events, authority use, lineage, handoff and decision records" so as to "replay state and reconstruct accountability" (Table 2). That names who acted per event, not an owner per responsibility, agent or asset. A reader who counts per-event authority records as naming a responsible party would give part. Primary.
- **C4 part.** Routing lives inside one coordinator module: the Workflow Protocol is to "translate a validated task input into a task graph; select specializations and a topology" (§3.4); cards appear "on a board filtered by specialization and Permission" (§3.4, quoted in notes `mapping-yu-zhu.md:275`, also read in primary). Primary.

### 3. Goujon, AAM/5C, arXiv:2610.30221 (primary: PDF text, targeted reading of §1.3.2, §2.2.2, §8.4, Appendix 3 §3.3, Definitions G.1, G.2, G.12; notes used as index)

- **C1 part. DISPUTABLE: yes.** Two candidate units: the seven IS layers, where "each layer has a single responsibility" (§2.2.2, p.27 region), and the AOM, "Operating model that frames the autonomy of agents, in six roles" (G.12, p.93). The AOM is defined and has several roles, but it is the single governance organization for the whole system, and the layers are technical strata, not areas of work. Read as an organizational unit, the AOM gives yes. Primary.
- **C2 part. DISPUTABLE: yes.** At the AOM level the source states functions and roles: AOM "organizes human work around three functions: defining intent, managing context, auditing compliance" (notes `mapping-aam5c.md:190`; G.12 in primary agrees) with six named roles (§8.4.1). If the AOM counts as an area, this is (a) plus (b) and gives yes; because C1 is doubtful, part. Notes (checked against primary G.12).
- **C3 part. DISPUTABLE: yes.** Table 14 (RACI) gives each of 14 governance activities an A, but some rows have two: "Two As on the same row signal a dual signature" (Appendix 3 §3.3, p.114). Accountability is stated but not always unique, and covers governance activities only. A RACI is the standard accountability record, so yes is defensible. Primary.
- **C4 part.** Discovery comes from the A2A protocol: "Agent Cards describe each agent’s capabilities there" (§1.3.2, p.23). Escalation goes "to the competent AOM role" without a stated lookup. Primary.

### 4. Microsoft Multi-Agent Reference Architecture (primary: repository cloned at commit `adbefc1`, 2026-10-27; files read: Agent-Registry.md, Reference-Architecture.md, Patterns.md, Long-Term-Memory.md, Evaluation.md)

- **C1 part.** Agent groups are used but not defined: "Use hierarchical organization (e.g., supervisor → agent group) to maintain clarity, scalability, and ease of intent resolution." (docs/reference-architecture/Reference-Architecture.md:150-151). "Domain" otherwise means one agent's specialty. Primary.
- **C2 part.** Responsibilities are per agent: "Each agent focuses on a particular domain (e.g., finance, healthcare, coding) or function" (Reference-Architecture.md, Agent #1 to #4; quoted in notes `mapping-vendors.md:209`). Primary and notes.
- **C3 part.** Owners appear as optional catalog metadata per agent, with no accountability stated: "for categorization or classification (such as `tags` or `owners` in the metadata" (docs/agent-registry/Agent-Registry.md:136-137). Long-term memory asks for "a named owner for the memory data of each scope" (docs/memory/Long-Term-Memory.md:374). Primary.
- **C4 yes.** Registry information is used "For the Agents to determine what's the best agent(s) to interact with to complete the task" (Agent-Registry.md:131-132); entries hold "capabilities, endpoints, security credentials" and a "Query-optimized schema for capability lookups" (Reference-Architecture.md, Registry Storage). Pattern 2: "Agent discovery based on capabilities and metadata." (Patterns.md). Primary.

### 5. AWS Prescriptive Guidance on agentic AI (primary: pages agents-layer, what-needs-to-be-governed, governance-models of `govern-architect-agentic-ai`, and getting-started-with-a2-a of `agentic-ai-frameworks`; notes for the Foundations guide)

- **C1 part.** Business units are named but not defined: "Federated Governance distributes responsibility to business units while maintaining alignment through shared standards." (governance-models). Agents are also "like organizational departments" (Foundations, per notes `mapping-vendors.md:474`), which makes the department one agent. Primary.
- **C2 part.** Specification is per agent: "A well-scoped agent has a clear job, defined responsibilities, and measurable success criteria" (Foundations F1, notes `mapping-vendors.md:472`). Notes.
- **C3 part.** The registry records ownership per agent, with no statement that it is the accountable owner: "Agent capabilities, permissions, and purpose Metadata on ownership, version history, and dependencies" (agents-layer, "Agent registry and catalog"). Also "authorization delegation to the tool or agent owners". Primary.
- **C4 part. DISPUTABLE: yes.** "Agents need to securely discover, select and access tools and other agents via well-known protocols like MCP and A2A." (agents-layer). A2A modes include "Capability-based discovery, enabling emergent division of labor" and "agents select the most suitable peer" (getting-started-with-a2-a). This is lookup from a capability, but the example manifest (`"can"`, `"needs"`, `"meta"`) carries no endpoint, so "how to reach it" is only implied by A2A. Primary.

### 6. Google Cloud Architecture Center, agentic AI pages (primary: multi-tenant-agentic-ai-system, multi-agent-private-networking-patterns, choose-agentic-ai-architecture-components, multiagent-ai-system)

- **C1 part. DISPUTABLE: yes.** "Each tenant project is a dedicated Google Cloud project for each business unit." Its runtime "hosts the specific business unit agent" (multi-tenant page, Tenant projects). The unit has stated properties, but the text gives it one agent, which the criteria place under part; another line says "only the tenant agents can access this data" (notes `mapping-vendors.md:853`), which supports yes. Primary.
- **C2 part.** Unit-level properties are isolation, tools, data and management, not responsibilities or roles: "Individual developer and operations teams manage tenant projects independently. This isolation provides autonomy for each business unit." (multi-tenant page). Primary.
- **C3 no.** Searched the four pages for owner, ownership, accountable, accountability: the only hit is "total cost of ownership". Agent Registry is "a centralized inventory and catalog" with no owner field stated (choose-components page). Primary.
- **C4 part.** Lookup is by agent name or by the assistant's own decision, then to an endpoint: "When a user specifies an agent by using @agent_name, or when the assistant decides to delegate, the app looks up the agent in the registry to find the associated endpoint." (private networking page). Not from a kind of work. Primary.

### 7. El Hassani, Charterion v2.0, Zenodo 22829848 (primary: 290-page PDF extracted with pypdf; targeted reading of pp. 45, 54, 69, 75, 96, 191, 211; notes rows from `mapping-round2-charters.md` §A.1 and `charterion-full.md` §1)

- **C1 yes.** Capability is a core sort of the metamodel: "Capability(c),Process(p), Realizes(p, c) capabilities and the processes that realise them" (Table 6.1, PDF p.45; extraction drops spaces). Several agents can be chartered on one capability: "A second agent, claim submission, was chartered commit on the same capability" (notes `charterion-full.md:207`, citing p.130). "Domain" itself is never defined. Primary and notes.
- **C2 part. DISPUTABLE: yes.** At the business layer, roles perform process steps and a staffing table records holders: "A role without holders is vacant; vacancy propagates to WF1 and WF9" (Staffing Table, notes `mapping-round2-charters.md:97`; PDF p.211 lists "Human,Role,Holds, Performs"). So a capability has processes (what it covers) and roles (filled by people). But agents get authority per agent through charters, and nothing states a capability's responsibilities apart from its processes. Read as capability plus processes plus roles, yes is defensible. Notes, checked against primary p.211.
- **C3 part.** The Charter Register names an accountable human per charter, that is per agent and scope: "Every charter that confers a write level names a human, or a role with a current holder, who is accountable." (X2, notes `charterion-full.md:62`, p.34). Several agents can hold charters on one capability, so accountability is not unique per capability. Notes.
- **C4 no. DISPUTABLE: part.** Searched for discover, directory, routing, registry used for hand-over. The only lookup is escalation to a human per agent: "An agent is reachable if it has at least one escalation human" (§8, PDF p.54, spaces restored). Foreign agents can read a catalogue at exposure level X1 "so a foreign agent can find out what exists and what could be requested" (§10.3, p.75). Neither is agent discovery or lookup from a kind of work; a reader who counts the escalation route or the X1 catalogue would give part. Primary.

### 8. Longmire and Longmire, AEON, Zenodo 20349596 (primary: 49-page PDF, keyword search plus §5, §10.2, §11.1)

- **C1 yes.** "AEON is the control plane. The subdomains are the capability areas the control plane orchestrates." (§5, p.8). Each subdomain "has its own runtime, its own internal architecture, its own engineering function" (§5, per notes `mapping-round2-charters.md:318`), and Appendix A lists nine subdomains. Primary.
- **C2 part.** Appendix A states each subdomain's scope, for example Human Capital: "HR, talent management, learning and development" (notes `mapping-round2-charters.md:325`). No roles or positions are specified per subdomain; the only roles are principal attributes ("role designations", §7.1). Notes plus primary search for "role".
- **C3 part. DISPUTABLE: yes.** "Every capability any subdomain exposes is registered in the registry along with its metadata: the subdomain that provides it" (§11.1, p.26). One providing subdomain per capability, but the record calls it the provider, not the accountable owner; reading provider as owner gives yes. Primary.
- **C4 yes.** "The protocol specifies how agents discover other agents (through the capability registry developed in Section 11), how they authenticate to each other" (§10.2, p.24); the registry entry also holds "the adapter that exposes it" (§11.1). Primary.

### 9. deVadoss, CEAD, arXiv:2605.08258 (primary: full arXiv HTML text)

- **C1 part. DISPUTABLE: yes.** Business capabilities come first: "define the business capability and owner before defining the agent role or prompt" (§V-E, principle 1), and the design plane "maintains the capability map" (§V-B, notes `mapping-round2-charters.md:367`). The capability has a stated property (an owner), but the text pairs one agent with one capability ("specialization maps to separate capabilities", §V-D), and the capability is not otherwise defined. Primary.
- **C2 part.** The contract is per agent: "Describes what the agent is allowed to do and explicitly what it must not do." (Table II, Purpose and non-purpose). Primary.
- **C3 part. DISPUTABLE: yes.** Each Agent Capability Contract "Names the durable capability, accountable product owner, operating team, funding model, and retirement owner." (Table II). Accountability is stated, but the record is per agent and uniqueness per capability is not stated. Primary.
- **C4 part.** "Registries: other systems must discover what an agent can do and who owns it." (§IV-A). Discovery runs from agent to capability; no lookup from a kind of work and no reach information is described. Primary.

### 10. Salesforce Architects, "The Agentic Enterprise" (primary: the page returned "Access Denied" to curl twice; read through WebFetch, which returns quoted fragments through a summarizing model; cross-checked against notes rows)

- **C1 part.** Business domains are used, not defined: agents can "work within and across business domains" (architecture principles section, via WebFetch). Primary (WebFetch).
- **C2 no.** WebFetch found no area-level or per-agent responsibility or role specification; "roles" appear only as access control ("from static, role-based controls to dynamic, intent-based permissions") and as human work agents may replace. Agents are "instantiated for specific tasks" (Agentic Layer, notes `mapping-round2-charters.md:447`). Primary (WebFetch) and notes.
- **C3 part.** Ownership is recorded per data asset only: Metadata Service holds "descriptive metadata, including data lineage, ownership, and classifications" (notes `mapping-round2-charters.md:500`; WebFetch returned the same phrase). Primary (WebFetch) and notes.
- **C4 part. DISPUTABLE: yes.** Agent Registry: "A curated ecosystem of pre-built AI solutions and agents that supports discovery and capability matching" (notes `mapping-round2-charters.md:474`; WebFetch returned the same sentence). Capability matching is lookup from a capability, but nothing says how a found agent is reached. Primary (WebFetch) and notes.

### 11. Sharma and Shah, AOS-0001 arXiv:2608.03214 with AOS-0000 arXiv:2606.01508 (primary: both PDFs extracted with pypdf, AOS-0001 72 text pages, AOS-0000 24 pages; keyword search plus §6, §9.3, §10.4, glossary, Appendix example)

- **C1 no. DISPUTABLE: part.** The only unit above an agent is a deployment and trust boundary: "AOS domain An administrative and trust boundary operating one or more AOS components." (AOS-0001 glossary, p.68). No business unit, department or organizational unit (searched). A reader who counts an administrative boundary as an organizational unit would give part. Primary.
- **C2 no. DISPUTABLE: part.** The model is capability-centric, not area-centric: "A stable capability name separates the requested outcome from replaceable providers" (AOS-0001 §2 design principles, p.10). Capability contracts describe outputs per capability, not responsibilities or roles per area; counting them as per-provider contracts would give part. Primary.
- **C3 part.** A provider record carries an owner, with accountability not stated: `"provider": { "id": "internal-workflow-west", "owner": "example-enterprise"` (AOS-0001 appendix example, p.58). Primary.
- **C4 yes.** "Routing binds a capability to a provider and protocol." and "It records the actual endpoint and version" (AOS-0001 §10.4, p.33); capability discovery outputs a "Feasible provider set and ranking evidence", and "Feasibility precedes ranking." (§9.3, p.30). Primary.

### 12. Steinder and Franke, arXiv:2607.25076 (primary: full arXiv HTML text, keyword search plus §IV)

- **C1 no.** Searched for domain, department, business unit, organization, team: "domain" refers to application domains ("harnesses are domain and model specific", §I) or a skill's provenance. No unit above an agent. Primary.
- **C2 no. DISPUTABLE: part.** No area specification. Per agent, the paper only names a missing artifact: "a signed agent card declaring the intended action space. Neither exists in standardized form." (§IV-H). Counting that proposed per-agent declaration would give part. Primary.
- **C3 no.** Searched owner, accountab, registry, catalog. The one registry is for skills: "provenance declaring a skill’s domain, model compatibility, and callable tools" (§IV-C). No owner per agent, asset or capability. Primary.
- **C4 no. DISPUTABLE: part.** Agent discovery is named as a requirement, not specified: "Agent deployment, discovery, and authorization requires first-class handling and runtime-context awareness" (§IV-A). A2A mediation of "task delegation" (§IV-F) assumes a known target. Primary.

### 13. Beheshti et al., ASOC manifesto, arXiv:2607.12619 (primary: full arXiv HTML text)

- **C1 no.** Searched for domain, department, business unit, organizational unit, team. "Organisation" appears only as a delegating principal ("under which a human or organisation delegates a goal to an agentic service", §III definitions). Primary.
- **C2 part.** Contracts are per agentic service: "Capability contracts specify functional capabilities, goal types, uncertainty characteristics, execution constraints, and resource/trust requirements" (§V-B, Principle 2). Primary.
- **C3 no.** No record of owners. Responsibility is a research question: "responsibility is distributed across a chain of principals that may include the delegating user or organisation, the agent provider" (§VI-A). Primary.
- **C4 part. DISPUTABLE: yes.** "In ASOC, discovery must work at the goal level: an orchestrating agent must find, assess, and bind to agentic services whose capabilities match a specified goal" (§IV, discovery and binding). That is lookup from a kind of work to a provider and binding, but stated as a requirement of a manifesto with no mechanism, and performed by an orchestrating agent. Primary.

### 14. Venkiteela, EAAF, doi:10.64539/sjcs.v2i1.2026.368 (primary: journal PDF from journal.futuristech.co.id, extracted with pypdf, keyword search plus §4.1.3, §6; notes for item rows)

- **C1 part.** Clusters and domains are named, each the same as one agent: "dedicated Specialist Agent Clusters (e.g., a Data Agent, a Compliance Agent)" (§4.1.3), and "a federation of multi-domain agents (Integration, Compliance, Data, Security, Finance, etc.)" (§6). Primary.
- **C2 no. DISPUTABLE: part.** No per-area specification and no per-agent charter; only agent types by function: "Task Agents, dedicated Integration Agents, Compliance Agents, and high-level Supervisor Agents" (§4.1.5, notes `mapping-round2-platforms.md:546`). Reading the type descriptions as per-agent responsibilities gives part. Notes.
- **C3 no.** Searched owner, accountab, registry: accountability is a principle ("Autonomy with Accountability", §3.4) and a registry appears only as future work ("consistent tool registry metadata", §8.2). Primary.
- **C4 part.** Routing sits in the orchestration engine: "large-task decomposition, intelligent delegation to specialist agents, dependency management across steps" (§4.1.3, notes `mapping-round2-platforms.md:533`). Notes, checked against primary §4.1.3.

### 15. Amazon Bedrock AgentCore (primary: AWS Agent Registry pages registry, registry-key-capabilities, registry-search-records, registry-mcp-endpoint; notes: `inventory-agentcore.md` for the other services)

- **C1 no.** Searched the inventory and registry pages for domain, department, business unit, team. "Organization" means an AWS Organization of accounts: "AgentCore Runtimes and Gateways in your organization's member accounts are automatically cataloged as registry records" (notes `inventory-agentcore.md:471`). Notes.
- **C2 no.** No area concept, and no per-agent responsibility specification found in the inventory's 146 components (searched role, responsib, charter). Notes.
- **C3 no. DISPUTABLE: part.** No owner field is part of the record model; an owner appears only as an example of free-form metadata: `{ "customMetadata.owner": { "$eq": "search-team"}}` (registry-search-records, filter examples). If an organization adopts that convention, part. Primary.
- **C4 yes.** "Your developers and agents can search the registry and invoke the MCP endpoint using their existing corporate credentials" (registry-key-capabilities), with natural-language search ("find a tool that can book flights") over MCP and A2A records validated "against the MCP and A2A protocol schemas" (notes `inventory-agentcore.md:463`), which carry the endpoint. Primary.

### 16. LangGraph with LangSmith and LangSmith Deployment (primary: docs.langchain.com pages administration-overview, set-up-hierarchy, agent-registry, server-a2a; notes: `inventory-langgraph.md`)

- **C1 part. DISPUTABLE: yes.** "A workspace is a logical grouping of users, agents, and resources within an organization. Workspaces are commonly used to isolate business units, so each unit's agents and resources stay separate from other units'." (administration-overview, Workspaces; link markup removed). It is defined and holds several agents, but it is defined as a trust and access boundary; standing for a business unit is a common use, not the definition. Primary.
- **C2 part.** Workspace-level properties are access roles and settings, not responsibilities: "A user can also receive a workspace role through a team that has access to the workspace." (set-up-hierarchy; link markup removed). Primary.
- **C3 no.** Agent Registry offers "one place to govern every agent your organization runs" (agent-registry), and the page has no owner or accountability field (searched owner, accountab). Primary.
- **C4 part.** "Each assistant automatically exposes an A2A Agent Card that describes its capabilities and provides the information needed for other agents to connect." (server-a2a). Retrieval is by `assistant_id`, so the caller must already know the agent; other routing is inside a graph. Primary.

### 17. OpenClaw, docs.openclaw.ai (primary: concepts/multi-agent and concepts/agent-bindings pages; notes: `inventory-openclaw.md`)

- **C1 part.** A team exists only as a preset of agents: "Create a small team with written role contracts and directed delegation" (concepts/multi-agent, Team preset). It is not a defined element with properties of its own. Primary.
- **C2 part.** Roles are written per agent: the preset "creates a chief of staff (`coordinator`), researcher, writer, and reviewer, each with its own workspace and completed identity" and "Their operating programs live in `AGENTS.md`" (concepts/multi-agent). Primary.
- **C3 part.** Bindings record which agent owns a slice of traffic, not a responsibility: "each binding names an `agentId` and matches channel facts such as the account, peer, guild, team, or Discord roles, and the matched agent owns the resulting session" (concepts/agent-bindings). Primary.
- **C4 part.** The coordinator finds specialists: "it discovers matching specialists, assigns bounded work, checks their artifacts" (concepts/multi-agent). The mechanism is not stated, and inbound routing follows channel facts, not the kind of work: "The model does not choose a channel; routing follows fixed rules controlled by the host configuration." (notes `inventory-openclaw.md:746`). Primary and notes.

## 3. Totals

| Criterion | yes | part | no | not assessed | DISPUTABLE cells |
|---|---|---|---|---|---|
| C1 area exists | 2 | 10 | 5 | 0 | 5 |
| C2 area specified | 0 | 11 | 6 | 0 | 5 |
| C3 accountability record | 0 | 9 | 8 | 0 | 5 |
| C4 finding where to send work | 4 | 11 | 2 | 0 | 5 |
| Directory (derived) | 0 | 16 | 1 | 0 | n/a |

DISPUTABLE cells in all: 20 of 68.

## 4. Sensitivity

| Criterion | As given (yes/part/no) | Every DISPUTABLE cell at its higher value | Every DISPUTABLE cell at its lower value |
|---|---|---|---|
| C1 | 2 / 10 / 5 | 6 / 7 / 4 | 2 / 10 / 5 |
| C2 | 0 / 11 / 6 | 2 / 12 / 3 | 0 / 11 / 6 |
| C3 | 0 / 9 / 8 | 3 / 8 / 6 | 0 / 9 / 8 |
| C4 | 4 / 11 / 2 | 7 / 10 / 0 | 4 / 11 / 2 |

The lower-value column equals the values given, because every DISPUTABLE cell already carries its lower value. At the higher values, Directory changes for one source: AEON becomes yes (C3 yes, C4 yes); Steinder and Franke becomes part.

## 5. Nearest to "yes" on all four

1. **AEON** (yes, part, part D:yes, yes). Lacks: (C2) no roles or positions are specified at the subdomain level, only each subdomain's scope; (C3) the capability registry names the providing subdomain per capability but never calls it accountable.
2. **Charterion** (yes, part D:yes, part, no D:part). Lacks: (C2) responsibilities are not stated per capability apart from its processes, and agents hold per-agent charters rather than filling the capability's roles; (C3) the accountable principal is per charter (per agent and scope) and not unique per capability; (C4) no lookup from a kind of work to an agent or role; only per-agent escalation to a human.
3. **AAM/5C** (part D:yes on C1 to C3, part on C4). Lacks: (C1, C2) its one clearly defined organizational unit, the AOM, is a single system-wide governance body, not one area among others; (C3) the RACI covers governance activities only and allows two accountable roles on a row; (C4) discovery is A2A Agent Cards, with no lookup from a kind of work.
4. **CEAD** (part D:yes, part, part D:yes, part). Lacks: (C1) the capability is not defined as an element apart from the per-agent contract; (C2) the contract is per agent; (C3) the accountable product owner sits in a per-agent contract and is not stated as unique per capability; (C4) registries answer "what can this agent do", not "who handles this work".
5. **AOS** reaches yes on C4 and part on C3, but has no area of work (C1 no, C2 no).

## 6. What I could not open, and the cells I trust least

Could not open or did not read:
- Salesforce: direct fetches returned "Access Denied". I read it only through WebFetch, whose output passes through a summarizing model, so the Salesforce quotations are not byte-verified against the page. Each Salesforce quotation also appears in the earlier notes, which agree. Figures were not seen.
- Charterion: I did not read all 290 pages. I read targeted pages (45, 54, 69, 75, 96, 191, 211, by keyword) and used item rows from the notes for the rest.
- AAM/5C: targeted pages only (§1.3.2, §2.2.2, §8.4, Appendix 3, Definitions), about 15 of 120 pages.
- AOS-0001: the arXiv PDF reports 199 pages but text extracts to 72; a few pages may be image-only and unread.
- AWS: only four pages read in primary; the Foundations guide (per-agent scope, departments) is from notes.
- AgentCore: only the four registry pages in primary; C1 and C2 rest on the notes inventory and a keyword search of it.
- OpenClaw: the sessions configuration page (`gateway/config-tools/sessions.md`) returned an empty body, and `tools/agents-list.md` returned "Not found", so I could not confirm from the docs whether an agent-listing tool exists. C4 rests on the coordinator passage.
- Google: the Well-Architected AI and ML pages and the remaining use-case pages were not read in primary.

Cells I trust least:
1. **OpenClaw C4** (part): if a documented agent-listing tool with descriptions exists, part still holds; if bindings or the coordinator use a lookup by kind of work, it could be yes. I could not open the relevant pages.
2. **Microsoft C4** (yes, not marked DISPUTABLE): the Pattern 2 text says "runtime resolution by orchestrator", which supports part; I gave yes because Agent-Registry.md states the use "For the Agents". A stricter reader would mark it DISPUTABLE.
3. **AAM/5C C1 to C3**: everything turns on whether the AOM counts as an organizational unit.
4. **Charterion C2 and C4**: long source, targeted reading.
5. **Salesforce C2** (no): rests on a summarizer reporting absence.
6. **AgentCore C3** (no, D: part): an owner exists only as example metadata.

## 7. Check of notes quotations

Every quotation attributed to a notes file and line above was checked by script (`grep -F`-style substring test of the quoted string against that exact line). Result: 21 quotations at 20 distinct lines checked, 0 mismatches in the final file. The first run found 4 wrong line numbers in my draft (yu-zhu 276, vendors 163 and 854, round2-charters 324); each quote was present one line or a few lines away, and the citations were corrected to 275, 209, 853 and 318 before this run. The list checked:

`mapping-yu-zhu.md:275`, `mapping-aam5c.md:190`, `mapping-vendors.md:209`, `mapping-vendors.md:472`, `mapping-vendors.md:474`, `mapping-vendors.md:853`, `charterion-full.md:207`, `charterion-full.md:62`, `mapping-round2-charters.md:97`, `mapping-round2-charters.md:318`, `mapping-round2-charters.md:325`, `mapping-round2-charters.md:367`, `mapping-round2-charters.md:447`, `mapping-round2-charters.md:474`, `mapping-round2-charters.md:500`, `mapping-round2-platforms.md:533`, `mapping-round2-platforms.md:546`, `inventory-agentcore.md:463`, `inventory-agentcore.md:471`, `inventory-openclaw.md:746`.
