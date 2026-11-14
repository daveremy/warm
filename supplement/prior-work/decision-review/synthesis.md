---
title: "What 39 sources and products, and ten found outside them, define about decisions by people"
date: 2026-11-12
author: sagan (from the five reader files in out/)
status: "written 2026-11-12 16:04. One reader per source (Claude subagents, model opus), no second reader. 34 quotations and named measures checked by sagan against live pages or PDFs; the rest are the readers' own."
---

## Counts (39 = 14 published models, 3 platforms, 5 recent sources, 8 older sources, 4 harnesses, 5 personal agents)

| Question | yes | part | no | The yes values |
|---|---|---|---|---|
| H1. A record of each decision with why a person was needed | 3 | 13 | 23 | Charterion; AOS-0001; OpenClaw |
| H2. A measure of how often people are required | 4 | 12 | 23 | AAM/5C (task completion rate); Charterion; Bedrock AgentCore (count of browser takeovers); Hua (takeovers per pull request) |
| H3. A review of past decisions that changes the rules | 1 | 13 | 25 | Charterion |
| H4. Authority that changes with the record | 1 | 8 | 30 | Charterion |
| H5. Tasks handed to a person for lack of capability, recorded and reduced | 0 | 12 | 27 | none |

Per reader (yes/part/no): A, fourteen models: H1 2/5/7, H2 2/7/5, H3 1/0/13, H4 1/6/7, H5 0/1/13. B, sixteen: H1 1/4/11, H2 2/1/13, H3 0/4/12, H4 0/2/14, H5 0/4/12. C, four harnesses: H1 0/2/2, H2 0/2/2, H3 0/4/0, H4 0/0/4, H5 0/3/1. D, five personal agents: H1 0/2/3, H2 0/2/3, H3 0/5/0, H4 0/0/5, H5 0/4/1. The eight older sources (2002 to 2013) rate no on all five.

Outside the set (reader E, 12 queries, ten sources): no clean yes on H3; one yes on H4 (an AWS Architecture Blog post on graduated autonomy); no clean yes on H5.

## The nearest counterpart: Charterion (verified in the PDF by sagan)

- Section 14.7, page 91 of the PDF: "The attributed Evidence Records and drift reports return to the refine phase, where they drive three kinds of change: narrowing (a charter whose scope produces many denials or reversals is too broad), widening (an agent whose needs produce many unwarranted or unserved outcomes is under-chartered or the slice under-observed), and level changes under the evidence-gated promotion rule of Section 18.8. B2 is the mechanism by which the architecture learns". (Spaces restored where the PDF text runs words together.)
- Section 18.8, page 103: "A charter's level shall be raised only at gate G6, only by one step in L, and only if over the review window its Evidence Record satisfies the organisation's thresholds on: (a) the reversal rate of permitted actions; (b) the denial rate; (c) the share of unwarranted outcomes; (d) the acceptance rate of its escalations by the overseer".
- Reader A reports default thresholds (acceptance of at least 90% and 98%, over at least 90 days and 500 decisions). NOT checked by sagan.
- How WARM v0.14 differs, stated narrowly: (1) Charterion acts on an agent's level through rates over a window; v0.14 reviews each stop with its reason. (2) Charterion concerns authority; v0.14 also counts tasks handed over for lack of capability, on which Charterion rates part. (3) Charterion grades autonomy in levels; v0.14 keeps three kinds of decision for classes of action.

## Other verified passages

- AOS-0001, section 9.9, page 31: "A human decision is itself evidence. The record includes the approver identity, authority, information presented, decision, time, and any modifications."
- AAM/5C, glossary, page 98: "Rate of agentic tasks completed without human intervention".
- Charterion, pages 66 and 219: "the escalate outcome degrades in fact to permit".
- Cheng and Cheng, arXiv:2604.23049, page 4: "repeated human approval of similar actions may indicate that certain decisions can be safely automated".
- AWS Architecture Blog: "the rolling rate at which operators reject proposed actions caps the effective safety metric"; "Promotion requires sustained performance"; "Demotion is immediate".
- Codex: "fix the boundary first instead of teaching the reviewer to approve noisy escalations forever"; "you can ask Codex to analyze past traffic there before changing policy or permissions"; "interrupts the turn after 3 consecutive denials or 10 denials in the last 50 reviews in that turn".
- Claude Code: "No tool_decision attribute names the permission rule or setting that refused the call"; "if the classifier blocks an action 3 times in a row or 20 times total, auto mode pauses and Claude Code resumes prompting"; the command `/fewer-permission-prompts`.
- Antigravity: "The agent leaves the login page open in the built-in browser tab, pauses, and asks you to finish signing in"; "Permissions manually granted during a conversation can persist, allowing the agent to learn trusted actions over time".
- Grok Bot changelog: "Auto-review cards say what paused an action: your Ask first rule, your team's Ask first rule, or your Needs approval setting"; "a Bot can offer to add, change, or remove one of your Auto-review rules on a card you confirm"; "it offers their connector, and connecting ends the handoff".
- Claude Duet: "Approval fatigue is a serious issue". Dots: "includes a step you must do yourself". Tasks in Gemini: "Asking you to take over when it can normally do the step". Muse (meta.com help): "learns over time which decisions need your sign off".
- OpenClaw: "The receipt names the durable owner and record reference"; reason code `operator_approval_denied_by_reviewer`.

Count of quotations checked by sagan: 23 on HTML or Markdown pages, 2 in the Cheng PDF, 4 in the Charterion PDF, 2 in the AOS-0001 PDF, 1 in the AAM/5C PDF: 32, all found. Checked afterward, also found: "takeovers per PR" in Hua (arXiv HTML) and `TakerOverCount` on the AgentCore observability page: 34.

## Not verified, and limits

- Electric Elves (Scerri, Pynadath and Tambe, JAIR 2002; reader E): the arXiv PDF's text layer extracts as glyph codes, so the reader's repaired quotations could not be checked. Do not quote or characterize it until a readable copy is read. The adjustable-autonomy and sliding-autonomy literature it belongs to has not been read.
- Reader B's AgentCore and EDDOps quotations (PDFs), reader A's values other than the three sources above, and reader E's other seven sources: not checked.
- Three papers on learning rules from approvals named in a survey (AutoPermissions, AgentGuardian, RTBAS) were not opened by reader E.
- One reader per source, all of one model family, and no second reader. 21 of reader A's cells are disputable.
- FALSE, do not write: "no source has a review of people's decisions" (Charterion does); "the review of stops is new".

## Addendum, 2026-11-13 07:46: the tenth product (reader F)

The author's decision, 2026-11-13 07:37: Claude Managed Agents is covered in full. Reader F (Claude subagent, model opus, protocol-v2 unchanged) read Claude Managed Agents, self-hosted, on 48 vendor pages: `out/f-claude-managed-agents.md`. Values: H1 yes, H2 no, H3 part, H4 no, H5 no; no cell marked disputable. Ten of its quotations checked by sagan against the live pages at 07:44, all found (34 + 10 = 44 checked in all).

Counts for 40 sources and products (39 + 1):

| Question | yes | part | no | The yes values |
|---|---|---|---|---|
| H1 | 4 | 13 | 23 | Charterion; AOS-0001; OpenClaw; Claude Managed Agents |
| H2 | 4 | 12 | 24 | unchanged |
| H3 | 1 | 14 | 25 | Charterion |
| H4 | 1 | 8 | 31 | Charterion |
| H5 | 0 | 12 | 28 | none |

The ten products: H1 1 yes, 4 part, 5 no; H2 0, 4, 6; H3 0, 10, 0; H4 0, 0, 10; H5 0, 7, 3.

H1 yes, the caveats reader F recorded: the reason (the policy type, or `reason_code` under `auto`) and the person's decision are in two events linked by event ID; with no database configured, the default, history is in memory and a restart erases it; no page says the event records which person decided. The H1 yes level asks for why a person was needed and what was decided, and both are stated. Like cases: Claude Code and Codex rate part because their decision events name no rule ("No `tool_decision` attribute names the permission rule or setting that refused the call").
