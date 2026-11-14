---
title: "Vendor mappings: do the unadjudicated cells follow the adjudication's rulings?"
date: 2026-11-13
author: "consistency checker (Claude subagent), read-only except this file"
status: "first pass; not reviewed"
inputs: "protocol.md, protocol-v2.md, second-reader/rerate-criteria-v2.md, adjudication-19.md, second-reader-comparison.md, second-reader/sample.txt, the nine reader files, paper/build/vendor-totals.json"
---

# How this check was done

- I read `protocol.md`, `protocol-v2.md`, `second-reader/rerate-criteria-v2.md` and `adjudication-19.md`, and wrote down each general ruling the adjudication applies (Section 1).
- For each ruling I read the governed row in all nine reader files, including cells the two readers agreed on and cells only one reader rated. I judged each cell only from what its row says (value, quotes, notes). I opened no vendor page and used no outside knowledge of the products.
- I did not open `paper/claude-review-d6.md`, `paper/astra-review-d6.log`, `paper/astra-review-d6-partial-codex.md`, or `claude-managed-agents.md` (a tenth product, outside the nine).
- Line numbers below are line numbers in the named file as it stood on 2026-11-13.

# Section 1. The rulings

Each ruling is stated so it could be applied to any product. "Source" is the line of `adjudication-19.md` that applies it.

| # | Service or criterion | Ruling | Source |
|---|---|---|---|
| R1 | Tasks | Yes needs a stated feature by which the product coordinates retry or recovery of the unit of work itself (the goal, task or session that keeps the request). A retry of one request inside a turn does not count. Tracking, cancellation and a kept request, without retry or recovery of the unit, rate part. | line 59 |
| R2 | Policy | The definition has four parts: a rule decides whether an action proceeds; a rule on what content may enter and leave; a rule on what stored data is kept; a grant is issued. Yes needs each part stated. Filesystem and network rules (what commands may read or write, which destinations they may reach) are not counted as a rule on what content may enter or leave. Retention limited to local history and workspace settings is noted as not covering kept data. | line 62 (applied again at lines 91 and 114) |
| R2b | Policy | A rule the agent only "tries to follow" is an instruction, not a decision by rule. | line 91 |
| R3 | Scheduling | Timers, loops and monitors that run only inside an open session, with no start at a clock time and nothing that starts work when the product is not running, rate part, even when interval, event and cap features all exist. A yes may rest on scheduled tasks that run when no session is open (Claude Code's cloud scheduled tasks), not on session-scoped ones. | line 65 |
| R4 | Improvement | A feature that turns one session or chat into a skill when the user asks (Grok Build `/skillify`, Antigravity `/learn`) rates part: not yes (it does not cover agents or the platform), and not no (line 119 names Tasks in Gemini's no on "build a skill from chats" as inconsistent with these part values). | line 68; line 119 |
| R5 | Sessions | History kept, with pause, resume and hand-off not described as features, rates part. | line 74 |
| R6 | Observability | Yes needs pages that say what is recorded (for example the steps and the files read or updated) or a log, trace or export. A task list or task page with no statement of what it records rates part. | line 77 |
| R7 | C3 (and through it the derived Directory row) | A kept record that names an owner, a provider or a responsible party per agent, asset or capability (plugin author, token creator, Bot owner, dot owner, connector provider, skill owner) rates part, even when the owner is only an access role and accountability is not stated. No applies only when there is no such record. | lines 80 to 83 |
| R8 | Environments | Yes needs isolation of each agent from the others. A place to act whose isolation the vendor disclaims for the agent's own boundaries rates part. | line 86 |
| R9 | Identity | Yes needs an identity for the agent distinct from the person. Where the agent acts under its owner's identity (for example in connected apps), the cell rates part. The adjudication also notes that the inventory and revocation are Enterprise only; it does not say whether that alone lowers a cell. | line 89 |
| R10 | Evaluation | Part needs a review feature with stated criteria (Codex custom review instructions, Grok Build's reviewer panel, Antigravity's Auditor). A check that names no criteria and no result for a check that could not run, or only action reviews counted under Policy, rates no. | line 95 |
| R11 | Orchestration | Hand-off between agents, where who does what and what depends on what come from a person's message and no record or mechanism of the product coordinates dependencies, rates part. | line 98 |
| R12 | C1 | Teams and groups that the pages define as cohorts for access and settings, with no statement that they divide the system's work into areas, rate part (version 2 ruling of the criteria). | line 102 |
| R13 | C4 | Yes when an agent at run time can look up, from a kind of work, the agent or role that handles it and how to reach it, and the lookup is not inside one orchestrator's logic. Limits of scope (only Team Bots shared with the asker; certain plans) do not lower the value; they are stated with it. | lines 106 to 108 |
| R14 | Models | Several models of one vendor meet "more than one model or vendor". Yes also needs the product or its configuration to choose the model for each task. A person switching models by hand rates part. | line 111 |
| R15 | C2 | When C1 has two candidate units and C2 rates differently on each, both values are defensible and the lower stands, marked DISPUTABLE. | line 71 |

The adjudication's method line (line 12) also restates the protocol's tie rule: when both values are defensible the lower stands, and a value is defensible only if the evidence fits the wording of that level. I used that rule only together with a ruling above, not as a ruling of its own.

# Section 2. Cells that do not follow a ruling

"Second-read" is from `second-reader/sample.txt`. "Consistent value" is the value the ruling gives on the reader's own evidence.

| Product | Service | Value given | Second-read | Ruling | Evidence (file:line) | Consistent value | Direction | Confidence |
|---|---|---|---|---|---|---|---|---|
| OpenAI Dots | Tasks | yes | no | R1 | `openai-dots.md:23`: "Tasks are listed as In progress, Scheduled and Completed (Help start) and can be stopped one by one (Controls). Retry and recovery are not described". Codex was lowered to part on the same gap (tracking and cancellation stated, retry and recovery of the unit not). | part | lower | clear |
| Claude Code | Policy | yes | no | R2 | `claude-code.md:38`: "Content in and out: "You set which files and network domains those commands can reach" (docs:sandboxing.md)." That is a filesystem and network rule, the kind R2 does not count as a content rule; no other content rule is quoted. | part | lower | clear |
| Grok Build | Policy | yes | no | R2 | `grok-build.md:38`: "Rules on actions (allow, deny, ask), on content paths (sandbox, `web_fetch` domain allowlist, MCP allowlists) and on retention (zero data retention)." The "content paths" are filesystem and network rules. The row also names no grant (the remembered grant is quoted in the Approvals row, line 39). | part | lower | clear |
| OpenAI Dots | Orchestration | yes | no | R11 | `openai-dots.md:35`: "Your dot can divide work among background agents that run in parallel and report back to it." and "Dependencies between tasks are not described." Codex rates part on the same gap (`codex.md:35`: "dependencies between pieces of work are not stated"). | part | lower | clear |
| Tasks in Gemini | Improvement | no (DISPUTABLE, part) | yes (both readers no) | R4 | `gemini-spark.md:44`: "A reader may count "Gemini can now help you build custom skills from your chats" (release notes 2026.09.30) as part." The adjudication itself calls this the same kind of feature as Grok Build's `/skillify` and Antigravity's `/learn` (line 119). | part | higher | clear |
| Tasks in Gemini | Environments | yes | no | R8 | `gemini-spark.md:25`: "Gemini can connect to the local Chrome browser on your desktop or use a separate remote browser in the cloud." and "Gemini can only view files or directories that you specifically add". The row states a place to act and a file scope but no isolation of the agent from others; the local Chrome option is the user's own browser. "Separate remote browser" may or may not mean isolated. | part | lower | unclear |
| Codex CLI | Identity | yes | yes (both readers yes) | R9 | `codex.md:37`: "Each token belongs to its creator ... Tokens act as agent identities" and "On other plans an agent acts as the signed-in user. Subagents have no identity of their own". Dots was lowered partly because its inventory and revocation are Enterprise only and the agent acts as the owner in connected apps. Codex's agent identities are Business, Enterprise and pay-as-you-go only, and elsewhere the agent acts as the user. R9 does not say whether a plan-limited agent identity is enough for yes, and R13 says plan limits do not lower a value. | part | lower | unclear |
| Grok Build | Orchestration | yes | no | R11 | `grok-build.md:34`: "Workflows orchestrate a bounded set of subagents in the background: fan out work, verify, then return a result." No dependency coordination is quoted; "fan out, verify, return" is a fixed order of steps, which may or may not count as coordinating what depends on what. | part | lower | unclear |
| Tasks in Gemini | Sessions | yes | no | R5 | `gemini-spark.md:23`: "Gemini will automatically resume paused tasks and schedules." History, pause and resume are stated; hand-off is not. R5 lowered a cell where none of pause, resume and hand-off was described; it does not settle a cell with pause and resume but no hand-off. | part | lower | unclear |
| Grok Bot | Sessions | yes | yes (both readers yes) | R5 | `grok-bot.md:22`: "Conversations are stored outside the computer, so they survive even a reset." and "A Bot that is mid-turn pauses at a safe point and resumes on the new computer." Same situation as the row above: pause and resume stated, hand-off not. (Antigravity and Grok Build also quote no hand-off, but each states fork, which I counted as covering it; Codex, Claude Code and Dots state a hand-off between surfaces or to the person.) | part | lower | unclear |

Cells checked and found consistent with the rulings (no entry above): Tasks for Claude Code (its row states restart and re-run of the tracked session), Grok Build, Antigravity, Claude Duet, Grok Bot, Tasks in Gemini and Muse; Policy for Antigravity, Claude Duet, Grok Bot, Tasks in Gemini; Scheduling for all products under R3 (only Grok Build is session-scoped); Improvement for the other eight; Sessions for Claude Code, Codex, Grok Build, Antigravity, Dots and Muse; Observability for all nine; Environments for the other eight (Muse and Duet state isolation, Grok Bot and Dots carry the vendor's disclaimer at part); Identity for the other eight; Evaluation for all nine; Orchestration for Claude Code and Antigravity (both state dependencies), Codex, Claude Duet, Tasks in Gemini and Muse; Models for all nine (Muse's part is the lower value and its row says no page states how a model is chosen); C3 for all nine (all part after adjudication); C1 for all nine under R12; C4 for all nine under R13 (Claude Code and Antigravity match work to an agent inside the delegating agent's reasoning, which the criteria rate part); C2 under R15 (no other product rated C2 on two units); the derived Directory row for all nine.

Counts of Section 2: 10 cells. Clear: 4 lower, 1 higher. Unclear: 5 lower, 0 higher.

# Section 3. Like-case pairs

| Kind of evidence | Lower value | Higher value | Value the ruling supports |
|---|---|---|---|
| Policy: action rules, grants, and filesystem and network rules as the only "content" rule (R2) | Codex part* (adjudicated, `codex.md:39`); Antigravity part* (`antigravity.md:39`: "Content is governed only by where the agent may read and browse") | Claude Code yes (`claude-code.md:38`); Grok Build yes (`grok-build.md:38`) | part |
| Tasks: tracking and stop stated, retry and recovery not (R1) | Codex part* (adjudicated); Grok Bot part (`grok-bot.md:23`); Claude Duet part* (`claude-duet.md:35`) | Dots yes (`openai-dots.md:23`) | part |
| Orchestration: work divided among agents and results returned, dependencies not stated (R11) | Codex part* (`codex.md:35`); Grok Bot part* (adjudicated) | Dots yes (`openai-dots.md:35`); Grok Build yes (`grok-build.md:34`, unclear) | part (Dots clear, Grok Build unclear) |
| Improvement: a skill built from a session or chats on request (R4) | Tasks in Gemini no* (`gemini-spark.md:44`) | Grok Build part* (adjudicated); Antigravity part* (`antigravity.md:43`) | part (the adjudication already names this pair, line 119) |
| Identity: agent identity on some plans only; elsewhere the agent acts as the person (R9) | Dots part* (adjudicated, `openai-dots.md:37`) | Codex yes (`codex.md:37`) | unclear; R9 points to part where the agent acts as the owner, R13 says plan scope does not lower a value |
| Environments: place to act supplied, isolation of the agent not established (R8) | Grok Bot part* (`grok-bot.md:24`); Dots part* (adjudicated) | Tasks in Gemini yes (`gemini-spark.md:25`) | unclear; Grok Bot and Dots carry an explicit vendor disclaimer, Gemini's row is silent on isolation |
| Scheduling: start at a time and on an event, in the vendor's cloud, no limit on how much may run at once | Muse part* (`meta-muse.md:46`: "A limit on how much runs at once is not found"); Claude Duet part* (`claude-duet.md:37`); Antigravity part (`antigravity.md:25`) | Dots yes (`openai-dots.md:25`: "No limit on how much may run at once is stated.") | No ruling settles this pair. R3 is about session scope, and Dots, Muse and Duet all run in the vendor's cloud. The adjudication applies other definitions clause by clause (R1, R2, R5, R11, R14), which would give part, but it never rules on the limits clause. Not counted in Section 2. |
| Secrets: a point-of-use store on one surface only (cloud or remote environments) | Antigravity part* (`antigravity.md:38`: "Yes is defensible for remote agents alone.") | Claude Code yes (`claude-code.md:37`, "Anthropic-hosted cloud environments only"); Codex yes (`codex.md:38`, "Codex Cloud environments only") | No ruling governs Secrets. The difference follows Claude Code's own surface rule (Section 4). Not counted in Section 2. |

# Section 4. Reader-specific rules

| Reader | Rule as stated | Differs from the protocol how | Cells it affects |
|---|---|---|---|
| Claude Code | `claude-code.md:14`: "when a feature carries out a service's full definition on one surface only (cloud sessions only, or local sessions only), I rate **yes** and name the surface in the Availability column." | The protocol says nothing about surfaces. Other readers did the opposite on like evidence (Antigravity Secrets, line 38, and Reliability, line 45, gave part and called yes "defensible" for one surface). R3 accepted this rule for Scheduling. | Scheduling (cloud only, line 24), Secrets (cloud only, line 37), Lifecycle ("local machine only", line 25). |
| Claude Code | Title and line 12: rated under protocol version 1. Directory (line 32) is rated "no. DISPUTABLE (part)" from the definition, with the derived part noted. | Version 2 says to derive Directory and not rate it from the definition. | Directory: the file's literal value is no; the derived value, used in the totals, is part. This is why the literal file count is 19/5/1 and the totals say 19/6/0. |
| Codex | `codex.md:13`: "I counted a ChatGPT-wide feature only where the page says it applies to Codex, and I say so in the cell." (Its title also says protocol version 1; its Directory row is derived as version 2 requires.) | A scope rule the protocol does not state. | C1 (Enterprise teams not counted, line 55); Policy, Identity and Observability rows that rest on workspace features say whether the page names Codex. |
| Grok Bot | `grok-bot.md:13`: "I treated docs.x.ai, x.ai and the cursor.com pages the Grok Bot docs link to as the vendor's own material." | The protocol requires the vendor's own material; Cursor is named as the account and admin provider. `table-25x9.md` notes this is not yet confirmed. | No service row in the table cites a cursor.com page; cursor.com pages are cited in question 3 and the pages list (lines 87, 137, 138). The adjudication cites a Cursor page for C1 (adjudication line 101). |
| Grok Bot | `grok-bot.md:15`: "Values below rate the product as a whole and say when a feature is limited to one kind." Line 149 leaves open "whether features documented only for Enterprise teams or only for Team Bots should count". | The protocol asks only whether "a user of the product can use it today". In Policy (line 39) the reader gives part partly because "the content and retention controls are not available to an individual"; in Observability (line 41) it gives yes with the full record Enterprise only. R13 says plan scope does not lower a value. | Policy (line 39); the reader names Lifecycle, Improvement and C4 as also moved by this question. Under R2 Grok Bot Policy stays part on other grounds (the network policy is a destination rule, and inference hooks call the customer's own server), so it is not in Section 2. |
| OpenAI Dots | `openai-dots.md:141`: pages that refused the requests "were therefore read from Internet Archive snapshots 5 to 37 days old" and "Cells that rest on a snapshot alone: none of the 25". | The protocol says every value rests "on a page you opened today" and does not mention archive copies. | Rows whose reasons cite a snapshot page: Tasks, Environments, Memory, Artifacts, Messaging, Identity, Observability, Improvement, Releases, Reliability (lines 23 to 45). |
| Meta Muse | `meta-muse.md` Disclosures: pages read [quotation withheld: muse.ai page] despite a robots.txt notice against automated collection. | A source-access decision, not a rating rule; listed because the author's ruling on these pages decides the column (adjudication line 122). | 19 of 24 rated rows cite a muse.ai page (adjudication line 122). |
| Claude Duet | `claude-duet.md:139`: "the lower value is given and the cell is marked DISPUTABLE, as the protocol requires." | Same as the protocol. Listed only to record that it was checked. | none |

# Section 5. Counts

Script: `scratch/counts.py`, run as `python3 -I counts.py <vendors-dir> paper/build/vendor-totals.json`. It parses the 25-row table of each reader file, sets Directory from C3 and C4 (with the adjudicated C3 and C4 values), applies the 19 adjudicated values, then applies the Section 2 changes. Its output, as read:

```
product        literal-files  (a)reader+19  vendor-totals  match  (b)+clear  (c)+clear+unclear
claude-code    19/5/1        19/6/0        19/6/0         True   18/7/0     18/7/0
codex          14/11/0       13/12/0       13/12/0        True   13/12/0    12/13/0
grok-build     13/12/0       13/12/0       13/12/0        True   12/13/0    11/14/0
antigravity    13/12/0       13/12/0       13/12/0        True   13/12/0    13/12/0
claude-duet    8/8/9         7/10/8        7/10/8         True   7/10/8     7/10/8
openai-dots    16/7/2        13/10/2       13/10/2        True   11/12/2    11/12/2
grok-bot       12/12/1       12/12/1       12/12/1        True   12/12/1    11/13/1
gemini-spark   8/11/6        8/12/5        8/12/5         True   8/13/4     6/15/4
meta-muse      8/16/1        8/16/1        8/16/1         True   8/16/1     8/16/1
(a) totals yes/part/no = 106/102/17 cells = 225
(b) totals yes/part/no = 102/107/16 cells = 225
(c) totals yes/part/no = 97/112/16 cells = 225
```

- (a) The reader files plus the 19 decided values (Directory derived) match `paper/build/vendor-totals.json` for all nine products. The only literal-file difference is Claude Code's Directory (see Section 4).
- (b) With the five clear changes: 102 yes, 107 part, 16 no.
- (c) With the clear and unclear changes: 97 yes, 112 part, 16 no.
- Effect on statements in `vendor-totals.json`: under (b) Policy has 0 yes (was 2) and Tasks 1 yes (was 2); Orchestration 3 yes (was 4); Improvement 0 yes, 8 part, 1 no. "Policy" would join the zero-yes services under (b).

The script:

```python
#!/usr/bin/env python3
"""Recount yes/part/no per product from the nine reader files, the 19 adjudicated
values, and the changes listed in consistency-check.md Section 2.
Usage: python3 -I counts.py <vendors-dir> <vendor-totals.json>"""
import json, re, sys
from pathlib import Path

D = Path(sys.argv[1])
PRODUCTS = ["claude-code", "codex", "grok-build", "antigravity", "claude-duet",
            "openai-dots", "grok-bot", "gemini-spark", "meta-muse"]
SERVICES = ["Harness", "Sessions", "Tasks", "Environments", "Scheduling", "Lifecycle",
            "Memory", "Retrieval", "Artifacts", "Models", "Tools", "Registry", "Directory",
            "Messaging", "Orchestration", "Channels", "Identity", "Secrets", "Policy",
            "Approvals", "Observability", "Evaluation", "Improvement", "Releases", "Reliability"]
VAL = re.compile(r"^\**\s*(yes|part|no|not assessed)\b", re.I)

def read_table(p):
    vals = {}
    for line in (D / f"{p}.md").read_text().splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        for i, c in enumerate(cells[:2]):          # service is col 0 or col 1 (with group)
            if c in SERVICES and i + 1 < len(cells):
                m = VAL.match(cells[i + 1])
                if m and c not in vals:
                    vals[c] = m.group(1).lower()
    missing = [s for s in SERVICES if s not in vals]
    assert not missing, (p, missing)
    return vals

# C3/C4 per reader (first-reader values, from each file's question 1) and adjudicated C3/C4
C34_FIRST = {"claude-code": ("part", "part"), "codex": ("part", "part"), "grok-build": ("part", "part"),
             "antigravity": ("part", "part"), "claude-duet": ("no", "no"), "openai-dots": ("part", "part"),
             "grok-bot": ("part", "part"), "gemini-spark": ("no", "no"), "meta-muse": ("part", "part")}
C_ADJ = {("claude-duet", "C3"): "part", ("gemini-spark", "C3"): "part", ("meta-muse", "C3"): "part",
         ("grok-bot", "C4"): "yes"}
ADJ = {("codex", "Tasks"): "part", ("codex", "Policy"): "part", ("grok-build", "Scheduling"): "part",
       ("grok-build", "Improvement"): "part", ("claude-duet", "Sessions"): "part",
       ("claude-duet", "Observability"): "part", ("openai-dots", "Environments"): "part",
       ("openai-dots", "Identity"): "part", ("openai-dots", "Policy"): "part",
       ("openai-dots", "Evaluation"): "no", ("grok-bot", "Orchestration"): "part",
       ("gemini-spark", "Models"): "part", ("meta-muse", "Policy"): "part"}
CLEAR = {("openai-dots", "Tasks"): "part", ("claude-code", "Policy"): "part",
         ("grok-build", "Policy"): "part", ("openai-dots", "Orchestration"): "part",
         ("gemini-spark", "Improvement"): "part"}
UNCLEAR = {("gemini-spark", "Environments"): "part", ("codex", "Identity"): "part",
           ("grok-build", "Orchestration"): "part", ("gemini-spark", "Sessions"): "part",
           ("grok-bot", "Sessions"): "part"}

def derive(c3, c4):
    if c3 == "yes" and c4 == "yes": return "yes"
    if "yes" in (c3, c4) or "part" in (c3, c4): return "part"
    return "no"

def count(table):
    return {p: [sum(table[p][s] == v for s in SERVICES) for v in ("yes", "part", "no")] for p in PRODUCTS}

raw = {p: read_table(p) for p in PRODUCTS}
literal = count(raw)
base = {}
for p in PRODUCTS:
    t = dict(raw[p])
    c3 = C_ADJ.get((p, "C3"), C34_FIRST[p][0]); c4 = C_ADJ.get((p, "C4"), C34_FIRST[p][1])
    t["Directory"] = derive(c3, c4)
    for (q, s), v in ADJ.items():
        if q == p:
            pass  # adjudicated value replaces the first reader's (often equal)
            t[s] = v
    base[p] = t

def apply(tbl, changes):
    out = {p: dict(v) for p, v in tbl.items()}
    for (p, s), v in changes.items():
        assert out[p][s] != v, (p, s)
        out[p][s] = v
    return out

a = count(base); b = count(apply(base, CLEAR)); c = count(apply(base, {**CLEAR, **UNCLEAR}))
cur = json.loads(Path(sys.argv[2]).read_text())["per_product"]
print("product        literal-files  (a)reader+19  vendor-totals  match  (b)+clear  (c)+clear+unclear")
for p in PRODUCTS:
    print(f"{p:14} {'/'.join(map(str, literal[p])):13} {'/'.join(map(str, a[p])):13} "
          f"{'/'.join(map(str, cur[p])):14} {str(a[p] == cur[p]):6} {'/'.join(map(str, b[p])):10} {'/'.join(map(str, c[p]))}")
for name, t in (("(a)", a), ("(b)", b), ("(c)", c)):
    tot = [sum(t[p][i] for p in PRODUCTS) for i in range(3)]
    print(name, "totals yes/part/no =", "/".join(map(str, tot)), "cells =", sum(tot))
```

The per-service statements in the bullet list after the output were worked out from the Section 2 table and the per-service figures in `vendor-totals.json`, not by the script.

# Section 6. What I did not check

- Services that no ruling governs: Harness, Lifecycle, Memory, Retrieval, Artifacts, Tools, Registry, Messaging, Channels, Secrets, Approvals, Releases and Reliability. I did not check them for consistency, apart from the Secrets pair in Section 3, which I came across while reading.
- Whether any quote is on the vendor's page, or says what the reader says it does. I took each row as written.
- The second reader's own files (`second-reader/out/*.md`). I used `second-reader-comparison.md` and `sample.txt` only to mark which cells were second-read and how they compared.
- Whether the 19 adjudicated values are right. I took them as given and checked the other cells against them.
- The C1 to C4 cells beyond R7, R12, R13 and R15. I did not re-rate C1, C2 or C4 on their own criteria.
- The questions the rulings leave open: whether plan-limited features (Enterprise, Team) count toward yes for services (R9 and R13 point different ways), whether a service's limits clause is required for yes on Scheduling, and whether fork counts as hand-off under Sessions. The "unclear" cells and the two pairs marked "no ruling settles" depend on these.
- The 19 adjudicated cells themselves, the Muse robots.txt question, and `claude-managed-agents.md`.
- The three files I was told not to open (`paper/claude-review-d6.md`, `paper/astra-review-d6.log`, `paper/astra-review-d6-partial-codex.md`); I did not open them.
