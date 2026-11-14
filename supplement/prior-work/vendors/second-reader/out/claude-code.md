Claude Code **2.1.322**; newest changelog entry seen: **November 10, 2026**. Sources read **November 12, 2026**. [Changelog](https://code.claude.com/docs/en/changelog.md)

| Service | Value | Quote | URL | Availability and reason |
|---|---|---|---|---|
| Harness | **yes** | “Claude Code is the layer around the model that provides the tools and manages the context the model sees.” | [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works#the-agentic-loop) | Generally available. Runs the model/tool loop and manages context across its surfaces. |
| Scheduling | **yes** | “run in the cloud on a schedule, on API calls, or on GitHub events.”; “limit on cloud sessions running at once.” | [Scheduled tasks](https://code.claude.com/docs/en/routines) | Research preview on paid subscription plans. Supplies time and event triggers and enforces simultaneous-session limits. |
| Lifecycle | **yes** | “List of running background sessions, used to reconnect after a restart”; “A session that has a saved conversation resumes it” | [Agent view](https://code.claude.com/docs/en/agent-view.md#manage-sessions-from-the-shell) | Research preview. Creates and lists background agents, stops them while retaining state, resumes them, and removes their entries. |
| Retrieval | **yes** | “Resources are automatically fetched and included as attachments when referenced” | [MCP resources](https://code.claude.com/docs/en/mcp#reference-mcp-resources), [built-in readers](https://code.claude.com/docs/en/tools-reference.md) | Generally available. Built-in file reading and MCP resource fetching retrieve named material; external sources require a connected server. |
| Registry | **yes** | “skills, agents, hooks, MCP servers, or other components that Claude Code installs and loads as one unit.”; “One directory per installed version of a marketplace plugin.” | [Plugins](https://code.claude.com/docs/en/plugins/overview.md), [versioned storage](https://code.claude.com/docs/en/plugins/loading.md#where-installed-plugins-live) | Generally available. Catalogs locate packages; versioned installations hold agent, skill, and tool-server definitions, with skill/agent content loaded when used. |
| Identity | **part** | “The creating user’s identity is in the `act` claim.”; “Anthropic doesn’t publish a revocation feed for session tokens.” | [Session identity](https://code.claude.com/docs/en/self-hosted-environments-identity) | Authentication is generally available; self-hosted session identity is public beta on Team/Enterprise. Creator attribution exists, but accountable-person records for every agent and session-token revocation are not established. |
| Approvals | **yes** | “Claude Code saves the rule to `.claude/settings.local.json`”; “Logged when a tool permission decision is made (accept/reject).” | [Permissions](https://code.claude.com/docs/en/permissions.md#permission-system), [decision records](https://code.claude.com/docs/en/monitoring-usage.md#tool-decision-event) | Generally available. Obtains one-time and standing human approvals; saves standing rules and exports individual decisions when telemetry is configured. |
| Observability | **yes** | “Track Claude Code usage, costs, and tool activity across your organization” | [Monitoring](https://code.claude.com/docs/en/monitoring-usage.md) | Metrics/events generally available; distributed traces beta. Built-in instrumentation collects and exports activity evidence; users configure export destinations. |

**C1 — part; DISPUTABLE: yes.** Projects are defined as “one coordinating conversation with Claude plus the threads it starts to do the work.” The conversation ruling supports the lower value; their named, persistent work scope and multiple workers make an area-of-work interpretation defensible. Projects are public beta. [Projects, organization](https://code.claude.com/docs/en/claude-projects.md#how-a-project-is-organized)

**C2 — part.** Project instructions cover “What the project is for”; subagents have “a custom system prompt, specific tool access, and independent permissions.” Scope exists at project level, but specialist responsibilities and configurations are per agent; the pages do not establish separately fillable area-level roles. [Project instructions](https://code.claude.com/docs/en/claude-projects.md#write-project-instructions), [subagents](https://code.claude.com/docs/en/sub-agents.md)

**C3 — part.** The marketplace `owner` field holds “Maintainer information. `name` is required; `email` and `url` are optional”; a plugin’s `author` field holds “`name`, which is required, plus optional `email` and `url`”. These are kept asset-provider records, without stated accountability for each responsibility or capability. [Marketplace fields](https://code.claude.com/docs/en/plugins/marketplace-reference.md#top-level-fields), [plugin manifest fields](https://code.claude.com/docs/en/plugins/manifest-reference.md#fields)

**C4 — part.** “Claude discovers the target with `ListAgents` and sends with `SendMessage`”. This supplies agent discovery and addressing. The documented listing is by session identity; capability-based subagent selection remains within the delegating orchestrator’s logic. [Cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging#message-another-session), [subagent delegation](https://code.claude.com/docs/en/sub-agents.md)

Pages opened, all on **2026-11-12**:

- [Documentation index](https://code.claude.com/docs/llms.txt)
- [Overview](https://code.claude.com/docs/en/overview)
- [Changelog](https://code.claude.com/docs/en/changelog.md)
- [GitHub CHANGELOG page](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) — page shell only
- [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)
- [Cloud scheduled tasks](https://code.claude.com/docs/en/routines)
- [Projects](https://code.claude.com/docs/en/claude-projects.md)
- [Run agents in parallel](https://code.claude.com/docs/en/agents.md)
- [Agent view](https://code.claude.com/docs/en/agent-view.md)
- [Subagents](https://code.claude.com/docs/en/sub-agents.md)
- [Agent teams](https://code.claude.com/docs/en/agent-teams)
- [Cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging)
- [Tools reference](https://code.claude.com/docs/en/tools-reference.md)
- [MCP](https://code.claude.com/docs/en/mcp)
- [Plugins overview](https://code.claude.com/docs/en/plugins/overview.md)
- [Marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference.md)
- [Plugin manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference.md)
- [Plugin loading reference](https://code.claude.com/docs/en/plugins/loading.md)
- [Authentication](https://code.claude.com/docs/en/authentication.md)
- [Self-hosted session identity](https://code.claude.com/docs/en/self-hosted-environments-identity)
- [Permissions](https://code.claude.com/docs/en/permissions.md)
- [Monitoring](https://code.claude.com/docs/en/monitoring-usage.md)

Could not open:

- [Background-agents URL](https://code.claude.com/docs/en/background-agents): inaccessible; used the documented agent-view page.
- These URL variants failed, but their alternate forms listed above opened: [Projects HTML](https://code.claude.com/docs/en/claude-projects), [changelog HTML](https://code.claude.com/docs/en/changelog), [agent-teams Markdown](https://code.claude.com/docs/en/agent-teams.md), [session-identity Markdown](https://code.claude.com/docs/en/self-hosted-environments-identity.md), [cross-session-messaging Markdown](https://code.claude.com/docs/en/cross-session-messaging.md), [MCP Markdown](https://code.claude.com/docs/en/mcp.md).
- GitHub’s CHANGELOG page did not expose the file body; the official documentation’s generated changelog supplied the release information.

Local sources: read `protocol-v2.md` and `rerate-criteria-v2.md` in full; ran `claude --version </dev/null` and `claude --help </dev/null`. No other local file content was opened or printed.