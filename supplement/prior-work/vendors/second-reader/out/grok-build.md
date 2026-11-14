Grok Build: newest changelog entry **1.0.77, November 5, 2026**; installed CLI: **1.0.67 (2fe064390d07) [stable]**.

| Service | Value | Quote | URL | Availability and reason |
|---|---|---|---|---|
| Sessions | **yes** | “Grok saves every conversation to disk automatically” | [Sessions](https://docs.x.ai/build/features/sessions) | Available in the stable CLI. Persisted prompts, responses, tool calls, resumable state, and conversation forks cover retention and handoff. |
| Tasks | **part — DISPUTABLE: yes** | “Progress is saved as the run goes, so pausing and resuming never redoes finished work.” | [Workflows](https://x.ai/news/workflows), [Background tasks](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/20-background-tasks.md), [Changelog](https://x.ai/changelog/build) | Available; workflows default on. Tracks work, cancellation, saved requests, and workflow recovery. **yes** is defensible if inference retries and workflow resumption satisfy unit-level retry/recovery; arbitrary failed-work retry is not established. |
| Scheduling | **yes** | “`/loop` runs a prompt on a recurring interval:” / “concurrent in-flight subagent sampling calls per process” | [Background tasks](https://docs.x.ai/build/features/background-tasks), [Configuration](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/05-configuration.md) | Available; `/loop` is feature-gated. Timers, monitor events, queued prompts, and concurrent sampling limits govern starts. |
| Retrieval | **yes** | “Before starting related work, Grok reads the topics that cover the area and applies them” | [Memory in Grok Build](https://x.ai/news/grok-build-memory) | Available now. Fetches stored project and global topic notes for related work. |
| Artifacts | **part — DISPUTABLE: yes** | “Restore the original session's repository snapshot when resuming” / “File changes made after that turn are left as-is on disk.” | Installed `grok --help </dev/null`; [Session guide](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/17-sessions.md) | Available in the stable CLI. Files and repository restoration exist; a general output-version history is not established. **yes** is defensible if repository snapshots suffice. Current guide contradicts the older Sessions page’s file-rewind claim. |
| Observability | **yes** | “Grok CLI can export usage metrics and events to your organization's own OpenTelemetry collector” | [Monitoring usage](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/24-monitoring-usage.md) | External OpenTelemetry is **alpha**, opt-in; session records and trace export also exist. Collects usage, tool decisions, and errors. |
| Evaluation | **part — DISPUTABLE: yes** | “a panel of reviewer subagents checks the work against the evidence.” | [Modes and Commands — Goals](https://docs.x.ai/build/modes-and-commands#goals), [Changelog](https://x.ai/changelog/build) | Available; goal feature must be enabled. Reviews measurable completion criteria. No general unavailable-check → “unknown” contract found. **yes** is defensible because stuck goals disclose gaps and Auto-review distinguishes inability to review. |
| Improvement | **yes** | “Capture any session as a new skill with /skillify” | [Grok Build — Skills](https://x.ai/build) | Available now; current page does not label it beta or preview. Converts session evidence into a reusable skill. |

**C1: part.** “`force_login_team_uuid` pins login to a team.” [Enterprise Deployments](https://docs.x.ai/build/enterprise#restricting-login-methods). Teams are named organizational groupings with membership and policy properties; no defined division of work among areas is described.

**C2: part.** “ZDR is enforced at the team level.” [Enterprise Deployments](https://docs.x.ai/build/enterprise#zero-data-retention). The team has rules, but no team-level mission together with independently defined work roles.

**C3: part.** `"owner": { "name": "Platform Team", "email": "platform@example.com" }` [Plugins — Write the index](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/09-plugins.md). The marketplace index demonstrates an asset owner record. It is an example, and does not assign accountability per responsibility or capability.

**C4: part.** “An unknown type fails the call with the list of valid types.” / “Only the top-level session spawns subagents.” [Subagents and Personas](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/16-subagents.md). The parent discovers and selects registered agent types; routing remains within the top-level orchestrator.

Pages opened, all read **November 12, 2026**:

- [Grok Build overview](https://docs.x.ai/build/overview)
- [Changelog](https://x.ai/changelog/build)
- [Official repository](https://github.com/xai-org/grok-build)
- [Workflows announcement](https://x.ai/news/workflows)
- [Sessions](https://docs.x.ai/build/features/sessions)
- [Background Tasks](https://docs.x.ai/build/features/background-tasks)
- [Subagents](https://docs.x.ai/build/features/subagents)
- [Hooks](https://docs.x.ai/build/features/hooks)
- [Skills, Plugins & Marketplaces](https://docs.x.ai/build/features/skills-plugins-marketplaces)
- [Skills, Plugins & Marketplaces — Markdown](https://docs.x.ai/build/features/skills-plugins-marketplaces.md)
- [CLI Reference](https://docs.x.ai/build/cli/reference)
- [CLI Reference — Markdown](https://docs.x.ai/build/cli/reference.md)
- [Modes and Commands](https://docs.x.ai/build/modes-and-commands)
- [Enterprise Deployments](https://docs.x.ai/build/enterprise)
- [MCP Servers](https://docs.x.ai/build/features/mcp-servers)
- [MCP Servers — Markdown](https://docs.x.ai/build/features/mcp-servers.md)
- [CLI landing URL](https://x.ai/cli), redirected to [Grok Build](https://x.ai/build), also opened directly
- [Memory announcement](https://x.ai/news/grok-build-memory)
- [Repository user-guide directory](https://github.com/xai-org/grok-build/tree/main/crates/codegen/xai-grok-pager/docs/user-guide)
- [User-guide index](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/README.md)
- [Configuration guide](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/05-configuration.md)
- [Skills guide](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/08-skills.md)
- [Plugins guide](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/09-plugins.md)
- [Subagents and Personas guide](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/16-subagents.md)
- [Session Management guide](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/17-sessions.md)
- [Background Tasks and Monitoring guide](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/20-background-tasks.md)
- [Monitoring Usage guide](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/24-monitoring-usage.md)

Local primary-source commands, all with stdin closed: `grok --version </dev/null`, `grok --help </dev/null`, `grok trace --help </dev/null`.

Could not open consistently: repeat requests for the MCP Servers and CLI Reference Markdown pages returned tool-access errors after initial responses; their HTML pages opened. One later request for the Background Tasks repository guide returned `UnexpectedStatusCode`; earlier opens and subsequent extracted passages were available.