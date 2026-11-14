---
title: "Vendor mappings, tenth product: does the Claude Managed Agents (self-hosted) column follow the adjudication's rulings?"
date: 2026-11-13
author: "consistency checker for the tenth product (Claude subagent), read-only except this file"
status: "first pass; not reviewed"
inputs: "protocol-v2.md, second-reader/rerate-criteria-v2.md, adjudication-19.md, second-reader/comparison-claude-managed-agents.md, consistency-check.md, claude-managed-agents.md, second-reader/out/claude-managed-agents.md, and for like cases the rows of claude-code.md, codex.md, grok-build.md, antigravity.md, claude-duet.md, openai-dots.md, grok-bot.md, gemini-spark.md, meta-muse.md"
---

# How the check was done

- I read the files in the order the brief gave. The general rulings are R1 to R15 of `consistency-check.md` Section 1 (lines 20 to 37), plus two rulings from `second-reader/comparison-claude-managed-agents.md`, stated so they apply to any product:
  - **R20 (Environments)**: a place to act that isolates sessions from one another, while agents inside one session share one sandbox, rates part, DISPUTABLE (yes); yes is defensible only if isolation between sessions suffices (comparison file line 36).
  - **R21 (Channels)**: when people reach the agent only through the vendor's own console, app or terminal, with no adapter to a channel people already use, the cell rates part, DISPUTABLE (yes), even when applications have an API (comparison file line 40).
  - Ruling 22 (C3) is the R7 ruling applied again (comparison file line 43), so I list it under R7.
- For every governed cell of the tenth product I read the first reader's row (`claude-managed-agents.md`) and, for the eight sampled services and C1 to C4, the second reader's row (`second-reader/out/claude-managed-agents.md`). I judged each cell from what its row says (value, quotations, notes), as `consistency-check.md` did.
- I used that file's three classes: **follows**; **clearly does not follow** (the row's own text meets the wording of a ruling that gives another value); **unclear** (the ruling does not settle the situation the row describes, or the row's text fits two readings).
- For like cases (Section B) I read the same service's row in the nine other reader files.
- Line numbers are line numbers of the named file as it stood on 2026-11-13. I checked each quoted string against its file with `grep -n -F`.
- The adjudicated values for this product are the first reader's values with Environments set to part* (ruling 20). Channels (part*) and C3 (part) kept the first reader's value.

# A. Governed cells

`*` marks DISPUTABLE. "CMA" is `claude-managed-agents.md`; "CMA-2" is `second-reader/out/claude-managed-agents.md`.

| Cell | Value now | Ruling | Evidence (file:line) | Classification | Direction and value |
|---|---|---|---|---|---|
| Tasks | part* (yes) | R1 | CMA:27: "the server retries failed model calls, a turn continues in a new sandbox, `user.interrupt` and a work-item stop cancel, and the request stays in the event history. There is no task record apart from the session, which can hold many requests." Also "The session’s status stays `running` between attempts". | unclear | Possibly higher, to yes. R1 lists the session as a possible unit ("the goal, task or session that keeps the request") and asks for retry or recovery of that unit; a turn that "continues in a new sandbox" and a status kept "between attempts" may be recovery of the session's work. Against: the model-call retry is a retry inside a turn, which R1 does not count, and the reader's objection is that the session is not one unit of work but holds many requests. Claude Code's yes rests on a session "that holds one dispatched task" (`claude-code.md:22`). R1 does not settle a session that holds many requests. |
| Sessions | yes | R5 | CMA:26: "Sessions pause (`idle`), resume on the next `user.message`, archive and delete." and "Sessions and their history stay in your database until you delete them." No hand-off is stated in the row. | unclear | Possibly lower, to part. Same situation as the two Sessions cells that `consistency-check.md` classified unclear (Tasks in Gemini, line 55; Grok Bot, line 56): history, pause and resume stated, hand-off not. R5 lowered a cell where none of pause, resume and hand-off was described. The row elsewhere says a session keeps running when the terminal chat is left (CMA:93, under question 4, not in the Sessions row), which a reader might count as a hand-off between clients. |
| Environments | part* (yes) | R8, R20 | CMA:28: "Agents in one multiagent session share the sandbox." CMA-2:5: "Supplied stacks isolate sessions, but agents within a session share their environment." | follows | Decided cell (ruling 20). |
| Scheduling | part | R3 | CMA:29: "It starts nothing at a time or on an event." and "The server has no routes for them." CMA-2:6: "Scheduled deployments and webhooks are absent; timed starts require the customer’s scheduler." | follows | None. R3 allows yes only on scheduled starts that run with no session open; the row states there are none. |
| Models | part* (yes) | R14 | CMA:34: "The builder names the model per agent, per session override or per listed subagent; the server does not choose a model for a task, except the refusal fallback under the Claude API." and "The server mediates every model call and sends it to one of five provider settings". | clearly does not follow | Higher, to yes (DISPUTABLE (part) would carry the reader's objection). R14: "Yes also needs the product or its configuration to choose the model for each task" and "Several models of one vendor meet "more than one model or vendor"". The row states a choice per agent and per listed subagent by configuration, and several Claude models across five providers. The reader's reason for part is that the server itself does not choose, which R14's "or its configuration" does not require. Like cases at yes on configuration alone: `codex.md:30` ("Model choice per agent is by configuration or spawn request ... no automatic routing by task is stated"); `grok-build.md:29` ("map of subagent → model id"); `antigravity.md:30` (a custom agent's `model` field). The one cell R14 lowered was a person switching by hand (`gemini-spark.md:31`). |
| Orchestration | part | R11 | CMA:39: "One agent delegates one level down to 1 to 20 listed agents and reads their reports; people enter only through tool confirmations. No fixed steps and no dependencies between assignments." | follows | None. |
| Channels | part* (yes) | R21 | CMA:40: "No adapter to chat, email or other channels people already use, and no webhooks; the customer builds those on the API." | follows | Decided cell (ruling 21). The second reader's yes (CMA-2:9) is the value ruling 21 set aside. |
| Identity | part* (yes) | R9 | CMA:41: "an agent token carries `agent_id` and, for a tool call, the session creator in `actor_sub`; archiving the agent stops its tokens." and "agent tokens are optional and cover MCP calls only." and "The pages record a creator ... not an accountable person". | follows | None. An identity distinct from the person exists only for MCP calls and only when turned on, and the row records no accountable person. R9 gives part where the agent does not have its own identity throughout. See also Section B (Codex). |
| Policy | part* (yes) | R2, R2b | CMA:43: "Rules decide tool calls (`always_allow`, `always_ask`, `auto`), which MCP, Git and web hosts and which push branches are allowed, what sandboxes can reach" and "For stored data the only rule is a retention period for sandbox volumes" and "No grant is issued". | follows | None for the value. Note: the row's DISPUTABLE reason, "Yes is defensible on the action and content rules", counts host allowlists as content rules, which R2 does not; under R2 yes also fails on the missing grant. The mark does not change the value. |
| Observability | yes | R6 | CMA:45: "Every session's events are kept and can be listed or streamed; the server logs to standard error, including the caller of each request; traces and metrics go to an OpenTelemetry collector or a Prometheus endpoint when turned on". | follows | None. R6 accepts a log, trace or export. |
| Evaluation | part* (yes) | R10 | CMA:46: "A grader scores a work product against a rubric and reports `satisfied`, `needs_revision`, `max_iterations_reached`, `failed` or `interrupted`. No result is described as "unknown" for a check that could not run". | follows | None. A review feature with stated criteria (a rubric) meets R10's floor for part. The yes argument (CMA:46, `failed` and `interrupted` are not verdicts) has the same shape as Claude Code's part* (`claude-code.md:41`). |
| Improvement | no | R4 | CMA:47: "Not found. Searched every downloaded page for "improv", "propos", "feedback", "dream", "learn"." CMA-2:11: "no feature proposing agent, skill, or platform changes from evidence." | follows | None. Neither row names a feature that turns a session into a skill, so R4's part does not apply. |
| C1 | part | R12 (and criteria) | CMA:57: "The only unit that stands for an organization is the deployment, which is the whole system" and "The other grouping is one agent with its listed subagents, which is one team of agents". CMA-2:14: "Areas appear as individual specialist agents". | follows | None. Both cases are named under part in the criteria. |
| C2 | part | R15 | CMA:61: "Rated on the deployment." and "No page states what a deployment as a whole is for, so (a) is not met." | follows | None. One unit is rated, so R15's two-candidate case does not arise. |
| C3 | part | R7 (ruling 22) | CMA:65: "The record names a creator per asset. It does not state accountability and is not per responsibility or capability." | follows | Decided cell (ruling 22). |
| C4 | part | R13 | CMA:69: "No agent can look up a handler from a kind of work, and no directory or broker is defined. Routing exists only inside one orchestrator's logic." | follows | None. |
| Directory | part (derived) | R7, derivation rule | CMA:37: "derived from C3 = part and C4 = part" | follows | None. |

Counts of Section A: 17 governed cells. Follows: 14. Clearly does not follow: 1 (Models, higher). Unclear: 2 (Tasks, possibly higher; Sessions, possibly lower).

# B. Like cases with no ruling

No ruling of the adjudication governs Approvals, Releases, Reliability, Harness, Lifecycle, Memory, Retrieval, Artifacts, Tools, Registry, Messaging or Secrets. Identity, Policy and Evaluation are governed (Section A); I compare them here as well because the brief asks.

## Approvals: out of line with the like cases (lower)

- Tenth product, part* (yes), CMA:44: "Approval in advance exists only as the `always_allow` policy on a tool: no stated conditions and no record of who approved. Yes is defensible if a per-tool policy counts as approval of a class of actions." The same row states the held single action and its record: "A held call waits for a person's `user.tool_confirmation` (allow or deny, with a message), which is kept in the session's events."
- Compare `gemini-spark.md:41`, yes: "Always allow: Approves the action for the current thread and all future task threads. Selecting this automatically updates your preference to “Always allow” in your settings." That row states no conditions and no record of who approved.
- Compare `antigravity.md:40`, yes: "access_grants (array of strings): Scoped, pre-approved permissions, such as command(gh issue list), read_file(/abs/path), write_file(/abs/path), mcp(<server>/<tool>), or read_url(github.com)." That is an advance permission written in configuration, scoped per tool or command, like `always_allow`.
- Also yes on a saved allow rule: `claude-code.md:39`, `codex.md:40`, `grok-build.md:39`, `grok-bot.md:40`. Also yes where the row says no record of approvals is described: `claude-duet.md:52` ("A separate record of approvals is not described.") and `openai-dots.md:40` ("a record of each single decision is not described").
- All nine other products rate Approvals yes. The two reasons the tenth reader gives for part (no stated conditions, no record of who approved the advance rule) are both true of at least one yes row (Gemini states neither). The tenth row also states a kept record of single decisions, which Dots and Duet lack.
- One difference: in Claude Code, Codex, Grok Build, Grok Bot and Gemini a person's click at a prompt creates the advance rule; in the tenth product the builder sets the policy on the agent. Antigravity's `access_grants` is set in configuration and rates yes, so this difference does not separate the tenth product from every yes row.
- No ruling settles this. On the like cases the consistent value is yes, which the cell's DISPUTABLE mark already names.

## Identity: not clearly out of line

- Tenth product, part* (yes), CMA:41 (quoted in Section A).
- Compare `codex.md:37`, yes: "Each token belongs to its creator and that user's ChatGPT workspace. Tokens act as agent identities for programmatic local workflows." with "On other plans an agent acts as the signed-in user." Codex records a creator per token, as the tenth product records a creator per resource, and rates yes; the tenth reader rates part because a creator is not an accountable person.
- Compare `claude-code.md:36`, part (yes), where yes is "defensible for self-hosted environments" on a signed session token, and Dots part* (adjudicated, cell 10).
- The tenth value sits with Claude Code and Dots. `consistency-check.md` line 53 already classified Codex's yes as unclear (lower). R9 governs this row; it does not settle whether a recorded creator counts as the accountable person.

## Policy: in line

- Tenth product, part* (yes), CMA:43. Compare `codex.md` Policy, part* (adjudicated, cell 2), and `antigravity.md:39`, part* ("Content is governed only by where the agent may read and browse", quoted at `consistency-check.md:66`). Same kind of evidence (action rules plus host and path rules), same value. R2 governs.

## Evaluation: in line

- Tenth product, part* (yes), CMA:46. Compare `claude-code.md:41`, part (yes): "a run that could not be graded is scored as a failure, not as unknown", and `codex.md:42`, part (yes): "`verify-fix` returns `2` if any check is inconclusive or fails." Each has a check with stated criteria and a non-verdict result short of "unknown". R10 governs.

## Releases: in line

- Tenth product, part* (yes), CMA:48: "Agents and skills have versions and a session can pin one" and "The server's settings file is not versioned by the product. Yes is defensible because versions and a way back exist for agents, skills and the platform."
- Compare `claude-code.md:43`, part (yes): "I found nothing that versions or releases rules or infrastructure. Yes is defensible on plugin versions plus the product's own release channels." and `grok-build.md:43`, part: "Agent definitions, skills and rules are plain files; no release or rollback mechanism of the product's own was found for them."
- No product rates Releases yes. The tenth row states more (versions and a way back for agents, skills and the platform) than any other row, and still lacks rules (the settings file). Part fits the definition's list ("agents, skills, rules, the platform and the infrastructure"). No ruling settles whether a missing item lowers a cell; the like cases do not show the tenth value out of line.

## Reliability: not clearly out of line; the like cases split

- Tenth product, part* (yes), CMA:49: "The product supplies mechanisms: the server chart "runs two servers behind a Service", readiness and health endpoints, retried model calls, a turn that continues in a new sandbox, and a documented backup and restore. Keeping the service, the database and the workers available is the customer's work." CMA-2:12: "On Kubernetes, the kubelet restarts a pod whose probes wait too long."
- Higher: `claude-code.md:44`, yes: "Exited unexpectedly while the supervisor is running: the supervisor restarts the process." and `grok-bot.md:45`, yes, on restore from a durable copy and **Recover**.
- Lower: `antigravity.md:45`, part (yes): "Antigravity manages the lifecycle of sidecars, automatically launching them and restarting them if they crash or error." and `codex.md:45`, part, on request retries and recoverable task state.
- In Claude Code and Grok Bot the product itself restarts or restores; in the tenth product the restart is done by the customer's Kubernetes cluster from the product's probes, and the product documents backup and restore for the operator to run. The tenth row sits between Antigravity (part*, restart of its own services) and Claude Code (yes). No ruling settles this.

## Other services checked, no finding

- Artifacts (part, CMA:33): the other nine rate part except Claude Code (yes, on a versioned publish). In line.
- Messaging (part, CMA:38): messages only between a coordinator and its listed subagents; like `codex.md:34` and `openai-dots.md:34`, both part*. In line.
- Secrets (yes, CMA:42): a placeholder in the sandbox with injection at the point of use, like `codex.md:38`, `claude-duet.md:50` and `meta-muse.md:59`, all yes. In line.
- Harness, Lifecycle, Memory, Retrieval, Tools and Registry (all yes): each row states the feature for the definition; I found no like case rated lower on the same kind of evidence.

# C. Counts

Adjudicated now: 9 yes, 15 part, 1 no (first reader with ruling 20 applied; checked by counting CMA lines 25 to 49: the first reader gives 10 yes, 14 part, 1 no, and ruling 20 moves Environments from yes to part).

| Case | Change | Yes | Part | No |
|---|---|---|---|---|
| Now (adjudicated) | none | 9 | 15 | 1 |
| (b) clear changes applied | Models part to yes | 10 | 14 | 1 |
| (c) clear and unclear changes applied | also Tasks part to yes, Sessions yes to part | 10 | 14 | 1 |

- Under (c) the two unclear changes cancel in the count; they do not cancel in the per-service totals (Tasks gains a yes, Sessions loses one).
- Not part of (b) or (c), because no ruling governs it: if Approvals were moved to yes on the like cases in Section B, (b) would be 11 yes, 13 part, 1 no.
- Directory stays part in every case (C3 and C4 are not changed).

# What I did not open

- Anything under `../../paper/`, `../../PROGRESS.md`, and `../decision-review/`. I did not open them.
- Any vendor page. Every judgment rests on the rows as written; I did not check whether a quotation is on the vendor's page or says what the reader says it does.
- `table-25x9.md`, `second-reader-comparison.md`, `second-reader/sample.txt`, the second reader's files for the nine other products, and the briefs and logs under `second-reader/`. The sample for this product is the one the brief and the comparison file name.
- I did not re-examine the three decided cells (Environments, Channels, C3) beyond confirming their values, and I did not re-rate C1, C2 or C4 on their own criteria.
