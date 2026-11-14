---
title: "Grok Build mapped to the 25 WARM platform services (protocol version 2)"
date: 2026-11-12
author: reader subagent (Claude, spawned for this product only)
product: "Grok Build (xAI / SpaceXSI): the grok CLI and TUI, headless mode, ACP agent mode, and the web and mobile surface the vendor names Grok Build"
product_version: "newest changelog entry v1.0.77, November 5, 2026 (x.ai/changelog/build); installed binary on this machine: grok 1.0.67 (2fe064390d07) [stable]"
status: "not yet checked by sagan"
---

# Reading notes

- Every page was opened on 2026-11-12. Values rest on the current documentation (docs.x.ai/build), the changelog, the product page, the vendor's news posts, the installed CLI's help output, and the user guide in the vendor's public repository.
- The public repository (`xai-org/grok-build`) was last synced from the vendor's monorepo on 2026-09-29, so its user guide is about six weeks older than the newest release. Where a cell uses it, the row says "repo guide, synced 2026-09-29".
- Short names for URLs in the table: **docs/** = `https://docs.x.ai/build/`; **changelog** = `https://x.ai/changelog/build`; **repo guide/** = `https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/`; **CLI help** = `grok --help` and subcommand help, run locally with stdin closed.

# The 25 services

| Group | Service | Value | Quote | URL | Availability and reason |
|---|---|---|---|---|---|
| Runtime | Harness | **yes** | "The agent loop: how context is assembled, how model responses are parsed, and how tool calls are dispatched" | https://x.ai/news/grok-build-open-source | Generally available (stable channel, v1.0.x). |
| Runtime | Sessions | **yes** | "Grok saves every conversation to disk automatically — prompts, responses, tool calls, and file snapshots — under `~/.grok/sessions/`, keyed by working directory." | docs/features/sessions | Generally available. Resume (`--resume`, `-c`), fork (`/fork`), rewind, export, `grok sessions list/search/delete`. |
| Runtime | Tasks | **part** DISPUTABLE (yes) | "`/goal` gives Grok an objective and lets it work toward it across many rounds, without you prompting each step." Also: "Items use statuses pending, in progress, completed, and cancelled (when a step is dropped)." | docs/modes-and-commands; docs/features/sessions | Generally available. A goal, the todo list, the tasks pane and workflow runs each track work inside one session, with pause, resume and stop. No single task record that coordinates retry and recovery is described. Yes is defensible: `/goal` keeps the objective, shows status, pauses, resumes and clears, and reviewers check completion; "Workflow runs that failed can now be resumed" (changelog 0.2.112). |
| Runtime | Environments | **yes** | "A worktree session runs in an isolated copy of your repository, so parallel agents cannot overwrite each other's files." Also: "The sandbox limits what the agent process and its children can read, write, and reach on the network (Landlock on Linux, Seatbelt on macOS). Off by default." | docs/features/worktrees; docs/features/sandbox | Generally available; sandbox off by default. No built-in browser found (Chrome DevTools is a marketplace plugin). |
| Runtime | Scheduling | **part** DISPUTABLE (yes) | "The interval accepts `Ns` (minimum 60), `Nm`, `Nh`, and `Nd`. The prompt fires immediately, then repeats; each firing is a new agent turn. Loops expire after 7 days, and at most 50 scheduled tasks can be active at once." | docs/features/background-tasks | Generally available. Intervals (`/loop`), event streams (monitors) and caps exist, inside a running Grok process. No start at a clock time, and nothing that starts work when Grok is not running, was found. Yes is defensible because all three parts of the definition (time, event, limits) have a feature. |
| Runtime | Lifecycle | **yes** | "The dashboard is a fullscreen overview of every session: which agents need input, which are working, and which are done." Also: "The input bar at the bottom dispatches prompts to new sessions." and the key "Stop / close agent (press twice)". | docs/features/dashboard | Generally available. Agents here are sessions; resume is `grok --resume`; `grok leader list/kill` for the shared process (CLI help). |
| Knowledge | Memory | **part** DISPUTABLE (yes) | "After a turn completes, Grok reviews it in the background and records anything durable: conventions, decisions, and project facts." Also: "Memory is now generally available" (changelog 1.0.34, September 16, 2026). | https://x.ai/news/grok-build-memory; changelog | Generally available per the changelog; the settings reference still lists `[memory]` `enabled` as "default off" and the CLI reference lists `--experimental-memory`. Retains facts across sessions and consolidates them (`/dream`). Where each entry came from is not described as a recorded property. Yes is defensible: session logs carry the session ID and date, and old session results get a staleness note (repo guide/13-memory.md, synced 2026-09-29). |
| Knowledge | Retrieval | **yes** | "Code search" — "Grep and navigate large codebases fast"; "Web search" — "Look up docs and packages from the terminal"; "MCP servers" — "Connect to Linear, Sentry, Grafana, and more" | https://x.ai/build | Generally available. `web_fetch` is off by default (docs/settings/reference). |
| Knowledge | Artifacts | **part** | "`/rewind` (or `Esc Esc` while idle) lists a rewind point per prompt. Selecting one restores all files to their state at that point and truncates the conversation to match." Web and mobile: "Every app you publish gets its own address on grok.me, and you decide who can open it" | docs/features/sessions; https://x.ai/news/grok-build-for-everyone | Output is files in the user's repository, or a published app on the web surface. No store of outputs with their versions is described; rewind points are per-session file snapshots. |
| Capabilities | Models | **yes** | "Custom / BYOK models (OpenAI-compatible or Anthropic Messages)." Also the `[subagents.models]` row: "map of subagent → model id" — "Per-subagent model routing." | docs/settings/reference | Generally available. Inference goes through the vendor's proxy or a configured endpoint. |
| Capabilities | Tools | **yes** | "Once configured, their tools are available alongside the built-in ones, namespaced as `<server>__<tool>`." Also: "Permissions decide which tool calls may run." | docs/features/mcp-servers; docs/features/permissions | Generally available. |
| Capabilities | Registry | **yes** | "A plugin bundles skills, slash commands, agents, hooks, MCP servers, and LSPs into one installable package." Also: "Every remote plugin in the catalog is pinned to a specific commit SHA, and Grok Build verifies the pin at install time." Skills: "Auto-invoked when a task matches, or called by name". | https://x.ai/news/grok-plugin-marketplace; https://x.ai/build | Generally available. Versions attach to plugins (`grok plugin update`, `grok plugin tag`: "Create a release git tag from the plugin's manifest version", CLI help); loose skill and agent files carry no version. |
| Interaction | Directory | **part** (derived) | derived from C3 = part and C4 = part | see question 1 | derived |
| Interaction | Messaging | **part** DISPUTABLE (yes) | "Subagents are independent child sessions with their own context. They return a summary to the parent when finished." Also: "Messages between subagents appear as left-aligned rows under the bullet that name the sender and recipient" (changelog 1.0.74). Events: "A hook is a shell command or HTTP endpoint that Grok calls when a lifecycle event occurs". | docs/features/subagents; changelog; docs/features/hooks | Messages travel only inside one session's tree; "The `send_subagent_message` tool is off by default." (repo guide/16-subagents.md, synced 2026-09-29). No delivery between top-level sessions was found; a person relays through the dashboard. Yes is defensible because both halves exist: agent-to-agent messages and events delivered to hook endpoints. |
| Interaction | Orchestration | **yes** | "Workflows orchestrate a bounded set of subagents in the background: fan out work, verify, then return a result. They are on by default." | docs/modes-and-commands | Generally available (on by default since 0.2.111, July 22, 2026). Plan approval and question cards bring people in. |
| Interaction | Channels | **yes** | "Use it via an interactive TUI, headlessly in scripts or bots, or through the Agent Client Protocol (ACP) in other apps." | docs/overview | Generally available: terminal, headless JSON, ACP (editors), a WebSocket server (`grok agent serve`, CLI help), and web, iOS and Android for the build surface. Searched docs and changelog for Slack, Telegram, Discord, email: none found. |
| Governance | Identity | **part** | "Grok Build supports four session authentication methods" Also: "The token's team principal must match the configured value, so a personal login or a login to the wrong team is rejected" | docs/enterprise | Generally available. Establishes the signed-in person and team. Agents and subagents have no identity of their own, and no record of the person accountable for an agent was found (searched "identity", "principal", "revoke", "on behalf"). Ending an identity is `grok logout` or a login policy that clears the session. |
| Governance | Secrets | **part** | "Grok expands `${VAR}` (and `${VAR:-default}`) in `url`, `command`, `args`, `env`, and `headers`, so secrets can stay in the environment." Also: "Built-ins do not permanently protect paths such as `~/.ssh`; use a custom `deny` list" | docs/features/mcp-servers; docs/features/sandbox | Mechanisms only: environment expansion and sandbox deny globs (for example `**/.env`). No store that withholds a value from the agent and releases it at the point of use was found. The web surface's "Secrets. Store API keys for third-party services outside your app's code." is for the apps it builds. |
| Governance | Policy | **yes** | "Values pinned in `requirements.toml` use a fail-closed "pin" mechanism: they cannot be overridden by user `config.toml`, environment variables, remote settings, or lower-priority layers." Also: "`deny` always wins over `allow`." and "ZDR is enforced at the team level." | docs/enterprise; docs/features/permissions | Generally available. Rules on actions (allow, deny, ask), on content paths (sandbox, `web_fetch` domain allowlist, MCP allowlists) and on retention (zero data retention). |
| Governance | Approvals | **yes** | "A remembered “always allow” grant still prompts for dangerous patterns such as `rm` and `git push`. An explicit config or CLI allow rule auto-approves them." Also: "Only the session plan file may be edited until you approve." | docs/features/permissions; docs/features/plan-mode | Generally available. Single held actions (permission prompt, plan review, answerable from the dashboard) and advance approval for a class (`Bash(git *)` rules, remembered grants). Remembered grants are kept per project in a `permission.toml` (repo guide/22-permissions-and-safety.md, synced 2026-09-29). |
| Operations | Observability | **yes** | "Grok can now export usage metrics and events to your own OpenTelemetry collector when enabled" (changelog 0.2.52). Also `grok trace`: "Export or upload session trace data"; `grok usage`: "Print persisted token and cost usage for a session". | changelog; CLI help | Session records and usage are generally available; the external OpenTelemetry stream is marked "Status: alpha." and off by default (repo guide/24-monitoring-usage.md, synced 2026-09-29). |
| Operations | Evaluation | **part** | "When the goal looks done, a panel of reviewer subagents checks the work against the evidence. The goal is marked complete only when most of them agree." | docs/modes-and-commands | Generally available. Checks one goal against its stated end state; workflows can add verification steps. No result of "unknown" when a check cannot run, and no evaluation suite, was found (searched "eval", "unknown", "grader", "criteria"). |
| Operations | Improvement | **part** | "Capture any session as a new skill with /skillify" Also: "Grok authors the workflow from your request, smoke-checks it before launching, and improves it between runs" | https://x.ai/build; https://x.ai/news/workflows | A session can become a skill or memory notes. No described path from traces, evaluations or reviews to proposed changes to agents or the platform. `/skillify` appears on the product page only; it is not in the docs command table or the changelog. |
| Operations | Releases | **part** | "`grok update`" — "Check for updates or install a specific version (`--check`, `--version <V>`, `--alpha`, `--stable`)" Also: "Every remote plugin in the catalog is pinned to a specific commit SHA" | docs/cli/reference; https://x.ai/news/grok-plugin-marketplace | Versions, channels and a way back exist for the CLI itself and for plugins. Agent definitions, skills and rules are plain files; no release or rollback mechanism of the product's own was found for them. |
| Operations | Reliability | **part** | "`max_retries` / `inference_idle_timeout_secs`" — "Reliability." Also: "Sessions interrupted by a crash show a clear marker instead of silently dropping the turn" (changelog 1.0.41) and "A stalled model call during a turn retries before the turn fails" (changelog 1.0.50). | docs/settings/reference; changelog | Retries and resumable state. Nothing that supervises a running agent or restarts it after a failure was found (searched "restart", "recover", "watchdog", "supervis"). |

# Four further questions

## 1. Areas of work (C1 to C4 of rerate-criteria-v2)

| Criterion | Value | Quote | Location | Reason |
|---|---|---|---|---|
| C1. An area of work exists in the model | **part** DISPUTABLE (yes) | "Project rules are Markdown files that Grok loads into context for every session in a directory tree." Also: "A nested `AGENTS.md` scopes to its subtree, so a monorepo can carry different conventions per package" | docs/features/project-rules | The product has grouping units: the project (a directory scope with rules, `.grok/agents/`, `.grok/config.toml` and workspace memory), the team (a login principal) and the plugin (an installable bundle). None is defined as an area of work or an organizational unit that agents or roles belong to. Yes is defensible: the project scope has stated properties, holds several agent definitions, and several projects or subtrees sit side by side. |
| C2. The area is specified apart from who does the work | **part** | "Project configs are limited to MCP servers, plugins, and permission rules, not full user configs." Also: "Add or override types under `.grok/agents/` or `~/.grok/agents/`." | docs/settings; docs/features/subagents | Rated on the project scope. Some properties sit at the level of the unit (rules, tools, permission rules, agent types; roles in `.grok/roles/*.toml` per repo guide/16-subagents.md, synced 2026-09-29). Nothing states what the unit as a whole is responsible for: `AGENTS.md` is free text for "coding conventions, build and test commands, and architecture notes". |
| C3. A record of accountability | **part** | "`grok inspect [--json]`" — "Show the configuration Grok discovers for this directory: rules, skills, plugins, hooks, and MCP servers" Also, skill frontmatter `metadata`: "String map. `author` and `short-description` are shown in the UI." | docs/cli/reference; docs/features/skills-plugins-marketplaces | A kept record names a source or author per skill, plugin and server ("the Skills section lists each skill's name and its source", repo guide/08-skills.md, synced 2026-09-29). Accountability is not stated, and the record is per asset, not per responsibility. |
| C4. Finding where to send work | **part** | "Workflows appear alongside skills in the model prompt so the agent can launch them by name" (changelog 1.0.9). Also, skill field `description`: "What it does and when to use it." | changelog; docs/features/skills-plugins-marketplaces | The top-level session picks a subagent type, skill or workflow from the list in its own prompt ("`spawn_subagent` has an optional `subagent_type` enum when plugin, project, or user agents exist" and "Only the top-level session spawns subagents.", repo guide/16-subagents.md, synced 2026-09-29). Routing lives inside one orchestrating session; no lookup that any agent may ask was found. |

Directory (derived) = **part** (C3 part, C4 part).

## 2. Supplied agents for an area of work

All supplied agents and skills found are for software development, research or document and media production. None is for a named business area such as finance or communications.

- Built-in subagent types `general-purpose` ("Default full-capability child"), `explore` ("Read, list, and search only (no shell, no edits)"), `plan` ("Drafts an implementation plan (no shell, no edits)"). https://docs.x.ai/build/features/subagents
- Built-in research workflow: "`/deep-research <query>` starts a built-in research workflow." https://docs.x.ai/build/modes-and-commands ; "it fans research questions out to parallel investigators, verifies every claim against its sources, and returns a cited report." https://x.ai/news/workflows
- Code review: "Code review" — "Line-by-line feedback before opening a PR". https://x.ai/build
- Partner plugins in the built-in marketplace: "MongoDB — Explore data, manage collections, and optimize queries.", "Vercel — Manage deployments, check build status, and configure domains.", "Sentry — Analyze stack traces and debug production errors.", "Chrome DevTools — Control a live browser, record performance traces, and inspect network requests.", "Cloudflare — Skills for Workers, Durable Objects, and more.", "Superpowers — Popular agent-driven workflows." https://x.ai/news/grok-plugin-marketplace
- Bundled skills, agents and workflows exist: "Built-in skills, agents and workflows are refreshed when their local cache's manifest is missing or corrupt" (changelog 1.0.74). Their names are not listed on the vendor pages opened. See the disclosure below for a local listing.
- Bundled personas exist ("bundled personas are read-only", repo guide/16-subagents.md, synced 2026-09-29); the pages give `researcher` and `concise` as examples and do not list the bundled set.

## 3. What fits nowhere

- **Spend accounting and token budgets.** "`/goal <objective>`" — "Start a goal. Add `--budget <tokens>` to cap the tokens it may spend." https://docs.x.ai/build/modes-and-commands ; "`/usage`" — "View credit usage or manage billing" (same page); `grok usage`: "Print persisted token and cost usage for a session" (CLI help). Scheduling covers how much may run at once, not what it may cost.
- **Hosting and publishing what the agent builds (web and mobile surface).** "Every app you publish gets its own address on grok.me, and you decide who can open it: just you, anyone with the link, or the whole internet. Bring your own domain if you'd rather." Also "Remix. Let others fork a published app and make it their own." https://x.ai/news/grok-build-for-everyone
- **Reading other vendors' harness configuration and sessions.** "Grok automatically reads Claude Code marketplaces, plugins, skills, MCPs, agents, hooks, and instruction files (`CLAUDE.md`, `Claude.md`, `CLAUDE.local.md`, and `.claude/rules/`) alongside `.grok/`." https://docs.x.ai/build/features/skills-plugins-marketplaces ; "`grok import [targets...]`" — "Import sessions from Claude Code" https://docs.x.ai/build/cli/reference
- **Offering the machine to another product's agents.** `grok worker`: "Run this machine as a Cursor private worker" (CLI help). Not documented on the docs pages opened; it may belong under Environments.

## 4. Where it runs and what the user supplies

- **Where the agent runs.** On the user's machine: "**Tool execution** — happens locally in the user's sandboxed environment." and "Local session history is stored in `~/.grok/`." (https://docs.x.ai/build/enterprise). Model calls go to the vendor: "**Transport** — sent over TLS 1.2/1.3 to the inference proxy." (same page), or to the user's own endpoint: "Grok Build can now run fully local-first: compile it yourself, point it at your own local inference, and drive everything from your config.toml." (https://x.ai/news/grok-build-open-source). The web and mobile surface runs in the vendor's service: "Describe an app, a game, a website, or a dashboard in Grok, and Grok builds a working version live in your chat — on the web, on iOS, and on Android." (https://x.ai/news/grok-build-for-everyone). So: both, with the CLI harness on the user's machine.
- **Whether an agent keeps running when the user is away.** Only while the Grok process runs on the user's machine. "Closing the dashboard leaves every session running, and they're all there when you reopen it." (https://x.ai/news/agent-dashboard). "`/goal` gives Grok an objective and lets it work toward it across many rounds, without you prompting each step." (docs/modes-and-commands). "Loops expire after 7 days" (docs/features/background-tasks). Quitting ends the work: "Quitting warns when it would stop a running workflow and asks you to confirm with a second quit" (changelog 1.0.53). A shared leader process can outlive its clients: `--no-exit-on-disconnect` "Keep the leader running after the last client disconnects" (CLI help for `grok agent leader`). For always-on agents the docs point to a different product: "[Grok Bot](/grok-bot/overview) — AI teammates on a cloud computer" (docs/overview).
- **What a user must supply or build for sustained work.** A machine that stays on, an account or API key ("On first launch, Grok opens a browser for authentication. In non-browser environments, use an API key", docs/overview), and a repository. The user writes the rules, skills, agent definitions, hooks and permission rules ("Put coding conventions, build and test commands, and architecture notes in an `AGENTS.md` at your repo root", docs/features/project-rules). Memory and the sandbox are off by default and must be enabled. Anything that starts work without a running session is the user's to build on headless mode ("Headless usage is ideal for scripts, automations, or integration into other apps.", docs/overview), and channels beyond the terminal are the user's to build on ACP ("Grok Build also provides full ACP support to build your own bots and agent orchestration apps.", https://x.ai/news/grok-build-cli).

# Pages opened (all on 2026-11-12)

Current documentation, fetched as markdown with curl:
- https://docs.x.ai/llms.txt (index)
- https://docs.x.ai/build/overview
- https://docs.x.ai/build/modes-and-commands
- https://docs.x.ai/build/features/plan-mode
- https://docs.x.ai/build/features/sessions
- https://docs.x.ai/build/features/background-tasks
- https://docs.x.ai/build/features/dashboard
- https://docs.x.ai/build/features/subagents
- https://docs.x.ai/build/features/worktrees
- https://docs.x.ai/build/cli/headless-scripting
- https://docs.x.ai/build/features/project-rules
- https://docs.x.ai/build/features/skills-plugins-marketplaces
- https://docs.x.ai/build/features/mcp-servers
- https://docs.x.ai/build/features/hooks
- https://docs.x.ai/build/features/permissions
- https://docs.x.ai/build/features/sandbox
- https://docs.x.ai/build/features/status-line
- https://docs.x.ai/build/settings
- https://docs.x.ai/build/settings/reference
- https://docs.x.ai/build/settings/zdr-video-storage
- https://docs.x.ai/build/cli/reference
- https://docs.x.ai/build/cli/terminal-support
- https://docs.x.ai/build/enterprise
- https://docs.x.ai/build/keyboard-shortcuts and https://docs.x.ai/build/features/theming (fetched; searched for keywords, not read in full)

Changelog, product page and news:
- https://x.ai/changelog/build (reached from https://x.ai/build/changelog; 186 releases, v0.1.209 of May 17, 2026 to v1.0.77 of November 5, 2026; newest entries read, the rest searched by keyword)
- https://x.ai/build (also served for https://x.ai/cli)
- https://x.ai/news (index)
- https://x.ai/news/grok-build-cli (May 25, 2026)
- https://x.ai/news/grok-plugin-marketplace (June 11, 2026)
- https://x.ai/news/agent-dashboard (June 15, 2026)
- https://x.ai/news/introducing-goal (June 22, 2026)
- https://x.ai/news/grok-build-open-source (July 15, 2026)
- https://x.ai/news/workflows (July 23, 2026)
- https://x.ai/news/grok-build-mode (July 28, 2026)
- https://x.ai/news/grok-build-for-everyone (August 19, 2026)
- https://x.ai/news/grok-build-memory (September 16, 2026)

Public repository (last sync commit 2026-09-29):
- https://github.com/xai-org/grok-build (metadata, README, commit list, `SOURCE_REV`; no releases or tags)
- User guide chapters read in full: `13-memory.md`, `15-agent-mode.md`, `16-subagents.md`, `24-monitoring-usage.md`
- User guide chapters read in part or searched: `08-skills.md`, `09-plugins.md`, `14-headless-mode.md`, `17-sessions.md`, `20-background-tasks.md`, `22-permissions-and-safety.md`, `23-dashboard.md`; downloaded and searched by keyword only: `01`, `02`, `04`, `05`, `07`, `10`, `11`, `18`, `26`, `README.md`

Installed CLI (grok 1.0.67, stdin closed): `grok --version`, `grok --help`, and `--help` for `agent`, `agent headless`, `agent serve`, `agent leader`, `memory`, `memory clear`, `sessions`, `sessions search`, `trace`, `worker`, `worker start`, `leader`, `leader info`, `dashboard`, `setup`, `usage`, `clone`, `export`, `inspect`, `plugin`, `mcp`, `update`.

# Disclosures and what could not be opened

- No file under `` was opened other than `protocol-v2.md` and `rerate-criteria-v2.md`. No search printed content from another one.
- The installed binary (1.0.67) is ten releases behind the newest changelog entry (1.0.77). Help output reflects 1.0.67.
- Beyond help output, I listed the directory names under `~/.grok/bundled/` on this machine (no file was opened, nothing was changed). It shows bundled skills `build-with-ai`, `code-review`, `create-skill`, `create-workflow`, `design`, `docx`, `execute-plan`, `game-animation-frames`, `game-asset-core`, `game-assets`, `game-character-consistency`, `game-tilesets`, `game-ui-icons`, `imagine`, `implement`, `learn`, `long-running-background-tasks`, `pdf`, `pptx`, `pr-babysit`, `resume-claude`, `resume-codex`, `resume-cursor`, `review`, `skill-design-principles`, `statusline`, `threejs-frame-conventions`; agents `explore`, `general-purpose`, `plan`; workflows `deep-research`, `learn-traces`. No cell value rests on this listing. The `learn` skill and `learn-traces` workflow may bear on the Improvement row; no vendor page opened describes them.
- No agent session was started, no prompt was sent to the product, and no configuration was changed. `grok models` and `grok inspect` were not run.
- Could not open: `https://x.ai/build/changelog` with an `Accept: text/markdown` header (HTTP 403 from Cloudflare; the HTML page opened normally). Not attempted because they need a login: grok.com, code.grok.com. Not opened: `github.com/xai-org/plugin-marketplace`, the Grok Bot documentation (a separate product in this study), repo guide chapters `03`, `06`, `12`, `19`, `21`, `25`, `27`.
- Two inconsistencies between vendor pages, recorded and not resolved: (1) docs/modes-and-commands lists "`/share`" — "Share the current session via URL", while changelog 1.0.51 (October 9, 2026) says "The /share command and session sharing are removed from the CLI". (2) The changelog says "Memory is now generally available" (1.0.34), while docs/settings/reference lists `[memory]` `enabled` as "default off" and docs/cli/reference lists "`--experimental-memory`" — "Enable cross-session memory".
- Whether the web and mobile surface ("Grok Build on web and mobile", first called Build Mode) runs the same harness as the CLI is not stated on the pages opened. Cells that cite it say so; no cell's value depends on it.
- No secondary source was used for any cell. One web search was run to locate the documentation; its third-party results were not used.
