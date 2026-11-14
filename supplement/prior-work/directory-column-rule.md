---
title: "Directory column re-derived under one rule"
date: 2026-11-12
author: "sagan (subagent, notes only)"
status: "not yet checked by sagan"
---

# Directory column re-derived under one rule

Derived on 2026-11-12 from the notes under `` only. No source was re-read and nothing was searched on the web. Paths are relative to ``. The old cells come from Grid A of `prior-work/source-by-part-grid.md`. Row 18 (LifeOS) has no row in that grid and is not counted in the totals.

## 1. The rule

For the Dir column, for every row:

- **yes**: the notes show the source has a record that gives BOTH (a) which area of work, domain or owner is accountable for a responsibility or capability, AND (b) how an agent reaches the agent or role that handles it.
- **part**: the notes show EITHER half in some form: (b) a lookup an agent can use at run time to find and reach another agent or role (an agent list, agent cards, a registry of agents with endpoints, discovery), OR (a) a record of an owner, provider or accountable party per capability or responsibility. Say which half is present and what is missing.
- **no**: the notes record neither, or record a search that found neither.
- **n.a.**: the notes do not say.

A doubtful case is "part" only if a note line supports one half; otherwise "no" or "n.a.". Do not infer from what a source "probably" has.

## 2. The Dir column under the rule

| # | Source | Old Dir | New Dir | Halves present, and what is missing | Evidence (`file:line` "quotation") | Flag |
|---|---|---|---|---|---|---|
| 1 | Yu, Rabhi, Zhu and Lu | no | part | (b) only: an agent registry for discovery, named as a realization of agent collaboration (NC17, VP1). Missing (a): ownership is set at design time per layer; no run-time record. | `prior-work/mapping-yu-zhu.md:109` "realization "Agent registry; A2A or direct calls"" | CHANGED |
| 2 | Zhu, Fluid Structure, Rigid Record | no | no | Neither. The board filters work by specialization; that routes tasks to capable agents, not a lookup to reach an agent or role. | `prior-work/mapping-yu-zhu.md:370` "No record of which area of work is accountable for what. The board filters by specialization, which routes by capability." |  |
| 3 | Goujon, AAM/5C | no | part | (b) only: Agent Cards (discovery metadata for agents) and an agentic registry of authorized agents. Missing (a): accountability is per act and per rule; the RACI covers governance activities only. | `prior-work/mapping-aam5c.md:179` "Discovery metadata for agents." | CHANGED |
| 4 | Microsoft Multi-Agent Reference Architecture | no | part | (b): registry entry holds url and authentication for reaching an agent. (a) only weakly: an `owners` tag per agent, for categorization, not accountability for a capability or responsibility. | `prior-work/mapping-vendors.md:264` "`owners` tag "for categorization or classification" for humans (A26), and endpoint and auth for reaching an agent." | CHANGED |
| 5 | AWS Prescriptive Guidance (agentic AI) | part | part | (a) weakly: registry entries carry ownership and business purpose per asset; (b): capability registries support peer discovery (B098). Missing: accountability for a responsibility. | `prior-work/mapping-vendors.md:643` "Registry entries include "ownership, and business purpose" (B006)"<br>`prior-work/mapping-vendors.md:482` "support versioned metadata for peer discovery" |  |
| 6 | Google Cloud Architecture Center (agentic AI) | part | part | (b) only: a discovery service maps agent name to endpoint. Missing (a): no page defines an owner of an agent, tool or domain. | `prior-work/mapping-vendors.md:926` "Discovery service maps agent name to endpoint (C109)" |  |
| 7 | Charterion v2.0 (El Hassani) | part | part | (a) only: the Charter Register names an accountable principal per agent and business scope (capability, process or step). Missing (b): never presented as a lookup an agent uses to find where to send work. | `prior-work/mapping-round2-charters.md:227` "a step-to-agent and agent-to-human map can be computed from the registers, but the text never presents it as a lookup an agent uses to find where to send work" |  |
| 8 | AEON | part | part | (a) as provider, not accountable party: the capability registry names the subdomain that provides each capability; (b): agents discover each other through it. Missing: accountability. | `prior-work/mapping-round2-charters.md:343` "Agents use it to find each other"<br>`prior-work/mapping-round2-charters.md:610` "P: registry names "the subdomain that provides it" (B30)" |  |
| 9 | CEAD | part | part | (a): an accountable owner per agent and per capability (ACC). (b) only as a stated requirement that discovery return the owner; no entry format and no route given. Missing: how to reach. | `prior-work/mapping-round2-charters.md:425` "So CEAD records an owner per agent and per capability, and states that discovery should return the owner. It describes no registry entry format." |  |
| 10 | Salesforce Agentic Enterprise IT Architecture | no | part | (b) only: an Agent Registry that supports discovery and capability matching. Missing (a): "Accountable" appears 0 times; the one owner is for data. | `prior-work/mapping-round2-charters.md:567` "Agent Registry: "A curated ecosystem of pre-built AI solutions and agents that supports discovery and capability matching"" | CHANGED |
| 11 | AOS-0001 and AOS-0000 | part | part | (b): routing reaches a provider for a capability. (a) as provider only: the capability registry lists providers per capability (see DirC below). Missing: any record of which domain is accountable. | `prior-work/mapping-round2-platforms.md:647` "P: reaches a provider for a capability (the "how to reach" half)" |  |
| 12 | Steinder and Franke | no | no | Neither. Task routing to specialists is orchestration; no agent discovery or owner record in the notes. | `prior-work/mapping-round2-platforms.md:647` "A: "routing tasks to the right specialist agent" §II-4 is orchestration" |  |
| 13 | ASOC manifesto | no | part | (b) only: capability directories for dynamic discovery; service discovery (C38); agent registries and discovery mechanisms (C55). Missing (a): responsibility allocation is liability across suppliers. | `prior-work/mapping-round2-platforms.md:515` ""capability directories" for "dynamic discovery and trust assessment" (§VI-C)" | CHANGED |
| 14 | EAAF | no | no | Neither. Agents negotiate responsibilities; a tool registry appears only as future work. | `prior-work/mapping-round2-platforms.md:647` "A: "agents negotiate responsibilities" §6.6 is the opposite approach" |  |
| 15 | Amazon Bedrock AgentCore | no | part | (b) only: A2A Agent Cards with service endpoint, and a Registry of agents with discovery (C137). Missing (a): no owner or responsibility field. | `platform-mapping/mapping-agentcore.md:294` "A2A Agent Cards "describe an A2A server's identity, capabilities, skills, service endpoint, and authentication requirements"" | CHANGED |
| 16 | LangGraph with LangSmith | no | part | (b) only: subagent discovery through a listing in the system prompt or a `list_agents` tool; Agent Registry inventory (Cloud). Missing (a): "a list of agents, not of responsibilities". | `platform-mapping/mapping-langgraph.md:365` "with a `list_agents` tool for "Large or dynamic agent registries"" | CHANGED |
| 17 | OpenClaw | no | part | (b): the coordinator uses `agents_list` to discover permitted specialists. (a) only as prose: specialists' duties written in the coordinator's program, matched by name. Missing: a record of responsibility to accountable area. | `platform-mapping/mapping-openclaw.md:667` "Use `agents_list` when available to discover permitted specialists." | CHANGED |
| 18 | LifeOS | (none) | part | (a): config/responsibilities.tsv records responsibility, domain and agent (with gaps). (b) present elsewhere, not in the record: ListAgents lists running agents and SendMessage reaches them. Missing: an entry does not say how to start or reach its agent. | `platform-mapping/mapping-lifeos.md:51` "an entry names an agent but not how to start one"<br>`platform-mapping/mapping-lifeos.md:826` "ListAgents lists which agents exist" |  |

8 of the 17 cells in rows 1 to 17 change, all from "no" to "part". No cell becomes "yes": no source in the notes has one record that names an accountable area, domain or owner for a responsibility AND says how to reach the agent or role that handles it. The rows that come closest (CEAD, AEON, AWS, Microsoft, LifeOS) have one half in full and the other half weakly or in a separate place.

## 3. The DirC column under its definition

Definition applied: **yes** if the notes show a record of which area is accountable for each responsibility; **part** if a record of owner or provider per capability or agent exists but not accountability per responsibility; **no** otherwise.

Three cells change, all from "no" to "part". The cells for Charterion, AEON and CEAD stay "part"; the other eleven stay "no".

| # | Source | Old DirC | New DirC | Why | Evidence |
|---|---|---|---|---|---|
| 4 | Microsoft Multi-Agent Reference Architecture | no | part | owner per agent (an `owners` tag on the registry entry); no accountability per responsibility | `prior-work/mapping-vendors.md:108` "for humans "`tags` or `owners`"" |
| 5 | AWS Prescriptive Guidance (agentic AI) | no | part | owner per registry entry (agents, tools, MCP servers); no accountability per responsibility | `prior-work/mapping-vendors.md:643` "No entry records which area of work is accountable for a responsibility." |
| 11 | AOS-0001 and AOS-0000 | no | part | provider per capability in the registry, the same kind of record that gives AEON its part; no accountable domain | `prior-work/mapping-round2-platforms.md:249` "Catalog of capabilities and providers with trust, cost, latency and health" |

The grid's "Disagreements with coverage-matrix.md" section judged the Microsoft and AWS DirC cells "no" under the grid's narrower definition ("a record of which area is accountable for which responsibility"). Under the definition used here, an owner per agent or per asset counts as "part", which matches the coverage matrix's "partial" for both. Google stays "no": "No page defines an owner of an agent, tool or domain" (`prior-work/mapping-vendors.md:983`). AOS changes for the same reason AEON is already "part": its registry names a provider per capability.

LifeOS (row 18, not in the grid): DirC **yes**, `platform-mapping/spot-check-lifeos.md:158` "config/responsibilities.tsv (since 2026-11-11) records responsibility, domain and agent". Gaps: one responsibility has two domains, and "life coaching and the daily summary" has domain `-` (`platform-mapping/spot-check-lifeos.md:180`).

New DirC totals over rows 1 to 17: yes 0, part 6, no 11, n.a. 0 (was 0, 3, 14, 0). Grid B's "Directory content" column changes for rows 4, 5 and 11 to "part".

## 4. Consequences

**Dir column totals over rows 1 to 17.**

| | yes | part | no | n.a. |
|---|---|---|---|---|
| Old (Grid A) | 0 | 6 | 11 | 0 |
| New (this rule) | 0 | 14 | 3 | 0 |

The three rows that stay "no" are Zhu, Steinder and Franke, and EAAF. The column is now comparable between rows 1 to 14 and rows 15 to 17: a run-time agent lookup counts as "part" in both groups.

**New Grid B "Interaction" cells** for the rows whose Dir cell changed (Interaction = Dir, Msg, Orc, Chn; "f + p of 4"):

| # | Source | Dir (new) | Msg | Orc | Chn | Old Interaction | New Interaction |
|---|---|---|---|---|---|---|---|
| 1 | Yu, Rabhi, Zhu and Lu | part | part | yes | yes | 2 + 1 of 4 | 2 + 2 of 4 |
| 3 | Goujon, AAM/5C | part | yes | part | part | 1 + 2 of 4 | 1 + 3 of 4 |
| 4 | Microsoft Multi-Agent Reference Architecture | part | yes | yes | yes | 3 + 0 of 4 | 3 + 1 of 4 |
| 10 | Salesforce Agentic Enterprise IT Architecture | part | part | yes | yes | 2 + 1 of 4 | 2 + 2 of 4 |
| 13 | ASOC manifesto | part | part | yes | part | 1 + 2 of 4 | 1 + 3 of 4 |
| 15 | Amazon Bedrock AgentCore | part | part | yes | part | 1 + 2 of 4 | 1 + 3 of 4 |
| 16 | LangGraph with LangSmith | part | yes | yes | part | 2 + 1 of 4 | 2 + 2 of 4 |
| 17 | OpenClaw | part | yes | yes | yes | 3 + 0 of 4 | 3 + 1 of 4 |

Other consequences to carry into the grid: the Dir row of "Column totals for Grid A" becomes 0 / 14 / 3 / 0; the DirC row becomes 0 / 6 / 11 / 0; the all-columns total moves 11 cells from "no" to "part" (part 226 to 237, no 101 to 90); the caveat in "What the notes do not support" about the Dir column no longer applies; the Evidence entries for Dir in the changed rows and for DirC in rows 4, 5 and 11 need the new lines above.

## 5. Quotation check

A Python script opened each cited file, took the cited line, and tested that each quotation above is a substring of that line. This covers every quotation in the tables of sections 2 and 3, plus six quotations in the prose of sections 2, 3 and 6 (`prior-work/mapping-vendors.md:983`, `platform-mapping/spot-check-lifeos.md:180`, `prior-work/mapping-yu-zhu.md:109`, `prior-work/mapping-aam5c.md:390`, `platform-mapping/mapping-langgraph.md:365`, `prior-work/mapping-round2-charters.md:572`).

Result: Checked 31 quotations against their cited lines; 0 mismatches.

## 6. Thin cells: where a careful reader could decide otherwise

- **Microsoft and AWS Dir (part, could be yes).** Each registry entry carries both an owner and a way to reach the agent (Microsoft: url and authentication; AWS: peer discovery). I read the owner as an owner of an asset, not a party accountable for a capability, following `prior-work/mapping-vendors.md:1032`, which keeps the two apart. A reader who counts an asset owner as half (a) would give "yes".
- **CEAD Dir (part, could be yes).** The accountable owner per capability is explicit; the reach half is only "discovery should return the owner", with no entry format.
- **AEON Dir (part, could be yes).** The registry gives a providing subdomain per capability and agents find each other through it. It fails only because "provider" is not "accountable".
- **LifeOS Dir (part, could be yes).** The record names responsibility, domain and agent; an agent is reached by name with SendMessage. I kept "part" because the entry itself says nothing about how to reach or start the agent, which the mapper lists as missing.
- **OpenClaw Dir (part, could be yes or stay part).** The coordinator's program lists specialists' duties in prose and finds them with `agents_list`; prose role text is a weak form of (a).
- **Yu Dir (part, could be no).** The agent registry is only a "realization" option, and the mapper says "Discovery here means a catalog, not WARM's Directory" (`prior-work/mapping-yu-zhu.md:109`).
- **Salesforce and ASOC Dir (part, could be no).** Each rests on one phrase about discovery ("supports discovery and capability matching"; "capability directories" for "dynamic discovery") with no entry contents.
- **Zhu Dir (no, could be part).** The board filtered by specialization finds work for capable agents; I did not count it as a lookup of agents.
- **Goujon AAM/5C DirC (no, could be part).** The RACI (Table 14) names an accountable role per governance activity, and one vignette names an owner of an agent ("No ownership relation is defined", `prior-work/mapping-aam5c.md:390`).
- **Provider per capability for DirC.** I counted a registry keyed by capability that names its provider (AEON, AOS). I did not count a registry of agents whose cards list capabilities (Google, AgentCore, LangGraph); a reader who does would move those DirC cells to "part".
- **LifeOS DirC (yes, could be part).** One responsibility has two domains and one has none, so not every responsibility has exactly one accountable area.
