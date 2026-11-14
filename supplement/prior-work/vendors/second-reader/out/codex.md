Codex CLI **0.167.2** installed; newest release seen: **2026-11-12**, **0.170.0-alpha.3** (prerelease). Read date: **2026-11-12**.

| Service | Value | Quote | URL | Availability and reason |
|---|---|---|---|---|
| Sessions | **yes** | “Fork a previous interactive session into a new chat, preserving the original transcript.” | [Developer commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | Stable CLI resume, fork, and archive commands preserve work across interruptions. App-server also exposes stored history and live state. |
| Tasks | **yes** | “If `willRetry` is `true`, the server retries and the turn stays active.” | [App-server: errors](https://learn.chatgpt.com/docs/app-server.md#errors) | Implemented in the harness; public app-server interface is experimental. Turns retain input, expose completion/failure, support cancellation, and coordinate retries; stored threads support recovery. |
| Scheduling | **part — DISPUTABLE: yes** | “scheduled tasks can work with local projects and run in the project directory or an isolated worktree.” | [Scheduled tasks](https://learn.chatgpt.com/docs/automations.md), [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents.md) | Desktop scheduling is available; maturity unspecified. CLI lacks its management interface. Subagent concurrency is capped, but coordination of scheduled runs against concurrency limits was not established. **Yes** is defensible if these separate mechanisms suffice. |
| Models | **yes** | “A model provider defines how Codex connects to a model (base URL, wire API, authentication, and optional HTTP headers).” | [Advanced configuration: providers](https://learn.chatgpt.com/docs/config-file/config-advanced.md#custom-model-providers) | Available in current local clients. Model selection and provider configuration support multiple models and providers, including local providers. |
| Identity | **yes** | “Tokens act as agent identities for programmatic local workflows.” | [Access tokens](https://learn.chatgpt.com/docs/enterprise/access-tokens.md), [Service accounts](https://learn.chatgpt.com/docs/enterprise/service-accounts.md) | Access tokens: Business and Enterprise; service accounts: pay-as-you-go plans. Tokens identify the represented user and creator, are listed, and can be revoked. Dedicated service identities support disabling and deletion. Maturity unspecified. |
| Secrets | **yes** | “Programs receive a placeholder; the proxy substitutes the real value for allowed destinations.” | [Cloud environments: network secrets](https://learn.chatgpt.com/docs/environments/cloud-environments.md#configure-environment-variables-and-network-secrets) | Available in Codex Cloud; maturity unspecified. Stored network secrets are substituted for allowed HTTPS destinations without placing raw credentials in agent processes or files. |
| Policy | **part — DISPUTABLE: yes** | “Run the command outside the sandbox without prompting.” / “Block the request without prompting.” | [Rules](https://learn.chatgpt.com/docs/agent-configuration/rules.md), [Agent Security](https://learn.chatgpt.com/docs/enterprise/agent-security.md), [Authentication](https://learn.chatgpt.com/docs/auth.md) | Sandbox controls are available; command rules are experimental. Action rules, network restrictions, grants, and account retention controls exist. General content ingress/egress policy was not established; **yes** is defensible if access restrictions satisfy that responsibility. |
| Evaluation | **part — DISPUTABLE: yes** | “**Custom review instructions** focuses the review on criteria you provide.” / “Timeouts are surfaced separately from explicit denials” | [Code review](https://learn.chatgpt.com/docs/code-review.md), [Auto-review](https://learn.chatgpt.com/docs/sandboxing/auto-review.md) | CLI review is stable; Auto-review is available with eligible interactive approvals. Reviews assess work and proposed behavior. Explicit unknown outcomes for unrun work-product checks were not established; **yes** is defensible if separately reported reviewer timeouts suffice. |

**C1 — part — DISPUTABLE: yes.** “Use a project to organize related chats and give ChatGPT the context it needs.” [Projects and chats](https://learn.chatgpt.com/docs/projects.md). Projects organize continuing work across chats and can coexist, but are defined primarily through context and folders rather than as responsibility areas. A broad reading of “area of work” supports **yes**.

**C2 — part.** “Core instructions that define the agent's behavior.” [Subagents, custom agent schema](https://learn.chatgpt.com/docs/agent-configuration/subagents.md#custom-agent-file-schema). Projects have scope and shared guidance; custom-agent responsibilities are specified per agent. No project-level specification combining collective responsibility and independently defined positions was found.

**C3 — part.** “Each token belongs to its creator and that user's ChatGPT workspace.” [Access tokens](https://learn.chatgpt.com/docs/enterprise/access-tokens.md). The maintained token list records creators and ownership per agent credential, not one accountable area per responsibility or capability.

**C4 — part.** “Human-facing guidance for when Codex should use this agent.” [Subagents, custom agent schema](https://learn.chatgpt.com/docs/agent-configuration/subagents.md#custom-agent-file-schema). Named custom agents have selection guidance and can receive delegated work. The documented routing is within Codex’s orchestration; no capability directory callable by any agent was established.

Pages opened, all on **2026-11-12**; HTML and Markdown variants are grouped:

- [Original Codex documentation URL](https://developers.openai.com/codex), redirected to [ChatGPT documentation](https://learn.chatgpt.com/docs).
- [Codex GitHub releases](https://github.com/openai/codex/releases).
- [Documentation index](https://learn.chatgpt.com/llms.txt), redirected to [docs/llms.txt](https://learn.chatgpt.com/docs/llms.txt).
- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli.md).
- [Codex App Server](https://learn.chatgpt.com/docs/app-server.md).
- [Scheduled tasks](https://learn.chatgpt.com/docs/automations.md).
- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents.md).
- [Authentication](https://learn.chatgpt.com/docs/auth.md).
- [Agent approvals & security](https://learn.chatgpt.com/docs/agent-approvals-security.md).
- [Code review](https://learn.chatgpt.com/docs/code-review.md).
- [Advanced configuration](https://learn.chatgpt.com/docs/config-file/config-advanced.md).
- [Projects and chats](https://learn.chatgpt.com/docs/projects), via the former `/codex/projects` URL; also [Markdown](https://learn.chatgpt.com/docs/projects.md).
- [Long-running work](https://learn.chatgpt.com/docs/long-running-work), via the former `/codex/long-running-work` URL; also [Markdown](https://learn.chatgpt.com/docs/long-running-work.md).
- [Cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments.md).
- [Rules](https://learn.chatgpt.com/docs/agent-configuration/rules.md).
- [Auto-review](https://learn.chatgpt.com/docs/sandboxing/auto-review.md).
- [Developer commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli); also [Markdown](https://learn.chatgpt.com/docs/developer-commands.md?surface=cli).
- [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees.md).
- [Access tokens](https://learn.chatgpt.com/docs/enterprise/access-tokens), via the former `/codex/enterprise/access-tokens` URL; also [Markdown](https://learn.chatgpt.com/docs/enterprise/access-tokens.md).
- [Agent Security](https://learn.chatgpt.com/docs/enterprise/agent-security.md).
- [Feature Maturity](https://learn.chatgpt.com/docs/feature-maturity.md).
- [Service accounts](https://learn.chatgpt.com/docs/enterprise/service-accounts.md).
- [ChatGPT & Codex changelog](https://learn.chatgpt.com/docs/changelog).

Could not open: [Guessed personal-access-tokens Markdown URL](https://learn.chatgpt.com/docs/enterprise/personal-access-tokens.md) returned 404; the Access tokens page above succeeded. One link-opening attempt from Agent approvals & security failed because the link identifier was invalid; the intended cloud-environments page was subsequently opened directly. GitHub release text loaded, but some asset and comparison widgets reported loading errors.

Disclosure: Read both requested local files in full. A higher-priority instruction additionally required opening the [OpenAI Docs skill](~/.codex/skills/.system/openai-docs/SKILL.md); it was not rating evidence. No earlier notes, ratings, paper, or model were opened or printed. Ran only `codex --version </dev/null` and `codex --help </dev/null`; both reported that PATH aliases could not be created on the read-only filesystem.