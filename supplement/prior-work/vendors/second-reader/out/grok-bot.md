Grok Bot v1.0.1 — newest changelog entry seen: November 11, 2026; sources read November 12, 2026.

| Service | Value | Quote | URL | Availability and reason |
|---|---|---|---|---|
| Harness | **yes** | “A turn that calls the model several times, for example between tool calls, sends one frame per call.” | [Inference hooks](https://docs.x.ai/grok-bot/inference-hooks) | Available in 1.0. Runs model/tool turns, supplies context, and summarizes older messages. The inspection hook is Enterprise beta; the underlying loop is product functionality. |
| Sessions | **yes** | “Conversations are stored outside the computer, so they survive even a reset.” / “A Bot that is mid-turn pauses at a safe point and resumes on the new computer.” | [Computer and apps](https://docs.x.ai/grok-bot/computer-and-apps); [Manage computers](https://docs.x.ai/grok-bot/computers) | Available; administrative recreation is Enterprise only. Preserves conversations and working state, supports pause/resume during recreation, and records handoffs in chats. |
| Artifacts | **part** | “A page lives in the Bot's Library” / “Click it to open the latest version.” | [Files and results](https://docs.x.ai/grok-bot/files-and-results) | Files and Library available; Pages documented as gradually rolling out, unavailable on Enterprise. Stores outputs, but retained earlier versions were not found in the files documentation or changelog searches. |
| Orchestration | **yes** | “The receiving Bot wakes, handles the request, and can reply later.” | [Message and collaborate](https://docs.x.ai/grok-bot/chat-and-collaboration) | Available in 1.0; no beta/preview label on the feature page. Bots assign stages, hand work to other Bots, receive results, and involve people. |
| Channels | **yes** | “You can also chat with your Bots in X Chat” | [FAQ](https://docs.x.ai/grok-bot/faq) | Available in desktop/mobile apps and X Chat; Team Bots also support Slack and Microsoft Teams subject to access and setup. Carries requests and results across these channels. |
| Approvals | **yes** | “Allow once: the Bot does the action now.” / “saves an Allow rule to your Custom Rules, so similar actions run on their own.” | [Approvals, security, and privacy](https://docs.x.ai/grok-bot/approvals-security-and-privacy) | Available in 1.0; no beta/preview label. Holds actions for decisions in chat and saves scoped standing authorizations. |
| Observability | **yes** | “Cursor records Bot actions, including scrubbed shell commands, in an internal store with a 90-day retention.” | [Security](https://docs.x.ai/grok-bot/security) | Enterprise Action Recording, off by default; separate audit logs and OpenTelemetry export are also documented. Collects evidence of agent and administrative actions. |
| Releases | **part** | “macOS and Windows installers keep a versioned URL for each release.” / “Its menu offers Sync to push your later edits to the team's copy, Copy link, and Unpublish.” | [Deployment](https://docs.x.ai/grok-bot/deployment); [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations) | Versioned client releases and team skill publishing available. No documented rollback for Bot configurations, skills, rules, or hosted images was found; recovery rebuilds on the latest image. |

- **C1 — yes.** “An Organization can include multiple teams, created around departments, business units, regions, or roles.” [Organizations, “Organizations model”](https://prod.cursor.com/docs/enterprise/organizations). Enterprise teams are defined organizational units with multiple members and roles. Grok Bot explicitly uses this [team and organization administration](https://docs.x.ai/grok-bot/teams-and-enterprises).
- **C2 — part.** “Each team defines its own membership, roles” [Organizations, “Organizations model”](https://prod.cursor.com/docs/enterprise/organizations). Teams have roles and administrative properties, but the searched organization and Grok Bot administration pages do not specify each unit’s substantive work responsibilities.
- **C3 — part.** “Lists every Bot on your team.” / “filter the list by sharing or by owner.” [Admin overview, “Manage Bots”](https://docs.x.ai/grok-bot/teams-and-enterprises). A kept roster identifies owners per Bot; it does not assign unique accountability per responsibility or capability.
- **C4 — yes.** “A Team Bot can suggest other team Bots that fit a request and link to a chat with one.” [Changelog, November 3, 2026](https://x.ai/changelog/bot). The [Team Bots documentation](https://docs.x.ai/grok-bot/team-bots) also describes searching by what Bots do. This supplies capability-based discovery and a reachable handler beyond the primary Bot’s own routing.

**Pages opened — all on November 12, 2026:**

- [Introducing Grok Bot](https://x.ai/news/introducing-grok-bot)
- [API documentation overview](https://docs.x.ai/overview) — redirected from `docs.x.ai`
- [Get started](https://docs.x.ai/grok-bot/get-started)
- [FAQ](https://docs.x.ai/grok-bot/faq)
- [Introducing Grok Bot 1.0](https://x.ai/news/grok-bot-1-0)
- [Files and results](https://docs.x.ai/grok-bot/files-and-results)
- [How Grok Bot works](https://docs.x.ai/grok-bot/how-grok-bot-works)
- [Grok Bot changelog](https://x.ai/changelog/bot)
- [Message and collaborate](https://docs.x.ai/grok-bot/chat-and-collaboration)
- [Create and manage Bots](https://docs.x.ai/grok-bot/bots)
- [Approvals, security, and privacy](https://docs.x.ai/grok-bot/approvals-security-and-privacy)
- [Team Bots](https://docs.x.ai/grok-bot/team-bots)
- [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations)
- [Inference hooks](https://docs.x.ai/grok-bot/inference-hooks)
- [Computer and apps](https://docs.x.ai/grok-bot/computer-and-apps)
- [Use cases](https://docs.x.ai/grok-bot/use-cases)
- [Security](https://docs.x.ai/grok-bot/security)
- [Teams and enterprises](https://docs.x.ai/grok-bot/teams-and-enterprises)
- [Manage computers](https://docs.x.ai/grok-bot/computers)
- [Settings and notifications](https://docs.x.ai/grok-bot/settings-and-notifications)
- [Deployment](https://docs.x.ai/grok-bot/deployment)
- [Organizations](https://prod.cursor.com/docs/enterprise/organizations)
- [Organization Groups](https://prod.cursor.com/docs/enterprise/organization-groups)
- [Organizations for Cursor Enterprise](https://cursor.com/changelog/enterprise-organizations)

Local reading: `protocol-v2.md` and `rerate-criteria-v2.md`, in full. No other local files were opened or printed.

**Could not open:** [Organization Groups at cursor.com](https://cursor.com/docs/enterprise/organization-groups) returned `UnexpectedStatusCode`. The official `prod.cursor.com` documentation page listed above opened successfully.