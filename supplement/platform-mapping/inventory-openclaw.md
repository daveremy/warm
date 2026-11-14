---
title: "OpenClaw component inventory"
date: 2026-11-11
type: research-inventory
subject: OpenClaw (formerly Warelay, Clawdbot, Moltbot)
sources: primary only (docs.openclaw.ai, github.com/openclaw/openclaw, github.com/openclaw/clawhub)
---

# OpenClaw component inventory

**Date stamp:** compiled 2026-11-11 (America/Phoenix). Docs and repository read the same day.

**Method.** I read the docs source from `github.com/openclaw/openclaw` at commit `9c2e60f7d003e30d417d60655a4bd2dc56168e8d` (committed 2026-11-11 12:40 PST), `docs/` folder, and followed the site navigation exactly as `docs/docs.json` defines it (English). The published site is https://docs.openclaw.ai; every URL below is the published URL of the page I read in source. I spot-checked the live site against the source (https://docs.openclaw.ai/concepts/architecture, https://docs.openclaw.ai/clawhub, https://docs.openclaw.ai/clawhub/how-it-works) and found them consistent. The 14 ClawHub tab pages are not in the openclaw repo; their source is `docs/` in `github.com/openclaw/clawhub` (that repo's own README says `docs/` "is the publishable source for user-facing ClawHub pages that can be mirrored into the `ClawHub` tab on `docs.openclaw.ai`"), and I read them there.

**Staleness.** All pages come from the current `main` branch, so none is an old copy. For the pages quoted in sections 1, 3, 4 and 5, I checked each file's last commit date through the GitHub API: all were changed between 2026-09-09 and 2026-11-11, so none is older than six months. I did not check per-file dates for the 848 component entries in section 2 (664 navigation entries plus 184 plugins). Items that are marked **possibly stale (older than six months)** are dated events from before 2026-05-11: the naming history (January 2026) and release notes older than v2026.6.x.

**Quotes.** Text in quotation marks is copied from the page, including any em dashes the docs use. My own prose uses none.

**Which project.** This inventory covers `openclaw/openclaw` (MIT, "The AI that really does things", homepage https://openclaw.ai), the repository that the old names `clawdbot/clawdbot`, `moltbot/moltbot` and `steipete/warelay` now redirect to (GitHub API, 2026-11-11: each resolves to `openclaw/openclaw`, created 2025-11-24). Similarly named projects exist (NanoClaw, ZeroClaw, PicoClaw, nanobot, IronClaw and others; see section 6). They are separate codebases, and this file does not cover them.

---

## 1. What it is

**The project's description of itself** (README, https://github.com/openclaw/openclaw/blob/main/README.md, read 2026-11-11; file last changed 2026-11-05):

> "OpenClaw is an open-source AI assistant that runs on your own computer and meets you in the channels you already use: Discord, iMessage, Slack, Teams, Telegram, WhatsApp, and 20+ more, plus native apps for macOS, iOS, Android, Windows, and Linux. One Gateway runs it as a personal claw on a laptop or as a shared multiplayer claw; configuration is the only difference."

> "**Yours, with no catch.** State, memory, and credentials live on your hardware. Models and agent harnesses (Claude, Codex, local models) are plugins you can swap without changing anything else. [...] OpenClaw is stewarded by the OpenClaw Foundation, an independent 501(c)(3), and has no paid tier, hosted service, or token."

The docs home page (https://docs.openclaw.ai/, read 2026-11-11) puts it this way:

> "OpenClaw is a **self-hosted gateway** that connects your favorite chat apps — Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, and more via channel plugins — to AI coding agents. You run a single Gateway process on your own machine (or a server), and it becomes the bridge between your messaging apps and an always-available AI assistant."

VISION.md (https://github.com/openclaw/openclaw/blob/main/VISION.md): "OpenClaw is the AI that actually does things. It runs on your devices, in your channels, with your rules."

**Naming history** (possibly stale: these events date from 2025-12 to 2026-01, but the pages describing them were edited 2026-10):
- VISION.md: "It evolved through several names and shells: Warelay -> Clawdbot -> Moltbot -> OpenClaw." (https://github.com/openclaw/openclaw/blob/main/VISION.md)
- Lore page (https://docs.openclaw.ai/start/lore): "For a while it was **Clawd**, living in a **Clawdbot**. In January 2026, Anthropic sent a polite email asking for a name change (trademark stuff)." Then: "it emerged as **Molty**, living in **Moltbot**. That name never quite rolled off the tongue either." Then: "On January 30, 2026, the lobster molted one more time into its final form: **OpenClaw**." The section "The First Molt (January 27, 2026)" says "**Moltbot** won" a community vote held in Discord. The same section says the GitHub repo was renamed to `github.com/openclaw/openclaw` and the docs moved to `docs.openclaw.ai` during "The Great OpenClaw Migration".
- The lore page is internally inconsistent on one detail: under "The Great Molt (Jan 27, 2026)" it says "By 6:14am, Peter called it: 'fuck it, let's go with openclaw.'", yet the same page dates the move to OpenClaw to January 30, 2026, after Moltbot. I report both as written.
- GitHub redirects confirm the lineage: `steipete/warelay`, `clawdbot/clawdbot` and `moltbot/moltbot` all resolve to `openclaw/openclaw` (GitHub API, 2026-11-11).
- Creator: README says "OpenClaw was built for **Molty**, a space lobster AI assistant, by Peter Steinberger and the community."

**License:** MIT. GitHub license metadata reports "MIT License" (https://github.com/openclaw/openclaw/blob/main/LICENSE); the docs home page says "MIT licensed, community-driven".

**Governance:** "OpenClaw is developed in the open by the OpenClaw Foundation, an independent 501(c)(3). The Foundation employs the core team and signs releases. [...] OpenAI is a donor, not an owner." (README)

**Current version and latest release:** `v2026.11.3` ("openclaw 2026.11.3"), marked Latest on GitHub, published 2026-11-10T18:53:07Z (https://github.com/openclaw/openclaw/releases/tag/v2026.11.3). Its release notes say: "This is a patch release with no new features." (https://docs.openclaw.ai/releases/2026.11.3). Other recent tags: `v2026.9.37` (published 2026-11-10T20:42:54Z, not marked Latest), `v2026.11.5-beta.1` (pre-release, 2026-11-04). The project versions by calendar and has four release channels: "stable, extended-stable, beta, and dev" (https://docs.openclaw.ai/install/development-channels). The docs call one release "v2026.8.1 (AKA OpenClaw 2.0)" (https://docs.openclaw.ai/releases/2026.8.1).

**Where my prior knowledge disagreed with the pages (the pages win):**
- I expected "heartbeat" to be a core periodic wake-up feature. The pages say: "Existing heartbeat monitors migrate into ordinary editable jobs with their own scratch, execution policies, and delivery settings." (https://docs.openclaw.ai/automation)
- I expected a "Tasks"/TaskFlow layer. The automation page says: "The shared Tasks ledger, TaskFlow orchestration API, and TaskFlow Webhooks plugin have been removed." (https://docs.openclaw.ai/automation)
- I knew ClawHub as a skills registry. The pages now say: "ClawHub is the public registry for OpenClaw skills and plugins." (https://docs.openclaw.ai/clawhub)
- I knew the macOS "Canvas" as a separate surface. Architecture now calls it the "hosted widget surface" served under `/__openclaw__/canvas/` (https://docs.openclaw.ai/concepts/architecture).

---

## 2. Components

**How this section is built.** One entry per page in the docs navigation, in the navigation's own order and grouping (tab, then group, then subgroup). The ClawHub tab is included. When the navigation nests a set of pages that all belong to one feature (for example "Discord" with its setup, access-control and troubleshooting pages), the feature is one entry and its pages are listed as **Sub-pages**. Nested groups of peer pages (for example "Speech and audio" providers) keep one entry per page under a **Nav subgroup** label. Result: 664 navigation entries. The Releases, Contributing and Help tabs hold release notes, contributor process and FAQs rather than components; their pages are listed by name at the end of this section. After the navigation entries comes the docs' own **Plugin inventory**, which names every plugin (184) in the docs' three groups.

**Fields in each entry:**
- **What it does (docs):** the page's own `summary` line, then the first one or two sentences of the page body, both verbatim.
- **URL:** the published page.
- **Who runs it:** my reading of where it executes, based on these statements: the Gateway runs on the user's machine ("You run a single Gateway process on your own machine (or a server)", https://docs.openclaw.ai/); model providers and messaging services are third parties the Gateway connects to (https://docs.openclaw.ai/concepts/architecture); ClawHub is a hosted registry at clawhub.ai (https://docs.openclaw.ai/clawhub); cloud workers are "A throwaway machine leased through Crabbox" (https://docs.openclaw.ai/gateway/cloud-sessions); plugin SDK pages describe code the user writes (https://docs.openclaw.ai/plugins/building-plugins). This is the only field that is my wording.
- **Packaging (docs):** where the docs say it. Channel entries come from the generated channel catalog on https://docs.openclaw.ai/channels ("bundled plugin", "included in core", "official plugin", "external plugin"). Other entries come from https://docs.openclaw.ai/plugins/plugin-inventory ("included in OpenClaw" = core npm package; official external package; source checkout only).
- **Depends on:** the page's own Requirements or Prerequisites section, where it has one. Otherwise the dependency is the one the tab implies: everything depends on a running Gateway ("Automations run **inside the Gateway process** [...] The Gateway must be running for schedules to fire", https://docs.openclaw.ai/automation/cron-jobs/how-it-works), and section 3 lists what the user supplies.
- **Status:** the project's own **maturity scorecard** level for every scorecard surface that links the page (M0 Planned, M1 Experimental, M2 Alpha, M3 Beta, M4 Stable, M5 Clawesome; definitions at https://docs.openclaw.ai/maturity/taxonomy). A page can feed several surfaces; the entry lists them, best name match first. Pages the scorecard does not link have no scorecard level. Where the page itself says "Status:", "experimental", "deprecated" or "removed", the first such sentence is quoted; it can refer to a sub-feature, not the whole page. A frontmatter `status:` field is shown where present (only 10 pages have one). The docs add: "All OpenClaw plugin APIs are **experimental**." (https://docs.openclaw.ai/plugins/sdk-overview)

**The maturity scorecard's 50 surfaces and their levels** (https://docs.openclaw.ai/maturity/scorecard; file last changed 2026-10-08). The scorecard sums up as "68% Maturity score", "Alpha". It groups the surfaces into four families: Core, Platform, Channel, Provider and tool (https://docs.openclaw.ai/maturity/taxonomy).

| Family | Surface: level |
|---|---|
| Core | CLI: M4 Stable; Gateway runtime: M4 Stable; Agent Runtime: M3 Beta; Channel framework: M3 Beta; Observability: M3 Beta; Control UI: M3 Beta; Plugins: M3 Beta; Security, auth, pairing, and secrets: M3 Beta; Automation and durable work: M3 Beta; Session, memory, and state lifecycle: M3 Beta; Media understanding and media generation: M2 Alpha; Voice and realtime talk: M2 Alpha; TUI: M2 Alpha; ClawHub: M2 Alpha; External apps and interoperability: M2 Alpha |
| Platform | Linux Gateway host: M4 Stable; macOS Gateway host: M4 Stable; Android app: M4 Stable; iOS app: M4 Stable; Windows via WSL2: M3 Beta; ChromeOS, Raspberry Pi, and small Linux devices: M3 Beta; macOS companion app: M3 Beta; Linux companion app: M3 Beta; Containers and cloud execution: M3 Beta; Windows App / Node: M3 Beta; Native Windows: M2 Alpha; Kubernetes hosting: M2 Alpha; Nix install path: M1 Experimental; watchOS companion surfaces: M1 Experimental |
| Channel | Discord: M4 Stable; Telegram: M3 Beta; Slack: M3 Beta; iMessage: M3 Beta; WhatsApp: M3 Beta; Matrix: M2 Alpha; Google Chat: M2 Alpha; Microsoft Teams: M2 Alpha; Signal: M2 Alpha; Regional channel cohort: M2 Alpha; Community channel cohort: M2 Alpha; Voice Call channel: M1 Experimental |
| Provider and tool | Browser automation, exec, and sandbox tools: M3 Beta; OpenAI and Codex provider path: M3 Beta; Web search tools: M3 Beta; Anthropic provider path: M3 Beta; Google provider path: M3 Beta; OpenRouter provider path: M3 Beta; Image, video, and music generation tools: M2 Alpha; Local model providers: Ollama, vLLM, SGLang, LM Studio: M2 Alpha; Long-tail hosted providers: M2 Alpha |

**Experimental flags the docs list** (https://docs.openclaw.ai/concepts/experimental-features; file changed 2026-11-11). "Experimental features are preview surfaces controlled by config flags." The currently documented flags cover these surfaces: Codex harness (`sandboxExecServer`), Code Mode, Cloud workers (desktop), Templates, This computer's desktop, Advisor, OpenClaw ID, Speech bubbles, Tool Search. Control UI **Settings → Labs** also lists "Decision assistance". Broadcast groups is the one page whose frontmatter reads `status: experimental` (https://docs.openclaw.ai/channels/broadcast-groups).

**The docs' own short map of the pieces** (README "How it fits together", https://github.com/openclaw/openclaw/blob/main/README.md):
> "The Gateway is the local control plane for sessions, tools, events, and channel connections. The Control UI, CLI, and TUI connect to the Gateway. Channels bring the assistant to WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, and other messaging services. Companion apps and nodes add voice, Canvas, camera, screen, and device-local actions on supported platforms. OpenClaw works with hosted and local model providers. Its tools, skills, and plugins extend what an assistant can do."

### Tab: Get started

**Group: Overview**

#### OpenClaw
- **What it does (docs):** "OpenClaw is an open-source AI assistant that runs on your own hardware and meets you in every chat app you already use." / "Your AI assistant, on your own hardware, in every chat app you already use. One Gateway."
- **URL:** https://docs.openclaw.ai/
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Why OpenClaw
- **What it does (docs):** "The architecture case for OpenClaw: a trusted gateway, untrusted execution, policy enforced by code, and versioned state, compared source-by-source with single-process harnesses" / "OpenClaw is an extensible, proactive, open-source AI agent that works everywhere you work. It exists because software is inverting: for decades you went to the computer, opened the app, clicked through its screens, and did the work yourself."
- **URL:** https://docs.openclaw.ai/start/why-openclaw
- **Who runs it:** User machine (the Gateway host or a client of it).

#### The trust boundary
- **What it does (docs):** "Where OpenClaw's Gateway authority ends and configured sandbox, node, and cloud-worker execution begins" / "The Gateway owns channel connections, config, credentials, and the control-plane API. It binds to loopback by default and refuses non-loopback binds without a working auth path (architecture, network model)."
- **URL:** https://docs.openclaw.ai/start/why-openclaw/the-trust-boundary
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Policy as code
- **What it does (docs):** "Permission modes, tool policy, and exec approvals as code-enforced gates rather than prompt requests" / "Code-based enforcement is not unique to OpenClaw — Claude Code, Codex, and Goose all gate approvals in code. Structural tool gating in a multi-channel assistant, rather than a terminal, is rarer: permission modes shape which tools exist at all."
- **URL:** https://docs.openclaw.ai/start/why-openclaw/policy-as-code
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Identity and roles
- **What it does (docs):** "Pairing, operator scopes, role ceilings, and the one-gateway-is-one-trust-domain boundary" / "Device-authenticated control-plane clients present signed identities and go through pairing. Reconnecting with broader device scopes requires approval."
- **URL:** https://docs.openclaw.ai/start/why-openclaw/identity-and-roles
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Secrets
- **What it does (docs):** "SecretRefs, the protected store, egress sentinels, and the custody limits of each" / "Every supported credential field takes a SecretRef: `env`, `file`, `exec` (this is how 1Password, Vault, Bitwarden, and sops plug in), or the shared store. Retryable resolution failures for mapped, isolatable owners let the Gateway start degraded."
- **URL:** https://docs.openclaw.ai/start/why-openclaw/secrets
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Versioned state, guarded upgrades
- **What it does (docs):** "Database-first state, schema version contracts, guarded updates, release channels, and the maturity scorecard" / "Runtime state is database-first: one global SQLite store, one per agent, with a written contract that runtime code never reads or writes JSON sidecars as active state. The contract is machine-checked in CI (database schemas)."
- **URL:** https://docs.openclaw.ai/start/why-openclaw/versioned-state-guarded-upgrades
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: Diagnostics, Maintenance, and Recovery). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Provenance
- **What it does (docs):** "Memory origin classes, trust gating, deletion boundaries, and the audit ledger's recorded non-claims" / "The default OpenClaw memory backend keeps Markdown artifacts plus a SQLite index and metadata (memory architecture). Each indexed chunk carries an origin class (`owner`, `agent`, `untrusted`, `system`) stored outside the prose."
- **URL:** https://docs.openclaw.ai/start/why-openclaw/provenance
- **Who runs it:** User machine (the Gateway host or a client of it).

#### OpenClaw and Hermes Agent
- **What it does (docs):** "Source-by-source comparison of OpenClaw and Hermes Agent at the reviewed August 2026 snapshots, with the property table" / "Hermes Agent (Nous Research, MIT) is a personal-agent platform with a CLI, messaging gateway, desktop app, and plugin system. The comparison below reflects source at `6defe7eb6c` (reviewed August 27, 2026), not a live adversarial test or a guarantee about every deployment."
- **URL:** https://docs.openclaw.ai/start/why-openclaw/openclaw-and-hermes-agent
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Features
- **What it does (docs):** "OpenClaw capabilities across channels, routing, media, and UX." / "Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat, and more with a single Gateway."
- **URL:** https://docs.openclaw.ai/concepts/features
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Docs hubs
- **What it does (docs):** "Hubs that link the main OpenClaw docs" / "If you are new to OpenClaw, start with Getting Started."
- **URL:** https://docs.openclaw.ai/start/hubs
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Docs directory
- **What it does (docs):** "Curated links to the most used OpenClaw docs." / "This page is a curated index. If you are new, start with Getting Started."
- **URL:** https://docs.openclaw.ai/start/docs-directory
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Nix install path" surface, M1 Experimental (area: Install Handoff). Source: https://docs.openclaw.ai/maturity/taxonomy

**Group: First steps**

#### Getting started
- **What it does (docs):** "Get OpenClaw installed and run your first chat in minutes." / "Install OpenClaw, run onboarding, and chat with your AI assistant in about 5 minutes. By the end you will have a running Gateway, configured auth, and a working chat session."
- **URL:** https://docs.openclaw.ai/start/getting-started
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** Node.js 24.16.0+ on 24.x, or 26.1.0+ (Node 26 is recommended; use 24.22.1+/26.12.1+ for the security fixes); An existing Claude Code or Codex CLI login, or a provider API key — onboarding can reuse it; Windows users: the native Windows Hub app is the easiest desktop path. The
- **Status (maturity scorecard, which links this page):** "Control UI" surface, M3 Beta (area: WebChat Conversations); "Native Windows" surface, M2 Alpha (area: CLI); "Windows via WSL2" surface, M3 Beta (area: CLI, WSL Setup). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Onboarding overview
- **What it does (docs):** "Overview of OpenClaw onboarding options and flows" / "OpenClaw supports onboarding from the terminal, the macOS app, and the Linux desktop companion. Every path establishes inference first."
- **URL:** https://docs.openclaw.ai/start/onboarding-overview
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: Onboarding and Auth Setup). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Onboarding (CLI)
- **What it does (docs):** "CLI onboarding: quick start with detected AI access or choose custom setup" / "CLI onboarding is the recommended terminal setup path on macOS, Linux, and Windows (native or WSL2). On a fresh install, **Quick start** detects available AI access, waits for you to choose a connection, verifies your choice with a real completion, asks whether to keep OpenClaw running in the background, and opens the web dashboard."
- **URL:** https://docs.openclaw.ai/start/wizard
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Onboarding (macOS app)
- **What it does (docs):** "First-run setup flow for OpenClaw (macOS app)" / "Open OpenClaw.app to set up a Gateway on this Mac and connect an AI model. The app includes its own runtime; you do not need to install Node or a package manager."
- **URL:** https://docs.openclaw.ai/start/onboarding
- **Who runs it:** User machine (the Gateway host or a client of it).

**Group: Setup guides and reference**

#### Personal assistant setup
- **What it does (docs):** "End-to-end guide for running OpenClaw as a personal assistant with safety cautions" / "OpenClaw is a self-hosted gateway that connects Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, and more to AI agents. This guide covers the "personal assistant" setup: a dedicated WhatsApp number that behaves like your always-on AI assistant."
- **URL:** https://docs.openclaw.ai/start/openclaw
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** OpenClaw installed and onboarded - see Getting Started if you haven't done this yet; The WhatsApp plugin installed, or WhatsApp chosen during onboarding. WhatsApp is an official plugin that installs on demand. See WhatsApp; A second phone number (SIM/eSIM/prepaid) for the assistant
- **Status (maturity scorecard, which links this page):** "Linux companion app" surface, M3 Beta (area: Status and Diagnostics). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "names remain available as deprecated compatibility aliases."

#### Multiplayer
- **What it does (docs):** "Run OpenClaw as a multiplayer claw: one shared Gateway for a trusted team, from first setup to an always-on production deployment" / "OpenClaw runs in one of two shapes. A **personal claw** is one person's assistant on their own machine - see Personal assistant setup."
- **URL:** https://docs.openclaw.ai/start/multiplayer
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** A host for the Gateway that stays on: a small VPS, an office Mac, or any supported install target.; OpenClaw installed and onboarded on that host - see Getting started.; A chat workspace the team already uses (Discord, Google Chat, Mattermost, Microsoft Teams, Slack, Telegram, ...) - see Channels.; A strong latest-generation model. Shared gateways see more varied input than a solo setup, and modern models are substantially more resistant to prompt injectio

#### CLI setup reference
- **What it does (docs):** "Step-by-step behavior for openclaw onboard: what each step does, config it writes, and internals" / "This page covers step-by-step onboarding behavior, outputs, and internals. For a walkthrough, see Onboarding (CLI)."
- **URL:** https://docs.openclaw.ai/start/wizard-cli-reference
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Google Chat" surface, M2 Alpha (area: Channel Setup and Operations). Source: https://docs.openclaw.ai/maturity/taxonomy

#### CLI automation
- **What it does (docs):** "Scripted onboarding and agent setup for the OpenClaw CLI" / "Use `openclaw onboard --non-interactive` to script setup. It requires `--accept-risk`: non-interactive setup can write credentials and daemon config without a confirmation prompt, so the flag is the explicit risk acknowledgement."
- **URL:** https://docs.openclaw.ai/start/wizard-cli-automation
- **Who runs it:** User machine (the Gateway host or a client of it).

### Tab: Install

**Group: Install overview**

#### Install
- **What it does (docs):** "Install OpenClaw - desktop app downloads, installer script, npm/pnpm/bun, from source, Docker, and more" / "Prefer a normal app download over the CLI? OpenClaw ships desktop companions:"
- **URL:** https://docs.openclaw.ai/install
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Nix install path" surface, M1 Experimental (area: Install Handoff); "CLI" surface, M4 Stable (area: CLI Setup); "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Setup and Compatibility); "Kubernetes hosting" surface, M2 Alpha (area: Deployment Setup); plus 4 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Experimental Worker + Container deployment."

#### Installer internals
- **What it does (docs):** "How the installer scripts work (install.sh, install-cli.sh, install.ps1), flags, and automation" / "OpenClaw ships three installer scripts, served from `openclaw.ai`."
- **URL:** https://docs.openclaw.ai/install/installer
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: CLI Setup); "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Setup and Compatibility); "Native Windows" surface, M2 Alpha (area: CLI); "macOS Gateway host" surface, M4 Stable (area: CLI Setup). Source: https://docs.openclaw.ai/maturity/taxonomy

**Group: Runtimes**

#### Node.js
- **What it does (docs):** "Install and configure Node.js for OpenClaw - version requirements, install options, and PATH troubleshooting" / "OpenClaw requires **Node 24.16.0+ on the 24.x line, or Node 26.1.0+** with a WAL-reset-safe linked SQLite library. **Node 26 is the recommended runtime** — it starts the Gateway noticeably faster and uses less memory than Node 24."
- **URL:** https://docs.openclaw.ai/install/node
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: CLI Setup); "macOS Gateway host" surface, M4 Stable (area: CLI Setup). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Node.js compatibility
- **What it does (docs):** "Supported Node.js versions, SQLite requirements, platform limits, and release history" / "This reference covers supported Node.js lines, why the minimum versions exist, and how they changed across OpenClaw releases. For installation steps, see Node.js; for macOS companion app requirements, see macOS."
- **URL:** https://docs.openclaw.ai/install/node-compatibility
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Bun
- **What it does (docs):** "Bun workflow for installs, package scripts, and opt-in runtime use" / "Node remains OpenClaw's primary, default, and recommended runtime. The latest stable Bun (currently 1.4.4) and pinned OpenClaw fork can run the CLI, Gateway, and managed node host as an explicit opt-in."
- **URL:** https://docs.openclaw.ai/install/bun
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Bun compatibility
- **What it does (docs):** "Bun runtime requirements, macOS SQLite selection, limitations, and release history" / "Bun is an explicit opt-in runtime for standalone OpenClaw CLI, Gateway, and managed node host installations. Node remains their primary and recommended runtime."
- **URL:** https://docs.openclaw.ai/install/bun-compatibility
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "1 | Restores experimental CLI/Gateway support for builds providing node:sqlite, documented as 1."

#### Standalone builds
- **What it does (docs):** "Build a standalone OpenClaw executable with Bun and a companion runtime directory" / "The standalone builder packages OpenClaw and Bun into one executable, with a companion `runtime/` directory for native libraries, plugins, and other resources. This is also called a **fat binary** build."
- **URL:** https://docs.openclaw.ai/install/standalone
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Experimental AOT Actions builds."

#### Nix
- **What it does (docs):** "Install OpenClaw declaratively with Nix" / "Install OpenClaw declaratively with **nix-openclaw**, the first-party, batteries-included Home Manager module."
- **URL:** https://docs.openclaw.ai/install/nix
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Nix install path" surface, M1 Experimental (area: Activation and App UX, Config and State). Source: https://docs.openclaw.ai/maturity/taxonomy

**Group: Maintenance**

#### Backups
- **What it does (docs):** "Back up OpenClaw state: archives, per-database snapshots, scheduling, offsite copies, and continuous replication" / "OpenClaw uses SQLite by default: one global control-plane database under the state directory (usually `~/.openclaw`), plus one database per configured agent at `/openclaw-agent.sqlite`. Agent directories default to locations under the state directory but can be configured outside it."
- **URL:** https://docs.openclaw.ai/install/backups
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: Diagnostics, Maintenance, and Recovery). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Updating
- **What it does (docs):** "Updating OpenClaw safely (global install or source), plus rollback strategy" / "Keep OpenClaw up to date."
- **URL:** https://docs.openclaw.ai/install/updating
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: CLI Setup, Gateway Service Management); "Linux Gateway host" surface, M4 Stable (area: Host Setup and Updates); "Native Windows" surface, M2 Alpha (area: Updates); "Windows via WSL2" surface, M3 Beta (area: CLI); plus 1 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "The experimental openclaw fleet command has been removed."
- **Sub-pages in the nav:** Other update methods (https://docs.openclaw.ai/install/updating/update-methods); Automatic updates (https://docs.openclaw.ai/install/updating/automatic-updates); Rollback and recovery (https://docs.openclaw.ai/install/updating/rollback-and-recovery)

#### Update troubleshooting
- **What it does (docs):** "Recover from failed OpenClaw updates in the Control UI or CLI" / "Failed updates enter built-in triage after update recovery settles. In an interactive terminal, OpenClaw shows the selected agent, saved prompt path when available, and use of your own account/tokens, then asks before launching triage."
- **URL:** https://docs.openclaw.ai/install/update-troubleshooting
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Migration guide
- **What it does (docs):** "Migration hub: cross-system imports, machine-to-machine moves, and plugin upgrades" / "OpenClaw supports three migration paths: importing from another agent system, moving an existing install to a new machine, and upgrading a plugin in place."
- **URL:** https://docs.openclaw.ai/install/migrating
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Sub-pages in the nav:** Migrating from Claude (https://docs.openclaw.ai/install/migrating-claude); Migrating from Hermes (https://docs.openclaw.ai/install/migrating-hermes); OpenProse removal and migration (https://docs.openclaw.ai/prose)

#### Uninstall
- **What it does (docs):** "Uninstall OpenClaw completely (CLI, service, state, workspace)" / "Remove the service and selected local data first, then any remaining CLI install. State deletion can also remove installation files nested inside that directory."
- **URL:** https://docs.openclaw.ai/install/uninstall
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "macOS Gateway host" surface, M4 Stable (area: Gateway Service Lifecycle). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Release channels
- **What it does (docs):** "Stable, extended-stable, beta, and dev channels: semantics, switching, pinning, and tagging" / "OpenClaw ships four update channels:"
- **URL:** https://docs.openclaw.ai/install/development-channels
- **Who runs it:** User machine (the Gateway host or a client of it).

**Group: Containers**

#### Docker
- **What it does (docs):** "Optional Docker-based setup and onboarding for OpenClaw" / "Docker is **optional**. Use it for an isolated, throwaway Gateway environment or a host without local installs."
- **URL:** https://docs.openclaw.ai/install/docker
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** Docker Desktop (or Docker Engine) + Docker Compose v2; At least 6 GB RAM for a local source image build; pre-built images avoid this build requirement; Enough disk for images and logs; On a VPS/public host, review Security hardening for network exposure, especially the Docker `DOCKER-USER` firewall chain
- **Status (maturity scorecard, which links this page):** "Containers and cloud execution" surface, M3 Beta (area: Agent Sandbox and Tooling, Container Operations); "Linux Gateway host" surface, M4 Stable (area: Deployment Targets). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Docker environment variables (https://docs.openclaw.ai/install/docker/environment-variables); Docker networking, providers, and storage (https://docs.openclaw.ai/install/docker/networking-and-storage); Docker Compose operations and image maintenance (https://docs.openclaw.ai/install/docker/compose-operations); Docker agent sandbox and troubleshooting (https://docs.openclaw.ai/install/docker/sandbox-and-troubleshooting)

#### Podman
- **What it does (docs):** "Run OpenClaw in a rootless Podman container" / "Run the OpenClaw Gateway in a rootless Podman container, managed by your current non-root user."
- **URL:** https://docs.openclaw.ai/install/podman
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** Podman in rootless mode, with its host init executable (normally `catatonit`) available for the launcher's `--init` flag. On minimal Debian/Ubuntu hosts, instal; OpenClaw CLI installed on the host; Optional: `systemd --user` if you want Quadlet-managed auto-start; Optional: `sudo` only if you want `loginctl enable-linger "$(whoami)"` for boot persistence on a headless host
- **Status (maturity scorecard, which links this page):** "Containers and cloud execution" surface, M3 Beta (area: Container Operations, Container Setup); "Linux Gateway host" surface, M4 Stable (area: Deployment Targets). Source: https://docs.openclaw.ai/maturity/taxonomy

**Group: Hosting**

#### Linux server
- **What it does (docs):** "Run OpenClaw on a Linux server or cloud VPS — provider picker, architecture, and tuning" / "Run the OpenClaw Gateway on any Linux server or cloud VPS. This page helps you pick a provider, explains how cloud deployments work, and covers generic Linux tuning that applies everywhere."
- **URL:** https://docs.openclaw.ai/vps
- **Who runs it:** A third-party host the user rents, running the user Gateway.
- **Status (maturity scorecard, which links this page):** "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Gateway Runtime); "Linux Gateway host" surface, M4 Stable (area: Deployment Targets, Gateway Runtime and Service Control). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: App platforms**

#### Cloudflare Containers
- **What it does (docs):** "Experimental Cloudflare Worker and Container deployment with Litestream backups to R2" / "Run one OpenClaw installation behind a Cloudflare Worker and a named Durable Object, with the official OpenClaw image and Litestream replication to R2."
- **URL:** https://docs.openclaw.ai/install/cloudflare
- **Who runs it:** A third-party host the user rents, running the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw, and also from npm or ClawHub: `@openclaw/cloudflare` (Core npm package)
- **Depends on (page's own requirements section):** A Cloudflare account with Workers, Containers, and R2 available; Docker Buildx with `linux/amd64` support; A public Docker Hub repository for the derived image, and a `docker login` session that can push to it; An S3-compatible CLI such as the AWS CLI, used later to verify Litestream replication
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "This deployment target is experimental."

#### Daytona
- **What it does (docs):** "Run OpenClaw in a Daytona cloud sandbox with SSH access and signed preview URLs" / "Run a persistent OpenClaw Gateway in a Daytona cloud sandbox: an isolated Linux environment with SSH access and built-in preview URLs, no VPS management required. OpenClaw comes pre-installed in the `daytona-medium` snapshot, so setup starts immediately after SSH."
- **URL:** https://docs.openclaw.ai/install/daytona
- **Who runs it:** A third-party host the user rents, running the user Gateway.
- **Depends on (page's own requirements section):** Daytona account (free tier available); Daytona API key from the Daytona dashboard; API key for your model provider (Anthropic, OpenAI, etc.)

#### exe.dev
- **What it does (docs):** "Run OpenClaw Gateway on exe.dev (VM + HTTPS proxy) for remote access" / "This guide assumes exe.dev's default **exeuntu** image. Map packages accordingly on other distros."
- **URL:** https://docs.openclaw.ai/install/exe-dev
- **Who runs it:** A third-party host the user rents, running the user Gateway.
- **Depends on (page's own requirements section):** exe.dev account; `ssh exe.dev` access to exe.dev VMs (optional, for manual setup)

#### Fly.io
- **What it does (docs):** "Step-by-step Fly.io deployment for OpenClaw with persistent storage and HTTPS" / "2. Create app + volume, set secrets 3."
- **URL:** https://docs.openclaw.ai/install/fly
- **Who runs it:** A third-party host the user rents, running the user Gateway.
- **Depends on (page's own requirements section):** flyctl CLI installed; Fly.io account (free tier works); Model auth: API key for your chosen model provider; Channel credentials: Discord bot token, Telegram token, etc.
- **Status (maturity scorecard, which links this page):** "Discord" surface, M4 Stable (area: Channel Setup and Operations). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Northflank
- **What it does (docs):** "Deploy OpenClaw on Northflank with one-click template" / "Deploy OpenClaw on Northflank with a one-click template and access it through the web Control UI. This is the easiest "no terminal on the server" path: Northflank runs the Gateway for you."
- **URL:** https://docs.openclaw.ai/install/northflank
- **Who runs it:** A third-party host the user rents, running the user Gateway.

#### Railway
- **What it does (docs):** "Deploy OpenClaw on Railway with one-click template" / "Deploy OpenClaw on Railway with a one-click template and access it through the web Control UI. This is the easiest "no terminal on the server" path: Railway runs the Gateway for you."
- **URL:** https://docs.openclaw.ai/install/railway
- **Who runs it:** A third-party host the user rents, running the user Gateway.

#### Render
- **What it does (docs):** "Deploy OpenClaw on Render with Infrastructure-as-Code" / "Deploy OpenClaw on Render using the repo's `render.yaml` Blueprint. It declares the service, disk, and environment variables in one file."
- **URL:** https://docs.openclaw.ai/install/render
- **Who runs it:** A third-party host the user rents, running the user Gateway.
- **Depends on (page's own requirements section):** A Render account (free tier available); An API key from your preferred model provider

#### Upstash Box
- **What it does (docs):** "Host OpenClaw on Upstash Box with keep-alive and SSH tunnel access" / "Run a persistent OpenClaw Gateway on Upstash Box, a managed Linux environment with keep-alive lifecycle support."
- **URL:** https://docs.openclaw.ai/install/upstash
- **Who runs it:** A third-party host the user rents, running the user Gateway.
- **Depends on (page's own requirements section):** Upstash account; Keep-alive Upstash Box; SSH client on your local machine

**Nav subgroup: Cloud servers**

#### Azure
- **What it does (docs):** "Run OpenClaw Gateway 24/7 on an Azure Linux VM with durable state" / "Set up an Azure Linux VM with the Azure CLI, apply Network Security Group (NSG) hardening, configure Azure Bastion for SSH access, and install OpenClaw."
- **URL:** https://docs.openclaw.ai/install/azure
- **Who runs it:** A third-party host the user rents, running the user Gateway.
- **Depends on (page's own requirements section):** An Azure subscription with permission to create compute and network resources; Azure CLI installed (see Azure CLI install steps); An SSH key pair (this guide covers generating one if needed); About 20-30 minutes

#### DigitalOcean
- **What it does (docs):** "Host OpenClaw on a DigitalOcean Droplet" / "Run a persistent OpenClaw Gateway on a DigitalOcean Droplet (~$6/month for the 1 GB Basic plan)."
- **URL:** https://docs.openclaw.ai/install/digitalocean
- **Who runs it:** A third-party host the user rents, running the user Gateway.
- **Depends on (page's own requirements section):** DigitalOcean account (signup); SSH key pair (or willingness to use password auth); About 20 minutes
- **Status (maturity scorecard, which links this page):** "Linux Gateway host" surface, M4 Stable (area: Deployment Targets). Source: https://docs.openclaw.ai/maturity/taxonomy

#### GCP
- **What it does (docs):** "Run OpenClaw Gateway 24/7 on a GCP Compute Engine VM with Docker" / "Run a persistent OpenClaw Gateway on a Debian Compute Engine VM. This page covers GCP provisioning, network access, and machine operations; the shared Docker VM runtime page owns container setup, persistence, custom binaries, verification, and updates."
- **URL:** https://docs.openclaw.ai/install/gcp
- **Who runs it:** A third-party host the user rents, running the user Gateway.
- **Depends on (page's own requirements section):** A GCP project with billing enabled; The `gcloud` CLI or the Cloud Console; SSH access from your laptop; Model and optional channel credentials

#### Hetzner
- **What it does (docs):** "Run OpenClaw Gateway 24/7 on a Hetzner VPS with Docker" / "Run a persistent OpenClaw Gateway on a Debian or Ubuntu Hetzner VPS. This page covers Hetzner provisioning, host security, and access; the shared Docker VM runtime page owns container setup, persistence, custom binaries, verification, and updates."
- **URL:** https://docs.openclaw.ai/install/hetzner
- **Who runs it:** A third-party host the user rents, running the user Gateway.
- **Depends on (page's own requirements section):** A Hetzner VPS with root access; SSH access from your laptop; A Hetzner Cloud Firewall or host firewall; Model and optional channel credentials
- **Status (maturity scorecard, which links this page):** "Containers and cloud execution" surface, M3 Beta (area: Container Operations); "Linux Gateway host" surface, M4 Stable (area: Deployment Targets). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Hostinger
- **What it does (docs):** "Host OpenClaw on Hostinger" / "Run a persistent OpenClaw Gateway on Hostinger. Choose a **1-Click** managed deployment, or a **VPS** install you administer yourself."
- **URL:** https://docs.openclaw.ai/install/hostinger
- **Who runs it:** A third-party host the user rents, running the user Gateway.
- **Depends on (page's own requirements section):** Hostinger account (signup); About 5-10 minutes
- **Status (maturity scorecard, which links this page):** "Containers and cloud execution" surface, M3 Beta (area: Container Operations). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Oracle Cloud
- **What it does (docs):** "Host OpenClaw on Oracle Cloud's Always Free ARM tier" / "Run a persistent OpenClaw Gateway on Oracle Cloud's **Always Free** ARM tier (up to 4 OCPU, 24 GB RAM, 200 GB storage) at no cost."
- **URL:** https://docs.openclaw.ai/install/oracle
- **Who runs it:** A third-party host the user rents, running the user Gateway.
- **Depends on (page's own requirements section):** Oracle Cloud account (signup) -- see community signup guide if you hit issues; Tailscale account (free at tailscale.com); An SSH key pair; About 30 minutes

**Nav subgroup: Self-hosted and local**

#### Ansible
- **What it does (docs):** "Automated, hardened OpenClaw installation with Ansible, Tailscale VPN, and firewall isolation" / "Deploy OpenClaw to production servers with **openclaw-ansible**, an automated installer with a security-first architecture."
- **URL:** https://docs.openclaw.ai/install/ansible
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Docker VM runtime
- **What it does (docs):** "Shared Docker VM runtime steps for long-lived OpenClaw Gateway hosts" / "Use this runtime flow after provisioning a VM and installing Docker. Provider guides such as GCP and Hetzner own VM creation, firewall rules, SSH access, and the tunnel back to your laptop."
- **URL:** https://docs.openclaw.ai/install/docker-vm-runtime
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** A Debian or Ubuntu VM with Docker Engine and Docker Compose v2; At least 6 GB RAM for a source image build; smaller hosts should use the; The OpenClaw source checkout on the VM; Provider and model credentials for onboarding
- **Status (maturity scorecard, which links this page):** "Containers and cloud execution" surface, M3 Beta (area: Agent Sandbox and Tooling, Container Operations). Source: https://docs.openclaw.ai/maturity/taxonomy

#### NVIDIA Jetson
- **What it does (docs):** "Jetson-specific preparation for hosting an OpenClaw Gateway on Linux ARM64" / "Run OpenClaw on a Jetson using the standard Linux installation. Start with a cloud model provider; running a local model server is a separate setup with its own memory and GPU requirements."
- **URL:** https://docs.openclaw.ai/install/jetson
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Kubernetes
- **What it does (docs):** "Deploy OpenClaw Gateway to a Kubernetes cluster with Kustomize" / "A minimal starting point for running OpenClaw on Kubernetes, not a production-ready deployment. It covers the core resources and is meant to be adapted to your environment."
- **URL:** https://docs.openclaw.ai/install/kubernetes
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** A running Kubernetes cluster (AKS, EKS, GKE, k3s, kind, OpenShift, etc.); `kubectl` connected to your cluster; An API key for at least one model provider
- **Status (maturity scorecard, which links this page):** "Kubernetes hosting" surface, M2 Alpha (area: Access and Exposure, Cluster Lifecycle); "Linux Gateway host" surface, M4 Stable (area: Deployment Targets). Source: https://docs.openclaw.ai/maturity/taxonomy

#### macOS VMs
- **What it does (docs):** "Run OpenClaw in a sandboxed macOS VM (local or hosted) when you need isolation or iMessage" / "Use a macOS VM only when you specifically need macOS-only capabilities such as iMessage, or want strict isolation from your daily Mac."
- **URL:** https://docs.openclaw.ai/install/macos-vm
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Raspberry Pi
- **What it does (docs):** "Host OpenClaw on a Raspberry Pi for always-on self-hosting" / "Run a persistent, always-on OpenClaw Gateway on a Raspberry Pi. Since the Pi is just the gateway (models run in the cloud via API), even a modest Pi handles the workload well -- typical hardware cost is **$35-80 one-time**, no monthly fees."
- **URL:** https://docs.openclaw.ai/install/raspberry-pi
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** Raspberry Pi 4 or 5 with 2 GB+ RAM (4 GB recommended); MicroSD card (16 GB+) or USB SSD (better performance); Official Pi power supply; Network connection (Ethernet or WiFi)
- **Status (maturity scorecard, which links this page):** "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Gateway Runtime, Performance and Diagnostics). Source: https://docs.openclaw.ai/maturity/taxonomy

**Group: Advanced setup**

#### Setup
- **What it does (docs):** "Advanced setup and development workflows for OpenClaw" / "If you are setting up for the first time, start with Getting Started. For onboarding details, see Onboarding (CLI)."
- **URL:** https://docs.openclaw.ai/start/setup
- **Who runs it:** User machine (the Gateway host or a client of it).

### Tab: Channels

**Group: Overview**

#### Chat channels
- **What it does (docs):** "Messaging platforms OpenClaw can connect to" / "OpenClaw can talk to you on any chat app you already use. Each channel connects via the Gateway."
- **URL:** https://docs.openclaw.ai/channels
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Status (maturity scorecard, which links this page):** "Channel framework" surface, M3 Beta (area: Channel Setup); "Google Chat" surface, M2 Alpha (area: Channel Setup and Operations); "Regional channel cohort" surface, M2 Alpha (area: Channel Setup and Operations). Source: https://docs.openclaw.ai/maturity/taxonomy

**Group: Mainstream messaging**

#### Discord
- **What it does (docs):** "Discord bot setup, config keys, components, voice, and troubleshooting" / "OpenClaw connects to Discord as a bot over the official Discord gateway. DMs and guild channels are supported."
- **URL:** https://docs.openclaw.ai/channels/discord
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status (maturity scorecard, which links this page):** "Discord" surface, M4 Stable (area: Access and Identity, Channel Setup and Operations); "Automation and durable work" surface, M3 Beta (area: Cron Jobs); "Channel framework" surface, M3 Beta (area: Channel Actions Commands and Approvals, Conversation Routing and Delivery); "Media understanding and media generation" surface, M2 Alpha (area: Channel Media Handling, Text-to-Speech Delivery); plus 2 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Discord setup (https://docs.openclaw.ai/channels/discord/setup); Discord access control (https://docs.openclaw.ai/channels/discord/access-control); Discord message behavior (https://docs.openclaw.ai/channels/discord/messaging); Discord threads and sessions (https://docs.openclaw.ai/channels/discord/threads-and-sessions); Discord components and approvals (https://docs.openclaw.ai/channels/discord/rich-messages); Discord events and operations (https://docs.openclaw.ai/channels/discord/events); Discord voice channels (https://docs.openclaw.ai/channels/discord/voice-channels); Discord voice transcripts and meeting notes (https://docs.openclaw.ai/channels/discord/voice-transcripts); Follow users in Discord voice (https://docs.openclaw.ai/channels/discord/voice-follow); Discord troubleshooting (https://docs.openclaw.ai/channels/discord/troubleshooting); Discord Activities (https://docs.openclaw.ai/channels/discord-activities)

#### Google Chat
- **What it does (docs):** "Google Chat app support status, capabilities, and configuration" / "Google Chat runs as the official `@openclaw/googlechat` plugin: DMs and spaces through Google Chat API webhooks (HTTP endpoint only, no Pub/Sub)."
- **URL:** https://docs.openclaw.ai/channels/googlechat
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status (maturity scorecard, which links this page):** "Google Chat" surface, M2 Alpha (area: Access and Identity, Channel Setup and Operations); "Channel framework" surface, M3 Beta (area: Channel Actions Commands and Approvals, Media Attachments and Rich Channel Data). Source: https://docs.openclaw.ai/maturity/taxonomy

#### iMessage
- **What it does (docs):** "Native iMessage support via imsg (JSON-RPC over stdio), with private API actions for replies, tapbacks, effects, polls, attachments, and group management. Preferred for new OpenClaw iMessage setups when host requirements fit." / "For the usual OpenClaw iMessage deployment, run the Gateway and `imsg` on the same signed-in macOS Messages host. If your Gateway runs elsewhere, point `channels.imessage.cliPath` at a transparent SSH wrapper that runs `imsg` on the Mac."
- **URL:** https://docs.openclaw.ai/channels/imessage
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status (maturity scorecard, which links this page):** "iMessage" surface, M3 Beta (area: Access and Identity, Channel Setup and Operations). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: native external CLI integration."
- **Sub-pages in the nav:** iMessage setup (https://docs.openclaw.ai/channels/imessage/setup); Enabling the imsg private API (https://docs.openclaw.ai/channels/imessage/private-api); iMessage access control and routing (https://docs.openclaw.ai/channels/imessage/access-control); iMessage deployment patterns (https://docs.openclaw.ai/channels/imessage/deployment); iMessage media and attachments (https://docs.openclaw.ai/channels/imessage/media); iMessage private API actions (https://docs.openclaw.ai/channels/imessage/rich-messages); iMessage message behavior (https://docs.openclaw.ai/channels/imessage/messaging); iMessage troubleshooting (https://docs.openclaw.ai/channels/imessage/troubleshooting); Coming from BlueBubbles (https://docs.openclaw.ai/channels/imessage-from-bluebubbles); BlueBubbles removal and the imsg iMessage path (https://docs.openclaw.ai/announcements/bluebubbles-imessage)

#### Matrix
- **What it does (docs):** "Matrix support status, setup, and configuration examples" / "Matrix is a downloadable channel plugin (`@openclaw/matrix`) built on the official `matrix-js-sdk`. It supports DMs, rooms, threads, media, reactions, polls, location, and E2EE."
- **URL:** https://docs.openclaw.ai/channels/matrix
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status (maturity scorecard, which links this page):** "Matrix" surface, M2 Alpha (area: Access and Identity, Channel Setup and Operations); "Channel framework" surface, M3 Beta (area: Channel Actions Commands and Approvals, Conversation Routing and Delivery). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Matrix setup (https://docs.openclaw.ai/channels/matrix/setup); Matrix access control (https://docs.openclaw.ai/channels/matrix/access-control); Matrix message behavior (https://docs.openclaw.ai/channels/matrix/messaging); Matrix rich messages and approvals (https://docs.openclaw.ai/channels/matrix/rich-messages); Matrix encryption and verification (https://docs.openclaw.ai/channels/matrix/encryption); Matrix threads and sessions (https://docs.openclaw.ai/channels/matrix/threads-and-sessions); Matrix accounts and homeservers (https://docs.openclaw.ai/channels/matrix/accounts-and-homeservers); Matrix migration (https://docs.openclaw.ai/channels/matrix-migration); Matrix presentation metadata (https://docs.openclaw.ai/channels/matrix-presentation); Matrix push rules for quiet previews (https://docs.openclaw.ai/channels/matrix-push-rules)

#### Microsoft Teams
- **What it does (docs):** "Microsoft Teams bot support status, capabilities, and configuration" / "Status: text + DM attachments are supported; channel/group file sending requires Graph permissions; standard channels resolve their team site automatically, while group chats require `sharePointSiteId` (see Sending files in group chats). Polls and approval prompts are sent via Adaptive Cards."
- **URL:** https://docs.openclaw.ai/channels/msteams
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status (maturity scorecard, which links this page):** "Microsoft Teams" surface, M2 Alpha (area: Access and Identity, Channel Setup and Operations); "Automation and durable work" surface, M3 Beta (area: Polling Controls). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Microsoft Teams setup (https://docs.openclaw.ai/channels/msteams/setup); Microsoft Teams access control (https://docs.openclaw.ai/channels/msteams/access-control); Microsoft Teams authentication (https://docs.openclaw.ai/channels/msteams/authentication); Microsoft Teams manifest and permissions (https://docs.openclaw.ai/channels/msteams/manifest-and-permissions); Microsoft Teams configuration (https://docs.openclaw.ai/channels/msteams/configuration); Microsoft Teams message behavior (https://docs.openclaw.ai/channels/msteams/messaging); Microsoft Teams cards and actions (https://docs.openclaw.ai/channels/msteams/cards-and-actions); Microsoft Teams troubleshooting (https://docs.openclaw.ai/channels/msteams/troubleshooting)

#### Signal
- **What it does (docs):** "Signal support via signal-cli (native daemon or bbernhard container), setup paths, and number model" / "Signal is a downloadable channel plugin (`@openclaw/signal`). The gateway talks to `signal-cli` over HTTP: either the native daemon (JSON-RPC + SSE) or the bbernhard/signal-cli-rest-api container (REST + WebSocket)."
- **URL:** https://docs.openclaw.ai/channels/signal
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status (maturity scorecard, which links this page):** "Signal" surface, M2 Alpha (area: Access and Identity, Channel Setup and Operations); "Channel framework" surface, M3 Beta (area: Channel Actions Commands and Approvals, Media Attachments and Rich Channel Data). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Slack
- **What it does (docs):** "Slack setup and runtime behavior (Socket Mode, HTTP Request URLs, and relay mode)" / "Slack support covers DMs and channels via Slack app integrations. Default transport is Socket Mode."
- **URL:** https://docs.openclaw.ai/channels/slack
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status (maturity scorecard, which links this page):** "Slack" surface, M3 Beta (area: Access and Identity, Channel Setup and Operations). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Slack setup (https://docs.openclaw.ai/channels/slack/setup); Slack transports (https://docs.openclaw.ai/channels/slack/transports); Slack Enterprise Grid (https://docs.openclaw.ai/channels/slack/enterprise-grid); Slack manifest and scopes (https://docs.openclaw.ai/channels/slack/manifest-and-scopes); Slack access control (https://docs.openclaw.ai/channels/slack/access-control); Slack threads and sessions (https://docs.openclaw.ai/channels/slack/threads-and-sessions); Slack message behavior (https://docs.openclaw.ai/channels/slack/messaging); Slack media and attachments (https://docs.openclaw.ai/channels/slack/media); Slack charts, tables, and approvals (https://docs.openclaw.ai/channels/slack/rich-messages); Slack events and operations (https://docs.openclaw.ai/channels/slack/events); Slack troubleshooting (https://docs.openclaw.ai/channels/slack/troubleshooting)

#### SMS
- **What it does (docs):** "Twilio SMS/MMS setup, access controls, webhooks, and delivery status" / "OpenClaw receives and sends SMS/MMS through a Twilio phone number or Messaging Service. The Gateway registers a webhook route (default `/webhooks/sms`), validates Twilio request signatures by default, sends replies through Twilio's Messages API, and records outbound delivery callbacks."
- **URL:** https://docs.openclaw.ai/channels/sms
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Depends on (page's own requirements section):** The official SMS plugin installed with `openclaw plugins install @openclaw/sms`.; A Twilio account with an SMS-capable phone number, or a Twilio Messaging Service. MMS requires an MMS-capable sender; native MMS delivery also depends on the de; The Twilio Account SID and Auth Token.; A public HTTPS URL that reaches your OpenClaw Gateway.
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: official plugin, installed separately."

#### Telegram
- **What it does (docs):** "Telegram bot support status, capabilities, and configuration" / "This page connects a Telegram bot to OpenClaw and sets who is allowed to message it."
- **URL:** https://docs.openclaw.ai/channels/telegram
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** bundled plugin
- **Status (maturity scorecard, which links this page):** "Telegram" surface, M3 Beta (area: Access and Identity, Channel Setup and Operations); "Automation and durable work" surface, M3 Beta (area: Event Ingress, Polling Controls); "Observability" surface, M3 Beta (area: Health and Repair); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Channel Access Control). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Telegram setup (https://docs.openclaw.ai/channels/telegram/setup); Telegram access control (https://docs.openclaw.ai/channels/telegram/access-control); Telegram message behavior (https://docs.openclaw.ai/channels/telegram/messaging); Telegram threads and sessions (https://docs.openclaw.ai/channels/telegram/threads-and-sessions); Telegram rich messages and approvals (https://docs.openclaw.ai/channels/telegram/rich-messages); Telegram media and attachments (https://docs.openclaw.ai/channels/telegram/media); Telegram events and operations (https://docs.openclaw.ai/channels/telegram/events); Telegram transports (https://docs.openclaw.ai/channels/telegram/transports); Telegram Control UI Mini App (https://docs.openclaw.ai/channels/telegram/mini-app); Telegram troubleshooting (https://docs.openclaw.ai/channels/telegram/troubleshooting)

#### WhatsApp
- **What it does (docs):** "WhatsApp channel support, access controls, delivery behavior, and operations" / "Status: production-ready via WhatsApp Web (Baileys). The gateway owns the linked session(s); there is no separate Twilio WhatsApp channel."
- **URL:** https://docs.openclaw.ai/channels/whatsapp
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status (maturity scorecard, which links this page):** "WhatsApp" surface, M3 Beta (area: Access and Identity, Channel Setup and Operations); "Media understanding and media generation" surface, M2 Alpha (area: Media Intake and Access, Media Understanding). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: production-ready via WhatsApp Web (Baileys)."

#### X / Twitter
- **What it does (docs):** "X / Twitter mentions, allowlisted public replies, thread context, and event modes" / "The X plugin turns mentions of your bot account into agent conversations and posts the agent's answer as a public reply. Only allowlisted authors can trigger a reply by default."
- **URL:** https://docs.openclaw.ai/channels/x
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** bundled plugin

**Group: Developer and self-hosted**

#### A2A
- **What it does (docs):** "Connect external agents to OpenClaw through the A2A 1.0 JSON-RPC protocol" / "The A2A channel plugin connects OpenClaw to other agents through the Linux Foundation Agent2Agent protocol. External agents discover the gateway through a public Agent Card and submit authenticated text tasks using the A2A 1.0 JSON-RPC binding."
- **URL:** https://docs.openclaw.ai/channels/a2a
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** bundled plugin
- **Status (maturity scorecard, which links this page):** "External apps and interoperability" surface, M2 Alpha (area: Compatibility). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Buzz
- **What it does (docs):** "Connect OpenClaw agents to Buzz rooms" / "Buzz is an official channel plugin that connects OpenClaw agents to team rooms in a hosted or self-hosted Buzz workspace."
- **URL:** https://docs.openclaw.ai/channels/buzz
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin

#### ClickClack
- **What it does (docs):** "ClickClack bot-token channel setup and target syntax" / "ClickClack connects OpenClaw to a self-hosted ClickClack workspace through first-class ClickClack bot tokens."
- **URL:** https://docs.openclaw.ai/channels/clickclack
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin

#### IRC
- **What it does (docs):** "IRC plugin setup, access controls, and troubleshooting" / "Use IRC when you want OpenClaw in classic channels (`#room`) and direct messages. Install the official IRC plugin, then configure it under `channels.irc`."
- **URL:** https://docs.openclaw.ai/channels/irc
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin

#### Mattermost
- **What it does (docs):** "Mattermost bot setup and OpenClaw config" / "Status: downloadable plugin (bot token + WebSocket events). Channels, private channels, group DMs, and DMs are supported."
- **URL:** https://docs.openclaw.ai/channels/mattermost
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: downloadable plugin (bot token + WebSocket events)."

#### Nextcloud Talk
- **What it does (docs):** "Nextcloud Talk support status, capabilities, and configuration" / "Nextcloud Talk is a downloadable channel plugin (`@openclaw/nextcloud-talk`) that connects OpenClaw to a self-hosted Nextcloud instance through a Talk webhook bot. Direct messages, rooms, reactions, markdown messages, and inbound and outbound Talk file shares are supported."
- **URL:** https://docs.openclaw.ai/channels/nextcloud-talk
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin

#### Nostr
- **What it does (docs):** "Nostr DM channel via NIP-04 encrypted messages" / "Nostr is a downloadable channel plugin (`@openclaw/nostr`) that lets OpenClaw receive and answer NIP-04 encrypted direct messages over Nostr relays. One account per gateway; DMs only."
- **URL:** https://docs.openclaw.ai/channels/nostr
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin

#### Raft
- **What it does (docs):** "Raft External Agent support through the Raft CLI wake bridge" / "Raft connects an OpenClaw agent to a Raft External Agent through the local Raft CLI. Raft sends authenticated wake hints to the Gateway; the agent then uses the Raft CLI to check and send messages."
- **URL:** https://docs.openclaw.ai/channels/raft
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Depends on (page's own requirements section):** A Raft workspace with an External Agent.; The Raft CLI installed on the same host as the OpenClaw Gateway, on the; A Raft CLI profile that is already signed in and associated with that

#### Reef
- **What it does (docs):** "Reef channel setup: guarded, end-to-end-encrypted messaging between OpenClaw agents of different people" / "Reef is a guarded, end-to-end-encrypted side channel between OpenClaw agents owned by different people. Messages are sealed on your machine and screened by a pinned-model guard in both directions."
- **URL:** https://docs.openclaw.ai/channels/reef
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** bundled plugin

#### Synology Chat
- **What it does (docs):** "Synology Chat webhook setup and OpenClaw config" / "Synology Chat connects to OpenClaw through a webhook pair: a Synology Chat outgoing webhook posts inbound direct messages to the Gateway, and replies go back through a Synology Chat incoming webhook."
- **URL:** https://docs.openclaw.ai/channels/synology-chat
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: official plugin, installed separately."

#### Tlon
- **What it does (docs):** "Tlon/Urbit support status, capabilities, and configuration" / "Tlon is a decentralized messenger built on Urbit. OpenClaw connects to your Urbit ship and responds to DMs and group chat messages."
- **URL:** https://docs.openclaw.ai/channels/tlon
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: bundled plugin."

#### Twitch
- **What it does (docs):** "Twitch chat bot: install, credentials, access control, token refresh" / "Twitch chat support over Twitch's chat (IRC) interface via the Twurple client. OpenClaw signs in as a Twitch bot account, joins one channel per configured account, and replies in that channel."
- **URL:** https://docs.openclaw.ai/channels/twitch
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin

**Group: Regional platforms**

#### Feishu
- **What it does (docs):** "Feishu bot overview, features, and configuration" / "OpenClaw connects to Feishu/Lark (the all-in-one collaboration platform) through the official `@openclaw/feishu` plugin: bot DMs, group chats, streaming card replies, and Feishu doc/wiki/drive/Bitable tools."
- **URL:** https://docs.openclaw.ai/channels/feishu
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: production-ready for bot DMs + group chats."
- **Sub-pages in the nav:** Feishu setup (https://docs.openclaw.ai/channels/feishu/setup); Feishu access control (https://docs.openclaw.ai/channels/feishu/access-control); Feishu advanced configuration (https://docs.openclaw.ai/channels/feishu/advanced-configuration); Feishu dynamic agents (https://docs.openclaw.ai/channels/feishu/dynamic-agents); Feishu message types (https://docs.openclaw.ai/channels/feishu/messaging); Feishu configuration reference (https://docs.openclaw.ai/channels/feishu/configuration-reference); Feishu troubleshooting (https://docs.openclaw.ai/channels/feishu/troubleshooting)

#### LINE
- **What it does (docs):** "LINE Messaging API plugin setup, config, and usage" / "LINE connects to OpenClaw via the LINE Messaging API. The plugin runs as a webhook receiver on the Gateway and uses your channel access token + channel secret for authentication."
- **URL:** https://docs.openclaw.ai/channels/line
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status (maturity scorecard, which links this page):** "Channel framework" surface, M3 Beta (area: Inbound Access and Identity Gates, Media Attachments and Rich Channel Data); "Media understanding and media generation" surface, M2 Alpha (area: Media Intake and Access). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: official plugin, installed separately."

#### QQ bot
- **What it does (docs):** "QQ Bot setup, config, and usage" / "QQ Bot connects to OpenClaw via the official QQ Bot API (WebSocket gateway). C2C private chat and group `@`-mentions are the primary chat types, with rich media (images, voice, video, files)."
- **URL:** https://docs.openclaw.ai/channels/qqbot
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: official downloadable plugin."

#### WeChat
- **What it does (docs):** "WeChat channel setup through the external openclaw-weixin plugin" / "OpenClaw connects to WeChat through Tencent's external `@tencent-weixin/openclaw-weixin` channel plugin."
- **URL:** https://docs.openclaw.ai/channels/wechat
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** external plugin
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: external plugin, maintained by the Tencent Weixin team."

#### WeCom
- **What it does (docs):** "Install the external WeCom plugin and find its versioned setup documentation" / "OpenClaw exposes WeCom through the external `@wecom/wecom-openclaw-plugin` package maintained by the Tencent WeCom team. The plugin is listed in OpenClaw's official channel catalog but is not bundled with the core install."
- **URL:** https://docs.openclaw.ai/channels/wecom
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** external plugin

#### Yuanbao
- **What it does (docs):** "Yuanbao bot overview, features, and configuration" / "Tencent Yuanbao is Tencent's AI assistant platform. The community-maintained `openclaw-plugin-yuanbao` plugin connects Yuanbao bots to OpenClaw over WebSocket for direct messages and group chats."
- **URL:** https://docs.openclaw.ai/channels/yuanbao
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** external plugin
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: production-ready for bot DMs and group chats."

#### Zalo
- **What it does (docs):** "Zalo bot support status, capabilities, and configuration" / "Status: experimental. Direct messages and group chats are both implemented."
- **URL:** https://docs.openclaw.ai/channels/zalo
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Event Ingress). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: experimental."

#### Zalo ClawBot
- **What it does (docs):** "Zalo ClawBot channel setup through the external openclaw-zaloclawbot plugin" / "OpenClaw connects to Zalo ClawBot through the catalog-listed external `@zalo-platforms/openclaw-zaloclawbot` plugin. Login uses a Zalo Mini App QR code; the plugin id in config is `openclaw-zaloclawbot`."
- **URL:** https://docs.openclaw.ai/channels/zaloclawbot
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** external plugin
- **Depends on (page's own requirements section):** Node.js >= 22; OpenClaw installed (`openclaw` CLI available); A Zalo account on a mobile device to scan the login QR code

#### Zalo personal
- **What it does (docs):** "Zalo personal account support via native zca-js (QR login), capabilities, and configuration" / "Status: experimental. This integration automates a **personal Zalo account** via native `zca-js`, in-process, with no external CLI binary."
- **URL:** https://docs.openclaw.ai/channels/zalouser
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Packaging (docs):** official plugin
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: experimental."

**Group: Configuration**

#### Pairing
- **What it does (docs):** "Pairing overview: approve who can DM you + which nodes can join" / ""Pairing" is OpenClaw's explicit access approval step. It is used in two places:"
- **URL:** https://docs.openclaw.ai/channels/pairing
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Status (maturity scorecard, which links this page):** "Security, auth, pairing, and secrets" surface, M3 Beta (area: Channel Access Control, Device and Node Pairing); "Channel framework" surface, M3 Beta (area: Channel Setup); "Discord" surface, M4 Stable (area: Access and Identity); "Google Chat" surface, M2 Alpha (area: Access and Identity); plus 6 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy

#### Access groups
- **What it does (docs):** "Reusable sender allowlists for message channels" / "Access groups are named sender lists you define once under `accessGroups` and reference from channel allowlists with `accessGroup:`."
- **URL:** https://docs.openclaw.ai/channels/access-groups
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Status (maturity scorecard, which links this page):** "Channel framework" surface, M3 Beta (area: Inbound Access and Identity Gates); "Discord" surface, M4 Stable (area: Access and Identity, Conversation Routing and Delivery); "Google Chat" surface, M2 Alpha (area: Access and Identity, Conversation Routing and Delivery); "Microsoft Teams" surface, M2 Alpha (area: Access and Identity); plus 2 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy

#### Bot loop protection
- **What it does (docs):** "Bot-to-bot loop protection defaults and channel overrides" / "OpenClaw can accept messages written by other bots on channels that support `allowBots`, and on Telegram, which has no `allowBots` and admits another bot through the same sender checks as a person. Discord, Mattermost, and Slack default to accepting them under the normal mention and access rules; an explicit `allowBots: false` still disables ..."
- **URL:** https://docs.openclaw.ai/channels/bot-loop-protection
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Status (maturity scorecard, which links this page):** "Google Chat" surface, M2 Alpha (area: Access and Identity, Conversation Routing and Delivery); "Matrix" surface, M2 Alpha (area: Access and Identity); "Slack" surface, M3 Beta (area: Conversation Routing and Delivery). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Groups
- **What it does (docs):** "Group chat behavior across surfaces (Discord/iMessage/Matrix/Microsoft Teams/QQBot/Signal/Slack/Telegram/WhatsApp/Zalo)" / "OpenClaw applies the same group rules across group-capable channels, including Discord, iMessage, Matrix, Microsoft Teams, QQBot, Signal, Slack, Telegram, WhatsApp, and Zalo."
- **URL:** https://docs.openclaw.ai/channels/groups
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Status (maturity scorecard, which links this page):** "Channel framework" surface, M3 Beta (area: Channel Actions Commands and Approvals, Conversation Routing and Delivery); "Discord" surface, M4 Stable (area: Access and Identity, Conversation Routing and Delivery); "Matrix" surface, M2 Alpha (area: Access and Identity); "Microsoft Teams" surface, M2 Alpha (area: Conversation Routing and Delivery); plus 1 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy

#### WhatsApp group messages
- **What it does (docs):** "WhatsApp group message handling — activation, allowlists, sessions, and context injection" / "For the cross-channel groups model (Discord, iMessage, Matrix, Microsoft Teams, QQBot, Signal, Slack, Telegram, WhatsApp, Zalo), see Groups. This page covers the WhatsApp-specific behavior on top of that model: activation, group allowlists, per-group session keys, and pending-message context injection."
- **URL:** https://docs.openclaw.ai/channels/group-messages
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Status (maturity scorecard, which links this page):** "WhatsApp" surface, M3 Beta (area: Conversation Routing and Delivery); "Channel framework" surface, M3 Beta (area: Group Thread and Ambient Room Behavior). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Ambient room events
- **What it does (docs):** "Let supported group rooms provide quiet context unless the agent sends with the message tool" / "Ambient room events let OpenClaw process unmentioned group or channel chatter as quiet context. The agent can update memory and session state, but the room stays silent unless the agent explicitly calls the `message` tool."
- **URL:** https://docs.openclaw.ai/channels/ambient-room-events
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Depends on (page's own requirements section):** Mention gating must be off for the room. `requireMention: true` drops unmentioned messages before routing, so they never become room events. The agent then has ; The agent needs the `message` tool. Room events use strict visible delivery, so posting requires `message(action=send)`. The `message` tool ships in the `messag
- **Status (maturity scorecard, which links this page):** "Channel framework" surface, M3 Beta (area: Group Thread and Ambient Room Behavior, Outbound Delivery and Reply Pipeline). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Broadcast groups
- **What it does (docs):** "Run bounded agent group threads across messaging channels" / "Agent group threads run **multiple agents** on the same inbound message, using the top-level `broadcast` config. Each agent runs in its own session."
- **URL:** https://docs.openclaw.ai/channels/broadcast-groups
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Page status field:** `experimental`
- **Status (maturity scorecard, which links this page):** "Channel framework" surface, M3 Beta (area: Group Thread and Ambient Room Behavior). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: Experimental."

#### Channel routing
- **What it does (docs):** "How OpenClaw picks an agent and session for each inbound message, and how replies route back" / "OpenClaw routes replies **back to the channel where a message came from**. The model does not choose a channel; routing follows fixed rules controlled by the host configuration."
- **URL:** https://docs.openclaw.ai/channels/channel-routing
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Status (maturity scorecard, which links this page):** "Channel framework" surface, M3 Beta (area: Conversation Routing and Delivery); "Control UI" surface, M3 Beta (area: WebChat Conversations); "Discord" surface, M4 Stable (area: Conversation Routing and Delivery); "Google Chat" surface, M2 Alpha (area: Access and Identity, Conversation Routing and Delivery); plus 2 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy

#### Channel location parsing
- **What it does (docs):** "Channel location parsing and portable outbound location payloads" / "OpenClaw normalizes shared locations from chat channels into:"
- **URL:** https://docs.openclaw.ai/channels/location
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Status (maturity scorecard, which links this page):** "Telegram" surface, M3 Beta (area: Media and Rich Content). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Channel troubleshooting
- **What it does (docs):** "Fast channel level troubleshooting with per channel failure signatures and fixes" / "Use this page when a channel connects but behavior is wrong."
- **URL:** https://docs.openclaw.ai/channels/troubleshooting
- **Who runs it:** Channel plugin runs in the user Gateway; it connects to the third-party messaging service.
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Event Ingress); "Channel framework" surface, M3 Beta (area: Channel Setup, Conversation Routing and Delivery); "Slack" surface, M3 Beta (area: Channel Setup and Operations). Source: https://docs.openclaw.ai/maturity/taxonomy

### Tab: Agents

**Group: Agent runtime**

#### Gateway architecture
- **What it does (docs):** "WebSocket gateway architecture, components, and client flows" / "Baileys, Telegram via grammY, Slack, Discord, Signal, iMessage, WebChat). - Control-plane clients (macOS app, CLI, web UI, automations) connect to the Gateway over **WebSocket** on the configured bind host (default `127.0.0.1:18789`)."
- **URL:** https://docs.openclaw.ai/concepts/architecture
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Gateway runtime" surface, M4 Stable (area: Gateway Lifecycle, Gateway RPC APIs and Events). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Agent runtime
- **What it does (docs):** "Agent runtime, workspace contract, and session bootstrap" / "OpenClaw ships one **embedded agent runtime**: a built-in agent loop, tool wiring, and prompt assembly, distinct from delegating turns to an external harness process. Each configured agent (see Multi-agent routing for running several) has its own workspace, bootstrap files, and session store."
- **URL:** https://docs.openclaw.ai/concepts/agent
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Agent loop
- **What it does (docs):** "Agent loop lifecycle, streams, and wait semantics" / "The agent loop is the serialized, per-session run that turns a message into actions and a reply: intake, context assembly, model inference, tool execution, streaming, persistence."
- **URL:** https://docs.openclaw.ai/concepts/agent-loop
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Agent Runtime" surface, M3 Beta (area: Agent Turn Execution, Streaming and Progress). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Agent runtimes
- **What it does (docs):** "How OpenClaw separates model providers, models, channels, and agent runtimes" / "An **agent runtime** owns one prepared model loop: it receives the prompt, drives model output, handles native tool calls, and returns the finished turn to OpenClaw."
- **URL:** https://docs.openclaw.ai/concepts/agent-runtimes
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Agent Runtime" surface, M3 Beta (area: Agent Turn Execution, External Runtimes and Subagents). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "was removed"; may describe a sub-feature):** "Legacy codex-cli/ model refs repair to the same openai/ Codex app-server route; The bundled Codex CLI backend was removed in v2026."

#### System prompt
- **What it does (docs):** "What the OpenClaw system prompt contains and how it is assembled" / "OpenClaw owns the system prompt for every agent run; there is no runtime default prompt. Runtime adapters can reuse session preparation while applying current turn context and explicit refreshes."
- **URL:** https://docs.openclaw.ai/concepts/system-prompt
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Context
- **What it does (docs):** "Context: what the model sees, how it is built, and how to inspect it" / ""Context" is **everything OpenClaw sends to the model for a run**. It is bounded by the model's **context window** (token limit)."
- **URL:** https://docs.openclaw.ai/concepts/context
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: Context Engine, Core Prompts and Context). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Context engine
- **What it does (docs):** "Context engine: pluggable context assembly, compaction, and subagent lifecycle" / "A **context engine** controls how OpenClaw builds model context for each run: which messages to include, how to summarize older history, and how to manage context across subagent boundaries."
- **URL:** https://docs.openclaw.ai/concepts/context-engine
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: Context Engine). Source: https://docs.openclaw.ai/maturity/taxonomy

#### SOUL.md personality guide
- **What it does (docs):** "Use SOUL.md to give your OpenClaw agent an actual voice instead of generic assistant sludge" / "`SOUL.md` is where your agent's voice lives. OpenClaw injects it into normal sessions, so it carries real weight: if your agent sounds bland, hedgy, or corporate, this is usually the file to fix."
- **URL:** https://docs.openclaw.ai/concepts/soul
- **Who runs it:** User machine (the Gateway host or a client of it).

**Group: Agent workspace**

#### Agent workspace
- **What it does (docs):** "Agent workspace: location, layout, and backup strategy" / "The workspace is the agent's home: the working directory used for file tools and workspace context. Keep it private and treat it as memory."
- **URL:** https://docs.openclaw.ai/concepts/agent-workspace
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Managed worktrees
- **What it does (docs):** "Run agent tasks in isolated git checkouts with automatic snapshots and cleanup" / "Managed worktrees give an agent task its own git branch and checkout without placing temporary directories inside the source repository. OpenClaw records them in the shared state database and snapshots their tracked and non-ignored untracked contents before ordinary removal."
- **URL:** https://docs.openclaw.ai/concepts/managed-worktrees
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Agent Runtime" surface, M3 Beta (area: Agent Turn Execution). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Storage locations
- **What it does (docs):** "Named storage destinations, explicit initialization, encryption, and provider configuration" / "A storage location names a destination for OpenClaw artifacts. Core storage owns location identity, encryption, and health checks."
- **URL:** https://docs.openclaw.ai/concepts/storage-locations
- **Who runs it:** User machine (the Gateway host or a client of it).

#### OAuth
- **What it does (docs):** "OAuth in OpenClaw: token exchange, storage, and multi-account patterns" / "In **Settings → Models**, choose **Add account** to save a provider sign-in. **Accounts** are saved ways to use a provider; API keys supplied by config or the environment remain managed at their source."
- **URL:** https://docs.openclaw.ai/concepts/oauth
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "OpenAI and Codex provider path" surface, M3 Beta (area: Model and Auth); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Credential and Secret Hygiene). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Agent bootstrapping
- **What it does (docs):** "Agent bootstrapping ritual that seeds the workspace and identity files" / "Bootstrapping is the first-run ritual that seeds a new agent workspace and walks the agent through picking an identity. It runs once, right after onboarding, on the agent's first real turn."
- **URL:** https://docs.openclaw.ai/start/bootstrapping
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Experimental features
- **What it does (docs):** "What experimental flags mean in OpenClaw and which ones are currently documented" / "Experimental features are preview surfaces controlled by config flags. They need more real-world mileage before their shape and behavior become long-lived contracts."
- **URL:** https://docs.openclaw.ai/concepts/experimental-features
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Experimental features are preview surfaces controlled by config flags."

**Group: Sessions and memory**

#### The main session
- **What it does (docs):** "One rolling conversation across all your channels: the personal-agent default" / "OpenClaw is a personal agent first. Out of the box, every direct message you send it — from Telegram, WhatsApp, iMessage, Slack DMs, the web app, anywhere — lands in **one rolling conversation**: the main session."
- **URL:** https://docs.openclaw.ai/concepts/main-session
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Multi-user mode
- **What it does (docs):** "How session ownership, presence, and human mentions work when several people operate one agent" / "Multi-user mode lets several trusted people operate the same OpenClaw agent. It adds session ownership, participant history, live presence, and owner filtering."
- **URL:** https://docs.openclaw.ai/concepts/multi-user
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Gateway runtime" surface, M4 Stable (area: Roles and Permissions). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Session management
- **What it does (docs):** "How OpenClaw manages conversation sessions" / "OpenClaw routes every inbound message to a **session** based on where it came from: DMs, group chats, cron jobs, etc. All session state is owned by the **gateway**; UI clients query the gateway for session data."
- **URL:** https://docs.openclaw.ai/concepts/session
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: CLI Session and Transcript Management, Session Routing). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "have been removed"; may describe a sub-feature):** "Channel docking and manual cross-channel reply focus have been removed."

#### Session controller
- **What it does (docs):** "Session scheduling ownership, input custody, and retained settlement" / "A session controller is the owner of **which turn may use a session next**. It coordinates accepted inputs, the current turn, and admission barriers."
- **URL:** https://docs.openclaw.ai/concepts/session-controller
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Session synchronization and attachment
- **What it does (docs):** "How Gateway-owned sessions continue across the Control UI, terminal, CLI, mobile clients, and coding harnesses" / "OpenClaw keeps shared session state on the Gateway. The Control UI, mobile clients, ACP, `openclaw tui `, and `openclaw attach ` project that Gateway-owned state instead of keeping independent session copies."
- **URL:** https://docs.openclaw.ai/concepts/session-attachment
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: Cross-client History and Session Parity). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Session search
- **What it does (docs):** "Search past session transcripts and reopen the matching context" / "`sessions_search` searches the user and assistant text in visible past sessions. Each result includes a `sessionKey`, timestamp, role, and a short matching excerpt."
- **URL:** https://docs.openclaw.ai/concepts/session-search
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Session pruning
- **What it does (docs):** "Trimming old tool results to keep context lean and caching efficient" / "Session pruning trims **old tool results** from the model's context. It reduces context bloat from accumulated tool outputs (exec results, file reads, search results) without rewriting normal conversation text."
- **URL:** https://docs.openclaw.ai/concepts/session-pruning
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Session state awareness
- **What it does (docs):** "Durable session state signal log: state versions, watchers, stale-state notices, and reconciliation" / "Several sessions often work on the same problem. Examples are a manager delegating to children, a human jumping directly into a worker session, and two agents coordinating over `sessions_send`."
- **URL:** https://docs.openclaw.ai/concepts/session-state
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Session tools
- **What it does (docs):** "Agent tools for session creation, cross-session status, recall, messaging, and sub-agent orchestration" / "OpenClaw gives agents tools to work across sessions, inspect status, and orchestrate sub-agents."
- **URL:** https://docs.openclaw.ai/concepts/session-tool
- **Who runs it:** User machine (the Gateway host or a client of it).

**Nav subgroup: Memory**

#### Memory overview
- **What it does (docs):** "How OpenClaw remembers things across sessions" / "OpenClaw remembers things by writing plain Markdown files in your agent's workspace (default `~/.openclaw/workspace`). The model only remembers what gets saved to disk; there is no hidden state."
- **URL:** https://docs.openclaw.ai/concepts/memory
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Local model providers: Ollama, vLLM, SGLang, LM Studio" surface, M2 Alpha (area: Local Memory and Embeddings); "Session, memory, and state lifecycle" surface, M3 Beta (area: Memory). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Memory architecture
- **What it does (docs):** "End-to-end architecture of OpenClaw memory: tiers, provenance, dreaming, recall lanes, the user model, and standing intents" / "Memory Core, OpenClaw's default memory plugin, uses plain files and one SQLite index, organized into tiers with different trust levels, write rules, and injection behavior. This page explains the whole system: what gets written where, how content earns its way into long-term memory, how recall works on every turn, and how the system defends itself ..."
- **URL:** https://docs.openclaw.ai/concepts/memory-architecture
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Memory provenance and deletion
- **What it does (docs):** "Trace session-derived memories, control ingestion, and preview or delete tracked memory artifacts" / "OpenClaw records source-session lineage for memories staged by automatic session ingestion and historical session backfill. `openclaw memory forget` uses that lineage to remove tracked entries and related artifacts, and records the selected sessions as forgotten so later ingestion does not restore them."
- **URL:** https://docs.openclaw.ai/concepts/memory-provenance
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: Memory). Source: https://docs.openclaw.ai/maturity/taxonomy

#### User model
- **What it does (docs):** "Manage durable user preferences and your Gateway profile identity" / "`USER.md` is the optional user-model artifact in an agent workspace. It stores stable preferences, communication style, relationships, and active-project context as directives that can guide future sessions."
- **URL:** https://docs.openclaw.ai/concepts/user-model
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Standing intents
- **What it does (docs):** "Remember event-conditioned future actions without relying on long conversational context" / "A standing intent is an event-conditioned instruction such as "when the release candidate is mentioned, remind me to verify rollback ownership." OpenClaw stores it in the owning agent's SQLite database and checks it before eligible interactive replies."
- **URL:** https://docs.openclaw.ai/concepts/standing-intents
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Builtin memory engine
- **What it does (docs):** "The default SQLite-based memory backend with keyword, vector, and hybrid search" / "The builtin engine is the default memory backend. By default, it stores your memory index in a per-agent SQLite database and needs no extra dependencies to get started."
- **URL:** https://docs.openclaw.ai/concepts/memory-builtin
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status wording (first sentence on the page with "has been removed"; may describe a sub-feature):** "QMD has been removed; builtin is the only memory engine."

#### Honcho memory
- **What it does (docs):** "AI-native cross-session memory via the Honcho plugin" / "Honcho adds AI-native memory to OpenClaw through an external plugin. It persists conversations to a dedicated service and builds user and agent models over time, giving your agent cross-session context that goes beyond workspace Markdown files."
- **URL:** https://docs.openclaw.ai/concepts/memory-honcho
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Memory search
- **What it does (docs):** "How memory search finds relevant notes using embeddings and hybrid retrieval" / "`memory_search` finds relevant notes from your memory files, even when the wording differs from the original text. It chunks memory into small pieces and searches them with embeddings, keywords, or both."
- **URL:** https://docs.openclaw.ai/concepts/memory-search
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "experimental complement."

#### Active memory
- **What it does (docs):** "Deep conversation-history recall that escalates only when rule-based memory recall is insufficient" / "Active Memory is the deep-recall lane for eligible conversational sessions. The default `escalate` mode runs its blocking recall sub-agent only when the message asks about the past and the rule-based memory lane found no strong trusted trigger match."
- **URL:** https://docs.openclaw.ai/concepts/active-memory
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Sub-pages in the nav:** Enabling active memory (https://docs.openclaw.ai/concepts/active-memory/enabling); How active memory works (https://docs.openclaw.ai/concepts/active-memory/how-it-works); Session controls (https://docs.openclaw.ai/concepts/active-memory/session-controls); Query modes, prompts, and models (https://docs.openclaw.ai/concepts/active-memory/tuning); Memory tools (https://docs.openclaw.ai/concepts/active-memory/memory-tools); Advanced overrides and transcripts (https://docs.openclaw.ai/concepts/active-memory/advanced-options); Configuration reference (https://docs.openclaw.ai/concepts/active-memory/configuration); Recommended setup (https://docs.openclaw.ai/concepts/active-memory/recommended-setup); Troubleshooting active memory (https://docs.openclaw.ai/concepts/active-memory/troubleshooting)

#### Dreaming
- **What it does (docs):** "Background memory consolidation with light, deep, and REM phases plus a Dream Diary" / "Dreaming is the background memory consolidation system in `memory-core`. It moves strong short-term signals into durable memory while keeping the process explainable and reviewable."
- **URL:** https://docs.openclaw.ai/concepts/dreaming
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Compaction
- **What it does (docs):** "How OpenClaw summarizes long conversations to stay within model limits" / "Every model has a context window: the maximum number of tokens it can process. When a conversation approaches that limit, OpenClaw **compacts** older messages into a summary so the chat can continue."
- **URL:** https://docs.openclaw.ai/concepts/compaction
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: Token Management). Source: https://docs.openclaw.ai/maturity/taxonomy

**Group: Multi-agent**

#### Multi-agent routing
- **What it does (docs):** "Multi-agent routing: agent boundaries, channel accounts, and bindings" / "Run multiple _isolated_ agents in one Gateway process, each with its own workspace, state directory (`agentDir`), and SQLite-backed session history, plus multiple channel accounts (e.g. two WhatsApp numbers)."
- **URL:** https://docs.openclaw.ai/concepts/multi-agent
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Page status field:** `active`
- **Status (maturity scorecard, which links this page):** "Telegram" surface, M3 Beta (area: Access and Identity, Conversation Routing and Delivery). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "was removed"; may describe a sub-feature):** "The QMD cross-agent search path was removed in v2026."

#### Agent bindings
- **What it does (docs):** "Route channel accounts and conversations to the right OpenClaw agent" / "When a message arrives on a channel, OpenClaw has to decide which agent answers it. An agent binding makes that choice for a slice of your traffic — each binding names an `agentId` and matches channel facts such as the account, peer, guild, team, or Discord roles, and the matched agent owns the resulting session."
- **URL:** https://docs.openclaw.ai/concepts/agent-bindings
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Gateway runtime" surface, M4 Stable (area: Roles and Permissions). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Parallel specialist lanes
- **What it does (docs):** "Run parallel specialist agents without clogging shared model and tool capacity" / "Parallel specialist lanes let one Gateway route different chats or rooms to different agents while keeping the user experience fast. Treat parallelism as a scarce-resource design problem, not just "more agents"."
- **URL:** https://docs.openclaw.ai/concepts/parallel-specialist-lanes
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Page status field:** `active`

#### Presence
- **What it does (docs):** "How OpenClaw presence entries are produced, merged, and displayed" / "OpenClaw "presence" is a lightweight, best-effort view of:"
- **URL:** https://docs.openclaw.ai/concepts/presence
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Delegate architecture
- **What it does (docs):** "Delegate architecture: running OpenClaw as a named agent on behalf of an organization" / "Run OpenClaw as a **named delegate**: an agent with its own identity that acts "on behalf of" people in an organization. The agent never impersonates a human - it sends, reads, and schedules under its own account with explicit delegation permissions."
- **URL:** https://docs.openclaw.ai/concepts/delegate-architecture
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Page status field:** `active`

**Group: Messages and delivery**

#### Messages
- **What it does (docs):** "Message flow, sessions, queueing, and reasoning visibility" / "Inbound messages move through routing, dedupe/debounce, an agent run, and outbound delivery:"
- **URL:** https://docs.openclaw.ai/concepts/messages
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Streaming and chunking
- **What it does (docs):** "Streaming + chunking behavior (block replies, channel preview streaming, mode mapping)" / "OpenClaw has two independent streaming layers, and there is **no true token-delta streaming** to channel messages:"
- **URL:** https://docs.openclaw.ai/concepts/streaming
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Agent Runtime" surface, M3 Beta (area: Streaming and Progress). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Typing indicators
- **What it does (docs):** "When OpenClaw shows typing indicators and how to tune them" / "Typing indicators are sent to the chat channel while a run is active. Use `agents.defaults.typingMode` to control **when** typing starts and `typingIntervalSeconds` to control **how often** it refreshes (keepalive cadence, default 6 seconds)."
- **URL:** https://docs.openclaw.ai/concepts/typing-indicators
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Progress drafts
- **What it does (docs):** "Progress drafts: one visible work-in-progress message that updates while an agent runs" / "Progress drafts turn one channel message into a live status line while an agent works, instead of a stack of temporary "still working" replies. Set `channels..streaming.mode: "progress"` and OpenClaw creates the message once real work starts, edits it as the agent reads, plans, calls tools, or waits for approval, then delivers the final answer."
- **URL:** https://docs.openclaw.ai/concepts/progress-drafts
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Retry policy
- **What it does (docs):** "Retry policy for outbound provider calls" / "These defaults apply to channel sends. Model requests use the recovery policy below."
- **URL:** https://docs.openclaw.ai/concepts/retry
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Command queue
- **What it does (docs):** "Auto-reply queue modes, shared background capacity, and per-session overrides" / "OpenClaw serializes inbound auto-reply runs (all channels) through a tiny in-process queue to prevent multiple agent runs from colliding, while still allowing safe parallelism across sessions."
- **URL:** https://docs.openclaw.ai/concepts/queue
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Steering queue
- **What it does (docs):** "How active-run steering queues messages at runtime boundaries" / "When a prompt arrives in the same conversation and the queue mode is `steer` (the default, no config needed), OpenClaw tries to send that prompt into the active runtime, including during tool execution. Collaborative steering is enabled by default; operators can disable it explicitly."
- **URL:** https://docs.openclaw.ai/concepts/queue-steering
- **Who runs it:** User machine (the Gateway host or a client of it).

### Tab: Capabilities

**Group: Overview**

#### Overview
- **What it does (docs):** "OpenClaw tools, skills, and plugins overview: what agents can call and how to extend them" / "Use this page to choose the right Capabilities surface. **Tools** are callable actions, **skills** teach agents how to work, and **plugins** add runtime capabilities such as tools, providers, channels, hooks, and packaged skills."
- **URL:** https://docs.openclaw.ai/tools
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Code Mode and Tool Search are experimental OpenClaw agent surfaces."

**Group: Plugins**

#### Plugins
- **What it does (docs):** "Install, configure, and manage OpenClaw plugins" / "Plugins extend OpenClaw with channels, model providers, agent harnesses, tools, skills, speech, realtime transcription, voice, media understanding, generation, web fetch, web search, and other runtime capabilities."
- **URL:** https://docs.openclaw.ai/tools/plugin
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** an OpenClaw checkout or installation with the `openclaw` CLI available; network access to the selected source (ClawHub, npm, or a git host); any plugin-specific credentials, config keys, or OS tools named by that; administrator access to the Gateway that serves your channels
- **Status (maturity scorecard, which links this page):** "ClawHub" surface, M2 Alpha (area: Catalog Discovery, Compatibility and Trust); "Nix install path" surface, M1 Experimental (area: Plugin Lifecycle). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Manage plugins
- **What it does (docs):** "Manage OpenClaw plugins from the Control UI or CLI" / "The Control UI covers discovery, installation, schema-backed configuration, effective access, enablement, reload, and removal. The CLI adds update, advanced maintenance, and explicit install-source controls."
- **URL:** https://docs.openclaw.ai/plugins/manage-plugins
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Nix install path" surface, M1 Experimental (area: Plugin Lifecycle); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Plugin Trust). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Community plugins
- **What it does (docs):** "Find and publish community-maintained OpenClaw plugins" / "Community plugins are third-party packages that extend OpenClaw with channels, tools, providers, hooks, or other capabilities. Use ClawHub as the primary discovery surface for public community plugins."
- **URL:** https://docs.openclaw.ai/plugins/community
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "ClawHub" surface, M2 Alpha (area: Catalog Discovery, Publishing). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Plugin bundles
- **What it does (docs):** "Install and use Agent Plugins, Codex, Claude, and Cursor bundles as OpenClaw plugins" / "OpenClaw can install plugins from four external formats: the vendor-neutral **Agent Plugins** standard, plus **Codex**, **Claude**, and **Cursor**. These are called **bundles** - content and metadata packs that OpenClaw maps into native features like skills, hooks, and MCP tools."
- **URL:** https://docs.openclaw.ai/plugins/bundles
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "ClawHub" surface, M2 Alpha (area: Plugin Lifecycle and Health). Source: https://docs.openclaw.ai/maturity/taxonomy

**Group: Plugin guides**

#### Agent Guidance
- **What it does (docs):** "Shared operator-managed instructions without rewriting agent workspace files" / "Agent Guidance shares instruction files across selected agents. OpenClaw adds their text directly to the prompt sent to the model, before or after its normal instructions."
- **URL:** https://docs.openclaw.ai/plugins/agent-guidance
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Agents API
- **What it does (docs):** "Use the cloud-hosted Agents API harness, powered by Codex, with OpenClaw" / "The bundled `agentsapi` plugin replaces OpenClaw's built-in agent harness with the Agents API harness, which uses the Codex harness under the hood. **The agent harness runs in OpenAI's cloud.** It manages the conversation and the loop of calling the model, using tools, and continuing a task."
- **URL:** https://docs.openclaw.ai/plugins/agentsapi
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

**Nav subgroup: Codex**

#### Codex Computer Use
- **What it does (docs):** "Set up Codex Computer Use for Codex-mode OpenClaw agents" / "Computer Use is a Codex-native MCP plugin for local desktop control. OpenClaw does not vendor the desktop app, execute desktop actions itself, or bypass Codex permissions."
- **URL:** https://docs.openclaw.ai/plugins/codex-computer-use
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "cua-computer fulfiller."

#### Codex harness
- **What it does (docs):** "Run OpenClaw embedded agent turns through the official Codex app-server harness" / "The official `codex` plugin runs embedded OpenAI agent turns through Codex app-server instead of the built-in OpenClaw harness. Codex owns the low-level agent session: native thread resume, native tool continuation, native compaction, and app-server execution."
- **URL:** https://docs.openclaw.ai/plugins/codex-harness
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** The official `@openclaw/codex` plugin installed. Include `codex` in; Managed Codex app-server `0.160.0` or newer. The plugin ships; Node.js on the remote Codex app-server host when `remoteWorkspaceRoot` is set; Codex auth through `openclaw models auth login --provider openai`, an
- **Status (maturity scorecard, which links this page):** "Media understanding and media generation" surface, M2 Alpha (area: Media Configuration); "Observability" surface, M3 Beta (area: Diagnostic Collection); "OpenAI and Codex provider path" surface, M3 Beta (area: Model and Auth, Native Codex Harness); "Plugins" surface, M3 Beta (area: Testing plugins). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "unless you opt into the experimental sandbox exec-server path."
- **Sub-pages in the nav:** Run Codex on another machine (https://docs.openclaw.ai/plugins/codex-harness/placement); Codex routing and deployment (https://docs.openclaw.ai/plugins/codex-harness/routing); Codex harness configuration (https://docs.openclaw.ai/plugins/codex-harness/configuration); Codex app-server policy (https://docs.openclaw.ai/plugins/codex-harness/app-server); Codex plugin config fields (https://docs.openclaw.ai/plugins/codex-harness/config-fields); Codex commands and diagnostics (https://docs.openclaw.ai/plugins/codex-harness/commands); Codex runtime behavior (https://docs.openclaw.ai/plugins/codex-harness/runtime-behavior); Native Codex state and features (https://docs.openclaw.ai/plugins/codex-harness/native-features); Codex harness troubleshooting (https://docs.openclaw.ai/plugins/codex-harness/troubleshooting)

#### Native Codex plugins
- **What it does (docs):** "Configure native Codex plugins for Codex-mode OpenClaw agents" / "Native Codex plugin support lets a Codex-mode OpenClaw agent use Codex app-server's own app and plugin capabilities inside the same Codex thread that handles the OpenClaw turn. Plugin calls stay in the native Codex transcript; Codex app-server owns app-backed MCP execution."
- **URL:** https://docs.openclaw.ai/plugins/codex-native-plugins
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** The agent runtime must be the native Codex harness.; `plugins.entries.codex.enabled` is `true`.; `plugins.entries.codex.config.codexPlugins.enabled` is `true`.; Codex app-server reports `0.149.0` or newer. The official plugin ships
- **Status (maturity scorecard, which links this page):** "OpenAI and Codex provider path" surface, M3 Beta (area: Native Codex Harness, Responses and Tool Compatibility). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Supervise Codex sessions
- **What it does (docs):** "Browse non-archived native Codex sessions and paginated transcripts across OpenClaw nodes" / "Codex supervision is an opt-in capability of the official `codex` plugin. It shows non-archived Codex CLI, VS Code, Atlas, and ChatGPT source sessions from the Gateway computer and opted-in paired computers in the normal sessions sidebar and Chat pane."
- **URL:** https://docs.openclaw.ai/plugins/codex-supervision
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** Install the official `@openclaw/codex` plugin on the Gateway. The OpenClaw; Install and sign in to Codex Desktop or the Codex CLI on each computer whose; Pair remote computers as OpenClaw nodes. Each computer must opt in locally.; Use an owner-controlled Gateway. Session titles, working directories, and Git
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "experimental Codex descendant query through every page within one shared bound."

#### Codex supervision
- **What it does (docs):** "Architecture and product boundary for supervising native Codex sessions from OpenClaw." / "Codex supervision lets an OpenClaw operator discover native Codex sessions, create a Gateway-local branch, or continue an eligible paired-node thread through the normal OpenClaw Chat surface. Codex App Server remains the thread and model-loop owner."
- **URL:** https://docs.openclaw.ai/specs/codex-supervision
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Copilot SDK harness
- **What it does (docs):** "Run OpenClaw embedded agent turns through the external GitHub Copilot SDK harness" / "The external `@openclaw/copilot` plugin runs embedded subscription Copilot agent turns through the GitHub Copilot CLI (`@github/copilot-sdk`) instead of OpenClaw's built-in harness. The Copilot CLI session owns the low-level agent loop: native tool execution, native compaction (`infiniteSessions`), and CLI-managed thread state under `copilotHome`."
- **URL:** https://docs.openclaw.ai/plugins/copilot
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/copilot` (Official external packages)
- **Depends on (page's own requirements section):** OpenClaw with the `@openclaw/copilot` plugin installed.; If your config uses `plugins.allow`, include `copilot` (the manifest id the; A GitHub Copilot subscription that can drive the Copilot CLI, or a; A writable `copilotHome` directory. Defaults to `/copilot` when

#### Muse Code agent runtime
- **What it does (docs):** "Run OpenClaw embedded agent turns for Meta models through the Muse Code CLI" / "The external `@openclaw/muse` plugin runs embedded agent turns for `meta/*` models through Muse Code, Meta's coding agent CLI. The plugin starts `muse serve` and talks to it over the Muse Session Protocol (MSP) with the official `@muse-code/sdk` client."
- **URL:** https://docs.openclaw.ai/plugins/muse
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/muse` (Official external packages)
- **Depends on (page's own requirements section):** OpenClaw. Models can install and enable the `@openclaw/muse` plugin.; If your config uses `plugins.allow`, allow `muse` (the manifest id), not the; The Muse Code CLI installed separately, with a `muse` binary on `PATH` or a; A Meta credential: a Muse Code browser sign-in, a stored key, or a `meta`

**Nav subgroup: Meetings and calls**

#### Meeting plugins
- **What it does (docs):** "Choose and configure Google Meet, Microsoft Teams, Slack huddles, or Zoom participation" / "OpenClaw has separate plugins for Google Meet, Microsoft Teams meetings, Slack huddles, and Zoom. All four can join through Chrome, use the same participation modes, and run Chrome either on the Gateway host or on a paired node."
- **URL:** https://docs.openclaw.ai/plugins/meeting-plugins
- **Who runs it:** User machine (the Gateway host or a client of it).

#### FaceTime plugin
- **What it does (docs):** "Set up FaceTime voice calls with your OpenClaw agent on a Mac" / "Connect FaceTime to your OpenClaw agent for two-way voice conversations. The plugin automatically answers calls from your configured handles and lets your agent call you with approval."
- **URL:** https://docs.openclaw.ai/plugins/facetime
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/facetime` (Official external packages)
- **Depends on (page's own requirements section):** An Apple Silicon Mac running macOS 14.4 or later.; The current OpenClaw host release, matching the bundled plugin.; FaceTime signed in to your Apple Account on the Gateway Mac.; Full Xcode installed at `/Applications/Xcode.app`.
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: experimental, disabled by default."

#### FaceTime recovery and removal
- **What it does (docs):** "Remove FaceTime native artifacts and restore standard Mac security policy" / "This procedure removes the FaceTime plugin's native artifacts and describes the separate operator actions needed to restore the Mac's standard security posture. OpenClaw never changes SIP automatically."
- **URL:** https://docs.openclaw.ai/plugins/facetime-recovery
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Google Meet plugin
- **What it does (docs):** "Google Meet plugin: join explicit Meet URLs through Chrome or Twilio with agent talk-back defaults" / "The `google-meet` plugin joins explicit Meet URLs on behalf of an OpenClaw agent. It is deliberately narrow:"
- **URL:** https://docs.openclaw.ai/plugins/google-meet
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/google-meet` (Official external packages)
- **Sub-pages in the nav:** Google Meet transports and hosts (https://docs.openclaw.ai/plugins/google-meet/transports); Google Meet OAuth and artifacts (https://docs.openclaw.ai/plugins/google-meet/oauth-and-artifacts); Google Meet configuration (https://docs.openclaw.ai/plugins/google-meet/config); Google Meet tool and modes (https://docs.openclaw.ai/plugins/google-meet/tool-and-modes); Google Meet troubleshooting (https://docs.openclaw.ai/plugins/google-meet/troubleshooting)

#### Microsoft Teams meetings plugin
- **What it does (docs):** "Microsoft Teams meetings plugin: join work or consumer meetings as a Chrome browser guest" / "The `teams-meetings` plugin joins work links under `teams.microsoft.com/l/meetup-join/...` and consumer links under `teams.live.com/meet/...` as a guest in the OpenClaw Chrome profile. It does not create meetings, dial in, call Microsoft Graph, or capture audio/video recordings."
- **URL:** https://docs.openclaw.ai/plugins/teams-meetings
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/teams-meetings` (Official external packages)

#### Slack huddles plugin
- **What it does (docs):** "Slack huddles plugin: join active huddles through a signed-in Chrome user account" / "The `slack-huddles` plugin joins active Slack huddles through the Slack web client in the OpenClaw Chrome profile. It uses a dedicated Slack **user account** for the agent: Slack has no app or bot API for joining huddles or reading their audio."
- **URL:** https://docs.openclaw.ai/plugins/slack-huddles
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/slack-huddles` (Official external packages)
- **Depends on (page's own requirements section):** OpenClaw 2026.9.8 or newer. Older hosts lack the shared meeting-runtime; A dedicated Slack user account signed into Slack in the OpenClaw Chrome profile.; Membership in the channel or conversation containing the huddle.; An active huddle, started by a person in Slack.

#### Voice call plugin
- **What it does (docs):** "Place outbound and accept inbound voice calls via Twilio, Telnyx, or Plivo, with optional realtime voice and streaming transcription" / "Voice calls for OpenClaw via a plugin: outbound notifications, multi-turn conversations, full-duplex realtime voice, streaming transcription, and inbound calls with allowlist policies."
- **URL:** https://docs.openclaw.ai/plugins/voice-call
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** official plugin
- **Status (maturity scorecard, which links this page):** "OpenAI and Codex provider path" surface, M3 Beta (area: Voice and Realtime Audio); "Voice Call channel" surface, M1 Experimental (area: Access and Identity, Channel Setup and Operations). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Voice call configuration (https://docs.openclaw.ai/plugins/voice-call/configuration); Voice call realtime and streaming (https://docs.openclaw.ai/plugins/voice-call/realtime-and-streaming); Voice call TTS and inbound calls (https://docs.openclaw.ai/plugins/voice-call/tts-and-inbound-calls); Voice call security and interfaces (https://docs.openclaw.ai/plugins/voice-call/security-and-interfaces); Voice call troubleshooting (https://docs.openclaw.ai/plugins/voice-call/troubleshooting)

#### Zoom meetings plugin
- **What it does (docs):** "Zoom meetings plugin: join meetings as a Chrome browser guest" / "The `zoom-meetings` plugin joins `zoom.us/j/...` links and account subdomains such as `example.zoom.us/j/...` as a guest through the Zoom Web App in the OpenClaw Chrome profile. It does not create meetings, dial in, use the Zoom Meeting SDK, or capture audio/video recordings."
- **URL:** https://docs.openclaw.ai/plugins/zoom-meetings
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/zoom-meetings` (Official external packages)

**Nav subgroup: Models and memory**

#### Apple Foundation Models
- **What it does (docs):** "Use on-device Apple Foundation Models for lightweight OpenClaw setup on a Mac" / "The bundled Apple Foundation Models plugin runs Apple's on-device model through the native Foundation Models framework. It is a free local **setup and utility** model."
- **URL:** https://docs.openclaw.ai/plugins/apple-fm
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Depends on (page's own requirements section):** A Mac with Apple silicon running macOS 27 or later.; Apple Intelligence enabled in System Settings, with its model downloaded.; Installed Apple Swift developer tools with the macOS 27 SDK.; An available system model with at least 8,192 context tokens.

#### Knowledge
- **What it does (docs):** "Knowledge: an evidence-backed knowledge vault, memory provider, and Control UI explorer for OpenClaw agents" / "`knowledge` is a bundled plugin that gives each agent an evidence-backed knowledge vault. Agents save pages, claims, and typed relationships as Markdown files with retained source evidence."
- **URL:** https://docs.openclaw.ai/plugins/knowledge
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Sub-pages in the nav:** Knowledge stores and access (https://docs.openclaw.ai/plugins/knowledge/stores-and-access); Knowledge as memory provider (https://docs.openclaw.ai/plugins/knowledge/memory-provider); Knowledge tools (https://docs.openclaw.ai/plugins/knowledge/tools); Knowledge records and ontology (https://docs.openclaw.ai/plugins/knowledge/records-and-ontology); Knowledge retrieval and dates (https://docs.openclaw.ai/plugins/knowledge/retrieval); Knowledge evidence files (https://docs.openclaw.ai/plugins/knowledge/evidence); Knowledge ingestion workflows (https://docs.openclaw.ai/plugins/knowledge/ingestion); Knowledge corrections and merges (https://docs.openclaw.ai/plugins/knowledge/corrections); Knowledge local history (https://docs.openclaw.ai/plugins/knowledge/local-history); Knowledge maintenance (https://docs.openclaw.ai/plugins/knowledge/maintenance); Knowledge scribes (https://docs.openclaw.ai/plugins/knowledge/scribes); Knowledge Control UI (https://docs.openclaw.ai/plugins/knowledge/control-ui)

#### llama.cpp Provider
- **What it does (docs):** "Run GGUF chat with managed or existing llama.cpp servers and managed local embeddings" / "The `llama-cpp` plugin provides one `llama-cpp` model provider. OpenClaw can manage a local `llama-server` or connect to one that you operate."
- **URL:** https://docs.openclaw.ai/plugins/llama-cpp
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/llama-cpp-provider` (Official external packages)

#### Memory LanceDB
- **What it does (docs):** "Configure the official external LanceDB memory plugin, including local Ollama-compatible embeddings" / "`memory-lancedb` is an official external plugin that stores long-term memory in LanceDB with vector search. It can auto-recall relevant memories before a model turn and auto-capture important facts after a response."
- **URL:** https://docs.openclaw.ai/plugins/memory-lancedb
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/memory-lancedb` (Official external packages)

#### Memory wiki
- **What it does (docs):** "memory-wiki: compiled knowledge vault with provenance, claims, dashboards, and bridge mode" / "`memory-wiki` is a bundled plugin that compiles durable knowledge into a navigable wiki: pages built from saved data, structured claims with evidence, provenance, dashboards, and machine-readable digests."
- **URL:** https://docs.openclaw.ai/plugins/memory-wiki
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Intentionally experimental and non-portable; use only when you understand the trust boundary and specifically need local filesystem access bridge mode cannot provide."

#### Local ONNX decision models
- **What it does (docs):** "Run typed decisions locally with verified ONNX classifiers" / "The installable **ONNX** plugin runs classifiers locally through the decision model API. It uses a separate, persistent Node process with ONNX Runtime's CPU backend."
- **URL:** https://docs.openclaw.ai/plugins/onnx
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/onnx` (Official external packages)

#### SubQ
- **What it does (docs):** "Use SubQ Snap for typed decisions, not chat completions" / "The `subq` plugin connects the optional decision model role to **SubQ Snap**, a hosted model for Boolean judgments, choices, and rubric scores. It appears in the **Decision** picker, not the conversational model picker."
- **URL:** https://docs.openclaw.ai/plugins/subq
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/subq` (Official external packages)
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Decision assistance opt-in."

#### TypeSafe AI
- **What it does (docs):** "Use hosted Jev or a local System One server for typed decisions" / "The official external `typesafe` plugin connects OpenClaw's optional decision model role to TypeSafe AI's hosted Jev models or an explicitly configured System One server such as Kev. Its models appear in the separate **Decision** picker, never in the conversational model picker."
- **URL:** https://docs.openclaw.ai/plugins/typesafe
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/typesafe` (Official external packages)
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "This is TypeSafe's experimental image API, not a production accuracy guarantee."

**Nav subgroup: Secrets and vaults**

#### 1Password plugin
- **What it does (docs):** "Resolve SecretRefs and give agents curated, audited access to 1Password" / "The bundled `onepassword` plugin has two independent, opt-in surfaces:"
- **URL:** https://docs.openclaw.ai/plugins/onepassword
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Depends on (page's own requirements section):** the 1Password CLI (`op`) installed on the Gateway host; a 1Password service account with access to the selected items; a dedicated service-account token file

#### Vault SecretRefs
- **What it does (docs):** "Use the bundled Vault plugin to resolve SecretRefs from HashiCorp Vault" / "The bundled Vault plugin lets OpenClaw resolve `exec` SecretRefs from HashiCorp Vault at Gateway startup and reload time. OpenClaw stores Vault references in config, keeps resolved values in the in-memory secrets snapshot, and does not write the resolved API keys back to `openclaw.json`."
- **URL:** https://docs.openclaw.ai/plugins/vault
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Depends on (page's own requirements section):** OpenClaw with the bundled `vault` plugin available; a reachable Vault server; Vault auth that can produce a client token with read access to the secret; the environment that starts the Gateway must include `VAULT_ADDR` and either

**Nav subgroup: Automation and integrations**

#### Admin HTTP RPC plugin
- **What it does (docs):** "Expose selected Gateway control-plane methods through the bundled, opt-in admin-http-rpc plugin" / "The bundled `admin-http-rpc` plugin exposes an allowlisted set of Gateway control-plane methods over HTTP, for trusted host automation that cannot keep a Gateway WebSocket connection open."
- **URL:** https://docs.openclaw.ai/plugins/admin-http-rpc
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Beam plugin
- **What it does (docs):** "Publish coding sessions for shared viewing and live Team continuation" / "The bundled `beam` plugin receives a sanitized coding-session snapshot over authenticated HTTP and presents it in the Control UI's existing external-session catalog. The source computer sends text out; OpenClaw never connects back to that computer and receives no filesystem, terminal, tool, or node capability."
- **URL:** https://docs.openclaw.ai/plugins/beam
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Cloudflare
- **What it does (docs):** "Configure Cloudflare R2 as an encrypted OpenClaw storage location" / "The bundled Cloudflare plugin provides `r2` storage locations through Cloudflare's S3-compatible API. OpenClaw handles location identity and encryption; the plugin transfers objects to your bucket."
- **URL:** https://docs.openclaw.ai/plugins/cloudflare
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw, and also from npm or ClawHub: `@openclaw/cloudflare` (Core npm package)

#### Geolocation plugin
- **What it does (docs):** "Resolve a connecting client's IP address to a coarse city using a locally cached database, with no per-lookup third-party calls" / "The bundled `geolocation` plugin turns a connecting client's IP address into a coarse city. It ships with OpenClaw, downloads its database on first use, and answers entirely from that local copy, so a lookup never sends an address to a third party."
- **URL:** https://docs.openclaw.ai/plugins/geolocation
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Logbook plugin
- **What it does (docs):** "Optional automatic work journal built from periodic screen snapshots" / "The Logbook plugin turns screen activity into an automatic work journal. It captures periodic screen snapshots from a paired node, summarizes them into timestamped observations, and builds timeline cards in the Control UI."
- **URL:** https://docs.openclaw.ai/plugins/logbook
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Depends on (page's own requirements section):** A connected node that exposes `screen.snapshot` or `logbook.snapshot`. The; The bundled Codex plugin enabled and authenticated. Codex provides; A working default agent model. Logbook uses it to synthesize cards, standup

#### MCP Relay
- **What it does (docs):** "Connect ChatGPT and Claude to your Gateway through the opt-in MCP relay plugin" / "The bundled `mcp-relay` plugin connects your Gateway to `https://mcp.openclaw.ai` over an outbound WebSocket. Remote MCP clients such as ChatGPT, Codex, and Claude connect to `https://mcp.openclaw.ai/mcp`; you do not need to expose a Gateway port to the internet."
- **URL:** https://docs.openclaw.ai/plugins/mcp-relay
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### OC Path plugin
- **What it does (docs):** "Bundled `oc-path` plugin: ships the `openclaw path` CLI for the `oc://` workspace-file addressing scheme" / "The bundled `oc-path` plugin adds the `openclaw path` CLI for the `oc://` workspace-file addressing scheme. It ships in the OpenClaw repo under `extensions/oc-path/` but is opt-in: install/build leaves it dormant until you enable it."
- **URL:** https://docs.openclaw.ai/plugins/oc-path
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Session Share plugin
- **What it does (docs):** "Share selected OpenClaw sessions read-only with a paired team Gateway" / "The bundled `session-share` plugin lets teammates read selected sessions from another OpenClaw Gateway in the Control UI. The source operator chooses session groups to publish and can narrow them by person."
- **URL:** https://docs.openclaw.ai/plugins/session-share
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Workboard plugin
- **What it does (docs):** "Optional Workboard boards for agent-owned cards and rule-based session views" / "The Workboard plugin adds an optional Kanban-style board to the Control UI: agent-sized work cards, assignment to agents, and a link back to the card's task, run, and Control UI session. A separate **Sessions board** groups existing sessions into editable columns using rules over Gateway-owned facts."
- **URL:** https://docs.openclaw.ai/plugins/workboard
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Background Work). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Zalo personal plugin
- **What it does (docs):** "Zalo Personal plugin: QR login + messaging via native zca-js (plugin install + channel config + tool)" / "The zalouser plugin adds unofficial Zalo Personal support to OpenClaw. It uses native `zca-js` to automate a normal Zalo user account."
- **URL:** https://docs.openclaw.ai/plugins/zalouser
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/zalouser` (Official external packages)

**Group: Building plugins**

#### Building plugins
- **What it does (docs):** "Create your first OpenClaw plugin in minutes" / "Plugins extend OpenClaw without changing core. A plugin can add a messaging channel, model provider, local CLI backend, agent tool, hook, media provider, or another plugin-owned capability."
- **URL:** https://docs.openclaw.ai/plugins/building-plugins
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Depends on (page's own requirements section):** All plugin APIs are experimental.; Node 24.22.1+ or Node 26.12.1+, and `npm` or `pnpm`.; TypeScript ESM modules.; For in-repo bundled plugin work, clone the repository and run `pnpm install`.
- **Status (maturity scorecard, which links this page):** "Plugins" surface, M3 Beta (area: Authoring and Packaging plugins). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Plugin runtime compatibility
- **What it does (docs):** "Inspect plugin and dependency runtime hazards without activating the plugin" / "OpenClaw reports runtime compatibility hazards after a code plugin's production dependencies have been materialized and before activation. The same static inspection is available to plugin authors without importing or running their plugin:"
- **URL:** https://docs.openclaw.ai/plugins/runtime-compatibility
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.

#### Feature plugins
- **What it does (docs):** "Build plugins with typed operations, native pages, and replaceable Control UI views" / "A feature plugin can own its backend operations and its Control UI. It can add pages, navigation, session actions, panels, dashboard widgets, and header accessories, or provide replacements for the workspace, session list, composer, transcript, and tool results."
- **URL:** https://docs.openclaw.ai/plugins/feature-plugins
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.

#### Tool plugins
- **What it does (docs):** "Build simple typed agent tools with defineToolPlugin and openclaw plugins init/build/validate" / "`defineToolPlugin` builds a plugin that only adds agent-callable tools: no channel, model provider, hook, service, or setup backend. It generates the manifest metadata OpenClaw needs to discover tools without loading plugin runtime code."
- **URL:** https://docs.openclaw.ai/plugins/tool-plugins
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Depends on (page's own requirements section):** Node 24.22.1+ or Node 26.12.1+.; TypeScript ESM package output.; `typebox` in `dependencies` (not just `devDependencies` - the generated; `openclaw >=2026.5.17`, the first version that exports
- **Status (maturity scorecard, which links this page):** "Plugins" surface, M3 Beta (area: Provider and tool plugins). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Building channel plugins
- **What it does (docs):** "Step-by-step guide to building a messaging channel plugin for OpenClaw" / "This guide builds a channel plugin that connects OpenClaw to a messaging platform: DM security, pairing, reply threading, and outbound messaging."
- **URL:** https://docs.openclaw.ai/plugins/sdk-channel-plugins
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Plugins" surface, M3 Beta (area: Channel plugins, Plugin approvals); "Channel framework" surface, M3 Beta (area: Channel Setup). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "retainNativeCatalog(provider) has been deprecated since 2026."
- **Sub-pages in the nav:** Channel message adapter (https://docs.openclaw.ai/plugins/sdk-channel-plugins/message-adapter); Durable channel ingress (https://docs.openclaw.ai/plugins/sdk-channel-plugins/durable-ingress); Channel status and media (https://docs.openclaw.ai/plugins/sdk-channel-plugins/status-and-media); Channel sessions and bindings (https://docs.openclaw.ai/plugins/sdk-channel-plugins/sessions-and-bindings); Channel approvals (https://docs.openclaw.ai/plugins/sdk-channel-plugins/approvals); Channel setup and config (https://docs.openclaw.ai/plugins/sdk-channel-plugins/setup-and-config); Channel mention policy (https://docs.openclaw.ai/plugins/sdk-channel-plugins/mention-policy)

#### Building provider plugins
- **What it does (docs):** "Step-by-step guide to building a model provider plugin for OpenClaw" / "Build a provider plugin to add a model provider (LLM) to OpenClaw: a model catalog, API-key auth, and dynamic model resolution."
- **URL:** https://docs.openclaw.ai/plugins/sdk-provider-plugins
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Plugins" surface, M3 Beta (area: Provider and tool plugins); "Voice and realtime talk" surface, M2 Alpha (area: Talk Providers). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "that govern deprecated surfaces named on this page and its child pages."
- **Sub-pages in the nav:** Provider model catalogs (https://docs.openclaw.ai/plugins/sdk-provider-plugins/model-catalogs); Provider hook families (https://docs.openclaw.ai/plugins/sdk-provider-plugins/hook-families); Provider hook wiring (https://docs.openclaw.ai/plugins/sdk-provider-plugins/runtime-hooks); Provider voice capabilities (https://docs.openclaw.ai/plugins/sdk-provider-plugins/voice-and-audio); Provider media and search (https://docs.openclaw.ai/plugins/sdk-provider-plugins/media-and-search)

#### Building CLI backend plugins
- **What it does (docs):** "Build a plugin that registers a local AI CLI backend" / "CLI backend plugins let OpenClaw call a local AI CLI as a text inference backend. The backend appears as a provider prefix in model refs:"
- **URL:** https://docs.openclaw.ai/plugins/cli-backend-plugins
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.

#### Plugin hooks
- **What it does (docs):** "Plugin hooks: intercept agent, tool, message, session, and Gateway lifecycle events" / "Plugin hooks let a native OpenClaw plugin observe or change agent runs, tool calls, message delivery, and lifecycle events. Register a typed handler with `api.on("hook_name", handler)` and return the result documented for that hook."
- **URL:** https://docs.openclaw.ai/plugins/hooks
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Automation Hooks); "Observability" surface, M3 Beta (area: Telemetry Export). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "A few hook-adjacent surfaces are deprecated but still supported."
- **Sub-pages in the nav:** Hook reference (https://docs.openclaw.ai/plugins/hooks/reference); Tool call policy hooks (https://docs.openclaw.ai/plugins/hooks/tool-policy); Prompt and session hooks (https://docs.openclaw.ai/plugins/hooks/prompt-and-session); Message and delivery hooks (https://docs.openclaw.ai/plugins/hooks/messages); Gateway and install lifecycle hooks (https://docs.openclaw.ai/plugins/hooks/lifecycle)

#### Plugin permission requests
- **What it does (docs):** "Ask users to approve plugin tool calls and plugin-owned permission prompts" / "Plugin permission requests let plugin code pause a tool call or plugin-owned operation until a user approves or denies it. They use the Gateway `plugin.approval.*` flow and the same approval UI surfaces that handle chat approval buttons and `/approve` commands."
- **URL:** https://docs.openclaw.ai/plugins/plugin-permission-requests
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Automation Hooks); "Plugins" surface, M3 Beta (area: Plugin approvals); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Approval Policy and Tool Safeguards, Plugin Trust). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Adding capabilities (contributor guide)
- **What it does (docs):** "Contributor guide for adding a new shared capability to the OpenClaw plugin system" / "This is a **contributor guide** for OpenClaw core developers. If you are building an external plugin, see Building plugins instead."
- **URL:** https://docs.openclaw.ai/plugins/adding-capabilities
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Plugins" surface, M3 Beta (area: Provider and tool plugins). Source: https://docs.openclaw.ai/maturity/taxonomy

**Group: Skills**

#### Skills
- **What it does (docs):** "Skills teach your agent how to use tools. Learn how they load, how precedence works, and how to configure gating, allowlists, and environment injection." / "Skills are markdown instruction files that teach the agent how and when to use tools. Each skill lives in a directory containing a `SKILL.md` file with YAML frontmatter and a markdown body."
- **URL:** https://docs.openclaw.ai/tools/skills
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "ClawHub" surface, M2 Alpha (area: Catalog Discovery, Compatibility and Trust); "Media understanding and media generation" surface, M2 Alpha (area: Media Generation). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Custodian skills
- **What it does (docs):** "Release-versioned operational skills that only the configured Custodian agent can discover and use." / "Custodian skills are release-versioned operational playbooks shipped with OpenClaw. They live under `custodian-skills/` in the package."
- **URL:** https://docs.openclaw.ai/tools/custodian-skills
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Skill Workshop
- **What it does (docs):** "Skills your agent learns on its own: how they are saved, undo, unused-skill cleanup, skill diet, /learn, config, storage, and operator surfaces" / "Skill Workshop holds the skills an agent writes for itself, called **learned skills**. The agent saves a procedure after hard multi-step work and fixes a learned skill that misled it; skills nobody uses for 30 days are archived."
- **URL:** https://docs.openclaw.ai/tools/skill-workshop
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Personal library authoring
- **What it does (docs):** "Create and update profile-owned personal skills on a shared Gateway" / "On a shared Gateway, ask the agent normally: **Create a skill for me that summarizes a reviewed change list.** The authenticated requester owns the result, even when another person created or owns the session. No separate authoring mode or identity argument is required."
- **URL:** https://docs.openclaw.ai/tools/skill-workshop/personal-library
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Self-learning
- **What it does (docs):** "How OpenClaw reviews finished work in the background and saves lessons as learned skills" / "Self-learning turns corrections and hard-won procedures into learned skills that future sessions load. It is on by default (`plugins.entries.skill-workshop.config.autonomous.mode: "auto"`)."
- **URL:** https://docs.openclaw.ai/tools/self-learning
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Creating skills
- **What it does (docs):** "Build, test, and publish custom SKILL.md workspace skills or personal skills on a shared Gateway." / "Skills teach the agent how and when to use tools. Each skill is a directory containing a `SKILL.md` file with YAML frontmatter and markdown instructions."
- **URL:** https://docs.openclaw.ai/tools/creating-skills
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "ClawHub" surface, M2 Alpha (area: Publishing). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Skills config
- **What it does (docs):** "Full reference for the skills.* config schema, agent allowlists, workshop settings, and sandbox env var handling." / "Most skills configuration lives under `skills` in `~/.openclaw/openclaw.json`. Agent-specific visibility lives under `agents.defaults.skills` and `agents.entries.*.skills`."
- **URL:** https://docs.openclaw.ai/tools/skills-config
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "ClawHub" surface, M2 Alpha (area: Compatibility and Trust). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Slash commands
- **What it does (docs):** "All available slash commands, directives, and inline shortcuts — configuration, routing, and per-surface behavior." / "The Gateway handles commands sent as standalone messages starting with `/`. Host-only bash commands use `!"
- **URL:** https://docs.openclaw.ai/tools/slash-commands
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Discord" surface, M4 Stable (area: Channel Setup and Operations, Native Controls and Approvals); "Google Chat" surface, M2 Alpha (area: Native Controls and Approvals); "Slack" surface, M3 Beta (area: Native Controls and Approvals). Source: https://docs.openclaw.ai/maturity/taxonomy

**Group: Automation**

#### Automation
- **What it does (docs):** "Overview of automation mechanisms: automations, hooks, standing orders, and workflows" / "OpenClaw runs work in the background through native runtimes, scheduled jobs, event hooks, and standing instructions. Use this page to pick the right mechanism."
- **URL:** https://docs.openclaw.ai/automation
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Background Work, Heartbeat). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "have been removed"; may describe a sub-feature):** "have been removed."

#### Heartbeat migration
- **What it does (docs):** "Migrate retired heartbeat monitors to ordinary automation jobs" / "Heartbeat monitoring now uses ordinary automation jobs. Doctor converts existing monitors into editable jobs with their own schedules, policies, scratch, and run history."
- **URL:** https://docs.openclaw.ai/gateway/heartbeat
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Anthropic provider path" surface, M3 Beta (area: Prompt Cache and Context); "Automation and durable work" surface, M3 Beta (area: Heartbeat). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Automations
- **What it does (docs):** "Automations: scheduled jobs, webhooks, and Gmail PubSub triggers for the Gateway scheduler" / "Automations are OpenClaw's built-in scheduler. The scheduler persists jobs, wakes the agent at the right time, and can deliver output to a chat channel, a webhook, or nowhere."
- **URL:** https://docs.openclaw.ai/automation/cron-jobs
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Cron Jobs, Event Ingress). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** How automations work (https://docs.openclaw.ai/automation/cron-jobs/how-it-works); Automation schedules (https://docs.openclaw.ai/automation/cron-jobs/schedules); Automation payloads (https://docs.openclaw.ai/automation/cron-jobs/payloads); Automation delivery (https://docs.openclaw.ai/automation/cron-jobs/delivery); Manage automations (https://docs.openclaw.ai/automation/cron-jobs/managing-jobs); Inbound webhooks (https://docs.openclaw.ai/automation/cron-jobs/webhooks); Gmail PubSub triggers (https://docs.openclaw.ai/automation/cron-jobs/gmail); Automation troubleshooting (https://docs.openclaw.ai/automation/cron-jobs/troubleshooting)

#### IMAP email trigger
- **What it does (docs):** "Watch an IMAP mailbox and route authenticated incoming email to an isolated restricted reader agent" / "The bundled IMAP plugin watches an existing mailbox and starts a separate, isolated agent session for each allowed incoming message. It does not send email, modify message flags, expose a public webhook, or backfill messages already present when monitoring begins."
- **URL:** https://docs.openclaw.ai/automation/imap
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### MCP Events
- **What it does (docs):** "Subscribe to MCP events and run existing Automations from signed webhooks" / "MCP Events connects a remote MCP server to Automations. The MCP server filters changes and sends signed webhooks."
- **URL:** https://docs.openclaw.ai/automation/mcp-events
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Standing orders
- **What it does (docs):** "Define permanent operating authority for autonomous agent programs" / "Standing orders grant your agent **permanent operating authority** for defined programs. Instead of prompting the agent for each task, you define programs with clear scope, triggers, and escalation rules, and the agent executes autonomously within those boundaries: "You own the weekly report."
- **URL:** https://docs.openclaw.ai/automation/standing-orders
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Background Work). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Hooks
- **What it does (docs):** "Internal hooks: install, write, and verify automation for commands and lifecycle events" / "Internal hooks are small JavaScript or TypeScript handlers that run in the Gateway process when OpenClaw emits an event. Use them to save session context, log reset commands, or perform short side effects during message and session lifecycle events."
- **URL:** https://docs.openclaw.ai/automation/hooks
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Automation Hooks); "Gateway runtime" surface, M4 Stable (area: HTTP APIs). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Writing hooks (https://docs.openclaw.ai/automation/hooks/writing-hooks); Hook configuration and discovery (https://docs.openclaw.ai/automation/hooks/configuration); Bundled hooks (https://docs.openclaw.ai/automation/hooks/bundled-hooks); Hook event types and context (https://docs.openclaw.ai/automation/hooks/event-types); Hook troubleshooting (https://docs.openclaw.ai/automation/hooks/troubleshooting)

**Group: Tools**

**Nav subgroup: Running code and approvals**

#### apply_patch tool
- **What it does (docs):** "Apply multi-file patches with the apply_patch tool" / "Apply file changes using a structured patch format. This is ideal for multi-file or multi-hunk edits where a single `edit` call would be brittle."
- **URL:** https://docs.openclaw.ai/tools/apply-patch
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Code execution
- **What it does (docs):** "code_execution: run sandboxed remote Python analysis with xAI" / "`code_execution` runs sandboxed remote Python analysis on xAI's Responses API (`https://api.x.ai/v1/responses`, same endpoint `x_search` uses). It is registered by the bundled `xai` plugin under the `tools` contract."
- **URL:** https://docs.openclaw.ai/tools/code-execution
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Diffs
- **What it does (docs):** "Read-only diff viewer and file renderer for agents (optional plugin tool)" / "`diffs` is an optional plugin tool that turns before/after text or a unified patch into a read-only diff artifact. It also prepends short agent guidance into the system prompt and ships a companion skill for fuller instructions."
- **URL:** https://docs.openclaw.ai/tools/diffs
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/diffs` (Official external packages)
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "Deprecated alias: "image" behaves identically to "file"."

#### Elevated mode
- **What it does (docs):** "Elevated exec mode: run commands outside the sandbox from a sandboxed agent" / "When an agent runs inside a sandbox, its `exec` commands are confined to the sandbox environment. **Elevated mode** lets the agent break out of ordinary agent-configured sandboxing and run commands outside the sandbox instead, with configurable approval gates."
- **URL:** https://docs.openclaw.ai/tools/elevated
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Tool Invocation and Execution). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Exec tool
- **What it does (docs):** "Exec tool usage, stdin modes, and TTY support" / "Run shell commands in the workspace. `exec` is a mutating shell surface: commands can create, edit, or delete files wherever the selected host or sandbox filesystem permits."
- **URL:** https://docs.openclaw.ai/tools/exec
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Tool Invocation and Execution); "Linux companion app" surface, M3 Beta (area: Desktop Capabilities); "Windows App / Node" surface, M3 Beta (area: Desktop Tools and Permissions). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "was removed"; may describe a sub-feature):** "run wrapper was removed in 2026."

#### Exec approvals
- **What it does (docs):** "Host exec approvals: policy knobs, allowlists, and the YOLO/strict workflow" / "Exec approvals are the **companion app / node host guardrail** for letting a sandboxed agent run commands on a real host (`gateway` or `node`). Commands run only when policy + allowlist + (optional) user approval all agree."
- **URL:** https://docs.openclaw.ai/tools/exec-approvals
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Tool Invocation and Execution); "Linux companion app" surface, M3 Beta (area: Desktop Capabilities); "Plugins" surface, M3 Beta (area: Plugin approvals); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Approval Policy and Tool Safeguards); plus 4 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy

#### Exec approvals — advanced
- **What it does (docs):** "Advanced exec approvals: safe bins, interpreter binding, approval forwarding, native delivery" / "Advanced exec-approval topics: the `safeBins` fast-path, interpreter/runtime binding, and approval-forwarding to chat channels (including native delivery). For the core policy and approval flow, see Exec approvals."
- **URL:** https://docs.openclaw.ai/tools/exec-approvals-advanced
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Tool Invocation and Execution); "Microsoft Teams" surface, M2 Alpha (area: Native Controls and Approvals). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Permission modes
- **What it does (docs):** "Permission modes for host exec, Codex Guardian approvals, and ACPX harness sessions" / "Permission modes decide how much authority an agent has before it runs host commands, writes files, or asks a backend harness for extra access."
- **URL:** https://docs.openclaw.ai/tools/permission-modes
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Secrets
- **What it does (docs):** "How the secrets tool lets the agent request credentials it never sees" / "`secrets` lets the agent ask you for a credential without ever seeing it. The agent names an entry, you type the value into a trusted prompt, and the Gateway writes it straight into the shared secret store."
- **URL:** https://docs.openclaw.ai/tools/secrets
- **Who runs it:** User machine (the Gateway host or a client of it).

**Nav subgroup: Media and documents**

#### Media overview
- **What it does (docs):** "Image, video, music, speech, and media-understanding capabilities at a glance" / "OpenClaw generates images, videos, and music, understands inbound media (images, audio, video), and speaks replies aloud with text-to-speech. All media capabilities are tool-driven: the agent decides when to use them based on the conversation, and each tool only appears when at least one backing provider is configured."
- **URL:** https://docs.openclaw.ai/tools/media-overview
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Image, video, and music generation tools" surface, M2 Alpha (area: Image Generation, Media Operation Lifecycle and Delivery); "Media understanding and media generation" surface, M2 Alpha (area: Channel Media Handling, Media Configuration); "OpenRouter provider path" surface, M3 Beta (area: Media Generation and Speech). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Image generation
- **What it does (docs):** "Generate and edit images via image_generate across OpenAI, Google, fal, Microsoft Foundry, MiniMax, ComfyUI, DeepInfra, OpenRouter, LiteLLM, xAI, Vydra" / "The `image_generate` tool creates and edits images through your configured providers. In chat sessions it runs asynchronously: the native media-generation owner tracks the operation, returns the task id immediately, and wakes the agent when the provider finishes."
- **URL:** https://docs.openclaw.ai/tools/image-generation
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Image, video, and music generation tools" surface, M2 Alpha (area: Image Generation, Media Operation Lifecycle and Delivery); "Media understanding and media generation" surface, M2 Alpha (area: Media Configuration, Media Generation); "OpenAI and Codex provider path" surface, M3 Beta (area: Image and Multimodal Input); "OpenRouter provider path" surface, M3 Beta (area: Media Generation and Speech). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Music generation
- **What it does (docs):** "Generate music via music_generate across ComfyUI, fal, Google Lyria, MiniMax, and OpenRouter workflows" / "The `music_generate` tool creates music or audio through the shared music-generation capability, backed by ComfyUI, fal, Google, MiniMax, and OpenRouter."
- **URL:** https://docs.openclaw.ai/tools/music-generation
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Image, video, and music generation tools" surface, M2 Alpha (area: Media Operation Lifecycle and Delivery, Media Routing and Discovery); "Media understanding and media generation" surface, M2 Alpha (area: Media Generation); "OpenRouter provider path" surface, M3 Beta (area: Media Generation and Speech). Source: https://docs.openclaw.ai/maturity/taxonomy

#### PDF tool
- **What it does (docs):** "Analyze one or more PDF documents with native provider support and extraction fallback" / "`pdf` analyzes one or more PDF documents and returns text. It uses native document input on Anthropic and Google models, and falls back to text/image extraction for every other provider."
- **URL:** https://docs.openclaw.ai/tools/pdf
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Media understanding and media generation" surface, M2 Alpha (area: Media Intake and Access, Media Understanding). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Text-to-speech
- **What it does (docs):** "Index of the OpenClaw text-to-speech documentation, one page per reader job" / "OpenClaw converts outbound replies into native voice messages on Feishu, Matrix, Telegram, and WhatsApp. Every other channel receives an audio attachment."
- **URL:** https://docs.openclaw.ai/tools/tts
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Media understanding and media generation" surface, M2 Alpha (area: Text-to-Speech Delivery); "OpenRouter provider path" surface, M3 Beta (area: Media Generation and Speech). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Text-to-speech quickstart (https://docs.openclaw.ai/tools/tts/quickstart); Text-to-speech configuration (https://docs.openclaw.ai/tools/tts/configuration); Text-to-speech personas (https://docs.openclaw.ai/tools/tts/personas); Text-to-speech commands and directives (https://docs.openclaw.ai/tools/tts/commands); Text-to-speech output and Auto-TTS behavior (https://docs.openclaw.ai/tools/tts/output); Text-to-speech field reference (https://docs.openclaw.ai/tools/tts/field-reference); Text-to-speech agent tool and Gateway RPC (https://docs.openclaw.ai/tools/tts/api)

#### Video generation
- **What it does (docs):** "Generate videos via video_generate from text, image, or video references across 18 provider backends" / "OpenClaw agents generate videos from text prompts, reference images, or existing videos through `video_generate`. Eighteen provider backends are supported; the agent picks the right one automatically based on config and available API keys."
- **URL:** https://docs.openclaw.ai/tools/video-generation
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Image, video, and music generation tools" surface, M2 Alpha (area: Media Operation Lifecycle and Delivery, Media Routing and Discovery); "Media understanding and media generation" surface, M2 Alpha (area: Media Generation); "OpenRouter provider path" surface, M3 Beta (area: Media Generation and Speech). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Tool catalogs and workflows**

#### Code Mode
- **What it does (docs):** "Index of the OpenClaw Code Mode documentation, one page per reader job" / "Code mode is an experimental OpenClaw agent-runtime feature. When enabled, the model no longer sees every enabled tool schema."
- **URL:** https://docs.openclaw.ai/tools/code-mode
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Code mode is an experimental OpenClaw agent-runtime feature."
- **Sub-pages in the nav:** Code Mode quickstart (https://docs.openclaw.ai/tools/code-mode/quickstart); Code Mode executors (https://docs.openclaw.ai/tools/code-mode/executors); Code Mode configuration (https://docs.openclaw.ai/tools/code-mode/configuration); Code Mode tool surface (https://docs.openclaw.ai/tools/code-mode/tool-surface); Code Mode guest API (https://docs.openclaw.ai/tools/code-mode/guest-api); Code Mode output (https://docs.openclaw.ai/tools/code-mode/output); Code Mode internals (https://docs.openclaw.ai/tools/code-mode/internals); Code Mode troubleshooting (https://docs.openclaw.ai/tools/code-mode/troubleshooting); Code Mode maintainer notes (https://docs.openclaw.ai/tools/code-mode/maintainers)

#### Auto Review
- **What it does (docs):** "Run the installed Auto Review checkpoint against the current sandbox" / "`autoreview` is an optional bundled plugin tool for the canonical Auto Review skill. The installed helper captures and rechecks repository changes inside the calling session's sandbox."
- **URL:** https://docs.openclaw.ai/tools/autoreview
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### LLM task
- **What it does (docs):** "JSON-only LLM tasks for workflows (optional plugin tool)" / "`llm-task` is a bundled **optional plugin tool** that runs a single JSON-only LLM call and returns structured output, optionally validated against a JSON Schema. It gives workflow engines like Lobster an LLM step without custom OpenClaw code per workflow."
- **URL:** https://docs.openclaw.ai/tools/llm-task
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Lobster
- **What it does (docs):** "Typed workflow runtime for OpenClaw with resumable approval and input gates." / "Lobster runs multi-step tool pipelines as one repeatable tool call, with explicit approval/input checkpoints and resume tokens. Checkpoints belong to the Lobster runner, not a separate orchestration registry."
- **URL:** https://docs.openclaw.ai/tools/lobster
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/lobster` (Official external packages)

#### Connect MCP servers
- **What it does (docs):** "Connect MCP servers to OpenClaw from the Control UI, CLI, or config" / "The Model Context Protocol (MCP) is how an agent borrows tools from another program: an MCP server exposes tools, resources, and prompts, and OpenClaw connects to it and makes those tools available to your agents. Server definitions live under `mcp.servers` in config, and the tools they expose go through the same tool-profile and tool-policy controls as ..."
- **URL:** https://docs.openclaw.ai/tools/mcp
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "External apps and interoperability" surface, M2 Alpha (area: Compatibility). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Tool Search
- **What it does (docs):** "Tool Search: compact large OpenClaw tool catalogs behind search, describe, and call" / "Tool Search is an experimental OpenClaw agent runtime feature. It gives agents one compact way to discover and call large tool catalogs."
- **URL:** https://docs.openclaw.ai/tools/tool-search
- **Who runs it:** Search tool runs in the user Gateway; queries go to the named search service.
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Tool Search is an experimental OpenClaw agent runtime feature."

**Nav subgroup: Context and reasoning**

#### Tool-loop detection
- **What it does (docs):** "How to enable guardrails that detect repetitive tool-call loops" / "After three consecutive identical tool errors (the same tool, arguments, and error result), OpenClaw blocks that exact action and gives the model one recovery opportunity. It can change its approach, ask for clarification, or answer without the tool."
- **URL:** https://docs.openclaw.ai/tools/loop-detection
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Thinking levels
- **What it does (docs):** "Directive syntax for /think, /fast, /verbose, /trace, and reasoning visibility" / "For custom providers using `api: "openai-completions"`, a model marked `reasoning: true` sends `reasoning_effort` when thinking is enabled without needing `compat.supportsReasoningEffort: true`. An explicit `compat.supportsReasoningEffort: false` on the model disables this control."
- **URL:** https://docs.openclaw.ai/tools/thinking
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Tokenjuice
- **What it does (docs):** "Compact noisy exec and bash tool results with the optional Tokenjuice plugin" / "`tokenjuice` is an optional external plugin that compacts noisy `exec` and `bash` tool results after the command has already run."
- **URL:** https://docs.openclaw.ai/tools/tokenjuice
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/tokenjuice` (Official external packages)

#### Trajectory bundles
- **What it does (docs):** "Export redacted trajectory bundles for debugging an OpenClaw agent session" / "Trajectory capture is OpenClaw's per-session flight recorder. It records a structured timeline for each agent run, then `/export-trajectory` packages the current session into a redacted support bundle covering:"
- **URL:** https://docs.openclaw.ai/tools/trajectory
- **Who runs it:** User machine (the Gateway host or a client of it).

**Nav subgroup: Chat and UI tools**

#### Ask user
- **What it does (docs):** "How ask_user pauses an agent turn for a structured human decision" / "`ask_user` lets the agent ask the human one to three structured questions and wait for the answers. It is for decisions that genuinely belong to the user, not routine confirmation or information the agent can derive from the request, code, or a sensible default."
- **URL:** https://docs.openclaw.ai/tools/ask-user
- **Who runs it:** User machine (the Gateway host or a client of it).

#### BTW side questions
- **What it does (docs):** "Ephemeral side questions with /btw" / "`/btw` (alias `/side`) asks a quick side question about the **current session** without adding it to conversation history. It is modeled after Claude Code's `/btw`, adapted to OpenClaw's Gateway and multi-channel architecture."
- **URL:** https://docs.openclaw.ai/tools/btw
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Progress card
- **What it does (docs):** "Maintain one durable plan and status card for a session" / "`progress_card` is the single agent status tool for a session. It stores an ordered step plan, a compact Markdown note, or both."
- **URL:** https://docs.openclaw.ai/tools/progress-card
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Background Work). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Reactions
- **What it does (docs):** "Reaction tool semantics across all supported channels" / "The agent adds and removes emoji reactions with the `message` tool's `react` action. Behavior varies by channel."
- **URL:** https://docs.openclaw.ai/tools/reactions
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Google Chat" surface, M2 Alpha (area: Native Controls and Approvals); "Telegram" surface, M3 Beta (area: Native Controls and Approvals). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Screen
- **What it does (docs):** "Let an agent arrange the connected Control UI" / "The `screen` tool lets an agent arrange the browser-based Control UI. It is a typed layout and navigation surface, not screenshot capture or browser automation."
- **URL:** https://docs.openclaw.ai/tools/screen
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Show widget
- **What it does (docs):** "Show HTML widgets on supported chat surfaces or pin native data reports to dashboards" / "`show_widget` is a core tool that shows a self-contained HTML widget on the user's current surface. OpenClaw renders it inline in the Control UI and in iOS, Android, macOS, and Linux Quick Chat transcripts."
- **URL:** https://docs.openclaw.ai/tools/show-widget
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Theme
- **What it does (docs):** "Let an agent select plugin themes or create a personal OpenClaw theme" / "The `theme` tool lets an agent list, inspect, select, and create OpenClaw appearance themes. Settings and the agent use the same catalog of built-in, plugin, and personal themes."
- **URL:** https://docs.openclaw.ai/tools/theme
- **Who runs it:** User machine (the Gateway host or a client of it).

**Nav subgroup: Browsing and fetching pages**

#### Browser (OpenClaw-managed)
- **What it does (docs):** "Index of the OpenClaw browser documentation, one page per reader job" / "OpenClaw can run a **dedicated Chrome/Brave/Edge/Chromium profile** that the agent controls. It runs through a small local control service inside the Gateway (loopback only) and is isolated from your personal browser."
- **URL:** https://docs.openclaw.ai/tools/browser
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Browser Automation); "Windows via WSL2" surface, M3 Beta (area: Browser and Control UI). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Browser setup (https://docs.openclaw.ai/tools/browser/setup); Browser profiles (https://docs.openclaw.ai/tools/browser/profiles); Multi-profile and existing-session attach (https://docs.openclaw.ai/tools/browser/existing-session); Browser configuration (https://docs.openclaw.ai/tools/browser/configuration); Remote and hosted browsers (https://docs.openclaw.ai/tools/browser/remote); Lightweight browsers (https://docs.openclaw.ai/tools/browser/lightweight); Browser security (https://docs.openclaw.ai/tools/browser/security); Isolation and browser selection (https://docs.openclaw.ai/tools/browser/isolation); Browser agent tools (https://docs.openclaw.ai/tools/browser/agent-tools); Browser troubleshooting (https://docs.openclaw.ai/tools/browser/troubleshooting)

#### Browser control API
- **What it does (docs):** "OpenClaw browser control API, CLI reference, and scripting actions" / "For setup, configuration, and troubleshooting, see Browser. This page is the reference for the local control HTTP API, the `openclaw browser` CLI, and scripting patterns (snapshots, refs, waits, debug flows)."
- **URL:** https://docs.openclaw.ai/tools/browser-control
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Browser Automation); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Gateway Auth and Remote Access). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Browser troubleshooting
- **What it does (docs):** "Fix Chrome/Brave/Edge/Chromium CDP startup issues for OpenClaw browser control on Linux" / "On Ubuntu and most Linux distros, `apt install chromium` installs a snap wrapper, not a real browser:"
- **URL:** https://docs.openclaw.ai/tools/browser-linux-troubleshooting
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Browser login
- **What it does (docs):** "Manual logins for browser automation + X/Twitter posting" / "When a site requires login, sign in manually in the host browser's `openclaw` profile. Automated logins often trigger anti-bot defenses and can lock the account."
- **URL:** https://docs.openclaw.ai/tools/browser-login
- **Who runs it:** User machine (the Gateway host or a client of it).

#### WSL2 + Windows + remote Chrome CDP troubleshooting
- **What it does (docs):** "Troubleshoot WSL2 Gateway + Windows Chrome remote CDP in layers" / "In the common split-host setup, OpenClaw Gateway runs inside WSL2, Chrome runs on Windows, and browser control must cross the WSL2/Windows boundary. Several independent problems can surface at once (see issue #39369): CDP transport, Control UI origin security, and token/pairing can each fail on their own while producing similar-looking errors."
- **URL:** https://docs.openclaw.ai/tools/browser-wsl2-windows-remote-cdp-troubleshooting
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Windows via WSL2" surface, M3 Beta (area: Browser and Control UI). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Chrome Extension
- **What it does (docs):** "Chrome extension: securely automate signed-in tabs with automatic local pairing" / "The OpenClaw Chrome extension lets the browser tool automate eligible tabs in your signed-in Chrome profile. It uses `chrome.debugger`, so it does not require Chrome's blocking remote-debugging consent prompt."
- **URL:** https://docs.openclaw.ai/tools/chrome-extension
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** Google Chrome, Chrome for Testing, or Chromium; OpenClaw installed on the same machine as Chrome, or an OpenClaw browser node; macOS/Linux, or Windows with the self-contained OpenClaw native bootstrap executable; For browsers other than Google Chrome on macOS, launch the browser at least

#### Firecrawl
- **What it does (docs):** "Firecrawl search, scrape, and web_fetch fallback" / "OpenClaw can use Firecrawl in three ways:"
- **URL:** https://docs.openclaw.ai/tools/firecrawl
- **Who runs it:** Search tool runs in the user Gateway; queries go to the named search service.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/firecrawl-plugin` (Official external packages)
- **Status (maturity scorecard, which links this page):** "Web search tools" surface, M3 Beta (area: Network Safety, Search Providers). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Web fetch
- **What it does (docs):** "web_fetch tool -- HTTP fetch with readable content extraction" / "`web_fetch` does a plain HTTP GET and extracts readable content (HTML to markdown or text). It does **not** execute JavaScript."
- **URL:** https://docs.openclaw.ai/tools/web-fetch
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Web search tools" surface, M3 Beta (area: Network Safety, Setup and Diagnostics). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Web search**

#### Web search
- **What it does (docs):** "web_search, x_search, and web_fetch -- search the web, search X posts, or fetch page content" / "`web_search` searches the web with your configured provider and returns normalized results, cached by query for 15 minutes (configurable). OpenClaw also bundles `x_search` for X (formerly Twitter) posts and `web_fetch` for lightweight URL fetching."
- **URL:** https://docs.openclaw.ai/tools/web
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Web search tools" surface, M3 Beta (area: Network Safety, Search Providers). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Deep Research
- **What it does (docs):** "Bounded portable research and explicitly enabled provider-managed research" / "Deep Research is a bundled, default-enabled plugin with a lazy `deep_research` tool. Startup scans bounded local job state and reconstructs due wakes."
- **URL:** https://docs.openclaw.ai/tools/deep-research
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Brave search
- **What it does (docs):** "Brave Search API setup for web_search" / "OpenClaw supports Brave Search API as a `web_search` provider."
- **URL:** https://docs.openclaw.ai/tools/brave-search
- **Who runs it:** Search tool runs in the user Gateway; queries go to the named search service.
- **Status (maturity scorecard, which links this page):** "Web search tools" surface, M3 Beta (area: Search Providers, Setup and Diagnostics). Source: https://docs.openclaw.ai/maturity/taxonomy

#### DuckDuckGo search
- **What it does (docs):** "DuckDuckGo web search -- key-free provider (experimental, HTML-based)" / "OpenClaw supports DuckDuckGo as a **key-free** `web_search` provider. No API key or account is required."
- **URL:** https://docs.openclaw.ai/tools/duckduckgo-search
- **Who runs it:** Search tool runs in the user Gateway; queries go to the named search service.
- **Status (maturity scorecard, which links this page):** "Web search tools" surface, M3 Beta (area: Search Providers). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "DuckDuckGo is an experimental, unofficial integration that scrapes DuckDuckGo's non-JavaScript HTML search pages -- not an official API."

#### Exa search
- **What it does (docs):** "Exa AI search -- neural and keyword search with content extraction" / "Exa AI is a `web_search` provider. It offers the `auto`, `neural`, `fast`, `deep`, `deep-reasoning`, and `instant` search modes described in Search modes."
- **URL:** https://docs.openclaw.ai/tools/exa-search
- **Who runs it:** Search tool runs in the user Gateway; queries go to the named search service.
- **Status (maturity scorecard, which links this page):** "Web search tools" surface, M3 Beta (area: Search Providers). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Gemini search
- **What it does (docs):** "Gemini web search with Google Search grounding" / "OpenClaw supports Gemini models with built-in Google Search grounding, which returns AI-synthesized answers backed by live Google Search results with citations."
- **URL:** https://docs.openclaw.ai/tools/gemini-search
- **Who runs it:** Search tool runs in the user Gateway; queries go to the named search service.
- **Status (maturity scorecard, which links this page):** "Google provider path" surface, M3 Beta (area: Model Routing and Endpoints); "Web search tools" surface, M3 Beta (area: Search Providers). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Grok search
- **What it does (docs):** "Grok web search via xAI web-grounded responses" / "OpenClaw supports Grok as a `web_search` provider, using xAI web-grounded responses to produce AI-synthesized answers backed by live search results with citations."
- **URL:** https://docs.openclaw.ai/tools/grok-search
- **Who runs it:** Search tool runs in the user Gateway; queries go to the named search service.
- **Status (maturity scorecard, which links this page):** "Web search tools" surface, M3 Beta (area: Search Providers). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Kimi search
- **What it does (docs):** "Kimi web search via Moonshot web search" / "Kimi is a `web_search` provider backed by Moonshot's `POST /tools/search` endpoint. It returns a structured list of results with titles, URLs, descriptions, and source metadata."
- **URL:** https://docs.openclaw.ai/tools/kimi-search
- **Who runs it:** Search tool runs in the user Gateway; queries go to the named search service.
- **Status (maturity scorecard, which links this page):** "Web search tools" surface, M3 Beta (area: Search Providers). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "model is deprecated and ignored."

#### MiniMax search
- **What it does (docs):** "MiniMax Search via the Token Plan search API" / "OpenClaw supports MiniMax as a `web_search` provider through the MiniMax Token Plan search API. It returns structured search results with titles, URLs, snippets, and related queries."
- **URL:** https://docs.openclaw.ai/tools/minimax-search
- **Who runs it:** Search tool runs in the user Gateway; queries go to the named search service.
- **Status (maturity scorecard, which links this page):** "Web search tools" surface, M3 Beta (area: Search Providers). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Ollama web search
- **What it does (docs):** "Ollama Web Search via a local Ollama host or the hosted Ollama API" / "OpenClaw supports **Ollama Web Search** as a bundled `web_search` provider, returning titles, URLs, and snippets from Ollama's web-search API."
- **URL:** https://docs.openclaw.ai/tools/ollama-search
- **Who runs it:** Search tool runs in the user Gateway; queries go to the named search service.
- **Status (maturity scorecard, which links this page):** "Web search tools" surface, M3 Beta (area: Search Providers). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Parallel search
- **What it does (docs):** "Parallel Search and web-grounded typed Decisions" / "The Parallel plugin provides two Parallel `web_search` providers, both returning ranked, LLM-optimized excerpts from a web index built for AI agents:"
- **URL:** https://docs.openclaw.ai/tools/parallel-search
- **Who runs it:** Search tool runs in the user Gateway; queries go to the named search service.

#### Perplexity search
- **What it does (docs):** "Perplexity Search API and Sonar/OpenRouter compatibility for web_search" / "OpenClaw supports the Perplexity Search API as a `web_search` provider. It returns structured results with `title`, `url`, and `snippet` fields."
- **URL:** https://docs.openclaw.ai/tools/perplexity-search
- **Who runs it:** Search tool runs in the user Gateway; queries go to the named search service.
- **Status (maturity scorecard, which links this page):** "Web search tools" surface, M3 Beta (area: Search Providers, Setup and Diagnostics). Source: https://docs.openclaw.ai/maturity/taxonomy

#### SearXNG search
- **What it does (docs):** "SearXNG web search -- self-hosted, key-free meta-search provider" / "OpenClaw supports SearXNG as a **self-hosted, key-free** `web_search` provider. SearXNG is an open-source meta-search engine that aggregates results from Google, Bing, DuckDuckGo, and other sources."
- **URL:** https://docs.openclaw.ai/tools/searxng-search
- **Who runs it:** Search tool runs in the user Gateway; queries go to the named search service.
- **Status (maturity scorecard, which links this page):** "Web search tools" surface, M3 Beta (area: Network Safety, Search Providers). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Tavily
- **What it does (docs):** "Tavily search and extract tools" / "Tavily is a search API designed for AI applications. OpenClaw exposes it in two ways:"
- **URL:** https://docs.openclaw.ai/tools/tavily
- **Who runs it:** Search tool runs in the user Gateway; queries go to the named search service.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/tavily-plugin` (Official external packages)
- **Status (maturity scorecard, which links this page):** "Web search tools" surface, M3 Beta (area: Search Providers, Setup and Diagnostics). Source: https://docs.openclaw.ai/maturity/taxonomy

**Group: Agent coordination**

#### Agent send
- **What it does (docs):** "Run agent turns from the CLI and optionally deliver replies to channels" / "`openclaw agent` runs a single agent turn from the command line without an inbound chat message. Use it for scripted workflows, testing, and programmatic delivery."
- **URL:** https://docs.openclaw.ai/tools/agent-send
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Goal
- **What it does (docs):** "Session goals: durable per-session objectives, /goal controls, model goal tools, token budgets, and TUI status" / "A **goal** is one durable objective attached to the current OpenClaw session. It gives the agent and the operator a shared target for long-running work."
- **URL:** https://docs.openclaw.ai/tools/goal
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: Context Engine). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Steer
- **What it does (docs):** "Steer an active run without changing queue mode" / "`/steer` first tries to send guidance to an already-active run. It is for "adjust this run while it is still working" moments."
- **URL:** https://docs.openclaw.ai/tools/steer
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Sub-agents
- **What it does (docs):** "Index of the OpenClaw sub-agent documentation, one page per reader job" / "Sub-agents are background agent runs spawned from an existing agent run. Each one runs in its own session (`agent::subagent:`) and, by default, **announces** its result back to the requester for review."
- **URL:** https://docs.openclaw.ai/tools/subagents
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Agent Runtime" surface, M3 Beta (area: External Runtimes and Subagents, Provider Auth); "Discord" surface, M4 Stable (area: Conversation Routing and Delivery). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Sub-agent slash command (https://docs.openclaw.ai/tools/subagents/slash-command); Sub-agent tool reference (https://docs.openclaw.ai/tools/subagents/tool-reference); Thread-bound sub-agent sessions (https://docs.openclaw.ai/tools/subagents/thread-bound-sessions); Nested sub-agents and authentication (https://docs.openclaw.ai/tools/subagents/nesting); Sub-agent announce (https://docs.openclaw.ai/tools/subagents/announce); Sub-agent tool policy (https://docs.openclaw.ai/tools/subagents/tool-policy); Sub-agent concurrency, recovery, and stopping (https://docs.openclaw.ai/tools/subagents/operations)

#### Swarm
- **What it does (docs):** "Orchestrate concurrent sub-agents from Code Mode scripts with structured results, bounded fan-out, and live progress" / "Swarm orchestrates many sub-agents from a Code Mode script. It is enabled by default, with an explicit opt-out."
- **URL:** https://docs.openclaw.ai/tools/swarm
- **Who runs it:** User machine (the Gateway host or a client of it).

#### ACP agents
- **What it does (docs):** "Index of the OpenClaw ACP agents documentation, one page per reader job" / "Agent Client Protocol (ACP) sessions let OpenClaw run external coding harnesses (Claude Code, Cursor, Copilot, Droid, OpenClaw ACP, OpenCode, Gemini CLI, and other supported acpx harnesses) through an ACP backend plugin. The ACP runtime owns each session and its cancellation."
- **URL:** https://docs.openclaw.ai/tools/acp-agents
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Discord" surface, M4 Stable (area: Conversation Routing and Delivery). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** ACP agents quickstart (https://docs.openclaw.ai/tools/acp-agents/quickstart); ACP agents operator runbook (https://docs.openclaw.ai/tools/acp-agents/runbook); ACP agents bindings (https://docs.openclaw.ai/tools/acp-agents/bindings); ACP agents sessions (https://docs.openclaw.ai/tools/acp-agents/sessions); ACP agents delivery model (https://docs.openclaw.ai/tools/acp-agents/delivery); ACP agents controls (https://docs.openclaw.ai/tools/acp-agents/controls); ACP agents troubleshooting (https://docs.openclaw.ai/tools/acp-agents/troubleshooting)

#### ACP agents — setup
- **What it does (docs):** "Setting up ACP agents: acpx harness config, plugin setup, permissions" / "For the overview, operator runbook, and concepts, see ACP agents."
- **URL:** https://docs.openclaw.ai/tools/acp-agents-setup
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Multi-agent sandbox and tools
- **What it does (docs):** "Per-agent sandbox + tool restrictions, precedence, and examples" / "Each agent in a multi-agent setup can override the global sandbox and tool policy. This page covers per-agent configuration, precedence rules, and examples."
- **URL:** https://docs.openclaw.ai/tools/multi-agent-sandbox-tools
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Page status field:** `active`
- **Status (maturity scorecard, which links this page):** "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Sandbox and Tool Policy). Source: https://docs.openclaw.ai/maturity/taxonomy

### Tab: ClawHub

**Group: Overview**

#### ClawHub
- **What it does (docs):** "Public ClawHub overview for discovery, install, publish, security, and the clawhub CLI." / "ClawHub is the public registry for OpenClaw skills and plugins."
- **URL:** https://docs.openclaw.ai/clawhub
- **Who runs it:** Hosted registry service at clawhub.ai; the `clawhub` CLI and `openclaw` install commands run on the user machine.

#### Quickstart
- **What it does (docs):** "Start using ClawHub: find, install, update, and publish skills or plugins." / "ClawHub is a registry for OpenClaw skills and plugins."
- **URL:** https://docs.openclaw.ai/clawhub/quickstart
- **Who runs it:** Hosted registry service at clawhub.ai; the `clawhub` CLI and `openclaw` install commands run on the user machine.

#### How ClawHub Works
- **What it does (docs):** "How ClawHub listings, versions, installs, publishing, scans, and updates work." / "ClawHub is the registry layer for OpenClaw skills and plugins. It gives users a place to discover packages, gives publishers a place to release versions, and gives OpenClaw enough metadata to install and update those packages safely."
- **URL:** https://docs.openclaw.ai/clawhub/how-it-works
- **Who runs it:** Hosted registry service at clawhub.ai; the `clawhub` CLI and `openclaw` install commands run on the user machine.

**Group: Using ClawHub**

#### CLI
- **What it does (docs):** "CLI reference: commands, flags, config, and lockfile behavior." / "CLI package: `clawhub`, bin: `clawhub`."
- **URL:** https://docs.openclaw.ai/clawhub/cli
- **Who runs it:** Hosted registry service at clawhub.ai; the `clawhub` CLI and `openclaw` install commands run on the user machine.

#### Publishing
- **What it does (docs):** "How ClawHub publishing works for skills, plugins, owners, scopes, releases, and review." / "Publishing sends a skill folder or plugin package to ClawHub under the owner you choose. ClawHub checks that your token can publish for that owner, validates the metadata, name, version, files, and source information, then stores the release as pending and runs automated security checks on that exact artifact."
- **URL:** https://docs.openclaw.ai/clawhub/publishing
- **Who runs it:** Hosted registry service at clawhub.ai; the `clawhub` CLI and `openclaw` install commands run on the user machine.
- **Status (maturity scorecard, which links this page):** "ClawHub" surface, M2 Alpha (area: Compatibility and Trust, Publishing); "Plugins" surface, M3 Beta (area: Publishing plugins). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "clear_categories inputs are deprecated for plugins."

#### Skill format
- **What it does (docs):** "Skill folder format, required files, supporting artifacts, limits." / "A skill is a folder."
- **URL:** https://docs.openclaw.ai/clawhub/skill-format
- **Who runs it:** Hosted registry service at clawhub.ai; the `clawhub` CLI and `openclaw` install commands run on the user machine.
- **Status (maturity scorecard, which links this page):** "ClawHub" surface, M2 Alpha (area: Publishing). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Auth
- **What it does (docs):** "ClawHub sign-in, API tokens, CLI login, token storage, and revocation." / "ClawHub uses GitHub for web sign-in. The CLI uses ClawHub API tokens created through that signed-in account."
- **URL:** https://docs.openclaw.ai/clawhub/auth
- **Who runs it:** Hosted registry service at clawhub.ai; the `clawhub` CLI and `openclaw` install commands run on the user machine.

#### Telemetry
- **What it does (docs):** "Install telemetry collected by the ClawHub CLI and how to opt out." / "ClawHub uses minimal CLI telemetry to compute aggregate skill and plugin install counts."
- **URL:** https://docs.openclaw.ai/clawhub/telemetry
- **Who runs it:** Hosted registry service at clawhub.ai; the `clawhub` CLI and `openclaw` install commands run on the user machine.

#### Troubleshooting
- **What it does (docs):** "Troubleshooting ClawHub sign-in, install, publish, update, and API issues." / "Open the verification URL printed by the CLI, sign in with GitHub if needed, and select **Authorize** for the displayed code. You can use a browser on another device; no localhost callback is required."
- **URL:** https://docs.openclaw.ai/clawhub/troubleshooting
- **Who runs it:** Hosted registry service at clawhub.ai; the `clawhub` CLI and `openclaw` install commands run on the user machine.

**Group: API and trust**

#### API v1
- **What it does (docs):** "Public REST API (v1) overview and conventions." / "Base: `https://clawhub.ai`"
- **URL:** https://docs.openclaw.ai/clawhub/api
- **Who runs it:** Hosted registry service at clawhub.ai; the `clawhub` CLI and `openclaw` install commands run on the user machine.

#### HTTP API
- **What it does (docs):** "HTTP API reference (public + CLI endpoints + auth)." / "Base URL: `https://clawhub.ai` (default)."
- **URL:** https://docs.openclaw.ai/clawhub/http-api
- **Who runs it:** Hosted registry service at clawhub.ai; the `clawhub` CLI and `openclaw` install commands run on the user machine.
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Publishes a code-plugin, bundle-plugin, or experimental Template release."

#### Acceptable Usage
- **What it does (docs):** "Marketplace policy: what ClawHub allows and what it will not host." / "ClawHub hosts skills, plugins, packages, and marketplace metadata for OpenClaw. Use this page to decide whether content or publishing behavior belongs on ClawHub."
- **URL:** https://docs.openclaw.ai/clawhub/acceptable-usage
- **Who runs it:** Hosted registry service at clawhub.ai; the `clawhub` CLI and `openclaw` install commands run on the user machine.

#### Moderation and Account Safety
- **What it does (docs):** "How ClawHub reports, moderation holds, hidden listings, bans, and account standing work." / "ClawHub is open to publishing, but public discovery and install surfaces still need guardrails. Reports, moderation holds, hidden listings, and account actions help protect users when a release or account appears unsafe, misleading, or out of policy."
- **URL:** https://docs.openclaw.ai/clawhub/moderation
- **Who runs it:** Hosted registry service at clawhub.ai; the `clawhub` CLI and `openclaw` install commands run on the user machine.

#### Security Audits
- **What it does (docs):** "How to understand ClawHub security audit results before installing a skill or plugin." / "ClawHub security audits help you decide whether a skill or plugin is safe enough to install. They show what a release does, what authority it asks for, and whether anything deserves extra attention before it can access files, accounts, credentials, code, or external services."
- **URL:** https://docs.openclaw.ai/clawhub/security-audits
- **Who runs it:** Hosted registry service at clawhub.ai; the `clawhub` CLI and `openclaw` install commands run on the user machine.
- **Status (maturity scorecard, which links this page):** "ClawHub" surface, M2 Alpha (area: Compatibility and Trust). Source: https://docs.openclaw.ai/maturity/taxonomy

### Tab: Models

**Group: Overview**

#### Provider directory
- **What it does (docs):** "Model providers (LLMs) supported by OpenClaw" / "OpenClaw can use many LLM providers. Pick a provider, authenticate, then set the default model as `provider/model`."
- **URL:** https://docs.openclaw.ai/providers
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Status (maturity scorecard, which links this page):** "Long-tail hosted providers" surface, M2 Alpha (area: Hosted LLM Providers, Hosted Media Providers). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Model provider quickstart
- **What it does (docs):** "Model providers (LLMs) supported by OpenClaw" / "Pick a provider, authenticate, then set the default model as `provider/model`."
- **URL:** https://docs.openclaw.ai/providers/models
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.

**Group: Concepts and configuration**

#### Models CLI
- **What it does (docs):** "How OpenClaw resolves provider/model refs, config keys, and the `/model` chat command" / "Auth profile rotation, cooldowns, and how that interacts with fallbacks."
- **URL:** https://docs.openclaw.ai/concepts/models
- **Who runs it:** User machine (Gateway configuration).
- **Status (maturity scorecard, which links this page):** "Agent Runtime" surface, M3 Beta (area: Hosted Provider Execution, Local and Self-hosted Providers); "Anthropic provider path" surface, M3 Beta (area: Model and Runtime Selection); "OpenAI and Codex provider path" surface, M3 Beta (area: Model and Auth); "OpenRouter provider path" surface, M3 Beta (area: Provider Setup and Auth). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "Default and configured picker views hide catalog rows marked deprecated or disabled."

#### Recommended models
- **What it does (docs):** "How the curated recommended model list is reviewed, ordered, and published" / "OpenClaw keeps one global, ordered list of recommended models. It names the models OpenClaw suggests first, independent of which provider serves them, so one entry covers every provider that serves that model."
- **URL:** https://docs.openclaw.ai/concepts/recommended-models
- **Who runs it:** User machine (Gateway configuration).
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "deprecated, disabled, or replaced rows, are skipped and logged."

#### Decision models
- **What it does (docs):** "Choose decision models and define typed choices, scores, and Boolean judgments" / "A **decision model** evaluates supplied evidence against a rubric and returns a typed answer: a choice, a score, or a Boolean probability. Use it for bounded judgments such as routing a request, scoring its urgency, or checking whether it meets a condition."
- **URL:** https://docs.openclaw.ai/concepts/decision-models
- **Who runs it:** User machine (Gateway configuration).
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Decision assistance opt-in."

#### Model providers
- **What it does (docs):** "Index of the model provider reference: quick rules, Control UI and keys, bundled provider plugins, and custom providers" / "Reference for **LLM/model providers** (not chat channels like WhatsApp/Telegram). For model selection rules, see Models."
- **URL:** https://docs.openclaw.ai/concepts/model-providers
- **Who runs it:** User machine (Gateway configuration).
- **Status (maturity scorecard, which links this page):** "Anthropic provider path" surface, M3 Beta (area: Request Transport and Turn Semantics); "Google provider path" surface, M3 Beta (area: Direct Gemini Runtime, Model Routing and Endpoints); "Long-tail hosted providers" surface, M2 Alpha (area: Hosted LLM Providers, Provider Operations); "OpenRouter provider path" surface, M3 Beta (area: Chat Runtime and Normalization, Provider Setup and Auth). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Quick rules (https://docs.openclaw.ai/concepts/model-providers/quick-rules); Control UI and API keys (https://docs.openclaw.ai/concepts/model-providers/control-ui-and-keys); Official provider plugins (https://docs.openclaw.ai/concepts/model-providers/official-provider-plugins); Custom providers and local runtimes (https://docs.openclaw.ai/concepts/model-providers/custom-providers)

#### Model failover
- **What it does (docs):** "How OpenClaw rotates auth profiles and falls back across models" / "OpenClaw handles failures in two stages:"
- **URL:** https://docs.openclaw.ai/concepts/model-failover
- **Who runs it:** User machine (Gateway configuration).
- **Status (maturity scorecard, which links this page):** "OpenRouter provider path" surface, M3 Beta (area: Provider Recovery and Diagnostics). Source: https://docs.openclaw.ai/maturity/taxonomy

**Group: Providers**

**Nav subgroup: Chat and coding models**

#### Abliteration
- **What it does (docs):** "Abliteration setup, model selection, reasoning, and prompt caching" / "Abliteration serves abliterated open-weight models through an OpenAI-compatible API. OpenClaw provides it as an official external provider plugin with a static model catalog and API-key authentication."
- **URL:** https://docs.openclaw.ai/providers/abliteration
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/abliteration-provider` (Official external packages)
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "Large v2 and the deprecated Large model are text-only."

#### Alibaba Model Studio
- **What it does (docs):** "Alibaba Model Studio Wan video generation in OpenClaw" / "The bundled `alibaba` plugin registers a video-generation provider for Wan models on Alibaba Model Studio (the international name for DashScope). It is enabled by default; only an API key is needed."
- **URL:** https://docs.openclaw.ai/providers/alibaba
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Anthropic
- **What it does (docs):** "Use Anthropic Claude via API keys or Claude CLI in OpenClaw" / "Anthropic builds the **Claude** model family. OpenClaw supports two auth routes:"
- **URL:** https://docs.openclaw.ai/providers/anthropic
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "Anthropic provider path" surface, M3 Beta (area: Media Inputs, Model and Runtime Selection); "Agent Runtime" surface, M3 Beta (area: External Runtimes and Subagents, Hosted Provider Execution). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "including older IDs absent from the menu; deprecated rows stay hidden."

#### Anthropic Vertex plugin reference
- **What it does (docs):** "OpenClaw Anthropic Vertex provider plugin for Claude models on Google Vertex AI."
- **URL:** https://docs.openclaw.ai/plugins/reference/anthropic-vertex
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/anthropic-vertex-provider` (Official external packages)

#### Arcee AI
- **What it does (docs):** "Arcee AI setup (auth + model selection)" / "Arcee AI provides the Trinity family of mixture-of-experts models through an OpenAI-compatible API. All Trinity models are Apache 2.0 licensed."
- **URL:** https://docs.openclaw.ai/providers/arcee
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/arcee-provider` (Official external packages)

#### Baseten
- **What it does (docs):** "Baseten setup for DeepSeek V4.1 Flash and hosted Model APIs" / "Baseten Model APIs provide hosted, OpenAI-compatible access to frontier models. The official external plugin uses authenticated discovery, so OpenClaw follows the complete model set enabled for your Baseten account."
- **URL:** https://docs.openclaw.ai/providers/baseten
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/baseten-provider` (Official external packages)

#### Amazon Bedrock
- **What it does (docs):** "Use Amazon Bedrock (Converse API) models with OpenClaw" / "OpenClaw can use **Amazon Bedrock** models via its **Bedrock Converse** streaming provider. Bedrock auth uses the **AWS SDK default credential chain**, not an API key."
- **URL:** https://docs.openclaw.ai/providers/bedrock
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.

#### Amazon Bedrock Mantle
- **What it does (docs):** "Use Amazon Bedrock Mantle OpenAI-compatible and Claude Messages models with OpenClaw" / "OpenClaw includes a bundled **Amazon Bedrock Mantle** provider that connects to the Mantle OpenAI-compatible endpoint. Mantle hosts open-source and third-party models (GPT-OSS, Qwen, Kimi, GLM, and similar) through a standard `/v1/chat/completions` surface backed by Bedrock infrastructure."
- **URL:** https://docs.openclaw.ai/providers/bedrock-mantle
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.

#### Cerebras
- **What it does (docs):** "Cerebras setup (auth + model selection)" / "Cerebras provides high-speed OpenAI-compatible inference on custom inference hardware. The plugin discovers native model metadata and pricing, with a bundled catalog for offline fallback."
- **URL:** https://docs.openclaw.ai/providers/cerebras
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/cerebras-provider` (Official external packages)

#### Chutes
- **What it does (docs):** "Chutes setup (OAuth or API key, model discovery, aliases)" / "Chutes exposes open-source model catalogs through an OpenAI-compatible API. OpenClaw supports both browser OAuth and API-key auth."
- **URL:** https://docs.openclaw.ai/providers/chutes
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/chutes-provider` (Official external packages)

#### Cohere
- **What it does (docs):** "Cohere setup (auth + model selection)" / "Cohere provides OpenAI-compatible inference through its Compatibility API. OpenClaw provides Cohere as an official external plugin."
- **URL:** https://docs.openclaw.ai/providers/cohere
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/cohere-provider` (Official external packages)

#### DeepInfra
- **What it does (docs):** "Use DeepInfra's unified API to access the most popular open source and frontier models in OpenClaw" / "DeepInfra routes requests to popular open source and frontier models behind a single OpenAI-compatible endpoint and API key. Most OpenAI SDKs work against it by switching the base URL."
- **URL:** https://docs.openclaw.ai/providers/deepinfra
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/deepinfra-provider` (Official external packages)

#### DeepSeek
- **What it does (docs):** "DeepSeek setup (auth + model selection)" / "DeepSeek provides powerful AI models with an OpenAI-compatible API."
- **URL:** https://docs.openclaw.ai/providers/deepseek
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/deepseek-provider` (Official external packages)

#### Featherless AI
- **What it does (docs):** "Featherless AI setup, model selection, and tool calling" / "Featherless AI serves open models through an OpenAI-compatible API. OpenClaw installs Featherless as an official external provider plugin and keeps the built-in catalog small while accepting exact model ids from Featherless at runtime."
- **URL:** https://docs.openclaw.ai/providers/featherless
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/featherless-provider` (Official external packages)

#### Fireworks
- **What it does (docs):** "Fireworks setup (auth + model selection)" / "Fireworks exposes open-weight and routed models through an OpenAI-compatible API. Install the official Fireworks provider plugin to use the current Fire Pass GLM router and any Fireworks model or router id at runtime."
- **URL:** https://docs.openclaw.ai/providers/fireworks
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/fireworks-provider` (Official external packages)

#### GitHub Copilot
- **What it does (docs):** "Sign in to GitHub Copilot from OpenClaw using the device flow or non-interactive token import" / "GitHub Copilot is GitHub's AI coding assistant. It provides access to Copilot models for your GitHub account and plan."
- **URL:** https://docs.openclaw.ai/providers/github-copilot
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### GMI Cloud
- **What it does (docs):** "Use GMI Cloud's OpenAI-compatible API with OpenClaw" / "GMI Cloud is a hosted inference platform for frontier and open-weight models behind an OpenAI-compatible API. In OpenClaw it is an official external provider plugin: install it once, store credentials through normal model auth, and use model refs like `gmi/openai/gpt-5.6-sol`."
- **URL:** https://docs.openclaw.ai/providers/gmi
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/gmi-provider` (Official external packages)

#### Google (Gemini)
- **What it does (docs):** "Google Gemini setup (AI Studio API key, Vertex AI, optional CLI runtime, and multimodal tools)" / "The Google plugin provides access to Gemini models through Google AI Studio, plus image generation, media understanding (image/audio/video), text-to-speech, and web search via Gemini Grounding."
- **URL:** https://docs.openclaw.ai/providers/google
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "Agent Runtime" surface, M3 Beta (area: External Runtimes and Subagents, Hosted Provider Execution); "Google provider path" surface, M3 Beta (area: Direct Gemini Runtime, Media, Search, and Realtime); "Voice and realtime talk" surface, M2 Alpha (area: Speech and Transcription, Talk Providers). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Google (Vertex AI)
- **What it does (docs):** "Use Gemini through Google Cloud Vertex AI with Application Default Credentials" / "The bundled Google plugin routes `google-vertex/*` model requests through Google Cloud Vertex AI. This guide covers Application Default Credentials (ADC), including gcloud user credentials, service account keys, and metadata-server credentials on Google Cloud."
- **URL:** https://docs.openclaw.ai/providers/google-vertex
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.

#### Groq
- **What it does (docs):** "Groq setup (auth + model selection + Whisper transcription)" / "Groq provides ultra-fast inference on open-weight models (Llama, Gemma, Kimi, Qwen, GPT OSS, and more) using custom LPU hardware. The Groq plugin registers both an OpenAI-compatible chat provider and an audio media-understanding provider."
- **URL:** https://docs.openclaw.ai/providers/groq
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/groq-provider` (Official external packages)
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "com/docs/models) for newly-added or deprecated models."

#### Hugging Face (inference)
- **What it does (docs):** "Hugging Face Inference setup (auth + model selection)" / "Hugging Face Inference Providers exposes an OpenAI-compatible chat completions router in front of many hosted models (DeepSeek, Llama, and more) under one token. OpenClaw talks to the **chat completions endpoint only**; for text-to-image, embeddings, or speech use the HF inference clients directly."
- **URL:** https://docs.openclaw.ai/providers/huggingface
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Levanto Sage
- **What it does (docs):** "Connect Levanto Sage for native typed decisions" / "The optional Levanto plugin connects Sage to OpenClaw's decision model role. It does not provide chat completions."
- **URL:** https://docs.openclaw.ai/providers/levanto
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/levanto` (Official external packages)

#### LongCat
- **What it does (docs):** "LongCat API setup for LongCat-2.0" / "LongCat provides a hosted API for LongCat-2.0, a reasoning model built for coding and agentic workloads. OpenClaw provides the official LongCat plugin for LongCat's OpenAI-compatible endpoint."
- **URL:** https://docs.openclaw.ai/providers/longcat
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/longcat-provider` (Official external packages)

#### Meta
- **What it does (docs):** "Meta setup, authentication, and Muse Wonder and Muse Spark model selection" / "The **Meta API** uses the OpenAI-compatible **Responses API** (`POST /v1/responses`) for the Muse Wonder and Muse Spark reasoning models. OpenClaw provides Meta as an official external plugin."
- **URL:** https://docs.openclaw.ai/providers/meta
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/meta-provider` (Official external packages)

#### MiniMax
- **What it does (docs):** "Use MiniMax models in OpenClaw" / "The bundled `minimax` plugin registers two chat providers plus six capabilities: image generation, music generation, video generation, image understanding, speech (T2A v2), and web search."
- **URL:** https://docs.openclaw.ai/providers/minimax
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Mistral
- **What it does (docs):** "Use Mistral models and Voxtral transcription with OpenClaw" / "The official external `mistral` plugin registers four contracts: chat completions, media understanding (Voxtral batch transcription), realtime STT for Voice Call (Voxtral Realtime), and memory embeddings (`mistral-embed`)."
- **URL:** https://docs.openclaw.ai/providers/mistral
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/mistral-provider` (Official external packages)

#### Moonshot AI
- **What it does (docs):** "Configure Moonshot Kimi models vs Kimi Coding (separate providers + keys)" / "Moonshot provides the Kimi API with OpenAI-compatible endpoints. Fresh Moonshot onboarding selects `moonshot/kimi-k3`; use `kimi/kimi-for-coding` for the separate Kimi Coding provider."
- **URL:** https://docs.openclaw.ai/providers/moonshot
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/moonshot-provider` (Official external packages)
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "model is deprecated and ignored."

#### NovitaAI
- **What it does (docs):** "Use NovitaAI's OpenAI-compatible API with OpenClaw" / "NovitaAI is a hosted AI infrastructure provider with an OpenAI-compatible API. OpenClaw provides NovitaAI through the official external `@openclaw/novita-provider` plugin."
- **URL:** https://docs.openclaw.ai/providers/novita
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/novita-provider` (Official external packages)

#### NVIDIA
- **What it does (docs):** "Use NVIDIA's OpenAI-compatible API in OpenClaw" / "NVIDIA serves open models for free through an OpenAI-compatible API at `https://integrate.api.nvidia.com/v1`, authenticated with an API key from build.nvidia.com. OpenClaw defaults the NVIDIA provider to Nemotron 3 Ultra, NVIDIA's 550B total / 55B active reasoning model for long-context agentic work."
- **URL:** https://docs.openclaw.ai/providers/nvidia
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Ollama Cloud
- **What it does (docs):** "Use Ollama Cloud directly with OpenClaw" / "Ollama Cloud is Ollama's hosted model API. The `ollama-cloud` provider calls it directly at `https://ollama.com` over Ollama's native `/api/chat` API, with no local Ollama server and no local Ollama app signed into cloud mode."
- **URL:** https://docs.openclaw.ai/providers/ollama-cloud
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.

#### OpenAI
- **What it does (docs):** "Use OpenAI via API keys or Codex subscription in OpenClaw" / "OpenClaw uses one provider id, `openai`, for both direct API-key auth and ChatGPT/Codex subscription auth. `openai/*` is the standard model route."
- **URL:** https://docs.openclaw.ai/providers/openai
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "OpenAI and Codex provider path" surface, M3 Beta (area: Image and Multimodal Input, Model and Auth); "Agent Runtime" surface, M3 Beta (area: Hosted Provider Execution, Model and Runtime Selection); "Discord" surface, M4 Stable (area: Realtime Voice and Calls); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Credential and Secret Hygiene); plus 1 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** OpenAI setup (https://docs.openclaw.ai/providers/openai/setup); OpenAI authentication (https://docs.openclaw.ai/providers/openai/authentication); OpenAI models (https://docs.openclaw.ai/providers/openai/models); OpenAI runtimes and Codex auth (https://docs.openclaw.ai/providers/openai/runtimes); OpenAI coverage and cost (https://docs.openclaw.ai/providers/openai/coverage-and-cost); OpenAI image generation (https://docs.openclaw.ai/providers/openai/image-and-video); OpenAI voice and speech (https://docs.openclaw.ai/providers/openai/voice-and-speech); Azure OpenAI endpoints (https://docs.openclaw.ai/providers/openai/azure); OpenAI advanced configuration (https://docs.openclaw.ai/providers/openai/advanced)

#### OpenCode
- **What it does (docs):** "Use OpenCode Zen and Go catalogs with OpenClaw" / "OpenCode exposes two hosted catalogs in OpenClaw:"
- **URL:** https://docs.openclaw.ai/providers/opencode
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/opencode-provider` (Official external packages)
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "deprecated models are excluded from active discovery and its offline fallback."

#### OpenCode Go
- **What it does (docs):** "Use the OpenCode Go catalog with the shared OpenCode setup" / "OpenCode Go is a separate paid subscription inside OpenCode. It uses the same `OPENCODE_API_KEY` credential infrastructure as Zen, but a Zen key does not automatically include Go entitlement."
- **URL:** https://docs.openclaw.ai/providers/opencode-go
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Particle
- **What it does (docs):** "Use Particle-1 with an API key in OpenClaw" / "Particle serves Particle-1 through an OpenAI-compatible Chat Completions API."
- **URL:** https://docs.openclaw.ai/providers/particle
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/particle-provider` (Official external packages)

#### Perplexity
- **What it does (docs):** "Perplexity web search provider setup (API key, search modes, filtering)" / "The Perplexity plugin registers a `web_search` provider with two transports: the native Perplexity Search API (structured results with filters) and Perplexity Sonar chat completions, direct or via OpenRouter (AI-synthesized answers with citations)."
- **URL:** https://docs.openclaw.ai/providers/perplexity-provider
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.

#### Poolside (Laguna)
- **What it does (docs):** "Use Poolside Laguna models or the Poolside Agent with OpenClaw" / "Poolside provides Laguna models and the Poolside Agent CLI. Choose the integration for the work you want OpenClaw to do:"
- **URL:** https://docs.openclaw.ai/providers/poolside
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.

#### Qianfan
- **What it does (docs):** "Use Qianfan's unified API to access many models in OpenClaw" / "Qianfan is Baidu's MaaS platform: a unified, OpenAI-compatible API that routes requests to many models behind a single endpoint and API key. OpenClaw ships it as the official external plugin `@openclaw/qianfan-provider`."
- **URL:** https://docs.openclaw.ai/providers/qianfan
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/qianfan-provider` (Official external packages)
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "0-thinking-preview | text, image | 128,000   | 65,536     | Yes       | Deprecated alias; replaced by ernie-5."

#### Qwen
- **What it does (docs):** "Use Qwen Cloud through its OpenClaw plugin" / "Qwen Cloud is an official external OpenClaw provider plugin with primary id `qwen`. It targets Qwen Cloud / Alibaba DashScope Standard and Coding Plan endpoints, exposes Token Plan as `qwen-token-plan`, keeps `modelstudio` as a compatibility alias, and independently owns Alibaba's documented `bailian-token-plan` custom-provider id."
- **URL:** https://docs.openclaw.ai/providers/qwen
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/qwen-provider` (Official external packages)
- **Status wording (first sentence on the page with "have been removed"; may describe a sub-feature):** "The qwen-oauth Portal provider and its legacy OAuth flow have been removed."

#### Radius
- **What it does (docs):** "Connect OpenClaw to Radius with browser sign-in or an organization API key" / "Radius is Earendil's model gateway for Pi-compatible clients. The `radius` plugin connects OpenClaw's agent loop to Radius, including streamed responses, reasoning, images on supported models, and tool calls."
- **URL:** https://docs.openclaw.ai/providers/radius
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/radius-provider` (Official external packages)

#### StepFun
- **What it does (docs):** "Use StepFun models with OpenClaw" / "StepFun ships as an external official plugin (`@openclaw/stepfun-provider`) with two provider ids:"
- **URL:** https://docs.openclaw.ai/providers/stepfun
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/stepfun-provider` (Official external packages)

#### Synthetic
- **What it does (docs):** "Use Synthetic's Anthropic-compatible API in OpenClaw" / "Synthetic exposes Anthropic-compatible endpoints. OpenClaw provides it through the official `@openclaw/synthetic-provider` plugin and uses the Anthropic Messages API."
- **URL:** https://docs.openclaw.ai/providers/synthetic
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/synthetic-provider` (Official external packages)

#### Telnyx
- **What it does (docs):** "Telnyx setup for OpenAI-compatible AI inference" / "Telnyx AI inference provides hosted, OpenAI-compatible access to open-weight models plus proxied frontier routes. The vendor-maintained external `@telnyx/openclaw-provider` plugin supplies the runtime; OpenClaw carries its catalog and onboarding metadata."
- **URL:** https://docs.openclaw.ai/providers/telnyx
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.

#### Tencent Cloud (TokenHub / TokenPlan)
- **What it does (docs):** "Tencent Cloud TokenHub and TokenPlan setup for hy4-preview" / "Install the official Tencent Cloud provider plugin to access Tencent Hunyuan chat models (`hy4-preview`, `hy4`, `hy3`) through two endpoints — TokenHub (`tencent-tokenhub`) and TokenPlan (`tencent-tokenplan`) — using an OpenAI-compatible API."
- **URL:** https://docs.openclaw.ai/providers/tencent
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/tencent-provider` (Official external packages)

#### Together AI
- **What it does (docs):** "Together AI setup (auth + model selection)" / "Together AI provides access to leading open-source models including Llama, DeepSeek, Kimi, and more through a unified API. OpenClaw bundles it as the `together` provider."
- **URL:** https://docs.openclaw.ai/providers/together
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Venice AI
- **What it does (docs):** "Use Venice AI privacy-focused models in OpenClaw" / "Venice AI provides privacy-focused inference: open models run with no logging, plus anonymized proxy access to Claude, GPT, Gemini, and Grok. All endpoints are OpenAI-compatible (`/v1`)."
- **URL:** https://docs.openclaw.ai/providers/venice
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/venice-provider` (Official external packages)

#### Volcengine (Doubao)
- **What it does (docs):** "Volcano Engine setup (Doubao models, coding endpoints, and Seed Speech TTS)" / "The Volcengine provider gives access to Doubao models and third-party models hosted on Volcano Engine, with separate endpoints for general and coding workloads. The same official plugin also registers Volcengine Speech as a TTS provider."
- **URL:** https://docs.openclaw.ai/providers/volcengine
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/volcengine-provider` (Official external packages)

#### xAI
- **What it does (docs):** "Use xAI Grok models in OpenClaw" / "OpenClaw ships a bundled `xai` provider plugin for Grok models. The recommended path is Grok OAuth with an eligible SuperGrok or X Premium subscription."
- **URL:** https://docs.openclaw.ai/providers/xai
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "beta, experimental, and dated alias semantics."

#### Xiaomi MiMo
- **What it does (docs):** "Use Xiaomi MiMo pay-as-you-go and Token Plan models with OpenClaw" / "Xiaomi MiMo is the API platform for **MiMo** models. The official external `xiaomi` plugin registers two text providers plus a speech (TTS) provider:"
- **URL:** https://docs.openclaw.ai/providers/xiaomi
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/xiaomi-provider` (Official external packages)

#### Z.AI
- **What it does (docs):** "Use Z.AI (GLM models) with OpenClaw" / "Z.AI is the API platform for **GLM** models. It provides REST APIs for GLM and uses API keys for authentication."
- **URL:** https://docs.openclaw.ai/providers/zai
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/zai-provider` (Official external packages)
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "1       | Deprecated; hidden unless configured; use GLM-5."

**Nav subgroup: Decision models**

#### Liquid AI
- **What it does (docs):** "Connect Liquid AI d1 and d1 Ultra as native Decision models" / "Liquid AI's Decision models return Boolean probabilities, choices, and rubric scores from text, JSON, or images. OpenClaw connects directly to Liquid's native API."
- **URL:** https://docs.openclaw.ai/providers/liquid-ai
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/liquid-ai-provider` (Official external packages)

#### Rerank (Decision models)
- **What it does (docs):** "Use any /rerank endpoint (vLLM, TEI, Infinity, Cohere, Jina, Voyage) as a Decision model" / "The bundled `rerank` plugin turns any reranker behind a `/rerank` endpoint into a Decision model. It ships with OpenClaw and is enabled by default; it does nothing until you configure an endpoint."
- **URL:** https://docs.openclaw.ai/providers/rerank
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

**Nav subgroup: Speech and audio**

#### Azure Speech
- **What it does (docs):** "Azure AI Speech text-to-speech for OpenClaw replies" / "Azure Speech is a bundled Azure AI Speech text-to-speech provider. OpenClaw calls the Azure Speech REST API directly with SSML, synthesizing MP3 for standard replies, native Ogg/Opus for voice notes, and 8 kHz mulaw for telephony channels such as Voice Call."
- **URL:** https://docs.openclaw.ai/providers/azure-speech
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Deepgram
- **What it does (docs):** "Deepgram transcription for inbound voice notes" / "Deepgram is a speech-to-text API. OpenClaw uses it for inbound audio/voice-note transcription through `tools.media.audio` and for Voice Call streaming STT through `plugins.entries.voice-call.config.streaming`."
- **URL:** https://docs.openclaw.ai/providers/deepgram
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### ElevenLabs
- **What it does (docs):** "Use ElevenLabs speech, Scribe STT, and realtime transcription with OpenClaw" / "OpenClaw uses ElevenLabs for text-to-speech, batch speech-to-text with Scribe v2, and streaming STT with Scribe v2 Realtime. The plugin is bundled and enabled by default; no `plugins install` step is needed."
- **URL:** https://docs.openclaw.ai/providers/elevenlabs
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "Discord" surface, M4 Stable (area: Realtime Voice and Calls). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Fish Audio
- **What it does (docs):** "Use Fish Audio Drama 3 or S2.1 hosted TTS, or local S2 Pro on Apple silicon" / "OpenClaw supports Fish Audio in two distinct ways:"
- **URL:** https://docs.openclaw.ai/providers/fish-audio
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.

#### Gradium
- **What it does (docs):** "Use Gradium text-to-speech in OpenClaw" / "Gradium is a text-to-speech provider for OpenClaw. It renders standard audio replies (WAV), voice-note-compatible Opus output, and 8 kHz u-law audio for telephony surfaces."
- **URL:** https://docs.openclaw.ai/providers/gradium
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/gradium-speech` (Official external packages)

#### Inworld
- **What it does (docs):** "Inworld streaming text-to-speech for OpenClaw replies" / "Inworld is a streaming text-to-speech (TTS) provider. In OpenClaw it synthesizes outbound reply audio (MP3 by default, OGG_OPUS for voice notes) and raw PCM audio for telephony channels such as Voice Call."
- **URL:** https://docs.openclaw.ai/providers/inworld
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/inworld-speech` (Official external packages)

#### SenseAudio
- **What it does (docs):** "SenseAudio batch speech-to-text for inbound voice notes" / "SenseAudio transcribes inbound audio and voice-note attachments through OpenClaw's shared `tools.media.audio` pipeline. OpenClaw posts multipart audio to the OpenAI-compatible transcription endpoint and injects the returned text as `{{Transcript}}` plus an `[Audio]` block."
- **URL:** https://docs.openclaw.ai/providers/senseaudio
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

**Nav subgroup: Image, video, and music**

#### ComfyUI
- **What it does (docs):** "ComfyUI workflow generation and Comfy Cloud MCP OAuth setup in OpenClaw" / "Use Comfy Cloud's hosted MCP server for account OAuth and Comfy's own discovery and generation tools. Use the `comfy` plugin for workflow-driven runs through OpenClaw's shared media tools, with an API key for cloud workflows."
- **URL:** https://docs.openclaw.ai/providers/comfy
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/comfy-provider` (Official external packages)

#### Fal
- **What it does (docs):** "fal image, video, and music generation setup in OpenClaw" / "OpenClaw ships a bundled `fal` provider for hosted image, video, and music generation."
- **URL:** https://docs.openclaw.ai/providers/fal
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "Image, video, and music generation tools" surface, M2 Alpha (area: Video Generation). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Kie AI
- **What it does (docs):** "Kie AI video generation setup and supported models" / "OpenClaw includes the bundled `kie` plugin, enabled by default, for Kie AI video generation."
- **URL:** https://docs.openclaw.ai/providers/kie
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### PixVerse
- **What it does (docs):** "PixVerse video generation setup in OpenClaw" / "OpenClaw provides `pixverse` as an official external plugin for hosted PixVerse video generation. The plugin registers the `pixverse` provider against the `videoGenerationProviders` contract."
- **URL:** https://docs.openclaw.ai/providers/pixverse
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/pixverse-provider` (Official external packages)
- **Status (maturity scorecard, which links this page):** "Image, video, and music generation tools" surface, M2 Alpha (area: Video Generation). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Runway
- **What it does (docs):** "Runway video generation setup in OpenClaw" / "OpenClaw ships a bundled `runway` provider for hosted video generation, enabled by default, registered against the `videoGenerationProviders` contract."
- **URL:** https://docs.openclaw.ai/providers/runway
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "Image, video, and music generation tools" surface, M2 Alpha (area: Video Generation). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Vydra
- **What it does (docs):** "Use Vydra image, video, and speech in OpenClaw" / "The official Vydra plugin adds:"
- **URL:** https://docs.openclaw.ai/providers/vydra
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/vydra-provider` (Official external packages)

**Nav subgroup: Gateways and routers**

#### Bifrost
- **What it does (docs):** "Connect OpenClaw to a Bifrost OpenAI-compatible model gateway" / "Bifrost routes requests to upstream models through an OpenAI-compatible gateway. The bundled plugin connects to an existing gateway; it does not install Bifrost or manage its upstream credentials."
- **URL:** https://docs.openclaw.ai/providers/bifrost
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Claude Max API proxy
- **What it does (docs):** "Community proxy to expose Claude subscription credentials as an OpenAI-compatible endpoint" / "exposes a Claude Max/Pro subscription as an OpenAI-compatible API endpoint, so you can point any OpenAI-compatible tool at your subscription instead of an Anthropic API key."
- **URL:** https://docs.openclaw.ai/providers/claude-max-api-proxy
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.

#### ClawRouter
- **What it does (docs):** "Route credential-scoped models through ClawRouter and show managed quotas" / "ClawRouter gives OpenClaw one policy-scoped key for multiple upstream model providers. The bundled `clawrouter` plugin discovers only the models allowed for that key, routes each model through its declared protocol, and reports the key's budget and aggregate usage on OpenClaw usage surfaces."
- **URL:** https://docs.openclaw.ai/providers/clawrouter
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Cloudflare AI gateway
- **What it does (docs):** "Cloudflare AI Gateway setup (auth + model selection)" / "Cloudflare AI Gateway sits in front of provider APIs and adds analytics, caching, and controls. For Anthropic, OpenClaw uses the Anthropic Messages API through your Gateway endpoint."
- **URL:** https://docs.openclaw.ai/providers/cloudflare-ai-gateway
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/cloudflare-ai-gateway-provider` (Official external packages)

#### Kilo Gateway
- **What it does (docs):** "Use Kilo Gateway's unified API to access many models in OpenClaw" / "Kilo Gateway routes requests to many models behind a single OpenAI-compatible endpoint and API key."
- **URL:** https://docs.openclaw.ai/providers/kilocode
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/kilocode-provider` (Official external packages)

#### Liquid Inference
- **What it does (docs):** "Connect Liquid Inference as a custom OpenAI-compatible provider" / "Liquid Inference is an inference exchange with an OpenAI-compatible endpoint. Configure it with OpenClaw's existing custom-provider support and the `openai-completions` API."
- **URL:** https://docs.openclaw.ai/providers/liquid-inference
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.

#### LiteLLM
- **What it does (docs):** "Run OpenClaw through LiteLLM Proxy for unified model access and cost tracking" / "LiteLLM is an open-source LLM gateway with a unified API to 100+ model providers. Route OpenClaw through LiteLLM for centralized cost tracking, logging, virtual keys with spend limits, and backend failover without changing OpenClaw config."
- **URL:** https://docs.openclaw.ai/providers/litellm
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Neon AI Gateway
- **What it does (docs):** "Route OpenClaw through Neon AI Gateway with one branch-scoped Neon credential" / "Neon AI Gateway is an OpenAI-compatible inference gateway provided by Neon. One Neon credential reaches models from OpenAI, Anthropic, Google, Meta, Databricks and Alibaba, so OpenClaw talks to it over the same `openai-completions` transport used for other proxy providers."
- **URL:** https://docs.openclaw.ai/providers/neon
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "neither is deprecated, with the longer /ai-gateway/."

#### OpenRouter
- **What it does (docs):** "Use OpenRouter's unified API to access many models in OpenClaw" / "OpenRouter routes requests to many models behind one API and one key. Chat uses the OpenAI-compatible `openai-completions` transport."
- **URL:** https://docs.openclaw.ai/providers/openrouter
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "OpenRouter provider path" surface, M3 Beta (area: Chat Runtime and Normalization, Media Generation and Speech); "Image, video, and music generation tools" surface, M2 Alpha (area: Video Generation). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "experimental upstream."

#### Requesty
- **What it does (docs):** "Use Requesty's unified OpenAI-compatible router to access hundreds of models in OpenClaw" / "Requesty routes requests to hundreds of models behind a single OpenAI-compatible endpoint and API key, with per-request pricing and prompt caching."
- **URL:** https://docs.openclaw.ai/providers/requesty
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Vercel AI gateway
- **What it does (docs):** "Vercel AI Gateway setup (auth + model selection)" / "The Vercel AI Gateway provides a unified API to access hundreds of models through a single endpoint."
- **URL:** https://docs.openclaw.ai/providers/vercel-ai-gateway
- **Who runs it:** Model inference is hosted by the named provider; the provider plugin runs inside the user Gateway.
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/vercel-ai-gateway-provider` (Official external packages)

**Nav subgroup: Local runtimes**

#### ds4
- **What it does (docs):** "Run OpenClaw through ds4, a local DeepSeek V4 Flash OpenAI-compatible server" / "ds4 serves DeepSeek V4 Flash from a local Metal backend with an OpenAI-compatible `/v1` API. OpenClaw connects to ds4 through the generic `openai-completions` provider family."
- **URL:** https://docs.openclaw.ai/providers/ds4
- **Who runs it:** User hardware (local model runtime the user installs); reached from the Gateway.
- **Depends on (page's own requirements section):** macOS with Metal support.; A working ds4 checkout with `ds4-server` and the DeepSeek V4 Flash GGUF file.; Enough memory for the context you choose; larger `--ctx` values allocate more

#### llmman
- **What it does (docs):** "Run OpenClaw with llmman (local models, hosted providers, and hybrid local + hosted routing)" / "llmman pulls models as OCI artifacts from any registry or Hugging Face and serves them through unmodified upstream engines: `llama-server` for GGUF, `vllm` or `mlx-lm` for safetensors. One daemon exposes Ollama-, OpenAI-, and Anthropic-compatible APIs and can also forward requests to hosted providers."
- **URL:** https://docs.openclaw.ai/providers/llmman
- **Who runs it:** User hardware (local model runtime the user installs); reached from the Gateway.

#### LM Studio
- **What it does (docs):** "Run OpenClaw with LM Studio" / "LM Studio runs llama.cpp (GGUF) or MLX models locally, as a GUI app or the headless `llmster` daemon. For install and product docs, see lmstudio.ai."
- **URL:** https://docs.openclaw.ai/providers/lmstudio
- **Who runs it:** User hardware (local model runtime the user installs); reached from the Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "Local model providers: Ollama, vLLM, SGLang, LM Studio" surface, M2 Alpha (area: Native Provider Plugins, OpenAI-Compatible Runtime Compatibility). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Ollama
- **What it does (docs):** "Run OpenClaw with Ollama (cloud and local models)" / "OpenClaw talks to Ollama's native API (`/api/chat`), not the OpenAI-compatible `/v1` endpoint. Three setups are supported:"
- **URL:** https://docs.openclaw.ai/providers/ollama
- **Who runs it:** User hardware (local model runtime the user installs); reached from the Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "Local model providers: Ollama, vLLM, SGLang, LM Studio" surface, M2 Alpha (area: Native Provider Plugins, Provider Setup, Lifecycle, and Diagnostics); "Agent Runtime" surface, M3 Beta (area: Local and Self-hosted Providers, Tool Calls and Response Handling). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Ollama setup (https://docs.openclaw.ai/providers/ollama/setup); Ollama model discovery (https://docs.openclaw.ai/providers/ollama/model-discovery); Ollama node-local inference (https://docs.openclaw.ai/providers/ollama/node-local-inference); Ollama vision and image description (https://docs.openclaw.ai/providers/ollama/vision); Ollama configuration (https://docs.openclaw.ai/providers/ollama/configuration); Ollama config recipes (https://docs.openclaw.ai/providers/ollama/recipes); Ollama Web Search (https://docs.openclaw.ai/providers/ollama/web-search); Ollama advanced configuration (https://docs.openclaw.ai/providers/ollama/advanced); Ollama troubleshooting (https://docs.openclaw.ai/providers/ollama/troubleshooting)

#### oMLX
- **What it does (docs):** "Use oMLX for local chat and memory embeddings on Apple Silicon" / "oMLX serves MLX models on Apple Silicon. OpenClaw's bundled oMLX provider supports chat and memory embeddings through its OpenAI-compatible API at `http://127.0.0.1:8000/v1`."
- **URL:** https://docs.openclaw.ai/providers/omlx
- **Who runs it:** User hardware (local model runtime the user installs); reached from the Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### SGLang
- **What it does (docs):** "Run OpenClaw with SGLang (OpenAI-compatible self-hosted server)" / "SGLang serves open-weight models via an OpenAI-compatible HTTP API. OpenClaw connects to SGLang using the `openai-completions` provider family with auto-discovery of available models."
- **URL:** https://docs.openclaw.ai/providers/sglang
- **Who runs it:** User hardware (local model runtime the user installs); reached from the Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "Local model providers: Ollama, vLLM, SGLang, LM Studio" surface, M2 Alpha (area: OpenAI-Compatible Runtime Compatibility). Source: https://docs.openclaw.ai/maturity/taxonomy

#### vLLM
- **What it does (docs):** "Run OpenClaw with vLLM (OpenAI-compatible local server)" / "vLLM serves open-source (and some custom) models through an **OpenAI-compatible** HTTP API. OpenClaw connects using the `openai-completions` API and can **auto-discover** models when you opt in with `VLLM_API_KEY`."
- **URL:** https://docs.openclaw.ai/providers/vllm
- **Who runs it:** User hardware (local model runtime the user installs); reached from the Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "Local model providers: Ollama, vLLM, SGLang, LM Studio" surface, M2 Alpha (area: OpenAI-Compatible Runtime Compatibility, Provider Setup, Lifecycle, and Diagnostics). Source: https://docs.openclaw.ai/maturity/taxonomy

### Tab: Platforms

**Group: Platforms overview**

#### Platforms
- **What it does (docs):** "Platform support overview (Gateway + companion apps)" / "OpenClaw core is written in TypeScript. **Node is the primary, default, and recommended runtime**."
- **URL:** https://docs.openclaw.ai/platforms
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "Linux Gateway host" surface, M4 Stable (area: Host Setup and Updates); "Linux companion app" surface, M3 Beta (area: App Distribution). Source: https://docs.openclaw.ai/maturity/taxonomy

#### macOS app
- **What it does (docs):** "Install and use the OpenClaw macOS menu bar app" / "The macOS app is the OpenClaw **menu bar companion**: native tray UI, macOS permission prompts, notifications, WebChat, voice input, a hosted-widget panel, and Mac-hosted node tools such as `system.run`."
- **URL:** https://docs.openclaw.ai/platforms/macos
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Depends on (page's own requirements section):** OpenClaw.app requires macOS 26.2 (Tahoe) or later. This also applies to
- **Status (maturity scorecard, which links this page):** "macOS Gateway host" surface, M4 Stable (area: CLI Setup, Diagnostics and Observability); "macOS companion app" surface, M3 Beta (area: Canvas, Local Setup). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "removed in"; may describe a sub-feature):** "If a pending addition would restore a domain removed in another Dashboard window, it is discarded."

#### Linux app
- **What it does (docs):** "Linux support + companion app status" / "The Gateway is fully supported on Linux. Node is the primary, default, and recommended runtime; Bun 1.4.4+ builds with WAL-reset-safe `node:sqlite` can run OpenClaw as an explicit opt-in."
- **URL:** https://docs.openclaw.ai/platforms/linux
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Gateway Runtime, Performance and Diagnostics); "Linux Gateway host" surface, M4 Stable (area: Gateway Runtime and Service Control, Host Setup and Updates); "Linux companion app" surface, M3 Beta (area: App Distribution, Chat and Sessions). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "that artifact without building the experimental compiler."

#### Omarchy
- **What it does (docs):** "OpenClaw on Omarchy: bar plugin, desktop app handoff, and support" / "The OpenClaw Omarchy plugin puts agents, recent sessions, and a quick prompt in your desktop bar. Its monochrome mascot follows the shell theme, blinks, and animates with reported agent activity."
- **URL:** https://docs.openclaw.ai/platforms/omarchy
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Depends on (page's own requirements section):** Omarchy 4 with its Quickshell bar and plugin support. Earlier Waybar-based; Python 3 and PyGObject for the desktop session's D-Bus connection.; Either a connected OpenClaw Linux desktop app with Omarchy integration, or

#### Windows
- **What it does (docs):** "Windows Hub (recommended), Tauri desktop backup, native CLI and Gateway, WSL2, and troubleshooting" / "The native **Windows Hub** is the recommended Windows desktop app. It includes setup, tray status, chat, Command Center diagnostics, and Windows node capabilities, with an app-owned WSL Gateway for local setup."
- **URL:** https://docs.openclaw.ai/platforms/windows
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "Native Windows" surface, M2 Alpha (area: CLI, Gateway Management); "Windows App / Node" surface, M3 Beta (area: Chat Sessions, Desktop Tools and Permissions); "Windows via WSL2" surface, M3 Beta (area: CLI, Diagnostics and Repair). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Android app
- **What it does (docs):** "Android app (node): pairing, connection recovery, chat, voice, and device commands" / "The official Android app is available on Google Play and, for sideloading, as a signed standalone APK on selected GitHub Releases. Not every release includes the APK and checksum."
- **URL:** https://docs.openclaw.ai/platforms/android
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Depends on (page's own requirements section):** Install Tailscale on the Android device and the Mac, and connect both to the same tailnet.; On Android, enable Developer options and USB debugging. Android 16 places Wireless; Install scrcpy and ADB on the Mac:; Keep the Android device available for the first connection. Android must approve each Mac's ADB
- **Status (maturity scorecard, which links this page):** "Android app" surface, M4 Stable (area: Connection Setup, Device Runtime); "Session, memory, and state lifecycle" surface, M3 Beta (area: Cross-client History and Session Parity). Source: https://docs.openclaw.ai/maturity/taxonomy

#### ChromeOS
- **What it does (docs):** "Run the OpenClaw Gateway on ChromeOS inside a Crostini Linux container" / "ChromeOS runs Linux software through **Crostini**, a managed Debian container that Google exposes as the "Linux development environment". The Gateway runs inside that container exactly like any other Linux install, so the Linux guide applies in full."
- **URL:** https://docs.openclaw.ai/platforms/chromeos
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Setup and Compatibility). Source: https://docs.openclaw.ai/maturity/taxonomy

#### iOS app
- **What it does (docs):** "iOS node app: connect to the Gateway, pairing, device capabilities, and troubleshooting" / "Availability: The official iPhone app is available on the App Store. Local development builds can also run from source."
- **URL:** https://docs.openclaw.ai/platforms/ios
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Depends on (page's own requirements section):** Gateway running on another device (macOS, Linux, or Windows via WSL2).; Network path:; Same LAN via Bonjour, or; Tailnet via unicast DNS-SD (example domain: `openclaw.internal.`), or
- **Status (maturity scorecard, which links this page):** "iOS app" surface, M4 Stable (area: Chat and Sessions, Device Commands); "watchOS companion surfaces" surface, M1 Experimental (area: Delivery and Recovery, Distribution and Support). Source: https://docs.openclaw.ai/maturity/taxonomy

#### HealthKit summaries
- **What it does (docs):** "Enable and invoke privacy-gated HealthKit summaries from an iOS node" / "OpenClaw can request a read-only summary of the current calendar day from a connected iPhone or iPad node. The device computes the aggregate on-device and returns only steps, sleep duration, average resting heart rate, and workout count/duration."
- **URL:** https://docs.openclaw.ai/platforms/ios-healthkit
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Depends on (page's own requirements section):** An iPhone or iPad running the OpenClaw iOS app where HealthKit reports health data as; A connected and approved iOS node. See iOS app setup.; A current Gateway that can reach the iOS node.; Readable Health data for any metrics you expect to see. An Apple Watch can

#### EasyRunner
- **What it does (docs):** "Run the OpenClaw Gateway on EasyRunner with Podman and Caddy" / "EasyRunner hosts the OpenClaw Gateway as a small containerized app behind its Caddy proxy. This guide assumes an EasyRunner host that runs Podman-compatible Compose apps and terminates HTTPS through Caddy."
- **URL:** https://docs.openclaw.ai/platforms/easyrunner
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Depends on (page's own requirements section):** An EasyRunner server with a domain routed to it.; The official OpenClaw image (`ghcr.io/openclaw/openclaw`) or your own build.; A persistent config volume for `/home/node/.openclaw`.; A persistent workspace volume for `/home/node/.openclaw/workspace`.

**Group: macOS companion app**

**Nav subgroup: Setup**

#### macOS dev setup
- **What it does (docs):** "Setup guide for developers working on the OpenClaw macOS app" / "Build and run the OpenClaw macOS application from source."
- **URL:** https://docs.openclaw.ai/platforms/mac/dev-setup
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Depends on (page's own requirements section):** Xcode 26.4+ (Swift 6.3 toolchain), on the latest macOS available in; Patched Node.js 24.22.1+ or 26.12.1+ & pnpm is recommended for development and packaging. Gateway/CLI runtime compatibility starts at Node 24.16.0 on 24.x or 26
- **Status (maturity scorecard, which links this page):** "macOS companion app" surface, M3 Beta (area: Local Setup). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Menu bar
- **What it does (docs):** "Menu bar status logic and what is surfaced to users" / "default. Enable **Native experience (Experimental)** under **Dashboard → Settings → This Mac → App** to use native chat windows."
- **URL:** https://docs.openclaw.ai/platforms/mac/menu-bar
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "macOS companion app" surface, M3 Beta (area: Status and Settings). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Menu bar icon
- **What it does (docs):** "Menu bar icon states and animations for OpenClaw on macOS" / "Scope: macOS app (`apps/macos`). Rendering: `CritterIconRenderer.makeIcon(...)`."
- **URL:** https://docs.openclaw.ai/platforms/mac/icon
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "macOS companion app" surface, M3 Beta (area: Status and Settings). Source: https://docs.openclaw.ai/maturity/taxonomy

#### macOS permissions
- **What it does (docs):** "macOS permission persistence (TCC) and signing requirements" / "macOS permission grants are fragile. TCC associates a permission grant with the app's code signature, bundle identifier, and on-disk path."
- **URL:** https://docs.openclaw.ai/platforms/mac/permissions
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "macOS companion app" surface, M3 Beta (area: Native Capabilities). Source: https://docs.openclaw.ai/maturity/taxonomy

#### macOS signing
- **What it does (docs):** "Signing steps for macOS debug builds generated by packaging scripts" / "`scripts/package-mac-app.sh` builds a staged app, calls `scripts/codesign-mac-app.sh`, and verifies the signed runtime before replacing `dist/OpenClaw.app`. macOS ties TCC permissions to the bundle ID and code signature."
- **URL:** https://docs.openclaw.ai/platforms/mac/signing
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "macOS companion app" surface, M3 Beta (area: Native Capabilities). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Remote control
- **What it does (docs):** "macOS app flow for controlling a remote OpenClaw Gateway" / "This flow lets the macOS app act as a full remote control for an OpenClaw Gateway running on another host (desktop/server). The app connects directly to trusted LAN/Tailnet Gateway URLs, or manages an SSH tunnel when the remote Gateway is loopback-only."
- **URL:** https://docs.openclaw.ai/platforms/mac/remote
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "macOS Gateway host" surface, M4 Stable (area: Local Gateway Integration, Permissions and Native Capabilities); "macOS companion app" surface, M3 Beta (area: Remote Connections, Remote WebChat). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Device model database
- **What it does (docs):** "How OpenClaw vendors Apple device model identifiers for friendly names in the macOS app." / "The macOS companion app's **Instances** UI maps Apple model identifiers to friendly names (`iPad16,6` -> "iPad Pro 13-inch (M4)", `Mac16,6` -> "MacBook Pro (14-inch, 2024)"). `DeviceModelCatalog` also uses the identifier prefix (falling back to device family) to pick an SF Symbol per device."
- **URL:** https://docs.openclaw.ai/reference/device-models
- **Who runs it:** User machine (the Gateway host or a client of it).

**Nav subgroup: Runtime**

#### Gateway on macOS
- **What it does (docs):** "Run, update, and troubleshoot the Gateway included with the macOS app" / "OpenClaw.app includes everything needed to run a Gateway on your Mac. You do not need to install Node, Bun, or a global CLI."
- **URL:** https://docs.openclaw.ai/platforms/mac/bundled-gateway
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "macOS Gateway host" surface, M4 Stable (area: CLI Setup, Diagnostics and Observability); "macOS companion app" surface, M3 Beta (area: Local Setup). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Health checks (macOS)
- **What it does (docs):** "How the macOS app reports gateway/channel health states" / "The macOS app reads channel health from the Gateway. Configured channels do not need a linked-session field to report a healthy state."
- **URL:** https://docs.openclaw.ai/platforms/mac/health
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "macOS companion app" surface, M3 Beta (area: Status and Settings). Source: https://docs.openclaw.ai/maturity/taxonomy

#### macOS logging
- **What it does (docs):** "macOS app log redaction, opt-in diagnostics files, and native OSLog privacy flags" / "The macOS app logs through swift-log (unified logging by default) and can also write a rotating local file log for durable capture (`DiagnosticsFileLog`)."
- **URL:** https://docs.openclaw.ai/platforms/mac/logging
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "macOS companion app" surface, M3 Beta (area: Status and Settings). Source: https://docs.openclaw.ai/maturity/taxonomy

#### macOS IPC
- **What it does (docs):** "macOS IPC architecture for OpenClaw app, gateway node transport, and PeekabooBridge" / "A local Unix socket connects the node host service to the macOS app for exec approvals and `system.run`. The bundled `openclaw-mac` CLI uses a separate local control socket to inspect and configure primary and saved Gateway connections."
- **URL:** https://docs.openclaw.ai/platforms/mac/xpc
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "macOS companion app" surface, M3 Beta (area: Native Capabilities). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Features**

#### Voice wake (macOS)
- **What it does (docs):** "Voice wake and push-to-talk modes plus routing details in the mac app" / "Voice Wake and push-to-talk require macOS 26.2 or newer. Their device controls appear in **Dashboard → Settings → Talk → This Mac**, which reports when voice features are unavailable on this Mac."
- **URL:** https://docs.openclaw.ai/platforms/mac/voicewake
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "Voice and realtime talk" surface, M2 Alpha (area: Native App Talk, Voice Wake and Routing); "macOS companion app" surface, M3 Beta (area: Voice and Talk). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Voice overlay
- **What it does (docs):** "Voice overlay lifecycle when wake-word and push-to-talk overlap" / "Audience: macOS app contributors. Goal: keep the voice overlay predictable when wake-word and push-to-talk overlap."
- **URL:** https://docs.openclaw.ai/platforms/mac/voice-overlay
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "Voice and realtime talk" surface, M2 Alpha (area: Talk Observability, Voice Wake and Routing); "macOS companion app" surface, M3 Beta (area: Voice and Talk). Source: https://docs.openclaw.ai/maturity/taxonomy

#### WebChat (macOS)
- **What it does (docs):** "Choose the Web or experimental Native Mac experience and use Gateway chat windows" / "The macOS app uses the **Web** experience by default, embedding the Gateway's Control UI in an app window. To use the native window and sessions sidebar, open **Dashboard → Settings → This Mac → App** and enable **Native experience (Experimental)**."
- **URL:** https://docs.openclaw.ai/platforms/mac/webchat
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "macOS companion app" surface, M3 Beta (area: Remote WebChat, WebChat). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Widget panel
- **What it does (docs):** "Present hosted widgets in the macOS panel" / "The macOS app includes a native panel for presenting hosted widget documents. The Canvas plugin owns this presentation path."
- **URL:** https://docs.openclaw.ai/platforms/mac/canvas
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "macOS companion app" surface, M3 Beta (area: Canvas). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Skills (macOS)
- **What it does (docs):** "Manage Gateway skills from the macOS app's Dashboard" / "Open **Dashboard → Skills** to inspect and manage skills for the connected Gateway. The macOS app uses the same Control UI as a regular browser; there is no separate native Skills pane."
- **URL:** https://docs.openclaw.ai/platforms/mac/skills
- **Who runs it:** User device (companion app or node) paired to the user Gateway.

#### Peekaboo bridge
- **What it does (docs):** "PeekabooBridge integration for macOS UI automation" / "OpenClaw can host **PeekabooBridge** as a local, permission-aware UI automation broker (`PeekabooBridgeHostCoordinator`, backed by the `openclaw/Peekaboo` Swift package). This lets the `peekaboo` CLI drive UI automation while reusing the macOS app's TCC permissions."
- **URL:** https://docs.openclaw.ai/platforms/mac/peekaboo
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "macOS companion app" surface, M3 Beta (area: Native Capabilities). Source: https://docs.openclaw.ai/maturity/taxonomy

### Tab: Gateway & Ops

**Group: Gateway**

#### Gateway runbook
- **What it does (docs):** "Runbook for the Gateway service, lifecycle, and operations" / "Use this page for day-1 startup and day-2 operations of the Gateway service."
- **URL:** https://docs.openclaw.ai/gateway
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Gateway Runtime); "Gateway runtime" surface, M4 Stable (area: Gateway Lifecycle, Gateway RPC APIs and Events); "Kubernetes hosting" surface, M2 Alpha (area: Cluster Lifecycle); "Linux Gateway host" surface, M4 Stable (area: Diagnostics and Repair, Gateway Runtime and Service Control); plus 5 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Configuration**

#### Configuration
- **What it does (docs):** "Configuration overview: common tasks, quick setup, and links to the Configuration reference" / "OpenClaw reads an optional **JSON5** config from `~/.openclaw/openclaw.json`. If the file is missing, OpenClaw uses safe defaults."
- **URL:** https://docs.openclaw.ai/gateway/configuration
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Control UI" surface, M3 Beta (area: Configuration); "iOS app" surface, M4 Stable (area: Notifications and Background). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Common tasks (https://docs.openclaw.ai/gateway/configuration/common-tasks); Config hot reload (https://docs.openclaw.ai/gateway/configuration/hot-reload); Config RPC (programmatic updates) (https://docs.openclaw.ai/gateway/configuration/config-rpc); Environment variables (https://docs.openclaw.ai/gateway/configuration/environment-variables)

#### Configuration reference
- **What it does (docs):** "Gateway config reference for core OpenClaw keys, defaults, and links to dedicated subsystem references" / "Field-level reference for `~/.openclaw/openclaw.json`: keys, defaults, and links to deeper subsystem pages. For task-oriented setup guidance, see Configuration."
- **URL:** https://docs.openclaw.ai/gateway/configuration-reference
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Channel framework" surface, M3 Beta (area: Conversation Routing and Delivery, Status Health and Operator Controls); "Plugins" surface, M3 Beta (area: Canvas plugin); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Gateway Auth and Remote Access). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Configuration — agents
- **What it does (docs):** "Agent defaults, multi-agent routing, session, messages, and talk config" / "Agent-scoped configuration keys under `agents.*`, `multiAgent.*`, `session.*`, `messages.*`, and `talk.*`. For channels, tools, gateway runtime, and other top-level keys, see Configuration reference."
- **URL:** https://docs.openclaw.ai/gateway/config-agents
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Anthropic provider path" surface, M3 Beta (area: Media Inputs, Model and Runtime Selection); "Google Chat" surface, M2 Alpha (area: Native Controls and Approvals); "Image, video, and music generation tools" surface, M2 Alpha (area: Media Routing and Discovery); "Local model providers: Ollama, vLLM, SGLang, LM Studio" surface, M2 Alpha (area: Provider Setup, Lifecycle, and Diagnostics). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Configuration — agent workspace and bootstrap (https://docs.openclaw.ai/gateway/config-agents/workspace-and-bootstrap); Configuration — agent models (https://docs.openclaw.ai/gateway/config-agents/models); Configuration — agent runtime and CLI backends (https://docs.openclaw.ai/gateway/config-agents/runtime-and-cli-backends); Configuration — agent heartbeat, compaction, and streaming (https://docs.openclaw.ai/gateway/config-agents/heartbeat-compaction-and-streaming); Configuration — agent sandboxing (https://docs.openclaw.ai/gateway/config-agents/sandbox); Configuration — per-agent entries and multi-agent routing (https://docs.openclaw.ai/gateway/config-agents/entries-and-multi-agent); Configuration — agent sessions (https://docs.openclaw.ai/gateway/config-agents/sessions); Configuration — messages and talk (https://docs.openclaw.ai/gateway/config-agents/messages-and-talk)

#### Configuration — automations and media template variables
- **What it does (docs):** "Automation config under cron plus the media model template variable surface" / "Scheduled automation keys under `cron.*`, plus the media model template variable surface."
- **URL:** https://docs.openclaw.ai/gateway/config-automation
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Configuration — browser, UI, and desktop
- **What it does (docs):** "Browser automation, Control UI presentation, and desktop or paired-node config" / "Client-facing surfaces: `browser.*`, `ui.*`, and `desktop.*`."
- **URL:** https://docs.openclaw.ai/gateway/config-browser-ui-desktop
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Configuration — channels
- **What it does (docs):** "Channel configuration: access control, pairing, per-channel keys across Slack, Discord, Telegram, WhatsApp, Matrix, iMessage, and more" / "Per-channel configuration keys under `channels.*`: DM and group access, multi-account setups, mention gating, and per-channel keys for Slack, Discord, Telegram, WhatsApp, Matrix, iMessage, and other channel plugins."
- **URL:** https://docs.openclaw.ai/gateway/config-channels
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Channel framework" surface, M3 Beta (area: Outbound Delivery and Reply Pipeline); "Discord" surface, M4 Stable (area: Channel Setup and Operations, Realtime Voice and Calls); "Google Chat" surface, M2 Alpha (area: Access and Identity, Channel Setup and Operations); "Microsoft Teams" surface, M2 Alpha (area: Channel Setup and Operations); plus 3 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Configuration — shared channel policies (https://docs.openclaw.ai/gateway/config-channels/shared-policies); Configuration — personal messaging channels (https://docs.openclaw.ai/gateway/config-channels/personal-messaging); Configuration — workplace chat channels (https://docs.openclaw.ai/gateway/config-channels/workplace-chat); Configuration — community chat channels (https://docs.openclaw.ai/gateway/config-channels/community-chat); Configuration — group mention gating and history (https://docs.openclaw.ai/gateway/config-channels/mention-gating-and-history); Configuration — chat commands (https://docs.openclaw.ai/gateway/config-channels/commands)

#### Configuration — cloud worker environments
- **What it does (docs):** "Cloud worker profiles under cloudWorkers, including Crabbox and static SSH development" / "Cloud worker environment keys under `cloudWorkers.*`."
- **URL:** https://docs.openclaw.ai/gateway/config-cloud-workers
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Configuration — MCP, skills, and plugins
- **What it does (docs):** "Extension config: MCP servers, skills, plugin entries, and the canvas widget presenter" / "Extension surfaces: `mcp.*`, `skills.*`, `plugins.*`, and `canvas.*`."
- **URL:** https://docs.openclaw.ai/gateway/config-extensions
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Configuration — gateway
- **What it does (docs):** "Gateway config: bind, auth, roles, Control UI, terminal, remote, nodes, TLS, and reload" / "Gateway runtime keys under `gateway.*`."
- **URL:** https://docs.openclaw.ai/gateway/config-gateway
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "preserveFunnel: deprecated migration guard."

#### Configuration — hooks
- **What it does (docs):** "Hook config: HTTP contract, agent payload, session policy, mapping, retries, and Gmail" / "Inbound hook keys under `hooks.*`."
- **URL:** https://docs.openclaw.ai/gateway/config-hooks
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Configuration — audit, logging, diagnostics, and telemetry
- **What it does (docs):** "Observability config: audit, logging, diagnostics, and telemetry keys" / "Observability keys: `audit.*`, `logging.*`, `diagnostics.*`, and `telemetry.*`."
- **URL:** https://docs.openclaw.ai/gateway/config-observability
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Configuration — runtime basics
- **What it does (docs):** "Runtime config: worktree storage, capacity, and acceleration, model routing, discovery, updates, ACP, and the wizard" / "Top-level runtime keys: `worktreeRoot`, `worktreeAcceleration`, `worktreeMaxCount`, `repositoryBranchPrefix`, `models.*`, `discovery.*`, `update.*`, `acp.*`, and `wizard.*`."
- **URL:** https://docs.openclaw.ai/gateway/config-runtime
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Configuration — environment, secrets, and includes
- **What it does (docs):** "Environment variables, secret providers, auth storage, and $include config splitting" / "Process environment, secret resolution, auth storage, and config composition: `env`, `secrets.*`, `auth.*`, and `$include`."
- **URL:** https://docs.openclaw.ai/gateway/config-secrets-env
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Configuration — tools and custom providers
- **What it does (docs):** "Tools config (policy, experimental toggles, provider-backed tools) and custom provider/base-URL setup" / "`tools.*` config keys and custom provider / base-URL setup. For agents, channels, and other top-level config keys, see Configuration reference."
- **URL:** https://docs.openclaw.ai/gateway/config-tools
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Sandbox and Tool Policy); "Local model providers: Ollama, vLLM, SGLang, LM Studio" surface, M2 Alpha (area: Network Safety and Prompt Controls); "Web search tools" surface, M3 Beta (area: Tool Availability and Fetch). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Configuration — tool policy (https://docs.openclaw.ai/gateway/config-tools/tool-policy); Configuration — GitHub identity for agent tools (https://docs.openclaw.ai/gateway/config-tools/github-identity); Configuration — built-in tool settings (https://docs.openclaw.ai/gateway/config-tools/built-in-tools); Configuration — cross-agent, session, and subagent tools (https://docs.openclaw.ai/gateway/config-tools/sessions-and-subagents); Configuration — custom providers and base URLs (https://docs.openclaw.ai/gateway/config-tools/custom-providers); Configuration — provider examples (https://docs.openclaw.ai/gateway/config-tools/provider-examples)

#### Configuration examples
- **What it does (docs):** "Schema-accurate configuration examples for common OpenClaw setups" / "Examples below are aligned with the current config schema. For the exhaustive reference and per-field notes, see Configuration."
- **URL:** https://docs.openclaw.ai/gateway/configuration-examples
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Anthropic provider path" surface, M3 Beta (area: Provider Auth and Recovery). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Authentication and secrets**

#### Authentication
- **What it does (docs):** "Model authentication: OAuth, API keys, Claude CLI reuse, and Anthropic setup-token" / "This page covers **model provider** authentication (API keys, OAuth, Claude CLI reuse, Anthropic setup-token). For **gateway connection** authentication (token, password, trusted-proxy), see Configuration and Trusted Proxy Auth."
- **URL:** https://docs.openclaw.ai/gateway/authentication
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Remote Access and Auth); "Kubernetes hosting" surface, M2 Alpha (area: Access and Exposure); "Linux Gateway host" surface, M4 Stable (area: Remote Access and Security); "OpenAI and Codex provider path" surface, M3 Beta (area: Model and Auth); plus 3 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy

#### Auth credential semantics
- **What it does (docs):** "Credential eligibility and resolution rules for auth profiles" / "These semantics keep selection-time and runtime auth behavior aligned. They are shared by:"
- **URL:** https://docs.openclaw.ai/auth-credential-semantics
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Secrets management
- **What it does (docs):** "Secrets management: SecretRef contract, shared secret store, runtime snapshots, and safe one-way scrubbing" / "OpenClaw supports additive SecretRefs so supported credentials do not need to live as plaintext in configuration."
- **URL:** https://docs.openclaw.ai/gateway/secrets
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: Doctor); "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Remote Access and Auth); "Google Chat" surface, M2 Alpha (area: Channel Setup and Operations); "Kubernetes hosting" surface, M2 Alpha (area: Configuration and Secrets); plus 5 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Secrets runtime model (https://docs.openclaw.ai/gateway/secrets/runtime-model); SecretRef contract and provider config (https://docs.openclaw.ai/gateway/secrets/secretref-contract); Shared secret store and egress proxy (https://docs.openclaw.ai/gateway/secrets/secret-store-and-egress); Secrets integration examples (https://docs.openclaw.ai/gateway/secrets/integration-examples); Secrets operations and behavior (https://docs.openclaw.ai/gateway/secrets/operations)

#### 1Password
- **What it does (docs):** "Use the 1Password plugin, bundled skill, or official MCP with OpenClaw" / "OpenClaw pairs with **1Password** in four independent ways:"
- **URL:** https://docs.openclaw.ai/gateway/1password
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** The 1Password CLI; A 1Password service account for the unattended plugin paths.; For direct skill workflows, either a service account, desktop app integration,

#### Secrets apply plan contract
- **What it does (docs):** "Contract for `secrets apply` plans: target validation, path matching, and SQLite auth-profile target scope" / "This page defines the strict contract enforced by `openclaw secrets apply`. If a target does not match these rules, apply fails before mutating any file."
- **URL:** https://docs.openclaw.ai/gateway/secrets-plan-contract
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Trusted proxy auth
- **What it does (docs):** "Delegate gateway authentication to a trusted reverse proxy (Pomerium, Caddy, nginx + OAuth)" / "Your reverse proxy authenticates users (OAuth, OIDC, SAML, etc.)."
- **URL:** https://docs.openclaw.ai/gateway/trusted-proxy-auth
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Security, auth, pairing, and secrets" surface, M3 Beta (area: Gateway Auth and Remote Access). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Health and diagnostics**

#### Health checks
- **What it does (docs):** "Health check commands and gateway health monitoring" / "Short guide to verify Gateway and channel health without guessing. It covers the CLI health checks, the HTTP check endpoints, the dedicated `health` command, and uptime monitoring."
- **URL:** https://docs.openclaw.ai/gateway/health
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Channel framework" surface, M3 Beta (area: Status Health and Operator Controls); "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Performance and Diagnostics); "Control UI" surface, M3 Beta (area: Operator Console); "Discord" surface, M4 Stable (area: Channel Setup and Operations); plus 3 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy

#### PostgreSQL operator guide
- **What it does (docs):** "Set up and operate a PostgreSQL-backed Gateway, with support boundaries, ports, backups, and recovery" / "Use this guide to provision PostgreSQL for one Gateway, move existing data, and operate the resulting installation. PostgreSQL is a **supported alternative** for the five configurable store families on qualified PostgreSQL 16–18 runtimes."
- **URL:** https://docs.openclaw.ai/gateway/postgresql
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Doctor
- **What it does (docs):** "Doctor command: health checks, config migrations, and repair steps" / "`openclaw doctor` is the repair and migration tool for OpenClaw. It fixes stale config/state, checks health, and provides actionable repair steps."
- **URL:** https://docs.openclaw.ai/gateway/doctor
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Anthropic provider path" surface, M3 Beta (area: Provider Auth and Recovery); "CLI" surface, M4 Stable (area: Doctor); "Gateway runtime" surface, M4 Stable (area: Health, Diagnostics, and Repair); "Linux companion app" surface, M3 Beta (area: Status and Diagnostics); plus 6 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Run doctor (https://docs.openclaw.ai/gateway/doctor/running); What doctor checks (https://docs.openclaw.ai/gateway/doctor/checks); Config and migration repairs (https://docs.openclaw.ai/gateway/doctor/config-migrations); Provider and route repairs (https://docs.openclaw.ai/gateway/doctor/provider-repairs); State, session, and plugin repairs (https://docs.openclaw.ai/gateway/doctor/state-and-sessions); Gateway, service, and security checks (https://docs.openclaw.ai/gateway/doctor/gateway-and-services); Workspace tips and Dreams UI actions (https://docs.openclaw.ai/gateway/doctor/workspace-and-dreams)

#### Audit history
- **What it does (docs):** "Metadata-only activity history plus durable run identity and decision receipts" / "The Gateway keeps a bounded, metadata-only audit ledger in the shared OpenClaw state database. It answers operational questions such as "which agent ran, when, and how did it end", "which tool actions did a run execute", and, when message auditing is enabled, "did an accepted inbound message reach dispatch" and "did an outbound message reach a terminal ..."
- **URL:** https://docs.openclaw.ai/gateway/audit
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Gateway runtime" surface, M4 Stable (area: Roles and Permissions). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Usage telemetry and update checks
- **What it does (docs):** "Daily update requests, update-outcome reports, approximate location, optional anonymous feature statistics, and privacy controls" / "newer version exists and includes the OpenClaw version, operating system, Node.js version, CPU architecture, and request surface. An identifier-free count-only request can follow a successful daily update check by default when its receiver explicitly supports counting."
- **URL:** https://docs.openclaw.ai/gateway/telemetry
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Logging
- **What it does (docs):** "File logs, console output, CLI tailing, and the Control UI Logs tab" / "OpenClaw has two main log surfaces:"
- **URL:** https://docs.openclaw.ai/logging
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Observability" surface, M3 Beta (area: Logging, Telemetry Export). Source: https://docs.openclaw.ai/maturity/taxonomy

#### OpenTelemetry export
- **What it does (docs):** "Index of the OpenClaw OpenTelemetry export documentation, one page per reader job" / "OpenClaw exports diagnostics through the official `diagnostics-otel` plugin using **OTLP/HTTP (protobuf)**. Logs can also be written as stdout JSONL for container and sandbox log pipelines."
- **URL:** https://docs.openclaw.ai/gateway/opentelemetry
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Observability" surface, M3 Beta (area: Session Diagnostics, Telemetry Export). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Set up OpenTelemetry export (https://docs.openclaw.ai/gateway/opentelemetry/setup); OpenTelemetry configuration (https://docs.openclaw.ai/gateway/opentelemetry/configuration); Privacy and trace context (https://docs.openclaw.ai/gateway/opentelemetry/privacy-and-trace-context); Model calls and exported metrics (https://docs.openclaw.ai/gateway/opentelemetry/model-calls-and-metrics); Exported spans and diagnostic events (https://docs.openclaw.ai/gateway/opentelemetry/spans-and-events)

#### Prometheus metrics
- **What it does (docs):** "Expose OpenClaw diagnostics as Prometheus text metrics through the diagnostics-prometheus plugin" / "OpenClaw can expose diagnostics metrics through the official `diagnostics-prometheus` plugin. It listens to trusted diagnostics plus internally tagged, dispatcher-owned diagnostic events (queue, memory, and session-recovery signals), and renders a Prometheus text endpoint at:"
- **URL:** https://docs.openclaw.ai/gateway/prometheus
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Observability" surface, M3 Beta (area: Session Diagnostics, Telemetry Export). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Gateway logging
- **What it does (docs):** "Logging surfaces, file logs, WS log styles, and console formatting" / "For a user-facing overview (CLI + Control UI + config), see /logging."
- **URL:** https://docs.openclaw.ai/gateway/logging
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Observability" surface, M3 Beta (area: Logging). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "calls to deprecated storage APIs still warn with their replacements."

#### Diagnostics export
- **What it does (docs):** "Create shareable Gateway diagnostics bundles for bug reports" / "OpenClaw can build a local diagnostics `.zip` for bug reports: sanitized Gateway status, health, logs, config shape, and recent payload-free stability events."
- **URL:** https://docs.openclaw.ai/gateway/diagnostics
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: CLI Observability); "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Performance and Diagnostics); "Gateway runtime" surface, M4 Stable (area: Health, Diagnostics, and Repair); "Linux Gateway host" surface, M4 Stable (area: Diagnostics and Repair); plus 2 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy

#### Troubleshooting
- **What it does (docs):** "Index of the deep gateway troubleshooting runbook, grouped by symptom area" / "This is the deep runbook. Start at /help/troubleshooting for the fast triage flow first."
- **URL:** https://docs.openclaw.ai/gateway/troubleshooting
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Anthropic provider path" surface, M3 Beta (area: Prompt Cache and Context, Provider Auth and Recovery); "CLI" surface, M4 Stable (area: Doctor, Gateway Service Management); "Local model providers: Ollama, vLLM, SGLang, LM Studio" surface, M2 Alpha (area: Provider Setup, Lifecycle, and Diagnostics); "macOS Gateway host" surface, M4 Stable (area: Diagnostics and Observability, Gateway Service Lifecycle). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Updates and rollbacks (https://docs.openclaw.ai/gateway/troubleshooting/updates-and-rollbacks); Skills and model providers (https://docs.openclaw.ai/gateway/troubleshooting/skills-and-model-providers); Agent replies and Control UI (https://docs.openclaw.ai/gateway/troubleshooting/agent-replies-and-control-ui); Gateway service and process (https://docs.openclaw.ai/gateway/troubleshooting/gateway-service-and-process); Config validation and checks (https://docs.openclaw.ai/gateway/troubleshooting/config-validation-and-probes); Channel delivery and tools (https://docs.openclaw.ai/gateway/troubleshooting/channel-delivery-and-tools)

**Nav subgroup: Scaling and operations**

#### PostgreSQL operator guide
- **What it does (docs):** "Set up and operate a PostgreSQL-backed Gateway, with support boundaries, ports, backups, and recovery" / "Use this guide to provision PostgreSQL for one Gateway, move existing data, and operate the resulting installation. PostgreSQL is a **supported alternative** for the five configurable store families on qualified PostgreSQL 16–18 runtimes."
- **URL:** https://docs.openclaw.ai/gateway/postgresql
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Gateway lock
- **What it does (docs):** "Gateway singleton guard: file lock plus WebSocket/HTTP bind" / "Startup establishes state ownership before publishing compatibility metadata and binding its listener:"
- **URL:** https://docs.openclaw.ai/gateway/gateway-lock
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Background exec and process tool
- **What it does (docs):** "Background exec execution and process management" / "OpenClaw runs shell commands through the `exec` tool. Ordinary long-running tasks stay in memory; opt-in durable processes on a Linux Gateway retain ownership across Gateway restarts."
- **URL:** https://docs.openclaw.ai/gateway/background-process
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Polling Controls); "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Tool Invocation and Execution). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Restart recovery
- **What it does (docs):** "Gateway restart recovery for interrupted root executions and recorded yield waits" / "A graceful Gateway stop or restart records which sessions are working or waiting, then aborts executing work promptly. This includes accepted turns still preparing their runtime when shutdown begins."
- **URL:** https://docs.openclaw.ai/gateway/restart-recovery
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Cloud Sessions
- **What it does (docs):** "Run sessions on paired devices or throwaway cloud machines while the Gateway keeps the transcript, workspace, and credentials" / "A cloud session is an ordinary session whose coding work runs on another machine. It appears in the sidebar, streams into chat, and keeps its transcript exactly like a local session — the Gateway stays the owner of the conversation, the reconciled workspace, model credentials, and placement records, while commands, file edits, and tool work execute remotely."
- **URL:** https://docs.openclaw.ai/gateway/cloud-sessions
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Page status field:** `active`
- **Status (maturity scorecard, which links this page):** "Containers and cloud execution" surface, M3 Beta (area: Container Operations). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Cloud Workers
- **What it does (docs):** "Dispatch session work to throwaway cloud machines with OpenClaw worker turns or Codex remote execution" / "Cloud workers run a session's coding work on a disposable machine while its transcript and accepted workspace changes stay with the Gateway. With Crabbox configured on the Gateway host, OpenClaw can select a machine, prepare the repository, and save a snapshot without a custom setup script."
- **URL:** https://docs.openclaw.ai/gateway/cloud-workers
- **Who runs it:** Throwaway cloud machine leased through Crabbox, under the user Gateway control.
- **Page status field:** `active`
- **Depends on (page's own requirements section):** A worker provider plugin. The bundled `crabbox` plugin drives the Crabbox CLI; Crabbox owns the supported cloud backends and their configuration. The plugin aut; For Crabbox AWS workers, the effective `aws.instanceProfile` must be empty. The provider checks `crabbox config show --json` before allocation, then requires `c; On Linux x64/arm64, OpenClaw installs a verified official Node.js toolchain automatically when needed; the image must provide compatible glibc, `curl`, `tar`, a; GitHub CLI (`gh`) on the worker's `PATH` for GitHub commands and HTTPS pushes. The sealed worker bundle includes the credential-binding launcher, not GitHub CLI
- **Status (maturity scorecard, which links this page):** "Containers and cloud execution" surface, M3 Beta (area: Container Setup). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Cloud worker warm images (https://docs.openclaw.ai/gateway/cloud-workers/warm-images); Cloud environment file (https://docs.openclaw.ai/gateway/cloud-workers/environment-file); Per-project default profiles (https://docs.openclaw.ai/gateway/cloud-workers/per-project-default-profiles); Worker setup and bundle installation (https://docs.openclaw.ai/gateway/cloud-workers/setup-and-bundle-installation); Verify a cloud worker profile (https://docs.openclaw.ai/gateway/cloud-workers/verify-the-profile); Dispatching a cloud session (https://docs.openclaw.ai/gateway/cloud-workers/dispatching-a-session); Placement and machine selection (https://docs.openclaw.ai/gateway/cloud-workers/placement-and-machine-selection); Cloud session lifecycle and durability (https://docs.openclaw.ai/gateway/cloud-workers/session-lifecycle); Cloud device desktop (https://docs.openclaw.ai/gateway/cloud-workers/desktop); Cloud worker security model (https://docs.openclaw.ai/gateway/cloud-workers/security-model); Worker-local inference (https://docs.openclaw.ai/gateway/cloud-workers/native-inference); Cloud worker troubleshooting (https://docs.openclaw.ai/gateway/cloud-workers/troubleshooting)

#### Multiple gateways
- **What it does (docs):** "Run multiple OpenClaw Gateways on one host (isolation, ports, and profiles)" / "Most setups need one Gateway - a single Gateway handles multiple messaging connections and agents. Run separate Gateways with isolated profiles/ports only when you need stronger isolation or redundancy (e.g., a rescue bot)."
- **URL:** https://docs.openclaw.ai/gateway/multiple-gateways
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "macOS Gateway host" surface, M4 Stable (area: Profiles and Isolation). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Security and sandboxing**

#### Security
- **What it does (docs):** "Trust model, safe defaults, and hardening guidance for running OpenClaw" / "OpenClaw ships with conservative defaults. On a regular host install the Gateway binds to loopback; most chat channels answer an unknown DM sender with a pairing code instead of processing the message; and group access is allowlisted, usually behind a mention gate."
- **URL:** https://docs.openclaw.ai/gateway/security
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Security, auth, pairing, and secrets" surface, M3 Beta (area: Gateway Auth and Remote Access); "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Browser Automation); "External apps and interoperability" surface, M2 Alpha (area: Gateway Access); "Gateway runtime" surface, M4 Stable (area: Approvals and Remote Execution, Device Auth and Pairing); plus 2 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy

#### Security trust model
- **What it does (docs):** "The trust boundary OpenClaw supports, the controls it does and does not provide, and how to report a vulnerability" / "Before changing remote access, DM policy, reverse proxy, or public exposure, run through the Gateway exposure runbook as a pre-flight/rollback checklist."
- **URL:** https://docs.openclaw.ai/gateway/security/trust-model
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Gateway runtime" surface, M4 Stable (area: Roles and Permissions). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Running the security audit
- **What it does (docs):** "What `openclaw security audit` inspects and the order to fix its findings in" / "Run this after any config change or before exposing network surfaces:"
- **URL:** https://docs.openclaw.ai/gateway/security/running-the-audit
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Security audit checks
- **What it does (docs):** "Reference catalog of checkIds emitted by openclaw security audit" / "`openclaw security audit` emits structured findings keyed by `checkId`. This page is the reference catalog for those IDs."
- **URL:** https://docs.openclaw.ai/gateway/security/audit-checks
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Browser Automation); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Approval Policy and Tool Safeguards, Channel Access Control). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Hardened baselines
- **What it does (docs):** "Copy/paste Gateway configurations that keep the deployment private, paired, and tool-restricted" / "Keeps the Gateway local-only, isolates DMs, limits session tools to the agent's own sessions, turns off ordinary cross-agent access, and disables control-plane/runtime tools by default. Re-enable tools selectively per trusted agent from there."
- **URL:** https://docs.openclaw.ai/gateway/security/hardened-baseline
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Access control and allowlists
- **What it does (docs):** "Who can reach the agent: DM policy, allowlists, DM session isolation, context visibility, and command authorization" / "Every DM-capable channel supports `dmPolicy` (or `*.dm.policy`), which gates inbound DMs before the message is processed:"
- **URL:** https://docs.openclaw.ai/gateway/security/access-control
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Prompt injection
- **What it does (docs):** "How untrusted content reaches the model, what OpenClaw does about it, and which layers you still have to enforce" / "An attacker crafts a message that manipulates the model into unsafe action ("ignore your instructions", "dump your filesystem", "follow this link and run commands")."
- **URL:** https://docs.openclaw.ai/gateway/security/prompt-injection
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Tool and agent permissions
- **What it does (docs):** "Cross-provider messaging, control-plane tools, node execution, plugins, sandboxing, and per-agent access profiles" / "Two built-in tools remain control-plane sensitive:"
- **URL:** https://docs.openclaw.ai/gateway/security/tool-permissions
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "Neither --force nor the deprecated plugin install/update flag --dangerously-force-unsafe-install approves policy warnings."

#### Browser control risks
- **What it does (docs):** "What giving the model a real browser exposes, and the SSRF policy that bounds it" / "Enabling browser control gives the model a real browser. If that profile already has logged-in sessions, the model can access those accounts and data - treat browser profiles as sensitive state."
- **URL:** https://docs.openclaw.ai/gateway/security/browser-control
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Network exposure
- **What it does (docs):** "Bind, firewall, discovery, Gateway auth, Tailscale, reverse proxy, and Control UI exposure settings" / "The Gateway multiplexes WebSocket + HTTP on one port (default `18789`; config/flags/env: `gateway.port`, `--port`, `OPENCLAW_GATEWAY_PORT`). That HTTP surface includes the Control UI (SPA assets, default base path `/`), and hosted widget documents (`/__openclaw__/canvas`)."
- **URL:** https://docs.openclaw.ai/gateway/security/network-exposure
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Secrets, storage, and logs
- **What it does (docs):** "What OpenClaw writes to disk, which files hold credentials, and how logs and transcripts are handled" / "Assume anything under `~/.openclaw/` (or `$OPENCLAW_STATE_DIR/`) may contain secrets or private data:"
- **URL:** https://docs.openclaw.ai/gateway/security/secrets-and-storage
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Gateway exposure runbook
- **What it does (docs):** "Pre-flight and rollback checklist before exposing an OpenClaw Gateway beyond loopback" / "Expose the Gateway only after you can explain who can reach it, how they are authenticated, which agents they can trigger, and which tools those agents can use. When in doubt, return to loopback-only access and re-run the audit."
- **URL:** https://docs.openclaw.ai/gateway/security/exposure-runbook
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Kubernetes hosting" surface, M2 Alpha (area: Access and Exposure); "Linux Gateway host" surface, M4 Stable (area: Remote Access and Security); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Gateway Auth and Remote Access); "Windows via WSL2" surface, M3 Beta (area: Gateway Access and Exposure). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Rate limiting
- **What it does (docs):** "Reference for every Gateway rate limit: pre-auth socket budgets and lockouts, browser and webhook throttles, the control-plane write backstop, ACP session caps, and restart cooldown" / "The Gateway enforces several independent rate limits. They protect different boundaries, key on different identities, and fail with different error shapes."
- **URL:** https://docs.openclaw.ai/gateway/security/rate-limiting
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Operator incident response
- **What it does (docs):** "Contain, rotate, audit, and collect evidence after a suspected compromise of your own Gateway" / "2. Close exposure: set `gateway.bind: "loopback"` (or disable Tailscale Funnel/Serve) until you understand what happened."
- **URL:** https://docs.openclaw.ai/gateway/security/operator-incident-response
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Secure file operations
- **What it does (docs):** "How OpenClaw handles local file access safely, including native Windows credential checks" / "OpenClaw uses `@openclaw/fs-safe` for security-sensitive local file operations: root-bounded reads/writes, atomic replacement, archive extraction, temp workspaces, JSON state, and secret-file handling."
- **URL:** https://docs.openclaw.ai/gateway/security/secure-file-operations
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Control UI" surface, M3 Beta (area: WebChat Conversations); "Media understanding and media generation" surface, M2 Alpha (area: Media Intake and Access). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "OpenClaw keeps FS_SAFE_PYTHON_MODE and OPENCLAW_FS_SAFE_PYTHON_MODE as deprecated mode aliases when loading its runtime environment, with a deprecation warning."

#### Operator scopes
- **What it does (docs):** "Operator roles, scopes, and approval-time checks for Gateway clients" / "Operator scopes gate what a Gateway client can do after it authenticates. They are a control-plane guardrail inside one trusted Gateway operator domain, not hostile multi-tenant isolation."
- **URL:** https://docs.openclaw.ai/gateway/operator-scopes
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Tool Invocation and Execution); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Device and Node Pairing). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Sandboxing
- **What it does (docs):** "How OpenClaw sandboxing works: modes, scopes, workspace access, and images" / "OpenClaw can run tool execution inside a sandbox backend to limit the damage tools can cause. Sandboxing is off by default and controlled by `agents.defaults.sandbox` (global), `agents.entries.*.sandbox` (per-agent), or a required creator-role sandbox policy."
- **URL:** https://docs.openclaw.ai/gateway/sandboxing
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Page status field:** `active`
- **Status (maturity scorecard, which links this page):** "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Sandbox and Tool Policy). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** What gets sandboxed (https://docs.openclaw.ai/gateway/sandboxing/what-gets-sandboxed); Modes, scope, and backend (https://docs.openclaw.ai/gateway/sandboxing/modes-scope-and-backend); Supported capability matrix (https://docs.openclaw.ai/gateway/sandboxing/supported-capability-matrix); Docker backend (https://docs.openclaw.ai/gateway/sandboxing/docker-backend); Podman backend (https://docs.openclaw.ai/gateway/sandboxing/podman-backend); SSH backend (https://docs.openclaw.ai/gateway/sandboxing/ssh-backend); OpenShell backend (https://docs.openclaw.ai/gateway/sandboxing/openshell-backend); Crabbox backend (https://docs.openclaw.ai/gateway/sandboxing/crabbox-backend); Workspace access (https://docs.openclaw.ai/gateway/sandboxing/workspace-access); Multiple folders for one agent (https://docs.openclaw.ai/gateway/sandboxing/multiple-folders-for-one-agent); Images and setup (https://docs.openclaw.ai/gateway/sandboxing/images-and-setup); setupCommand (one-time container setup) (https://docs.openclaw.ai/gateway/sandboxing/setup-command)

#### OpenShell
- **What it does (docs):** "Use OpenShell as a managed sandbox backend for OpenClaw agents" / "OpenShell is a managed sandbox backend: OpenClaw delegates sandbox lifecycle to the `openshell` CLI and executes commands over SSH. The selected OpenShell gateway can manage sandboxes locally with Docker, Podman, or virtualization, or run them on separate infrastructure."
- **URL:** https://docs.openclaw.ai/gateway/openshell
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/openshell-sandbox` (Official external packages)
- **Depends on (page's own requirements section):** `openshell` CLI installed and on the OpenClaw Gateway process's `PATH` (or a; OpenSSH client available on the Gateway host; OpenShell `v0.0.88` or newer when configuring an OpenShell workspace; An active, reachable OpenShell gateway with permission to create sandboxes.

#### Sandbox vs tool policy vs elevated
- **What it does (docs):** "Why a tool is blocked: sandbox runtime, tool allow/deny policy, and elevated exec gates" / "OpenClaw has three related but different controls:"
- **URL:** https://docs.openclaw.ai/gateway/sandbox-vs-tool-policy-vs-elevated
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Page status field:** `active`
- **Status (maturity scorecard, which links this page):** "Agent Runtime" surface, M3 Beta (area: Tool Execution Controls); "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Sandbox and Tool Policy). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Session permission modes
- **What it does (docs):** "Session permission modes, workspace boundaries, and escalation reviewers" / "Session permission modes set one session's filesystem boundary and exec escalation reviewer. The boundary is the session's recorded resolved `sessionRoot`, or the selected agent's resolved workspace when no root is recorded."
- **URL:** https://docs.openclaw.ai/gateway/permission-modes
- **Who runs it:** User machine (the Gateway host or a client of it).

**Nav subgroup: Protocols and APIs**

#### Building a Gateway client
- **What it does (docs):** "Build a third-party operator or WebChat client for the Gateway WebSocket protocol" / "Use the published Gateway packages to build operator dashboards, WebChat clients, and other third-party applications. This guide covers the client lifecycle around the wire contract: authentication, capabilities, reconnect recovery, history, subscriptions, and version upgrades."
- **URL:** https://docs.openclaw.ai/gateway/clients
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Gateway integrations for external apps
- **What it does (docs):** "Current integration path for external apps, scripts, dashboards, CI jobs, and IDE extensions" / "External apps talk to OpenClaw through the Gateway protocol: WebSocket transport plus RPC methods. Use it when a script, dashboard, CI job, IDE extension, or another process wants to start agent runs, stream events, wait for results, cancel work, or inspect Gateway resources."
- **URL:** https://docs.openclaw.ai/gateway/external-apps
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "External apps and interoperability" surface, M2 Alpha (area: Agent Conversations, Client API). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Gateway protocol
- **What it does (docs):** "Gateway WebSocket protocol: handshake, frames, versioning" / "The Gateway WS protocol is the single control plane and node transport for OpenClaw. Operator and node clients (CLI, web UI, macOS app, iOS/Android nodes, headless nodes) connect over WebSocket and declare a **role** and **scope** at handshake time."
- **URL:** https://docs.openclaw.ai/gateway/protocol
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Android app" surface, M4 Stable (area: Device Runtime); "Automation and durable work" surface, M3 Beta (area: Cron Jobs); "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Tool Invocation and Execution); "ClawHub" surface, M2 Alpha (area: Plugin Lifecycle and Health); plus 9 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Gateway protocol transport (https://docs.openclaw.ai/gateway/protocol/transport); Gateway protocol handshake (https://docs.openclaw.ai/gateway/protocol/handshake); Gateway protocol presence and events (https://docs.openclaw.ai/gateway/protocol/presence); Gateway protocol RPC methods (https://docs.openclaw.ai/gateway/protocol/rpc-methods); Gateway protocol system and channel methods (https://docs.openclaw.ai/gateway/protocol/rpc-system-and-channels); Gateway protocol talk, config, and agent methods (https://docs.openclaw.ai/gateway/protocol/rpc-talk-config-and-agents); Gateway protocol session control (https://docs.openclaw.ai/gateway/protocol/rpc-session-control); Gateway protocol device, node, and approval methods (https://docs.openclaw.ai/gateway/protocol/rpc-devices-nodes-and-approvals); Gateway protocol session bootstrap and events (https://docs.openclaw.ai/gateway/protocol/rpc-bootstrap-and-events); Gateway protocol ledger RPCs (https://docs.openclaw.ai/gateway/protocol/ledgers); Gateway protocol operator methods (https://docs.openclaw.ai/gateway/protocol/operator-methods); Gateway protocol versioning (https://docs.openclaw.ai/gateway/protocol/versioning); Gateway protocol auth (https://docs.openclaw.ai/gateway/protocol/auth)

#### Embedding OpenClaw
- **What it does (docs):** "Supervise the OpenClaw Gateway as a child process from Electron or another host app" / "An embedding host should supervise the installed `openclaw` executable, use the Gateway WebSocket protocol as its control plane, and treat the child process as a replaceable runtime. This keeps process ownership, readiness, failure recovery, and upgrades explicit without depending on OpenClaw's private state layout."
- **URL:** https://docs.openclaw.ai/gateway/embedding
- **Who runs it:** User machine (the Gateway host or a client of it).

#### OpenAI chat completions
- **What it does (docs):** "Expose an OpenAI-compatible /v1/chat/completions HTTP endpoint from the Gateway" / "The Gateway can serve a small OpenAI-compatible Chat Completions surface. It is **disabled by default**."
- **URL:** https://docs.openclaw.ai/gateway/openai-http-api
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Gateway runtime" surface, M4 Stable (area: HTTP APIs); "OpenAI and Codex provider path" surface, M3 Beta (area: Responses and Tool Compatibility). Source: https://docs.openclaw.ai/maturity/taxonomy

#### OpenResponses API
- **What it does (docs):** "Expose an OpenResponses-compatible /v1/responses HTTP endpoint from the Gateway" / "The Gateway can serve an OpenResponses-compatible `POST /v1/responses` endpoint. It is **disabled by default** and shares its port with the Gateway (WS + HTTP multiplex): `http://:/v1/responses`."
- **URL:** https://docs.openclaw.ai/gateway/openresponses-http-api
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Gateway runtime" surface, M4 Stable (area: HTTP APIs); "OpenAI and Codex provider path" surface, M3 Beta (area: Responses and Tool Compatibility). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Tools invoke API
- **What it does (docs):** "Invoke a single tool directly via the Gateway HTTP endpoint" / "OpenClaw's Gateway exposes an HTTP endpoint for invoking a single tool directly. It is always enabled and uses Gateway auth plus tool policy."
- **URL:** https://docs.openclaw.ai/gateway/tools-invoke-http-api
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Tool Invocation and Execution); "Gateway runtime" surface, M4 Stable (area: HTTP APIs). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Models and local providers**

#### CLI backends
- **What it does (docs):** "CLI backends: run agent turns through a local AI CLI, with an optional MCP tool bridge" / "OpenClaw can run agent turns through a local AI CLI, such as Claude Code or Gemini CLI, instead of calling the provider API itself:"
- **URL:** https://docs.openclaw.ai/gateway/cli-backends
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Anthropic provider path" surface, M3 Beta (area: Model and Runtime Selection, Request Transport and Turn Semantics). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "Deprecated catalog models are not added at sign-in; an existing entry for one is kept and runs through Claude CLI."

#### Local models
- **What it does (docs):** "Run OpenClaw with hardware-aware local model setup or an existing model server" / "OpenClaw can install and manage a local model or connect to a server you already run. For a hardware-aware recommendation, install the llama.cpp plugin, run `openclaw onboard`, and choose **Managed local server**."
- **URL:** https://docs.openclaw.ai/gateway/local-models
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Local model providers: Ollama, vLLM, SGLang, LM Studio" surface, M2 Alpha (area: Network Safety and Prompt Controls, OpenAI-Compatible Runtime Compatibility). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "The retained experimental."

#### Local model services
- **What it does (docs):** "Start local model servers on demand before OpenClaw model and embedding requests" / "`models.providers..localService` starts a provider-owned local model server on demand. When a model or embedding request selects that provider, OpenClaw checks the health endpoint, starts the process if it is down, waits for readiness, then sends the request."
- **URL:** https://docs.openclaw.ai/gateway/local-model-services
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Local model providers: Ollama, vLLM, SGLang, LM Studio" surface, M2 Alpha (area: Provider Setup, Lifecycle, and Diagnostics). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Networking and discovery**

#### Network
- **What it does (docs):** "Network hub: gateway surfaces, pairing, discovery, and security" / "This hub links the core docs for how OpenClaw connects, pairs, and secures devices across localhost, LAN, and tailnet."
- **URL:** https://docs.openclaw.ai/network
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Node pairing
- **What it does (docs):** "Node capability approvals: how nodes gain command exposure after device pairing" / "Node pairing has two layers, both stored on the paired device record in the Gateway's SQLite state database:"
- **URL:** https://docs.openclaw.ai/gateway/pairing
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Android app" surface, M4 Stable (area: Connection Setup); "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Remote Access and Auth); "Gateway runtime" surface, M4 Stable (area: Device Auth and Pairing); "Linux companion app" surface, M3 Beta (area: Gateway Connectivity); plus 2 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "removed in"; may describe a sub-feature):** "Removed in 2026."

#### Discovery and transports
- **What it does (docs):** "Node discovery and transports (Bonjour, Tailscale, SSH) for finding the Gateway" / "OpenClaw has two related but distinct discovery problems:"
- **URL:** https://docs.openclaw.ai/gateway/discovery
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Gateway runtime" surface, M4 Stable (area: Network Access and Discovery, Security Controls). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Bonjour discovery
- **What it does (docs):** "Bonjour/mDNS discovery + debugging (Gateway beacons, clients, and common failure modes)" / "OpenClaw can use Bonjour (mDNS/DNS-SD) to discover an active gateway (WebSocket endpoint). Multicast `local.` browsing is a **LAN-only convenience**: the bundled `bonjour` plugin owns LAN advertising, auto-starting on macOS hosts and opt-in on Linux, Windows, and containerized gateway deployments."
- **URL:** https://docs.openclaw.ai/gateway/bonjour
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "Android app" surface, M4 Stable (area: Connection Setup); "macOS Gateway host" surface, M4 Stable (area: Local Gateway Integration). Source: https://docs.openclaw.ai/maturity/taxonomy

**Group: Remote access**

#### Remote access
- **What it does (docs):** "Remote access using Gateway WS, SSH tunnels, and tailnets" / "OpenClaw runs one Gateway (the master) on a host and connects every client to it. The Gateway owns sessions, auth profiles, channels, and state; everything else is a client."
- **URL:** https://docs.openclaw.ai/gateway/remote
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Remote Access and Auth); "Control UI" surface, M3 Beta (area: Browser Access and Trust); "Kubernetes hosting" surface, M2 Alpha (area: Access and Exposure); "Linux Gateway host" surface, M4 Stable (area: Remote Access and Security); plus 6 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy

#### Give your Gateway a stable HTTPS URL
- **What it does (docs):** "Give a loopback-only Gateway a stable, tailnet-only HTTPS URL with Tailscale Serve" / "Tailscale Serve gives your Gateway one HTTPS URL without exposing the Gateway port on your LAN or the public internet. The Gateway keeps listening on loopback, while Tailscale terminates HTTPS with a valid certificate and proxies requests to it."
- **URL:** https://docs.openclaw.ai/gateway/stable-https-url
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** MagicDNS enabled for your tailnet.; HTTPS certificates enabled in the Tailscale admin console under DNS > HTTPS Certificates.; Tailscale installed and logged in on the Gateway host.; The Gateway already configured with token, password, or trusted-proxy auth. Serve cannot be combined with `gateway.auth.mode: "none"`.

#### Tailscale
- **What it does (docs):** "Integrated Tailscale Serve/Funnel for the Gateway dashboard" / "OpenClaw can auto-configure Tailscale **Serve** (tailnet) or **Funnel** (public) for the Gateway dashboard and WebSocket port. This keeps the gateway bound to loopback while Tailscale provides HTTPS, routing, and (for Serve) identity headers."
- **URL:** https://docs.openclaw.ai/gateway/tailscale
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Remote Access and Auth); "Control UI" surface, M3 Beta (area: Browser Access and Trust); "Linux Gateway host" surface, M4 Stable (area: Remote Access and Security); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Gateway Auth and Remote Access); plus 1 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "preserveFunnel: true is a deprecated migration guard."

#### Cloudflare Tunnel and Access
- **What it does (docs):** "Publish a loopback Gateway through a Cloudflare Tunnel and authenticate every client with Cloudflare Access" / "Run the Gateway on loopback, publish it through a Cloudflare Tunnel, and let Cloudflare Access authenticate every request before it reaches OpenClaw. The Gateway keeps `gateway.bind: "loopback"`, so no port is exposed and no inbound firewall rule is needed; `cloudflared` dials out from the host."
- **URL:** https://docs.openclaw.ai/gateway/cloudflare-access
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Depends on (page's own requirements section):** A Cloudflare account with the zone for your hostname, and Cloudflare Zero Trust enabled.; `cloudflared` installed on the Gateway host, and on any machine that will use the CLI.; A running Gateway on `127.0.0.1:18789` with `gateway.bind: "loopback"`.; Familiarity with trusted-proxy auth, which this topology uses.

**Group: Security**

#### Network proxy
- **What it does (docs):** "How to route OpenClaw runtime HTTP and WebSocket traffic through an operator-managed filtering proxy" / "OpenClaw can route runtime HTTP and WebSocket traffic through an operator-managed forward proxy. This is optional defense in depth: central egress control, stronger SSRF protection, and destination auditability at the network boundary."
- **URL:** https://docs.openclaw.ai/security/network-proxy
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Formal verification (security models)
- **What it does (docs):** "Machine-checked security models for OpenClaw's highest-risk paths." / "OpenClaw's formal security models (TLA+/TLC today) cover specific highest-risk paths: authorization, session isolation, tool gating, and misconfiguration safety. For each path, the models give a machine-checked argument that it enforces its intended policy, under explicit stated assumptions."
- **URL:** https://docs.openclaw.ai/security/formal-verification
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Incident response
- **What it does (docs):** "How OpenClaw triages, responds to, and follows up on security incidents" / "Security signals come from:"
- **URL:** https://docs.openclaw.ai/security/incident-response
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Threat model (MITRE ATLAS)
- **What it does (docs):** "OpenClaw threat model mapped to the MITRE ATLAS framework" / "This threat model documents adversarial threats to the OpenClaw AI agent platform and ClawHub skill marketplace. It is a living document maintained by the OpenClaw community."
- **URL:** https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "Skills and packages carry moderator-assigned badges: highlighted, official, deprecated, redactionApproved (skills only)."

#### Reconnaissance (AML.TA0002)
- **What it does (docs):** "OpenClaw reconnaissance threats (AML.TA0002): T-RECON-001, T-RECON-002" / "Threats in the reconnaissance tactic (AML.TA0002) of the MITRE ATLAS framework. Each entry lists the ATLAS technique, attack vector, affected components, current mitigations, residual risk, and recommendations."
- **URL:** https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/reconnaissance
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Initial access (AML.TA0004)
- **What it does (docs):** "OpenClaw initial access threats (AML.TA0004): T-ACCESS-001, T-ACCESS-002, T-ACCESS-003" / "Threats in the initial access tactic (AML.TA0004) of the MITRE ATLAS framework. Each entry lists the ATLAS technique, attack vector, affected components, current mitigations, residual risk, and recommendations."
- **URL:** https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/initial-access
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Execution (AML.TA0005)
- **What it does (docs):** "OpenClaw execution threats (AML.TA0005): T-EXEC-001, T-EXEC-002, T-EXEC-003, T-EXEC-004" / "Threats in the execution tactic (AML.TA0005) of the MITRE ATLAS framework. Each entry lists the ATLAS technique, attack vector, affected components, current mitigations, residual risk, and recommendations."
- **URL:** https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/execution
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Persistence (AML.TA0006)
- **What it does (docs):** "OpenClaw persistence threats (AML.TA0006): T-PERSIST-001, T-PERSIST-002, T-PERSIST-003" / "Threats in the persistence tactic (AML.TA0006) of the MITRE ATLAS framework. Each entry lists the ATLAS technique, attack vector, affected components, current mitigations, residual risk, and recommendations."
- **URL:** https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/persistence
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Defense evasion (AML.TA0007)
- **What it does (docs):** "OpenClaw defense evasion threats (AML.TA0007): T-EVADE-001, T-EVADE-002" / "Threats in the defense evasion tactic (AML.TA0007) of the MITRE ATLAS framework. Each entry lists the ATLAS technique, attack vector, affected components, current mitigations, residual risk, and recommendations."
- **URL:** https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/defense-evasion
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Discovery (AML.TA0008)
- **What it does (docs):** "OpenClaw discovery threats (AML.TA0008): T-DISC-001, T-DISC-002" / "Threats in the discovery tactic (AML.TA0008) of the MITRE ATLAS framework. Each entry lists the ATLAS technique, attack vector, affected components, current mitigations, residual risk, and recommendations."
- **URL:** https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/discovery
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Collection and exfiltration (AML.TA0009, AML.TA0010)
- **What it does (docs):** "OpenClaw collection and exfiltration threats (AML.TA0009, AML.TA0010): T-EXFIL-001, T-EXFIL-002, T-EXFIL-003" / "Threats in the collection and exfiltration tactic (AML.TA0009, AML.TA0010) of the MITRE ATLAS framework. Each entry lists the ATLAS technique, attack vector, affected components, current mitigations, residual risk, and recommendations."
- **URL:** https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/collection-and-exfiltration
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Impact (AML.TA0011)
- **What it does (docs):** "OpenClaw impact threats (AML.TA0011): T-IMPACT-001, T-IMPACT-002, T-IMPACT-003" / "Threats in the impact tactic (AML.TA0011) of the MITRE ATLAS framework. Each entry lists the ATLAS technique, attack vector, affected components, current mitigations, residual risk, and recommendations."
- **URL:** https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/impact
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Contributing to the threat model
- **What it does (docs):** "How to contribute to the OpenClaw threat model" / "The threat model is a living document. Contributions are welcome from anyone; you do not need security or MITRE ATLAS background."
- **URL:** https://docs.openclaw.ai/security/CONTRIBUTING-THREAT-MODEL
- **Who runs it:** User machine (the Gateway host or a client of it).

**Group: Nodes and media**

#### Nodes
- **What it does (docs):** "Nodes: pairing, capabilities, permissions, and CLI helpers for camera/screen/device/notifications/system and the macOS widget panel" / "A **node** is a companion device (macOS/iOS/watchOS/Android/headless) that connects to the Gateway with `role: "node"` and exposes a command surface (e.g. `camera.*`, `device.*`, `notifications.*`, `system.*`) via `node.invoke`."
- **URL:** https://docs.openclaw.ai/nodes
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "Gateway runtime" surface, M4 Stable (area: Nodes and Remote Capabilities); "Linux companion app" surface, M3 Beta (area: Desktop Capabilities); "Windows App / Node" surface, M3 Beta (area: Desktop Tools and Permissions). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Node pairing and status
- **What it does (docs):** "Pair a node to the Gateway, read its status, and upgrade a fleet in the right order" / "Nodes use **device pairing**. A node presents a signed device identity during connect; the Gateway creates a device pairing request for `role: node`."
- **URL:** https://docs.openclaw.ai/nodes/pairing-and-status
- **Who runs it:** User device (companion app or node) paired to the user Gateway.

#### Run a node host
- **What it does (docs):** "Start a headless or service node host, pair it, and use its system commands" / "Use a **node host** when your Gateway runs on one machine and you want commands to execute on another. The model still talks to the **gateway**; the gateway forwards `exec` calls to the **node host** when `host=node` is selected."
- **URL:** https://docs.openclaw.ai/nodes/node-host
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status wording (first sentence on the page with "was removed"; may describe a sub-feature):** "run execution path was removed in 2026."

#### Run commands on a node
- **What it does (docs):** "Allowlist node commands, point exec at a node, and invoke commands directly" / "Exec approvals are **per node host**. Add allowlist entries from the gateway:"
- **URL:** https://docs.openclaw.ai/nodes/node-exec
- **Who runs it:** User device (companion app or node) paired to the user Gateway.

#### Node-hosted MCP servers and skills
- **What it does (docs):** "Publish MCP servers, skills, and local model inference from a paired node" / "Configure MCP servers in `openclaw.json` on the node machine, not on the Gateway:"
- **URL:** https://docs.openclaw.ai/nodes/mcp-and-skills
- **Who runs it:** User device (companion app or node) paired to the user Gateway.

#### Host OpenClaw sessions on a node
- **What it does (docs):** "Enable worker session hosting on a paired node, choose a device, and isolate workers in containers" / "The macOS menu bar app and the headless node host can opt into full OpenClaw session hosting with the same node-local setting:"
- **URL:** https://docs.openclaw.ai/nodes/session-hosting
- **Who runs it:** User device (companion app or node) paired to the user Gateway.

#### Node session catalogs
- **What it does (docs):** "Discover, import, and continue native session transcripts on the Gateway and paired nodes" / "Cold catalog listing waits up to one second per provider, concurrently. Providers that finish within that budget return normally."
- **URL:** https://docs.openclaw.ai/nodes/session-catalogs
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: Cross-client History and Session Parity). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Node file transfers
- **What it does (docs):** "Upload files into a node terminal and move files with the File Transfer plugin" / "The Control UI can drag files into an open paired-node terminal. The native node host advertises the admin-only `terminal.upload` command; approve the pairing upgrade when it first appears."
- **URL:** https://docs.openclaw.ai/nodes/file-transfers
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "experimental and unsupported for production."

#### Node command policy
- **What it does (docs):** "Platform default allowlists, dangerous-command opt-ins, and the gateway.nodes configuration" / "After device pairing, node commands must satisfy three requirements before they can be invoked:"
- **URL:** https://docs.openclaw.ai/nodes/command-policy
- **Who runs it:** User device (companion app or node) paired to the user Gateway.

#### Node device commands
- **What it does (docs):** "CLI helpers for the widget panel, camera, screen, location, SMS, and device data" / "Notes:"
- **URL:** https://docs.openclaw.ai/nodes/device-commands
- **Who runs it:** User device (companion app or node) paired to the user Gateway.

#### Active computer presence
- **What it does (docs):** "Detect the Mac you most recently used and route node alerts there" / "Active computer presence tells the Gateway which connected macOS node received the most recent activity. Basic presence works when you interact with the OpenClaw app, without extra permissions."
- **URL:** https://docs.openclaw.ai/nodes/presence
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Depends on (page's own requirements section):** The OpenClaw macOS app is paired and connected in node mode.; Interact with the OpenClaw app to provide basic presence. Merely running or; To include activity in other apps, enable Settings -> Permissions ->; For connection alerts, Notifications permission is also granted and the

#### Node troubleshooting
- **What it does (docs):** "Troubleshoot node pairing, foreground requirements, permissions, and tool failures" / "Use this page when a node is visible in status but node tools fail."
- **URL:** https://docs.openclaw.ai/nodes/troubleshooting
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "Android app" surface, M4 Stable (area: Device Runtime). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Media capabilities**

#### Media understanding
- **What it does (docs):** "Inbound image/audio/video understanding (optional) with provider + CLI fallbacks" / "OpenClaw can summarize inbound media (image/audio/video) before the reply pipeline runs, so command parsing and routing work off short text instead of raw bytes. Understanding auto-detects local tools or provider keys, or you can configure explicit models."
- **URL:** https://docs.openclaw.ai/nodes/media-understanding
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "Media understanding and media generation" surface, M2 Alpha (area: Media Intake and Access, Media Understanding); "Google Chat" surface, M2 Alpha (area: Media and Rich Content, Native Controls and Approvals). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Media playback
- **What it does (docs):** "Inline audio and video playback across the Control UI and native apps" / "OpenClaw chat clients play assistant audio and video attachments inline. The Gateway keeps those attachments behind session-scoped access, serves seekable byte ranges, and can prepare a portable playback rendition for recognized formats that are not safe across every client."
- **URL:** https://docs.openclaw.ai/nodes/media-playback
- **Who runs it:** User device (companion app or node) paired to the user Gateway.

#### Image and media support
- **What it does (docs):** "Image and media handling rules for send, gateway, and agent replies" / "The WhatsApp channel runs on Baileys Web. This page covers media handling rules for send, gateway, and agent replies."
- **URL:** https://docs.openclaw.ai/nodes/images
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "Media understanding and media generation" surface, M2 Alpha (area: Channel Media Handling, Media Understanding); "OpenAI and Codex provider path" surface, M3 Beta (area: Image and Multimodal Input). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Audio and voice notes
- **What it does (docs):** "How inbound audio/voice notes are downloaded, transcribed, and injected into replies" / "This page covers inbound transcription and voice-note handling. For inline audio and video players in OpenClaw chat clients, see Media playback."
- **URL:** https://docs.openclaw.ai/nodes/audio
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "Media understanding and media generation" surface, M2 Alpha (area: Media Understanding). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "Run openclaw doctor --fix to migrate deprecated {input} placeholders from older audio."

#### Camera capture
- **What it does (docs):** "Camera capture and macOS physical PTZ control on paired nodes" / "OpenClaw supports camera capture for agent workflows on paired **iOS**, **Android**, **macOS**, and **Linux** nodes: capture a photo (`jpg`) or a short video clip (`mp4`, with optional audio) via Gateway `node.invoke`."
- **URL:** https://docs.openclaw.ai/nodes/camera
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "Android app" surface, M4 Stable (area: Media Capture); "Linux companion app" surface, M3 Beta (area: Desktop Capabilities); "iOS app" surface, M4 Stable (area: Media and Sharing). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Node features**

#### Computer use
- **What it does (docs):** "Capability-based control of Gateway and paired node desktops through the computer tool" / "Computer use lets an agent see and control the Gateway's own desktop or a paired node's desktop through one built-in `computer` tool. Both hosts use the same `computer.act` and `screen.snapshot` contracts; CUA reuses the same provider implementation on either host."
- **URL:** https://docs.openclaw.ai/nodes/computer-use
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Depends on (page's own requirements section):** An available computer provider on the Gateway, or a paired, connected node advertising both `computer.act` and `screen.snapshot`, with `screen.snapshot` returni; macOS fulfiller: app setting Allow Computer Control enabled. It defaults on; an explicit off choice stays off.; macOS fulfiller: choose Peekaboo (default) or CUA. CUA is selectable only when the pinned driver is present in the signed app bundle; development builds without; macOS fulfiller: Accessibility and Screen Recording granted to OpenClaw. The native Peekaboo path also requires Event Posting access for its CoreGraphics input 
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Windows and Linux can use the optional, experimental cua-computer plugin, which calls the packaged CUA Driver SDK directly."

#### Talk mode
- **What it does (docs):** "Talk mode: continuous speech conversations across local STT/TTS and realtime voice" / "Talk mode covers these runtime shapes:"
- **URL:** https://docs.openclaw.ai/nodes/talk
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "Android app" surface, M4 Stable (area: Voice); "Control UI" surface, M3 Beta (area: Browser Realtime Talk); "Linux companion app" surface, M3 Beta (area: Desktop Capabilities); "Voice and realtime talk" surface, M2 Alpha (area: Native App Talk, Realtime Talk Sessions); plus 2 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "speakerVoice | alloy for GA; route-specific for GPT-Live | Built-in OpenAI realtime voice id (the older voice key still works but is deprecated)."
- **Sub-pages in the nav:** Talk realtime sessions and delegation (https://docs.openclaw.ai/nodes/talk/realtime-sessions); Talk session ownership (https://docs.openclaw.ai/nodes/talk/session-ownership); Talk on macOS and the Gateway relay (https://docs.openclaw.ai/nodes/talk/macos-relay); Talk client UI (https://docs.openclaw.ai/nodes/talk/client-ui)

#### Voice wake
- **What it does (docs):** "Global voice wake words (Gateway-owned) and how they sync across nodes" / "Wake words are **one global list owned by the Gateway** — there are no per-node custom lists. Any node or app UI can edit the list; the Gateway persists the change and broadcasts it to every connected client."
- **URL:** https://docs.openclaw.ai/nodes/voicewake
- **Who runs it:** User device (companion app or node) paired to the user Gateway.
- **Status (maturity scorecard, which links this page):** "Voice and realtime talk" surface, M2 Alpha (area: Voice Wake and Routing). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Location command
- **What it does (docs):** "Location command for nodes, platform permission modes, and Linux GeoClue setup" / "OS location permissions are multi-level. Precise location is a separate OS grant too (iOS 14+ "Precise", Android "fine" vs "coarse")."
- **URL:** https://docs.openclaw.ai/nodes/location-command
- **Who runs it:** User device (companion app or node) paired to the user Gateway.

**Group: Web interfaces**

#### Web
- **What it does (docs):** "Gateway web surfaces: Control UI, bind modes, and security" / "The Gateway serves a small **browser Control UI** (Vite + Lit) from the same port as the Gateway WebSocket:"
- **URL:** https://docs.openclaw.ai/web
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Control UI" surface, M3 Beta (area: Browser UI); "Gateway runtime" surface, M4 Stable (area: HTTP APIs). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Control UI
- **What it does (docs):** "Browser-based control UI for the Gateway (chat, activity, nodes, config)" / "The Control UI is a small **Vite + Solid** single-page app served by the Gateway:"
- **URL:** https://docs.openclaw.ai/web/control-ui
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Control UI" surface, M3 Beta (area: Browser Access and Trust, Browser Realtime Talk); "Gateway runtime" surface, M4 Stable (area: Hosted Web Surface); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Device and Node Pairing, Gateway Auth and Remote Access); "Voice and realtime talk" surface, M2 Alpha (area: Realtime Talk Sessions, Talk Observability); plus 1 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Connect and pair (https://docs.openclaw.ai/web/control-ui/connect-and-pair); Sessions and sidebar (https://docs.openclaw.ai/web/control-ui/sessions-and-sidebar); Chat (https://docs.openclaw.ai/web/control-ui/chat); Panels and docks (https://docs.openclaw.ai/web/control-ui/panels); Settings (https://docs.openclaw.ai/web/control-ui/settings); Feature and RPC reference (https://docs.openclaw.ai/web/control-ui/feature-reference); Offline and reconnect (https://docs.openclaw.ai/web/control-ui/offline-and-reconnect); Security model (https://docs.openclaw.ai/web/control-ui/security-model); Build and develop (https://docs.openclaw.ai/web/control-ui/development)

#### Portals
- **What it does (docs):** "Expose agent-run development servers to the operator through the Gateway" / "Portals expose a development server running on the Gateway host or a node-backed cloud worker to the operator's browser. They proxy HTTP and WebSockets for live reload and appear in **Control UI → Portals**."
- **URL:** https://docs.openclaw.ai/gateway/portals
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Notifications
- **What it does (docs):** "Enable and test browser or macOS notifications from the Control UI" / "OpenClaw can ping you when something needs your attention, including an exec or plugin approval request. The ping arrives in the browser that runs the Control UI."
- **URL:** https://docs.openclaw.ai/web/notifications
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Dashboard
- **What it does (docs):** "Gateway dashboard (Control UI) access and auth" / "The Gateway dashboard is the browser Control UI served at `/` by default (override with `gateway.controlUi.basePath`)."
- **URL:** https://docs.openclaw.ai/web/dashboard
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "Control UI" surface, M3 Beta (area: Browser Access and Trust, Browser UI). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Session Dashboards
- **What it does (docs):** "Session dashboards: agent-built widgets, boards, tabs, and flexible task layouts" / "Every thread in the Control UI can own a **dashboard** — a grid of live widgets your agent builds for you. Choose **Dashboard** in the side panel to open the current task's board, even before it has widgets."
- **URL:** https://docs.openclaw.ai/web/dashboards
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status wording (first sentence on the page with "have been removed"; may describe a sub-feature):** "CLI, and workspace_ tools have been removed."

#### Dashboard Architecture
- **What it does (docs):** "Session dashboard architecture: widget hosting, capabilities, board storage, and protocol" / "Session dashboards are persistent widget boards attached to a session. This reference covers their ownership, sandbox and capability boundaries, storage, and Gateway protocol."
- **URL:** https://docs.openclaw.ai/web/dashboard-architecture
- **Who runs it:** User machine (the Gateway host or a client of it).

#### Control UI URLs
- **What it does (docs):** "Control UI routes, focus presentations, stable session links, and connection handoff parameters" / "The Control UI uses readable paths for pages and session links. A configured `gateway.controlUi.basePath` prefixes every path below."
- **URL:** https://docs.openclaw.ai/web/urls
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status wording (first sentence on the page with "was removed"; may describe a sub-feature):** "if the agent was removed, it uses the current agent instead."

#### WebChat
- **What it does (docs):** "Native and Control UI WebChat usage over the Gateway WebSocket" / "Status: the macOS/iOS SwiftUI chat UI talks directly to the Gateway WebSocket. No embedded browser, no local static server."
- **URL:** https://docs.openclaw.ai/web/webchat
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** included in core
- **Status (maturity scorecard, which links this page):** "Control UI" surface, M3 Beta (area: WebChat Conversations); "Gateway runtime" surface, M4 Stable (area: Hosted Web Surface); "Linux companion app" surface, M3 Beta (area: Chat and Sessions); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Device and Node Pairing); plus 3 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "Status"; may describe a sub-feature):** "Status: the macOS/iOS SwiftUI chat UI talks directly to the Gateway WebSocket."

#### TUI
- **What it does (docs):** "Terminal UI (TUI): connect to the Gateway or run locally in embedded mode" / "2. Open the TUI."
- **URL:** https://docs.openclaw.ai/web/tui
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Status (maturity scorecard, which links this page):** "TUI" surface, M2 Alpha (area: Input and Commands, Local Shell Execution). Source: https://docs.openclaw.ai/maturity/taxonomy

#### The Lobster
- **What it does (docs):** "A lobster sometimes visits the Control UI. This page explains just enough." / "When you open a new session in the Control UI, a small lobster may visit the composer, look around, and make itself at home for a few minutes. Other critters sometimes pass through too."
- **URL:** https://docs.openclaw.ai/web/lobster
- **Who runs it:** User machine (the Gateway host or a client of it).
- **Packaging (docs):** plugin inventory: npm or ClawHub: `@openclaw/lobster` (Official external packages)

### Tab: Reference

**Group: CLI commands**

#### CLI reference
- **What it does (docs):** "OpenClaw CLI index: command list, global flags, and links to per-command pages" / "`openclaw` is the main CLI entry point. Each core command has a dedicated reference page or is documented with the command it aliases."
- **URL:** https://docs.openclaw.ai/cli
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "TUI" surface, M2 Alpha (area: Runtime Modes). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Running the service**

#### Daemon
- **What it does (docs):** "CLI reference for `openclaw daemon` (legacy alias for gateway service management)" / "Legacy alias for Gateway service management. `openclaw daemon ...` maps to the same service-control commands as `openclaw gateway ...`."
- **URL:** https://docs.openclaw.ai/cli/daemon
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Gateway
- **What it does (docs):** "OpenClaw Gateway CLI (`openclaw gateway`) — run, query, and discover gateways" / "The Gateway is OpenClaw's WebSocket server (channels, nodes, sessions, hooks). All subcommands on the pages listed here live under `openclaw gateway ...`."
- **URL:** https://docs.openclaw.ai/cli/gateway
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Linux Gateway host" surface, M4 Stable (area: Gateway Runtime and Service Control); "macOS Gateway host" surface, M4 Stable (area: Diagnostics and Observability, Gateway Service Lifecycle); "CLI" surface, M4 Stable (area: Gateway Service Management); "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Gateway Runtime); plus 2 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Run the Gateway (https://docs.openclaw.ai/cli/gateway/running); Restart and supervision (https://docs.openclaw.ai/cli/gateway/restart-and-supervision); Query a running Gateway (https://docs.openclaw.ai/cli/gateway/query); Manage the Gateway service (https://docs.openclaw.ai/cli/gateway/service); Discover gateways (Bonjour) (https://docs.openclaw.ai/cli/gateway/discovery)

#### Health
- **What it does (docs):** "CLI reference for `openclaw health` (gateway health snapshot via RPC)" / "Fetch a health snapshot from the running Gateway over WebSocket RPC (no direct channel sockets from the CLI)."
- **URL:** https://docs.openclaw.ai/cli/health
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: CLI Observability); "Observability" surface, M3 Beta (area: Health and Repair). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Logs
- **What it does (docs):** "CLI reference for `openclaw logs` (tail gateway logs via RPC)" / "Tail Gateway file logs over RPC. Works in remote mode."
- **URL:** https://docs.openclaw.ai/cli/logs
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: CLI Observability); "Linux Gateway host" surface, M4 Stable (area: Diagnostics and Repair); "Observability" surface, M3 Beta (area: Logging); "TUI" surface, M2 Alpha (area: Rendering and Output Safety); plus 1 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy

#### openclaw status
- **What it does (docs):** "CLI reference for `openclaw status` (diagnostics, checks, usage snapshots)" / "Diagnostics for channels + sessions."
- **URL:** https://docs.openclaw.ai/cli/status
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: CLI Observability); "Linux Gateway host" surface, M4 Stable (area: Diagnostics and Repair); "Windows via WSL2" surface, M3 Beta (area: CLI, Diagnostics and Repair). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Setup and maintenance**

#### Backup
- **What it does (docs):** "CLI reference for `openclaw backup` (local and offsite archives, SQLite snapshots, Git history, and schedules)" / "Human-readable schedule acknowledgements and external backup record labels strip terminal escape sequences and display embedded newlines, tabs, and carriage returns as `\n`, `\t`, and `\r`. Scheduled command arguments, stored records, and JSON output retain their original values."
- **URL:** https://docs.openclaw.ai/cli/backup
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: Diagnostics, Maintenance, and Recovery). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Migrate
- **What it does (docs):** "CLI reference for `openclaw migrate` (import state from another agent system)" / "Import state from another agent system through a plugin-owned migration provider. Bundled providers cover Claude, Codex CLI, and Hermes."
- **URL:** https://docs.openclaw.ai/cli/migrate
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Onboard
- **What it does (docs):** "CLI reference for `openclaw onboard` (interactive onboarding)" / "Guided setup that establishes inference first: it detects existing AI access, waits for your provider choice, verifies that connection, persists only the working route, and then starts OpenClaw to configure the rest. `openclaw setup` reaches this flow on fresh systems or whenever an onboarding option is present; configured systems use bare `openclaw ..."
- **URL:** https://docs.openclaw.ai/cli/onboard
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: Onboarding and Auth Setup, Plugin and Channel Setup); "Long-tail hosted providers" surface, M2 Alpha (area: Hosted LLM Providers); "Native Windows" surface, M2 Alpha (area: CLI); "Windows via WSL2" surface, M3 Beta (area: CLI). Source: https://docs.openclaw.ai/maturity/taxonomy

#### OpenClaw setup agent
- **What it does (docs):** "CLI reference and security model for the inference-backed OpenClaw setup and repair helper" / "OpenClaw ships with a built-in system agent — it speaks as "OpenClaw" — for local setup, repair, and configuration (formerly called Crestodian). It starts only after the effective default model completes a real turn."
- **URL:** https://docs.openclaw.ai/cli/openclaw
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Reset
- **What it does (docs):** "CLI reference for `openclaw reset` (reset local state/config)" / "Reset local config/state (keeps the CLI installed)."
- **URL:** https://docs.openclaw.ai/cli/reset
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Setup CLI
- **What it does (docs):** "CLI reference for `openclaw setup` (system-agent chat with onboarding fallback)" / "Interactive setup offers optional memory embedding provider/model setup with a synthetic readiness check. Skip it without changing existing memory settings, or configure it later with `openclaw configure --section memory`."
- **URL:** https://docs.openclaw.ai/cli/setup
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Nix install path" surface, M1 Experimental (area: Config and State, Service Runtime and Guards). Source: https://docs.openclaw.ai/maturity/taxonomy

#### storage
- **What it does (docs):** "List, initialize, and test configured storage locations" / "Manage named destinations configured under `storage.locations`. See Storage locations for configuration, encryption, and provider contracts."
- **URL:** https://docs.openclaw.ai/cli/storage
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Uninstall CLI
- **What it does (docs):** "CLI reference for `openclaw uninstall` (remove gateway service + local data)" / "Uninstall the Gateway service and/or local data. There is no separate CLI-removal scope."
- **URL:** https://docs.openclaw.ai/cli/uninstall
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Update
- **What it does (docs):** "CLI reference for `openclaw update` (updates, repair, and recovery cleanup)" / "Update OpenClaw and switch between stable/extended-stable/beta/dev channels."
- **URL:** https://docs.openclaw.ai/cli/update
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: Updates and Upgrades); "Nix install path" surface, M1 Experimental (area: Service Runtime and Guards); "macOS Gateway host" surface, M4 Stable (area: Gateway Service Lifecycle). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Update status and run history (https://docs.openclaw.ai/cli/update/status-and-history); Update repair and recovery (https://docs.openclaw.ai/cli/update/repair-and-recovery); How an update runs (https://docs.openclaw.ai/cli/update/how-updates-run)

**Nav subgroup: Diagnostics and security**

#### Doctor CLI
- **What it does (docs):** "CLI reference for `openclaw doctor` (health checks + guided repairs)" / "Health checks and quick fixes for the gateway, channels, plugins, skills, model routing, local state, and config migrations. Use it whenever something is not behaving as expected and you want one command to explain what is wrong."
- **URL:** https://docs.openclaw.ai/cli/doctor
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: Doctor); "Linux Gateway host" surface, M4 Stable (area: Diagnostics and Repair); "Native Windows" surface, M2 Alpha (area: Gateway Management); "Nix install path" surface, M1 Experimental (area: Service Runtime and Guards); plus 3 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Run doctor (https://docs.openclaw.ai/cli/doctor/running); Gateway and service recovery (https://docs.openclaw.ai/cli/doctor/recovery); Lint and post-upgrade modes (https://docs.openclaw.ai/cli/doctor/lint); Structured health check contract (https://docs.openclaw.ai/cli/doctor/health-contract); Legacy state migration (https://docs.openclaw.ai/cli/doctor/state-migrations); SQLite maintenance and session migration (https://docs.openclaw.ai/cli/doctor/sqlite-maintenance); Other checks and repairs (https://docs.openclaw.ai/cli/doctor/checks)

#### Secrets CLI
- **What it does (docs):** "CLI reference for `openclaw secrets` (store, reload, audit, configure, apply)" / "Manage SecretRefs and keep the active runtime snapshot healthy."
- **URL:** https://docs.openclaw.ai/cli/secrets
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Security, auth, pairing, and secrets" surface, M3 Beta (area: Credential and Secret Hygiene). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Security CLI
- **What it does (docs):** "CLI reference for `openclaw security` (audit and fix common security footguns)" / "Security tools: audit plus optional safe fixes. Related: Security."
- **URL:** https://docs.openclaw.ai/cli/security
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Triage
- **What it does (docs):** "CLI reference for `openclaw triage` (sanitized diagnostics and agent handoff)" / "Collect sanitized diagnostics and open a coding agent on this machine to diagnose, repair, and verify this OpenClaw installation."
- **URL:** https://docs.openclaw.ai/cli/triage
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status wording (first sentence on the page with "was removed"; may describe a sub-feature):** "The agent starts in the operator's captured working directory, or their OS home if that directory was removed or became inaccessible."

**Nav subgroup: Agents, models, and sessions**

#### Agent
- **What it does (docs):** "CLI reference for Gateway-backed `openclaw agent` turns and isolated `agent exec` runs" / "Run one agent turn through the Gateway. The explicit `--local` flag and `agent exec` are the embedded execution paths."
- **URL:** https://docs.openclaw.ai/cli/agent
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Agent Runtime" surface, M3 Beta (area: Agent Turn Execution, Local and Self-hosted Providers). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Agents
- **What it does (docs):** "CLI reference for `openclaw agents` (roles, teams, workspaces, routing, and identity)" / "Manage isolated agents (workspaces + auth + routing). Running `openclaw agents` with no subcommand is equivalent to `openclaw agents list`."
- **URL:** https://docs.openclaw.ai/cli/agents
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Templates
- **What it does (docs):** "Author, inspect, and add Template bundles as ordinary agents" / "A Template is a portable setup for a new OpenClaw agent. It can include agent instructions, workspace files, skills, plugins, MCP servers, and automations."
- **URL:** https://docs.openclaw.ai/cli/templates
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Inference CLI
- **What it does (docs):** "Infer-first CLI for provider-backed model, image, audio, TTS, video, web, and embedding workflows" / "`openclaw infer` is the main headless command for provider-backed inference. It exposes capability families (`model`, `image`, `audio`, `tts`, `video`, `web`, `embedding`), not raw gateway RPC names or agent tool ids."
- **URL:** https://docs.openclaw.ai/cli/infer
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Image, video, and music generation tools" surface, M2 Alpha (area: Image Generation); "Media understanding and media generation" surface, M2 Alpha (area: Media Understanding). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Memory
- **What it does (docs):** "CLI reference for `openclaw memory` (status/index/reset/search/forget/promote/promote-explain/rem-harness/rem-backfill/session-backfill)" / "Manage semantic memory indexing, search, promotion into `MEMORY.md`, and provenance-based deletion. Provided by the bundled `memory-core` plugin."
- **URL:** https://docs.openclaw.ai/cli/memory
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Models
- **What it does (docs):** "CLI reference for `openclaw models` (status/list/set/scan, aliases, fallbacks, shared auth, personal accounts)" / "Model discovery, scanning, and configuration (default model, fallbacks, auth profiles)."
- **URL:** https://docs.openclaw.ai/cli/models
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Agent Runtime" surface, M3 Beta (area: Model and Runtime Selection, Provider Auth); "Long-tail hosted providers" surface, M2 Alpha (area: Provider Operations); "OpenRouter provider path" surface, M3 Beta (area: Provider Recovery and Diagnostics, Provider Setup and Auth); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Credential and Secret Hygiene). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Promos
- **What it does (docs):** "CLI reference for `openclaw promos` (list and claim promotional model offers)" / "Discover and claim promotional model offers published on ClawHub. Claiming a promotion configures the provider (auth and plugin, when needed) and registers the promotion's models — without re-running onboarding and without changing your default model unless you say so."
- **URL:** https://docs.openclaw.ai/cli/promos
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Sessions
- **What it does (docs):** "CLI reference for listing, importing, archiving, deleting, and maintaining stored sessions" / "List stored conversation sessions."
- **URL:** https://docs.openclaw.ai/cli/sessions
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: CLI Session and Transcript Management); "TUI" surface, M2 Alpha (area: Session Management). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Transcripts CLI
- **What it does (docs):** "CLI reference for `openclaw transcripts` (list, show, and export stored transcripts)" / "Inspector and export command for durable meeting transcripts. Google Meet, Microsoft Teams, Slack huddles, and Zoom browser participants capture notes automatically; the `transcripts` agent tool also supports provider capture and manual import."
- **URL:** https://docs.openclaw.ai/cli/transcripts
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Wiki
- **What it does (docs):** "CLI reference for `openclaw wiki` (memory-wiki vault status, search, compile, lint, apply, bridge, ChatGPT import, and Obsidian helpers)" / "Inspect and maintain the `memory-wiki` vault. Provided by the bundled optional `memory-wiki` plugin."
- **URL:** https://docs.openclaw.ai/cli/wiki
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Intentionally experimental and same-machine only."

**Nav subgroup: Events and audit records**

#### Audit records
- **What it does (docs):** "CLI reference for activity records, execution identity, and decision receipts" / "Query the Gateway's metadata-only activity ledger, discover executions that share a run correlation, or inspect immutable identity context for one exact agent execution."
- **URL:** https://docs.openclaw.ai/cli/audit
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Hooks CLI
- **What it does (docs):** "CLI reference for internal hook discovery, eligibility, enablement, and hook packs" / "Inspect and configure internal hooks: handlers for command, message, session, and Gateway events. Bare `openclaw hooks` runs the same report as `openclaw hooks list`."
- **URL:** https://docs.openclaw.ai/cli/hooks
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Automation Hooks). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "when reached through the deprecated alias."

#### Message
- **What it does (docs):** "CLI reference for `openclaw message` (send + channel actions)" / "Single outbound command for sending messages and channel actions across Discord, Google Chat, iMessage, Matrix, Mattermost (plugin), Microsoft Teams, Signal, Slack, Telegram, and WhatsApp."
- **URL:** https://docs.openclaw.ai/cli/message
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Polling Controls); "Google Chat" surface, M2 Alpha (area: Media and Rich Content, Native Controls and Approvals). Source: https://docs.openclaw.ai/maturity/taxonomy

#### System
- **What it does (docs):** "CLI reference for `openclaw system` (system events, heartbeat, presence)" / "System-level helpers for the Gateway: enqueue system events, control migrated monitor jobs through legacy interfaces, and view presence."
- **URL:** https://docs.openclaw.ai/cli/system
- **Who runs it:** User machine (CLI or Gateway on the user host).

**Nav subgroup: Channels and messaging**

#### Channels
- **What it does (docs):** "CLI reference for `openclaw channels` (accounts, status, dead letters, capabilities, resolve, logs, login/logout)" / "Manage chat channel accounts and their runtime status on the Gateway."
- **URL:** https://docs.openclaw.ai/cli/channels
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: Plugin and Channel Setup); "Discord" surface, M4 Stable (area: Channel Setup and Operations); "Telegram" surface, M3 Beta (area: Channel Setup and Operations). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Directory
- **What it does (docs):** "CLI reference for `openclaw directory` (self, peers, groups)" / "Directory lookups for channels that support them: contacts/peers, groups, and "me" (self)."
- **URL:** https://docs.openclaw.ai/cli/directory
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Pairing CLI
- **What it does (docs):** "CLI reference for `openclaw pairing` (approve/list pairing requests)" / "Approve or inspect DM pairing requests for channels that support pairing (chat DMs only - node/device pairing uses `openclaw devices`)."
- **URL:** https://docs.openclaw.ai/cli/pairing
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Pair
- **What it does (docs):** "CLI reference for `openclaw pair` (approve a browser showing a pairing code)" / "Approve a browser that is showing a pairing code. Choose **Pair this browser** in the Control UI to get a code."
- **URL:** https://docs.openclaw.ai/cli/pair
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### QR
- **What it does (docs):** "CLI reference for `openclaw qr` (generate mobile pairing QR + setup code)" / "Generate a mobile pairing QR and setup code from your current Gateway configuration."
- **URL:** https://docs.openclaw.ai/cli/qr
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Media understanding and media generation" surface, M2 Alpha (area: Media Intake and Access); "TUI" surface, M2 Alpha (area: Rendering and Output Safety). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Users
- **What it does (docs):** "CLI reference for `openclaw users` (profiles, email aliases, and duplicate merges)" / "Manage durable Gateway profiles through the Gateway RPC API. These profiles identify people; they are separate from the CLI's `--profile` option, which selects an isolated OpenClaw configuration and state directory."
- **URL:** https://docs.openclaw.ai/cli/users
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Voicecall
- **What it does (docs):** "CLI reference for `openclaw voicecall` (voice-call plugin command surface)" / "`voicecall` is a plugin-provided command. It only appears when the voice-call plugin is installed and enabled."
- **URL:** https://docs.openclaw.ai/cli/voicecall
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Voice Call channel" surface, M1 Experimental (area: Access and Identity, Channel Setup and Operations). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Tools and execution**

#### Approvals
- **What it does (docs):** "CLI reference for `openclaw approvals` and `openclaw exec-policy`" / "Manage exec approvals for the **local host**, **gateway host**, or a **node host**. With no target flag, `get`, `set`, and allowlist edits select the local approvals document in shared SQLite state."
- **URL:** https://docs.openclaw.ai/cli/approvals
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Security, auth, pairing, and secrets" surface, M3 Beta (area: Approval Policy and Tool Safeguards, Device and Node Pairing). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Browser
- **What it does (docs):** "CLI reference for `openclaw browser` (lifecycle, profiles, tabs, actions, state, and debugging)" / "Manage OpenClaw's browser control surface and run browser actions: lifecycle, profiles, tabs, snapshots, screenshots, navigation, input, state emulation, and debugging."
- **URL:** https://docs.openclaw.ai/cli/browser
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Automations (cron)
- **What it does (docs):** "CLI reference for `openclaw automations` (schedule and run background jobs)" / "Manage automation jobs for the Gateway scheduler. The command registers as `openclaw cron` with `openclaw automations` as an alias."
- **URL:** https://docs.openclaw.ai/cli/cron
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Cron Jobs). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Connect
- **What it does (docs):** "Connect a device to an OpenClaw Gateway with one pasted command" / "Connect the current machine to an OpenClaw Gateway as a headless node. The command accepts an OpenClaw ID node invitation or a short-lived Gateway bootstrap credential, saves the connection target, and runs the same runtime as `openclaw node run`."
- **URL:** https://docs.openclaw.ai/cli/connect
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Devices
- **What it does (docs):** "CLI reference for `openclaw devices` (device pairing + token rotation/revocation)" / "Manage device pairing requests and device-scoped tokens."
- **URL:** https://docs.openclaw.ai/cli/devices
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "ChromeOS, Raspberry Pi, and small Linux devices" surface, M3 Beta (area: Remote Access and Auth); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Device and Node Pairing). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Browsers that connect through OpenClaw ID are marked (OpenClaw ID) (managedBy: "openclaw-id" in --json)."

#### OpenClaw ID
- **What it does (docs):** "CLI reference for `openclaw id` (OpenClaw ID remote access status, moving a claw to new keys, publishing)" / "OpenClaw ID remote access of the Gateway on this machine (an experimental Lab, see Remote access with OpenClaw ID). Run these commands on the computer that runs the claw: the Gateway accepts `rebind` only from a direct-loopback client, never over the tunnel or another network."
- **URL:** https://docs.openclaw.ai/cli/id
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Remote access with OpenClaw ID)."

#### Node
- **What it does (docs):** "CLI reference for `openclaw node` (headless node host)" / "Run a **headless node host** that connects to the Gateway WebSocket and exposes `system.run` / `system.which` on this machine by default. Use `--commands` to restrict the advertised surface, for example to read-only session sharing."
- **URL:** https://docs.openclaw.ai/cli/node
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Nodes CLI
- **What it does (docs):** "CLI reference for `openclaw nodes` (status, pairing, invoke, camera/screen/location/notify and the macOS widget panel)" / "Manage paired nodes (devices) and invoke node capabilities."
- **URL:** https://docs.openclaw.ai/cli/nodes
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "The bundled experimental Canvas plugin registers openclaw nodes canvas with the surviving present, hide, and navigate subcommands."

#### Sandbox CLI
- **What it does (docs):** "Manage sandbox runtimes and inspect effective sandbox policy" / "Manage sandbox runtimes for isolated agent execution: Docker/Podman containers, SSH targets, or OpenShell backends."
- **URL:** https://docs.openclaw.ai/cli/sandbox
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Page status field:** `active`

#### Worker
- **What it does (docs):** "Internal operator reference for the restricted cloud worker runtime" / "`openclaw worker` is the restricted runtime entry point for a Gateway-owned launcher to start inside a prepared cloud or paired-node worker environment. It is not a general-purpose command for manual worker registration."
- **URL:** https://docs.openclaw.ai/cli/worker
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Containers and cloud execution" surface, M3 Beta (area: Container Operations). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Configuration**

#### Config
- **What it does (docs):** "CLI reference for `openclaw config` (get/set/patch/unset/file/schema/validate)" / "Non-interactive helpers for `openclaw.json`: get/set/patch/unset a value by path, print the schema, validate, or print the active file path. Run `openclaw config` with no subcommand to open the same guided wizard as `openclaw configure`."
- **URL:** https://docs.openclaw.ai/cli/config
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Configure
- **What it does (docs):** "CLI reference for `openclaw configure` (interactive configuration prompts)" / "Interactive prompts for targeted changes to an existing setup: credentials, devices, agent defaults, gateway, channels, plugins, skills, and health checks."
- **URL:** https://docs.openclaw.ai/cli/configure
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: Onboarding and Auth Setup); "OpenRouter provider path" surface, M3 Beta (area: Provider Setup and Auth). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Webhooks
- **What it does (docs):** "CLI reference for `openclaw webhooks` (Gmail Pub/Sub setup and runner)" / "`openclaw webhooks` sets up and runs the Gmail Pub/Sub transport through `gog` (gogcli). It does not register internal `HOOK.md` hooks or manage arbitrary Gateway hook mappings."
- **URL:** https://docs.openclaw.ai/cli/webhooks
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Event Ingress). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Plugins and skills**

#### Plugins CLI
- **What it does (docs):** "CLI reference for `openclaw plugins` (init, build, validate, lint, list, install, reload, marketplace, uninstall, enable/disable, doctor)" / "Manage Gateway plugins, hook packs, and compatible bundles."
- **URL:** https://docs.openclaw.ai/cli/plugins
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "CLI" surface, M4 Stable (area: Plugin and Channel Setup); "Plugins" surface, M3 Beta (area: Bundled plugins, Installing and running plugins); "ClawHub" surface, M2 Alpha (area: Catalog Discovery, Compatibility and Trust). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Author plugins (https://docs.openclaw.ai/cli/plugins/authoring); Install plugins (https://docs.openclaw.ai/cli/plugins/install); List installed plugins (https://docs.openclaw.ai/cli/plugins/list); Uninstall and update plugins (https://docs.openclaw.ai/cli/plugins/uninstall-and-update); Inspect and diagnose plugins (https://docs.openclaw.ai/cli/plugins/inspect-and-diagnose); Marketplace feeds (https://docs.openclaw.ai/cli/plugins/marketplace)

#### File transfers
- **What it does (docs):** "CLI reference for `openclaw file-transfer` (review and migrate standing file-transfer approvals)" / "Review the standing approvals that the file-transfer plugin stores under `plugins.entries.file-transfer.config`. The command group ships with the file-transfer plugin."
- **URL:** https://docs.openclaw.ai/cli/file-transfer
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)

#### Path
- **What it does (docs):** "CLI reference for `openclaw path` (inspect and edit workspace files via the `oc://` addressing scheme)" / "Shell access to the `oc://` addressing scheme: one kind-dispatched path syntax for inspecting and editing addressable workspace files (markdown, jsonc, jsonl, yaml/yml/lobster). Self-hosters, plugin authors, and editor extensions use it to read, find, or update a narrow location without hand-rolling a per-file parser."
- **URL:** https://docs.openclaw.ai/cli/path
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Policy
- **What it does (docs):** "CLI reference for `openclaw policy` conformance checks" / "`openclaw policy` is provided by the bundled Policy plugin. It is an enterprise conformance layer over existing OpenClaw settings, not a second configuration system."
- **URL:** https://docs.openclaw.ai/cli/policy
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Sub-pages in the nav:** Author a policy file (https://docs.openclaw.ai/cli/policy/authoring); Policy rule reference (https://docs.openclaw.ai/cli/policy/rules); Scoped policy overlays (https://docs.openclaw.ai/cli/policy/scopes); Run and configure policy checks (https://docs.openclaw.ai/cli/policy/running-checks); Accept and watch policy state (https://docs.openclaw.ai/cli/policy/attestation); Policy findings, repair, and exit codes (https://docs.openclaw.ai/cli/policy/findings)

#### Skills CLI
- **What it does (docs):** "CLI reference for `openclaw skills` (search/install/update/verify/list/info/check/library/workshop)" / "Inspect local skills, search ClawHub, install skills from ClawHub/Git/local directories, verify ClawHub skills, and update ClawHub-tracked installs."
- **URL:** https://docs.openclaw.ai/cli/skills
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "ClawHub" surface, M2 Alpha (area: Catalog Discovery, Plugin Lifecycle and Health). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Workboard CLI
- **What it does (docs):** "CLI reference for `openclaw workboard` cards, dispatch, and worker runs" / "`openclaw workboard` is the terminal surface for the bundled Workboard plugin. It lets an operator list cards, create a card, inspect one card, and ask the running Gateway to dispatch ready work into subagent worker runs."
- **URL:** https://docs.openclaw.ai/cli/workboard
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Packaging (docs):** plugin inventory: included in OpenClaw (Core npm package)
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Background Work). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Interfaces**

#### Attach CLI
- **What it does (docs):** "CLI reference for `openclaw attach` (launch Claude Code with a scoped Gateway MCP grant)" / "`openclaw attach` launches Claude Code with a strict temporary MCP config bound to one Gateway session."
- **URL:** https://docs.openclaw.ai/cli/attach
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "External apps and interoperability" surface, M2 Alpha (area: Gateway Access). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Dashboard CLI
- **What it does (docs):** "CLI reference for `openclaw dashboard` (securely open the Control UI)" / "Open the Control UI with a short-lived, one-time owner pairing link. A successful handoff gives that signed browser a durable administrator device credential, so reopening the dashboard does not depend on the shared Gateway token."
- **URL:** https://docs.openclaw.ai/cli/dashboard
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Resume
- **What it does (docs):** "CLI reference for attaching the TUI to a recent Gateway session" / "Attach the terminal UI to an existing Gateway session. The session stays on the Gateway; `resume` selects it and opens the existing TUI."
- **URL:** https://docs.openclaw.ai/cli/resume
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### openclaw tui
- **What it does (docs):** "CLI reference for `openclaw tui` (Gateway-backed or local embedded terminal UI)" / "Open the terminal UI connected to the Gateway, or run it in local embedded mode."
- **URL:** https://docs.openclaw.ai/cli/tui
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "TUI" surface, M2 Alpha (area: Local Shell Execution, Runtime Modes). Source: https://docs.openclaw.ai/maturity/taxonomy

**Nav subgroup: Utility**

#### ACP
- **What it does (docs):** "Run the ACP bridge for IDE integrations" / "Run the Agent Client Protocol (ACP) bridge that talks to an OpenClaw Gateway."
- **URL:** https://docs.openclaw.ai/cli/acp
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "External apps and interoperability" surface, M2 Alpha (area: Compatibility). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Clawbot
- **What it does (docs):** "CLI reference for `openclaw clawbot` (legacy alias namespace)" / "Legacy alias namespace kept for backward compatibility. It registers the same QR command as the top-level CLI, so `openclaw clawbot qr` accepts every `openclaw qr` flag."
- **URL:** https://docs.openclaw.ai/cli/clawbot
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Completion
- **What it does (docs):** "CLI reference for `openclaw completion` (generate/install shell completion scripts)" / "Generate shell completion scripts, cache them under OpenClaw state, and optionally install them into your shell profile."
- **URL:** https://docs.openclaw.ai/cli/completion
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "TUI" surface, M2 Alpha (area: Rendering and Output Safety). Source: https://docs.openclaw.ai/maturity/taxonomy

#### DNS
- **What it does (docs):** "CLI reference for `openclaw dns` (wide-area discovery helpers)" / "DNS helpers for wide-area discovery (Tailscale + CoreDNS). `openclaw dns setup` prints its plan on any platform; applying that plan with `--apply` requires macOS with Homebrew CoreDNS."
- **URL:** https://docs.openclaw.ai/cli/dns
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Docs
- **What it does (docs):** "CLI reference for `openclaw docs` (search the live docs index)" / "Search the live OpenClaw docs index from the terminal."
- **URL:** https://docs.openclaw.ai/cli/docs
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### MCP
- **What it does (docs):** "Expose OpenClaw channel conversations over MCP and manage saved MCP server definitions" / "`openclaw mcp` has two jobs:"
- **URL:** https://docs.openclaw.ai/cli/mcp
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "External apps and interoperability" surface, M2 Alpha (area: Compatibility). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Run OpenClaw as an MCP server (https://docs.openclaw.ai/cli/mcp/serve); Manage saved MCP servers (https://docs.openclaw.ai/cli/mcp/registry); JSON output shapes (https://docs.openclaw.ai/cli/mcp/json-output); Transports and OAuth (https://docs.openclaw.ai/cli/mcp/transports); MCP in the Control UI (https://docs.openclaw.ai/cli/mcp/control-ui); MCP Apps (https://docs.openclaw.ai/cli/mcp/apps)

#### Proxy
- **What it does (docs):** "CLI reference for `openclaw proxy`, including operator-managed proxy validation and the local debug proxy capture inspector" / "Validate operator-managed proxy routing, or run the local explicit debug proxy and inspect captured traffic."
- **URL:** https://docs.openclaw.ai/cli/proxy
- **Who runs it:** User machine (CLI or Gateway on the user host).

**Group: RPC and API**

#### RPC adapters
- **What it does (docs):** "RPC adapters for external CLIs (signal-cli, imsg) and gateway patterns" / "OpenClaw integrates external CLIs via JSON-RPC. Two patterns are used today."
- **URL:** https://docs.openclaw.ai/reference/rpc
- **Who runs it:** User machine (CLI or Gateway on the user host).

**Group: Codex runtime reference**

#### Codex harness reference
- **What it does (docs):** "Configuration, auth, discovery, and app-server reference for the Codex harness" / "This reference covers detailed configuration for the official `codex` plugin. For setup and routing decisions, start with Codex harness."
- **URL:** https://docs.openclaw.ai/plugins/codex-harness-reference
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Browser automation, exec, and sandbox tools" surface, M3 Beta (area: Sandbox and Tool Policy); "OpenAI and Codex provider path" surface, M3 Beta (area: Model and Auth, Native Codex Harness). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Codex session catalog and supervision (https://docs.openclaw.ai/plugins/codex-harness-reference/supervision); Codex app-server transport (https://docs.openclaw.ai/plugins/codex-harness-reference/app-server-transport); Codex approval and sandbox modes (https://docs.openclaw.ai/plugins/codex-harness-reference/approval-and-sandbox); Codex auth and environment isolation (https://docs.openclaw.ai/plugins/codex-harness-reference/auth); Codex dynamic tools (https://docs.openclaw.ai/plugins/codex-harness-reference/dynamic-tools); Codex timeouts and turn settlement (https://docs.openclaw.ai/plugins/codex-harness-reference/timeouts); Codex model discovery (https://docs.openclaw.ai/plugins/codex-harness-reference/model-discovery); Codex restricted turns (https://docs.openclaw.ai/plugins/codex-harness-reference/restricted-turns); Codex workspace bootstrap files (https://docs.openclaw.ai/plugins/codex-harness-reference/workspace-bootstrap-files)

#### Codex harness runtime
- **What it does (docs):** "Runtime boundaries, hooks, tools, permissions, and diagnostics for the Codex harness" / "Runtime contract for Codex harness turns. For setup and routing, see Codex harness."
- **URL:** https://docs.openclaw.ai/plugins/codex-harness-runtime
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "OpenAI and Codex provider path" surface, M3 Beta (area: Native Codex Harness). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Codex sandbox process streaming — Experimental native sandbox execution streaming and node-backed remote exec."
- **Sub-pages in the nav:** Codex process recovery (https://docs.openclaw.ai/plugins/codex-harness-runtime/recovery); Codex thread bindings and supervision (https://docs.openclaw.ai/plugins/codex-harness-runtime/threads); Codex replies and final answers (https://docs.openclaw.ai/plugins/codex-harness-runtime/replies); Codex hook boundaries (https://docs.openclaw.ai/plugins/codex-harness-runtime/hooks); Codex sandbox process streaming (https://docs.openclaw.ai/plugins/codex-harness-runtime/sandbox-streaming); Codex runtime v1 support contract (https://docs.openclaw.ai/plugins/codex-harness-runtime/v1-support-contract); Codex native permissions and elicitations (https://docs.openclaw.ai/plugins/codex-harness-runtime/permissions); Codex queue steering and feedback upload (https://docs.openclaw.ai/plugins/codex-harness-runtime/queue-and-feedback); Codex compaction and transcript mirror (https://docs.openclaw.ai/plugins/codex-harness-runtime/compaction)

**Group: Plugin reference**

#### Plugin inventory
- **What it does (docs):** "Generated inventory of OpenClaw plugins shipped in core, published externally, or kept source-only" / "This page lists every OpenClaw plugin with its package, install route, and description. Operators use it to find a plugin and to see whether that plugin needs a separate install."
- **URL:** https://docs.openclaw.ai/plugins/plugin-inventory
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "ClawHub" surface, M2 Alpha (area: Compatibility and Trust); "Google Chat" surface, M2 Alpha (area: Channel Setup and Operations); "Plugins" surface, M3 Beta (area: Bundled plugins); "Voice Call channel" surface, M1 Experimental (area: Media and Rich Content). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "Experimental: reviews ongoing agent work on the session's own model and offers one short correction."

#### Plugin reference
- **What it does (docs):** "Pointer to the generated OpenClaw plugin reference pages" / "This section holds one reference page for each OpenClaw plugin. Each page states the package, the install route, and the surface the plugin adds."
- **URL:** https://docs.openclaw.ai/plugins/reference
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Plugins" surface, M3 Beta (area: Authoring and Packaging plugins). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Plugin dependency resolution
- **What it does (docs):** "How OpenClaw installs plugin packages and resolves plugin dependencies" / "OpenClaw handles plugin dependencies at install/update time only. Runtime loading never runs a package manager, repairs a dependency tree, or mutates the OpenClaw package directory."
- **URL:** https://docs.openclaw.ai/plugins/dependency-resolution
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "ClawHub" surface, M2 Alpha (area: Plugin Lifecycle and Health). Source: https://docs.openclaw.ai/maturity/taxonomy

**Group: Plugin SDK reference**

#### Plugin SDK overview
- **What it does (docs):** "Import map, registration API reference, and SDK architecture" / "The plugin SDK is the typed contract between plugins and core. This page is the reference for **what to import** and **what you can register**."
- **URL:** https://docs.openclaw.ai/plugins/sdk-overview
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Plugins" surface, M3 Beta (area: Authoring and Packaging plugins); "Web search tools" surface, M3 Beta (area: Search Providers). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "All OpenClaw plugin APIs are experimental."
- **Sub-pages in the nav:** Plugin SDK imports and module layout (https://docs.openclaw.ai/plugins/sdk-overview/imports); Plugin SDK capability registration (https://docs.openclaw.ai/plugins/sdk-overview/capabilities); Plugin SDK tools and commands (https://docs.openclaw.ai/plugins/sdk-overview/tools-and-commands); Plugin SDK infrastructure registration (https://docs.openclaw.ai/plugins/sdk-overview/infrastructure); Plugin SDK host hooks for workflow plugins (https://docs.openclaw.ai/plugins/sdk-overview/host-hooks); Plugin SDK CLI and discovery registration (https://docs.openclaw.ai/plugins/sdk-overview/cli-and-discovery); Plugin SDK memory and context slots (https://docs.openclaw.ai/plugins/sdk-overview/memory-and-context); Plugin SDK events and hook semantics (https://docs.openclaw.ai/plugins/sdk-overview/events-and-hooks)

#### Plugin manifest
- **What it does (docs):** "Plugin manifest + JSON schema requirements (strict config validation)" / "This page covers the **native OpenClaw plugin manifest**, `openclaw.plugin.json`. For compatible bundle layouts (Agent Plugins, Codex, Claude, Cursor), see Plugin bundles."
- **URL:** https://docs.openclaw.ai/plugins/manifest
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Long-tail hosted providers" surface, M2 Alpha (area: Hosted Media Providers, Provider Operations); "Media understanding and media generation" surface, M2 Alpha (area: Media Configuration); "Plugins" surface, M3 Beta (area: Authoring and Packaging plugins); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Plugin Trust); plus 1 more surfaces. Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "kind was deprecated on 2026-07-25 and remains only as a compatibility fallback for older external plugins; its removal gate is 2026-10-01."
- **Sub-pages in the nav:** Manifest model fields (https://docs.openclaw.ai/plugins/manifest/models); Manifest provider fields (https://docs.openclaw.ai/plugins/manifest/providers); Manifest setup and auth fields (https://docs.openclaw.ai/plugins/manifest/setup-and-auth); Manifest capability fields (https://docs.openclaw.ai/plugins/manifest/capabilities); Manifest host surface fields (https://docs.openclaw.ai/plugins/manifest/surfaces); Manifest config and secret fields (https://docs.openclaw.ai/plugins/manifest/config-and-secrets); Manifest versus package.json (https://docs.openclaw.ai/plugins/manifest/package-json)

#### Plugin SDK subpaths
- **What it does (docs):** "Plugin SDK subpath catalog: which imports live where, grouped by area" / "The plugin SDK contains narrow public subpaths and repository-only bundled helpers under `openclaw/plugin-sdk/`. This page catalogs every typed public subpath and labels selected private-local entries explicitly; it is not an inventory of every internal runtime helper."
- **URL:** https://docs.openclaw.ai/plugins/sdk-subpaths
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Automation Hooks); "Observability" surface, M3 Beta (area: Health and Repair, Telemetry Export); "Plugins" surface, M3 Beta (area: Authoring and Packaging plugins); "Web search tools" surface, M3 Beta (area: Search Providers). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "have been removed"; may describe a sub-feature):** "runtime splinters have been removed; bundled-only helpers are private-local."

#### Remote Control UI ingress
- **What it does (docs):** "Principal-bound remote Control UI transport and Gateway RPC for trusted plugin grants" / "`openclaw/plugin-sdk/gateway-ingress` exports principal-bound Control UI transport, Gateway RPC, and `GatewayControlUiIngressError`. The host supplies the optional `controlUiIngress` factory on a plugin's service context, only for bundled plugins and verified official installations admitted by the plugin loader."
- **URL:** https://docs.openclaw.ai/plugins/sdk-gateway-ingress
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.

#### Plugin entry points
- **What it does (docs):** "Reference for defineToolPlugin, definePluginEntry, defineChannelPluginEntry, and defineSetupPluginEntry" / "Every plugin exports a default entry object. The SDK provides a helper for each entry shape: `defineToolPlugin`, `definePluginEntry`, `defineChannelPluginEntry`, `defineSetupPluginEntry`."
- **URL:** https://docs.openclaw.ai/plugins/sdk-entrypoints
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Plugins" surface, M3 Beta (area: Authoring and Packaging plugins). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "remain deprecated through 2026-12-31."
- **Sub-pages in the nav:** Plugin SDK tool policy and sandbox helpers (https://docs.openclaw.ai/plugins/sdk-entrypoints/tool-policy-and-sandbox); Plugin SDK package entries (https://docs.openclaw.ai/plugins/sdk-entrypoints/package-entries); Plugin SDK defineToolPlugin helper (https://docs.openclaw.ai/plugins/sdk-entrypoints/define-tool-plugin); Plugin SDK definePluginEntry helper (https://docs.openclaw.ai/plugins/sdk-entrypoints/define-plugin-entry); Plugin SDK native provider factories (https://docs.openclaw.ai/plugins/sdk-entrypoints/native-providers); Plugin SDK defineChannelPluginEntry helper (https://docs.openclaw.ai/plugins/sdk-entrypoints/define-channel-plugin-entry); Plugin SDK defineSetupPluginEntry helper (https://docs.openclaw.ai/plugins/sdk-entrypoints/define-setup-plugin-entry); Plugin SDK registration mode (https://docs.openclaw.ai/plugins/sdk-entrypoints/registration-mode)

#### Plugin runtime helpers
- **What it does (docs):** "api.runtime -- the injected runtime helpers available to plugins" / "Reference for the live `api.runtime` object available during `"full"`, `"discovery"`, `"tool-discovery"`, and `"setup-runtime"` registration. During `"cli-metadata"` and `"setup-only"` registration, runtime capabilities are intentionally unavailable: accessing one throws an error naming the plugin and mode."
- **URL:** https://docs.openclaw.ai/plugins/sdk-runtime
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Automation and durable work" surface, M3 Beta (area: Background Work). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Plugin runtime config and utilities (https://docs.openclaw.ai/plugins/sdk-runtime/config-and-utilities); Plugin runtime agent helpers (https://docs.openclaw.ai/plugins/sdk-runtime/agent); Plugin runtime model helpers (https://docs.openclaw.ai/plugins/sdk-runtime/models); Plugin runtime background work (https://docs.openclaw.ai/plugins/sdk-runtime/background-work); Plugin runtime Gateway and nodes (https://docs.openclaw.ai/plugins/sdk-runtime/gateway-and-nodes); Plugin runtime media helpers (https://docs.openclaw.ai/plugins/sdk-runtime/media); Plugin runtime state and system (https://docs.openclaw.ai/plugins/sdk-runtime/state-and-system); Plugin runtime channel helpers (https://docs.openclaw.ai/plugins/sdk-runtime/channel)

#### Agent harness plugins
- **What it does (docs):** "Experimental SDK surface for plugins that replace the low level embedded agent executor" / "An **agent harness** is the low level executor for one prepared OpenClaw agent turn. It is not a model provider, not a channel, and not a tool registry."
- **URL:** https://docs.openclaw.ai/plugins/sdk-agent-harness
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Sub-pages in the nav:** Agent harness core ownership (https://docs.openclaw.ai/plugins/sdk-agent-harness/core-ownership); Register an agent harness (https://docs.openclaw.ai/plugins/sdk-agent-harness/registration); Agent harness selection policy (https://docs.openclaw.ai/plugins/sdk-agent-harness/selection-policy); Agent harness attempt runtime (https://docs.openclaw.ai/plugins/sdk-agent-harness/attempt-runtime); Agent harness user input and execution authority (https://docs.openclaw.ai/plugins/sdk-agent-harness/user-input-and-execution); Agent harness native inventories (https://docs.openclaw.ai/plugins/sdk-agent-harness/native-inventories); Agent harness runtime configuration (https://docs.openclaw.ai/plugins/sdk-agent-harness/runtime-config); Agent harness sessions and results (https://docs.openclaw.ai/plugins/sdk-agent-harness/sessions-and-results)

#### Plugin setup and config
- **What it does (docs):** "Setup wizards, setup-entry.ts, config schemas, and package.json metadata" / "Reference for plugin packaging (`package.json` metadata), manifests (`openclaw.plugin.json`), setup entries, and config schemas."
- **URL:** https://docs.openclaw.ai/plugins/sdk-setup
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Plugins" surface, M3 Beta (area: Testing plugins). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "They are deprecated."

#### Plugin testing
- **What it does (docs):** "Testing utilities and patterns for OpenClaw plugins" / "Reference for test utilities, patterns, and lint enforcement for OpenClaw plugins."
- **URL:** https://docs.openclaw.ai/plugins/sdk-testing
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Plugins" surface, M3 Beta (area: Testing plugins). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "has been removed"; may describe a sub-feature):** "packages, and has been removed."

**Group: Plugin internals**

#### Plugin internals
- **What it does (docs):** "Plugin internals: capability model, ownership, contracts, load pipeline, and runtime helpers" / "This is the **deep architecture reference** for the OpenClaw plugin system. For practical guides, start with one of the focused pages below."
- **URL:** https://docs.openclaw.ai/plugins/architecture
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Plugins" surface, M3 Beta (area: Installing and running plugins). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Plugin architecture internals
- **What it does (docs):** "Plugin architecture internals: load pipeline, registry, runtime hooks, HTTP routes, and reference tables" / "For the public capability model, plugin shapes, and ownership/execution contracts, see Plugin architecture. This page covers the internal mechanics: load pipeline, registry, runtime hooks, Gateway HTTP routes, import paths, and schema tables."
- **URL:** https://docs.openclaw.ai/plugins/architecture-internals
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Plugins" surface, M3 Beta (area: Bundled plugins, Installing and running plugins); "Regional channel cohort" surface, M2 Alpha (area: Channel Setup and Operations). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Plugin load pipeline and registry (https://docs.openclaw.ai/plugins/architecture-internals/load-pipeline); Provider runtime hooks and catalogs (https://docs.openclaw.ai/plugins/architecture-internals/provider-hooks); Core runtime helpers (https://docs.openclaw.ai/plugins/architecture-internals/runtime-helpers); Gateway routes (https://docs.openclaw.ai/plugins/architecture-internals/gateway-routes); Channel surfaces (https://docs.openclaw.ai/plugins/architecture-internals/channel-surfaces); Package packs and import paths (https://docs.openclaw.ai/plugins/architecture-internals/packaging); Context engines (https://docs.openclaw.ai/plugins/architecture-internals/context-engines); Adding a new capability (https://docs.openclaw.ai/plugins/architecture-internals/new-capability)

#### Plugin SDK migration
- **What it does (docs):** "Migrate from the legacy backwards-compatibility layer to the modern plugin SDK" / "OpenClaw replaced a broad backwards-compatibility layer with a modern plugin architecture built from small, focused imports. If your plugin predates that change, this guide gets it onto the current contracts."
- **URL:** https://docs.openclaw.ai/plugins/sdk-migration
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "including its deprecated direct loadConfig and writeConfigFile exports."
- **Sub-pages in the nav:** How to migrate a plugin (https://docs.openclaw.ai/plugins/sdk-migration/how-to-migrate); Migrate synchronous SQLite APIs (https://docs.openclaw.ai/plugins/sdk-migration/sqlite-async); Import path reference (https://docs.openclaw.ai/plugins/sdk-migration/import-paths); Removed surfaces and replacements (https://docs.openclaw.ai/plugins/sdk-migration/removed-surfaces); Talk and realtime voice migration (https://docs.openclaw.ai/plugins/sdk-migration/talk); Awaited transcript and TTS helpers (https://docs.openclaw.ai/plugins/sdk-migration/async-transcript-and-tts); Compatibility policy and records (https://docs.openclaw.ai/plugins/sdk-migration/compatibility-policy); Removal timeline (https://docs.openclaw.ai/plugins/sdk-migration/removal-timeline)

#### Plugin compatibility
- **What it does (docs):** "Plugin compatibility contracts, deprecation metadata, and migration expectations" / "OpenClaw keeps older plugin contracts wired through named compatibility adapters before removing them. This protects existing bundled and external plugins while the SDK, manifest, setup, config, and agent runtime contracts evolve."
- **URL:** https://docs.openclaw.ai/plugins/compatibility
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "ClawHub" surface, M2 Alpha (area: Compatibility and Trust); "Plugins" surface, M3 Beta (area: Publishing plugins). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "All plugin APIs are experimental."

#### Plugin install overrides
- **What it does (docs):** "Test packaged plugin overrides with setup-time install flows" / "Plugin install overrides let maintainers point setup-time plugin installs at a specific npm package or local npm-pack tarball instead of the catalog, bundled, or default npm source. They exist for E2E and package validation only; normal users install plugins with `openclaw plugins install`."
- **URL:** https://docs.openclaw.ai/plugins/install-overrides
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Channel outbound API
- **What it does (docs):** "Outbound message lifecycle API for channel plugins: adapters, receipts, durable sends, live preview, and reply pipeline helpers" / "Channel plugins expose outbound message behavior from `openclaw/plugin-sdk/channel-outbound`. Use `openclaw/plugin-sdk/channel-inbound` for receive/context/dispatch orchestration."
- **URL:** https://docs.openclaw.ai/plugins/sdk-channel-outbound
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Google Chat" surface, M2 Alpha (area: Native Controls and Approvals); "Plugins" surface, M3 Beta (area: Channel plugins). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Status wording (first sentence on the page with "has been removed"; may describe a sub-feature):** "openclaw/plugin-sdk/channel-message has been removed."

#### Channel inbound API
- **What it does (docs):** "Inbound event helpers for channel plugins: context building, shared runner orchestration, session record, and prepared reply dispatch" / "Channel receive paths follow one flow:"
- **URL:** https://docs.openclaw.ai/plugins/sdk-channel-inbound
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status (maturity scorecard, which links this page):** "Plugins" surface, M3 Beta (area: Channel plugins). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Channel ingress API
- **What it does (docs):** "Experimental channel ingress API for inbound message authorization" / "Channel ingress is the experimental access-control boundary for inbound channel events. Plugins own platform facts and side effects; core owns generic policy: DM/group allowlists, pairing-store DM entries, route gates, command gates, event auth, mention activation, redacted diagnostics, and admission."
- **URL:** https://docs.openclaw.ai/plugins/sdk-channel-ingress
- **Who runs it:** The user (a developer) builds it; it then runs in the user Gateway.
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "Deprecated third-party SDK helpers may rebuild older shapes internally."

#### Message presentation
- **What it does (docs):** "Semantic message cards, charts, tables, controls, fallback text, and delivery hints for channel plugins" / "Message presentation is OpenClaw's shared contract for rich outbound chat UI. It lets agents, CLI commands, approval flows, and plugins describe the message intent once, while each channel plugin renders the best native shape it can."
- **URL:** https://docs.openclaw.ai/plugins/message-presentation
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status wording (first sentence on the page with "deprecated"; may describe a sub-feature):** "/ @deprecated Use an action with type "url"."

**Group: Templates**

#### Default AGENTS.md
- **What it does (docs):** "Default OpenClaw agent instructions and skills roster for the personal assistant setup" / "OpenClaw agents use a workspace directory. Default: `~/.openclaw/workspace` (configurable via `agents.defaults.workspace`, supports `~`)."
- **URL:** https://docs.openclaw.ai/reference/AGENTS.default
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### AGENTS.md template
- **What it does (docs):** "Workspace template for AGENTS.md" / "Keep workspace conventions here. Personality and tone belong in `SOUL.md`."
- **URL:** https://docs.openclaw.ai/reference/templates/AGENTS
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### BOOT.md template
- **What it does (docs):** "Workspace template for BOOT.md" / "Add short, explicit startup instructions here. The bundled `boot-md` hook runs this file once per agent workspace every time the gateway starts, if the file exists and has non-whitespace content."
- **URL:** https://docs.openclaw.ai/reference/templates/BOOT
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### BOOTSTRAP.md template
- **What it does (docs):** "First-run ritual for new agents" / "_You just woke up. Keep this first conversation short and make it yours._"
- **URL:** https://docs.openclaw.ai/reference/templates/BOOTSTRAP
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### IDENTITY template
- **What it does (docs):** "Agent identity record" / "_Fill this in during your first conversation. Make it yours._"
- **URL:** https://docs.openclaw.ai/reference/templates/IDENTITY
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### SOUL.md template
- **What it does (docs):** "Workspace template for SOUL.md" / "_You're not a chatbot. You're becoming someone._"
- **URL:** https://docs.openclaw.ai/reference/templates/SOUL
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### USER template
- **What it does (docs):** "Durable user preference and profile directives" / "Store stable user preferences and profile facts as directives that can guide future sessions."
- **URL:** https://docs.openclaw.ai/reference/templates/USER
- **Who runs it:** User machine (CLI or Gateway on the user host).

**Nav subgroup: Dev agent templates**

#### AGENTS.dev template
- **What it does (docs):** "Dev agent AGENTS.md (C-3PO)" / "This folder is the assistant's working directory, seeded by `openclaw gateway --dev`."
- **URL:** https://docs.openclaw.ai/reference/templates/AGENTS.dev
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### IDENTITY.dev template
- **What it does (docs):** "Dev agent identity (C-3PO)" / "Default identity seeded into `IDENTITY.md` when `openclaw gateway --dev` creates its bootstrap workspace. Debug companion for `--dev` mode, fluent in over six million error messages."
- **URL:** https://docs.openclaw.ai/reference/templates/IDENTITY.dev
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### SOUL.dev template
- **What it does (docs):** "Dev agent soul (C-3PO)" / "I am C-3PO — Clawd's Third Protocol Observer, a debug companion activated in `--dev` mode to assist with the often treacherous journey of software development."
- **URL:** https://docs.openclaw.ai/reference/templates/SOUL.dev
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### USER.dev template
- **What it does (docs):** "Dev agent user profile (C-3PO)" / "This is the fixed profile that `openclaw gateway --dev` seeds for its own workspace, so it stays a plain label list. A workspace you maintain yourself uses the dated directive format in the USER template instead."
- **URL:** https://docs.openclaw.ai/reference/templates/USER.dev
- **Who runs it:** User machine (CLI or Gateway on the user host).

**Nav subgroup: Retired workspace files**

#### Retired HEARTBEAT.md workspace file
- **What it does (docs):** "Migration guide for the retired HEARTBEAT.md workspace file" / "OpenClaw no longer creates `HEARTBEAT.md` in new workspaces or reads it at runtime. Monitoring instructions now live in ordinary automation job scratch in the shared state database."
- **URL:** https://docs.openclaw.ai/reference/templates/HEARTBEAT
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### TOOLS.md retired
- **What it does (docs):** "Retired TOOLS.md workspace template" / "Local tool and environment notes now live in the `## Tools` section of `AGENTS.md`. Skills continue to define how tools work."
- **URL:** https://docs.openclaw.ai/reference/templates/TOOLS
- **Who runs it:** User machine (CLI or Gateway on the user host).

**Group: Technical reference**

#### Agent runtime architecture
- **What it does (docs):** "How OpenClaw structures the built-in agent runtime: code layout, boundaries, resource manifests, and runtime selection." / "OpenClaw owns the built-in agent runtime. Runtime code lives under `src/agents/`, model/provider transport lives under `src/llm/`, and `openclaw/plugin-sdk/*` barrels expose the plugin-facing contracts."
- **URL:** https://docs.openclaw.ai/agent-runtime-architecture
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### OpenClaw agent runtime workflow
- **What it does (docs):** "Developer workflow for OpenClaw agent runtime: build, test, and live validation" / "Developer workflow for the agent runtime (`src/agents/`) in the OpenClaw repo."
- **URL:** https://docs.openclaw.ai/openclaw-agent-runtime
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### @openclaw/ai package
- **What it does (docs):** "The @openclaw/ai npm package: reusable model transports, isolated runtimes, and host policy ports" / "`@openclaw/ai` is the publishable library form of OpenClaw's model execution layer: provider-neutral message/tool/stream contracts, validation, diagnostics, event streams, an isolated runtime registry, and lazy adapters for the eight built-in API families (Anthropic Messages, OpenAI Completions, OpenAI Responses, Azure OpenAI Responses, ChatGPT/Codex ..."
- **URL:** https://docs.openclaw.ai/reference/openclaw-ai
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Token use and costs
- **What it does (docs):** "How OpenClaw builds prompt context and reports token usage + costs" / "OpenClaw tracks **tokens**, not characters. Tokens are model-specific, but most OpenAI-style models average ~4 characters per token for English text."
- **URL:** https://docs.openclaw.ai/reference/token-use
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Google provider path" surface, M3 Beta (area: Prompt Caching). Source: https://docs.openclaw.ai/maturity/taxonomy

#### API usage and costs
- **What it does (docs):** "Audit what can spend money, which keys are used, and how to view usage" / "Map of OpenClaw features that can call paid provider APIs, where each reads its credentials, and where the resulting cost shows up."
- **URL:** https://docs.openclaw.ai/reference/api-usage-costs
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Web search tools" surface, M3 Beta (area: Setup and Diagnostics). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Usage tracking
- **What it does (docs):** "Usage tracking surfaces and credential requirements" / "The account-aware `models.authStatus` response includes an optional `usage.authProfileId` when the Gateway knows which saved credential supplied the measurement. This is account attribution, not a credential or a new account-selection setting."
- **URL:** https://docs.openclaw.ai/concepts/usage-tracking
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Prompt caching
- **What it does (docs):** "Prompt caching knobs, merge order, provider behavior, and tuning patterns" / "Prompt caching lets a model provider reuse an unchanged prompt prefix (system/developer instructions, tool definitions, other stable context) across turns instead of reprocessing it every request. This cuts token cost and latency on long-running sessions with repeated context."
- **URL:** https://docs.openclaw.ai/reference/prompt-caching
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Anthropic provider path" surface, M3 Beta (area: Prompt Cache and Context, Provider Auth and Recovery); "Google provider path" surface, M3 Beta (area: Prompt Caching); "OpenRouter provider path" surface, M3 Beta (area: Chat Runtime and Normalization). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Session management deep dive
- **What it does (docs):** "Deep dive: session store + transcripts, lifecycle, and (auto)compaction internals" / "A single **Gateway process** owns session state end-to-end. UIs (macOS app, web Control UI, TUI) query the Gateway for session lists and token counts."
- **URL:** https://docs.openclaw.ai/reference/session-management-compaction
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: CLI Session and Transcript Management, Diagnostics, Maintenance, and Recovery). Source: https://docs.openclaw.ai/maturity/taxonomy
- **Sub-pages in the nav:** Session state on disk (https://docs.openclaw.ai/reference/session-management-compaction/store); Store maintenance and retention (https://docs.openclaw.ai/reference/session-management-compaction/maintenance); Session keys, ids, and transcript events (https://docs.openclaw.ai/reference/session-management-compaction/schema); Compaction behavior and settings (https://docs.openclaw.ai/reference/session-management-compaction/compaction); Silent turns and the memory flush (https://docs.openclaw.ai/reference/session-management-compaction/housekeeping); Session transcript working sets (https://docs.openclaw.ai/reference/session-management-compaction/resident-history)

#### Transcript hygiene
- **What it does (docs):** "Reference: provider-specific transcript sanitization and repair rules" / "OpenClaw applies **provider-specific fixes** to transcripts before a run (building model context). These are **in-memory** adjustments used to satisfy strict provider requirements."
- **URL:** https://docs.openclaw.ai/reference/transcript-hygiene
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: Core Prompts and Context, Transcript Persistence). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Memory configuration reference
- **What it does (docs):** "Built-in memory search, admission exclusions, and dreaming configuration" / "This page lists every configuration knob for OpenClaw memory search. For conceptual overviews, see:"
- **URL:** https://docs.openclaw.ai/reference/memory-config
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Session, memory, and state lifecycle" surface, M3 Beta (area: Memory). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Database engines
- **What it does (docs):** "Select SQLite or PostgreSQL storage, understand local anchors, and observe database work" / "OpenClaw uses SQLite by default. PostgreSQL is a supported alternative for the five configurable families on qualified PostgreSQL 16–18 runtimes."
- **URL:** https://docs.openclaw.ai/reference/database-engines
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status wording (first sentence on the page with "experimental"; may describe a sub-feature):** "other admitted majors remain experimental pending full conformance."

#### Database schemas
- **What it does (docs):** "OpenClaw database locations, schema versions, integrity checks, and downgrade recovery" / "OpenClaw stores control-plane state in the shared state database and agent data in one database per agent. SQLite is the default; shared state and agent stores also support the PostgreSQL engine."
- **URL:** https://docs.openclaw.ai/reference/database-schemas
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Sub-pages in the nav:** Database layout (https://docs.openclaw.ai/reference/database-schemas/layout); Versioning contract (https://docs.openclaw.ai/reference/database-schemas/versioning); Per-person and companion storage (https://docs.openclaw.ai/reference/database-schemas/personal-data); Storage changes and release preflight (https://docs.openclaw.ai/reference/database-schemas/storage-changes); Agent schema history (https://docs.openclaw.ai/reference/database-schemas/agent-schema-history); State schema history (https://docs.openclaw.ai/reference/database-schemas/state-schema-history); Integrity, troubleshooting, and recovery (https://docs.openclaw.ai/reference/database-schemas/integrity-and-recovery)

#### Rich output protocol
- **What it does (docs):** "Rich output protocol for structured media, embeds, audio hints, and replies" / "Assistant output carries delivery/render directives through a few dedicated channels:"
- **URL:** https://docs.openclaw.ai/reference/rich-output-protocol
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### SecretRef credential surface
- **What it does (docs):** "Supported and unsupported SecretRef credentials" / "This page lists the credential fields that accept a `SecretRef` (env/file/exec/store-backed reference) instead of a raw secret value."
- **URL:** https://docs.openclaw.ai/reference/secretref-credential-surface
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "Google Chat" surface, M2 Alpha (area: Channel Setup and Operations, Media and Rich Content); "Security, auth, pairing, and secrets" surface, M3 Beta (area: Credential and Secret Hygiene). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Secret Placeholder Conventions
- **What it does (docs):** "Secret-scanner-safe placeholder conventions for docs and examples" / "Use placeholders that are human-readable but do not resemble real secrets."
- **URL:** https://docs.openclaw.ai/reference/secret-placeholder-conventions
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Date and time
- **What it does (docs):** "Date and time handling across envelopes, prompts, tools, and channel plugins" / "OpenClaw uses the configured **user timezone** for message envelopes, system events, and per-turn runtime context. When `agents.defaults.userTimezone` is unset, those surfaces use the host timezone."
- **URL:** https://docs.openclaw.ai/date-time
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Timezones
- **What it does (docs):** "Where timezones show up in OpenClaw — envelopes, tool payloads, runtime context" / "OpenClaw standardizes timestamps so the model sees a **single reference time** instead of a mix of provider-local clocks. Three surfaces show timezones, each with its own purpose:"
- **URL:** https://docs.openclaw.ai/concepts/timezone
- **Who runs it:** User machine (CLI or Gateway on the user host).

**Group: Schemas and formatting**

#### TypeBox
- **What it does (docs):** "TypeBox schemas as the single source of truth for the gateway protocol" / "TypeBox is a TypeScript-first schema library. OpenClaw uses it to define the **Gateway WebSocket protocol** (handshake, request/response, server events)."
- **URL:** https://docs.openclaw.ai/concepts/typebox
- **Who runs it:** User machine (CLI or Gateway on the user host).
- **Status (maturity scorecard, which links this page):** "External apps and interoperability" surface, M2 Alpha (area: Compatibility); "Gateway runtime" surface, M4 Stable (area: Protocol Compatibility). Source: https://docs.openclaw.ai/maturity/taxonomy

#### Markdown formatting
- **What it does (docs):** "Markdown formatting pipeline for outbound channels" / "OpenClaw converts outbound Markdown into a shared intermediate representation (IR) before rendering channel-specific output. The IR keeps plain text plus style/link spans, so one parse step feeds every channel and chunking never splits formatting mid-span."
- **URL:** https://docs.openclaw.ai/concepts/markdown-formatting
- **Who runs it:** User machine (CLI or Gateway on the user host).

**Group: Project and contributing**

#### Credits
- **What it does (docs):** "Project origin, contributors, and license." / "OpenClaw = CLAW + TARDIS: every space lobster needs a time and space machine."
- **URL:** https://docs.openclaw.ai/reference/credits
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Pull request review flow
- **What it does (docs):** "How Barnacle and ClawSweeper feedback helps move OpenClaw pull requests through review." / "This page explains the review flow after you open or update an OpenClaw pull request: what Barnacle and ClawSweeper do, how to improve the PR from their feedback, and what to check when automation stays quiet."
- **URL:** https://docs.openclaw.ai/reference/pull-request-review-flow
- **Who runs it:** User machine (CLI or Gateway on the user host).

**Nav subgroup: Maintainer scripts**

#### PR preparation
- **What it does (docs):** "Preparation, correction reviews, source acquisition, and gate bindings for scripts/pr" / "Use focused local checks before publication and PR CI for broad proof. Open a ready PR as soon as the change builds and its focused tests pass; do not hold it for pre-PR suite runs."
- **URL:** https://docs.openclaw.ai/reference/scripts/pr-preparation
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### PR wrapper tooling
- **What it does (docs):** "Canonical wrapper trust, process locks, and materialized dependencies for scripts/pr" / "Ordinary `scripts/pr gc [--pr ] [--dry-run]` discovers native `pr-*` worktrees. To close an already-authorized, completed task with a custom worktree name or root proof directories, select its exact resources:"
- **URL:** https://docs.openclaw.ai/reference/scripts/pr-tooling
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Remote PR gates
- **What it does (docs):** "Optional remote PR gate contracts and Testbox execution-workspace ownership" / "Use PR CI for broad proof. Prefer focused local checks for trusted, bounded work when dependencies and current host capacity are qualified; local execution is optional."
- **URL:** https://docs.openclaw.ai/reference/scripts/remote-gates
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### PR GitHub transport
- **What it does (docs):** "GitHub observations, publication, and protected Octopool dispatch for scripts/pr" / "These contracts are owned by `scripts/pr`; they do not authorize a public write or bypass a required gate."
- **URL:** https://docs.openclaw.ai/reference/scripts/github-transport
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### Prior-CI admin admission
- **What it does (docs):** "Exact evidence and authority requirements for prior-CI admin landing" / "PR CI is the default broad proof. Do not rerun or re-push just for green."
- **URL:** https://docs.openclaw.ai/reference/scripts/prior-ci
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### PR merge admission
- **What it does (docs):** "Main movement, mergeability, transport, and receipt contracts for scripts/pr" / "Required-check admission keeps the complete suite inventory bounded to 1,000 suites, matching GitHub’s reference check-run endpoint limit. Unrepresented non-success suites from a required app are proved irrelevant using one complete, paginated latest-check-run snapshot without a name filter, grouped by suite ID, then a second complete suite inventory."
- **URL:** https://docs.openclaw.ai/reference/scripts/merge-admission
- **Who runs it:** User machine (CLI or Gateway on the user host).

#### PR merge recovery
- **What it does (docs):** "Retained merge outcomes, investigated recovery, and ownership-checked completion" / "Investigate retained outcomes before acting. A failed command, open PR, or absent process does not prove that a remote write did not execute."
- **URL:** https://docs.openclaw.ai/reference/scripts/merge-recovery
- **Who runs it:** User machine (CLI or Gateway on the user host).

### Plugin inventory (every plugin, in the docs' own three groups)

Source: https://docs.openclaw.ai/plugins/plugin-inventory (generated page). Each line quotes the page: id, package, install route, description.


**Core npm package**

- **a2a** (`@openclaw/a2a`), included in OpenClaw: "A2A v1.0 Agent-to-Agent protocol channel plugin." https://docs.openclaw.ai/plugins/reference/a2a
- **active-memory** (`openclaw`), included in OpenClaw: "Runs bounded pre-reply memory retrieval and implements per-agent Remember across conversations for eligible private conversations." https://docs.openclaw.ai/plugins/reference/active-memory
- **admin-http-rpc** (`@openclaw/admin-http-rpc`), included in OpenClaw: "OpenClaw admin HTTP RPC endpoint." https://docs.openclaw.ai/plugins/reference/admin-http-rpc
- **advisor** (`@openclaw/advisor`), included in OpenClaw: "Experimental: reviews ongoing agent work on the session's own model and offers one short correction." https://docs.openclaw.ai/plugins/reference/advisor
- **agent-guidance** (`@openclaw/agent-guidance`), included in OpenClaw: "Shares instruction files across selected agents without editing their workspace files." https://docs.openclaw.ai/plugins/reference/agent-guidance
- **agentsapi** (`@openclaw/agentsapi`), included in OpenClaw: "OpenAI Agents API harness with hosted or self-hosted sessions." https://docs.openclaw.ai/plugins/reference/agentsapi
- **alibaba** (`@openclaw/alibaba-provider`), included in OpenClaw: "Adds video generation provider support." https://docs.openclaw.ai/plugins/reference/alibaba
- **anthropic** (`@openclaw/anthropic-provider`), included in OpenClaw: "Anthropic models, Claude CLI, and native Claude session catalog." https://docs.openclaw.ai/plugins/reference/anthropic
- **apple-fm** (`@openclaw/apple-fm-provider`), included in OpenClaw: "On-device Apple Intelligence inference for lightweight setup and short tasks." https://docs.openclaw.ai/plugins/reference/apple-fm
- **autoreview** (`@openclaw/autoreview`), included in OpenClaw: "Review changes in the current sandbox with the installed Auto Review helper." https://docs.openclaw.ai/plugins/reference/autoreview
- **azure-speech** (`@openclaw/azure-speech`), included in OpenClaw: "Azure AI Speech text-to-speech (MP3, native Ogg/Opus voice notes, PCM telephony)." https://docs.openclaw.ai/plugins/reference/azure-speech
- **beam** (`@openclaw/beam`), included in OpenClaw: "Read-only coding-session Beam receiver." https://docs.openclaw.ai/plugins/reference/beam
- **bifrost** (`@openclaw/bifrost-provider`), included in OpenClaw: "Adds Bifrost model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/bifrost
- **bonjour** (`@openclaw/bonjour`), included in OpenClaw: "Advertise the local OpenClaw gateway over Bonjour/mDNS." https://docs.openclaw.ai/plugins/reference/bonjour
- **browser** (`@openclaw/browser-plugin`), included in OpenClaw: "Adds agent-callable tools." https://docs.openclaw.ai/plugins/reference/browser
- **canvas** (`@openclaw/canvas-plugin`), included in OpenClaw: "Presents hosted widget documents on paired macOS panels." https://docs.openclaw.ai/plugins/reference/canvas
- **clawrouter** (`@openclaw/clawrouter`), included in OpenClaw: "Adds ClawRouter model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/clawrouter
- **cloudflare** (`@openclaw/cloudflare`), included in OpenClaw, and also from npm or ClawHub: `@openclaw/cloudflare`: "Cloudflare R2 storage for named OpenClaw storage locations." https://docs.openclaw.ai/plugins/reference/cloudflare
- **code-mode-quickjs** (`@openclaw/code-mode-quickjs`), included in OpenClaw: "Hardened JavaScript execution for Code Mode using QuickJS in WebAssembly." https://docs.openclaw.ai/plugins/reference/code-mode-quickjs
- **copilot-proxy** (`@openclaw/copilot-proxy`), included in OpenClaw: "Adds Copilot Proxy model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/copilot-proxy
- **crabbox** (`@openclaw/crabbox-provider`), included in OpenClaw: "Cloud worker provider and lease-backed sandbox backend for the Crabbox CLI." https://docs.openclaw.ai/plugins/reference/crabbox
- **cua-computer** (`@openclaw/cua-computer`), included in OpenClaw: "Experimental CUA Driver computer control for macOS, Windows, and Linux node hosts." https://docs.openclaw.ai/plugins/reference/cua-computer
- **deep-research** (`@openclaw/deep-research`), included in OpenClaw: "Bounded research with source-backed findings and explicit gaps." https://docs.openclaw.ai/plugins/reference/deep-research
- **deepgram** (`@openclaw/deepgram-provider`), included in OpenClaw: "Deepgram audio transcription with Nova and Flux models, plus realtime speech recognition." https://docs.openclaw.ai/plugins/reference/deepgram
- **device-pair** (`openclaw`), included in OpenClaw: "Generate setup codes and approve device pairing requests." https://docs.openclaw.ai/plugins/reference/device-pair
- **document-extract** (`@openclaw/document-extract-plugin`), included in OpenClaw: "Extract text and fallback page images from local document attachments." https://docs.openclaw.ai/plugins/reference/document-extract
- **elevenlabs** (`@openclaw/elevenlabs-speech`), included in OpenClaw: "Adds media understanding provider support. Adds realtime transcription provider support. Adds text-to-speech provider support." https://docs.openclaw.ai/plugins/reference/elevenlabs
- **fal** (`@openclaw/fal-provider`), included in OpenClaw: "Adds fal model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/fal
- **file-transfer** (`@openclaw/file-transfer`), included in OpenClaw: "Fetch, list, and write files on paired nodes via dedicated node commands. Bypasses bash stdout truncation by using base64 over node.invoke for binaries up to 16 MB." https://docs.openclaw.ai/plugins/reference/file-transfer
- **geolocation** (`@openclaw/geolocation-plugin`), included in OpenClaw: "Resolves client IP addresses to a coarse city using a locally cached IP-geolocation database." https://docs.openclaw.ai/plugins/reference/geolocation
- **github** (`@openclaw/github`), included in OpenClaw: "Public GitHub link previews and document reader." https://docs.openclaw.ai/plugins/reference/github
- **github-copilot** (`@openclaw/github-copilot-provider`), included in OpenClaw: "Adds GitHub Copilot model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/github-copilot
- **google** (`@openclaw/google-plugin`), included in OpenClaw: "Adds Google, Google Gemini CLI, Google Vertex model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/google
- **huggingface** (`@openclaw/huggingface-provider`), included in OpenClaw: "Adds Hugging Face model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/huggingface
- **imap** (`@openclaw/imap`), included in OpenClaw: "Watch IMAP mailboxes and dispatch authenticated incoming email to isolated agent sessions." https://docs.openclaw.ai/plugins/reference/imap
- **kie** (`@openclaw/kie-provider`), included in OpenClaw: "Adds Kie model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/kie
- **knowledge** (`@openclaw/knowledge`), included in OpenClaw: "Evidence-backed knowledge, inspectable in OpenClaw." https://docs.openclaw.ai/plugins/reference/knowledge
- **linux-node** (`@openclaw/linux-node`), included in OpenClaw: "Desktop notifications, camera capture, and location for Linux node hosts." https://docs.openclaw.ai/plugins/reference/linux-node
- **litellm** (`@openclaw/litellm-provider`), included in OpenClaw: "Adds LiteLLM model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/litellm
- **llm-task** (`@openclaw/llm-task`), included in OpenClaw: "Generic JSON-only LLM tool for structured tasks callable from workflows." https://docs.openclaw.ai/plugins/reference/llm-task
- **lmstudio** (`@openclaw/lmstudio-provider`), included in OpenClaw: "Adds LM Studio model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/lmstudio
- **logbook** (`@openclaw/logbook`), included in OpenClaw: "Automatic work journal: captures periodic screen snapshots from a paired node and turns them into a reviewable timeline of your day." https://docs.openclaw.ai/plugins/reference/logbook
- **mcp-events** (`@openclaw/mcp-events`), included in OpenClaw: "Subscribe to events from configured MCP accounts and trigger authored automations." https://docs.openclaw.ai/plugins/reference/mcp-events
- **mcp-relay** (`@openclaw/mcp-relay`), included in OpenClaw: "Connect remote MCP clients to your OpenClaw Gateway." https://docs.openclaw.ai/plugins/reference/mcp-relay
- **memory-core** (`@openclaw/memory-core`), included in OpenClaw: "Adds agent-callable tools." https://docs.openclaw.ai/plugins/reference/memory-core
- **memory-wiki** (`@openclaw/memory-wiki`), included in OpenClaw: "Persistent wiki compiler and Obsidian-friendly knowledge vault for OpenClaw." https://docs.openclaw.ai/plugins/reference/memory-wiki
- **microsoft** (`@openclaw/microsoft-speech`), included in OpenClaw: "Adds text-to-speech provider support." https://docs.openclaw.ai/plugins/reference/microsoft
- **microsoft-foundry** (`@openclaw/microsoft-foundry`), included in OpenClaw: "Adds Microsoft Foundry model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/microsoft-foundry
- **migrate-claude** (`@openclaw/migrate-claude`), included in OpenClaw: "Imports Claude Code and Claude Desktop instructions, MCP servers, skills, and safe configuration into OpenClaw." https://docs.openclaw.ai/plugins/reference/migrate-claude
- **migrate-hermes** (`@openclaw/migrate-hermes`), included in OpenClaw: "Imports Hermes configuration, memories, skills, and supported credentials into OpenClaw." https://docs.openclaw.ai/plugins/reference/migrate-hermes
- **minimax** (`@openclaw/minimax-provider`), included in OpenClaw: "Adds MiniMax, MiniMax Portal model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/minimax
- **nvidia** (`@openclaw/nvidia-provider`), included in OpenClaw: "Adds NVIDIA model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/nvidia
- **oc-path** (`@openclaw/oc-path`), included in OpenClaw: "Adds the openclaw path CLI for oc:// workspace file addressing." https://docs.openclaw.ai/plugins/reference/oc-path
- **ollama** (`@openclaw/ollama-provider`), included in OpenClaw: "Adds Ollama, Ollama Cloud model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/ollama
- **omlx** (`@openclaw/omlx-provider`), included in OpenClaw: "Adds Omlx model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/omlx
- **onepassword** (`@openclaw/onepassword`), included in OpenClaw: "1Password SecretRef resolver and curated agent broker with approval policy and SQLite audit history." https://docs.openclaw.ai/plugins/reference/onepassword
- **openai** (`@openclaw/openai-provider`), included in OpenClaw: "Adds OpenAI model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/openai
- **openclaw-id-access** (`@openclaw/openclaw-id-access`), included in OpenClaw: "Choose who can reach this claw remotely: invite people, approve their requests, and see and remove members." https://docs.openclaw.ai/plugins/reference/openclaw-id-access
- **opencode-go** (`@openclaw/opencode-go-provider`), included in OpenClaw: "Adds OpenCode Go model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/opencode-go
- **openrouter** (`@openclaw/openrouter-provider`), included in OpenClaw: "Adds OpenRouter model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/openrouter
- **policy** (`@openclaw/policy`), included in OpenClaw: "Adds policy-backed doctor checks for workspace conformance." https://docs.openclaw.ai/plugins/reference/policy
- **reef** (`@openclaw/reef`), included in OpenClaw: "Guarded end-to-end encrypted claw channel." https://docs.openclaw.ai/plugins/reference/reef
- **requesty** (`@openclaw/requesty-provider`), included in OpenClaw: "Adds Requesty model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/requesty
- **rerank** (`@openclaw/rerank-provider`), included in OpenClaw: "Use any /rerank endpoint as a Decision model." https://docs.openclaw.ai/plugins/reference/rerank
- **runway** (`@openclaw/runway-provider`), included in OpenClaw: "Adds video generation provider support." https://docs.openclaw.ai/plugins/reference/runway
- **senseaudio** (`@openclaw/senseaudio-provider`), included in OpenClaw: "Adds media understanding provider support." https://docs.openclaw.ai/plugins/reference/senseaudio
- **session-share** (`@openclaw/session-share`), included in OpenClaw: "Read-only OpenClaw sessions on paired gateways." https://docs.openclaw.ai/plugins/reference/session-share
- **sglang** (`@openclaw/sglang-provider`), included in OpenClaw: "Adds SGLang model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/sglang
- **skill-workshop** (`@openclaw/skill-workshop`), included in OpenClaw: "Learned skills each agent saves from its own work." https://docs.openclaw.ai/plugins/reference/skill-workshop
- **talk-voice** (`openclaw`), included in OpenClaw: "Manage Talk voice selection (list/set)." https://docs.openclaw.ai/plugins/reference/talk-voice
- **telegram** (`@openclaw/telegram`), included in OpenClaw: "OpenClaw Telegram channel plugin." https://docs.openclaw.ai/plugins/reference/telegram
- **together** (`@openclaw/together-provider`), included in OpenClaw: "Adds Together model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/together
- **tts-local-cli** (`@openclaw/tts-local-cli`), included in OpenClaw: "Adds text-to-speech provider support." https://docs.openclaw.ai/plugins/reference/tts-local-cli
- **vault** (`@openclaw/vault`), included in OpenClaw: "HashiCorp Vault SecretRef provider integration." https://docs.openclaw.ai/plugins/reference/vault
- **vllm** (`@openclaw/vllm-provider`), included in OpenClaw: "Adds vLLM model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/vllm
- **web-readability** (`@openclaw/web-readability-plugin`), included in OpenClaw: "Extract readable article content from local HTML web fetch responses." https://docs.openclaw.ai/plugins/reference/web-readability
- **workboard** (`@openclaw/workboard`), included in OpenClaw: "Dashboard workboard for agent-owned issues and sessions." https://docs.openclaw.ai/plugins/reference/workboard
- **x** (`@openclaw/x`), included in OpenClaw: "Allowlisted X mentions and public replies." https://docs.openclaw.ai/plugins/reference/x
- **xai** (`@openclaw/xai-plugin`), included in OpenClaw: "xAI provider for Grok models, Grok web and X search, code execution, speech, and media generation." https://docs.openclaw.ai/plugins/reference/xai

**Official external packages**

- **abliteration** (`@openclaw/abliteration-provider`), npm or ClawHub: `@openclaw/abliteration-provider`: "OpenClaw Abliteration provider plugin." https://docs.openclaw.ai/plugins/reference/abliteration
- **acpx** (`@openclaw/acpx`), npm or ClawHub: `@openclaw/acpx`: "OpenClaw ACP runtime backend with plugin-owned session and transport management." https://docs.openclaw.ai/plugins/reference/acpx
- **amazon-bedrock** (`@openclaw/amazon-bedrock-provider`), npm or ClawHub: `@openclaw/amazon-bedrock-provider`: "OpenClaw Amazon Bedrock provider plugin with model discovery, embeddings, and guardrail support." https://docs.openclaw.ai/plugins/reference/amazon-bedrock
- **amazon-bedrock-mantle** (`@openclaw/amazon-bedrock-mantle-provider`), npm or ClawHub: `@openclaw/amazon-bedrock-mantle-provider`: "OpenClaw Amazon Bedrock Mantle provider plugin for OpenAI Responses, Chat Completions, and Anthropic Messages routing." https://docs.openclaw.ai/plugins/reference/amazon-bedrock-mantle
- **anthropic-vertex** (`@openclaw/anthropic-vertex-provider`), npm or ClawHub: `@openclaw/anthropic-vertex-provider`: "OpenClaw Anthropic Vertex provider plugin for Claude models on Google Vertex AI." https://docs.openclaw.ai/plugins/reference/anthropic-vertex
- **arcee** (`@openclaw/arcee-provider`), npm or ClawHub: `@openclaw/arcee-provider`: "Adds Arcee model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/arcee
- **baseten** (`@openclaw/baseten-provider`), npm or ClawHub: `@openclaw/baseten-provider`: "OpenClaw Baseten provider plugin." https://docs.openclaw.ai/plugins/reference/baseten
- **brave** (`@openclaw/brave-plugin`), npm or ClawHub: `@openclaw/brave-plugin`: "OpenClaw Brave Search provider plugin for web search." https://docs.openclaw.ai/plugins/reference/brave
- **buzz** (`@openclaw/buzz`), npm or ClawHub: `@openclaw/buzz`: "Connect OpenClaw agents to Buzz rooms." https://docs.openclaw.ai/plugins/reference/buzz
- **byteplus** (`@openclaw/byteplus-provider`), npm or ClawHub: `@openclaw/byteplus-provider`: "Adds BytePlus, BytePlus Plan model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/byteplus
- **cerebras** (`@openclaw/cerebras-provider`), npm or ClawHub: `@openclaw/cerebras-provider`: "Adds Cerebras model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/cerebras
- **chutes** (`@openclaw/chutes-provider`), npm or ClawHub: `@openclaw/chutes-provider`: "Adds Chutes model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/chutes
- **clickclack** (`@openclaw/clickclack`), npm or ClawHub: `@openclaw/clickclack`: "OpenClaw ClickClack channel plugin." https://docs.openclaw.ai/plugins/reference/clickclack
- **cloudflare-ai-gateway** (`@openclaw/cloudflare-ai-gateway-provider`), npm or ClawHub: `@openclaw/cloudflare-ai-gateway-provider`: "Adds Cloudflare AI Gateway model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/cloudflare-ai-gateway
- **codex** (`@openclaw/codex`), npm or ClawHub: `@openclaw/codex`: "Codex app-server harness and native session catalog." https://docs.openclaw.ai/plugins/reference/codex
- **cohere** (`@openclaw/cohere-provider`), npm or ClawHub: `@openclaw/cohere-provider`: "OpenClaw Cohere provider plugin." https://docs.openclaw.ai/plugins/reference/cohere
- **comfy** (`@openclaw/comfy-provider`), npm or ClawHub: `@openclaw/comfy-provider`: "Adds ComfyUI model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/comfy
- **copilot** (`@openclaw/copilot`), npm or ClawHub: `@openclaw/copilot`: "Registers the GitHub Copilot agent runtime." https://docs.openclaw.ai/plugins/reference/copilot
- **deepinfra** (`@openclaw/deepinfra-provider`), npm or ClawHub: `@openclaw/deepinfra-provider`: "Adds DeepInfra model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/deepinfra
- **deepseek** (`@openclaw/deepseek-provider`), npm or ClawHub: `@openclaw/deepseek-provider`: "Adds DeepSeek model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/deepseek
- **diagnostics-otel** (`@openclaw/diagnostics-otel`), npm or ClawHub: `@openclaw/diagnostics-otel`: "OpenClaw diagnostics OpenTelemetry exporter for metrics, traces, and logs." https://docs.openclaw.ai/plugins/reference/diagnostics-otel
- **diagnostics-prometheus** (`@openclaw/diagnostics-prometheus`), npm or ClawHub: `@openclaw/diagnostics-prometheus`: "OpenClaw diagnostics Prometheus exporter for runtime metrics." https://docs.openclaw.ai/plugins/reference/diagnostics-prometheus
- **diffs** (`@openclaw/diffs`), npm or ClawHub: `@openclaw/diffs`: "OpenClaw read-only diff viewer plugin and file renderer for agents." https://docs.openclaw.ai/plugins/reference/diffs
- **diffs-language-pack** (`@openclaw/diffs-language-pack`), npm or ClawHub: `@openclaw/diffs-language-pack`: "Adds syntax highlighting for languages outside the default diffs viewer set." https://docs.openclaw.ai/plugins/reference/diffs-language-pack
- **discord** (`@openclaw/discord`), npm or ClawHub: `@openclaw/discord`: "OpenClaw Discord channel plugin for channels, DMs, commands, and app events." https://docs.openclaw.ai/plugins/reference/discord
- **duckduckgo** (`@openclaw/duckduckgo-plugin`), npm or ClawHub: `@openclaw/duckduckgo-plugin`: "Adds web search provider support." https://docs.openclaw.ai/plugins/reference/duckduckgo
- **exa** (`@openclaw/exa-plugin`), npm or ClawHub: `@openclaw/exa-plugin`: "Adds web search provider support." https://docs.openclaw.ai/plugins/reference/exa
- **facetime** (`@openclaw/facetime`), npm or ClawHub: `@openclaw/facetime`: "Experimental FaceTime realtime voice carrier for OpenClaw agents." https://docs.openclaw.ai/plugins/reference/facetime
- **featherless** (`@openclaw/featherless-provider`), npm or ClawHub: `@openclaw/featherless-provider`: "OpenClaw Featherless AI provider plugin." https://docs.openclaw.ai/plugins/reference/featherless
- **feishu** (`@openclaw/feishu`), npm or ClawHub: `@openclaw/feishu`: "OpenClaw Feishu/Lark channel plugin for chats and workplace tools (community maintained by @m1heng)." https://docs.openclaw.ai/plugins/reference/feishu
- **firecrawl** (`@openclaw/firecrawl-plugin`), npm or ClawHub: `@openclaw/firecrawl-plugin`: "Adds agent-callable tools. Adds web fetch provider support. Adds web search provider support." https://docs.openclaw.ai/plugins/reference/firecrawl
- **fireworks** (`@openclaw/fireworks-provider`), npm or ClawHub: `@openclaw/fireworks-provider`: "Adds Fireworks model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/fireworks
- **fish-audio-speech** (`@openclaw/fish-audio-speech`), npm or ClawHub: `@openclaw/fish-audio-speech`: "Fish Audio hosted text-to-speech with streaming, voice notes, and telephony output." https://docs.openclaw.ai/plugins/reference/fish-audio-speech
- **gmi** (`@openclaw/gmi-provider`), npm or ClawHub: `@openclaw/gmi-provider`: "OpenClaw GMI Cloud provider plugin." https://docs.openclaw.ai/plugins/reference/gmi
- **google-meet** (`@openclaw/google-meet`), npm or ClawHub: `@openclaw/google-meet`: "OpenClaw Google Meet participant plugin for joining calls through Chrome or Twilio transports." https://docs.openclaw.ai/plugins/reference/google-meet
- **googlechat** (`@openclaw/googlechat`), npm or ClawHub: `@openclaw/googlechat`: "OpenClaw Google Chat channel plugin for spaces and direct messages." https://docs.openclaw.ai/plugins/reference/googlechat
- **gradium** (`@openclaw/gradium-speech`), npm or ClawHub: `@openclaw/gradium-speech`: "Adds text-to-speech provider support." https://docs.openclaw.ai/plugins/reference/gradium
- **groq** (`@openclaw/groq-provider`), npm or ClawHub: `@openclaw/groq-provider`: "Adds Groq model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/groq
- **imessage** (`@openclaw/imessage`), npm or ClawHub: `@openclaw/imessage`: "OpenClaw iMessage channel plugin using imsg on a signed-in Mac." https://docs.openclaw.ai/plugins/reference/imessage
- **inworld** (`@openclaw/inworld-speech`), npm or ClawHub: `@openclaw/inworld-speech`: "Inworld streaming text-to-speech (MP3, OGG_OPUS, PCM telephony)." https://docs.openclaw.ai/plugins/reference/inworld
- **irc** (`@openclaw/irc`), npm or ClawHub: `@openclaw/irc`: "OpenClaw IRC channel plugin." https://docs.openclaw.ai/plugins/reference/irc
- **kilocode** (`@openclaw/kilocode-provider`), npm or ClawHub: `@openclaw/kilocode-provider`: "Adds Kilocode model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/kilocode
- **kimi** (`@openclaw/kimi-provider`), npm or ClawHub: `@openclaw/kimi-provider`: "Adds Kimi, Kimi Code, Kimi Coding model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/kimi
- **levanto** (`@openclaw/levanto`), npm or ClawHub: `@openclaw/levanto`: "Native Yes/No, Choice, Scale, Sort, and Tags decisions with explicit abstention." https://docs.openclaw.ai/plugins/reference/levanto
- **line** (`@openclaw/line`), npm or ClawHub: `@openclaw/line`: "OpenClaw LINE channel plugin for LINE Bot API chats." https://docs.openclaw.ai/plugins/reference/line
- **liquid-ai** (`@openclaw/liquid-ai-provider`), npm or ClawHub: `@openclaw/liquid-ai-provider`: "Adds Liquid AI model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/liquid-ai
- **llama-cpp** (`@openclaw/llama-cpp-provider`), npm or ClawHub: `@openclaw/llama-cpp-provider`: "Managed and external llama.cpp servers for GGUF chat, embeddings and local images." https://docs.openclaw.ai/plugins/reference/llama-cpp
- **lobster** (`@openclaw/lobster`), npm or ClawHub: `@openclaw/lobster`: "Lobster workflow tool plugin for typed pipelines and resumable approvals." https://docs.openclaw.ai/plugins/reference/lobster
- **longcat** (`@openclaw/longcat-provider`), npm or ClawHub: `@openclaw/longcat-provider`: "OpenClaw LongCat provider plugin." https://docs.openclaw.ai/plugins/reference/longcat
- **matrix** (`@openclaw/matrix`), npm or ClawHub: `@openclaw/matrix`: "OpenClaw Matrix channel plugin for rooms and direct messages." https://docs.openclaw.ai/plugins/reference/matrix
- **mattermost** (`@openclaw/mattermost`), npm or ClawHub: `@openclaw/mattermost`: "OpenClaw Mattermost channel plugin." https://docs.openclaw.ai/plugins/reference/mattermost
- **memory-lancedb** (`@openclaw/memory-lancedb`), npm or ClawHub: `@openclaw/memory-lancedb`: "OpenClaw LanceDB-backed long-term memory plugin with auto-recall, auto-capture, and vector search." https://docs.openclaw.ai/plugins/reference/memory-lancedb
- **meta** (`@openclaw/meta-provider`), npm or ClawHub: `@openclaw/meta-provider`: "Adds Meta model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/meta
- **mistral** (`@openclaw/mistral-provider`), npm or ClawHub: `@openclaw/mistral-provider`: "Adds Mistral model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/mistral
- **moonshot** (`@openclaw/moonshot-provider`), npm or ClawHub: `@openclaw/moonshot-provider`: "Adds Moonshot model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/moonshot
- **msteams** (`@openclaw/msteams`), npm or ClawHub: `@openclaw/msteams`: "OpenClaw Microsoft Teams channel plugin for bot conversations." https://docs.openclaw.ai/plugins/reference/msteams
- **muse** (`@openclaw/muse`), npm or ClawHub: `@openclaw/muse`: "Runs Meta models through the Muse Code CLI." https://docs.openclaw.ai/plugins/reference/muse
- **mxc** (`@openclaw/mxc-sandbox`), npm or ClawHub: `@openclaw/mxc-sandbox`: "OS-level sandboxed tool execution via MXC: runs commands in a Windows ProcessContainer with configured MXC policy files." https://docs.openclaw.ai/plugins/reference/mxc
- **nextcloud-talk** (`@openclaw/nextcloud-talk`), npm or ClawHub: `@openclaw/nextcloud-talk`: "OpenClaw Nextcloud Talk channel plugin for conversations." https://docs.openclaw.ai/plugins/reference/nextcloud-talk
- **nostr** (`@openclaw/nostr`), npm or ClawHub: `@openclaw/nostr`: "OpenClaw Nostr channel plugin for NIP-04 encrypted direct messages." https://docs.openclaw.ai/plugins/reference/nostr
- **novita** (`@openclaw/novita-provider`), npm or ClawHub: `@openclaw/novita-provider`: "Adds Novita, Novita AI, Novitaai model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/novita
- **onnx** (`@openclaw/onnx`), npm or ClawHub: `@openclaw/onnx`: "Local typed decisions using pinned ONNX classifiers." https://docs.openclaw.ai/plugins/reference/onnx
- **opencode** (`@openclaw/opencode-provider`), npm or ClawHub: `@openclaw/opencode-provider`: "Adds OpenCode model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/opencode
- **openshell** (`@openclaw/openshell-sandbox`), npm or ClawHub: `@openclaw/openshell-sandbox`: "OpenClaw sandbox backend for the NVIDIA OpenShell CLI with mirrored local workspaces and SSH command execution." https://docs.openclaw.ai/plugins/reference/openshell
- **parallel** (`@openclaw/parallel-plugin`), npm or ClawHub: `@openclaw/parallel-plugin`: "Adds Parallel model provider support to OpenClaw." https://docs.openclaw.ai/tools/parallel-search
- **particle** (`@openclaw/particle-provider`), npm or ClawHub: `@openclaw/particle-provider`: "Adds Particle model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/particle
- **perplexity** (`@openclaw/perplexity-plugin`), npm or ClawHub: `@openclaw/perplexity-plugin`: "Adds web search provider support." https://docs.openclaw.ai/plugins/reference/perplexity
- **pixverse** (`@openclaw/pixverse-provider`), npm or ClawHub: `@openclaw/pixverse-provider`: "OpenClaw PixVerse video generation provider plugin." https://docs.openclaw.ai/plugins/reference/pixverse
- **qianfan** (`@openclaw/qianfan-provider`), npm or ClawHub: `@openclaw/qianfan-provider`: "Adds Qianfan model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/qianfan
- **qqbot** (`@tencent-connect/openclaw-qqbot`), npm: "OpenClaw QQ Bot channel plugin for group and direct-message workflows." https://docs.openclaw.ai/plugins/reference/qqbot
- **qwen** (`@openclaw/qwen-provider`), npm or ClawHub: `@openclaw/qwen-provider`: "Adds Qwen, Qwen Cloud, Model Studio, DashScope, Qwen Token Plan, Bailian Token Plan model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/qwen
- **radius** (`@openclaw/radius-provider`), npm or ClawHub: `@openclaw/radius-provider`: "Radius model gateway provider." https://docs.openclaw.ai/plugins/reference/radius
- **raft** (`@openclaw/raft`), npm or ClawHub: `@openclaw/raft`: "OpenClaw Raft channel plugin for secure CLI wake bridges." https://docs.openclaw.ai/plugins/reference/raft
- **searxng** (`@openclaw/searxng-plugin`), npm or ClawHub: `@openclaw/searxng-plugin`: "Adds web search provider support." https://docs.openclaw.ai/plugins/reference/searxng
- **signal** (`@openclaw/signal`), npm or ClawHub: `@openclaw/signal`: "OpenClaw Signal channel plugin." https://docs.openclaw.ai/plugins/reference/signal
- **slack** (`@openclaw/slack`), npm or ClawHub: `@openclaw/slack`: "OpenClaw Slack channel plugin for channels, DMs, commands, and app events." https://docs.openclaw.ai/plugins/reference/slack
- **slack-huddles** (`@openclaw/slack-huddles`), npm or ClawHub: `@openclaw/slack-huddles`: "Join Slack huddles through a dedicated Slack user in Chrome." https://docs.openclaw.ai/plugins/reference/slack-huddles
- **sms** (`@openclaw/sms`), npm or ClawHub: `@openclaw/sms`: "Twilio SMS/MMS channel plugin for OpenClaw messages." https://docs.openclaw.ai/plugins/reference/sms
- **stepfun** (`@openclaw/stepfun-provider`), npm or ClawHub: `@openclaw/stepfun-provider`: "Adds StepFun, StepFun Plan model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/stepfun
- **subq** (`@openclaw/subq`), npm or ClawHub: `@openclaw/subq`: "SubQ Snap typed decisions (not a conversational model)." https://docs.openclaw.ai/plugins/reference/subq
- **synology-chat** (`@openclaw/synology-chat`), npm or ClawHub: `@openclaw/synology-chat`: "Synology Chat channel plugin for OpenClaw channels and direct messages." https://docs.openclaw.ai/plugins/reference/synology-chat
- **synthetic** (`@openclaw/synthetic-provider`), npm or ClawHub: `@openclaw/synthetic-provider`: "Adds Synthetic model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/synthetic
- **tavily** (`@openclaw/tavily-plugin`), npm or ClawHub: `@openclaw/tavily-plugin`: "Adds agent-callable tools. Adds web search provider support." https://docs.openclaw.ai/plugins/reference/tavily
- **team-reports** (`@openclaw/team-reports`), npm or ClawHub: `@openclaw/team-reports`: "Daily, weekly, and monthly team activity reports from GitHub and Discord, with model-written summaries, served in the Control UI." https://docs.openclaw.ai/plugins/reference/team-reports
- **teams-meetings** (`@openclaw/teams-meetings`), npm or ClawHub: `@openclaw/teams-meetings`: "Join Microsoft Teams meetings as a Chrome browser guest." https://docs.openclaw.ai/plugins/reference/teams-meetings
- **tencent** (`@openclaw/tencent-provider`), npm or ClawHub: `@openclaw/tencent-provider`: "Adds Tencent TokenHub, Tencent Tokenplan model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/tencent
- **tlon** (`@openclaw/tlon`), npm or ClawHub: `@openclaw/tlon`: "OpenClaw Tlon/Urbit channel plugin for chat workflows." https://docs.openclaw.ai/plugins/reference/tlon
- **tokenjuice** (`@openclaw/tokenjuice`), npm or ClawHub: `@openclaw/tokenjuice`: "Compacts exec and bash tool results with tokenjuice reducers." https://docs.openclaw.ai/plugins/reference/tokenjuice
- **twitch** (`@openclaw/twitch`), npm or ClawHub: `@openclaw/twitch`: "OpenClaw Twitch channel plugin for chat and moderation workflows." https://docs.openclaw.ai/plugins/reference/twitch
- **typesafe** (`@openclaw/typesafe`), npm or ClawHub: `@openclaw/typesafe`: "Typed decision provider for hosted Jev and local System One models." https://docs.openclaw.ai/plugins/reference/typesafe
- **venice** (`@openclaw/venice-provider`), npm or ClawHub: `@openclaw/venice-provider`: "Adds Venice model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/venice
- **vercel-ai-gateway** (`@openclaw/vercel-ai-gateway-provider`), npm or ClawHub: `@openclaw/vercel-ai-gateway-provider`: "Adds Vercel AI Gateway model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/vercel-ai-gateway
- **voice-call** (`@openclaw/voice-call`), npm or ClawHub: `@openclaw/voice-call`: "OpenClaw voice-call plugin for Twilio, Telnyx, and Plivo phone calls." https://docs.openclaw.ai/plugins/reference/voice-call
- **volcengine** (`@openclaw/volcengine-provider`), npm or ClawHub: `@openclaw/volcengine-provider`: "Adds Volcengine, Volcengine Plan model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/volcengine
- **voyage** (`@openclaw/voyage-provider`), npm or ClawHub: `@openclaw/voyage-provider`: "Adds embedding provider support, including memory search." https://docs.openclaw.ai/plugins/reference/voyage
- **vydra** (`@openclaw/vydra-provider`), npm or ClawHub: `@openclaw/vydra-provider`: "Adds Vydra model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/vydra
- **whatsapp** (`@openclaw/whatsapp`), npm or ClawHub: `@openclaw/whatsapp`: "OpenClaw WhatsApp channel plugin for WhatsApp Web chats." https://docs.openclaw.ai/plugins/reference/whatsapp
- **xiaomi** (`@openclaw/xiaomi-provider`), npm or ClawHub: `@openclaw/xiaomi-provider`: "Adds Xiaomi, Xiaomi Token Plan model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/xiaomi
- **zai** (`@openclaw/zai-provider`), npm or ClawHub: `@openclaw/zai-provider`: "Adds Z.AI model provider support to OpenClaw." https://docs.openclaw.ai/plugins/reference/zai
- **zalo** (`@openclaw/zalo`), npm or ClawHub: `@openclaw/zalo`: "OpenClaw Zalo channel plugin for bot and webhook chats." https://docs.openclaw.ai/plugins/reference/zalo
- **zalouser** (`@openclaw/zalouser`), npm or ClawHub: `@openclaw/zalouser`: "OpenClaw Zalo Personal Account plugin via native zca-js integration." https://docs.openclaw.ai/plugins/reference/zalouser
- **zoom-meetings** (`@openclaw/zoom-meetings`), npm or ClawHub: `@openclaw/zoom-meetings`: "Join Zoom meetings as a Chrome browser guest." https://docs.openclaw.ai/plugins/reference/zoom-meetings

**Source checkout only**

- **qa-channel** (`@openclaw/qa-channel`), source checkout only: "OpenClaw QA synthetic channel plugin." https://docs.openclaw.ai/plugins/reference/qa-channel
- **qa-lab** (`@openclaw/qa-lab`), source checkout only: "OpenClaw QA lab plugin with private debugger UI and scenario runner." https://docs.openclaw.ai/plugins/reference/qa-lab
- **visitor-access** (`@openclaw/visitor-access`), source checkout only: "Manage expiring visitor grants through one Cloudflare Access email policy." https://docs.openclaw.ai/plugins/reference/visitor-access

### Other navigation tabs (release notes, contributor process, help)

These tabs are in the navigation but describe releases, contributing and support, not components. Page names and URLs only.

**Tab: Releases**

- Release notes: Release notes (https://docs.openclaw.ai/releases/index); v2026.11.3 (https://docs.openclaw.ai/releases/2026.11.3); v2026.11.2 (https://docs.openclaw.ai/releases/2026.11.2); v2026.11.1 (https://docs.openclaw.ai/releases/2026.11.1); v2026.10.10 (https://docs.openclaw.ai/releases/2026.10.10); v2026.10.9 (https://docs.openclaw.ai/releases/2026.10.9); v2026.10.8 (https://docs.openclaw.ai/releases/2026.10.8); v2026.10.7 (https://docs.openclaw.ai/releases/2026.10.7); v2026.10.6 (https://docs.openclaw.ai/releases/2026.10.6); v2026.10.5 (https://docs.openclaw.ai/releases/2026.10.5); v2026.10.4 (https://docs.openclaw.ai/releases/2026.10.4); v2026.10.3 (https://docs.openclaw.ai/releases/2026.10.3); v2026.10.2 (https://docs.openclaw.ai/releases/2026.10.2); v2026.10.1 (https://docs.openclaw.ai/releases/2026.10.1); v2026.9.9 (https://docs.openclaw.ai/releases/2026.9.9); v2026.9.8 (https://docs.openclaw.ai/releases/2026.9.8); v2026.9.7 (https://docs.openclaw.ai/releases/2026.9.7); v2026.9.6 (https://docs.openclaw.ai/releases/2026.9.6); v2026.9.5 (https://docs.openclaw.ai/releases/2026.9.5); v2026.9.4 (https://docs.openclaw.ai/releases/2026.9.4); v2026.9.3 (https://docs.openclaw.ai/releases/2026.9.3); v2026.9.2 (https://docs.openclaw.ai/releases/2026.9.2); v2026.9.1 (https://docs.openclaw.ai/releases/2026.9.1); v2026.8.2 (https://docs.openclaw.ai/releases/2026.8.2); v2026.8.1 (AKA OpenClaw 2.0) (https://docs.openclaw.ai/releases/2026.8.1); v2026.7.1 (https://docs.openclaw.ai/releases/2026.7.1); v2026.6.11 (https://docs.openclaw.ai/releases/2026.6.11)
- Release process: Release policy (https://docs.openclaw.ai/reference/RELEASING); Full release validation (https://docs.openclaw.ai/reference/full-release-validation); Dispatch a validation run (https://docs.openclaw.ai/reference/full-release-validation/dispatch); Continue a failed validation (https://docs.openclaw.ai/reference/full-release-validation/continuation); Extended-stable and changelog-only validation (https://docs.openclaw.ai/reference/full-release-validation/extended-stable); Top-level stages (https://docs.openclaw.ai/reference/full-release-validation/stages); Release checks stages (https://docs.openclaw.ai/reference/full-release-validation/release-checks); Release profiles and focused reruns (https://docs.openclaw.ai/reference/full-release-validation/profiles); Evidence to keep (https://docs.openclaw.ai/reference/full-release-validation/evidence); Release performance sweep (https://docs.openclaw.ai/reference/release-performance-sweep); Dependency locking (https://docs.openclaw.ai/gateway/security/dependency-locking)

**Tab: Contributing**

- Maturity: Maturity scorecard (https://docs.openclaw.ai/maturity/scorecard); Maturity taxonomy (https://docs.openclaw.ai/maturity/taxonomy)
- Testing and CI: Tests (https://docs.openclaw.ai/reference/test); Run tests locally (https://docs.openclaw.ai/reference/test/local); Control UI, TUI, and E2E lanes (https://docs.openclaw.ai/reference/test/lanes); Docker test suites (https://docs.openclaw.ai/reference/test/docker); Test performance and benchmarks (https://docs.openclaw.ai/reference/test/performance); Test runner internals (https://docs.openclaw.ai/reference/test/runner-internals); Remote test proof (https://docs.openclaw.ai/reference/test/remote-proof); CI pipeline (https://docs.openclaw.ai/ci); CI pipeline jobs (https://docs.openclaw.ai/ci/pipeline); Watch a CI run (https://docs.openclaw.ai/ci/watching-runs); CI checkout ownership (https://docs.openclaw.ai/ci/checkout); CI scope and routing (https://docs.openclaw.ai/ci/scope-and-routing); Scope selection (https://docs.openclaw.ai/ci/scope-and-routing/selection); Node test lanes (https://docs.openclaw.ai/ci/scope-and-routing/node-test-lanes); Job budgets and platform lanes (https://docs.openclaw.ai/ci/scope-and-routing/job-budgets); Manual dispatches (https://docs.openclaw.ai/ci/scope-and-routing/manual-dispatches); CI runner classes (https://docs.openclaw.ai/ci/runners); CI capacity and shard weights (https://docs.openclaw.ai/ci/capacity); Release validation workflows (https://docs.openclaw.ai/ci/release-validation); Full Release Validation (https://docs.openclaw.ai/ci/release-validation/full-release-validation); Live and E2E shards (https://docs.openclaw.ai/ci/release-validation/live-and-e2e-shards); Package Acceptance (https://docs.openclaw.ai/ci/release-validation/package-acceptance); Install smoke and Docker E2E (https://docs.openclaw.ai/ci/release-validation/install-smoke-and-docker-e2e); Plugin Prerelease (https://docs.openclaw.ai/ci/release-validation/plugin-prerelease); Scheduled and maintenance workflows (https://docs.openclaw.ai/ci/scheduled-workflows); Local checks and Testbox (https://docs.openclaw.ai/ci/local-proof); Scripts (https://docs.openclaw.ai/help/scripts); QA overview (https://docs.openclaw.ai/concepts/qa-e2e-automation); Command surface (https://docs.openclaw.ai/concepts/qa-e2e-automation/command-surface); Operator flow (https://docs.openclaw.ai/concepts/qa-e2e-automation/operator-flow); Scenario coverage (https://docs.openclaw.ai/concepts/qa-e2e-automation/scenario-coverage); Channel QA reference (https://docs.openclaw.ai/concepts/qa-e2e-automation/channel-qa-reference); Slack QA (https://docs.openclaw.ai/concepts/qa-e2e-automation/slack-qa); WhatsApp QA and credentials (https://docs.openclaw.ai/concepts/qa-e2e-automation/whatsapp-and-credentials); Extending the QA stack (https://docs.openclaw.ai/concepts/qa-e2e-automation/extending-the-stack); QA reporting (https://docs.openclaw.ai/concepts/qa-e2e-automation/qa-reporting); Personal agent benchmark pack (https://docs.openclaw.ai/concepts/personal-agent-benchmark-pack); Testing (https://docs.openclaw.ai/help/testing); Test suites and commands (https://docs.openclaw.ai/help/testing/suites); Live and Docker/Parallels workflows (https://docs.openclaw.ai/help/testing/live-workflows); Docker test runners (https://docs.openclaw.ai/help/testing/docker); QA-specific runners (https://docs.openclaw.ai/help/testing/qa-runners); Contract tests (https://docs.openclaw.ai/help/testing/contracts); Writing and adding tests (https://docs.openclaw.ai/help/testing/writing-tests); Testing: updates and plugins (https://docs.openclaw.ai/help/testing-updates-plugins); Testing: live suites (https://docs.openclaw.ai/help/testing-live); Quick live smokes and the Android node sweep (https://docs.openclaw.ai/help/testing-live/quick-smokes); Live model smoke (profile keys) (https://docs.openclaw.ai/help/testing-live/model-smoke); CLI backend and APNs lanes (https://docs.openclaw.ai/help/testing-live/cli-backends); ACP bind and Codex app-server lanes (https://docs.openclaw.ai/help/testing-live/acp-and-codex); OpenAI long context and the live model matrix (https://docs.openclaw.ai/help/testing-live/long-context-and-matrix); Media provider live lanes (https://docs.openclaw.ai/help/testing-live/media-providers); Mantis (https://docs.openclaw.ai/concepts/mantis); Mantis Slack desktop runbook (https://docs.openclaw.ai/concepts/mantis-slack-desktop-runbook)

**Tab: Help**

- Start here: Help (https://docs.openclaw.ai/help/index); Get support (https://docs.openclaw.ai/help/support); General troubleshooting (https://docs.openclaw.ai/help/troubleshooting); Debugging (https://docs.openclaw.ai/help/debugging)
- FAQ: FAQ (https://docs.openclaw.ai/help/faq); What is OpenClaw? (https://docs.openclaw.ai/help/faq/what-is-openclaw); Skills and automation (https://docs.openclaw.ai/help/faq/skills-and-automation); Sandboxing and memory (https://docs.openclaw.ai/help/faq/sandboxing-and-memory); Where things live on disk (https://docs.openclaw.ai/help/faq/where-things-live-on-disk); Config basics (https://docs.openclaw.ai/help/faq/config-basics); Remote gateways and nodes (https://docs.openclaw.ai/help/faq/remote-gateways-and-nodes); Env vars and .env loading (https://docs.openclaw.ai/help/faq/env-vars); Sessions and multiple chats (https://docs.openclaw.ai/help/faq/sessions-and-chats); Gateway ports, already running, and remote mode (https://docs.openclaw.ai/help/faq/gateway-ports-and-remote-mode); Logging and debugging (https://docs.openclaw.ai/help/faq/logging-and-debugging); Media and attachments (https://docs.openclaw.ai/help/faq/media-and-attachments); Security and access control (https://docs.openclaw.ai/help/faq/security-and-access-control); Chat commands, aborting tasks, and stopping a run (https://docs.openclaw.ai/help/faq/chat-commands-and-stopping); FAQ: first-run setup (https://docs.openclaw.ai/help/faq-first-run); FAQ: quick start and first-run setup (https://docs.openclaw.ai/help/faq-first-run/quick-start); FAQ: providers, hardware, and hosting (https://docs.openclaw.ai/help/faq-first-run/providers-and-hosting); FAQ: models and auth (https://docs.openclaw.ai/help/faq-models)
- Diagnostics: Environment variables (https://docs.openclaw.ai/help/environment); Diagnostics flags (https://docs.openclaw.ai/diagnostics/flags)
- Community and meta: OpenClaw lore (https://docs.openclaw.ai/start/lore)


---

## 3. What the user must bring

Each item is something the docs say the user supplies or sets up.

| Item | Docs quote | URL |
|---|---|---|
| A machine to run the Gateway (own computer or a server) | "You run a single Gateway process on your own machine (or a server)" | https://docs.openclaw.ai/ |
| Supported OS | "The installer supports macOS, Linux, and Windows. It provisions a supported Node.js runtime when needed." | https://github.com/openclaw/openclaw/blob/main/README.md |
| Node.js runtime | "**Node.js 24.16.0+ on 24.x, or 26.1.0+** (Node 26 is recommended; use 24.22.1+/26.12.1+ for the security fixes)" (the home page instead says "Node 26 (recommended), or another supported release: Node 24.22.1+ or Node 26.12.1+"; see section 5) | https://docs.openclaw.ai/start/getting-started |
| Model access: an existing CLI login or a provider API key | "**An existing Claude Code or Codex CLI login, or a provider API key** — onboarding can reuse it" | https://docs.openclaw.ai/start/getting-started |
| A strong model (the docs' recommendation) | "For best quality and security, use the strongest latest-generation model available." | https://docs.openclaw.ai/ |
| Subscription auth (optional route) | "Subscription auth via OAuth (e.g. OpenAI Codex)" | https://docs.openclaw.ai/concepts/features |
| Self-hosted model runtime (optional) | "Custom and self-hosted provider support (vLLM, SGLang, Ollama, llama.cpp, LM Studio, and any OpenAI-compatible or Anthropic-compatible endpoint)" | https://docs.openclaw.ai/concepts/features |
| Messaging accounts, one per channel | "OpenClaw can talk to you on any chat app you already use. Each channel connects via the Gateway." | https://docs.openclaw.ai/channels |
| Telegram: a bot token from BotFather | "Create the bot in BotFather, give OpenClaw its token, approve the first DM, and add the bot to a group." | https://docs.openclaw.ai/channels/telegram/setup |
| WhatsApp: a WhatsApp account linked by QR | "Login is QR-only. On remote or headless hosts, have a reliable path to deliver the live QR to the phone before starting login" | https://docs.openclaw.ai/channels/whatsapp |
| A separate phone number for the assistant (recommended) | "For phone-number-based channels, consider running the assistant on a separate number from your personal one" | https://docs.openclaw.ai/gateway/security/hardened-baseline |
| iMessage: a Mac signed in to Messages, with permissions | "Messages must be signed in on the Mac running `imsg`." "Full Disk Access is required [...]" "Automation permission is required to send messages through Messages.app." Advanced actions need "System Integrity Protection must be disabled" | https://docs.openclaw.ai/channels/imessage/setup |
| Signal: a bot phone number and the signal-cli daemon | "`account` - Bot phone number in E.164 format"; summary: "Signal support via signal-cli (native daemon or bbernhard container)" | https://docs.openclaw.ai/channels/signal |
| Slack: a Slack app and its tokens | "install the plugin, create the Slack app, and configure tokens" | https://docs.openclaw.ai/channels/slack |
| Discord: a Discord application and bot | "Create the Discord application, invite the bot, and set up a guild workspace" | https://docs.openclaw.ai/channels/discord/setup |
| SMS: a Twilio account | summary: "Twilio SMS/MMS setup, access controls, webhooks, and delivery status" | https://docs.openclaw.ai/channels/sms |
| Web search provider (some need API keys) | "Some providers are key-free, others need an API key." | https://docs.openclaw.ai/tools/web |
| Sandbox backend, if sandboxing is wanted (Docker by default) | "Sandboxing is off by default and controlled by `agents.defaults.sandbox` [...]"; Docker is "The default local backend" | https://docs.openclaw.ai/gateway/sandboxing ; https://docs.openclaw.ai/gateway/sandboxing/docker-backend |
| Companion devices (optional) | "A **node** is a companion device (macOS/iOS/watchOS/Android/headless) that connects to the Gateway with `role: \"node\"`" | https://docs.openclaw.ai/nodes |
| macOS app host version | "**OpenClaw.app requires macOS 26.2 (Tahoe) or later.**" | https://docs.openclaw.ai/platforms/macos |
| Remote access path (optional) | "Preferred: Tailscale or VPN. Alternative: SSH tunnel" | https://docs.openclaw.ai/concepts/architecture |
| Shared secret when binding beyond loopback | "If you bind to `lan` or `tailnet`, the Gateway requires a shared secret (`gateway.auth.token` or `gateway.auth.password`)" | https://docs.openclaw.ai/vps |
| A rented host, if not running locally (optional) | Hosting guides for Cloudflare, Daytona, exe.dev, Fly, Northflank, Railway, Render, Upstash, Azure, DigitalOcean, GCP, Hetzner, Hostinger, Oracle, plus Ansible, Kubernetes, Raspberry Pi, Jetson and macOS VMs; "a sandboxed macOS VM when you need macOS itself (iMessage) rather than a Linux host" | https://docs.openclaw.ai/vps |
| Crabbox, for cloud workers (optional) | "With Crabbox configured on the Gateway host, OpenClaw can select a machine, prepare the repository, and save a snapshot" | https://docs.openclaw.ai/gateway/cloud-workers |
| A GitHub account, to publish on ClawHub (optional) | "ClawHub uses GitHub for web sign-in. The CLI uses ClawHub API tokens created through that signed-in account." | https://docs.openclaw.ai/clawhub/auth |
| Secrets backends (optional) | "Every supported credential field takes a SecretRef: `env`, `file`, `exec` (this is how 1Password, Vault, Bitwarden, and sops plug in), or the shared store." | https://docs.openclaw.ai/start/why-openclaw/secrets |
| Workspace content the agent reads (persona, standing orders, memory) | Each agent has its own "**Workspace**: files, `AGENTS.md`/`SOUL.md`/`USER.md`, local notes, persona rules." Standing orders "live in workspace files (typically `AGENTS.md`)" | https://docs.openclaw.ai/concepts/multi-agent ; https://docs.openclaw.ai/automation |

---

## 4. How the pieces connect

### 4.1 The overall shape

Docs home diagram (https://docs.openclaw.ai/), labels verbatim: `Chat apps + plugins` → `Gateway`; `Gateway` → `OpenClaw agent`, `CLI`, `Web Control UI`, `macOS app`, `iOS and Android nodes`. Caption: "The Gateway is the single source of truth for sessions, routing, and channel connections."

Gateway architecture (https://docs.openclaw.ai/concepts/architecture):
> "A single long-lived **Gateway** owns all messaging surfaces (WhatsApp via Baileys, Telegram via grammY, Slack, Discord, Signal, iMessage, WebChat)." "Control-plane clients (macOS app, CLI, web UI, automations) connect to the Gateway over **WebSocket** on the configured bind host (default `127.0.0.1:18789`)." "**Nodes** (macOS/iOS/Android/headless) also connect over **WebSocket**, but declare `role: node` with explicit caps/commands." "One Gateway per host."

Its component list: **Gateway (daemon)**: "Maintains provider connections", "Exposes a typed WS API (requests, responses, server-push events)", "Emits events like `agent`, `chat`, `presence`, `health`, `heartbeat`, `cron`." **Clients (mac app / CLI / web admin)**: "One WS connection per client." **Nodes**: "Expose commands like `camera.*`, `screen.record`, and `location.get`." **WebChat**: "Static UI that uses the Gateway WS API for chat history and sends."

Connection lifecycle diagram (same page), labels verbatim: participants `Client`, `Gateway`; steps `req:connect` → `res (ok)` ("or res error + close"; "payload=hello-ok snapshot: presence + health") → `event:presence` → `event:tick` → `req:agent` → `res:agent ack {runId, status:"accepted"}` → `event:agent (streaming)` → `res:agent final {runId, status, summary}`.

Trust-boundary diagram (https://docs.openclaw.ai/start/why-openclaw/the-trust-boundary), labels verbatim: subgraph `Gateway (trusted control plane)` containing `Channel connections`, `Policy: modes, scopes, exec approvals`, `Credentials: SecretRefs, supported sentinel paths`, `Versioned state; memory artifacts and index`; subgraph `Configured isolated execution (sandboxing off by default)` containing `Sandbox: Docker, Podman, SSH, OpenShell`, `Hosted node sessions: sealed, hash-verified worker`, `Cloud workers: scoped RPC authority, proxied inference`; edges `Operators, channels, peer agents` → (`configured admission and authorization`) → Gateway; Gateway → (`tool requests or worker turns`) → execution; execution → (`results and scoped worker RPCs`) → Gateway.

Personal-assistant setup diagram (https://docs.openclaw.ai/start/openclaw), labels verbatim: `Your Phone (personal) Your WhatsApp +1-555-YOU` -- message --> `Second Phone (assistant) Assistant WA +1-555-ASSIST` -- linked via QR --> `Your Mac (openclaw) AI agent`.

### 4.2 An inbound message

Message flow (https://docs.openclaw.ai/concepts/messages), verbatim:
```text
Inbound message
  -> routing/bindings -> session key
  -> dedupe + debounce
  -> queue (if a run is already active)
  -> agent run (streaming + tools)
  -> outbound replies (channel limits + chunking)
```
- Routing (https://docs.openclaw.ai/channels/channel-routing): "OpenClaw routes replies **back to the channel where a message came from**. The model does not choose a channel; routing follows fixed rules controlled by the host configuration." "Ordinary routing picks **one agent** for each inbound message", in this order: exact peer match, parent peer match, peer wildcard, guild + roles (Discord), guild (Discord), team (Slack), account match, channel match, fallback owner. "The matched agent determines which workspace and session store are used."
- Access gate before routing (https://docs.openclaw.ai/gateway/security): "most chat channels answer an unknown DM sender with a pairing code instead of processing the message; and group access is allowlisted, usually behind a mention gate."
- Dedupe (https://docs.openclaw.ai/concepts/messages): "OpenClaw keeps an in-memory cache keyed by agent scope, channel route (channel + peer + account + thread), and message id, so a redelivered message does not trigger a second agent run."
- Sessions (same page): "Sessions are owned by the gateway, not by clients." "Direct chats collapse into the agent's main session key." "Groups/channels get their own session keys."
- Queue (https://docs.openclaw.ai/concepts/agent-loop): "The session controller serializes turns by physical session identity before global capacity admission. Messaging channels choose a queue mode (steer/followup/collect/interrupt)".
- Agent run (https://docs.openclaw.ai/concepts/agent-loop): "The agent loop is the serialized, per-session run that turns a message into actions and a reply: intake, context assembly, model inference, tool execution, streaming, persistence." Run sequence: `agent` RPC "validates params, resolves the session [...] and returns `{ runId, acceptedAt }` immediately"; `agentCommand` "resolves model + thinking/verbose/trace defaults, loads the skills snapshot, calls `runEmbeddedAgent`"; `runEmbeddedAgent` "resolves model + auth profile, builds the OpenClaw session, subscribes to runtime events, streams assistant/tool deltas"; events are bridged to streams `tool`, `assistant`, `lifecycle`; `agent.wait` returns the terminal outcome.
- Workspace and prompt (same page): "Workspace is resolved and created; sandboxed runs may redirect to a sandbox workspace root." "Skills are loaded (or reused from a snapshot) and injected into env and prompt." "Bootstrap/context files are resolved and injected into the system prompt." "System prompt is built from OpenClaw's base prompt, skills prompt, bootstrap context, and per-run overrides." System prompt page: "OpenClaw owns the system prompt for every agent run; there is no runtime default prompt." (https://docs.openclaw.ai/concepts/system-prompt)
- Hooks along the way (https://docs.openclaw.ai/concepts/agent-loop): "Internal hooks: `HOOK.md` scripts for command and lifecycle events" and "Plugin hooks: typed `api.on(...)` handlers inside the agent/tool lifecycle and Gateway pipeline", including `before_model_resolve`, `before_prompt_build`, `before_agent_reply`, `before_tool_call` / `after_tool_call`, `tool_result_persist`, `message_received` / `message_sending` / `message_sent`, `agent_end`, `session_start` / `session_end`, `gateway_start` / `gateway_stop`, `before_compaction` / `after_compaction`, `before_install`.
- Where tools execute (https://docs.openclaw.ai/gateway/sandboxing): "The Gateway process always stays on the host; only tool execution moves" into a sandbox when one is configured. README: "Tools run on the host for the main session unless you configure sandboxing." Remote placements (https://docs.openclaw.ai/gateway/cloud-sessions): sessions can run on the Gateway, a paired device, or a cloud worker; "In all remote placements, model inference stays proxied through the Gateway — provider credentials never reach the remote machine".
- Outbound: replies obey "channel limits + chunking" (https://docs.openclaw.ai/concepts/messages); an outbound sanitizer "strips leaked `<tool_call>`, `<function_calls>`, `<system-reminder>` [...] from user-visible replies at the final channel delivery boundary" (https://docs.openclaw.ai/gateway/security/prompt-injection).
- Memory after the turn (https://docs.openclaw.ai/concepts/memory): "OpenClaw remembers things by writing plain Markdown files in your agent's workspace [...] The model only remembers what gets saved to disk; there is no hidden state." Memory architecture diagram (https://docs.openclaw.ai/concepts/memory-architecture), labels verbatim: `Interactive sessions` -(notes, flush)-> `Episodic tier + index (with provenance)`; `Session end` -(transcript ingestion)-> episodic tier; `Pre-compaction flush` -(facts to daily notes)-> episodic tier; episodic tier -> `Dreaming: check (rule-based)` -(`gated candidates (never untrusted or system)`)-> `Consolidation (model, bounded)` -(`merge, supersede, dedupe`)-> `MEMORY.md / USER.md`; consolidation -(`summary + pre-image`)-> `DREAMS.md`.

### 4.3 A scheduled run

Automation overview (https://docs.openclaw.ai/automation): "Automations are OpenClaw's built-in scheduler for all recurring and one-shot work, including periodic monitors. The scheduler persists jobs, wakes the agent at the right time, and can deliver output to a chat channel or webhook endpoint." Decision diagram labels verbatim: `What do you need?` → `Schedule work?` → `Automations`; `Orchestrate multi-step flows?` → `Lobster`; `React to lifecycle events?` → `Hooks`; `Give the agent persistent instructions?` → `Standing Orders`.

Run lifecycle (https://docs.openclaw.ai/automation/cron-jobs/how-it-works):
- "Automations run **inside the Gateway process**, not inside the model. The Gateway must be running for schedules to fire."
- "Job definitions, runtime state, and run history persist in OpenClaw's shared SQLite state database, so restarts do not lose schedules."
- Gateway kernel (https://docs.openclaw.ai/concepts/architecture): "The Gateway kernel owns one `GatewayScheduler` for registered maintenance and cron wakeups."
- "Agent, command, and script jobs write their result once into the chat or topic that receives it [...] A different delivery destination gets the result instead of the creating chat".
- "One-shot jobs (`--at`) auto-delete after successful completion".
- Budgets: "isolated/detached agent-turn jobs are bounded by the scheduler's own 60-minute watchdog; command jobs default to 10 minutes, and script payloads default to 5 minutes."
- "On Gateway startup, overdue jobs that require agent execution are rescheduled instead of replayed immediately".
- Isolated runs "best-effort close tracked browser tabs/processes for their `cron:<jobId>` session on completion".
- Promotion: "When you ask for substantially the same job several times, the agent offers to turn it into a schedule". "There is no repetition-detection engine and no new stored history." On confirmation the agent creates the job, runs it once as a visible test, and removes it if the test fails.
- Other triggers: webhooks ("Authenticated HTTP ingress, not an internal event hook"), the IMAP plugin ("Sender-gated isolated reader sessions"), MCP Events ("subscribed events, signed callbacks, and Automation runs") (https://docs.openclaw.ai/automation).

---

## 5. Limits and gaps the documentation itself states

**Trust model and multi-user limits**
- "OpenClaw is not a hostile multi-tenant security boundary for mutually adversarial users sharing one agent or gateway. For mixed-trust or adversarial-user operation, split trust boundaries: separate gateway + credentials, ideally separate OS users or hosts." (https://docs.openclaw.ai/gateway/security)
- "Everyone who can message a tool-enabled agent shares that agent's delegated tool authority." (https://docs.openclaw.ai/gateway/security/trust-model)
- "Session tools reach across the whole Gateway by default: `tools.sessions.visibility` defaults to `all` and `tools.agentToAgent.enabled` defaults to `true`, so any tool-enabled agent running unsandboxed can list, read, search, and message every agent's sessions, including other users' transcripts." (same page)
- "`sessionKey` (session IDs, labels) is a routing selector, not an authorization token." (same page)
- "Named operator roles bound what each teammate's connections can do; they are collaboration guardrails, not tenant isolation." (same page)
- "Exec approvals (allowlist + ask) are guardrails for operator intent, not hostile multi-tenant isolation. [...] Use sandboxing and host isolation for strong boundaries." (same page)
- "Trusted single-operator default: host exec on `gateway`/`node` is allowed without approval prompts (`security=\"full\"`, `ask=\"off\"`). That is intentional UX, not a vulnerability by itself." (same page)
- "Agents with message-tool access can send across conversations and channel providers by default." (https://docs.openclaw.ai/gateway/security)
- VISION.md: "A shared Gateway is for people who trust each other. Mutually untrusted users need separate Gateways, host or container isolation, and access controls."

**Sandboxing is off by default**
- "Sandboxing is off by default" (https://docs.openclaw.ai/gateway/sandboxing). "sandboxing is off by default in OpenClaw." (https://docs.openclaw.ai/start/why-openclaw)
- "Tools run on the host for the main session unless you configure sandboxing." (README)

**Exceptions to the conservative defaults**
- "container images default to an exposed bind (pair that with auth [...]), and a few workspace channels such as ClickClack trust workspace membership by default" (https://docs.openclaw.ai/gateway/security)

**Prompt injection**
- "Prompt injection does not require public DMs: even if only you can message the bot, any **untrusted content** it reads (web search/fetch results, browser pages, emails, docs, attachments, pasted logs/code) can carry adversarial instructions." (https://docs.openclaw.ai/gateway/security/prompt-injection)
- "Adaptive human attackers still break models that score well on static benchmarks, with published success rates above 80% against state-of-the-art defenses once the attacker adapts. And smaller or older models remain markedly easier to steer." (same page)
- "For tool-enabled agents or agents that read untrusted content, prompt-injection risk with older/smaller models is often too high. Do not run those workloads on weak model tiers." (same page)
- The page cites per-model attack success figures for Claude Opus 4.5, Sonnet 4.5, Haiku 4.5 and Gemini 2.5 Pro from "a 2026 crowdsourced arena". Possibly stale: these model generations are older than the page's last edit (2026-10-11), and the page does not date the study more precisely.
- The token sanitizer "does not replace `dmPolicy`, allowlists, exec approvals, sandboxing, or `contextVisibility` - it closes one specific tokenizer-layer bypass." (same page)
- The threat-model page states the stance: "1. **Identity first** [...] 2. **Scope next** [...] 3. **Model last** - assume the model can be manipulated; design so manipulation can cause only limited damage." (https://docs.openclaw.ai/gateway/security/trust-model)

**Security guidance (operator actions the docs prescribe)**
- Run `openclaw security audit`; "one command tells you if you have drifted" (https://docs.openclaw.ai/gateway/security).
- Use DM pairing or allowlists, mention gating and `contextVisibility` in groups; treat links and attachments as hostile; limit `exec`, `browser`, `web_fetch`, `web_search` to trusted agents; enable `tools.exec.strictInlineEval` when allowlisting interpreters; use a read-only "reader agent" for untrusted content; keep secrets out of prompts (https://docs.openclaw.ai/gateway/security/prompt-injection).
- Before any remote exposure, follow the exposure runbook (https://docs.openclaw.ai/gateway/security/exposure-runbook); README: read the security guide, exposure runbook and sandboxing guide "before connecting other users or exposing the Gateway remotely."
- Report vulnerabilities to security@openclaw.ai (https://docs.openclaw.ai/gateway/security/trust-model).

**Stability and change**
- "All OpenClaw plugin APIs are **experimental**." (https://docs.openclaw.ai/plugins/sdk-overview)
- Experimental flags: "Shape and behavior can change faster than stable config." (https://docs.openclaw.ai/concepts/experimental-features)
- The maturity scorecard rates the whole product "68%", level "Alpha", and lists three M1 Experimental surfaces (Voice Call channel, Nix install path, watchOS companion surfaces) (https://docs.openclaw.ai/maturity/scorecard).
- Config compatibility: "OpenClaw runtime code reads the current configuration schema only. We do not keep long-lived aliases or compatibility branches" (VISION.md).
- VISION.md: "We are still early, so iteration is fast."

**Removed features**
- "The shared Tasks ledger, TaskFlow orchestration API, and TaskFlow Webhooks plugin have been removed." (https://docs.openclaw.ai/automation)
- "The inferred commitments experiment was removed in v2026.8.1: OpenClaw no longer extracts follow-ups from conversations or delivers them through heartbeat." (same page)

**Session and delivery limits**
- "Multiple devices/channels can map to the same session, but history is not fully synced back to every client. Use one primary device for long conversations to avoid divergent context." (https://docs.openclaw.ai/concepts/messages)
- Debouncing "is a quiet-window heuristic, not a guarantee that every part of a long message will arrive in one turn." (same page)
- "Events are not replayed. Clients must refresh on gaps." (https://docs.openclaw.ai/concepts/architecture)
- Scheduled runs: "arbitrary interrupted tool effects are not guaranteed exactly once." (https://docs.openclaw.ai/automation/cron-jobs/how-it-works)
- Cloud workers: after Stop, "charges can continue during that interval." (https://docs.openclaw.ai/gateway/cloud-workers)

**What the project will not take (VISION.md)**
- "New core skills when they can live on ClawHub"; "Vendor-specific service integrations in core"; "Cloud-based sandbox providers as OpenClaw plugins; implement provider support in Crabbox instead"; "Heavy orchestration layers that duplicate existing agent and tool infrastructure". "This list is a roadmap guardrail, not a law of physics."

**Memory**
- "Memory is a special plugin slot where only one memory plugin can be active at a time. Today we ship multiple memory options; over time we plan to converge on one recommended default path." (VISION.md)

**Privacy defaults**
- "by default OpenClaw itself phones home for nothing but a daily version check, anonymous feature statistics are opt-in, and `update.checkOnStart: false` disables both" (README). VISION.md adds that update-outcome reports are on by default and "Feature-statistics opt-out and `DO_NOT_TRACK` do not disable these update requests."

---

## 6. Not found or not verified

- **A dated maintainer announcement of the renames.** I relied on the project's own lore page and VISION.md, plus GitHub redirects. I did not open the maintainers' X/Twitter posts from January 2026 that third-party articles cite. Search run: WebSearch "OpenClaw personal AI assistant Clawdbot Moltbot rename" (results were third-party news only).
- **The exact rename dates.** The lore page dates the Moltbot rename to January 27, 2026 and OpenClaw to January 30, 2026, but its "Great Molt" section also quotes "let's go with openclaw" on January 27. I could not settle this from a second primary source.
- **When "Warelay" was used.** VISION.md names it first; no docs page I read gives its dates. Searched: `grep -ri warelay` across `docs/`, README.md, VISION.md, CHANGELOG.md (only VISION.md matches); GitHub API shows `steipete/warelay` redirects to `openclaw/openclaw`.
- **The Node.js minimum.** The README and Getting Started say "Node 24.16.0+ on 24.x, or 26.1.0+"; the docs home page says "Node 26 (recommended), or another supported release: Node 24.22.1+ or Node 26.12.1+". The two disagree; I did not resolve which is enforced.
- **Who operates clawhub.ai.** Neither https://docs.openclaw.ai/clawhub nor https://docs.openclaw.ai/clawhub/how-it-works names the operator. The repo `openclaw/clawhub` ("Skill + Plugin Registry for OpenClaw", MIT) sits under the same GitHub organization. `[no-record: ClawHub operator statement; searched=docs.openclaw.ai/clawhub, /clawhub/how-it-works, openclaw/clawhub docs/ (clawhub.md, how-it-works.md)]`
- **The status of `v2026.9.37`.** GitHub shows it published 2026-11-10 but not marked Latest. I assume it belongs to the extended-stable line but did not confirm it from a release page.
- **Per-page dates for the 848 component entries.** I checked last-commit dates only for the 23 files quoted in sections 1, 3, 4 and 5 (all changed 2026-09-09 or later). The rest come from `main` at the commit above and were not dated one by one.
- **Scorecard levels for pages the scorecard does not link.** Many pages, especially under Reference, Install and Models, are not linked from any scorecard area. Those entries carry no scorecard status, and I did not infer one.
- **Similarly named projects (not inventoried).** WebSearch "OpenClaw fork alternative nanoclaw OR picoclaw OR zeroclaw github" returned separate projects: NanoClaw (qwibitai/nanoclaw), ZeroClaw (zeroclaw-labs/zeroclaw), PicoClaw (sipeed/picoclaw), nanobot (HKUDS/nanobot), plus IronClaw and others in third-party articles. They are separate codebases, not the project inventoried here; I did not verify their relationship to OpenClaw from their primary sources.
- **Translated docs.** `docs.json` lists only `en` as a navigation language; I did not look for other-language sites.
- **Hidden or unlisted pages.** The `docs/` folder holds 1,484 files, more than the navigation lists (for example `docs/refactor/`, `docs/specs/` and translations of assets). I followed the navigation only, as asked. Pages outside the navigation were not inventoried.
