---
title: "WARM vendor table: seven cells changed after the final review of draft 8"
date: 2026-11-13
author: sagan
status: "written 2026-11-13 10:08; applied in draft 9 (paper/build/gen_vendors.py, RULED). Recodings of recorded evidence. No vendor page was read again."
---

Source of the findings: `paper/astra-review-d8.md` (gpt-6-astra, findings 1 and 3). Authority: the author's decision, 2026-11-13 about 07:37 (a cell that does not follow a ruling is changed to follow it and marked).

## Ruling 24. Approvals: a yes needs a stated record of decisions on single held actions

Version 0.13 (`protocol-v2.md:53`): "Obtain and record people's authorizations: approvals given in advance for a class of actions under stated conditions, and decisions on single actions that are held." A row that states how an approval in advance is saved, and no record of a decision on a single held action, rates part. The H1 reading is used as a second look at the same pages.

| Product | As read | Readers | Row evidence | H1 reading | Value |
|---|---|---|---|---|---|
| Dots | yes | one | `openai-dots.md:40`: "a record of each single decision is not described" | no* (`d-personal-agents.md:21`: the vendor tells admins to check whether approvals appear in exports) | part |
| Claude Duet | yes | one | `claude-duet.md:52`: "A separate record of approvals is not described." | no* (`d-personal-agents.md:20`: pages "never say an approval decision is kept as a record") | part |
| Grok Build | yes | one | `grok-build.md:39`: remembered grants kept in `permission.toml`; no record of single decisions | no* (`c-harnesses.md:41`: "No page defines a record of permission decisions") | part |
| Antigravity | yes | two (both yes) | `antigravity.md:40`: allow rules in settings and `agent_permissions`; an interactive card for single actions, no record of the answer | no (`c-harnesses.md:51`) | part |
| Tasks in Gemini | yes | two (both yes) | `gemini-spark.md:41`: "Always allow" updates a saved preference; no record of single decisions | no* (`d-personal-agents.md:23`: "neither page says the decision is recorded") | part |

The five that keep yes, and the record each row or H1 reading states:

| Product | Record of single decisions |
|---|---|
| Claude Code | `claude-code.md:39`: `tool_decision` event "Logged when a tool permission decision is made (accept/reject)" |
| Codex CLI | `codex.md:40`: `codex.tool_decision` (approved or denied, and whether from config or user) |
| Grok Bot | `grok-bot.md:40`: Action Recording keeps "the decision that allowed or refused it" (Enterprise) |
| Muse | not in the service row; H1 reading `d-personal-agents.md:24`: an Activity log of actions taken "and permissions you've given it" |
| Claude Managed Agents | ruling 23 (`second-reader/comparison-claude-managed-agents.md`, addendum): kept allow and deny confirmations; a database is needed to keep them past a restart |

Muse's yes rests on the H reader's quotation, not on its service row. The reviewer did not list it among the cells to lower.

## Two of the seven cells that the earlier checks left unclear

| Cell | As read | Readers | Reviewer's judgment | Value |
|---|---|---|---|---|
| Tasks in Gemini, Environments | yes | one | `gemini-spark.md:25` states a remote browser and a file scope and no isolation of an agent from others; rulings 9 and 20 lowered Dots and Claude Managed Agents on stated limits | part |
| Codex CLI, Identity | yes | two (both yes) | `codex.md:37`: "Subagents have no identity of their own"; elsewhere the agent acts as the signed-in user. The by-agent reading of ruling 9 (Dots) gives part. The reviewer's alternative: keep yes and offer the same rule for a scoped feature to every product, which needs readings the freeze excludes | part |

Consequence of the second: Identity has no full rating in Table 7.

## Left as read (five cells)

Grok Build on Orchestration (the reviewer: do not force a change), Tasks in Gemini and Grok Bot on Sessions (hand-off undefined), Claude Managed Agents on Sessions (retain) and on Tasks (retain as disputed).

## Counts

As read 116, 116, 18. With thirteen cells changed (six in draft 8, seven here): 106, 127, 17. With the five unclear cells also changed: 103, 130, 17. With the reviewer's values for the three decisions it disputes (rulings 12, 16, 21): 108, 126, 16.

## Not done (to the backlog on lifeos#3502)

- Rulings 12, 16 and 21 are kept. The author ruled at 07:37 that 12 and 16 (and 2) are kept; 21 is kept under the lower-value rule, with the reviewer's disagreement stated in Section 5.5.
- Like cases with no ruling: Dots on Scheduling; Antigravity on Secrets and Reliability; isolation between agents in the columns where both readers rated yes.
- H1 to H5 applied unevenly (Grok Bot H1; Claude Code and Codex CLI H2; three harnesses H4). Values left as read; Section 5.6 states the alternatives.
