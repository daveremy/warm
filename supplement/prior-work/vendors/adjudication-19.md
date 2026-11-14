---
title: "Vendor mappings: the 19 cells where the two readers differ, adjudicated"
date: 2026-11-12
author: sagan
status: "decided 2026-11-12 14:44 MST by sagan, one adjudicator, not blind (both readers' files were open). Deciding quotes checked against the live vendor pages today, except muse.ai pages."
---

## Method

- Input: the 19 DIFF lines in `second-reader-comparison.md`.
- For each cell I read both readers' rows, then applied `protocol-v2.md` (services) or `rerate-criteria-v2.md` (C1 to C4) as written.
- Rule for a tie: the protocol's own. When both values are defensible, the lower one stands and the cell is marked DISPUTABLE. A value counts as defensible only if the evidence fits the wording of that level.
- Consistency: where the same question decides several cells (Policy in three products, C3 in three), one ruling decides all of them, and I compared it with the values both readers agreed on for the other products.
- Quote check: I downloaded the cited pages with curl between 14:40 and 14:44 and searched the page text for each deciding quote (script with a negative control). 32 quoted strings on 16 pages were found as written. Not checked: the two Muse cells' quotes (muse.ai pages are not re-read until the author rules on the robots.txt notice) and the first reader's Dots safety-post quote (openai.com refuses automated requests).
- I wrote the paper these values serve, so I have an interest in low values on C1 to C4. Against the first readers' values, three cells went up, one of them (Grok Bot, C4) to yes.

## Result

| # | Product | Cell | First | Second | Adjudicated | Whose value |
|---|---|---|---|---|---|---|
| 1 | Codex CLI | Tasks | part* | yes | part* | first |
| 2 | Codex CLI | Policy | yes | part* | part* | second |
| 3 | Grok Build | Scheduling | part* | yes | part* | first |
| 4 | Grok Build | Improvement | part | yes | part* | first |
| 5 | Antigravity | C2 | part* | yes | part* | first |
| 6 | Claude Duet | Sessions | yes | part* | part* | second |
| 7 | Claude Duet | Observability | part* | yes | part* | first |
| 8 | Claude Duet | C3 | no* | part | part | second |
| 9 | Dots | Environments | yes | part* | part* | second |
| 10 | Dots | Identity | yes | part* | part* | second |
| 11 | Dots | Policy | yes | part* | part* | second |
| 12 | Dots | Evaluation | no* | part | no* | first |
| 13 | Grok Bot | Orchestration | part* | yes | part* | first |
| 14 | Grok Bot | C1 | part* | yes | part* | first |
| 15 | Grok Bot | C4 | part* | yes | **yes** | second |
| 16 | Tasks in Gemini | Models | part* | yes | part* | first |
| 17 | Tasks in Gemini | C3 | no* | part | part | second |
| 18 | Muse | Policy | part* | yes | part* | first |
| 19 | Muse | C3 | part | no* | part | first |

`*` marks DISPUTABLE.

- The first reader's value stands in 11 cells, the second reader's in 8.
- The lower of the two values stands in 15 cells. The higher stands in 4: C3 for Claude Duet, Tasks in Gemini and Muse (part over no) and Grok Bot C4 (yes over part).
- Adjudicated values: 17 part, 1 no, 1 yes.

## What changes

- **One yes on C1 to C4.** Grok Bot rates yes on C4. "No product rates yes on any of C1 to C4" is false after adjudication. What holds: no product rates yes on C1, C2 or C3; one product (Grok Bot) rates yes on C4, for Team Bots on the Team and Enterprise plans.
- **Improvement.** No product rates yes on Improvement after adjudication (Grok Build stays part).
- **Directory (derived).** Claude Duet and Tasks in Gemini move from no to part. Directory is then part for all nine products: 0 yes, 9 part, 0 no. Grok Bot stays part (C3 is part).
- **First-reader yes values lowered:** Codex Policy; Claude Duet Sessions; Dots Environments, Identity and Policy.
- **Per-product counts, sampled cells only** (yes/part/no): Codex 13/12/0 (was 14/11/0); Claude Duet 7/10/8 (was 8/8/9); Dots 13/10/2 (was 16/7/2); Tasks in Gemini 8/12/5 (was 8/11/6). The other five products are unchanged. `table-25x9.md` still shows first-reader values.
- Dots loses three yes values. Its first reader was the one that could not open openai.com or help.openai.com.

## The cells

### 1. Codex CLI, Tasks: part, DISPUTABLE (yes)
The second reader's quote is on the page: "If willRetry is true, the server retries and the turn stays active." (app-server, Errors). It describes the server retrying a failed request inside a turn of the experimental app-server interface. The units that keep the request and a status are the goal and the cloud task (first reader). No page says Codex coordinates the retry or recovery of a goal or a cloud task. Tracking, cancellation and the kept request are stated; retry and recovery of the unit of work are not.

### 2. Codex CLI, Policy: part, DISPUTABLE (yes)
One ruling for cells 2, 11 and 18. The definition has four parts: a rule decides whether an action proceeds; what content may enter and leave; what stored data is kept; a grant is issued. Yes needs each part stated. Codex states action rules, filesystem and network rules and grants. Neither reader found a rule on what content may enter or leave, and the first reader notes that rules on kept data "are limited to local history settings and workspace retention settings."

### 3. Grok Build, Scheduling: part, DISPUTABLE (yes)
The page states an interval timer, event monitors and a cap: "Loops expire after 7 days, and at most 50 scheduled tasks can be active at once." All three run inside an open Grok session. There is no start at a clock time and nothing starts work when Grok is not running. Claude Code's yes on this row rests on cloud scheduled tasks; its reader noted that `/loop` and `CronCreate` are session-scoped and did not rest the value on them. Same treatment here.

### 4. Grok Build, Improvement: part, DISPUTABLE (yes)
"Capture any session as a new skill with /skillify" is on x.ai/build, and both readers quote it. It turns one session into a skill when the user asks. It does not cover agents or the platform, and it is on the product page only (not in the documentation's command table or the changelog, first reader). Antigravity's `/learn` is the same kind of feature and both of its readers gave part. The second reader did not mark this cell DISPUTABLE; I do.

### 5. Antigravity, C2: part, DISPUTABLE (yes)
Both readers rate C1 part and name two candidate units: the Teamwork team, built for one request, and the Project, defined as folders and settings. Rated on the Teamwork team, C2 meets the wording of yes: the Request artifact "Captures your initial prompt, goals, constraints, and testable acceptance criteria", and the roles are defined apart from the agents. Rated on the Project, C2 is part (scope and settings, no statement of what the unit is for, no roles). The criteria do not say which unit to rate when C1 has two candidates, and version 2 rules that a unit that models a task is not an area of work. Both values are defensible, so the lower stands. This is the cell most likely to move if the criteria are tightened.

### 6. Claude Duet, Sessions: part, DISPUTABLE (yes)
History is kept ("keeps your conversation history and its memory so it can carry context between tasks"). Pause, resume and hand-off are not described as features; the first reader says so in its own row. Muse has the same evidence (history kept, pause, resume and hand-off not described) and its first reader gave part. Same value here.

### 7. Claude Duet, Observability: part, DISPUTABLE (yes)
The only statement is "You can see what Claude Duet has done and is doing in its task list, where each task has its own page". No page says what a task page records, and no log, trace or export was found. Tasks in Gemini rates yes on a page that names the steps and the files read or updated. The Duet sentence does not say that much.

### 8, 17, 19. C3 for Claude Duet, Tasks in Gemini and Muse: part
One ruling. The part level of C3 reads: "a record names an owner, a provider or a responsible party per agent, asset or capability, but accountability is not stated, not unique, or not per responsibility or capability." For the other six products both readers gave part on exactly such a record (a plugin author, a token creator, a Bot owner, a dot owner). The same reading applies here.
- **Claude Duet:** the Claude connector directory names a provider per connector ("Made by Google" on the Google Drive entry), and "The apps you have connected to Claude carry over to Claude Duet". The first reader's no does not fit the wording of the no level ("no such record").
- **Tasks in Gemini:** a shared skill has one owner ("As the owner of a skill, you can transfer ownership to anyone that it's been shared with."). The first reader gave no because the owner is an access role and not a statement of who answers for a responsibility. The part level covers exactly a record where "accountability is not stated".
- **Muse:** the first reader's part rests on the connector directory, which names a provider and a responsible developer per connector. That page is on a muse.ai host. If the author rules those pages out, the cell rests on the second reader's about.fb.com sentence, which names no provider, and becomes no, DISPUTABLE (part).

### 9. Dots, Environments: part, DISPUTABLE (yes)
Each dot "has its own computer and browser in the cloud". The vendor's own architecture diagram says of the boundary around delegated tasks: "Dashed box: separate task boundary, not an isolation guarantee." A place to act is supplied; isolation of each agent from the others is stated for users' environments (first reader, from an archive snapshot) and disclaimed for delegated tasks.

### 10. Dots, Identity: part, DISPUTABLE (yes)
The inventory that records the creator and the dot's identity, and the revocation, are Enterprise only. In connected apps the vendor's diagram says "Acting identity: dot owner", so the agent is not distinguished from the person there.

### 11. Dots, Policy: part, DISPUTABLE (yes)
Ruling as in cell 2. The action review is stated ("The review determines whether the action can proceed, needs your approval, or includes a step you must do yourself."). The vendor also says of custom rules: "They are instructions your dot tries to follow, and it can make mistakes", and "Auto-review coverage across browser, desktop, and delegated actions remains under review." A rule the agent tries to follow is not a decision by rule. Retention rules do not cover the dot's own notes (first reader).

### 12. Dots, Evaluation: no, DISPUTABLE (part)
The second reader's quote is on the page: "Your dot can check results and send follow-up instructions to tasks it created." It names no criteria and no result for a check that could not run. The products that rate part on this row have a review feature with stated criteria (Codex custom review instructions, Grok Build's reviewer panel, Antigravity's Auditor). Claude Duet, Muse and Grok Bot, where the only checks are action reviews counted under Policy, rate no. Same treatment here.

### 13. Grok Bot, Orchestration: part, DISPUTABLE (yes)
Handoff between Bots is stated ("The receiving Bot wakes, handles the request, and can reply later."). Who does what and what depends on what come from the person's message: "A useful kickoff assigns one owner per stage", and the page advises "Ask for a single owner at each stage." No record or mechanism of the product coordinates dependencies.

### 14. Grok Bot, C1: part, DISPUTABLE (yes). The closest call of the 19.
For yes: teams and groups are defined units with members, roles and rules; Bots belong to them ("Lists every Bot on your team"; Group Rules apply to a group's Bots); an organization holds several; and the Cursor Organizations page says teams are "created around departments, business units, regions, or roles." C1 lists "group" and "organization" among its examples.
For part: the Grok Bot pages define a team and a group as who may use a Bot and which settings apply ("To widen that baseline for one cohort"). The sentence about departments is on Cursor's Enterprise page and says what customers build teams around. Version 2 rules that the criterion asks whether the model can divide a system's work into more than one area, and no page says a team does that. The second reader applied this same reasoning to Grok Build's teams and gave part.
Both are defensible; the lower stands. Not re-examined: whether the agreed part values for Codex (Enterprise teams) and Dots (workspace groups) would also be disputable on this ground.

### 15. Grok Bot, C4: yes
The yes level reads: "at run time an agent can look up, from a kind of work or a capability, the agent or role that handles it and how to reach it." The pages state each element. Lookup by an agent from a kind of work: "Ask one of your Bots in your own chat, for example 'Is there a Team Bot for on-call triage?' It searches the Team Bots you can use by what they do" (Team Bots page; the source uses double quotation marks around the question). The handler and how to reach it: "A Team Bot can suggest other team Bots that fit a request and link to a chat with one." and "In a DM with a Team Bot, teammates can have it message other Team Bots they can use." (changelog).
Neither clause of the part level fits: the lookup is from a kind of work, and it is not inside one orchestrator's logic (any of a person's Bots can ask, about Bots other people made). The first reader's reasons for part (the lookup covers only Team Bots shared with the asking person; the pages describe it as answering a person) are limits of scope, and the criterion does not ask about them.
Scope to state with the value: Team Bots only, on the Team and Enterprise plans; among a person's own Bots, routing is inside the primary Bot (part).

### 16. Tasks in Gemini, Models: part, DISPUTABLE (yes)
Several models of one vendor meet "more than one model or vendor". The definition also asks the service to "choose the model for each task". The page says the person switches: "you can manually switch models in both Chat Mode and Task Mode." Automatic routing is not stated for tasks (first reader). The products that rate yes state a choice per task by the product or its configuration.

### 18. Muse, Policy: part, DISPUTABLE (yes)
Ruling as in cell 2. Both readers quote the vendor's safety post for rule decisions on actions and on content at egress, with scoped grants. The first reader searched for a rule on what stored data is kept and found none; the second reader says separate controls "govern stored data" and gives no quote for it. Both quotes are on a muse.ai page that I did not re-read; this cell depends on the author's ruling in the same way as cell 19.

## Limits

- One adjudicator, who is the paper's author and saw which reader gave which value.
- Only the 19 differing cells were adjudicated. The 89 cells where the readers agree were not re-read, and the 16 unsampled services per product have one reader. Two inconsistencies among agreed or unsampled cells are visible and not resolved: Tasks in Gemini rates no* on Improvement for building a skill from chats, where Grok Build and Antigravity rate part for the same kind of feature; and the C1 treatment of enterprise teams and groups (cell 14).
- The second reader is a different model family (gpt-6-astra); the first readers are Claude. Own-vendor readings are listed in `second-reader-comparison.md`.
- The Muse cells (18, 19) and the Dots safety-post quote were not checked against live pages.
- Muse as a whole: 19 of its 24 rated rows cite a muse.ai page and 12 cite nothing else (counted from the reader file's source keys). The author's ruling on those pages decides the column, not two cells.
- A quote check shows the words are on the page today. It does not show the reader understood them; for the 19 cells I read the surrounding text as well.
