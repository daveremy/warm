Newest changelog date seen: **2026-11-12**, announcing self-hosted Claude Managed Agents. [Release notes](https://platform.claude.com/docs/en/release-notes/overview)

| Service | Value | Quote | URL | Availability and reason |
|---|---|---|---|---|
| Approvals | **yes** | **Held actions:** “If a tool call waits for you, its card shows Approve and Deny.” **Advance approval:** “To auto-approve tools from a trusted MCP server, set `default_config.permission_policy` on the `mcp_toolset` entry.” **Configuration record:** “Updating an agent generates a new version when the configuration changes.” **Decision record:** “The CLI sends your choice as a `user.tool_confirmation` event, with any reason you type as its `deny_message`.” **Retention:** “Sessions and their history stay in your database until you delete them.” | [Console](https://platform.claude.com/docs/en/managed-agents/self-hosted/console); [Permissions](https://platform.claude.com/docs/en/managed-agents/permission-policies); [Agent versions](https://platform.claude.com/docs/en/managed-agents/agent-setup); [CLI decisions](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/sessions-connect); [Storage](https://platform.claude.com/docs/en/managed-agents/self-hosted-data-and-access) | Permission policies are **beta**; self-hosted distribution requires account-team access. Explicit `always_allow` settings authorize a class defined by tool/toolset, with per-tool overrides and applicable domain restrictions. Agent versions and session configuration retain those settings; tool events record permission evaluations. Held calls receive recorded allow/deny decisions through the console, CLI, or API. `auto` evaluates tool inputs and session intent, allowing, denying, or holding calls; it does not itself constitute human approval. Custom-tool approvals require application code. Durable retention requires the database. |

Pages opened, all read **2026-11-13**:

- [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- [Self-hosted Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/self-hosted)
- [Differences from the hosted service](https://platform.claude.com/docs/en/managed-agents/self-hosted/differences)
- [Use the console on your server](https://platform.claude.com/docs/en/managed-agents/self-hosted/console)
- [Permission policies](https://platform.claude.com/docs/en/managed-agents/permission-policies)
- [Define your agent](https://platform.claude.com/docs/en/managed-agents/agent-setup)
- [Tools](https://platform.claude.com/docs/en/managed-agents/tools)
- [Restrict web search and web fetch domains](https://platform.claude.com/docs/en/managed-agents/tools-web-restrictions)
- [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)
- [Session operations](https://platform.claude.com/docs/en/managed-agents/session-operations)
- [Managed Agents reference](https://platform.claude.com/docs/en/managed-agents/reference)
- [Connect to a Managed Agents session from your terminal](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/sessions-connect)
- [Secure your Managed Agents deployment](https://platform.claude.com/docs/en/managed-agents/secure-deployment)
- [Review and monitor agent sessions](https://platform.claude.com/docs/en/managed-agents/secure-deployment-monitoring)
- [Data and access in self-hosted Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/self-hosted-data-and-access)
- [Upgrade self-hosted Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/self-hosted/upgrade)

Could not inspect: the release archive’s `CHANGELOG.md` and `operator-guide.md`; access to the archive was unavailable. Their locations are documented in the [upgrade guide](https://platform.claude.com/docs/en/managed-agents/self-hosted/upgrade) and [self-hosted overview](https://platform.claude.com/docs/en/managed-agents/self-hosted). All attempted public pages opened.