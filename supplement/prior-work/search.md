---
title: "WARM prior work: a documented search for reference models, architectures and taxonomies of AI agent systems"
date: 2026-11-11
author: subagent for sagan
tags: [research, warm, agents]
---

# A documented search for reference models of agent systems

## 1. Protocol (written before any search was run)

**Question.** Which published works propose a general model of the parts of a system in which LLM agents work, and say how the parts relate? "The same kind of thing" as WARM v0.11 (a model with layers People / Domains / Platform / Infrastructure / Providers, 24 platform services in six groups, and a domain layer in which an area of work has a charter).

**Date of search.** 2026-11-11. **Publication window.** 2023-01-01 to 2026-11-11.

**Inclusion rule.** Include a source if it proposes a general model, architecture or taxonomy of the parts of an LLM-agent system or platform: a layered model, a component taxonomy, a reference architecture, a capability map, or a maturity model that names components. Vendor-published or not.

**Exclusion rule.** Exclude:
- E1 single-domain architectures (for example "agents for network operations", "agents for healthcare");
- E2 security-only threat or risk taxonomies, unless they include a component model of the whole system;
- E3 surveys or taxonomies of agent reasoning methods (planning, reflection, memory techniques) with no system component model;
- E4 product documentation that only lists one product's features;
- E5 outside the date window, not about LLM agents, or not a model at all (benchmarks, opinion, single technique, protocol spec for one interface only).

**Databases and instruments.**
1. arXiv API, `http://export.arxiv.org/api/query`, `search_query=<string> AND submittedDate:[202301010000 TO 202611112359]`, `sortBy=relevance`, `max_results=100`. Hit count = `opensearch:totalResults`.
2. OpenAlex API, `https://api.openalex.org/works?filter=title.search:<string>,from_publication_date:2023-01-01&sort=relevance_score:desc&per-page=50`. Hit count = `meta.count`. (OpenAlex chosen over Semantic Scholar because it needs no key and returns exact counts.)
3. General web search (the WebSearch tool of Claude Code, standard mode). No hit count is exposed; the number of result blocks returned is recorded.
4. GitHub search API, `gh api 'search/repositories?q=<string>&sort=stars&per_page=30'`. Hit count = `total_count`.
5. Vendor architecture centers and standards bodies: WebSearch restricted with `allowed_domains` to the vendor's or body's domain, one query each.

**Query strings.** The concept terms are the twelve in the brief. Exact strings, by database:

| ID | Concept | arXiv `search_query` | OpenAlex `title.search` |
|---|---|---|---|
| Q1 | reference architecture | `ti:"reference architecture" AND (abs:agent OR abs:agents OR abs:agentic) AND (abs:LLM OR abs:"language model" OR abs:"foundation model" OR abs:"generative AI")` | `reference architecture agentic` ; `reference architecture LLM agents` |
| Q2 | reference model | `ti:"reference model" AND (abs:agent OR abs:agentic)` | `reference model agentic` |
| Q3 | taxonomy | `ti:taxonomy AND (ti:agent OR ti:agents OR ti:agentic) AND (abs:architecture OR abs:component OR abs:components)` | `taxonomy LLM agent architecture` |
| Q4 | layered architecture | `(ti:layered OR ti:layer OR ti:layers) AND (ti:agent OR ti:agents OR ti:agentic)` | `layered architecture agentic` |
| Q5 | agent platform | `ti:"agent platform" OR ti:"agentic platform" OR ti:"agents platform"` | `agentic AI platform architecture` |
| Q6 | agentic AI | `ti:"agentic AI" AND (ti:architecture OR ti:framework OR ti:model) AND abs:components` | `agentic AI architecture` |
| Q7 | multi-agent system | `ti:"multi-agent" AND ti:architecture AND (abs:LLM OR abs:"language model")` | `LLM multi-agent system architecture` |
| Q8 | agent operating system | `ti:"agent operating system" OR ti:"agentic operating system" OR ti:AgentOS OR ti:"operating system for agents" OR ti:"LLM operating system"` | `agent operating system` |
| Q9 | agent infrastructure stack | `ti:"agent infrastructure" OR ti:"agentic infrastructure" OR (ti:agent AND ti:stack) OR (ti:agentic AND ti:stack)` | `agent infrastructure` |
| Q10 | LLMOps / AgentOps | `ti:AgentOps OR ti:LLMOps OR ti:"agent operations" OR ti:"AgentOps"` | `AgentOps` ; `LLMOps` |
| Q11 | enterprise agent | `ti:enterprise AND (ti:agent OR ti:agents OR ti:agentic) AND (ti:architecture OR abs:"reference architecture" OR abs:layers)` | `enterprise agentic architecture` |
| Q12 | agent mesh | `ti:"agent mesh" OR ti:"agentic mesh" OR ti:"mesh of agents"` | `agentic mesh` |
| Q13 | capability / maturity model | `(ti:"maturity model" OR ti:"capability model" OR ti:"capability map") AND (abs:agent OR abs:agentic)` | `maturity model agentic AI` |
| Q14 | anatomy / harness | `(ti:anatomy OR ti:harness) AND (ti:agent OR ti:agents OR ti:agentic) AND abs:components` | `agent harness architecture` |

Web search strings (W) and GitHub strings (G):

| ID | String |
|---|---|
| W1 | `reference architecture for LLM agent systems` |
| W2 | `agentic AI reference model layers` |
| W3 | `taxonomy of AI agent platform components` |
| W4 | `agent infrastructure stack layers 2026` |
| W5 | `AgentOps reference architecture` |
| W6 | `agentic mesh architecture` |
| W7 | `enterprise agentic AI reference architecture whitepaper` |
| W8 | `agent operating system architecture LLM` |
| W9 | `agentic AI maturity model components` |
| W10 | `"reference architecture" agentic AI site:scholar or journal` (run as `agentic AI reference architecture journal article 2025`) |
| G1 | `agent architecture` (topic search: `"agent architecture" in:name,description,readme`) |
| G2 | `agentic reference architecture` |
| G3 | `agent platform taxonomy` |
| G4 | `awesome agent architecture` |
| G5 | `awesome agentic` (stars>500) |
| G6 | `agentic AI reference architecture` |
| G7 | `agent infrastructure stack` |

Vendor and standards sites (V): one restricted WebSearch each, string `agentic AI reference architecture` (or `AI agent architecture` where the first returns nothing) with `allowed_domains` set to: aws.amazon.com; cloud.google.com; learn.microsoft.com; ibm.com; nvidia.com (incl. developer.nvidia.com); salesforce.com / architect.salesforce.com; databricks.com; snowflake.com; oracle.com; nist.gov; iso.org; ieee.org (standards.ieee.org); linuxfoundation.org, agntcy.org, a2a-protocol.org, aaif.io; owasp.org / genai.owasp.org; cloudsecurityalliance.org; openai.com / cdn.openai.com; anthropic.com; w3.org.

**Screening procedure.**
1. Collect all hits (titles and links); for databases that return more than the page size, screen only the first page (arXiv 100, OpenAlex 50, GitHub 30, web as returned) and record the total. This cap is part of the protocol: a hit beyond the first page was not screened.
2. De-duplicate by arXiv id, DOI, then normalized title.
3. Title screening: keep a hit if its title could plausibly satisfy the inclusion rule (mentions an architecture, model, taxonomy, layers, framework, platform, stack or anatomy of LLM/agentic systems, without an obvious single domain). Title-screen rejects are counted but not listed individually.
4. Abstract/first-page screening for every title-screen pass: include or exclude with the rule code (I or E1–E5) and one line.

**Recorded per included hit.** Title; authors or publisher; date; link (opened); kind of model; top-level components verbatim; (a) area of work / business domain as an entity separate from agents; (b) registry or directory and what its entries are; (c) long-lived vs per-task agents; (d) components with no place in WARM v0.11; adoption evidence with date read. Unopened primaries are marked UNVERIFIED.

**Known-source check.** For each source already listed in the three earlier reports (2026-11-09 platform reference models, 2026-11-09 prior art, 2026-11-11 prior-work reading), record which query (if any) returned it.

## 2. Deviations from the protocol

Recorded so a repeat run can match or correct them.

1. **Semantic Scholar was not used**; OpenAlex was (the protocol allowed either). Google Scholar has no API and was not used; general web search stands in for it.
2. **arXiv Q10** was run as `ti:AgentOps OR ti:LLMOps OR ti:"agent operations"` (the protocol text repeats `ti:"AgentOps"`; the duplicate was dropped). arXiv requires HTTPS (`https://export.arxiv.org/api/query`); the HTTP URL in the protocol returns a 301 with an empty body.
3. **Three web queries were added after the protocol was written**, because the first ten returned mostly the same arXiv papers: W11 `agentic AI control plane reference architecture registry identity policy observability`, W12 `agent platform engineering reference architecture layers`, and a McKinsey-restricted search `agentic AI mesh architecture capabilities` (`allowed_domains: mckinsey.com`). Three included sources (Bain, Digital Applied, Knowlee) were found only by W12.
4. **The `allowed_domains` filter did not restrict results.** Every vendor-restricted search also returned arXiv papers. The vendor rows in section 3 therefore record what came back, not only the vendor's own pages. The Snowflake-restricted search returned no snowflake.com page.
5. **GitHub awesome-lists** (G4, G5) were screened by grepping their READMEs for "reference architecture|reference model|taxonomy|layered|maturity model|operating system|agent os". No entry led to a source outside the result set.
6. **Screening and extraction were split among eight readers** (subagents) working from one written brief that restates the inclusion rule, the exclusion codes and the recording template. Their decisions were checked against the rule, and four were changed. C4 (2603.15021) was recoded from weak INCLUDE to E5, because it is a description notation, not a model of the parts. Three "provisional" includes that were read from an abstract or a landing page only (CSA, Koubaa, Living Mesh) were moved to UNVERIFIED, because the brief requires an opened primary.
7. **Some readers used a fetch tool that returns a model-written summary of a page.** Sources read that way are marked "fetch summary" in section 6; their component names were not checked against the raw page a second time. Sources read from arXiv HTML, PDFs or Zenodo files were read as text.
8. **Exclusion code N** (the source models one subsystem only, such as a control plane or memory) was added at screening time. It applies the inclusion rule ("the parts of an LLM-agent system"). Harness anatomies were included and marked "harness-scoped", because they name the parts around the model.

## 3. Search log

All searches were run on 2026-11-11 between 16:00 and 16:20 MST. Raw responses are not kept in the vault; re-running the strings reproduces the candidate pool, subject to index growth after this date.

### 3.1 arXiv API

Endpoint `https://export.arxiv.org/api/query`, `search_query=(<string>) AND submittedDate:[202301010000 TO 202611112359]`, `sortBy=relevance`, `max_results=100`. Q4 is the only query with more than 100 hits; its hits 101 to 162 were not screened.

| ID | Total hits | Screened |
|---|---|---|
| Q1 reference architecture | 12 | 12 |
| Q2 reference model | 5 | 5 |
| Q3 taxonomy | 35 | 35 |
| Q4 layered | 162 | 100 |
| Q5 agent platform | 24 | 24 |
| Q6 agentic AI | 35 | 35 |
| Q7 multi-agent | 66 | 66 |
| Q8 agent operating system | 20 | 20 |
| Q9 agent infrastructure / stack | 39 | 39 |
| Q10 AgentOps / LLMOps | 37 | 37 |
| Q11 enterprise | 47 | 47 |
| Q12 agent mesh | 1 | 1 |
| Q13 maturity / capability model | 5 | 5 |
| Q14 anatomy / harness | 73 | 73 |
| **Total** | **561** | **499 records, 467 unique ids** |

### 3.2 OpenAlex API

Endpoint `https://api.openalex.org/works?filter=title.search:<string>,from_publication_date:2023-01-01&sort=relevance_score:desc&per-page=50`. Only the first 50 results per string were screened.

| ID | String | Total hits (`meta.count`) | Screened |
|---|---|---|---|
| Q1a | `reference architecture agentic` | 141 | 50 |
| Q1b | `reference architecture LLM agents` | 8 | 8 |
| Q2 | `reference model agentic` | 58 | 50 |
| Q3 | `taxonomy LLM agent architecture` | 6 | 6 |
| Q4 | `layered architecture agentic` | 157 | 50 |
| Q5 | `agentic AI platform architecture` | 38 | 38 |
| Q6 | `agentic AI architecture` | 1,429 | 50 |
| Q7 | `LLM multi-agent system architecture` | 53 | 50 |
| Q8 | `agent operating system` | 159 | 50 |
| Q9 | `agent infrastructure` | 743 | 50 |
| Q10a | `AgentOps` | 13 | 13 |
| Q10b | `LLMOps` | 91 | 50 |
| Q11 | `enterprise agentic architecture` | 263 | 50 |
| Q12 | `agentic mesh` | 90 | 50 |
| Q13 | `maturity model agentic AI` | 16 | 16 |
| Q14 | `agent harness architecture` | 26 | 26 |
| **Total** | | **3,291** | **607 records** |

OpenAlex returns a large amount of self-published material (Zenodo, SSRN, small journals). It was screened under the same rule as everything else; adoption evidence in section 6 shows how little uptake most of it has.

### 3.3 General web search

Claude Code's WebSearch tool, standard mode. The tool shows no total; "Links" is the number of result links it returned.

| ID | Exact string | Links |
|---|---|---|
| W1 | `reference architecture for LLM agent systems` | 10 |
| W2 | `agentic AI reference model layers` | 10 |
| W3 | `taxonomy of AI agent platform components` | 10 |
| W4 | `agent infrastructure stack layers 2026` | 10 |
| W5 | `AgentOps reference architecture` | 27 |
| W6 | `agentic mesh architecture` | 26 |
| W7 | `enterprise agentic AI reference architecture whitepaper` | 10 |
| W8 | `agent operating system architecture LLM` | 10 |
| W9 | `agentic AI maturity model components` | 10 |
| W10 | `agentic AI reference architecture journal article 2025` | 10 |
| W11 (added) | `agentic AI control plane reference architecture registry identity policy observability` | 10 |
| W12 (added) | `agent platform engineering reference architecture layers` | 10 |

### 3.4 Vendor architecture centers, standards bodies and consortia

WebSearch with `allowed_domains`. String `agentic AI reference architecture` unless stated. "Own-domain pages" counts results on the named domain; the rest were arXiv papers (see deviation 4).

| Body | Domains | String (if different) | Links | Own-domain pages | What the own-domain pages were |
|---|---|---|---|---|---|
| AWS | aws.amazon.com, docs.aws.amazon.com | | 10 | 5 | Prescriptive Guidance (already known; being mapped elsewhere), Pluggable Agentic AI Framework blog, lakehouse blog, HIPAA blog |
| Google Cloud | cloud.google.com, docs.cloud.google.com | | 10 | 5 | Architecture Center agentic guides (already known; being mapped elsewhere), multi-tenant, single-agent, multi-agent, Agent Engine patterns |
| Microsoft | learn.microsoft.com | | 9 | 2 | OPC UA agentic solution; adoption maturity model, technology pillar |
| IBM | ibm.com | | 9 | 2 | "The 2026 Guide to AI Agents"; "What is agentic AI?" (explainers, no model) |
| NVIDIA | nvidia.com | | 9 | 3 | Enterprise Reference Architecture for AI factories; retail agentic commerce; OpenShell reference architecture (sandbox) |
| Salesforce | salesforce.com | | 10 | 3 | Agentforce architecture; The Agentic Enterprise IT architecture; Data 360 architecture |
| Databricks | databricks.com | | 9 | 3 | Industrial AI RA for manufacturing; "What is agentic AI" |
| Snowflake | snowflake.com | | 9 | 0 | none |
| Oracle | oracle.com | | 9 | 3 | OCI agent platform deployment blueprint; video analysis blueprint; OCI observability for agentic AI |
| NIST | nist.gov | `AI agent architecture reference model standard` | 9 | 0 | none (the AI Agent Standards Initiative appeared only in a result summary) |
| ISO/IEC JTC 1/SC 42 | iso.org | `AI agent systems standard architecture` | 9 | 0 | none |
| IEEE | ieee.org, standards.ieee.org | `agentic AI architecture standard working group` | 9 | 4 | P3709, P7022, P3833, P3154.1 project pages |
| Linux Foundation agent projects | linuxfoundation.org, agntcy.org, docs.agntcy.org, a2a-protocol.org, aaif.io | `agent architecture reference model framework` | 10 | 0 | none |
| OWASP | owasp.org, genai.owasp.org | `agentic AI architecture components threat model` | 10 | 1 | DSOMM mappings |
| Cloud Security Alliance | cloudsecurityalliance.org | `agentic AI reference architecture layers` | 10 | 5 | AI Agents: Architecture and Control Plane; Zero Trust for agentic AI (two versions); Agentic Secure Development Lifecycle; agentic IAM |
| OpenAI | openai.com, cdn.openai.com, developers.openai.com | `building agents guide architecture components` | 10 | 10 | practical guide (known), building-agents track, Agents API architecture, cookbooks, harness engineering (known) |
| Anthropic | anthropic.com, claude.com | `building agents architecture components guide` | 10 | 10 | building effective agents (known), architecture patterns guide, managed agents (known), harness design, containment, enterprise guide |
| W3C | w3.org | `AI agent architecture community group report` | 9 | 8 | community group pages (protocol, memory interop, web agents, semantic communication, identity registry, conformance) |
| McKinsey (added) | mckinsey.com | `agentic AI mesh architecture capabilities` | 9 | 7 | "Seizing the agentic AI advantage", "Rethinking enterprise architecture for the agentic era", others |

### 3.5 GitHub search

`gh api -X GET search/repositories -f q=<string> -f sort=stars -f per_page=30`.

| ID | String | Total (`total_count`) | Screened |
|---|---|---|---|
| G1 | `"agent architecture" in:name,description,readme` | 114,821 | 30 |
| G2 | `agentic reference architecture` | 742 | 30 |
| G3 | `agent platform taxonomy` | 16 | 16 |
| G4 | `awesome agent architecture` | 70 | 30 |
| G5 | `awesome agentic stars:>500` | 133 | 30 |
| G6 | `agentic AI reference architecture` | 397 | 30 |
| G7 | `agent infrastructure stack` | 279 | 30 |
| **Total** | | **116,458** | **196** |

GitHub search ranks by stars, so its first pages are dominated by large app collections and skill lists. Two repositories passed screening: microsoft/multi-agent-reference-architecture (already known) and Sarony11/agentic-infrastructure-bootstrap.

## 4. Would the search have found the already-known sources?

"Found by" lists the queries whose screened results contained the source. "Not found" means no query in this protocol returned it within the screening cap.

### 4.1 The 34 sources of the 2026-11-09 platform survey

| # | Source | Found by |
|---|---|---|
| 1 | Lu et al., arXiv 2311.13148 | arXiv Q1; OpenAlex Q1a, Q2; W1; 10 vendor-restricted searches |
| 2 | Zhou et al., arXiv 2408.02920 | arXiv Q3; W3; LF-restricted search |
| 3 | Alenezi, arXiv 2602.10479 | W1, W7, W10, W11; 12 vendor-restricted searches. Not by arXiv or OpenAlex queries |
| 4 | Derouiche et al., arXiv 2508.10146 | Not found |
| 5 | AIOS, arXiv 2403.16971 | arXiv Q8, Q10; OpenAlex Q8; W8 |
| 6 | AgentOS, arXiv 2603.08938 | arXiv Q8 |
| 7 | NIST CAISI AI Agent Standards Initiative | Not found (named in one result summary only) |
| 8 | Linux Foundation Agentic AI Foundation | Not found |
| 9 | MCP architecture overview | Not found |
| 10 | A2A specification | Not found |
| 11 | AGNTCY docs | Not found (an AGNTCY-authored protocol paper, arXiv 2511.19699, was found) |
| 12 | OWASP Top 10 for Agentic Applications | Not found (named in one result summary only) |
| 13 | CSA MAESTRO | Not found as a link (named in the CSA search summary) |
| 14 | IEEE P3394 | Not found as a link (named in the IEEE search summary) |
| 15 | IEEE P3931 | Not found |
| 16 | OpenTelemetry GenAI conventions | Not found |
| 17 | Claude Managed Agents overview (docs) | Not found |
| 18 | Anthropic engineering, Managed Agents post | Anthropic-restricted search |
| 19 | Claude Agent SDK and Claude Code overviews | Not found |
| 20 | AWS Bedrock AgentCore docs | Not found (AWS AgentOps blog on AgentCore was found) |
| 21 | Google Gemini Enterprise Agent Platform | Not found |
| 22 | Google ADK | Not found |
| 23 | Microsoft Foundry Agent Service | Not found |
| 24 | Microsoft Agent Framework | Not found |
| 25 | OpenAI Agents SDK docs | Not found |
| 26 | OpenAI Agents guide (API docs) | Not found as that page; a sibling page (Agents API architecture) was found |
| 27 | LangSmith Deployment / Agent Server | Not found |
| 28 | Cloudflare Agents | Not found |
| 29 | Letta docs | Not found (Letta appears inside an awesome-list README) |
| 30 | Temporal AI cookbook | Not found |
| 31 | Trivedy, "The Anatomy of an Agent Harness" | Not found |
| 32 | Builder Methods Agent OS | Not found |
| 33 | StrongDM software factory | Not found |
| 34 | A2A project home | Not found |

**Reading.** The protocol found 6 of the 34 (1, 2, 3, 5, 6, 18). The other 28 are product documentation, protocol specifications and standards projects. Most fall under exclusion E4 or E5 of this protocol, so a search for reference models is not expected to return them. The earlier survey's purpose (how products decompose a platform) needed product pages; this search's purpose does not. Derouiche et al. (4) is the one academic miss: its title has "Agentic AI Frameworks: Architectures, Protocols" and matched no query string.

### 4.2 Sources of the prior-art report (2026-11-09) and the prior-work reading (2026-11-11)

| Source | Found by |
|---|---|
| Yu et al., arXiv 2610.14818 (being mapped elsewhere) | arXiv Q1, Q11; OpenAlex Q1a |
| Zhu, arXiv 2608.08516 (being mapped elsewhere) | arXiv Q4 |
| Goujon AAM/5C, arXiv 2610.30221 (being mapped elsewhere) | arXiv Q2; OpenAlex Q2 |
| Microsoft Multi-Agent Reference Architecture (being mapped elsewhere) | GitHub G2 |
| AWS Prescriptive Guidance, agentic AI (being mapped elsewhere) | AWS-restricted search |
| Google Cloud agentic AI architecture (being mapped elsewhere) | Google-restricted search |
| Tallam five-plane, arXiv 2606.12320 | OpenAlex Q1a |
| Athenian Academy, arXiv 2504.12735 | arXiv Q4; OpenAlex Q4 |
| Nechepurenko and Shuvalov, arXiv 2605.03310 | arXiv Q4, Q7; OpenAlex Q4, Q7 |
| PBSAI, arXiv 2602.11301 | arXiv Q1, Q7, Q11 |
| Zhong and Zhu, AI Harness Engineering, arXiv 2605.13357 | arXiv Q14 |
| Schluntz and Zhang, "Building effective agents" | Anthropic-restricted search |
| OpenAI, "A practical guide to building agents" | OpenAI-restricted search |
| Lopopolo, "Harness engineering" (OpenAI) | OpenAI-restricted search |
| Guo et al., arXiv 2602.03128 | arXiv Q7 |
| arXiv 2611.03066, 2608.15832, 2608.20201, 2606.17368, 2411.12357 (titles seen in prior reading) | Not found. Each exists on arXiv (checked by exact-title query); none of the 14 strings matches its title |
| 12-factor agents (HumanLayer), AutoGen 2308.08155, LangChain multi-agent docs, DDD-for-agents posts, Koo and Chung (2026) | Not found |
| Young, effective harnesses; Trivedy; agent surveys 2308.11432, 2309.07864, 2309.02427 (CoALA), 2402.01680, 2606.20683, 2504.01963; Tang et al. (Frontiers) | Not found (CoALA appears only as the awesome-language-agents repository in G4) |
| Team Topologies, CNCF Platforms White Paper, internaldeveloperplatform.org, OASIS SOA-RM, Ontolingua | Not found (not agent-specific or before the window, by design) |
| Software-factory sources (StrongDM, Shapiro, Factory 2.0, Gas Town, BMAD, Pocock) | Not found |

**Reading.** The strings find titled reference architectures well and miss papers whose titles say "framework", "frameworks", "networks", "restructuring" or "ontology" without "architecture", "reference", "taxonomy" or "layer". A repeat should add `ti:framework AND ti:agentic AND abs:layers` and `ti:"agentic AI frameworks"` to arXiv if those papers matter.

## 5. Screening results

### 5.1 Included sources

61 sources meet the inclusion rule: 13 already known and 48 new. The 13 known ones were not re-read (as instructed); they are counted from the earlier reports: Lu et al. 2311.13148, Zhou et al. 2408.02920, Alenezi 2602.10479, AIOS 2403.16971, AgentOS 2603.08938, Zhong and Zhu 2605.13357, Nechepurenko and Shuvalov 2605.03310, Yu et al. 2610.14818, Zhu 2608.08516, Goujon 2610.30221, Microsoft MARA, AWS Prescriptive Guidance, Google Cloud agentic architecture guides. The 48 new ones are detailed in section 6.

Six known sources that the search returned do not meet this protocol's rule and are not counted as included: Tallam 2606.12320 (E2, runtime security governance), Athenian Academy 2504.12735 (E1, AI art), Anthropic "Building effective agents" (E3), OpenAI practical guide (E3), OpenAI "Harness engineering" (E5) and Anthropic's Managed Agents post (E4). A seventh, PBSAI 2602.11301 (E2), is listed in table 5.3.

### 5.2 Excluded after reading the primary

| Title | Link | Found by | Code | Reason |
|---|---|---|---|---|
| AgentOps: Enabling Observability of LLM Agents (Dong, Lu, Zhu; 101 citations) | https://arxiv.org/abs/2411.05285 | arXiv Q10; OpenAlex Q10a | N | Taxonomy of traceable artifacts (span types) for one agent's run; observability only |
| Agentic Configuration Management (ACM): A Reference Configuration Model for Governed Agentic Systems | https://arxiv.org/abs/2608.11166 | OpenAlex Q2; LF-restricted search | N (borderline) | Configuration-governance subsystem. Its item types ("agents, prompts, skills, composite subsystems, workflows, tools, language models, policies, assurance evidence, runtime observations") come close to a parts list; a lenient reader could include it |
| AgentStripes: An Evidence-Graded Maturity Model for AI Agents | https://arxiv.org/abs/2610.18603 | arXiv Q13; OpenAlex Q13 | E5 | Rating rubric for one released agent (12 areas, 40 capabilities), not a model of system parts |
| Agentic Risk & Capability (ARC) Framework | https://arxiv.org/abs/2512.22211 | arXiv Q6 | E2 | Risk-governance framework; components are one agent's "LLM", "Tools", "Instructions", "Memory" |
| Architectures for Building Agentic AI (Nowaczyk) | https://arxiv.org/abs/2512.09458 | W10; 9 vendor-restricted searches | E3 | Modules of one agent's loop ("goal manager, planner, tool-router, executor, memory, verifiers, safety monitor, telemetry") |
| ASTELD: A Six-Axis Classification Framework for Autonomous AI Agents | https://arxiv.org/abs/2608.05201 | W3 | E5 | Classification axes for comparing platforms, not parts |
| Describing Agentic AI Systems with C4: Lessons from Industry Projects | https://arxiv.org/abs/2603.15021 | IBM- and Microsoft-restricted searches | E5 | Description notation (C1 to C4 levels). Noted: "it is the Tasks that require inputs and produce outputs, not the Agents themselves" |
| Pylon-7: A 7-Layer Reference Model for AI Agent Workflows | https://doi.org/10.5281/zenodo.18808598 | OpenAlex Q2 | E3 | Layers are depth-of-action stages of one workflow, defined for infrastructure operations |
| Agency as an Architecture Layer (El Hassani, Research Square) | https://www.researchsquare.com/article/rs-10943728/latest.pdf | OpenAlex Q4, Q11 | N | Authority metamodel only; the same author's Charterion is the system model and is included |
| Agent Task Control Plane (Ran) | https://zenodo.org/records/22259004 | OpenAlex Q1a | N | Says it is a task control plane, not a whole platform |
| A Technical Architecture Framework for Enterprise AI Agents (EAAAM) | https://zenodo.org/records/20508015 | OpenAlex Q11 | E3 | Six layers of one agent's internals |
| ONUG, Large Enterprise Requirements to Scale Agentic AI, Part A | https://onug.net/?p=118621 | W7 | N | Landing text describes an identity/policy/zero-trust overlay; full paper not public |
| Anthropic/Claude, Building effective AI agents: Architecture patterns | https://claude.com/resources/guides/building-effective-ai-agents/common-architecture-patterns | Anthropic-restricted search | E3 | Catalog of orchestration patterns |
| Microsoft Learn, Agentic AI adoption maturity model | https://learn.microsoft.com/en-us/agents/adoption-maturity-model | W9; Microsoft-restricted search | E5 | Organizational adoption pillars, not system parts |
| IEEE P3709, Framework and Technical Requirements of Agentic AI | https://standards.ieee.org/ieee/3709/12159/ | IEEE-restricted search | E5 | Active PAR (approved 2025-09-10); no published content |
| Governed Agentic AI for Software Platforms (Karuppuchamy, IEEE SoutheastCon 2026) | https://doi.org/10.1109/southeastcon63549.2026.11475963 | OpenAlex Q1a, Q5 | N (UNVERIFIED) | Paywalled; abstract describes a four-stage governance control plane |
| Nine GitHub awesome-lists and pattern repositories (gtzheng/Awesome-Agentic-System-Design, ai-boost and walkinglabs awesome-harness-engineering, nibzard/awesome-agentic-patterns, NeuZhou/awesome-ai-anatomy, subinium/awesome-agent-frameworks, dyronrh/awesome-agentops-landscape, devwithmohit/ai-agent-architecture-patterns, eshwarvijay/agent-architecture) | github.com/<name> | G4, G5, G2, G6 | E5 | Lists and pattern catalogs; README scan found no model outside the result set |

### 5.3 Excluded or not screened at abstract or first-page level

Every hit that passed title screening and is not in 5.1 or 5.2 is listed here. Rows that group several hits give the count in the title cell.

| Title | Link | Found by | Code | Reason (abstract or first page) |
|---|---|---|---|---|
| Harnessing Agent Skills: Architectural Patterns and a Reference Architecture for Skill-Mediated LLM Agents | https://arxiv.org/abs/2606.20631 | arXiv Q1; OA Q1a, Q1b, Q14; W1 | N | Reference architecture of skill handling inside the harness only |
| Swiss Cheese Model for AI Safety: A Taxonomy and Reference Architecture for Multi-Layered Guardrails of FM Based Agents | https://arxiv.org/abs/2408.02205 | arXiv Q1, Q3; OA Q2 | E2 | Guardrail taxonomy; no component model of the whole system |
| Containing the Autonomous Operator: A Defense-in-Depth Framework and Reference Architecture for Securing AI Agents on Kubernetes | https://arxiv.org/abs/2610.02861 | arXiv Q1 | E2 | Security architecture for agents on Kubernetes |
| The PBSAI Governance Ecosystem (already known, title-only in prior reading) | https://arxiv.org/abs/2602.11301 | arXiv Q1, Q7, Q11 | E2 | Reference architecture for securing AI estates |
| When Agentic Trust Crosses Organizational Boundaries: ... a Reference Model for Trust Evidence | https://arxiv.org/abs/2609.22961 | arXiv Q1, OA Q2 | N | Model of cross-domain trust evidence only |
| AgentScope: A Flexible yet Robust Multi-Agent Platform | https://arxiv.org/abs/2402.14034 | arXiv Q5 | E4 | Describes one platform's features |
| AgentKernel: The Trust-Native Agentic Operating System | https://arxiv.org/abs/2609.29647 | arXiv Q8, Q10; OA Q8 | E2 | Security enforcement substrate (identity, input mediation, memory governance, execution control) |
| KAOS: Large Model Multi-Agent Operating System | https://arxiv.org/abs/2406.11342 | arXiv Q8, Q10; OA Q8 | E4 | One OS built on Kylin |
| Architecting AgentOS: From Token-Level Context to Emergent System-Level Intelligence | https://arxiv.org/abs/2602.20934 | arXiv Q8 | E3 | Context management inside the model ("Reasoning Kernel") |
| Agent Mesh: Reliability Primitives for Non-Idempotent Agent Delegation | https://arxiv.org/abs/2608.26225 | arXiv Q12; OA Q12 | N | Failure study of retry/breaker primitives |
| AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges | https://arxiv.org/abs/2505.10468 | arXiv Q3 | E3 | Conceptual distinction and applications; no system component model in abstract |
| Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents (Arunkumar, Gangadharan, Buyya) | https://arxiv.org/abs/2601.12560 | arXiv Q3; W3 | E3 | Taxonomy is one agent's modules: "Perception, Brain, Planning, Action, Tool Use, and Collaboration" |
| MI9: An Integrated Runtime Governance Framework for Agentic AI | https://arxiv.org/abs/2508.03858 | arXiv Q6 | E2 | Six runtime safety controls only |
| A Baseline Assessment for the Agentic Web Technology Stack | https://arxiv.org/abs/2610.13703 | arXiv Q9 | E5 | Benchmark of technology combinations |
| EnterpriseLab: A Full-Stack Platform for developing and deploying agents in Enterprises | https://arxiv.org/abs/2603.21630 | arXiv Q9 | E4 | One training/deployment platform |
| A Survey on AgentOps: Categorization, Challenges, and Future Directions | https://arxiv.org/abs/2508.02121 | arXiv Q10; OA Q10a | E5 | Categorizes operations tasks (monitoring, anomaly detection, root cause, resolution), not system parts |
| Organizational Control Layer: Governance Infrastructure at the Execution Boundary | https://arxiv.org/abs/2606.04306 | arXiv Q4 | N | One approval/blocking layer |
| A Layered Protocol Architecture for the Internet of Agents | https://arxiv.org/abs/2511.19699 | arXiv Q4; OA Q4 | E5 | Communication protocol stack only |
| Scaling LLM-Driven Multi-Agent Systems: Design Principles and Architectural Scalability Analysis | https://arxiv.org/abs/2607.27942 | arXiv Q7; OA Q7 | E3 | Workflow-graph topology of agents solving one task |
| Multi-agent LLMs on the Cloud-Edge-IoT Continuum: A Systematic Mapping Study | https://arxiv.org/abs/2610.28702 | arXiv Q7 | E1 | IoT deployments |
| Foundations of Proactive Agents: Principles, Technical Layers, and Proactivity-Gym | https://arxiv.org/abs/2609.37267 | arXiv Q4 | E3 | Design space for proactive behavior of one agent |
| Layered Mutability: Continuity and Governance in Persistent Self-Modifying Agents | https://arxiv.org/abs/2604.14717 | arXiv Q4 | E3 | Layers are pretraining, alignment, self-narrative, memory, weights |
| A Reference Architecture for Autonomous Networks: An Agent-Based Approach | https://arxiv.org/abs/2503.12871 | OA Q1a; VNIST | E1 | Network operations |
| Leveraging AI Agents for Autonomous Networks: A Reference Architecture and Empirical Studies | https://arxiv.org/abs/2509.08312 | OA Q1a; VIBM | E1 | Network operations |
| Agentic IoT: Architectures, Applications, and Challenges Toward the Internet of Agents | https://arxiv.org/abs/2607.04219 | VSFDC | E1 | IoT |
| Socio-technical aspects of Agentic AI | https://arxiv.org/abs/2601.06064 | VIBM | E3 | Perception-planning-execution loop of one agent plus orchestration overview |
| Multi-Model Agentic Systems Taxonomy (MMAS-T) and reference architecture | https://doi.org/10.1109/icaiset66439.2026.11541520 | OA Q1b, Q2, Q3, Q7 | N | Classes of models only |
| Agents Are Not Users: A Reference Architecture for Governed Agent Actions in Third-Party Products | https://doi.org/10.5281/zenodo.21133995 | OA Q1a | N | Action authorization only |
| The Temporal Governance Architecture: A Reference Model for Autonomous Multi Agent Systems | https://doi.org/10.5281/zenodo.21326292 | OA Q1a, Q2 | E2 | Governance scoring primitives |
| Agent Trust: reference architecture for the governance of SI agents (AT-ARCH-001) | https://doi.org/10.5281/zenodo.23483885 | OA Q1a | N | A governance layer over agents, not the system |
| Governance-Gated Execution as an Agentic Zero-Trust Reference Model | https://doi.org/10.5281/zenodo.20180230 | OA Q2 | E2 | Zero-trust controls |
| Governing Autonomous AI Agents: A Two-Layer Architecture | https://doi.org/10.5281/zenodo.19923332 | OA Q4 | E2 | Security governance |
| Capability Lattice and Governance Architecture for Agentic Systems | https://doi.org/10.5281/zenodo.20371646 | OA Q14 | E2 | Threat-bounding lattice over harness rings |
| The five-layer trust stack for agent-to-agent coordination | https://doi.org/10.21079/11681/50507 | OA Q4 | E2 | Trust/security between agents |
| AEGIS: Agent Execution Governance and Integrity Standard | https://doi.org/10.2139/ssrn.6392459 | OA Q1a | E2 | Action accountability; abstract not available |
| Standardizing AI Agent Protocols: Definitions, Layered Architectures | https://doi.org/10.63282/3050-9262.ijaidsml-v7i1p109 | OA Q4 | E5 | Protocol layering |
| Reference Architecture & Interface Contracts for a Stratified, Constraint-Governed Agent Stack (Spanda) | https://doi.org/10.5281/zenodo.18810121 | OA Q14 | E3 | Module boundaries of one cognitive agent design |
| The PTSA Framework: An Enterprise Architecture for Autonomous AI Agents | https://doi.org/10.32628/cseit2410612395 | OA Q11 | E3 | Four components of one agent (personality, task, skill, accountability) |
| Multi-Agent Architecture for Enterprise AI Orchestration (Dhayakar) | https://doi.org/10.48047/jocaaa.2025.34.11.13 | OA Q11 | E3 | Review of ReAct, memory, planning paradigms |
| The Enterprise Agentic Mesh: Semantic Control Planes | https://doi.org/10.29322/ijsrp.15.12.2025.p16803 | OA Q12 | N | Networking/control plane layer only |
| Enterprise Agent Mesh Fabric for Financial Services | https://doi.org/10.5281/zenodo.20738299 | OA Q12 | E1 | Financial services |
| From Navigation to Intent: Architecture of the Agentic Enterprise | https://doi.org/10.5281/zenodo.21307542 | OA Q11 | E5 | Paradigm essay (intent interface layers), no component model in abstract |
| From AIOps to AgentOps: SLOs and Error-Budget-Governed Autonomy | https://doi.org/10.30574/wjaets.2026.21.1.0466 | OA Q10a | N | Service-level indicators only |
| Autonomous AI agents in enterprise systems: A review of architectural gaps | https://al-kindipublisher.com/index.php/jcsts/article/view/13630 | OA Q11 | E5 | Literature review of themes |
| LLMOps: Definitions, Framework and Best Practices; MLOps, LLMOps, FMOps, and Beyond; Three Essential Elements of the LLMOps Tech Stack; LLMOps, AgentOps, and MLOps for Generative AI | (OpenAlex W4403212614, W4405092785, W4393082163, W4411716463) | OA Q10a, Q10b | E5 | Model operations, not LLM-agent system parts |
| AgentOps-Bench, AgentOps Replay, Clinical AgentOps, 8-Ball Effect | (OpenAlex Q10a) | OA Q10a | E5/E1 | Benchmark, replay tool, clinical domain, activation technique |
| Agentic Mesh (Wisdom Hill essay "5. The Agentic Mesh") | https://doi.org/10.5281/zenodo.23487258 | OA Q12 | E5 | Market essay |
| Architectural Patterns for Scalable Multi-Agent LLM Systems | https://doi.org/10.1109/fine71157.2026.00045 | OA Q7 | E5 | Pattern catalog (four patterns), not a model of parts |
| Agentic AI Architectures: A Survey of Patterns, Memory Systems, and Protocols | https://doi.org/10.6084/m9.figshare.34741932 | OA Q6 | E3 | Survey of reasoning patterns and memory |
| Multi-Agent LLM Systems: Architectures, Coordination, and Evaluation (2025) | https://doi.org/10.5281/zenodo.19597158 | OA Q7 | E3 | POMDP formalization and coordination protocols |
| The Systems Architecture of LLM Multi-Agent Systems: Routing, Memory, and Resource Optimisation | https://doi.org/10.21863/ijkbcs/2026.14.1.004 | OA Q7 | N | KV-cache and token overhead |
| Registry, Compiler, and Cloud Memory | https://doi.org/10.5281/zenodo.20738981 | OA Q8 | N | Memory and communication mechanism |
| Agent Centric Operating System – A Comprehensive Review | https://doi.org/10.32388/xpjyho | OA Q8 | E5 | Review of operating systems |
| Comprehensive Survey of LLM-based Agent Operating Systems (Chinese) | https://doaj.org/article/b1b5b901008540628ba8fcb0b6318ad4 | OA Q8 | E5 | Survey of others' Agent OS designs; no own model in abstract |
| Toward Securing AI Agents Like Operating Systems | https://arxiv.org/abs/2605.14932 | OA Q8 | E2 | Security analysis |
| The Azure Operating Model for Agentic Systems (Apress chapter) | https://doi.org/10.1007/979-8-8688-3222-2_1 | OA Q8 | E4 | One vendor's services; paywalled |
| Agentic AI on AWS — Production Reference Architecture (Zenodo) | https://doi.org/10.5281/zenodo.23215140 | OA Q1a | E4 | One vendor's stack |
| Enterprise Agentic AI: A Reference Architecture for MCP, RAG, Multi-Agent Systems (Bothraj) | https://doi.org/10.5281/zenodo.21740332 | OA Q1a | E5 | Implementation white paper; abstract names technologies, not a model |
| A Systematic Review of Agentic AI - Architectures, Evaluation, and Safety (Ali) | https://doi.org/10.5281/zenodo.18246385 | OA Q6 | E3 | Taxonomy of agent capabilities (interfaces, memory, reasoning, tool use ...) |
| The Age of Autonomous Agents: A Bibliometric Review | https://doi.org/10.63646/kpqm1958 | OA Q6 | E5 | Bibliometrics |
| Long-Horizon AI Agents and Managed Agent Harnesses (Singh) | https://doi.org/10.5281/zenodo.23046689 | OA Q14 | E5 | Practice report |
| Agent Execution Harnesses: Volume I (Mamun) | https://doi.org/10.5281/zenodo.23530918 | OA Q14 | E5 | Synthesis of others' harness layers |
| The Empire, Long Divided, Must Unite: Architectural Convergence in Three LLM Agent Harnesses | https://arxiv.org/abs/2608.23953 | OA Q14 | E5 | Case comparison of three harnesses |
| Portable Agent Harness Architecture (Longmire) | https://doi.org/10.5281/zenodo.20112631 | OA Q14 | N | Governance meta-harness pattern |
| ArchiMate models of an AI-agent reference architecture (Twente MSc) | https://doi.org/10.5281/zenodo.22914640 | OA Q2 | E1 | Data-driven decision making in retail |
| From Data Platforms to Agentic AI: RA on the Lakehouse | https://doi.org/10.5281/zenodo.22807069 | OA Q1a, Q5 | N | Data-platform view; logistics example |
| From Pipelines to Agent Fabrics | https://doi.org/10.71238/snnst.v1i02.237 | OA Q2 | N | Data platform for small-model fleets |
| Governance-Aware Agentic AI for Enterprise Engineering Systems | https://doi.org/10.5281/zenodo.21264295 | OA Q2 | E2 | Controls for planning, tool invocation, data access, escalation |
| Agent Governance Maturity Model v1.0 (Hasbini) | https://mahasbini.org/papers/agent-governance-maturity-model/ | OA Q2 | E2 | Thirty-five security/governance controls |
| ASMM-AI organizational maturity model | https://doi.org/10.9790/0661-2802022631 | OA Q13 | E5 | Organizational maturity, no system components in abstract |
| Beyond Agentic Operating Systems: A Governance-Centric Architecture | https://doi.org/10.5281/zenodo.22682679 | OA Q8 | E5 | Review of agentic OS landscape |
| Cryptographically Enforced Governance ... Y.I.N. Gateway | https://doi.org/10.5281/zenodo.19117751 | OA Q5 | E4 | Patent defensive publication for one gateway |
| Enterprise Agentic Technology Reference Architecture (Goniwada, Apress chapter) | https://doi.org/10.1007/979-8-8688-3109-6_5 | OA Q1a, Q11 | UNVERIFIED | Paywalled chapter; abstract has no component list |
| Enterprise Agentic AI Governance & Execution RA (Gurumani); Enterprise AI Agent Ecosystems (Shinde et al.); The Agent Infrastructure Stack (Vatsa, SSRN); AAWDS (Santhanam); Enterprise Anchors (Tadinada); Human Governance as a Distinct Layer (Kwarsick); Four Layers of AI Governance (Chen); ARMM (Newman) | OpenAlex W7166890439, W7171712116, W7165777119, W7159957045, W7134946436, W7171713967, W7171703217, W7171628718 | OA Q1a, Q2, Q4, Q9, Q11 | UNVERIFIED | No abstract in OpenAlex; ResearchGate/SSRN primaries not opened. Not screened beyond title |
| AgentArcEval: An Architecture Evaluation Method for FM-based Agents | https://arxiv.org/abs/2510.21031 | VNIST | E5 | Evaluation method |
| Fetch.ai: An Architecture for Modern Multi-Agent Systems | https://arxiv.org/abs/2510.18699 | arXiv Q7; VISO | E4 | One platform |
| Survey of AI Agent Protocols; AI Agent Communication from Internet Architecture Perspective | https://arxiv.org/abs/2504.16736 ; https://arxiv.org/abs/2509.02317 | VISO; VW3C | E5 | Protocols only |
| Gartner/analyst items, gated white papers (Exadel, OneReach, Niveus, EXL) | see web hits W7 | W7 | UNVERIFIED | Gated behind forms; not opened by rule |
| Glean "7 core components"; Leanware; Vendia LAMP stack; Sevendays component map; Towards AI "7 layers" (member-only); Pravitech; smruti26 | see web hits W2, W3 | W2, W3 | E3 / UNVERIFIED | Single-agent component lists (Glean, Leanware) or not opened |
| OCI blueprint; Oracle five-plane observability; NVIDIA OpenShell RA; NVIDIA AI factory; Databricks industrial RA; AWS HIPAA; AWS lakehouse; Azure OPC UA; Google single/multi-agent and multi-tenant guides | see web hits V* | V* | E4 / E1 / N | One product's deployment, one domain, or one concern (observability, sandbox) |
| AWS AgentOps with AgentCore; Microsoft AgentOps Control Tower; Azure AgentOps toolkit; Databricks Big Book of AgentOps | see W5 | W5 | E4 | Product operations guidance |
| W3C community groups (AI Agent Protocol, Memory Interop, Web Agents, Semantic Agent Communication, Agent Identity Registry, Agent Conformance) | see VW3C | VW3C | E5 | Protocol or conformance work; no architecture report found |
| IEEE P7022, P3833, P3154.1 | see VIEEE | VIEEE | E5 / E1 | Requirements for trustworthiness; proactive HCI agents; talent services |
| Agentic mesh vendor posts (Centizen, AIMultiple, Maxim, Gravitee mesh, JumpCloud, Solo.io, Hatchworks, Sigmoid, Fintricity, Flevy, TCS, IEEE CS, OODA, Solace, Auxiliobits, Ema, Knowlee glossary) | see W6 | W6 | E5 / E4 | Definitions, product pages or marketing; McKinsey and Broda screened separately |
| Agent infrastructure stack posts (GMI Cloud, Bitloops, Toolradar, SocioLogic, AI Agent Rank, Pulse, Blaxel) | see W4 | W4 | E5 | Listicles; not opened beyond result text. Shakudo, Augment and O'Reilly screened separately |
| Control-plane posts (Fiddler, Speakeasy x2, Agentic Stack, Obot, Gravitee control plane / productizing / API management) | see W11 | W11 | N | Control plane only |

## 6. The 48 newly found included sources

Read on 2026-11-11. "Read as" says how the primary was read: **text** (arXiv HTML, PDF or Zenodo file read as text, quotes verbatim) or **fetch summary** (a model-written summary of the page; names were requested verbatim but not re-checked). Citation counts are OpenAlex `cited_by_count` on 2026-11-11 unless stated. Statements about WARM are inferences and are marked so in section 7.

### 6.1 Identity, kind and adoption

| # | Title | Authors / publisher | Date | Link opened | Kind | Found by | Adoption evidence (2026-11-11) | Read as |
|---|---|---|---|---|---|---|---|---|
| 1 | The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems (AOS-0001, draft v0.8) | Ankur Sharma, Deep Shah | 2026-08-04 | https://arxiv.org/pdf/2608.03214 | reference architecture (two planes, semantic object model, maturity model) | arXiv Q8, Q10; OpenAlex Q1a, Q8; W5; 12 vendor-restricted searches | 0 citations; reference implementation "aos-core" named, no repository found; companion specs AOS-0002 to 0005 "Planned" | text (199-page PDF, sections read) |
| 2 | Agent Operating Systems (AOS): Integrating Agentic Control Planes into, and Beyond, Traditional Operating Systems (AOS-0000; precursor of #1) | Ankur Sharma, Deep Shah | 2026-06-01 | https://arxiv.org/pdf/2606.01508 | reference architecture / component taxonomy (OS analogy) | arXiv Q8, Q10; OpenAlex Q8 | 3 citations | text |
| 3 | Towards an Agent Operating System - Lessons from Classical and Cloud OS | Gosia Steinder, Hubertus Franke (IBM T.J. Watson Research Center); IEEE ICWS 2026 | 2026-07-27 | https://arxiv.org/html/2607.25076 | component taxonomy (13 platform primitives) | arXiv Q8, Q10; OpenAlex Q8 | 0 citations; prototype github.com/rossoctl/rossoctl, 304 stars | text |
| 4 | Agentic Service-Oriented Computing: A Manifesto for the Next Frontier of Service-Oriented Computing | Beheshti, Chang, Benatallah, Casati, Dustdar, Fox, Sheng, Wang, Yang, Zomaya | 2026-07-14 | https://arxiv.org/html/2607.12619 | layered reference architecture ("ASOC Stack") plus principles | CSA-restricted search | 0 citations; manifesto, no implementation | text |
| 5 | Orchestrating Agents and Data for Enterprise: A Blueprint Architecture for Compound AI | Kandogan, Bhutani, Zhang, Chen, Gurajada, Hruschka (Megagon Labs) | 2025-04-10 | https://arxiv.org/html/2504.08148 | reference architecture (blueprint) | arXiv Q11; OpenAlex Q11 | 23 citations | text |
| 6 | Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture (EDDOps) | Xia, Lu, Zhu, Xing, Zhao, Zhang (CSIRO Data61, UNSW) | v1 2024-11-21, v3 2025-11-17 | https://arxiv.org/html/2411.13768 | reference architecture plus process model | arXiv Q1; OpenAlex Q1a, Q1b, Q2; W1, W5 | 37 citations | fetch summary (first ~100k characters) |
| 7 | Designing Intelligent Enterprise Agents: A Capability-Aligned Multi-Agent Architecture (CEAD) | John deVadoss | 2026-05-07 | https://arxiv.org/html/2605.08258 | reference architecture (planes) | arXiv Q7, Q11; OpenAlex Q11 | 0 citations | fetch summary |
| 8 | The CASE Framework: A Multi-Disciplinary Control Architecture for Governing Enterprise Agentic AI (borderline: layers are scales of agency) | Telukunta, Lilis, Baron | 2026-08-10 | https://arxiv.org/html/2608.10153 | layered model plus maturity model and 36 controls | arXiv Q11 | 0 citations | fetch summary (first ~100k characters) |
| 9 | The Orchestration of Multi-Agent Systems: Architectures, Protocols, and Enterprise Adoption | Adimulam, Gupta, Kumar | 2026-01-20 | https://arxiv.org/html/2601.13671 | reference architecture (orchestration layer) | arXiv Q11; OpenAlex Q11 | 40 citations | fetch summary |
| 10 | Balancing Autonomy and Alignment: A Multi-Dimensional Taxonomy for Autonomous LLM-powered Multi-Agent Architectures | Thorsten Händler | 2023-10-05 | https://arxiv.org/html/2310.03659 | component taxonomy (dimensions, viewpoints, ontology) | arXiv Q3, Q7; OpenAlex Q3 | 51 citations (plus 29 for the conference version) | fetch summary (first ~100k characters) |
| 11 | SALLMA: A Software Architecture for LLM-Based Multi-Agent Systems | Becattini, Verdecchia, Vicario (Univ. of Florence); IEEE SATrends 2025 | 2025 | https://robertoverdecchia.github.io/papers/SATrends_2025.pdf | reference architecture (two layers) | OpenAlex Q7 | 24 citations; deployed for public-administration information and a business simulation (source states) | text |
| 12 | Beyond the Agent Harness: Boundary Criteria for Software-Factory Orchestration - A Single-Operator Case Study (harness-scoped; coding pipelines) | Lei Hua | 2026-11-03 | https://arxiv.org/html/2611.06946 | layered model with placement rules | arXiv Q14 | 0 citations (8 days old) | fetch summary |
| 13 | The Agentic Company OS: Substrate Inversion for Sustained Enterprise Agent Deployment | Larsen, Moghaddam | 2026-09-11 | https://arxiv.org/html/2609.13334 | layered model (four layers) | arXiv Q11 | no OpenAlex record | fetch summary |
| 14 | Governing the Agentic Enterprise: A Governance Maturity Model for Managing AI Agent Sprawl (AAGMM; governance-scoped) | Vivek Acharya | 2026-03-13 | https://arxiv.org/html/2604.16338 | maturity model with 12 domains | arXiv Q13; OpenAlex Q13 | 9 citations; repo 0 stars | text |
| 15 | Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering (harness-scoped) | Zhou et al. (21 authors; SJTU, SYSU, CMU, OPPO) | 2026-04-09 | https://arxiv.org/html/2604.08224 | harness anatomy / component taxonomy | arXiv Q14 | 112 citations | text |
| 16 | Architecting AgentOps Needs CHANGE | Biswas, Bhatt, Vaidhyanathan (IIIT Hyderabad) | 2026-01-10 | https://arxiv.org/html/2601.06456 | capability map (six capabilities) | arXiv Q10; OpenAlex Q10a | 2 citations | text |
| 17 | From Model Scaling to System Scaling: Scaling the Harness in Agentic AI (harness-scoped) | Shangding Gu (UC Berkeley) | 2026-05-25 | https://arxiv.org/html/2605.26112 | harness anatomy | arXiv Q6, Q14 | 14 citations; reference harness SafeRL-Lab/cheetahclaws, 799 stars | text |
| 18 | Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems (harness-scoped) | Barbaste, Darrigol, Vu, Wiltberger et al. | 2026-07-15 (OpenAlex) | https://arxiv.org/html/2609.00006 | harness anatomy | OpenAlex Q14 | 16 citations | text |
| 19 | Towards Portable Specification of the Agent Harness (harness-scoped) | Gertler, Novelli, Floridi (Yale Digital Ethics Center) | 2026-10-29 | https://arxiv.org/pdf/2610.40917 | harness anatomy plus specification record | arXiv Q14 | 0 citations | text (partial PDF extraction) |
| 20 | Architectural Design Decisions in AI Agent Harnesses (harness-scoped) | Hu Wei | 2026-04-20 | https://arxiv.org/html/2604.18071 | taxonomy of design decisions (70 projects) | OpenAlex Q14 | 5 citations | text |
| 21 | Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures (harness-scoped) | Benjamin Rombaut | 2026-04-03 | https://arxiv.org/html/2604.03515 | layered component taxonomy (12 dimensions) | arXiv Q3 | 22 citations | text |
| 22 | The Architecture of Agent Harness Engineering: Execution Scaffolding for Autonomous Systems (harness-scoped) | Santosh Kumar Chennuri (Google Cloud); IJSRCSEIT 12(5) | 2026-10-26 | https://zenodo.org/records/23668981 | harness anatomy (six parts) | OpenAlex Q14 | 0 citations; Zenodo 50 views | text |
| 23 | An Enterprise Agentic Architecture Framework for Agentic AI Governance and Scalable Autonomy (EAAF) | Padmanabham Venkiteela; Scientific Journal of Computer Science 2(1) | 2026 | https://journal.futuristech.co.id/index.php/sjcs/article/view/368 | layered model plus control plane | OpenAlex Q11; W10 | 19 citations | text |
| 24 | Enterprise Agentic AI Reference Architecture | Sanjeeve Kumar Gajadi (HCL Technologies); Zenodo / IJSRED 9(5) | 2026-10-16 | https://zenodo.org/records/23419932 | layered reference architecture (13 sections) | OpenAlex Q1a, Q11 | 0 citations; 62 views | text |
| 25 | Enterprise Multi-Agent Architecture Framework | Sanjeeve Kumar Gajadi; Zenodo / IJSRED 9(5) | 2026-10-16 | https://zenodo.org/records/23419926 | layered framework / component taxonomy | OpenAlex Q11 | 0 citations; 6 views | text |
| 26 | Enterprise Agentic AI: A Reference Architecture for Production-Grade Systems | Vikas Khanna; Zenodo | 2026-07-26 | https://zenodo.org/records/21482610 | design-dimension framework (eight dimensions) | OpenAlex Q1a, Q11 | 0 citations; 212 views | text |
| 27 | A Reference Architecture for Enterprise Agentic AI Infrastructure Platforms | Gopalasivam Palaniappan; Zenodo | 2026-08-06 | https://zenodo.org/records/21830553 | layered reference architecture plus Day-0/1/2 lifecycle | OpenAlex Q5 | 0 citations; 61 views | text (figures not extracted) |
| 28 | AEON: An Enterprise Control Plane Architecture for the Agentic Era | James D. Longmire, Micah Longmire; Zenodo | 2026-05-22 | https://zenodo.org/records/20349596 | reference architecture (six planes, nine subdomains, capability registry) | OpenAlex Q11 | 2 citations; 124 views | text (sections read, rest by heading) |
| 29 | ARIA: Agent Reference Intelligence Architecture (borderline vs E3) | Roni Mulyana (PT Trillium Technologies); Zenodo | 2026-10-05 (v1.4) | https://zenodo.org/records/23162918 | layered reference model (seven layers, OSI-inspired) | OpenAlex Q1a | 0 citations; 59 views | text |
| 30 | Reusable Agentic Infrastructure: A Component Architecture for Scalable Multi-Agent System Deployment in Enterprise Environments | Kandala; Int. J. AI and ML 6(5s) | 2026 | https://www.svedbergopen.com/index.php/ijaiml/article/download/596/457 | component architecture (two layers, six components) | OpenAlex Q9 | 0 citations; one unnamed healthcare SaaS adopter (3 to 11 agents) stated | text |
| 31 | Enterprise Agent Architecture: The Case for a Fifth Architecture Domain for the Agentic Enterprise | Michael K. Saleme; Zenodo | 2026-07-05 | https://zenodo.org/records/21207197 | layered model (four layers; position paper) | OpenAlex Q11 | 1 citation; 160 views | text |
| 32 | Charterion — Agentic Enterprise Architecture Framework (v2.0; record 22406488 now resolves to v2.0) | Samir El Hassani; Zenodo | 2026-09-18 | https://zenodo.org/records/22829848 | layered model plus 43-block catalog plus conformance model | OpenAlex Q11 | 0 citations; 193 downloads | text (290 pages; chapters 5, 8.12, 27, 29 read) |
| 33 | WorkMate: A Human-AI Collaborative Agent Infrastructure for Enterprise Organizational Governance | Li, Jing, Liu et al.; Zenodo | 2026-06-11 | https://zenodo.org/records/20644795 | layered reference architecture (five layers) | OpenAlex Q9 | 0 citations; 79 views | text |
| 34 | Pluggable Agentic AI Framework: A seven-layer composable enterprise agentic AI reference architecture on Amazon Bedrock AgentCore | Palakodety, Annamalai Sekar, Kuppuraju, Vangara; AWS ML Blog | 2026-11-09 | https://aws.amazon.com/blogs/machine-learning/pluggable-agentic-ai-framework-a-seven-layer-composable-enterprise-agentic-ai-reference-architecture-on-amazon-bedrock-agentcore/ | layered reference architecture | AWS-restricted search | none stated | fetch summary |
| 35 | The Agentic Enterprise - The IT Architecture for the AI-Powered Future | Salesforce Architects | not stated | https://architect.salesforce.com/docs/architect/fundamentals/guide/agentic-enterprise-it-architecture.html | layered model plus maturity levels plus component taxonomy | Salesforce-restricted search | none checked | fetch summary |
| 36 | Agent architecture components | Microsoft Learn | ms.date 2026-01-07, updated 2026-09-30 | https://learn.microsoft.com/en-us/agents/architecture/components-of-agent-architecture | component taxonomy | W3 | none stated | text |
| 37 | The Three Layers of an Agentic AI Platform | Sheng, Zhu, O'Rourke, Pedzinski, Zhang; Bain & Company | 2026-04-02 | https://www.bain.com/insights/the-three-layers-of-an-agentic-ai-platform/ | layered model | W12 (added query) | none stated | fetch summary |
| 38 | Agent Platform Engineering: A Reference Architecture | Ani Galstian; Augment Code | 2026-07-04 | https://www.augmentcode.com/guides/agent-platform-engineering-reference-architecture | reference architecture (seven layers) | W5, W12 | none stated | fetch summary |
| 39 | Agentic Infrastructure: What Actually Goes in the Stack | Ani Galstian; Augment Code | 2026-05-03 | https://augmentcode.com/guides/agentic-infrastructure-stack | component taxonomy (five layers) | W4 | none stated | fetch summary |
| 40 | The AI Agents Stack (2026 Edition) | Paolo Perrone; O'Reilly Radar | 2026-06-08 | https://www.oreilly.com/radar/the-ai-agents-stack/ | layered model (six layers) | W4 | none for the model | fetch summary |
| 41 | The 7 Core Layers of an Enterprise-Ready Agentic AI Architecture | Jyot Singh; RTS Labs | 2026-06-09 | https://rtslabs.com/agentic-ai-architecture | layered model | W2, W12 | none stated | fetch summary |
| 42 | Building an Agentic Enterprise, ch. 05 "The Reference Stack" | unattributed (regantih/reports-lab GitHub Pages) | undated (mid-2026) | https://regantih.github.io/reports-lab/agentic-enterprise/chapters/05-reference-stack.html | reference stack | W2 | none; weak provenance | fetch summary |
| 43 | Enterprise Agent Platform: 2026 Reference Architecture | Digital Applied | 2026-04-14 | https://www.digitalapplied.com/blog/enterprise-agent-platform-reference-architecture | reference architecture (five components) | W12 (added query) | none stated | fetch summary |
| 44 | AI Agent Platform Architecture 2026: Reference Patterns + Layer Decomposition | Knowlee | April 2026 | https://www.knowlee.ai/blog/ai-agent-platform-architecture-2026 | layered model (seven layers) | W12 (added query) | none stated | fetch summary |
| 45 | The Enterprise AI Agent Infrastructure Stack, Explained | Shakudo | updated 2026-09-04 | https://www.shakudo.io/blog/enterprise-ai-agent-infrastructure-stack | layered model (six layers) | W4 | none for the model | fetch summary |
| 46 | Agentic Architecture Components Selection (harness-scoped, low confidence) | agentic-ai.readthedocs.io (cites Arsanjani and Bustos 2026) | undated | https://agentic-ai.readthedocs.io/en/latest/Architecture/components-selection/ | component list | W3 | none | fetch summary |
| 47 | Breaking Down the Agentic Layers of AI | Boomi | 2026-11-10 | https://boomi.com/blog/agentic-layers-of-ai-integration/ | layered model (six layers) | W2 | none (one day old) | fetch summary |
| 48 | Agentic Infrastructure Bootstrap | Sarony11 (GitHub) | created 2026-03-22 | https://github.com/Sarony11/agentic-infrastructure-bootstrap | reference implementation of a three-part model | G2, G6 | 11 stars | text (README) |

### 6.2 Components and the three WARM questions

Components are quoted as the source names them. (a) area of work or business domain as an entity separate from agents; (b) registry or directory and its entries; (c) long-lived versus per-task agents.

| # | Top-level components (verbatim) | (a) Domain entity | (b) Registry / directory | (c) Long-lived vs per-task |
|---|---|---|---|---|
| 1 | "a Control & Governance Plane" ("Intent management", "Capability discovery", "Policy and trust", "Confidence and risk", "Delegation governance", "Audit and observability", "Human oversight") and "a Runtime & Coordination Plane" ("Agent lifecycle", "Workflow coordination", "Model and tool routing", "Context and memory coordination", "Scheduling", "Traffic management", "Runtime assurance"); external "Platform services". Semantic objects: "Intent", "Context", "Capability", "Provider", "Plan", "Policy", "Identity and Authority", "Delegation", "Trust", "Confidence", "Evidence and Provenance", "Execution" | No. "AOS domain" is "An administrative and trust boundary". Nearest is the per-request "Intent" object | Yes: capability registry; "A Capability is a stable, discoverable description of what an actor or system can perform ... may be provided by an agent, model, tool, API, workflow, human, service, or infrastructure function"; "it may index domain registries" | Partial: "The managed object may be a persistent agent identity or a transient runtime instance" |
| 2 | "Agent Lifecycle Manager", "Agent Scheduler", "Context and Memory Management", "Tool and Capability Registry", "Policy, Permissions, And Trust", "Observability and Audit"; planes "reasoning", "execution", "policy" | No | Yes: tool definitions ("name and version, input schema ..., side effect classification, required capabilities and scopes, rate limits and quotas") | Partial: "agents are long-lived, stateful loops. They may remain resident for days or weeks" |
| 3 | "Agent lifecycle", "Orchestrator", "Skills registry", "Tool mediation", "Context management", "A2A communication", "Agent memory", "Identity & AuthZ", "Behavioral guardrails", "Failure detection", "Observability", "Secure Code Execution", "AI-Aware Networking" ("not claimed to be complete or minimal") | No | Yes, for skills: "self-contained SKILL.md instruction files" with "provenance declaring a skill's domain, model compatibility, and callable tools" | No |
| 4 | "human/organisational delegation" (L1), "Agentic Interface" (L2), "Agent Harness" (L3), "Agent Reasoning and Planning" (L4), "Agent-Service Composition" (L5), "Service and Tool Infrastructure" (L6); cross-cutting "Governance and Observability", "Security and Trust" | No (L1 is the nearest) | Yes: "agent registry and marketplace", "versioned prompt/tool/model registries" | No |
| 5 | "agent(s)", "agent registry", "task planner", "task coordinator", "budget", "data registry", "data planner", "optimizer", "streams"; "sessions" | No | Yes, two: agent registry ("descriptions, input and output parameters ... deployment information") and "data registry" | No |
| 6 | "Supply Chain Layer", "Agent Layer" ("External Environments", "Context Engine", "Reasoning & Planning", "Workflow Execution", "Multi-layered Guardrails", "Memory"), "Operation Layer" ("Evaluation (Backbone and Control Loop)", "AgentOps Infrastructure and Observability") | No | No | No |
| 7 | "Intent and Outcome Layer", "Agent Design Plane", "Agent Runtime Plane", "Enterprise Capability Plane", "Supporting Control and Assurance Plane"; design artifact "ACC" | Partial: "Capability before agent: define the business capability and owner before defining the agent role or prompt" | No (registries named only as an SOA lesson) | Partial: prefers "a few accountable agents over many role-playing prompt wrappers" |
| 8 | "Individual agent" (control theory), "Agent collectives and swarms", "Human-agent teams", "Automated fleet at scale"; 36 controls, e.g. "Registry-backed interaction graph", "Approval gates", "Progressive rollout with atomic rollback", "Budget caps" | No | Partial: "Registry-backed interaction graph" | No |
| 9 | Orchestration layer: "planning unit", "policy unit", "Execution unit", "control unit", "state unit", "knowledge unit", "Quality and operations management"; agent types "Worker agents", "Service agents", "Support agents"; protocols "MCP", "A2A" | No | No | Partial: worker, service and support agent types; stateless vs stateful workers |
| 10 | Axes "autonomy" (L0 to L2) and "alignment" (L0 to L2); viewpoints "Goal-driven Task Management", "Agent Composition", "Multi-Agent Collaboration", "Context Interaction"; ontology "Library", "Agent", "Activity Log", "Activity Memory", "Preferences", "Alignment Techniques", "Communication Protocol", "Context" | No ("Domain Role Agents" are an agent attribute) | No ("Library" stores knowledge) | No |
| 11 | "the Operational Layer" ("Intent Management Agent", "Workflow Management Agent", "Routing Manager", "Deployment Manager", "Cognitive Workflow Manager") and "the Knowledge Layer" ("Workflow Metamodel Catalog", "LLM Configuration Catalog", "Deployment Metamodels Catalog") | No | Partial: catalogs of workflow, agent-configuration and deployment metamodels | Partial: "atomic, task-specific LLM agents"; a workflow instance is reused or "a dedicated instance" is created |
| 12 | "Domain", "Factory Harness", "Agent Harness", "Foundation Model", "Plant" | Partial: "Domain" is a layer ("industry rules, cases, evaluation sets and compliance boundaries") that "must change when the application domain changes" | No | No (the unit is a "run") |
| 13 | "Data Layer", "Knowledge Layer" ("a single Git repository of Markdown files"), "Intelligence Layer" (department, sync, quality, orchestrator agents), "Governance Layer"; "trust gradient" | Partial: "department agents" | No | No |
| 14 | Levels "Ad-hoc", "Reactive", "Defined", "Managed", "Optimized"; domains "Agent Lifecycle Mgmt.", "Identity & Access Ctrl.", "Observability", "Policy Enforcement", "Data Governance", "Human Oversight", "Sprawl Containment", "Audit & Compliance", "Inter-Agent Coord.", "Risk Classification", "Incident Response", "Continuous Improvement" | Partial: business functions appear in the simulation only | Yes, as a control: "Basic registry" (L2), "centralized catalog" (L3); entries are agents | Partial: "Orphaned Agents: Agents whose purpose expired but continue operating" |
| 15 | "Memory (externalized state)", "Skills (externalized expertise)", "Protocols (externalized interaction)", "the Harness that unifies them"; harness dimensions "Agent Loop and Control Flow", "Sandboxing and Execution Isolation", "Human Oversight and Approval Gates", "Observability and Structured Feedback", "Configuration, Permissions, and Policy Encoding", "Context Budget Management" | No | Yes, for skills: "a local repository, an organizational registry, or a platform-level marketplace" | No |
| 16 | "Contextualize", "Harmonize", "Anticipate", "Negotiate", "Generate", "Evolve" | No | No | Partial: agents "operate continuously, learning from interaction" |
| 17 | "foundation model, memory substrate, context constructor, skill-routing layer for tools and subagents, orchestration loop, and verification-and-governance layer" | No | No | Partial ("persistent project memory") |
| 18 | "Agent loop", "LLM integration", "Tools & actions", "Memory & context", "Safety & permissions", "Orchestration", "Extensibility"; cross-cutting "interface layer" and "session substrate (transcripts, persistence, resume/fork)" | No | Partial: skill registries, an "AgentRegistry" inside one harness | Partial: session substrate only |
| 19 | "Orchestration and planning", "Context and memory", "Tool and action interfaces", "Operational knowledge", "Sandboxing", "Permission model", "Verification, evaluation, and observability", "Execution runtime and lifecycle management" | No | Partial (tool registry mentioned) | No |
| 20 | "subagent architecture, context management, tool systems, safety mechanisms, and orchestration" | No | Partial: "Explicit Registry (34.3%)" for tools | Partial ("persistence scope") |
| 21 | "control architecture", "tool and environment interface", "resource management" (12 dimensions, e.g. "Execution Isolation", "Context Compaction", "Multi-Model Routing", "Persistent Memory") | No | Partial (per-agent tool registry) | No |
| 22 | "Execution loop (E)", "Tools and isolation (T)", "Context manager (C)", "State store (S)", "Lifecycle policies (L)", "Validation (V)" | No | No | Partial: "every agent session is a goldfish"; project memory persists in files |
| 23 | "Infrastructure Layer", "Enterprise Integration Layer", "Orchestration & Coordination Layer", "Governance & Safety Layer", "Agent Intelligence Layer", "Agent Interaction Layer"; control plane "Identity & Access Subsystem", "Policy & Compliance Engine", "Orchestration & Scheduling Engine", "Agent Lifecycle Manager", "Observability & Telemetry Fabric" | Partial: "multi-domain agents (Integration, Compliance, Data, Security, Finance, etc.)" | Partial (registry metadata in future work only) | No |
| 24 | "Experience and Interaction Layer", "Agent Orchestration Layer", "Planning and Reasoning Layer", "Enterprise Knowledge Layer", "Memory Architecture", "Model Runtime Layer", "Tool and Integration Layer", "Identity and Policy Layer", "Human Oversight Layer", "Security Architecture", "Observability and FinOps", "Governance and Responsible AI", "High Availability and Resilience" | No | Partial ("agent registration"; tools "registered") | No |
| 25 | "Agent Roles and Capability Model", "Multi-Agent Orchestration", "Inter-Agent Communication", "Shared Knowledge and Memory", "Tool and API Architecture", "Identity, Delegation, and Trust", "Conflict Resolution and Consensus", "Security Architecture", "Observability and Operations", "Governance and Responsible AI" | Partial: "Agent capabilities should be reusable across business domains" | Yes in effect: "Every agent should have a defined purpose, owner, capability profile, risk tier, approved tools, data scope, and decision boundary" | No |
| 26 | "Cognitive Decomposition", "Workflow & Platform Architecture", "Knowledge Management and Context Engineering", "Memory and Collaboration", "Enterprise LLM Gateway", "Governance, Security & Privacy", "Observability", "Evaluation and Evolution" | Partial: each cognitive responsibility is "a well-defined business capability with clear inputs, outputs, execution boundaries, and success criteria" | No | No |
| 27 | "Experience, Agent, Orchestration, AI Services, Enterprise Knowledge, Platform Engineering, and cloud-native Infrastructure layers"; cross-cutting "security, identity, governance, compliance, and observability"; "Day-0 planning, Day-1 deployment, and Day-2 operations" | No | Not in text (figures unread) | No |
| 28 | "six service planes (identity, authority, evidence, integration, capability composition, orchestration runtime)"; nine subdomains ("Governance and Strategy, AIDEX, DevSecOps, Cybersecurity, Digital Engineering, Enterprise Platforms, Human Capital, Insights and Intelligence, and Infrastructure and Operations") | Yes: "The subdomains are the capability areas the control plane orchestrates"; each has a "Subdomain Contract" per plane. Organizational IT units, not charters | Yes: "The capability registry is the canonical record of what the enterprise can do"; entries carry the providing subdomain, evidence requirements, dependencies and "the principals authorized to invoke it" | No |
| 29 | "L7 Intent", "L6 Assembly", "L5 State", "L4 Orchestration", "L3 Routing", "L2 Execution", "L1 Inference" | No | Partial: Routing resolves "tools, agents, services, and models from registries" | No ("a delegated agent is a complete stack") |
| 30 | "infrastructure layer" ("Agent base class", "MCP tool registry", "RAG pipeline module", "Memory manager", "Observability module", "Human handoff manager") and "application layer" | No | Yes, tools: "a versioned YAML-based catalog that maps registry keys to MCP tool connection specifications" | No |
| 31 | "Agent / Workforce", "Capability", "Control Plane", "Governance" | No | No | No |
| 32 | "L0. Motivation & Strategy", "L1. Business", "L2. Agency", "L3. Application", "L4. Data & Knowledge", "L5. Technology / Agentic Runtime"; aspects "Warrant/Trust", "Governance", "Boundary"; planes "design", "execution", "boundary"; 43 building blocks (e.g. "Agent Register", "Charter Register", "Tool Catalogue", "Scoped Memory Store", "Staffing Table") | Partial: "A charter binds an agent to a capability, process or step" under a named principal; owner is "Domain authority". The charter is per-agent authority, not a work-area bundle | Yes: "Agent Register", "Charter Register", "Tool Catalogue", "Staffing Table" (humans, roles) | Partial: "An agent type is chartered once and instantiated many times, ephemerally" |
| 33 | "user interaction layer", "governance control layer", "skill orchestration layer", "agent execution layer", "infrastructure layer"; memory "session memory, task memory, and behavioral memory" | Partial: maps "enterprise departments, positions, and responsibilities to permissions, skill accessibility, and contextual boundaries" | No | Partial: "master agent" vs SubAgents bound to "business modules or employee roles" |
| 34 | "Data and Knowledge", "Model and Inference", "Orchestration", "Security and Guardrails", "Application", "Observability", "Agentic Operations" | No | Yes: "AWS Agent Registry" cataloging each agent's tools, skills and owner | No |
| 35 | "Infrastructure Layer", "Data Layer", "Integration Layer", "Application Layer", "Experience Layer", "Security", "IT Operations and Observability", "Agentic Layer", "Semantic Layer", "AI/ML Layer", "Enterprise Orchestration Layer"; Agentic Layer parts include "Agent Runtime Environment", "Agent Lifecycle Management Suite", "Tool Registry", "Agent Registry", "Distributed Agent Policy Enforcement" | Partial: maturity levels "Single-domain agents", "Multi-domain agents", "Multi-agent, multi-domain orchestration" | Yes: "Agent Registry", "Tool Registry", "Model & Asset Registry", "Composable Capability Catalog & Marketplace" | Partial: "Agents are instantiated for specific tasks, and the specific agent instances are decommissioned afterwards" |
| 36 | "Client", "Chat/app/storage infrastructure", "Orchestrator", "Language model", "Catalog", "Tool calling", "OpenAPI based APIs", "Semantic indexes", "MCP servers", "Proprietary protocols", "Parsing and chunking", "RAI" | No | Yes: "Catalog: A registry or directory of available skills, plugins, or actions that the agent can invoke" | No |
| 37 | "Application and orchestration layer", "Analytics and insight layer", "Data and knowledge layer" | No | Yes: registry logging each agent's capabilities, tool entitlements and policy constraints | No |
| 38 | "Orchestration", "Model / inference", "Tool / function-calling", "Memory / state", "Retrieval / context", "Control plane / data plane", "Agent runtime / compute" | No | No | No |
| 39 | "Compute", "Orchestration", "Context", "Observability", "Security" | No | No | No |
| 40 | "Models and inference", "Protocols and tools", "Memory and knowledge", "Frameworks and SDKs", "Eval and observability", "Guardrails and safety" | No | No | Partial (agent types include "an agent that learns across sessions") |
| 41 | "Experience and Interface", "Orchestration and Workflow", "Agent and Reasoning", "Tools and Integrations", "Data and Knowledge", "Observability and Control", "Platform Infrastructure and Governance" | Partial: domain teams own agents; not a formal construct | Partial: tool registry | No |
| 42 | "Experience", "Orchestration", "Registry & Identity", "Memory", "Tools", "Evals & Observability" | No | Yes: "the catalogue of every agent in the organisation" (owner, purpose, tools, model, data touched, regulatory classification, version, kill-switch URL) | No |
| 43 | "Agent Fabric", "Tool Registry", "Memory Layer", "Policy Engine", "Eval Pipeline" | No | Partial: tool registry "versioned, permissioned, and discoverable" | Yes: "Short-lived, request-scoped agents" vs long-running stateful agents; "most platforms end up with both" |
| 44 | "Model layer", "Inference and gateway layer", "Framework layer", "Memory layer", "Tool and MCP layer", "Orchestration layer", "Governance and observability layer" | Partial: a "world model" of business entities in memory | Partial: "automation registry", "schedule registry" | No |
| 45 | "Foundation Models", "Agent Runtime and Orchestration", "Data, Memory, and Context", "Tool Integration", "AI Gateway", "Observability and Governance" | No | No | No |
| 46 | "Language Model Layer", "Agent Framework", "Memory System", "Tool Integration Layer", "Orchestration Engine" | No | No | No |
| 47 | "Application Layer", "Orchestration Layer", "Agent Layer", "Context Layer", "Data Layer", "Model Layer" | No | No | No |
| 48 | "resource-catalog/", "agent-library/", "agent-setup/" | Partial: the catalog lets agents "discover what systems, domains, and repositories exist"; "each domain maintains its own library" | Yes: "A Backstage-style service catalog. It acts as the 'Service Registry'" (systems, domains, repositories) | No |

**What the three questions show across the 48.**

- (a) **One source treats an area of work as a standing entity with its own contract:** AEON (#28), whose nine "subdomains" each have a "Subdomain Contract" per plane. Charterion (#32) has a "Charter" but binds it to one agent's authority. Beyond the Agent Harness (#12) has a "Domain" layer defined by a change test that resembles WARM's placement test. Eleven others have a partial form: departments, business capabilities with owners, or domain-specialist agents.
- (b) **Registries are common (29 of 48 have one at least partly: 17 yes, 12 partial); none is a directory of accountability.** Entries are capabilities, agents, tools, skills, data sources or metamodels. The nearest to WARM's Directory are AEON's capability registry (each entry names the providing subdomain and the principals allowed to invoke it) and Charterion's Charter Register.
- (c) **Three sources draw the distinction explicitly:** AOS-0001 (#1: "a persistent agent identity or a transient runtime instance"), Digital Applied (#43: "Short-lived, request-scoped agents" vs long-running stateful agents) and Salesforce (#35, task-instantiated agents with shared long-running memory). Charterion (#32) has ephemeral instances of a chartered type. None has a long-lived agent that holds a role and a channel as WARM's persistent agent does.

## 7. Components with no place in WARM v0.11 (item 4d)

Each row is the reader's inference against the one-line responsibilities of WARM's 24 services, five layers and seven domain parts. Quotes are the source's definitions. "Partial" means one or more WARM services cover part of it.

| Source | Component | Definition (quoted) | Nearest WARM part |
|---|---|---|---|
| AOS-0001 (#1) | "Confidence and risk" / Confidence object | "A system-level assurance signal linked to evidence and a control action." | Evaluation, Policy (partial). No WARM service aggregates confidence as a control signal |
| AOS-0001 (#1) | "Delegation governance" | "Bounded DelegationContext"; "Delegation attenuation and authority monotonicity" | Identity, Policy, Orchestration (partial). WARM states no rule that authority narrows along a delegation chain |
| AOS-0001 (#1) | "Intent management" | "Normalized IntentEnvelope"; Intent "I = {G, C, A, Π, X, S, T}" (goal, constraints, authority, policies, context, success criteria, temporal requirements) | Channels, Tasks (partial). A per-request goal/criteria object has no WARM service |
| Charterion (#32) | "Reserved-Step Register" | "the business decision that a step stays human" | Approvals, domain Workflow (partial). WARM has no standing designation of steps that only people may do |
| Charterion (#32) | "Obligation Register" | "Human-decision obligations ground reserved steps" | Domain rules (partial) |
| Charterion (#32) | "Boundary plane" | "the pair of substrates of two organisations with disjoint approvers ... two-sided admissibility" | None. WARM describes one system's boundary and has no cross-organization component |
| Charterion (#32) | "Warrant / Trust" aspect | every assertion carries "provenance, confidence, validity, status" | Memory provenance (partial) |
| AAGMM (#14) | "Sprawl Containment" | "Shadow Agents: Agents deployed outside IT governance without registration"; "Orphaned Agents: Agents whose purpose expired but continue operating" | Registry, Directory (partial). No WARM service detects duplicate, shadow or orphaned agents |
| AAGMM (#14) | "Risk Classification" | risk tiers for agents | Policy (partial) |
| CHANGE (#16) | "Anticipate" | "for predicting and preparing for unanticipated situations" | None clear |
| CHANGE (#16) | "Negotiate" | "for dynamically managing autonomy and oversight" | Approvals, Policy (partial). WARM has no service that changes an agent's autonomy level at run time |
| CHANGE (#16) | "Generate" | "for enabling agents to propose and validate new tools or capabilities" | Improvement, Releases (partial) |
| Gajadi MAS (#25) | "Conflict Resolution and Consensus" | "ranking, voting, arbitration, verification, or escalation" | Orchestration, Approvals (partial). WARM has no service that arbitrates between conflicting agent outputs |
| Gajadi RA (#24) | "Observability and FinOps" | "token budgets, model routing policies, concurrency limits, and cost allocation to business units" | Models, Policy, Scheduling, Observability (partial). WARM treats cost as a concern, not a service; cost allocation has no home |
| Megagon (#5) | "optimizer" | "multi-objective optimization over task and data plans" (cost, accuracy, latency) | Models routing, Orchestration (partial) |
| ASOC (#4) | registry "and marketplace" | "registries, discovery mechanisms, reputation systems, billing models, and certification requirements" | Registry (partial). Reputation, billing and certification have no WARM service |
| CASE (#8) | emergence controls | "Emergent behavior detection", "Contagion controls", "Population simulation" (definitions not read) | None clear |
| Portable harness spec (#19) | harness specification record | "records which model ran in which harness" (release record, run-start configuration, material-change events, run-end state) for regulatory disclosure | Releases, Observability (partial) |
| Salesforce (#35); Knowlee (#44) | "Semantic Layer"; "world model" | business entities and relationships shared by agents (summarized, not verbatim) | Domain knowledge, Retrieval (partial). A shared ontology of business entities is not a platform service in WARM |
| Orchestration of MAS (#9) | "Service agents" | "reusable utilities" | Tools, Registry (partial). WARM has no category of agent that serves other agents as a utility |
| CEAD (#7) | "ACC" and capability map with owners | "The ACC is the core design artifact" (the design decision that justifies an agent's existence) | Registry, Directory, domain Roles (partial) |

**Recurring candidates** (named by two or more sources): cost management and allocation (#24, #5, #8 "Budget caps", #1 "Traffic management"); conflict resolution or consensus among agents (#25, #16 "Harmonize"); sprawl, shadow and orphaned agents (#14, #42 "kill-switch URL", #8); confidence or risk as a run-time signal (#1, #14, #32).

## 8. Ranking: which new sources are worth a full component-by-component mapping

Ranked by how complete and general the model is, then by how directly it bears on WARM's distinctive parts (domains, directory, persistent agents). Adoption is weak for all of them; none has more than 51 citations.

| Rank | Source | Why |
|---|---|---|
| 1 | AOS-0001, Sharma and Shah, arXiv 2608.03214 (with its precursor 2606.01508) | The most complete general model found: 199 pages, two planes with 14 named responsibilities, a semantic object model, a capability registry and a persistent-identity vs transient-instance split. Vendor-neutral by statement. 0 citations |
| 2 | Charterion v2.0, El Hassani, Zenodo 22829848 | Six layers, three planes and 43 named building blocks, with a Charter Register, Staffing Table and human-reserved steps: the nearest thing to WARM's charter and roles. Enterprise-architecture framing; self-published, 0 citations |
| 3 | Salesforce, "The Agentic Enterprise - The IT Architecture" | Eleven layers with a nine-part agentic layer, four registries and maturity levels from single-domain to multi-domain agents. The broadest vendor model found. Read only as a fetch summary, so a mapping must re-read the page |
| 4 | Steinder and Franke (IBM), arXiv 2607.25076 | Thirteen platform primitives derived from OS and cloud-OS, a prototype with 304 GitHub stars, and an IEEE ICWS venue. Maps cleanly onto service-level WARM |
| 5 | AEON, Longmire and Longmire, Zenodo 20349596 | Six planes plus nine subdomains with per-plane contracts and a capability registry whose entries name the providing subdomain: the only source with an area-of-work entity that has a contract |
| 6 | ASOC manifesto, Beheshti, Dustdar, Benatallah, Casati et al., arXiv 2607.12619 | Six layers with an "Agent Harness" layer and two cross-cutting planes, from senior service-computing authors; likely to be cited. Thin on each component |
| 7 | CEAD, deVadoss, arXiv 2605.08258 | Five planes and a "capability before agent" rule with named owners: the closest academic statement of WARM's "a domain defines roles before agents fill them". Read as fetch summary |
| 8 | EAAF, Venkiteela, Sci. J. Comput. Sci. 2026 | Six layers plus a five-part control plane; 19 citations, the most-cited of the enterprise reference architectures found |

Next in line: Megagon blueprint (#5, 23 citations, agent and data registries), Orchestration of MAS (#9, 40 citations), WorkMate (#33, departments mapped to permissions), Gajadi's two papers (#24, #25, broad but four pages each) and Beyond the Agent Harness (#12, a "Domain" layer with a placement test, but scoped to coding pipelines).

## 9. Flow count

| Stage | arXiv | OpenAlex | Web (incl. vendor/standards) | GitHub | Total |
|---|---|---|---|---|---|
| Hits reported by the database | 561 | 3,291 | 332 links returned (no totals exposed) | 116,458 | — |
| Records screened (within the caps) | 499 | 607 | 332 | 196 | 1,634 |
| After de-duplication across all databases | | | | | 1,314 |
| Passed title screening | | | | | 258 |
| Included | | | | | 61 |
| of which already known | | | | | 13 |
| of which new | | | | | 48 |

Notes on the counts:
- De-duplication used arXiv id, then DOI, then normalized title, then normalized URL. Mirror pages and repeated arXiv links in vendor searches were collapsed when recorded, so the web share of the 1,314 is approximate to within a few links.
- The 258 that passed title screening divide as: 61 included; 25 excluded after reading the primary (table 5.2: 16 sources, one of them read from its abstract only, and 9 GitHub lists); 158 excluded or not screened at abstract level (table 5.3, grouped rows counted by item); 8 UNVERIFIED (section 10); 6 known sources outside this protocol's rule. 61 + 25 + 158 + 8 + 6 = 258.
- Included by database of first appearance, new sources only: arXiv 17, OpenAlex 15, web 15, GitHub 1. Three of the web ones (Bain, Digital Applied, Knowlee) came only from query W12, which was added during the search.

## 10. What could not be opened (UNVERIFIED)

| Source | Link tried | Problem | Likely decision if opened |
|---|---|---|---|
| Cloud Security Alliance, "AI Agents: Architecture and Control Plane" (released 2026-06-22; ten-layer reference architecture in three groups: "Infrastructure, Intelligence, and Knowledge (Layers 1–3)", "Agency, Environment, and Execution (Layers 4–7)", "Governance and Accountability (Layers 8–10)") | https://cloudsecurityalliance.org/artifacts/ai-agents-architecture-and-control-plane | Landing page only; "Resource unavailable"; download is behind a form | INCLUDE; a strong candidate for mapping |
| Koubaa, "Agent Operating Systems (Agent-OS): A Blueprint Architecture" (Kernel, Services, Agent Runtime, Orchestration, User layers, per the abstract) | https://www.preprints.org/manuscript/202509.0077 ; TechRxiv; Springer doi 10.1007/978-3-032-24013-2_4 | HTTP 403 and a JavaScript challenge; abstract read via OpenAlex only | INCLUDE |
| Tekinerdogan and Tekinerdoğan, "Living Mesh: A Reference Architecture for Human-Governed Multi-Agent Systems" | https://doi.org/10.2139/ssrn.7536800 | SSRN 403; abstract read via Crossref only | INCLUDE or N (governance core) |
| McKinsey QuantumBlack, "agentic AI mesh" (seven capabilities) | Medium post; https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage/ and the PDF | Medium 403; McKinsey pages timed out twice; PDF download returned nothing | INCLUDE if the seven capabilities are named |
| Eric Broda, *Agentic Mesh* (book) | ebooks.com; O'Reilly library page | HTTP 403 | Unknown |
| DataStax, "An LLM Agent Reference Architecture" | https://www.datastax.com/resources/whitepaper/an-llm-agent-reference-architecture-demystifying-llm-based-systems | Redirects to an IBM product page | Unknown |
| T-Systems enterprise agentic AI platform architecture (ten layers per search summary) | https://ui.dmw.agentichub.ai.t-systems.net/docs/ARCHITECTURE | Login required | Likely E4 (one product) |
| Gravitee, "Reference Architectures and Standard Building Blocks for AI Agent, MCP, and API Governance Platforms" | gravitee.io/corpus/gen-1372/... | HTTP 404 | Likely N |

Also not opened, listed in table 5.3: eight OpenAlex records with no abstract (Gurumani; Shinde et al.; Vatsa, "The Agent Infrastructure Stack"; Santhanam, AAWDS; Tadinada; Kwarsick; Chen; Newman, ARMM), Goniwada's Apress chapter (paywalled), four gated vendor white papers (Exadel, OneReach, Niveus, EXL), Karuppuchamy's IEEE paper (paywalled), and Towards AI's member-only "7 layers" post. `[no-record: published reference model or architecture from NIST, ISO/IEC JTC 1/SC 42, the Linux Foundation agent projects, OWASP, W3C or IEEE; searched = the restricted web searches in 3.4 plus the IEEE P3709 page; as of 2026-11-11]`. The restricted searches leaked arXiv results (deviation 4), so this is a weak negative.
