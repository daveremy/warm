---
title: "Claude Managed Agents (self-hosted): first reader against the blind second reader, and the three differing cells adjudicated"
date: 2026-11-13
author: sagan
status: "decided 2026-11-13 07:21 MST by sagan, one adjudicator, not blind (both readers' files were open). The five deciding quotes were found as written on the live vendor pages at 07:20 (curl, with a negative control)."
---

## Design

Same as `../second-reader-comparison.md`. First reader: a Claude subagent (claude-fable-5-2), all 25 services and C1 to C4, protocol version 2. Second reader: gpt-6-astra through `codex --search exec -s read-only`, given only `protocol-v2.md` and `rerate-criteria-v2.md`; run 2026-11-13 07:03 to 07:07, rc=0, 8,707 bytes (`out/claude-managed-agents.md`). Sample: 8 of the 24 non-derived services (seed "20261112-claude-managed-agents", line 10 of `sample.txt`) plus C1 to C4. Own-vendor reading: the first reader is an Anthropic model reading an Anthropic product.

## Result

```
claude-managed-agents  services 6/8  C 3/4   C1:part/part C2:part/part C3:part/no* C4:part/part
DIFF claude-managed-agents Environments yes part*
DIFF claude-managed-agents Channels part* yes
DIFF claude-managed-agents C3 part no*
```

Agreed and unchanged: Scheduling part, Memory yes, Registry yes, Secrets yes, Improvement no, Reliability part (the second reader marks it DISPUTABLE (yes), so the cell carries the mark), C1 part, C2 part, C4 part.

With the nine earlier products: services 65 of 80, criteria 33 of 40, and 22 differing cells (19 in `../adjudication-19.md`, 3 here).

## Rulings

Rules as in `../adjudication-19.md`: the protocol as written; when both values are defensible the lower stands and the cell is marked DISPUTABLE; one ruling for one question across products.

| # | Cell | First | Second | Adjudicated | Whose value |
|---|---|---|---|---|---|
| 20 | Environments | yes | part* | part* | second |
| 21 | Channels | part* | yes | part* | first |
| 22 | C3 | part | no* | part | first |

### 20. Environments: part, DISPUTABLE (yes)
Both readers cite the same facts. Each session's worker runs "in a container or pod of its own" (self-hosted overview). Inside a multiagent session, "All agents share the same sandbox, filesystem, and vault credentials" (multiagent orchestration). The service's definition is a place to act for each agent, "isolated from the others". Sessions are isolated; agents within one session are not. Same question as ruling 9 (Dots), where isolation was stated for one boundary and not for delegated tasks, and the same answer. Yes is defensible if isolation between sessions suffices.
Not re-opened: cells where both readers gave yes for products whose subagents can share a workspace. The freeze admits no new readings.

### 21. Channels: part, DISPUTABLE (yes)
Requests and results travel over the API ("Your code calls it with the official SDK, cURL, or the `ant` CLI"), a terminal chat and the console page on the server ("Enter a message in the box at the bottom of the page"). Applications have a channel. People have only the product's own console and a terminal; the pages describe no adapter to chat, email or another channel people already use, and no webhooks. The definition ends "on the channel each one uses". Same reading as the agreed cell for Tasks in Gemini (part, DISPUTABLE: every channel for people is the vendor's own app). Yes is defensible because people and applications each have some channel.

### 22. C3: part
The one C3 ruling of `../adjudication-19.md` (cells 8, 17, 19) applies. "the server records it as part of the creator of each resource": a record names a creator per agent, session, vault, memory store and skill and uses it to decide who sees the resource. That fits the part level ("a record names an owner, a provider or a responsible party per agent, asset or capability, but accountability is not stated"). The second reader's no does not fit the wording of the no level ("no such record"). Directory (derived from C3 part and C4 part) stays part.

## Counts after the three rulings

- The first reader's value stands in 2 cells, the second reader's in 1. The lower value stands in 2; the higher in 1 (C3, part over no).
- Claude Managed Agents: 9 yes, 15 part, 1 no (the first reader alone: 10, 14, 1).
- All ten products, from `paper/build/gen_vendors.py`: 115 yes, 117 part, 18 no of 250 cells.

## Addendum, 2026-11-13 07:45: Approvals second-read by choice, and decided

The author's decision, 2026-11-13 07:37: the cell gets a second reading. The Approvals cell is not in the seeded sample. It was second-read because the first reader's part was the one value that kept Approvals from a yes in all ten products, a headline claim of the paper, and it had one reader. Same second reader and protocol; brief `briefs/claude-managed-agents-approvals.txt` (the sample brief with the service list replaced by Approvals alone); run 07:38 to 07:41, rc=0, 4,030 bytes, `out/claude-managed-agents-approvals.md`.

```
DIFF claude-managed-agents Approvals part* yes
```

| # | Cell | First | Second | Adjudicated | Whose value |
|---|---|---|---|---|---|
| 23 | Approvals | part* | yes | yes | second |

### 23. Approvals: yes
The definition (version 0.13): "Obtain and record people's authorizations: approvals given in advance for a class of actions under stated conditions, and decisions on single actions that are held."
- Held single actions, obtained and recorded: "If a tool call waits for you, its card shows Approve and Deny." (console) and "The CLI sends your choice as a `user.tool_confirmation` event, with any reason you type as its `deny_message`." (sessions-connect); "Sessions and their history stay in your database until you delete them." (data and access). Both readers agree on this half.
- In advance, for a class: "To auto-approve tools from a trusted MCP server, set `default_config.permission_policy` on the `mcp_toolset` entry." (permission policies). The class is a tool or a toolset; the setting is kept in the agent's versioned configuration.
- The first reader's part rests on "no stated conditions and no record of who approved", and its own row says yes is defensible "if a per-tool policy counts as approval of" a class.
- Like cases decide it, as they did for C3 (ruling 8, 17, 19). Both readers rated yes on Approvals for the four products where the cell was in the sample: Claude Code, Antigravity, Grok Bot and Tasks in Gemini. Tasks in Gemini's row states an "Always allow" preference with neither conditions nor a record of who approved (`../gemini-spark.md:41`), and Antigravity's rests on configured grants (`../antigravity.md:40`). A part here would hold this product to a reading that no other column was held to. The blind check of this column (`../consistency-check-tenth.md`, Section B) reached the same finding without seeing the second reading: "out of line, too low".
- Not marked DISPUTABLE, as Grok Bot's C4 (ruling 15) is not: the value follows the like cases. The first reader's part* is recorded here and in the generator.
- My interest: I wrote the paper, and "every product rates yes on Approvals" is the simpler claim. The second reader is a model of another vendor that saw none of this, and the column check was blind to the paper.
- Quotes: the four passages above were found as written on the live pages at 07:44 (curl, with a negative control).

## Counts after ruling 23

- 23 decided cells: the first reader's value stands in 13, the second reader's in 10. The lower value stands in 17, the higher in 6.
- On the seeded sample alone the agreement is unchanged: services 65 of 80, criteria 33 of 40.
- Claude Managed Agents after adjudication: 10 yes, 14 part, 1 no. The column check also finds Models (part*) clearly below ruling R14; with that cell changed as the five cells of the other nine columns were (the author's decision, 2026-11-13), the column is 11 yes, 13 part, 1 no.
