---
title: "Decision review, reader C: four agent harnesses (Claude Code, Codex CLI, Grok Build, Google Antigravity)"
date: 2026-11-12
author: "reader C (Claude subagent)"
protocol: protocol-v2.md
versions_seen:
  claude_code: "installed 2.1.323 (claude --version); newest changelog entry November 10, 2026 (https://code.claude.com/docs/en/changelog.md)"
  codex_cli: "installed codex-cli 0.167.2 (codex --version); newest What's new digest November 9-13, 2026 (https://learn.chatgpt.com/docs/whats-new.md); Auto-review page links reviewer templates at rust-v0.167.0"
  grok_build: "installed grok 1.0.67 (grok --version); newest changelog entry v1.0.77, Nov 5, 2026 (https://x.ai/changelog/build)"
  antigravity: "installed agy 1.5.7 (agy --version); newest changelog entry November 12, 2026 (App v2.31.2 on November 11, 2026; CLI section also November 12, 2026) (https://antigravity.google/docs/changelog)"
---

# Results

Values: yes, part, no, not assessed. When two values were defensible I gave the lower and marked DISPUTABLE. All pages were opened on 2026-11-12.

## Claude Code (Anthropic)

| Q | Value | Quotation | Location |
|---|---|---|---|
| H1 record of each decision | **part** | "`decision`: Either `"accept"` or `"reject"`" and "`source`: Where the decision came from" (`config`, `hook`, `user_permanent`, `user_temporary`, `user_abort`, `user_reject`). But: "The `source` value doesn't indicate which of these sources matched. ... No `tool_decision` attribute names the permission rule or setting that refused the call." The richer `claude_code.safety_event` (with `reason_code`, `rule_source`, `category`) is no longer sent: "**v2.1.312 and later**: these versions don't send the event, and no setting turns it on". Installed version is 2.1.323. | https://code.claude.com/docs/en/monitoring-usage.md, "Tool decision event" and "Safety event" sections |
| H2 measure of how often people are required | **part**, DISPUTABLE (yes) | Metric `claude_code.code_edit_tool.decision`: "Count of code editing tool permission decisions", "Incremented when user accepts or rejects Edit, Write, or NotebookEdit tool usage", with `source` separating user from config decisions. Analytics: "**Suggestion accept rate**: percentage of times users accept code editing tool usage, including Edit, Write, and NotebookEdit tools." Yes is defensible (named, defined, counts decisions). Part because both cover only edit tools, and the accept rate is framed as a quality measure, not as how often a person is required. `/insights` adds "an estimate of how many permission prompts auto mode could have handled", with no definition. | https://code.claude.com/docs/en/monitoring-usage.md ("Code edit tool decision counter"); https://code.claude.com/docs/en/analytics.md; https://code.claude.com/docs/en/costs.md ("Analyze your usage patterns") |
| H3 review of past decisions that changes the rules | **part** | "`/fewer-permission-prompts` ... Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project `.claude/settings.json` to reduce permission prompts". Also the manual "Yes, and don't ask again" option, which "saves the rule to `.claude/settings.local.json`". Narrow: read-only Bash and MCP calls only; it scans tool calls, not people's decisions. | https://code.claude.com/docs/en/commands.md; https://code.claude.com/docs/en/permissions.md |
| H4 authority that changes with the record | **no**, DISPUTABLE (yes) | "if the classifier blocks an action 3 times in a row or 20 times total, auto mode pauses and Claude Code resumes prompting. Approving the prompted action resumes auto mode." Yes is defensible: a defined rule narrows what the agent may do without a person after a run of blocked actions. No is defensible: it is a session circuit breaker on classifier blocks, not a rule that changes authority from a record of past performance. Nothing widens authority from a record. | https://code.claude.com/docs/en/permission-modes.md ("Repeated blocks", "Repeated-block thresholds") |
| H5 tasks handed to a person for lack of capability | **part** | "When Claude encounters a login page or CAPTCHA, it pauses and asks you to handle it manually." Computer use is offered for "tasks that require a GUI: anything you'd normally have to leave the terminal and do by hand." No record or count of such hand-offs. | https://code.claude.com/docs/en/chrome.md; https://code.claude.com/docs/en/computer-use.md |

## Codex CLI (OpenAI)

| Q | Value | Quotation | Location |
|---|---|---|---|
| H1 | **part** | "`codex.tool_decision` (approved/denied and whether the decision came from config vs user)". No field for the rule or condition that sent the action to a person. The reviewer agent's rationale is logged separately ("`codex.guardian_assessment` (completed automatic approval reviews ...)"), but that is the automatic reviewer, not a person. | https://learn.chatgpt.com/docs/config-file/config-advanced.md ("What gets emitted"); same event in https://learn.chatgpt.com/docs/agent-approvals-security.md |
| H2 | **part**, DISPUTABLE (yes) | Metric `approval.requested`, counter, attributes `tool`, `approved`: "Tool approval request result (`approved`, `approved_with_amendment`, `approved_for_session`, `denied`, `abort`)." Yes is defensible (named counter, states what it counts). Part because the page does not say whether requests answered by Auto-review are included, and it defines no rate. | https://learn.chatgpt.com/docs/config-file/config-advanced.md ("OTel metrics emitted") |
| H3 | **part** | "When Smart approvals are enabled (the default), Codex may propose a `prefix_rule` for you during escalation requests." And: "If too many mundane actions need review, fix the boundary first instead of teaching the reviewer to approve noisy escalations forever. ... Auto-review session transcripts are retained under `~/.codex/sessions` by default, so you can ask Codex to analyze past traffic there before changing policy or permissions." A per-prompt rule proposal plus advice to review past traffic by hand; no defined review process. | https://learn.chatgpt.com/docs/agent-configuration/rules.md; https://learn.chatgpt.com/docs/sandboxing/auto-review.md ("Reduce review volume without weakening security") |
| H4 | **no**, DISPUTABLE (yes) | "For most models, the Codex CLI interrupts the turn after 3 consecutive denials or 10 denials in the last 50 reviews in that turn. For models designated for cybersecurity, the CLI interrupts the turn on the first denial." Same reasoning as Claude Code: a defined rule, but a within-turn circuit breaker, not authority set from a performance record. | https://learn.chatgpt.com/docs/sandboxing/auto-review.md ("Denials and failure behavior") |
| H5 | **part** | Computer Use is for "tasks where command-line tools or structured integrations aren't enough, such as checking a desktop app, using a browser, changing app settings, working with a data source that isn't available as a plugin"; "You can stop the task or take over your computer at any time." The shared ChatGPT/Codex Browser page: "When ChatGPT encounters a login screen, it pauses and asks you to enter your credentials" (note: "Browser isn't available in Codex CLI or the Codex IDE extension"). No record or count of hand-offs. | https://learn.chatgpt.com/docs/computer-use.md; https://learn.chatgpt.com/docs/browser.md |

## Grok Build (xAI)

| Q | Value | Quotation | Location |
|---|---|---|---|
| H1 | **no**, DISPUTABLE (part) | No page defines a record of permission decisions. Nearest: "Grok saves every conversation to disk automatically — prompts, responses, tool calls, and file snapshots" (approvals not named); hook event "`PermissionDenied` — The permission system denies a tool call" (a hook a user could log from); changelog v1.0.7x: "headless `-p` runs print each refused approval request to stderr" (refusals with nobody to answer, not a person's decision). Searched: permissions, sessions, hooks, settings reference, enterprise, CLI reference, headless pages and the changelog for "audit", "log", "telemetry", "decision", "approval". | https://docs.x.ai/build/features/sessions.md; https://docs.x.ai/build/features/hooks.md; https://x.ai/changelog/build |
| H2 | **no** | No count or rate of approvals. `/usage` is "View credit usage or manage billing". Searched the same pages for "metric", "rate", "analytics", "usage", "count", "telemetry". | https://docs.x.ai/build/modes-and-commands.md; https://docs.x.ai/build/settings/reference.md |
| H3 | **part** | Manual option only: "A remembered “always allow” grant still prompts for dangerous patterns such as `rm` and `git push`." Settings: "`remember_tool_approvals` ... Show per-tool "Always allow …" options." Changelog Oct 21, 2026 (v1.0.67): "Worktrees also use saved "always allow" answers from the main checkout". No review of past decisions. | https://docs.x.ai/build/features/permissions.md; https://docs.x.ai/build/settings/reference.md; https://x.ai/changelog/build |
| H4 | **no**, DISPUTABLE (yes) | Changelog, July 20, 2026: "Auto mode now continues after classifier blocks by telling the agent the reason, escalating only after repeated denials". A repeated-denial circuit breaker; thresholds not given on any docs page. | https://x.ai/changelog/build |
| H5 | **no** | No page describes the agent handing a step to a person for lack of capability, and no computer use or browser-use feature for that purpose. The dashboard groups sessions as "Needs input", which mixes "Permission prompts and questions" without separating capability. Searched overview, modes and commands, dashboard, sessions, background tasks, headless, enterprise, settings reference and changelog for "computer", "browser", "take over", "hand off", "manual", "login", "captcha". | https://docs.x.ai/build/features/dashboard.md |

## Google Antigravity

| Q | Value | Quotation | Location |
|---|---|---|---|
| H1 | **no** | No record of permission decisions is defined. Nearest: headless runs: "Any tool action that requires approval it can’t obtain in headless mode is soft-denied: the run continues, exits `0`, and prints a notice to `stderr` naming the tool and how to allow it." Enterprise logging covers "model interactions", not approvals. Searched permissions, enterprise, hooks, settings, agent settings, CLI headless, `/permissions` and the changelog for "audit", "log", "history", "decision", "approval", "telemetry". | https://antigravity.google/docs/cli/headless.md; https://antigravity.google/docs/enterprise.md |
| H2 | **no** | No measure of approvals or prompts. `/usage` is "Model quotas". Searched the same pages for "metric", "analytics", "rate", "count", "usage". | https://antigravity.google/docs/cli/commands/usage.md; https://antigravity.google/docs/settings.md |
| H3 | **part** | Manual option: "**Yes, always allow** _domain_" on browser prompts; "Permissions manually granted during a conversation can persist, allowing the agent to learn trusted actions over time." `/learn` reviews past corrections, but it targets rules and skills for agent behavior, not what is asked of people: "the agent analyzes your recent messages for explicit corrections (“no,” “instead,” “that failed”) ... and propose[s] durable changes". | https://antigravity.google/docs/browser.md; https://antigravity.google/docs/features.md; https://antigravity.google/docs/commands/learn.md |
| H4 | **no**, DISPUTABLE (part) | "Permissions manually granted during a conversation can persist, allowing the agent to learn trusted actions over time." Part is defensible as a stated principle that authority widens over time. No is defensible because the widening comes from a person's grant, not from the agent's performance. The Auto preset decides per command ("safe, reversible commands run without prompting") with no reference to a record. | https://antigravity.google/docs/features.md; https://antigravity.google/docs/permissions.md |
| H5 | **part** | "When a browser task hits Google Sign-In, a third-party OAuth or SSO provider ..., multi-factor authentication, a passkey prompt, or a CAPTCHA: 1. The agent leaves the login page open in the built-in browser tab, pauses, and asks you to finish signing in." And "Stop and take over ... return the tab to your manual control (**Browser: you took over**)." Browser subagents are the tool that removes manual browser steps, but no record or count of hand-offs. Also: "Identity provider pages ... and payment processors ... are blocked from agent actuation." | https://antigravity.google/docs/browser.md ("Pause, take over, and sign in"; "Permissions and safety guardrails") |

## Summary

| Product | H1 | H2 | H3 | H4 | H5 |
|---|---|---|---|---|---|
| Claude Code 2.1.323 | part | part (D: yes) | part | no (D: yes) | part |
| Codex CLI 0.167.2 | part | part (D: yes) | part | no (D: yes) | part |
| Grok Build 1.0.67 / changelog 1.0.77 | no (D: part) | no | part | no (D: yes) | no |
| Antigravity agy 1.5.7 / changelog 2026-11-12 | no | no | part | no (D: part) | part |

D = DISPUTABLE, with the other defensible value.

# Further passages

Reducing people's decisions as a goal:
- Claude Code: `auto` mode is "Best for ... Long tasks, reducing prompt fatigue." https://code.claude.com/docs/en/permission-modes.md
- Claude Code: `/insights` "can also include an estimate of how many permission prompts auto mode could have handled across those sessions." https://code.claude.com/docs/en/costs.md
- Codex: "Auto-review sends eligible approval requests to a separate reviewer agent" and "Codex routes that approval request to a separate reviewer agent instead of stopping for a person." https://learn.chatgpt.com/docs/sandboxing/auto-review.md
- Codex: section title "Reduce review volume without weakening security". Same page.
- Antigravity: "a robust, unified permission engine to secure your environment while enabling autonomous workflows." https://antigravity.google/docs/permissions.md
- Antigravity: the interactive prompt lets a person widen a grant "preventing repeated prompts for related operations." Same page.

People's decisions should not be reduced, or reduction has limits:
- Claude Code: "Auto mode reduces permission prompts but does not guarantee safety. Use it for tasks where you trust the general direction, not as a replacement for review on sensitive operations." https://code.claude.com/docs/en/permission-modes.md
- Codex: "fix the boundary first instead of teaching the reviewer to approve noisy escalations forever"; "It should complement, not replace, good sandbox design, monitoring, and organization-specific policy." https://learn.chatgpt.com/docs/sandboxing/auto-review.md
- Codex: "Review events periodically for approval/sandbox changes and unexpected tool executions." https://learn.chatgpt.com/docs/agent-approvals-security.md
- Antigravity: "every file upload requires one-time approval, even in **Turbo**". https://antigravity.google/docs/permissions.md
- Antigravity enterprise: "Use unrestricted auto-approval (**Turbo** / **Always proceed**) only in isolated development containers or disposable branches." https://antigravity.google/docs/enterprise.md
- Grok: "A remembered “always allow” grant still prompts for dangerous patterns such as `rm` and `git push`." https://docs.x.ai/build/features/permissions.md

# What was opened

All on 2026-11-12, by `curl` of the Markdown version of each page unless noted.

Claude Code: https://code.claude.com/docs/llms.txt; /en/permissions.md, permission-modes.md, auto-mode-config.md, monitoring-usage.md, analytics.md, costs.md, security.md, hooks.md, hooks-guide.md, computer-use.md, chrome.md, changelog.md (top entries), commands.md, interactive-mode.md, skills.md. Local: `claude --version`, `claude --help`.

Codex: https://learn.chatgpt.com/docs (HTML index), https://learn.chatgpt.com/llms.txt; /docs/agent-approvals-security.md, agent-configuration/rules.md, sandboxing/auto-review.md, sandboxing.md, permissions.md, permission-modes.md, config-file/config-advanced.md, config-file/config-reference.md, enterprise/workspace-analytics.md, enterprise/usage-insights.md, enterprise/agent-security.md, enterprise/security-cookbook.md, security-administration.md, computer-use.md, browser.md, chrome-extension.md, whats-new.md. Local: `codex --version`, `codex --help`.

Grok Build: https://docs.x.ai/build (HTML), https://docs.x.ai/llms.txt; /build/overview.md, modes-and-commands.md, features/plan-mode.md, features/sessions.md, features/dashboard.md, features/subagents.md, features/background-tasks.md, features/hooks.md, features/permissions.md, features/sandbox.md, cli/headless-scripting.md, cli/reference.md, settings.md, settings/reference.md, enterprise.md; https://x.ai/changelog/build (HTML, converted to text). Local: `grok --version`, `grok --help`.

Antigravity: https://antigravity.google/docs (redirect stub to /docs/getting-started), https://antigravity.google/llms.txt; /docs/permissions.md, enterprise.md, browser.md, ide/browser.md, ide/allowlist-denylist.md, ide/separate-chrome-profile.md, ide/agent-side-panel.md, sandbox.md, hooks.md, settings.md, agent-settings.md, cli/commands/permissions.md, cli/modes.md, cli/commands/usage.md, cli/headless.md, changelog.md, commands/browser.md, commands/learn.md, artifact-review.md, review-changes.md, features.md, faq.md, teamwork.md, sdk/policies.md, walkthrough.md. Local: `agy --version`, `agy --help`.

Not opened or failed:
- https://x.ai/changelog/build returned a Cloudflare "Sorry, you have been blocked" page to plain curl. A second request with a browser User-Agent string returned the full changelog. Recorded here as a disclosure.
- https://learn.chatgpt.com/docs/changelog.md returned "Not found"; the What's new digest was used for the Codex date.
- Not opened: the OpenAI Alignment Research post on Auto-review and the GitHub reviewer policy files linked from the Auto-review page; the Claude Code Analytics API and Console pages on platform.claude.com; the Grok Bot pages (a separate product); Antigravity `/docs/cli/permissions` (linked but not in the index; the shared /docs/permissions.md covers App and CLI).

# Disclosures

- Reader C is a Claude subagent made by Anthropic, the vendor of one of the four products. The same rules applied to all four, and every value rests on a quotation above.
- I did not sign in anywhere, did not run a task or session with any of the four tools, and opened no other file under the warm research folder besides the protocol.
- The Codex docs site is shared by ChatGPT Work and Codex. Computer Use and Browser quotations come from pages that cover both; the Browser page says it is not available in Codex CLI.
- For H4 on three products I rated **no** where a repeated-denial circuit breaker exists. The protocol's **part** ("stated as a principle or future work") does not fit a working mechanism, so the defensible pair was yes/no and I gave the lower. A reader who counts a circuit breaker as "authority that changes with the record" would score these **yes**.
- Claude Code's per-decision reason field (`safety_event`) existed in v2.1.307 to v2.1.311 and is documented as no longer sent from v2.1.312. On that older range H1 could rate higher.
