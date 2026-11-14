---
title: "WARM v0.10 mapped onto OpenClaw"
date: 2026-11-11
type: platform-mapping
subject: OpenClaw (openclaw/openclaw, docs.openclaw.ai)
model: warm-model-v0.10.md
inventory: platform-mapping/inventory-openclaw.md
---

# WARM v0.10 mapped onto OpenClaw

**Purpose.** This file tests WARM against OpenClaw's own inventory of components. A forced fit is the worst error, so where a component did not fit a service's one-sentence responsibility, it is marked strained or MISFIT.

**Inputs.** WARM v0.10 (Steps 1 to 4 and the Glossary; the responsibility sentences in Step 3 are the definitions). The OpenClaw inventory (848 components: 664 navigation entries plus 184 plugins), compiled 2026-11-11 by a researcher who had not seen WARM. For steps 2 and 4 I also read the docs source in `github.com/openclaw/openclaw` (main branch, 2026-11-11) and searched the web. I did not read `predictions.md`.

**Method notes.**
- Each component has exactly one assignment: (a) one WARM service, (b) a layer that is not the platform, (c) BUILDER tooling, (d) SPANS, or (e) MISFIT. Confidence is "clear" or "strained"; a fit that needs more than one sentence of justification is strained.
- Tabs assigned one row per component: Get started, Agents, Capabilities (except the 12 search-provider pages), ClawHub, Gateway and Ops. The few non-provider pages in the Channels, Models, Install, Platforms and Reference tabs are also assigned one row each (they are not members of any named class). Everything else is assigned as a class with its count.
- Orientation pages ("Why OpenClaw", "Features", docs indexes) describe the product and add no capability. I put them under BUILDER so that every component is counted, and say so in each row.
- Plugins repeat many navigation pages (the Telegram page and the `telegram` plugin, for example). The inventory counts both, so this file does too.
- The Releases, Contributing and Help tabs are outside the inventory's 848 and outside this mapping.
- Page titles that contain an em dash are written here with a hyphen.

## Summary

| Assignment | Components | Of which strained | Rows |
|---|---|---|---|
| (a) One WARM service | 329 | 67 | 205 individual, 23 class |
| (b) A layer that is not the platform | 212 (Providers 182, Domains 18, Infrastructure 12, People 0) | 46 | 18 individual, 17 class |
| (c) BUILDER tooling | 256 | 1 | 102 individual, 9 class |
| (d) SPANS | 38 | n/a | 36 individual, 2 class |
| (e) MISFIT | 13 | n/a | 12 individual, 1 class |
| **Total** | **848** | **113 of 541 fits (a + b) are strained** | |

Within the tabs assigned one row per component (373 rows), the split is 205 service, 18 layer, 102 builder, 36 spans, 12 misfit.

Components per service (a only, counting class members): Human channels 109, Harness 25, Tools 25, Memory 22, Environments 22, Retrieval 15, Observability 15, Policy 14, Sessions 13, Secrets 11, Models 9, Identity 7, Registry 7, Scheduling 7, Evaluation 7, Messaging 6, Orchestration 4, Reliability 4, Releases 3, Artifacts 2, Approvals 1, Tasks 1. The low counts for Tasks and Approvals are partly an artifact of the method: most of their matches are SPANS rows (see the service table).

**Main findings, in short.**
1. Every one of the 22 services has at least one matching component, but four are PARTIAL: Tasks, Artifacts, Registry (the directory part) and Evaluation. No service is ABSENT.
2. Tasks is the sharpest challenge. OpenClaw built a shared Tasks ledger and a TaskFlow orchestration API, then removed both on 2026-09-27 because "The Tasks ledger duplicated execution and completion state already owned elsewhere" (PR #159179). Run tracking now lives with each runtime: the scheduler, the sub-agent lifecycle owner, the session controller.
3. The 13 misfits cluster into four responsibilities WARM does not have: admission and capacity control (who runs next, on shared capacity), agent provisioning (creating an agent and its identity), inbound interfaces for programs and outside agents, and governance of third-party extensions (a plugin host plus a moderated marketplace). Two single misfits stand alone: prospective memory (standing intents) and a shared coordination log across sessions.
4. OpenClaw has roles but no domains, and no directory of responsibilities. Work is routed by where a message came from (bindings), and a coordinator finds specialists by role text in its own instructions plus an `agents_list` tool. The platform also ships domain work as default plugins (Deep Research, Logbook, team reports).

## 1. Assignment tables

### 1.1 Individual rows


#### Get started

| Component | Assignment | Confidence | Why |
|---|---|---|---|
| [OpenClaw](https://docs.openclaw.ai/) | BUILDER | clear | Orientation or comparison page; describes the product, adds no capability. |
| [Why OpenClaw](https://docs.openclaw.ai/start/why-openclaw) | BUILDER | clear | Orientation or comparison page; describes the product, adds no capability. |
| [The trust boundary](https://docs.openclaw.ai/start/why-openclaw/the-trust-boundary) | SPANS: Environments + Policy + Secrets | clear | Defines where the trusted Gateway (policy, credentials) ends and isolated execution begins. |
| [Policy as code](https://docs.openclaw.ai/start/why-openclaw/policy-as-code) | SPANS: Policy + Approvals | clear | "Permission modes, tool policy, and exec approvals as code-enforced gates". |
| [Identity and roles](https://docs.openclaw.ai/start/why-openclaw/identity-and-roles) | SPANS: Identity + Policy | clear | Pairing establishes who; operator scopes and role ceilings decide what they may do. |
| [Secrets](https://docs.openclaw.ai/start/why-openclaw/secrets) | Secrets | clear | SecretRefs and a protected store; values resolved at use. |
| [Versioned state, guarded upgrades](https://docs.openclaw.ai/start/why-openclaw/versioned-state-guarded-upgrades) | SPANS: Releases + Reliability | strained | Schema-versioned state store plus guarded updates; the state store itself has no WARM service. |
| [Provenance](https://docs.openclaw.ai/start/why-openclaw/provenance) | Memory | clear | Origin classes and deletion boundaries for memory; WARM Memory records "where it came from". |
| [OpenClaw and Hermes Agent](https://docs.openclaw.ai/start/why-openclaw/openclaw-and-hermes-agent) | BUILDER | clear | Orientation or comparison page; describes the product, adds no capability. |
| [Features](https://docs.openclaw.ai/concepts/features) | BUILDER | clear | Orientation or comparison page; describes the product, adds no capability. |
| [Docs hubs](https://docs.openclaw.ai/start/hubs) | BUILDER | clear | Orientation or comparison page; describes the product, adds no capability. |
| [Docs directory](https://docs.openclaw.ai/start/docs-directory) | BUILDER | clear | Orientation or comparison page; describes the product, adds no capability. |
| [Getting started](https://docs.openclaw.ai/start/getting-started) | BUILDER | clear | Setup guide or onboarding interface for the person who installs the platform. |
| [Onboarding overview](https://docs.openclaw.ai/start/onboarding-overview) | BUILDER | clear | Setup guide or onboarding interface for the person who installs the platform. |
| [Onboarding (CLI)](https://docs.openclaw.ai/start/wizard) | BUILDER | clear | Setup guide or onboarding interface for the person who installs the platform. |
| [Onboarding (macOS app)](https://docs.openclaw.ai/start/onboarding) | BUILDER | clear | Setup guide or onboarding interface for the person who installs the platform. |
| [Personal assistant setup](https://docs.openclaw.ai/start/openclaw) | BUILDER | clear | Setup guide or onboarding interface for the person who installs the platform. |
| [Multiplayer](https://docs.openclaw.ai/start/multiplayer) | BUILDER | clear | Setup guide or onboarding interface for the person who installs the platform. |
| [CLI setup reference](https://docs.openclaw.ai/start/wizard-cli-reference) | BUILDER | clear | Setup guide or onboarding interface for the person who installs the platform. |
| [CLI automation](https://docs.openclaw.ai/start/wizard-cli-automation) | BUILDER | clear | Setup guide or onboarding interface for the person who installs the platform. |

#### Install

| Component | Assignment | Confidence | Why |
|---|---|---|---|
| [Backups](https://docs.openclaw.ai/install/backups) | Reliability | clear | State archives, snapshots and replication. |
| [Updating](https://docs.openclaw.ai/install/updating) | Releases | clear | Update with a rollback strategy. |
| [Update troubleshooting](https://docs.openclaw.ai/install/update-troubleshooting) | Releases | clear | Recover from a failed update. |
| [Migration guide](https://docs.openclaw.ai/install/migrating) | BUILDER | clear | Imports from other systems and machine moves. |
| [Uninstall](https://docs.openclaw.ai/install/uninstall) | BUILDER | clear | Removal. |
| [Release channels](https://docs.openclaw.ai/install/development-channels) | Releases | clear | Stable, extended-stable, beta, dev; pinning. |

#### Channels

| Component | Assignment | Confidence | Why |
|---|---|---|---|
| [Chat channels](https://docs.openclaw.ai/channels) | Human channels | clear | Overview of messaging platforms. |
| [A2A](https://docs.openclaw.ai/channels/a2a) | Messaging | clear | Agent-to-agent protocol channel. |
| [Raft](https://docs.openclaw.ai/channels/raft) | Messaging | strained | Wake bridge to an external agent through a CLI. |
| [Reef](https://docs.openclaw.ai/channels/reef) | Messaging | clear | Encrypted messaging "between OpenClaw agents of different people": crosses owners, which WARM Messaging does not mention. |
| [Pairing](https://docs.openclaw.ai/channels/pairing) | SPANS: Identity + Approvals | clear | "Explicit access approval step" for DM senders and nodes. |
| [Access groups](https://docs.openclaw.ai/channels/access-groups) | Policy | clear | Reusable sender allowlists. |
| [Bot loop protection](https://docs.openclaw.ai/channels/bot-loop-protection) | Policy | strained | Limits bot-to-bot loops on channels. |
| [Groups](https://docs.openclaw.ai/channels/groups) | Human channels | clear | Channel behavior. |
| [WhatsApp group messages](https://docs.openclaw.ai/channels/group-messages) | Human channels | clear | Channel behavior. |
| [Ambient room events](https://docs.openclaw.ai/channels/ambient-room-events) | Human channels | strained | Rooms supply quiet context unless the agent chooses to send. |
| [Broadcast groups](https://docs.openclaw.ai/channels/broadcast-groups) | Orchestration | clear | Several agents on the same inbound message, in bounded group threads. |
| [Channel routing](https://docs.openclaw.ai/channels/channel-routing) | Human channels | strained | Picks one agent and session per inbound message by fixed rules; routing by origin, not by responsibility. |
| [Channel location parsing](https://docs.openclaw.ai/channels/location) | Human channels | clear | Channel behavior. |
| [Channel troubleshooting](https://docs.openclaw.ai/channels/troubleshooting) | BUILDER | clear | Troubleshooting. |

#### Agents

| Component | Assignment | Confidence | Why |
|---|---|---|---|
| [Gateway architecture](https://docs.openclaw.ai/concepts/architecture) | SPANS: Sessions + Human channels + Tools + Scheduling + Identity | strained | The Gateway is one control-plane process that owns sessions, channels, tools and events; WARM has no service for the process that owns the others. |
| [Agent runtime](https://docs.openclaw.ai/concepts/agent) | Harness | clear | Context assembly, the model loop, or what stays in the context window. |
| [Agent loop](https://docs.openclaw.ai/concepts/agent-loop) | Harness | clear | Context assembly, the model loop, or what stays in the context window. |
| [Agent runtimes](https://docs.openclaw.ai/concepts/agent-runtimes) | Harness | clear | Context assembly, the model loop, or what stays in the context window. |
| [System prompt](https://docs.openclaw.ai/concepts/system-prompt) | Harness | clear | Context assembly, the model loop, or what stays in the context window. |
| [Context](https://docs.openclaw.ai/concepts/context) | Harness | clear | Context assembly, the model loop, or what stays in the context window. |
| [Context engine](https://docs.openclaw.ai/concepts/context-engine) | Harness | clear | Context assembly, the model loop, or what stays in the context window. |
| [SOUL.md personality guide](https://docs.openclaw.ai/concepts/soul) | Domains (layer) | strained | Persona and voice file; WARM's agent definition has role, instructions and skills but no persona. |
| [Agent workspace](https://docs.openclaw.ai/concepts/agent-workspace) | SPANS: Environments + Memory | clear | "The working directory used for file tools ... treat it as memory." |
| [Managed worktrees](https://docs.openclaw.ai/concepts/managed-worktrees) | Environments | clear | Isolated git checkout per agent task. |
| [Storage locations](https://docs.openclaw.ai/concepts/storage-locations) | SPANS: Artifacts + Reliability | strained | Named, encrypted storage destinations used for artifacts and backups; each consumer decides retention. |
| [OAuth](https://docs.openclaw.ai/concepts/oauth) | Secrets | strained | Stores provider sign-ins (tokens) per account; also feeds model account rotation. |
| [Agent bootstrapping](https://docs.openclaw.ai/start/bootstrapping) | MISFIT | n/a | First-run ritual in which a new agent picks its own identity; agent provisioning has no WARM service (Registry holds definitions but nothing creates them). |
| [Experimental features](https://docs.openclaw.ai/concepts/experimental-features) | BUILDER | clear | Config flags for preview surfaces. |
| [The main session](https://docs.openclaw.ai/concepts/main-session) | Sessions | clear | "One rolling conversation across all your channels." |
| [Multi-user mode](https://docs.openclaw.ai/concepts/multi-user) | SPANS: Sessions + Identity | clear | Session ownership, participant history and presence for several people on one agent. |
| [Session management](https://docs.openclaw.ai/concepts/session) | Sessions | clear | Gateway-owned session state and session keys. |
| [Session controller](https://docs.openclaw.ai/concepts/session-controller) | MISFIT | n/a | Decides "which turn may use a session next" with admission barriers; admission and capacity control has no WARM service. |
| [Session synchronization and attachment](https://docs.openclaw.ai/concepts/session-attachment) | Sessions | clear | Gateway-owned session continued across clients and harnesses. |
| [Session search](https://docs.openclaw.ai/concepts/session-search) | Retrieval | clear | Searches past session transcripts as a named source. |
| [Session pruning](https://docs.openclaw.ai/concepts/session-pruning) | Harness | clear | Context assembly, the model loop, or what stays in the context window. |
| [Session state awareness](https://docs.openclaw.ai/concepts/session-state) | MISFIT | n/a | Durable state-version log, watchers and stale-state notices shared by several sessions working one problem; a coordination blackboard that is neither Sessions nor Messaging. |
| [Session tools](https://docs.openclaw.ai/concepts/session-tool) | SPANS: Sessions + Messaging + Orchestration | clear | Tools for session creation, cross-session messaging and sub-agent orchestration. |
| [Memory overview](https://docs.openclaw.ai/concepts/memory) | Memory | clear | Durable learned memory, its backends, provenance or consolidation. |
| [Memory architecture](https://docs.openclaw.ai/concepts/memory-architecture) | Memory | clear | Durable learned memory, its backends, provenance or consolidation. |
| [Memory provenance and deletion](https://docs.openclaw.ai/concepts/memory-provenance) | Memory | clear | Durable learned memory, its backends, provenance or consolidation. |
| [User model](https://docs.openclaw.ai/concepts/user-model) | Memory | clear | Durable learned memory, its backends, provenance or consolidation. |
| [Standing intents](https://docs.openclaw.ai/concepts/standing-intents) | MISFIT | n/a | Stored event-conditioned future actions ("when X is mentioned, remind me"); prospective memory is none of WARM's three memory kinds, and it does not start work as Scheduling does. |
| [Builtin memory engine](https://docs.openclaw.ai/concepts/memory-builtin) | Memory | clear | Durable learned memory, its backends, provenance or consolidation. |
| [Honcho memory](https://docs.openclaw.ai/concepts/memory-honcho) | Memory | clear | Durable learned memory, its backends, provenance or consolidation. |
| [Memory search](https://docs.openclaw.ai/concepts/memory-search) | SPANS: Memory + Retrieval | clear | Hybrid search over memory files: WARM separates learned memory from looked-up material, this crosses that line. |
| [Active memory](https://docs.openclaw.ai/concepts/active-memory) | Memory | strained | A blocking recall sub-agent that injects memories before a reply; also a Harness context decision. |
| [Dreaming](https://docs.openclaw.ai/concepts/dreaming) | Memory | clear | Durable learned memory, its backends, provenance or consolidation. |
| [Compaction](https://docs.openclaw.ai/concepts/compaction) | Harness | clear | Context assembly, the model loop, or what stays in the context window. |
| [Multi-agent routing](https://docs.openclaw.ai/concepts/multi-agent) | SPANS: Human channels + Registry | strained | Isolated agents plus bindings that decide which agent answers; WARM keeps "which agent to reach" in the Registry directory, keyed by responsibility, not by channel. |
| [Agent bindings](https://docs.openclaw.ai/concepts/agent-bindings) | Human channels | strained | Maps channel accounts and peers to agents: a routing table keyed by where the message came from. |
| [Parallel specialist lanes](https://docs.openclaw.ai/concepts/parallel-specialist-lanes) | MISFIT | n/a | Treats parallelism across agents as "a scarce-resource design problem"; capacity planning across shared model and tool capacity has no WARM service. |
| [Presence](https://docs.openclaw.ai/concepts/presence) | Observability | strained | Best-effort view of connected clients and nodes. |
| [Delegate architecture](https://docs.openclaw.ai/concepts/delegate-architecture) | Identity | clear | An agent "with its own identity that acts on behalf of" people. |
| [Messages](https://docs.openclaw.ai/concepts/messages) | Human channels | strained | Inbound routing, dedupe, queueing and outbound delivery in one pipeline. |
| [Streaming and chunking](https://docs.openclaw.ai/concepts/streaming) | Human channels | clear | How a reply appears on the person's channel. |
| [Typing indicators](https://docs.openclaw.ai/concepts/typing-indicators) | Human channels | clear | How a reply appears on the person's channel. |
| [Progress drafts](https://docs.openclaw.ai/concepts/progress-drafts) | Human channels | clear | How a reply appears on the person's channel. |
| [Retry policy](https://docs.openclaw.ai/concepts/retry) | Reliability | strained | Retries for outbound channel sends and model requests (call-level, not task-level retry). |
| [Command queue](https://docs.openclaw.ai/concepts/queue) | MISFIT | n/a | Serializes inbound runs and shares background capacity; same admission and capacity gap as the session controller. |
| [Steering queue](https://docs.openclaw.ai/concepts/queue-steering) | Harness | strained | Injects a new prompt into an active run, including during tool execution. |

#### Capabilities

| Component | Assignment | Confidence | Why |
|---|---|---|---|
| [Overview](https://docs.openclaw.ai/tools) | BUILDER | clear | Index page for tools, skills and plugins. |
| [Plugins](https://docs.openclaw.ai/tools/plugin) | MISFIT | n/a | The plugin host loads implementations of almost every service (channels, providers, harnesses, memory slot); WARM treats implementations as outside the model (Step 5) and has no service that installs and swaps them. |
| [Manage plugins](https://docs.openclaw.ai/plugins/manage-plugins) | BUILDER | clear | Operator interface to install, enable and remove plugins. |
| [Community plugins](https://docs.openclaw.ai/plugins/community) | Registry | strained | Discovery of third-party plugins through ClawHub. |
| [Plugin bundles](https://docs.openclaw.ai/plugins/bundles) | Registry | strained | Imports Codex, Claude and Cursor bundles as plugins. |
| [Agent Guidance](https://docs.openclaw.ai/plugins/agent-guidance) | Registry | strained | Operator-managed instruction files shared across selected agents; part of the agent definition, written by the operator, not a domain. |
| [Agents API](https://docs.openclaw.ai/plugins/agentsapi) | Harness | clear | Replaces the built-in loop with a vendor harness while OpenClaw keeps channels, sessions, policy and state. |
| [Codex Computer Use](https://docs.openclaw.ai/plugins/codex-computer-use) | Environments | clear | Desktop control for Codex-mode agents. |
| [Codex harness](https://docs.openclaw.ai/plugins/codex-harness) | Harness | clear | Replaces the built-in loop with a vendor harness while OpenClaw keeps channels, sessions, policy and state. |
| [Native Codex plugins](https://docs.openclaw.ai/plugins/codex-native-plugins) | Tools | clear | Codex app-server tools inside the Codex thread. |
| [Supervise Codex sessions](https://docs.openclaw.ai/plugins/codex-supervision) | Sessions | strained | Browses native Codex sessions on paired computers. |
| [Codex supervision](https://docs.openclaw.ai/specs/codex-supervision) | Sessions | strained | Spec for discovering and continuing native Codex sessions. |
| [Copilot SDK harness](https://docs.openclaw.ai/plugins/copilot) | Harness | clear | Replaces the built-in loop with a vendor harness while OpenClaw keeps channels, sessions, policy and state. |
| [Muse Code agent runtime](https://docs.openclaw.ai/plugins/muse) | Harness | clear | Replaces the built-in loop with a vendor harness while OpenClaw keeps channels, sessions, policy and state. |
| [Meeting plugins](https://docs.openclaw.ai/plugins/meeting-plugins) | Human channels | clear | A surface on which a person talks with the agent (meeting, call or chat). |
| [FaceTime plugin](https://docs.openclaw.ai/plugins/facetime) | Human channels | clear | A surface on which a person talks with the agent (meeting, call or chat). |
| [FaceTime recovery and removal](https://docs.openclaw.ai/plugins/facetime-recovery) | BUILDER | clear | Operator removal procedure. |
| [Google Meet plugin](https://docs.openclaw.ai/plugins/google-meet) | Human channels | clear | A surface on which a person talks with the agent (meeting, call or chat). |
| [Microsoft Teams meetings plugin](https://docs.openclaw.ai/plugins/teams-meetings) | Human channels | clear | A surface on which a person talks with the agent (meeting, call or chat). |
| [Slack huddles plugin](https://docs.openclaw.ai/plugins/slack-huddles) | Human channels | clear | A surface on which a person talks with the agent (meeting, call or chat). |
| [Voice call plugin](https://docs.openclaw.ai/plugins/voice-call) | Human channels | clear | A surface on which a person talks with the agent (meeting, call or chat). |
| [Zoom meetings plugin](https://docs.openclaw.ai/plugins/zoom-meetings) | Human channels | clear | A surface on which a person talks with the agent (meeting, call or chat). |
| [Apple Foundation Models](https://docs.openclaw.ai/plugins/apple-fm) | Providers (layer) | clear | A model source the platform calls. |
| [Knowledge](https://docs.openclaw.ai/plugins/knowledge) | Memory | clear | Durable knowledge or procedural memory (skills) and how it is written. |
| [llama.cpp Provider](https://docs.openclaw.ai/plugins/llama-cpp) | Providers (layer) | clear | A model source the platform calls. |
| [Memory LanceDB](https://docs.openclaw.ai/plugins/memory-lancedb) | Memory | clear | Durable knowledge or procedural memory (skills) and how it is written. |
| [Memory wiki](https://docs.openclaw.ai/plugins/memory-wiki) | Memory | clear | Durable knowledge or procedural memory (skills) and how it is written. |
| [Local ONNX decision models](https://docs.openclaw.ai/plugins/onnx) | Models | clear | A local classifier behind the decision-model role. |
| [SubQ](https://docs.openclaw.ai/plugins/subq) | Providers (layer) | clear | A model source the platform calls. |
| [TypeSafe AI](https://docs.openclaw.ai/plugins/typesafe) | Providers (layer) | clear | A model source the platform calls. |
| [1Password plugin](https://docs.openclaw.ai/plugins/onepassword) | Secrets | clear | Resolves SecretRefs from an external vault. |
| [Vault SecretRefs](https://docs.openclaw.ai/plugins/vault) | Secrets | clear | Resolves SecretRefs from an external vault. |
| [Admin HTTP RPC plugin](https://docs.openclaw.ai/plugins/admin-http-rpc) | BUILDER | clear | Control-plane methods over HTTP for host automation. |
| [Beam plugin](https://docs.openclaw.ai/plugins/beam) | Sessions | strained | Publishes coding-session snapshots for shared viewing. |
| [Cloudflare](https://docs.openclaw.ai/plugins/cloudflare) | Infrastructure (layer) | clear | R2 bucket as a storage location. |
| [Geolocation plugin](https://docs.openclaw.ai/plugins/geolocation) | Observability | strained | Coarse city for a connecting client IP. |
| [Logbook plugin](https://docs.openclaw.ai/plugins/logbook) | Domains (layer) | strained | Work journal built from screen snapshots of the person's activity: meaning for one area of work, shipped as a platform plugin. |
| [MCP Relay](https://docs.openclaw.ai/plugins/mcp-relay) | MISFIT | n/a | Lets ChatGPT, Codex and Claude connect into the Gateway as MCP clients; an inbound interface for outside agents and apps is neither Messaging (between this platform's agents) nor Human channels. |
| [OC Path plugin](https://docs.openclaw.ai/plugins/oc-path) | BUILDER | clear | CLI for oc:// workspace addressing. |
| [Session Share plugin](https://docs.openclaw.ai/plugins/session-share) | Sessions | strained | Read-only sessions shared with a paired team Gateway. |
| [Workboard plugin](https://docs.openclaw.ai/plugins/workboard) | SPANS: Tasks + Orchestration | clear | Kanban cards assigned to agents, linked to task, run and session, and dispatched to worker runs: the backlog way of starting work. |
| [Zalo personal plugin](https://docs.openclaw.ai/plugins/zalouser) | Human channels | clear | A surface on which a person talks with the agent (meeting, call or chat). |
| [Building plugins](https://docs.openclaw.ai/plugins/building-plugins) | BUILDER | clear | Builder guide, reference, troubleshooting, or CLI entry point. |
| [Plugin runtime compatibility](https://docs.openclaw.ai/plugins/runtime-compatibility) | BUILDER | clear | Builder guide, reference, troubleshooting, or CLI entry point. |
| [Feature plugins](https://docs.openclaw.ai/plugins/feature-plugins) | BUILDER | clear | Builder guide, reference, troubleshooting, or CLI entry point. |
| [Tool plugins](https://docs.openclaw.ai/plugins/tool-plugins) | BUILDER | clear | Builder guide, reference, troubleshooting, or CLI entry point. |
| [Building channel plugins](https://docs.openclaw.ai/plugins/sdk-channel-plugins) | BUILDER | clear | Builder guide, reference, troubleshooting, or CLI entry point. |
| [Building provider plugins](https://docs.openclaw.ai/plugins/sdk-provider-plugins) | BUILDER | clear | Builder guide, reference, troubleshooting, or CLI entry point. |
| [Building CLI backend plugins](https://docs.openclaw.ai/plugins/cli-backend-plugins) | BUILDER | clear | Builder guide, reference, troubleshooting, or CLI entry point. |
| [Plugin hooks](https://docs.openclaw.ai/plugins/hooks) | SPANS: Policy + Observability | clear | Typed handlers that can block or change runs and tool calls, or only observe them. |
| [Plugin permission requests](https://docs.openclaw.ai/plugins/plugin-permission-requests) | Approvals | clear | Pauses a plugin tool call until a user approves. |
| [Adding capabilities (contributor guide)](https://docs.openclaw.ai/plugins/adding-capabilities) | BUILDER | clear | Builder guide, reference, troubleshooting, or CLI entry point. |
| [Skills](https://docs.openclaw.ai/tools/skills) | SPANS: Memory + Registry | clear | Skill files (procedural memory) plus loading, precedence and gating (index and load). |
| [Custodian skills](https://docs.openclaw.ai/tools/custodian-skills) | Memory | strained | Release-versioned operational skills visible only to the system agent; procedural memory written by the project, for a platform agent. |
| [Skill Workshop](https://docs.openclaw.ai/tools/skill-workshop) | Memory | clear | Durable knowledge or procedural memory (skills) and how it is written. |
| [Personal library authoring](https://docs.openclaw.ai/tools/skill-workshop/personal-library) | Memory | clear | Durable knowledge or procedural memory (skills) and how it is written. |
| [Self-learning](https://docs.openclaw.ai/tools/self-learning) | Memory | clear | Durable knowledge or procedural memory (skills) and how it is written. |
| [Creating skills](https://docs.openclaw.ai/tools/creating-skills) | BUILDER | clear | Builder guide, reference, troubleshooting, or CLI entry point. |
| [Skills config](https://docs.openclaw.ai/tools/skills-config) | BUILDER | clear | Builder guide, reference, troubleshooting, or CLI entry point. |
| [Slash commands](https://docs.openclaw.ai/tools/slash-commands) | Human channels | clear | Commands a person sends on a channel. |
| [Automation](https://docs.openclaw.ai/automation) | SPANS: Scheduling + Orchestration + Policy | clear | Overview of automations, Lobster workflows, hooks and standing orders. |
| [Heartbeat migration](https://docs.openclaw.ai/gateway/heartbeat) | Scheduling | clear | Converts heartbeat monitors into ordinary scheduled jobs. |
| [Automations](https://docs.openclaw.ai/automation/cron-jobs) | Scheduling | strained | The scheduler also persists each job's run history and delivery, which WARM gives to Tasks and Human channels. |
| [IMAP email trigger](https://docs.openclaw.ai/automation/imap) | Scheduling | clear | An event starts an isolated restricted reader agent (a job). |
| [MCP Events](https://docs.openclaw.ai/automation/mcp-events) | Scheduling | clear | Signed webhook events start automations. |
| [Standing orders](https://docs.openclaw.ai/automation/standing-orders) | Domains (layer) | strained | "Permanent operating authority for defined programs" written into AGENTS.md: a role's responsibilities, held in the agent's file rather than in a directory. |
| [Hooks](https://docs.openclaw.ai/automation/hooks) | Scheduling | strained | Scripts started by lifecycle events; they do side effects, not agent work. |
| [apply_patch tool](https://docs.openclaw.ai/tools/apply-patch) | Tools | clear | A callable tool or tool connection. |
| [Code execution](https://docs.openclaw.ai/tools/code-execution) | Tools | clear | A callable tool or tool connection. |
| [Diffs](https://docs.openclaw.ai/tools/diffs) | Tools | clear | A callable tool or tool connection. |
| [Elevated mode](https://docs.openclaw.ai/tools/elevated) | Policy | clear | A gated exception that lets sandboxed exec run outside the sandbox. |
| [Exec tool](https://docs.openclaw.ai/tools/exec) | Tools | clear | A callable tool or tool connection. |
| [Exec approvals](https://docs.openclaw.ai/tools/exec-approvals) | SPANS: Policy + Approvals | clear | "policy + allowlist + (optional) user approval". |
| [Exec approvals - advanced](https://docs.openclaw.ai/tools/exec-approvals-advanced) | SPANS: Policy + Approvals | clear | Safe-bin fast path (policy) and approval forwarding to chat (approvals). |
| [Permission modes](https://docs.openclaw.ai/tools/permission-modes) | Policy | clear | How much authority an agent has before host commands. |
| [Secrets](https://docs.openclaw.ai/tools/secrets) | Secrets | clear | Agent requests a credential it never sees; the value goes straight to the store. |
| [Media overview](https://docs.openclaw.ai/tools/media-overview) | Tools | clear | A callable tool or tool connection. |
| [Image generation](https://docs.openclaw.ai/tools/image-generation) | Tools | clear | A callable tool or tool connection. |
| [Music generation](https://docs.openclaw.ai/tools/music-generation) | Tools | clear | A callable tool or tool connection. |
| [PDF tool](https://docs.openclaw.ai/tools/pdf) | Tools | clear | A callable tool or tool connection. |
| [Text-to-speech](https://docs.openclaw.ai/tools/tts) | Human channels | clear | Converts outbound replies into voice messages. |
| [Video generation](https://docs.openclaw.ai/tools/video-generation) | Tools | clear | A callable tool or tool connection. |
| [Code Mode](https://docs.openclaw.ai/tools/code-mode) | SPANS: Harness + Tools | clear | The model writes code against tools instead of seeing every tool schema. |
| [Auto Review](https://docs.openclaw.ai/tools/autoreview) | Evaluation | clear | Rechecks repository changes in the sandbox with a reviewer. |
| [LLM task](https://docs.openclaw.ai/tools/llm-task) | Tools | clear | A callable tool or tool connection. |
| [Lobster](https://docs.openclaw.ai/tools/lobster) | SPANS: Orchestration + Approvals + Tasks | clear | Typed multi-step pipelines with approval gates and resume tokens. |
| [Connect MCP servers](https://docs.openclaw.ai/tools/mcp) | Tools | clear | A callable tool or tool connection. |
| [Tool Search](https://docs.openclaw.ai/tools/tool-search) | Registry | clear | Discover and load tools from a large catalog when needed. |
| [Tool-loop detection](https://docs.openclaw.ai/tools/loop-detection) | Policy | strained | Blocks a repeated failing tool call; a guardrail inside the loop. |
| [Thinking levels](https://docs.openclaw.ai/tools/thinking) | Models | strained | Reasoning-effort directives per request. |
| [Tokenjuice](https://docs.openclaw.ai/tools/tokenjuice) | Harness | clear | Compacts noisy tool results before they fill context. |
| [Trajectory bundles](https://docs.openclaw.ai/tools/trajectory) | Observability | clear | "Per-session flight recorder." |
| [Ask user](https://docs.openclaw.ai/tools/ask-user) | Human channels | clear | Structured questions to the person; decisions, not authorization of an action. |
| [BTW side questions](https://docs.openclaw.ai/tools/btw) | Human channels | strained | Side question that is kept out of session history. |
| [Progress card](https://docs.openclaw.ai/tools/progress-card) | Sessions | strained | Durable plan and status card for one session. |
| [Reactions](https://docs.openclaw.ai/tools/reactions) | Human channels | clear | Emoji reactions on the channel. |
| [Screen](https://docs.openclaw.ai/tools/screen) | Human channels | strained | Agent arranges the operator's Control UI. |
| [Show widget](https://docs.openclaw.ai/tools/show-widget) | Human channels | strained | HTML widget on the person's surface, optionally pinned to a dashboard (an artifact). |
| [Theme](https://docs.openclaw.ai/tools/theme) | Human channels | strained | Agent selects the UI theme. |
| [Browser (OpenClaw-managed)](https://docs.openclaw.ai/tools/browser) | Environments | clear | A browser the agent acts in. |
| [Browser control API](https://docs.openclaw.ai/tools/browser-control) | Environments | clear | A browser the agent acts in. |
| [Browser troubleshooting](https://docs.openclaw.ai/tools/browser-linux-troubleshooting) | BUILDER | clear | Builder guide, reference, troubleshooting, or CLI entry point. |
| [Browser login](https://docs.openclaw.ai/tools/browser-login) | Environments | strained | A person signs in manually in the agent's browser profile. |
| [WSL2 + Windows + remote Chrome CDP troubleshooting](https://docs.openclaw.ai/tools/browser-wsl2-windows-remote-cdp-troubleshooting) | BUILDER | clear | Builder guide, reference, troubleshooting, or CLI entry point. |
| [Chrome Extension](https://docs.openclaw.ai/tools/chrome-extension) | Environments | clear | A browser the agent acts in. |
| [Firecrawl](https://docs.openclaw.ai/tools/firecrawl) | Retrieval | clear | Fetches material from the web. |
| [Web fetch](https://docs.openclaw.ai/tools/web-fetch) | Retrieval | clear | Fetches material from the web. |
| [Web search](https://docs.openclaw.ai/tools/web) | Retrieval | clear | Fetches material from the web. |
| [Deep Research](https://docs.openclaw.ai/tools/deep-research) | Domains (layer) | strained | "Source-backed findings and explicit gaps": by WARM's test this applies judgment, so it is research-domain work, shipped as a default platform plugin. |
| [Agent send](https://docs.openclaw.ai/tools/agent-send) | BUILDER | clear | Builder guide, reference, troubleshooting, or CLI entry point. |
| [Goal](https://docs.openclaw.ai/tools/goal) | Tasks | strained | One durable objective per session with a token budget. |
| [Steer](https://docs.openclaw.ai/tools/steer) | Harness | strained | Adjusts an active run. |
| [Sub-agents](https://docs.openclaw.ai/tools/subagents) | Orchestration | clear | Spawned background runs that announce results to the requester. |
| [Swarm](https://docs.openclaw.ai/tools/swarm) | Orchestration | clear | Bounded fan-out of sub-agents with structured results. |
| [ACP agents](https://docs.openclaw.ai/tools/acp-agents) | Orchestration | strained | Runs external coding harnesses as delegated sessions; the ACP runtime owns each session and its cancellation. |
| [ACP agents - setup](https://docs.openclaw.ai/tools/acp-agents-setup) | BUILDER | clear | Builder guide, reference, troubleshooting, or CLI entry point. |
| [Multi-agent sandbox and tools](https://docs.openclaw.ai/tools/multi-agent-sandbox-tools) | Policy | clear | Per-agent sandbox and tool restrictions. |

#### ClawHub

| Component | Assignment | Confidence | Why |
|---|---|---|---|
| [ClawHub](https://docs.openclaw.ai/clawhub) | Registry | clear | "The public registry for OpenClaw skills and plugins." |
| [Quickstart](https://docs.openclaw.ai/clawhub/quickstart) | BUILDER | clear | Builder or publisher interface and reference. |
| [How ClawHub Works](https://docs.openclaw.ai/clawhub/how-it-works) | Registry | clear | Listings, versions, installs and scans. |
| [CLI](https://docs.openclaw.ai/clawhub/cli) | BUILDER | clear | Builder or publisher interface and reference. |
| [Publishing](https://docs.openclaw.ai/clawhub/publishing) | SPANS: Registry + Releases | clear | Publishing a versioned release of a skill or plugin into the registry. |
| [Skill format](https://docs.openclaw.ai/clawhub/skill-format) | BUILDER | clear | Builder or publisher interface and reference. |
| [Auth](https://docs.openclaw.ai/clawhub/auth) | Identity | strained | Publisher sign-in and API tokens for the hosted registry. |
| [Telemetry](https://docs.openclaw.ai/clawhub/telemetry) | Observability | strained | Install counts collected by the registry CLI. |
| [Troubleshooting](https://docs.openclaw.ai/clawhub/troubleshooting) | BUILDER | clear | Builder or publisher interface and reference. |
| [API v1](https://docs.openclaw.ai/clawhub/api) | BUILDER | clear | Builder or publisher interface and reference. |
| [HTTP API](https://docs.openclaw.ai/clawhub/http-api) | BUILDER | clear | Builder or publisher interface and reference. |
| [Acceptable Usage](https://docs.openclaw.ai/clawhub/acceptable-usage) | MISFIT | n/a | Marketplace content policy for a public registry; governance of a third-party supply chain has no WARM service (Policy evaluates actions, not what may be published). |
| [Moderation and Account Safety](https://docs.openclaw.ai/clawhub/moderation) | MISFIT | n/a | Reports, holds, hidden listings and bans on a public marketplace; same supply-chain governance gap. |
| [Security Audits](https://docs.openclaw.ai/clawhub/security-audits) | Evaluation | strained | Judges a third-party release before install (what it does, what authority it asks for); evaluates components, not agents' work. |

#### Models

| Component | Assignment | Confidence | Why |
|---|---|---|---|
| [Provider directory](https://docs.openclaw.ai/providers) | BUILDER | clear | Index of providers. |
| [Model provider quickstart](https://docs.openclaw.ai/providers/models) | BUILDER | clear | Setup guide. |
| [Models CLI](https://docs.openclaw.ai/concepts/models) | Models | clear | Resolves model refs, aliases and auth-profile rotation. |
| [Recommended models](https://docs.openclaw.ai/concepts/recommended-models) | Models | strained | Project-curated list that guides model choice. |
| [Decision models](https://docs.openclaw.ai/concepts/decision-models) | Models | clear | A separate model role for typed judgments; still "choose the model for each task". |
| [Model providers](https://docs.openclaw.ai/concepts/model-providers) | Models | clear | Provider rules and bundled provider plugins. |
| [Model failover](https://docs.openclaw.ai/concepts/model-failover) | Models | clear | Rotates auth profiles and falls back across models. |

#### Platforms

| Component | Assignment | Confidence | Why |
|---|---|---|---|
| [HealthKit summaries](https://docs.openclaw.ai/platforms/ios-healthkit) | Tools | strained | Privacy-gated health data from an iOS node; a data connector most useful to one domain (health). |
| [Peekaboo bridge](https://docs.openclaw.ai/platforms/mac/peekaboo) | Environments | clear | macOS UI automation. |

#### Gateway & Ops

| Component | Assignment | Confidence | Why |
|---|---|---|---|
| [Gateway runbook](https://docs.openclaw.ai/gateway) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration](https://docs.openclaw.ai/gateway/configuration) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration reference](https://docs.openclaw.ai/gateway/configuration-reference) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration - agents](https://docs.openclaw.ai/gateway/config-agents) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration - automations and media template variables](https://docs.openclaw.ai/gateway/config-automation) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration - browser, UI, and desktop](https://docs.openclaw.ai/gateway/config-browser-ui-desktop) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration - channels](https://docs.openclaw.ai/gateway/config-channels) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration - cloud worker environments](https://docs.openclaw.ai/gateway/config-cloud-workers) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration - MCP, skills, and plugins](https://docs.openclaw.ai/gateway/config-extensions) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration - gateway](https://docs.openclaw.ai/gateway/config-gateway) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration - hooks](https://docs.openclaw.ai/gateway/config-hooks) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration - audit, logging, diagnostics, and telemetry](https://docs.openclaw.ai/gateway/config-observability) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration - runtime basics](https://docs.openclaw.ai/gateway/config-runtime) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration - environment, secrets, and includes](https://docs.openclaw.ai/gateway/config-secrets-env) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration - tools and custom providers](https://docs.openclaw.ai/gateway/config-tools) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Configuration examples](https://docs.openclaw.ai/gateway/configuration-examples) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Authentication](https://docs.openclaw.ai/gateway/authentication) | Secrets | strained | Model-provider credentials (API keys, OAuth, CLI reuse). |
| [Auth credential semantics](https://docs.openclaw.ai/auth-credential-semantics) | Secrets | strained | Rules for which stored credential is eligible at selection and run time. |
| [Secrets management](https://docs.openclaw.ai/gateway/secrets) | Secrets | clear | SecretRef contract, shared store, runtime snapshots. |
| [1Password](https://docs.openclaw.ai/gateway/1password) | Secrets | clear | 1Password as a secrets source. |
| [Secrets apply plan contract](https://docs.openclaw.ai/gateway/secrets-plan-contract) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Trusted proxy auth](https://docs.openclaw.ai/gateway/trusted-proxy-auth) | Identity | clear | A reverse proxy authenticates users. |
| [Health checks](https://docs.openclaw.ai/gateway/health) | Reliability | clear | Gateway and channel health checks and uptime monitoring. |
| [PostgreSQL operator guide](https://docs.openclaw.ai/gateway/postgresql) | Infrastructure (layer) | clear | Database backend for the Gateway (listed twice in the nav). |
| [Doctor](https://docs.openclaw.ai/gateway/doctor) | SPANS: Reliability + Releases | clear | Repairs stale state and runs config and data migrations. |
| [Audit history](https://docs.openclaw.ai/gateway/audit) | Observability | clear | Metadata-only ledger: which agent ran, when, how it ended; decision receipts. |
| [Usage telemetry and update checks](https://docs.openclaw.ai/gateway/telemetry) | SPANS: Observability + Releases | clear | Phone-home update checks and opt-in feature statistics. |
| [Logging](https://docs.openclaw.ai/logging) | Observability | clear | Logs, metrics, traces or diagnostic bundles. |
| [OpenTelemetry export](https://docs.openclaw.ai/gateway/opentelemetry) | Observability | clear | Logs, metrics, traces or diagnostic bundles. |
| [Prometheus metrics](https://docs.openclaw.ai/gateway/prometheus) | Observability | clear | Logs, metrics, traces or diagnostic bundles. |
| [Gateway logging](https://docs.openclaw.ai/gateway/logging) | Observability | clear | Logs, metrics, traces or diagnostic bundles. |
| [Diagnostics export](https://docs.openclaw.ai/gateway/diagnostics) | Observability | clear | Logs, metrics, traces or diagnostic bundles. |
| [Troubleshooting](https://docs.openclaw.ai/gateway/troubleshooting) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [PostgreSQL operator guide](https://docs.openclaw.ai/gateway/postgresql) | Infrastructure (layer) | clear | Database backend for the Gateway (listed twice in the nav). |
| [Gateway lock](https://docs.openclaw.ai/gateway/gateway-lock) | Reliability | clear | Singleton guard for the Gateway. |
| [Background exec and process tool](https://docs.openclaw.ai/gateway/background-process) | SPANS: Tools + Tasks | clear | Long-running processes that keep ownership across Gateway restarts. |
| [Restart recovery](https://docs.openclaw.ai/gateway/restart-recovery) | SPANS: Tasks + Reliability | clear | Records which sessions are working or waiting at stop, aborts and recovers them. |
| [Cloud Sessions](https://docs.openclaw.ai/gateway/cloud-sessions) | Environments | clear | Session work runs on a paired device or throwaway cloud machine; Gateway keeps transcript and credentials. |
| [Cloud Workers](https://docs.openclaw.ai/gateway/cloud-workers) | Environments | clear | Disposable machines for a session's coding work. |
| [Multiple gateways](https://docs.openclaw.ai/gateway/multiple-gateways) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Security](https://docs.openclaw.ai/gateway/security) | SPANS: Policy + Identity + Environments | clear | Overview of trust model and hardening; WARM calls security a concern, not a group. |
| [Security trust model](https://docs.openclaw.ai/gateway/security/trust-model) | SPANS: Policy + Identity + Environments | clear | Which boundary the project supports and which it does not. |
| [Running the security audit](https://docs.openclaw.ai/gateway/security/running-the-audit) | Evaluation | strained | Checks the platform's configuration against criteria; WARM Evaluation judges agents' behavior and work products. |
| [Security audit checks](https://docs.openclaw.ai/gateway/security/audit-checks) | Evaluation | strained | Catalog of audit check ids. |
| [Hardened baselines](https://docs.openclaw.ai/gateway/security/hardened-baseline) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Access control and allowlists](https://docs.openclaw.ai/gateway/security/access-control) | Policy | clear | Who can reach the agent: DM policy, allowlists, command authorization. |
| [Prompt injection](https://docs.openclaw.ai/gateway/security/prompt-injection) | SPANS: Policy + Environments + Models | clear | Defense in layers: access, sandbox, and model strength. |
| [Tool and agent permissions](https://docs.openclaw.ai/gateway/security/tool-permissions) | Policy | clear | Per-agent access profiles for sensitive tools. |
| [Browser control risks](https://docs.openclaw.ai/gateway/security/browser-control) | Policy | clear | SSRF policy bounding the browser. |
| [Network exposure](https://docs.openclaw.ai/gateway/security/network-exposure) | Infrastructure (layer) | clear | Bind, firewall, discovery and proxy settings. |
| [Secrets, storage, and logs](https://docs.openclaw.ai/gateway/security/secrets-and-storage) | SPANS: Secrets + Observability | clear | Which files hold credentials, and how logs and transcripts are handled. |
| [Gateway exposure runbook](https://docs.openclaw.ai/gateway/security/exposure-runbook) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Rate limiting](https://docs.openclaw.ai/gateway/security/rate-limiting) | Policy | strained | Independent rate limits that protect the Gateway; also Reliability. |
| [Operator incident response](https://docs.openclaw.ai/gateway/security/operator-incident-response) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Secure file operations](https://docs.openclaw.ai/gateway/security/secure-file-operations) | Environments | strained | Root-bounded file operations library. |
| [Operator scopes](https://docs.openclaw.ai/gateway/operator-scopes) | Policy | clear | Gates what an authenticated client may do. |
| [Sandboxing](https://docs.openclaw.ai/gateway/sandboxing) | Environments | clear | Sandbox backends for tool execution. |
| [OpenShell](https://docs.openclaw.ai/gateway/openshell) | Environments | clear | Managed sandbox backend. |
| [Sandbox vs tool policy vs elevated](https://docs.openclaw.ai/gateway/sandbox-vs-tool-policy-vs-elevated) | SPANS: Environments + Policy | clear | Explains three related controls. |
| [Session permission modes](https://docs.openclaw.ai/gateway/permission-modes) | Policy | strained | One session's filesystem boundary plus an escalation reviewer (an approval by a reviewer). |
| [Building a Gateway client](https://docs.openclaw.ai/gateway/clients) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Gateway integrations for external apps](https://docs.openclaw.ai/gateway/external-apps) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Gateway protocol](https://docs.openclaw.ai/gateway/protocol) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Embedding OpenClaw](https://docs.openclaw.ai/gateway/embedding) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [OpenAI chat completions](https://docs.openclaw.ai/gateway/openai-http-api) | MISFIT | n/a | Exposes the agent as an OpenAI-compatible model endpoint for other programs; an inbound program interface has no WARM service. |
| [OpenResponses API](https://docs.openclaw.ai/gateway/openresponses-http-api) | MISFIT | n/a | Same as the chat-completions endpoint, for the Responses API. |
| [Tools invoke API](https://docs.openclaw.ai/gateway/tools-invoke-http-api) | Tools | strained | Outside callers invoke one tool directly under Gateway auth and tool policy. |
| [CLI backends](https://docs.openclaw.ai/gateway/cli-backends) | Harness | clear | Agent turns run through a local AI CLI instead of the built-in loop. |
| [Local models](https://docs.openclaw.ai/gateway/local-models) | Models | strained | Installs and manages a local model or connects to one. |
| [Local model services](https://docs.openclaw.ai/gateway/local-model-services) | Models | strained | Starts a provider-owned local model server on demand. |
| [Network](https://docs.openclaw.ai/network) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Node pairing](https://docs.openclaw.ai/gateway/pairing) | SPANS: Identity + Approvals | clear | Device identity plus approved command exposure. |
| [Discovery and transports](https://docs.openclaw.ai/gateway/discovery) | Infrastructure (layer) | clear | Network reachability. |
| [Bonjour discovery](https://docs.openclaw.ai/gateway/bonjour) | Infrastructure (layer) | clear | Network reachability. |
| [Remote access](https://docs.openclaw.ai/gateway/remote) | Infrastructure (layer) | clear | Network reachability. |
| [Give your Gateway a stable HTTPS URL](https://docs.openclaw.ai/gateway/stable-https-url) | Infrastructure (layer) | clear | Network reachability. |
| [Tailscale](https://docs.openclaw.ai/gateway/tailscale) | Infrastructure (layer) | clear | Network reachability. |
| [Cloudflare Tunnel and Access](https://docs.openclaw.ai/gateway/cloudflare-access) | SPANS: Identity + Infrastructure | clear | Tunnel (network) plus Access authenticating every request. |
| [Network proxy](https://docs.openclaw.ai/security/network-proxy) | Policy | strained | Egress filtering through an operator-managed proxy. |
| [Formal verification (security models)](https://docs.openclaw.ai/security/formal-verification) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Incident response](https://docs.openclaw.ai/security/incident-response) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Threat model (MITRE ATLAS)](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS) | BUILDER | clear | Threat-model documentation; describes risks, adds no capability. |
| [Reconnaissance (AML.TA0002)](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/reconnaissance) | BUILDER | clear | Threat-model documentation; describes risks, adds no capability. |
| [Initial access (AML.TA0004)](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/initial-access) | BUILDER | clear | Threat-model documentation; describes risks, adds no capability. |
| [Execution (AML.TA0005)](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/execution) | BUILDER | clear | Threat-model documentation; describes risks, adds no capability. |
| [Persistence (AML.TA0006)](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/persistence) | BUILDER | clear | Threat-model documentation; describes risks, adds no capability. |
| [Defense evasion (AML.TA0007)](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/defense-evasion) | BUILDER | clear | Threat-model documentation; describes risks, adds no capability. |
| [Discovery (AML.TA0008)](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/discovery) | BUILDER | clear | Threat-model documentation; describes risks, adds no capability. |
| [Collection and exfiltration (AML.TA0009, AML.TA0010)](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/collection-and-exfiltration) | BUILDER | clear | Threat-model documentation; describes risks, adds no capability. |
| [Impact (AML.TA0011)](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/impact) | BUILDER | clear | Threat-model documentation; describes risks, adds no capability. |
| [Contributing to the threat model](https://docs.openclaw.ai/security/CONTRIBUTING-THREAT-MODEL) | BUILDER | clear | Threat-model documentation; describes risks, adds no capability. |
| [Nodes](https://docs.openclaw.ai/nodes) | SPANS: Environments + Tools | clear | Companion devices that expose command surfaces (camera, screen, exec). |
| [Node pairing and status](https://docs.openclaw.ai/nodes/pairing-and-status) | Identity | clear | Signed device identity and pairing. |
| [Run a node host](https://docs.openclaw.ai/nodes/node-host) | Environments | clear | Commands execute on another machine. |
| [Run commands on a node](https://docs.openclaw.ai/nodes/node-exec) | SPANS: Environments + Policy | clear | Point exec at a node; per-node allowlists. |
| [Node-hosted MCP servers and skills](https://docs.openclaw.ai/nodes/mcp-and-skills) | Tools | clear | MCP servers published from a node. |
| [Host OpenClaw sessions on a node](https://docs.openclaw.ai/nodes/session-hosting) | Environments | clear | Worker sessions isolated in containers on a node. |
| [Node session catalogs](https://docs.openclaw.ai/nodes/session-catalogs) | Sessions | clear | Discover and import native session transcripts. |
| [Node file transfers](https://docs.openclaw.ai/nodes/file-transfers) | Tools | clear | Move files to and from nodes. |
| [Node command policy](https://docs.openclaw.ai/nodes/command-policy) | Policy | clear | Default allowlists and dangerous-command opt-ins. |
| [Node device commands](https://docs.openclaw.ai/nodes/device-commands) | Tools | clear | Camera, screen, location, SMS commands. |
| [Active computer presence](https://docs.openclaw.ai/nodes/presence) | Human channels | clear | Routes alerts to the Mac the person used most recently: the channel the person is using. |
| [Node troubleshooting](https://docs.openclaw.ai/nodes/troubleshooting) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Media understanding](https://docs.openclaw.ai/nodes/media-understanding) | Human channels | strained | Summarizes inbound media before routing; a model-backed preprocessing step on the inbound channel. |
| [Media playback](https://docs.openclaw.ai/nodes/media-playback) | Human channels | clear | How people and the agent exchange requests and results. |
| [Image and media support](https://docs.openclaw.ai/nodes/images) | Human channels | clear | How people and the agent exchange requests and results. |
| [Audio and voice notes](https://docs.openclaw.ai/nodes/audio) | Human channels | clear | How people and the agent exchange requests and results. |
| [Camera capture](https://docs.openclaw.ai/nodes/camera) | Tools | clear | Device camera as a tool. |
| [Computer use](https://docs.openclaw.ai/nodes/computer-use) | Environments | clear | Agent controls a desktop. |
| [Talk mode](https://docs.openclaw.ai/nodes/talk) | Human channels | clear | How people and the agent exchange requests and results. |
| [Voice wake](https://docs.openclaw.ai/nodes/voicewake) | Human channels | clear | How people and the agent exchange requests and results. |
| [Location command](https://docs.openclaw.ai/nodes/location-command) | Tools | clear | Device location as a tool. |
| [Web](https://docs.openclaw.ai/web) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Control UI](https://docs.openclaw.ai/web/control-ui) | SPANS: Human channels + Observability | strained | One app is both the person's chat surface and the operator's console (activity, nodes, config). |
| [Portals](https://docs.openclaw.ai/gateway/portals) | Environments | strained | Exposes an agent-run dev server to the operator's browser. |
| [Notifications](https://docs.openclaw.ai/web/notifications) | Human channels | clear | How people and the agent exchange requests and results. |
| [Dashboard](https://docs.openclaw.ai/web/dashboard) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [Session Dashboards](https://docs.openclaw.ai/web/dashboards) | Artifacts | strained | Persistent widget boards the agent builds per thread; WARM Artifacts says nothing about live, updating products. |
| [Dashboard Architecture](https://docs.openclaw.ai/web/dashboard-architecture) | Artifacts | strained | Board storage and capability boundaries for those dashboards. |
| [Control UI URLs](https://docs.openclaw.ai/web/urls) | BUILDER | clear | Configuration reference, runbook, protocol or project process for operators and builders. |
| [WebChat](https://docs.openclaw.ai/web/webchat) | Human channels | clear | How people and the agent exchange requests and results. |
| [TUI](https://docs.openclaw.ai/web/tui) | Human channels | clear | How people and the agent exchange requests and results. |
| [The Lobster](https://docs.openclaw.ai/web/lobster) | BUILDER | strained | A UI mascot; not a platform capability. Placed here only to account for it. |

#### Reference

| Component | Assignment | Confidence | Why |
|---|---|---|---|
| [RPC adapters](https://docs.openclaw.ai/reference/rpc) | BUILDER | clear | Builder reference or migration note. |
| [Codex harness reference](https://docs.openclaw.ai/plugins/codex-harness-reference) | BUILDER | clear | Builder reference or migration note. |
| [Codex harness runtime](https://docs.openclaw.ai/plugins/codex-harness-runtime) | BUILDER | clear | Builder reference or migration note. |
| [Retired HEARTBEAT.md workspace file](https://docs.openclaw.ai/reference/templates/HEARTBEAT) | BUILDER | clear | Builder reference or migration note. |
| [TOOLS.md retired](https://docs.openclaw.ai/reference/templates/TOOLS) | BUILDER | clear | Builder reference or migration note. |
| [Agent runtime architecture](https://docs.openclaw.ai/agent-runtime-architecture) | BUILDER | clear | Builder reference or migration note. |
| [OpenClaw agent runtime workflow](https://docs.openclaw.ai/openclaw-agent-runtime) | BUILDER | clear | Builder reference or migration note. |
| [@openclaw/ai package](https://docs.openclaw.ai/reference/openclaw-ai) | BUILDER | clear | Builder reference or migration note. |
| [Token use and costs](https://docs.openclaw.ai/reference/token-use) | SPANS: Harness + Observability | clear | How context is built and how token use is reported; WARM treats cost as a concern. |
| [API usage and costs](https://docs.openclaw.ai/reference/api-usage-costs) | Observability | strained | Audit what can spend money and which keys are used. |
| [Usage tracking](https://docs.openclaw.ai/concepts/usage-tracking) | Observability | clear | Usage surfaces. |
| [Prompt caching](https://docs.openclaw.ai/reference/prompt-caching) | Harness | strained | Cache knobs and merge order for prompts. |
| [Session management deep dive](https://docs.openclaw.ai/reference/session-management-compaction) | Sessions | clear | Session store, transcripts, lifecycle. |
| [Transcript hygiene](https://docs.openclaw.ai/reference/transcript-hygiene) | Sessions | strained | Provider-specific repair of stored transcripts. |
| [Memory configuration reference](https://docs.openclaw.ai/reference/memory-config) | BUILDER | clear | Builder reference or migration note. |
| [Database engines](https://docs.openclaw.ai/reference/database-engines) | Infrastructure (layer) | clear | SQLite or PostgreSQL. |
| [Database schemas](https://docs.openclaw.ai/reference/database-schemas) | BUILDER | clear | Builder reference or migration note. |
| [Rich output protocol](https://docs.openclaw.ai/reference/rich-output-protocol) | Human channels | clear | Structured media and embeds in replies. |
| [SecretRef credential surface](https://docs.openclaw.ai/reference/secretref-credential-surface) | BUILDER | clear | Builder reference or migration note. |
| [Secret Placeholder Conventions](https://docs.openclaw.ai/reference/secret-placeholder-conventions) | BUILDER | clear | Builder reference or migration note. |
| [Date and time](https://docs.openclaw.ai/date-time) | Harness | strained | Time in envelopes, prompts and tool payloads. |
| [Timezones](https://docs.openclaw.ai/concepts/timezone) | Harness | strained | Same. |
| [TypeBox](https://docs.openclaw.ai/concepts/typebox) | BUILDER | clear | Builder reference or migration note. |
| [Markdown formatting](https://docs.openclaw.ai/concepts/markdown-formatting) | Human channels | clear | Formatting pipeline for outbound channels. |

### 1.2 Class rows

| Source | Class | Count | Assignment | Confidence | Why |
|---|---|---|---|---|---|
| Capabilities | Web search provider pages (Brave, DuckDuckGo, Exa, Gemini, Grok, Kimi, MiniMax, Ollama, Parallel, Perplexity, SearXNG, Tavily) | 12 | Providers (layer) | clear | External search services that Retrieval calls. |
| Channels | Individual chat channels for people (Discord, Google Chat, iMessage, Matrix, Teams, Signal, Slack, SMS, Telegram, WhatsApp, X; 9 developer and self-hosted; 9 regional) | 29 | Human channels | clear | Each carries requests and results on the app the person uses. A2A, Reef and Raft are agent channels and are assigned individually. |
| Models | Chat and coding model providers | 49 | Providers (layer) | clear | Model vendors the platform calls. |
| Models | Decision-model providers (Liquid AI, Rerank) | 2 | Providers (layer) | clear | Model vendors for the typed-decision role. |
| Models | Speech and audio providers | 7 | Providers (layer) | clear | TTS and STT vendors. |
| Models | Image, video and music providers | 6 | Providers (layer) | clear | Media-generation vendors. |
| Models | Model gateways and routers (Bifrost, OpenRouter, LiteLLM, ClawRouter and 7 others) | 11 | Providers (layer) | strained | Each is an outside implementation of the Models service (routing across vendors), sitting below the platform's own Models service. |
| Models | Local model runtimes (Ollama, vLLM, SGLang, LM Studio, ds4, llmman, oMLX) | 7 | Providers (layer) | strained | Model servers that run on the user's own machines, so they are also Infrastructure. |
| Install | Install targets (Docker, Podman, Linux server, 8 app platforms, 6 cloud servers, 6 self-hosted and local) | 23 | BUILDER | clear | Installer guides for the Infrastructure the Gateway runs on. |
| Install | Runtime install pages (Node.js, Bun, compatibility, standalone builds, Nix) | 6 | BUILDER | clear | Installer guides. |
| Install | Install overview, installer internals, advanced setup | 3 | BUILDER | clear | Installer guides. |
| Platforms | Host platform guides (Platforms overview, Linux app, Omarchy, Windows, ChromeOS, EasyRunner) | 6 | BUILDER | clear | Where and how to run the Gateway and its apps. |
| Platforms | Companion app pages used by the person (macOS, iOS and Android apps, menu bar and icon, voice wake, voice overlay, WebChat, widget panel) | 9 | Human channels | clear | The apps a person talks to the agent through. |
| Platforms | macOS app developer and operations pages (dev setup, signing, permissions, remote control, device models, bundled Gateway, health, logging, IPC, skills) | 10 | BUILDER | clear | Build, sign, run and troubleshoot the app. |
| Reference | CLI reference commands (index plus 69 commands) | 70 | BUILDER | clear | Operator interface. Each command exposes a service already assigned above. |
| Reference | Plugin reference, plugin SDK reference and plugin internals | 21 | BUILDER | clear | For plugin authors. |
| Reference | Workspace templates (default AGENTS.md, AGENTS, BOOT, BOOTSTRAP, IDENTITY, SOUL, USER, and 4 dev-agent templates) | 11 | Domains (layer) | strained | Agent definition files. The platform ships defaults, and USER.md is memory about the person, not a definition. |
| Reference | Project and contributing pages (credits, PR review flow, 7 maintainer scripts) | 9 | BUILDER | clear | Contributor process. |
| Plugins | LLM model provider plugins | 51 | Providers (layer) | clear | Adds a model vendor. |
| Plugins | Media provider plugins (speech, transcription, image, video, music) | 16 | Providers (layer) | clear | Adds a media vendor. |
| Plugins | Decision-model provider plugins | 6 | Providers (layer) | clear | Adds a typed-decision model vendor. |
| Plugins | Embedding provider plugin (voyage) | 1 | Providers (layer) | clear | Adds an embedding vendor. |
| Plugins | Model gateway and router plugins | 10 | Providers (layer) | strained | External implementations of model routing. |
| Plugins | Human chat channel plugins | 25 | Human channels | clear | Adds a channel for people. |
| Plugins | Meeting and voice-call plugins | 7 | Human channels | clear | Adds calls and meetings. |
| Plugins | Agent-to-agent channel plugins (a2a, reef, raft) | 3 | Messaging | clear | Adds a channel between agents. |
| Plugins | Alternative harness plugins (agentsapi, acpx, codex, copilot, muse) | 5 | Harness | clear | Swaps the agent loop. |
| Plugins | Web search, fetch and document-reader plugins | 11 | Retrieval | clear | Adds a source to fetch from. |
| Plugins | Memory and knowledge plugins (memory-core, active-memory, knowledge, memory-wiki, memory-lancedb) | 5 | Memory | clear | Fills the single memory slot or adds a knowledge vault. |
| Plugins | skill-workshop | 1 | Memory | clear | Learned skills (procedural memory). |
| Plugins | Secrets resolver plugins (onepassword, vault) | 2 | Secrets | clear | Resolves SecretRefs. |
| Plugins | Sandbox, cloud-worker and computer-control plugins (browser, code-mode-quickjs, crabbox, cua-computer, mxc, openshell) | 6 | Environments | clear | Adds a place to act. |
| Plugins | Node and device plugins (linux-node, file-transfer, canvas) | 3 | Tools | strained | Device commands; canvas is a display surface. |
| Plugins | Observability exporters (diagnostics-otel, diagnostics-prometheus) | 2 | Observability | clear | Exports metrics, traces, logs. |
| Plugins | Identity and access plugins (device-pair, openclaw-id-access, visitor-access) | 3 | Identity | clear | Pairing and remote-access grants. |
| Plugins | bonjour | 1 | Infrastructure (layer) | clear | LAN discovery. |
| Plugins | geolocation | 1 | Observability | strained | Coarse city for client IPs. |
| Plugins | Event-trigger plugins (imap, mcp-events) | 2 | Scheduling | clear | Starts work on an event. |
| Plugins | Tool plugins (llm-task, diffs, diffs-language-pack) | 3 | Tools | clear | Adds a tool. |
| Plugins | tokenjuice | 1 | Harness | clear | Compacts tool results in context. |
| Plugins | lobster | 1 | SPANS: Orchestration + Approvals + Tasks | clear | Workflow runner with approval gates and resume. |
| Plugins | workboard | 1 | SPANS: Tasks + Orchestration | clear | Backlog cards dispatched to worker runs. |
| Plugins | Session-sharing plugins (session-share, beam) | 2 | Sessions | strained | Shares sessions across Gateways. |
| Plugins | autoreview | 1 | Evaluation | clear | Reviews changes. |
| Plugins | advisor | 1 | Evaluation | strained | Reviews ongoing work and offers one correction. |
| Plugins | policy | 1 | Evaluation | strained | Despite its name: conformance checks run by Doctor. |
| Plugins | agent-guidance | 1 | Registry | strained | Shared instruction files across agents. |
| Plugins | deep-research | 1 | Domains (layer) | strained | Research judgment shipped as a platform plugin. |
| Plugins | Activity journal and report plugins (logbook, team-reports) | 2 | Domains (layer) | strained | Domain features (a work journal; team activity reports from GitHub and Discord). |
| Plugins | cloudflare (R2 storage) | 1 | Infrastructure (layer) | clear | Object storage. |
| Plugins | mcp-relay | 1 | MISFIT | n/a | Inbound interface for outside agents and apps. |
| Plugins | Builder plugins (admin-http-rpc, oc-path, migrate-claude, migrate-hermes, qa-channel, qa-lab) | 6 | BUILDER | clear | Operator, migration and test tooling. |

## 2. The 22 services

"Matched" lists the components assigned to the service, including SPANS rows that name it (marked "spans"). Class rows are shown with their counts. For each service with a thin or partial match I searched the inventory text under other names, then the repository (`gh search code` over `openclaw/openclaw`) and the web; the queries are recorded.

| Service | Matched components | Status | Evidence and searches |
|---|---|---|---|
| **Harness** | Agent runtime, Agent loop, Agent runtimes, System prompt, Context, Context engine, Compaction, Session pruning, Steering queue, Steer, Tokenjuice, CLI backends, Agents API, Codex harness, Copilot SDK harness, Muse Code agent runtime, Prompt caching, Date and time, Timezones; spans: Code Mode, Token use and costs; classes: 5 harness plugins, tokenjuice | FOUND | "OpenClaw ships one **embedded agent runtime**: a built-in agent loop, tool wiring, and prompt assembly" (https://docs.openclaw.ai/concepts/agent). Vendor harnesses plug in while "OpenClaw keeps ownership of channels, sessions, policy, and state" (https://docs.openclaw.ai/start/why-openclaw). |
| **Sessions** | The main session, Session management, Session synchronization and attachment, Node session catalogs, Session management deep dive, Transcript hygiene, Progress card, Supervise Codex sessions, Codex supervision, Beam, Session Share; spans: Gateway architecture, Multi-user mode, Session tools; class: 2 session-sharing plugins | FOUND | "All session state is owned by the **gateway**" (https://docs.openclaw.ai/concepts/session). |
| **Tasks** | Goal (strained); spans: Workboard, Lobster, Background exec and process tool, Restart recovery | PARTIAL | No shared run ledger. The Tasks ledger and TaskFlow were removed: "The shared Tasks ledger, TaskFlow orchestration API, and TaskFlow Webhooks plugin have been removed." (https://docs.openclaw.ai/automation). What exists: per-runtime run tracking ("Subagent runs are tracked by the native subagent lifecycle owner", https://docs.openclaw.ai/tools/subagents), automation run history, restart recovery, Workboard cards. Searches: web "openclaw Tasks ledger TaskFlow removed run tracking retry cancellation" (results are mirrors of the pre-removal docs at v2026.9.2, e.g. https://docs.openclaw.ai/automation/tasks.md); repo "task_runs", "run ledger" (hits: database schema pages and update history only). |
| **Environments** | Managed worktrees, Sandboxing, OpenShell, Cloud Sessions, Cloud Workers, Browser, Chrome Extension, Computer use, Codex Computer Use, Peekaboo bridge, Run a node host, Host sessions on a node, Secure file operations, Portals, Browser login; spans: Agent workspace, Nodes, trust boundary, security pages; class: 6 sandbox plugins | FOUND | "OpenClaw can run tool execution inside a sandbox backend" (https://docs.openclaw.ai/gateway/sandboxing). |
| **Scheduling** | Automations, Heartbeat migration, IMAP email trigger, MCP Events, Hooks; spans: Automation, Gateway architecture; class: 2 trigger plugins | FOUND | "Automations are OpenClaw's built-in scheduler" (https://docs.openclaw.ai/automation/cron-jobs). |
| **Memory** | Memory overview, Memory architecture, Memory provenance and deletion, Provenance, User model, Builtin memory engine, Honcho, Dreaming, Active memory, Knowledge, Memory LanceDB, Memory wiki, Skill Workshop, Self-learning, Personal library authoring, Custodian skills; spans: Agent workspace, Memory search, Skills; classes: 5 memory plugins, skill-workshop | FOUND | All three WARM kinds exist (MEMORY.md facts, an episodic tier, learned skills) with provenance (https://docs.openclaw.ai/concepts/memory-architecture). |
| **Retrieval** | Web fetch, Web search, Firecrawl, Session search; spans: Memory search; class: 11 search and fetch plugins | FOUND | https://docs.openclaw.ai/tools/web |
| **Artifacts** | Session Dashboards, Dashboard Architecture (both strained); spans: Storage locations | PARTIAL | No artifact store with versions. Work products live in the agent workspace and its git worktree (snapshots, a Changes panel), and storage locations are "a destination for OpenClaw artifacts" where "each consumer decides what to store and retain" (https://docs.openclaw.ai/concepts/storage-locations). Searches: web "openclaw artifacts storage versions agent outputs files docs.openclaw.ai" (only third-party vendor guides); repo "artifact versions", "artifact store", "artifacts panel" (no docs hits). |
| **Models** | Models CLI, Model providers, Model failover, Decision models, Recommended models, Local ONNX decision models, Thinking levels, Local models, Local model services; spans: Prompt injection | FOUND | "How OpenClaw rotates auth profiles and falls back across models" (https://docs.openclaw.ai/concepts/model-failover). |
| **Tools** | Exec, apply_patch, Code execution, Diffs, media tools, PDF, LLM task, Connect MCP servers, Native Codex plugins, node commands, Camera, Location, Node file transfers, Tools invoke API, HealthKit summaries; spans: Code Mode, Nodes, Background exec, Gateway architecture; classes: 3 node plugins, 3 tool plugins | FOUND | https://docs.openclaw.ai/tools/mcp |
| **Registry** | ClawHub, How ClawHub Works, Tool Search, Community plugins, Plugin bundles, Agent Guidance; spans: Skills, Publishing, Multi-agent routing; class: agent-guidance | PARTIAL | Definitions of tools, skills and plugins can be found and loaded (ClawHub, skill precedence, Tool Search). The directory of responsibilities is absent: no list maps a responsibility to a domain and an agent. The closest things are channel bindings (routing by origin), the `agents_list` tool ("discover permitted specialists", in the coordinator's AGENTS.md: https://github.com/openclaw/openclaw/blob/main/docs/reference/templates/roles/coordinator/workspace/AGENTS.md) and a fallback `systemAgent`. `openclaw directory` is a channel lookup "(self, peers, groups)", not this. Searches: web "openclaw multi-agent which agent handles what routing specialists directory agents_list" (found routing by bindings only); repo "agents_list" (tool catalog and role templates), "who owns which" (no hits). |
| **Messaging** | A2A, Reef, Raft; spans: Session tools; class: 3 agent-channel plugins | FOUND | `sessions_send`, and "Reef is a guarded, end-to-end-encrypted" channel between agents of different people (https://docs.openclaw.ai/channels/reef). |
| **Orchestration** | Sub-agents, Swarm, Broadcast groups, ACP agents; spans: Session tools, Workboard, Automation, Lobster | FOUND | https://docs.openclaw.ai/tools/subagents |
| **Human channels** | 29 chat channels, 7 meeting and call plugins, 25 channel plugins, 9 companion apps, WebChat, TUI, Talk mode, Voice wake, Notifications, Active computer presence, Ask user, Slash commands, streaming and typing, and more (109 components) | FOUND | https://docs.openclaw.ai/channels |
| **Identity** | Delegate architecture, Trusted proxy auth, Node pairing and status, ClawHub Auth; spans: Identity and roles, Pairing, Node pairing, Multi-user mode, Cloudflare Access, security pages; class: 3 access plugins | FOUND | A delegate "Has its **own identity**" and "Acts **on behalf of** one or more humans" (https://docs.openclaw.ai/concepts/delegate-architecture). |
| **Secrets** | Secrets (Get started), Secrets tool, Secrets management, 1Password (page and plugin), Vault, OAuth, Authentication, Auth credential semantics; spans: trust boundary, Secrets storage and logs; class: 2 resolver plugins | FOUND | "`secrets` lets the agent ask you for a credential without ever seeing it" (https://docs.openclaw.ai/tools/secrets). |
| **Policy** | Permission modes, Elevated mode, Access groups, Access control and allowlists, Operator scopes, Tool and agent permissions, Multi-agent sandbox and tools, Node command policy, Browser control risks, Tool-loop detection, Rate limiting, Network proxy, Bot loop protection, Session permission modes; spans: Policy as code, Exec approvals, Plugin hooks, Prompt injection and others | FOUND | "Permission modes, tool policy, and exec approvals as code-enforced gates" (https://docs.openclaw.ai/start/why-openclaw/policy-as-code). |
| **Approvals** | Plugin permission requests; spans: Policy as code, Exec approvals (both pages), Pairing, Node pairing, Lobster | FOUND | Exec approvals: "Commands run only when policy + allowlist + (optional) user approval" (https://docs.openclaw.ai/tools/exec-approvals). Audit history keeps "decision receipts" (https://docs.openclaw.ai/gateway/audit). |
| **Observability** | Audit history, Logging, Gateway logging, OpenTelemetry, Prometheus, Diagnostics export, Trajectory bundles, Usage tracking, API usage and costs, Presence, Geolocation, ClawHub Telemetry; spans: Plugin hooks, Control UI, Token use; classes: 2 exporters, geolocation | FOUND | https://docs.openclaw.ai/gateway/audit |
| **Evaluation** | Auto Review; Running the security audit, Security audit checks, ClawHub Security Audits (strained); classes: autoreview, advisor, policy (conformance) | PARTIAL | What exists reviews code changes (Auto Review), offers one correction to ongoing work (advisor), or checks configuration and third-party packages. Nothing assesses an agent's work products against a domain's stated criteria. Closest to WARM's "unknown": Custodian playbooks "never [claim] success without its Prove outcome" and report "the exact blocker when live proof is unavailable" (https://docs.openclaw.ai/tools/custodian-skills). Reliability evals for skills exist only in the contributor testing docs (https://docs.openclaw.ai/help/testing). The Foundation convenes "councils on agent identity, agent profiles, evals" (https://docs.openclaw.ai/start/why-openclaw). Searches: web "docs.openclaw.ai evaluation evals agent quality criteria" (only third-party ClawHub skills, e.g. https://clawhub.ai/skills/openclaw-skill-eval); repo "eval harness", "evals", "acceptance criteria" (hits: testing docs and the role templates). |
| **Releases** | Updating, Update troubleshooting, Release channels; spans: Versioned state guarded upgrades, Doctor, Publishing, Usage telemetry and update checks | FOUND | Platform releases with rollback (https://docs.openclaw.ai/install/updating). For agents, versioning is narrower: learned skills save "the previous version first, and can be undone" (https://docs.openclaw.ai/tools/skill-workshop) and ClawHub versions packages; AGENTS.md and config changes have no release mechanism of their own. |
| **Reliability** | Health checks, Backups, Gateway lock, Retry policy; spans: Doctor, Restart recovery, Storage locations, Versioned state | FOUND | https://docs.openclaw.ai/gateway/health |

**ABSENT:** none. **PARTIAL:** Tasks, Artifacts, Registry (directory), Evaluation.

## 3. MISFIT list (13)

| Component | Why it fits no WARM service | Inventory quote | URL |
|---|---|---|---|
| Agent bootstrapping | Creating an agent and its identity is a lifecycle step; Registry holds definitions but no service creates them. | "Bootstrapping is the first-run ritual that seeds a new agent workspace and walks the agent through picking an identity." | https://docs.openclaw.ai/start/bootstrapping |
| Session controller | Admission control: decides which input runs next on a session. | "A session controller is the owner of **which turn may use a session next**. It coordinates accepted inputs, the current turn, and admission barriers." | https://docs.openclaw.ai/concepts/session-controller |
| Command queue | Admission and shared capacity across runs. | "OpenClaw serializes inbound auto-reply runs (all channels) through a tiny in-process queue to prevent multiple agent runs from colliding, while still allowing safe parallelism across sessions." | https://docs.openclaw.ai/concepts/queue |
| Parallel specialist lanes | Capacity planning across agents that share model and tool capacity. | "Treat parallelism as a scarce-resource design problem, not just \"more agents\"." | https://docs.openclaw.ai/concepts/parallel-specialist-lanes |
| Session state awareness | A shared, versioned coordination log for several sessions on one problem; neither a session's own history nor a message. | "Durable session state signal log: state versions, watchers, stale-state notices, and reconciliation" | https://docs.openclaw.ai/concepts/session-state |
| Standing intents | Prospective memory (an intention bound to a future event); not semantic, episodic or procedural, and it does not start work. | "A standing intent is an event-conditioned instruction such as \"when the release candidate is mentioned, remind me to verify rollback ownership.\"" | https://docs.openclaw.ai/concepts/standing-intents |
| Plugins (the plugin host) | Loads and swaps the implementation of most services, with slots ("only one memory plugin can be active"); WARM keeps implementations outside the model. | "Plugins extend OpenClaw with channels, model providers, agent harnesses, tools, skills, speech, ... and other runtime capabilities." | https://docs.openclaw.ai/tools/plugin |
| Acceptable Usage (ClawHub) | Governance of what third parties may publish into the ecosystem; Policy decides actions, not supply. | "Marketplace policy: what ClawHub allows and what it will not host." | https://docs.openclaw.ai/clawhub/acceptable-usage |
| Moderation and Account Safety (ClawHub) | Same supply-chain governance. | "How ClawHub reports, moderation holds, hidden listings, bans, and account standing work." | https://docs.openclaw.ai/clawhub/moderation |
| MCP Relay (page) | Inbound interface for outside agents and apps; WARM's Interaction covers this platform's agents and people only. | "Remote MCP clients such as ChatGPT, Codex, and Claude connect to `https://mcp.openclaw.ai/mcp`" | https://docs.openclaw.ai/plugins/mcp-relay |
| mcp-relay (plugin) | Same component as a plugin. | "Connect remote MCP clients to your OpenClaw Gateway." | https://docs.openclaw.ai/plugins/plugin-inventory |
| OpenAI chat completions | The agent exposed as a model API to programs. | "Expose an OpenAI-compatible /v1/chat/completions HTTP endpoint from the Gateway" | https://docs.openclaw.ai/gateway/openai-http-api |
| OpenResponses API | Same, for the Responses API. | "Expose an OpenResponses-compatible /v1/responses HTTP endpoint from the Gateway" | https://docs.openclaw.ai/gateway/openresponses-http-api |

The scorecard independently names this last cluster: "External apps and interoperability" is a Core surface at M2 Alpha (https://docs.openclaw.ai/maturity/scorecard).

## 4. SPANS list (38)

| Component | Services | Inventory quote | URL |
|---|---|---|---|
| The trust boundary | Environments, Policy, Secrets | "The Gateway owns channel connections, config, credentials, and the control-plane API." | https://docs.openclaw.ai/start/why-openclaw/the-trust-boundary |
| Policy as code | Policy, Approvals | "Permission modes, tool policy, and exec approvals as code-enforced gates" | https://docs.openclaw.ai/start/why-openclaw/policy-as-code |
| Identity and roles | Identity, Policy | "Pairing, operator scopes, role ceilings, and the one-gateway-is-one-trust-domain boundary" | https://docs.openclaw.ai/start/why-openclaw/identity-and-roles |
| Versioned state, guarded upgrades | Releases, Reliability | "Database-first state, schema version contracts, guarded updates, release channels" | https://docs.openclaw.ai/start/why-openclaw/versioned-state-guarded-upgrades |
| Gateway architecture | Sessions, Human channels, Tools, Scheduling, Identity | "A single long-lived **Gateway** owns all messaging surfaces" | https://docs.openclaw.ai/concepts/architecture |
| Agent workspace | Environments, Memory | "The workspace is the agent's home ... Keep it private and treat it as memory." | https://docs.openclaw.ai/concepts/agent-workspace |
| Storage locations | Artifacts, Reliability | "A storage location names a destination for OpenClaw artifacts." | https://docs.openclaw.ai/concepts/storage-locations |
| Multi-user mode | Sessions, Identity | "It adds session ownership, participant history, live presence, and owner filtering." | https://docs.openclaw.ai/concepts/multi-user |
| Session tools | Sessions, Messaging, Orchestration | "Agent tools for session creation, cross-session status, recall, messaging, and sub-agent orchestration" | https://docs.openclaw.ai/concepts/session-tool |
| Memory search | Memory, Retrieval | "finds relevant notes from your memory files ... with embeddings, keywords, or both" | https://docs.openclaw.ai/concepts/memory-search |
| Multi-agent routing | Human channels, Registry | "Inbound messages route to the right agent through **bindings**." | https://docs.openclaw.ai/concepts/multi-agent |
| Workboard plugin | Tasks, Orchestration | "agent-sized work cards, assignment to agents, and a link back to the card's task, run, and Control UI session" | https://docs.openclaw.ai/plugins/workboard |
| Plugin hooks | Policy, Observability | "observe or change agent runs, tool calls, message delivery, and lifecycle events" | https://docs.openclaw.ai/plugins/hooks |
| Skills | Memory, Registry | "how they load, how precedence works, and how to configure gating" | https://docs.openclaw.ai/tools/skills |
| Automation | Scheduling, Orchestration, Policy | "automations, hooks, standing orders, and workflows" | https://docs.openclaw.ai/automation |
| Exec approvals | Policy, Approvals | "Commands run only when policy + allowlist + (optional) user approval" | https://docs.openclaw.ai/tools/exec-approvals |
| Exec approvals - advanced | Policy, Approvals | "safe bins, interpreter binding, approval forwarding" | https://docs.openclaw.ai/tools/exec-approvals-advanced |
| Code Mode | Harness, Tools | "When enabled, the model no longer sees every enabled tool schema." | https://docs.openclaw.ai/tools/code-mode |
| Lobster (page and plugin, 2) | Orchestration, Approvals, Tasks | "multi-step tool pipelines ... with explicit approval/input checkpoints and resume tokens" | https://docs.openclaw.ai/tools/lobster |
| workboard (plugin) | Tasks, Orchestration | "Dashboard workboard for agent-owned issues and sessions." | https://docs.openclaw.ai/plugins/plugin-inventory |
| Publishing (ClawHub) | Registry, Releases | "sends a skill folder or plugin package to ClawHub ... validates the metadata, name, version" | https://docs.openclaw.ai/clawhub/publishing |
| Doctor | Reliability, Releases | "health checks, config migrations, and repair steps" | https://docs.openclaw.ai/gateway/doctor |
| Usage telemetry and update checks | Observability, Releases | "Daily update requests, update-outcome reports ... optional anonymous feature statistics" | https://docs.openclaw.ai/gateway/telemetry |
| Background exec and process tool | Tools, Tasks | "opt-in durable processes on a Linux Gateway retain ownership across Gateway restarts" | https://docs.openclaw.ai/gateway/background-process |
| Restart recovery | Tasks, Reliability | "records which sessions are working or waiting, then aborts executing work promptly" | https://docs.openclaw.ai/gateway/restart-recovery |
| Security; Security trust model (2) | Policy, Identity, Environments | "Trust model, safe defaults, and hardening guidance" | https://docs.openclaw.ai/gateway/security |
| Prompt injection | Policy, Environments, Models | "which layers you still have to enforce" | https://docs.openclaw.ai/gateway/security/prompt-injection |
| Secrets, storage, and logs | Secrets, Observability | "which files hold credentials, and how logs and transcripts are handled" | https://docs.openclaw.ai/gateway/security/secrets-and-storage |
| Sandbox vs tool policy vs elevated | Environments, Policy | "OpenClaw has three related but different controls" | https://docs.openclaw.ai/gateway/sandbox-vs-tool-policy-vs-elevated |
| Node pairing (Gateway and Ops) | Identity, Approvals | "how nodes gain command exposure after device pairing" | https://docs.openclaw.ai/gateway/pairing |
| Pairing (Channels) | Identity, Approvals | "\"Pairing\" is OpenClaw's explicit access approval step." | https://docs.openclaw.ai/channels/pairing |
| Cloudflare Tunnel and Access | Infrastructure (layer), Identity | "let Cloudflare Access authenticate every request" | https://docs.openclaw.ai/gateway/cloudflare-access |
| Nodes | Environments, Tools | "a companion device ... that connects to the Gateway with `role: \"node\"` and exposes a command surface" | https://docs.openclaw.ai/nodes |
| Run commands on a node | Environments, Policy | "Allowlist node commands, point exec at a node" | https://docs.openclaw.ai/nodes/node-exec |
| Control UI | Human channels, Observability | "Browser-based control UI for the Gateway (chat, activity, nodes, config)" | https://docs.openclaw.ai/web/control-ui |
| Token use and costs | Harness, Observability | "How OpenClaw builds prompt context and reports token usage + costs" | https://docs.openclaw.ai/reference/token-use |

Most SPANS rows are overview or security pages, which span services by design. The ones that matter for the model: the Gateway (one process owns the control plane), Agent workspace (one directory is both the place to act and memory), Session tools and Workboard (tracking and orchestration in one surface), and Lobster (orchestration, approvals and resumable tracking in one runner).

## 5. Groupings compared (step 3)

**OpenClaw's top-level groups** are the documentation tabs: Get started, Install, Channels, Agents, Capabilities, ClawHub, Models, Platforms, Gateway and Ops, Reference. The maturity scorecard adds a second grouping into four families: Core, Platform, Channel, Provider and tool (https://docs.openclaw.ai/maturity/taxonomy).

| OpenClaw group | WARM groups it contains |
|---|---|
| Agents tab | Runtime (agent loop, sessions), Knowledge (memory, in the same "Sessions and memory" group as sessions), Interaction (multi-agent routing, message delivery) |
| Capabilities tab | Capabilities (tools, plugins), Knowledge (skills, self-learning), Runtime (Automation, which is Scheduling), Interaction (Agent coordination: sub-agents, swarm), Governance (exec approvals, permission modes and the secrets tool sit under "Tools: Running code and approvals") |
| Gateway and Ops tab | Governance (auth, secrets, security, sandbox policy), Operations (health, logging, telemetry), Runtime (sandboxing, cloud workers, nodes), Interaction (web interfaces), Infrastructure (networking, remote access, PostgreSQL), builder tooling (configuration reference, protocol) |
| Channels tab | Interaction: Human channels, plus A2A, Reef and Raft, which are Messaging |
| Models tab | Capabilities (Models) plus the Providers layer |
| ClawHub tab | Capabilities (Registry) plus marketplace governance (a misfit) |
| Install, Platforms, Reference | Builder tooling and Infrastructure |

**Where the cuts differ.**
- OpenClaw groups by **what a person is doing with the product** (installing, connecting a chat app, choosing a model, operating the Gateway) and by **what kind of plugin supplies it** (channel, provider, tool). WARM groups by the question a service answers. The two cut across each other in every tab except Channels and Models.
- OpenClaw groups by **transport**, not by who is on the other end. A2A and Reef (agents) sit beside Telegram (people) in Channels.
- Sessions and memory are one group in the docs and one scorecard surface ("Session, memory, and state lifecycle"). WARM splits them across Runtime and Knowledge. OpenClaw's reason is visible in the memory architecture: session transcripts are ingested into the episodic memory tier at session end (https://docs.openclaw.ai/concepts/memory-architecture).
- Automation (Scheduling) sits under Capabilities, next to tools, not with the runtime.
- "Security, auth, pairing, and secrets" is one scorecard surface: Identity, Secrets and Policy as one unit. Approvals is not in it; approvals are documented with each surface that asks for them (exec, plugins, pairing, Lobster).

**Does it treat identity, policy and observability as cross-cutting?** Partly, and more explicitly than most platforms.
- The "Why OpenClaw" pages state the architecture as cross-cutting properties: The trust boundary, Policy as code, Identity and roles, Secrets, Versioned state, Provenance. Four of the six are WARM Governance. "Policy is enforced in code, and state is versioned and migrated" (https://docs.openclaw.ai/start/why-openclaw).
- The threat model orders them: "**Identity first** ... **Scope next** ... **Model last** - assume the model can be manipulated" (https://docs.openclaw.ai/gateway/security/trust-model).
- Policy is enforced centrally but configured per surface: DM policy in Channels, tool policy per agent, node command policy in Nodes, sub-agent tool policy in Sub-agents. Plugin hooks give one interception point "inside the agent/tool lifecycle and Gateway pipeline" (https://docs.openclaw.ai/concepts/agent-loop).
- Observability is one Core scorecard surface, and the audit ledger is one store for all runs ("which agent ran, when, and how did it end", https://docs.openclaw.ai/gateway/audit).
- Identity is cross-cutting for clients and devices (pairing, operator scopes) but not for agents talking to each other: "`sessionKey` (session IDs, labels) is a routing selector, not an authorization token" and "any tool-enabled agent running unsandboxed can list, read, search, and message every agent's sessions" by default (https://docs.openclaw.ai/gateway/security/trust-model). The boundary is the Gateway: "one gateway is one trust domain".

## 6. WARM ideas in OpenClaw (step 4)

### 6.1 A domain or area of work with roles

OpenClaw has **roles** and **teams**, but no **domain**. Its unit is the agent: "An **agent** is the full per-persona scope: workspace files, auth profiles, model registry, and session store" (https://docs.openclaw.ai/concepts/multi-agent).

- Bundled roles: "`coordinator` | Chief of staff | Coordinate specialists as your single point of contact", "`researcher` ... Gather evidence and return a cited research brief", "`writer`", "`reviewer` ... Check artifacts against requirements and return actionable findings." `openclaw agents team create` "Creates a chief of staff (`coordinator`) plus `researcher`, `writer`, and `reviewer` from the role templates" (https://docs.openclaw.ai/cli/agents).
- A role is written as an agent definition: "each role directory contains a `CLAW.md` manifest with identity and `SOUL.md` content, plus its operating program in `workspace/AGENTS.md`" (same page). This matches WARM's "each role that an agent fills is written as an agent definition", with one addition WARM lacks: a persona (`SOUL.md`).
- Responsibilities attach to an agent, not to a domain. Standing orders "grant your agent **permanent operating authority** for defined programs ... with clear scope, triggers, and escalation rules ... \"You own the weekly report.\"" They "live in workspace files (typically `AGENTS.md`)" (https://docs.openclaw.ai/automation/standing-orders, https://docs.openclaw.ai/automation).
- Two deployment shapes stand in for scope: "A **personal claw** is one person's assistant" and a multiplayer claw is "one shared Gateway for a trusted team" (https://docs.openclaw.ai/start/multiplayer). The delegate architecture adds capability tiers for an organization (Tier 1 "Read-Only + Draft", Tier 2 "Send on Behalf") (https://docs.openclaw.ai/concepts/delegate-architecture).

### 6.2 A directory of who is responsible for what

Not found as such (as of 2026-11-11). `[no-record: a responsibility-to-domain-to-agent directory; searched=inventory-openclaw.md (grep directory, responsib, owner), openclaw/openclaw docs via gh code search ("agents_list", "who owns which"), web search]`. What exists instead:
- **Routing by origin.** "Ordinary routing picks **one agent** for each inbound message" by exact peer, guild, team, account or channel; "The model does not choose a channel; routing follows fixed rules controlled by the host configuration" (https://docs.openclaw.ai/channels/channel-routing).
- **Discovery by role text.** The coordinator's program lists the specialists' duties in prose and says: "Use `agents_list` when available to discover permitted specialists. Match their names to the role descriptions above" (https://github.com/openclaw/openclaw/blob/main/docs/reference/templates/roles/coordinator/workspace/AGENTS.md). Delegation permission is config: "The coordinator's `subagents.allowAgents` names the three specialist ids" (https://docs.openclaw.ai/cli/agents).
- **A fallback owner.** `agents.defaults.systemAgent.agentId` catches unbound traffic and "ambient system work" (https://docs.openclaw.ai/concepts/multi-agent).
- **Agent provenance.** "OpenClaw records how each configured agent was created: `operator` ... `agent` when the system agent requested it; and `template`", and an agent can ask for another agent, created "only after operator approval" (same page).
- Name collision: `openclaw directory` is "Directory lookups for" channel "self, peers, groups" (https://docs.openclaw.ai/cli/directory), not a directory of responsibilities.

### 6.3 Persistent agents and short-lived task agents

The distinction exists and is drawn the same way WARM draws it.
- Persistent: each configured agent has its own workspace, state directory and "SQLite-backed session history" (https://docs.openclaw.ai/concepts/multi-agent); the main session is "one rolling conversation across all your channels" (https://docs.openclaw.ai/concepts/main-session).
- Task agents: "Sub-agents are background agent runs spawned from an existing agent run. Each one runs in its own session ... and, by default, **announces** its result back to the requester." "A subagent run ends; a session does not." Sub-agents "do **not** get session or message tools by default" (https://docs.openclaw.ai/tools/subagents).
- Jobs as task agents: the IMAP trigger "starts a separate, isolated agent session for each allowed incoming message" for a "restricted reader agent" (https://docs.openclaw.ai/automation/imap); isolated automation jobs run "a dedicated agent turn with a fresh session" (https://docs.openclaw.ai/automation/cron-jobs/payloads).
- Memory boundary: "Keep personal memory in the human's main session; delegated tasks receive only the context they need and must not read private main-session memory" (coordinator AGENTS.md, above).
- One difference from WARM: in the team preset the specialists are persistent agents with their own workspaces, but the coordinator reaches them "using `sessions_spawn` for a bounded task or `sessions_send` for a follow-up". A persistent agent is also the target of task-sized runs.
- Records outlive the run, as WARM requires: the audit ledger keeps "durable run identity" (https://docs.openclaw.ai/gateway/audit).

### 6.4 Conversation versus scheduled or background work

**What the documentation says now.** "Automations run **inside the Gateway process**, not inside the model" (https://docs.openclaw.ai/automation/cron-jobs/how-it-works). A job chooses where it runs:

| Style | Runs in | Best for |
|---|---|---|
| Main session | "Owning agent's main session" | "Reminders, system events" |
| Isolated | "Dedicated `cron:<jobId>`" | "Reports, background chores" |
| Current session | "Child run of the creating conversation" | "Context-aware recurring work" |
| Custom session | "Persistent named session" | "Workflows that build on history" |

(https://docs.openclaw.ai/automation/cron-jobs/payloads). "System events default to `main`; command and script payloads still default to `isolated`." "Internal automation turns do not extend daily or idle reset freshness; only visible user activity updates session freshness." So OpenClaw separates scheduled work from the conversation per job, not as a rule: running a job inside the main session is still a supported, default choice for system events.

**Heartbeats and their migration to automation jobs.**
- Current text: "Heartbeat monitoring now uses ordinary automation jobs. Doctor converts existing monitors into editable jobs with their own schedules, policies, scratch, and run history." "A scheduled check belongs to an automation job. Its schedule, prompt, scratch, model, session, and delivery settings live with that job." "Background-command, task, hook, and restart follow-ups use normal session execution; they do not require a periodic monitor or an enabled cron scheduler." (https://docs.openclaw.ai/gateway/heartbeat)
- `HEARTBEAT.md`: "OpenClaw no longer creates `HEARTBEAT.md` in new workspaces or reads it at runtime. Monitoring instructions now live in ordinary automation job scratch in the shared state database." (https://docs.openclaw.ai/reference/templates/HEARTBEAT)
- Results: "Meaningful pending results that still belong to the current session move into ordinary session context without sending a notification." (https://docs.openclaw.ai/gateway/heartbeat)
- Notice Doctor prints: "Migrated heartbeats now use standard Automations delivery. Heartbeat-specific duplicate suppression and no-route skipping were removed" (same page).
- Dates, from the repository history of `docs/automation/index.md` and the linked PRs:
  - 2026-04-29: "fix(heartbeat): defer during cron and nested lane pressure" (heartbeat runs competing with other work).
  - 2026-07-23: "convert heartbeat tasks: entries into independent cron jobs" (#113165).
  - 2026-08-26: "unify heartbeat automations under cron ownership" (#129862): "Make system-owned cron monitors the single owner of recurring heartbeat schedules". Shipped in v2026.8.1 ("OpenClaw 2.0", published 2026-08-31), whose notes say "Heartbeat schedules are now managed as Automations" and "OpenClaw no longer reads that file at runtime" (https://docs.openclaw.ai/releases/2026.8.1).
  - 2026-10-21: "migrate heartbeat jobs through Doctor" (#179387), "slice 3 of 4 of the heartbeat-to-Automations migration", implementing "Peter's approved October 3/12 migration design". Slice 4 removes "the retired heartbeat executor and the approved breaking plugin-SDK surfaces"; the SDK migration page already lists `requestHeartbeat`, `runHeartbeatOnce` and the `heartbeat_respond` tool as removed (https://docs.openclaw.ai/plugins/sdk-migration/removed-surfaces).
- A related removal: "The inferred commitments experiment was removed in v2026.8.1: OpenClaw no longer extracts follow-ups from conversations or delivers them through heartbeat." (https://docs.openclaw.ai/automation)

**Removal of TaskFlow and the Tasks ledger.**
- Current text: "Use Sub-agents to launch and wait for delegated runs, ACP for coding harness sessions, and automation run history to inspect scheduled work. Each runtime owns execution and completion. ... The shared Tasks ledger, TaskFlow orchestration API, and TaskFlow Webhooks plugin have been removed." (https://docs.openclaw.ai/automation)
- SDK: "The Tasks registry and TaskFlow orchestration APIs have been removed ... No compatibility facade remains. Use native subagent launch/wait/history APIs, cron run history, and the ordinary Lobster runner." Stored `task_runs` and `flow_runs` rows remain but are "untouched and unused by the runtime" (https://docs.openclaw.ai/plugins/sdk-migration/removed-surfaces).
- History: TaskFlow began as "ClawFlow: add linear flow control surface" (2026-03-31, #58227), was renamed TaskFlow on 2026-04-02, and gained a plugin seam (`api.runtime.taskFlow`, CHANGELOG 2026.4.2). The ledger had retry, cancel and maintenance commands (`openclaw tasks retry`, `tasks flow cancel`) as late as the v2026.9.2 docs.
- Removal merged 2026-09-27 (PR #159179, "refactor: remove Tasks and TaskFlow runtime"). Its stated reason: "**The Tasks ledger duplicated execution and completion state already owned elsewhere.** The cut moves each retained decision to that owner." "This removal introduces no ... replacement ledger." I did not confirm which release first shipped it.

### 6.5 Improvement loops

| Loop | What it changes | Quote and URL |
|---|---|---|
| Self-learning | Learned skills (procedural memory), immediately, with undo | "Self-learning turns corrections and hard-won procedures into learned skills that future sessions load. It is on by default." A background review runs when "a session reaches 10" model iterations. "Every change applies immediately and can be undone"; a `propose` mode saves drafts for review instead. https://docs.openclaw.ai/tools/self-learning |
| Skill Workshop | Learned skills: saves, patches, archives, shrinks | "The agent saves a procedure after hard multi-step work and fixes a learned skill that misled it; skills nobody uses for 30 days are archived." Skill diet "shrinks one oversized learned skill a day". https://docs.openclaw.ai/tools/skill-workshop |
| Dreaming | Durable memory (`MEMORY.md`, `USER.md`), with a diary | "Dreaming is the background memory consolidation system ... It moves strong short-term signals into durable memory while keeping the process explainable and reviewable." Phases run "light -> REM -> deep"; output goes to `DREAMS.md`; "Long-term promotion still writes only to `MEMORY.md`." It runs as scheduled jobs. https://docs.openclaw.ai/concepts/dreaming |
| Advisor (experimental plugin) | The current run only | "reviews ongoing agent work on the session's own model and offers one short correction." https://docs.openclaw.ai/plugins/plugin-inventory |
| Job promotion | Creates a schedule | "When you ask for substantially the same job several times, the agent offers to turn it into a schedule." The agent runs it once as a test and removes it if the test fails. https://docs.openclaw.ai/automation/cron-jobs/how-it-works |

None of the loops changes an agent's definition (`AGENTS.md`, `SOUL.md`) or its standing orders. A retired loop: "The weekly Skill Workshop curator ... is retired"; cleanup "now runs without a schedule" (https://docs.openclaw.ai/automation/cron-jobs/payloads).

## 7. What this says about the model

Each item says whether OpenClaw suggests WARM is **missing a service**, has **cut a boundary in the wrong place**, or has **a service this project does not need**. These are findings from one system, as WARM's own guidance on the reference implementation is.

### Missing services

1. **Admission and capacity control.** Session controller, command queue, parallel specialist lanes, the steering queue and rate limiting all decide which work runs next on shared capacity. WARM's Tasks tracks a unit of work; nothing in WARM decides when it may start or what it may displace. OpenClaw spends five pages on it and calls parallelism "a scarce-resource design problem". Candidate: a Runtime service, "Admit work to sessions and shared model and tool capacity, and queue or reject what does not fit."
2. **Agent provisioning (agent lifecycle).** Bootstrapping, role templates, `agents team create`, agent creation by another agent "only after operator approval", provenance of how each agent was created, and deletion that re-homes bindings. WARM's Registry holds definitions and WARM says domains write them, but no service creates, wires or retires an agent. Candidate: part of Registry, or a separate service.
3. **Inbound interfaces for programs and outside agents.** An OpenAI-compatible endpoint, an OpenResponses endpoint, an MCP relay for ChatGPT and Claude, and a tool-invoke API. WARM's Interaction group has people (Human channels) and this platform's agents (Messaging). Reef adds a third case WARM does not mention: agents of different owners. Candidate: widen Messaging to "agents and programs inside or outside the platform", or add an interface service.
4. **Extension and supply-chain governance.** The plugin host loads implementations of almost every service into slots, and ClawHub runs moderation, acceptable-use rules and security audits on third-party packages. WARM Step 5 treats implementations as outside the model, so it has no place for the mechanism that installs them or for deciding whether a third-party implementation can be trusted. Releases versions changes; it does not vet suppliers.
5. **Smaller gaps.** Prospective memory ("standing intents") is not one of WARM's three memory kinds. A shared coordination log across sessions ("session state awareness") is neither Sessions nor Messaging. A persona (`SOUL.md`) is part of OpenClaw's agent definition but not WARM's.

### Boundaries that may be in the wrong place

6. **Tasks as a separate service (the strongest challenge).** OpenClaw built exactly WARM's Tasks service (a shared ledger with retry, cancel and flow orchestration), ran it for six months, and removed it because it "duplicated execution and completion state already owned elsewhere". Now "Each runtime owns execution and completion": the scheduler keeps its own run history, the sub-agent lifecycle owner tracks sub-agents, restart recovery records interrupted sessions. This suggests Tasks may be a **contract that each runtime implements** (with a shared read model at most, such as the audit ledger) rather than a service with its own state. WARM Step 3 already says contracts are unspecified; OpenClaw's history says the contract may be the whole of it.
7. **The directory is keyed by responsibility; OpenClaw keys routing by origin.** Messages go to the agent bound to the channel, account or peer they came from; a coordinator finds specialists by role text and `agents_list`. OpenClaw has no domain layer at all: roles, teams and standing orders attach to agents. Either WARM's Domain layer and directory become necessary only once a system has several domains (OpenClaw is mostly one personal agent plus helpers), or they are specific to the reference implementation. WARM should state which.
8. **Mechanism and meaning are split differently.** OpenClaw ships meaning in the platform: Deep Research ("source-backed findings and explicit gaps", default-enabled), a work journal (Logbook), team activity reports, HealthKit summaries, default `AGENTS.md` programs, and four role templates. By WARM's test ("if the provider applies its own knowledge or judgment, it is domain work"), these are domain work packaged as platform plugins. WARM's rule is a design choice, so this is not a refutation, but it shows that a product platform ships default domains, and WARM has no word for a platform-supplied domain.
9. **Memory versus Retrieval versus Sessions.** OpenClaw ingests session transcripts into the episodic memory tier at session end, searches memory with the same hybrid search used for retrieval, and treats sessions and memory as one lifecycle surface. WARM's "five services, not five bins" note anticipates this; OpenClaw suggests the Memory and Retrieval line is a policy about trust (memory chunks carry an origin class `owner`, `agent`, `untrusted` or `system`) more than a difference in mechanism.
10. **Evaluation covers more and less than WARM says.** OpenClaw evaluates platform configuration (`openclaw security audit`) and third-party packages (ClawHub audits), which WARM's definition ("behavior and work products") does not cover. It does not evaluate work against domain acceptance criteria. Its improvement loops (self-learning, dreaming) change memory directly with an undo, without passing through Evaluation and Releases as WARM's "improve" stage describes.
11. **Builder tooling versus Human channels.** For a personal assistant the person is also the operator, and the Control UI is both their chat and their console. WARM's line between the two holds for a team platform and blurs for a personal one.

### Points of agreement worth recording

12. **The Harness boundary holds.** OpenClaw swaps the loop (Codex, Copilot, Claude Code, Agents API) while "OpenClaw keeps ownership of channels, sessions, policy, and state". This is WARM's harness-service versus harness-product distinction, independently arrived at.
13. **Scheduled work moved out of a special path.** Heartbeats became ordinary jobs with their own session, scratch, policy and delivery, and the "inferred commitments" feature that delivered through the heartbeat was removed. This matches WARM's observation that unattended work belongs in a job. OpenClaw stops short of WARM's guidance, though: a job may still run in the main session, and system events do so by default.
14. **Persistent versus task agents.** Drawn the same way, including the memory boundary between the main session and delegated work.

### Services this project does not seem to need

15. **Artifacts as a separate store.** Work products live in the agent's workspace and git worktree, and the platform offers storage destinations but leaves retention to each consumer. OpenClaw has not needed a versioned artifact store; WARM's Artifacts may be a responsibility that Environments plus Releases (git) cover.
16. **The directory part of Registry**, for the reason in item 7.

## Sources

Primary: https://docs.openclaw.ai (pages cited inline) and https://github.com/openclaw/openclaw (docs source, release notes and PRs #58227, #113165, #129862, #159179, #179387, read 2026-11-11). Web searches, with results used only to confirm absence or history:
- "docs.openclaw.ai evaluation evals agent quality criteria": third-party results, e.g. [Skill Eval on ClawHub](https://clawhub.ai/skills/openclaw-skill-eval), [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents).
- "openclaw artifacts storage versions agent outputs files docs.openclaw.ai": third-party vendor guides, e.g. [Fastio: OpenClaw file versioning](https://fast.io/resources/openclaw-file-versioning/).
- "openclaw multi-agent which agent handles what routing specialists directory agents_list": [OpenClaw multi-agent docs mirror](https://cdn.jsdelivr.net/npm/openclaw@2026.7.1-2/docs/concepts/multi-agent.md), [notes on OpenClaw multi-agent routing](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenClaw+Multi-Agent+Routing).
- "openclaw Tasks ledger TaskFlow removed run tracking retry cancellation": pre-removal docs, e.g. [Tasks (v2026.7.1 mirror)](https://cdn.jsdelivr.net/npm/openclaw@2026.7.1-2/docs/automation/tasks.md), [tasks CLI (v2026.9.2 mirror)](https://app.unpkg.com/openclaw@2026.9.2/files/docs/cli/tasks.md).
