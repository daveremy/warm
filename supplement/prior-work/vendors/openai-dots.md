---
title: "OpenAI Dots mapped to the 25 WARM platform services"
date: 2026-11-12
author: reader subagent (Claude, model claude-fable-5-2), for sagan
product: "Dots (OpenAI's always-on personal agent in ChatGPT)"
product_version: "No version number is published for dots. Newest entries seen: What's new digest for the week of November 9-13, 2026 (dots: custom instructions); ChatGPT and Codex changelog entry dated 2026-11-11; launch post update dated November 3, 2026 (GPT-6.1 Terra added)."
protocol: prior-work/vendors/protocol-v2.md
status: not yet checked by sagan
---

# How to read this file

- Every quote is from an OpenAI page opened on 2026-11-12. "Live" means fetched directly today. "Snapshot" means the page refused direct access (HTTP 403) and was read today from an Internet Archive copy of the vendor page, taken on the date shown. See Disclosures.
- Availability, unless a row says otherwise: dots are rolling out gradually to Pro and Business Premium accounts (Pro: users 18 and older outside the EEA, Switzerland and the UK), and are "Generally available in eligible workspaces" for Enterprise, Edu and Healthcare, with an admin preview through November 18, 2026. The pages put no maturity label on dots for personal plans; one workspace permission is still labeled "Use dots (Beta)".
- Short page names used in the table: **Meet** = https://learn.chatgpt.com/docs/dots ; **Tasks** = https://learn.chatgpt.com/docs/dots/tasks-and-memory ; **Controls** = https://learn.chatgpt.com/docs/dots/controls ; **Computers** = https://learn.chatgpt.com/docs/dots/computers-and-apps ; **Channels** = https://learn.chatgpt.com/docs/dots/channels ; **Admin** = https://learn.chatgpt.com/docs/enterprise/dots-admin-guide ; **Security** = https://learn.chatgpt.com/docs/enterprise/dots-security ; **Plugins** = https://learn.chatgpt.com/docs/plugins ; **Personalize** = https://learn.chatgpt.com/training/walkthroughs/personalize-your-dot (all live); **Launch** = https://openai.com/index/introducing-dots/ (snapshot 2026-11-06); **Safety post** = https://openai.com/index/how-we-build-safety-security-and-privacy-into-dots/ (snapshot 2026-10-27); **FAQ** = https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs (snapshot 2026-10-30); **Help start** = https://help.openai.com/en/articles/20001530-getting-started-with-your-dot (snapshot 2026-11-07).

# The 25 services

| Group | Service | Value | Quote | URL | Availability and reason |
|---|---|---|---|---|---|
| Runtime | Harness | yes | "Context is the information available to your dot while it responds or works: messages, instructions, relevant source material, and results from its tools or delegated work." | Tasks | Rollout as above. The loop is closed: the user cannot configure it. The same page says "The context available for an interaction is a selection of this information." |
| Runtime | Sessions | yes | "The main dot keeps its own history, configuration and schedules for its lifetime." | Security | Rollout as above. Also: "Dots can preserve cloud computer snapshots across sessions, so work can continue without starting from scratch." Pause, resume, takeover and separate task threads are documented. |
| Runtime | Tasks | yes | "In the desktop app, open your dot’s profile, select Activity, and open a task to inspect its progress, files, results, or requests for input." | Tasks | Activity is in the desktop app. Tasks are listed as In progress, Scheduled and Completed (Help start) and can be stopped one by one (Controls). Retry and recovery are not described; the vendor warns "A completed run doesn’t by itself confirm that the requested result was achieved or delivered." |
| Runtime | Environments | yes | "Your dot has its own computer and browser in the cloud for research, files, and running software." | Meet | Rollout as above; admins can turn browser, network and computer use off. Safety post: "We also isolate users’ cloud environments from one another". A connected local computer and Codex cloud environments are optional extra places. |
| Runtime | Scheduling | yes | "You can also specify a time or a supported event that should trigger work." | Tasks | Rollout as above. The dot also "can decide when to pause and wake up to continue". Event triggers only "When a connected service supports event monitoring". No limit on how much may run at once is stated. |
| Runtime | Lifecycle | yes | "Open Admin Console > Dots to see the personal dots created in your workspace. Use the inventory to find a dot and review its owner and status, then open its details to manage it." | Admin | Create, Pause, Resume and Delete are available to every owner (Controls). The inventory is Enterprise only. One personal dot per member; background agents are not listed as agents. |
| Knowledge | Memory | part. DISPUTABLE (yes) | "It also keeps its own notes about preferences, decisions, and ongoing work so it can use them in later conversations." | Tasks | Retention across sessions and updating are stated ("your dot can update these notes to reflect new decisions and changing priorities"). Where each entry came from is not stated, and the FAQ says "You currently cannot view, delete, or directly modify individual dot memories". Yes is defensible because the notes persist and are kept current. |
| Knowledge | Retrieval | yes | "Your dot can search your past ChatGPT conversations for relevant context." | Tasks | Rollout as above. Connected apps are the other named sources: "use Gmail to find relevant email, Google Drive to work with documents" (Meet). |
| Knowledge | Artifacts | part. DISPUTABLE (yes) | "Select a task to review its progress, files, and results, including work happening in the background." | Controls | Files and results are kept per task and in an Outputs list; other copies live in ChatGPT Library, Space or connected storage (FAQ). No versions of a dot's outputs are described in the dots pages or in the Space pages doc. Yes is defensible on storage alone. |
| Capabilities | Models | yes | "Your dot can draw on different models for different parts of its work." | Meet | Two OpenAI models (GPT-6 Astra, GPT-6.1 Terra); one vendor. The choice is the product's: "Enterprise model controls and defaults do not apply to the main dot" (Admin). |
| Capabilities | Tools | yes | "Through each plugin, the dot can only access data and take actions that the connected account, the plugin permissions, and the workspace settings allow." | Security | Rollout as above. Also "Auto-review checks tool calls labeled “write” before they run." Tools are plugins (MCP servers), the cloud browser and computer, and optional local tools. |
| Capabilities | Registry | part. DISPUTABLE (yes) | "Both products use one universal plugin directory, so the same public plugins are discoverable from their supported surfaces." | Plugins | The directory holds tools and skills, not agent definitions, and the Plugins page does not mention dots; Meet says only that a dot "can use supported" plugins "installed and enabled for your account". Versions are stated only for workspace marketplaces synced from GitHub ("A fixed commit keeps the version you selected", https://learn.chatgpt.com/docs/enterprise/plugin-management). Yes is defensible because skills are found and loaded "when needed". |
| Interaction | Directory | part (derived) | derived from C3 = part and C4 = part | see C3 and C4 below | derived |
| Interaction | Messaging | part. DISPUTABLE (yes) | "Your dot can check results and send follow-up instructions to tasks it created." | Meet | Messages pass only between a dot and the background agents and task threads it started. Events: "When a connected service supports event monitoring, you can instead ask your dot to respond to a specific event." (Tasks). No messaging between dots: "Over time, we envision teams of dots working together" (Launch). Yes is defensible because both halves have a stated feature. |
| Interaction | Orchestration | yes | "Your dot can divide work among background agents that run in parallel and report back to it." | Tasks | Rollout as above. The dot also delegates to ChatGPT Work and Codex and hands steps back to the owner. Dependencies between tasks are not described. |
| Interaction | Channels | yes | "You reach the same dot in ChatGPT, Slack, Teams, or a call." | Meet | ChatGPT desktop, web and mobile apps; Slack and Teams need an admin permission in workspaces; texting (iMessage, RCS) is beta for Pro users in the U.S.; the dot cannot yet start a call. |
| Governance | Identity | yes | "The details include the member who created the dot, its active or paused status, its identity, and its Slack or Microsoft Teams connection status. The identity is the dot’s service account, or its dot ID when a service account isn’t available." | Admin | The inventory and admin revocation are Enterprise only. In connected apps the dot acts as its owner ("Acting identity: dot owner", Security); a separate Slack identity is optional. Specialist dots "with their own identity for access management" are a preview (Launch). |
| Governance | Secrets | yes | "For supported sign-ins, OpenAI sends the password directly from the private form to the cloud browser without exposing it to the model." | Security | Supported sign-in and saved-password flows only. Vendor caveat on the same page: "Code on the dot’s computer can read an app token or browser cookie if its value is exposed to that code". |
| Governance | Policy | yes | "Before your dot takes an action that could affect your accounts or share information, an automatic review checks it against your instructions, permissions, custom rules, and built-in safety requirements." | Controls | Custom rules need a workspace permission in Enterprise. Limits the vendor states: "Auto-review coverage across browser, desktop, and delegated actions remains under review" (Security); custom rules "are instructions your dot tries to follow, and it can make mistakes" (Controls). Retention rules exist for workspace files and snapshots, not for the dot's own notes. |
| Governance | Approvals | yes | "A specific instruction can cover future actions within that scope; an action outside it needs another decision." | Controls | Rollout as above. Held single actions: "If it’s waiting for a decision, app connection, sign-in, or approval, open the request and respond to continue." Advance approvals are saved as custom rules or schedules; a record of each single decision is not described. |
| Operations | Observability | yes | "Supported dots records include user prompts and responses, supported tool-call events, and connected-app MCP calls and results." | Admin | The Compliance API and audit logs are Enterprise only; every owner has Activity ("You can also review steps your dot has taken", FAQ), in the desktop app. Vendor limit: "Even with status=completed, the detailed output may be missing." (Security). |
| Operations | Evaluation | no. DISPUTABLE (part) | Searched all pages below for "evaluat", "criteria", "verify", "test", "check". Found only action checks (Auto-review) and safety monitoring, counted under Policy, and the warning "A completed run doesn’t by itself confirm that the requested result was achieved or delivered." | Tasks | Nothing assesses work products against stated criteria or reports "unknown". Part is defensible because safety monitoring assesses behavior: it "looks for potentially harmful behavior, such as attempts to bypass a safeguard or act outside the owner’s instructions" (Security). |
| Operations | Improvement | part | "Review how your dot summarizes the change, correct anything it misunderstood, and ask it to remember the guidance you want to keep." | Personalize | Feedback from the owner changes the dot's notes, instructions and rules ("Dots can help you write Custom Rules, but they need your approval to change them", Safety post). No feature turns traces or evaluations into proposed changes. |
| Operations | Releases | no. DISPUTABLE (part) | Searched the dots pages for "version", "rollback", "revert", "restore", "undo", "release". Found nothing for a dot's instructions, rules or memory; "Deletion can’t be undone." (Help start) | Help start | Part is defensible because workspace plugins (skills and tools a dot can use) sync from a pinned commit and "If an update is invalid, the existing plugin keeps its last working version." (https://learn.chatgpt.com/docs/enterprise/plugin-management); that page does not mention dots. |
| Operations | Reliability | part | "Cloud work can continue while your devices are off, and the computer can keep its state between periods of use." | Computers | The vendor hosts the service and says "It’s available 24/7" (Launch). No page read describes how service is restored after a failure, and none states a service level. The status page (status.openai.com) is linked from the footers and was not opened. |

Counts: 16 yes, 7 part (including Directory), 2 no. Six cells are marked DISPUTABLE; C1 below is a seventh.

# Four further questions

## 1. Areas of work (C1 to C4)

| Criterion | Value | Quote | URL | Reason |
|---|---|---|---|---|
| C1. An area of work exists in the model | part. DISPUTABLE (yes) | "You choose who can use dots, configure their capabilities, and manage personal dots across your workspace." | Admin | The only defined unit that holds more than one dot is the workspace, which is the whole system; the pages define no way to divide a workspace's dots into areas. Yes is defensible because groups are defined, several can exist side by side, and they hold members who own dots ("Groups organize people in a ChatGPT workspace and can carry custom roles", https://learn.chatgpt.com/docs/enterprise/groups-and-provisioning); but a group is described as a set of people with "a shared access need", and dots do not belong to groups. Personal plans have no unit at all. Specialist dots (preview) "take on dedicated responsibilities within your organization" (Launch): there the unit is one agent. |
| C2. The area is specified apart from who does the work | part | "Workspace owners manage access through workspace defaults and custom roles." | Admin | Rated on the workspace. It has owners, roles, permissions and capabilities, but no statement of what the unit is for. The roles are access roles. For specialist dots the responsibilities are set per agent: "Our engineering teams will work directly with organizations to define each dot’s responsibilities, the tools it can use, and how people review and approve its work." (Launch) |
| C3. A record of accountability | part | "Use the inventory to find a dot and review its owner and status, then open its details to manage it." | Admin | The inventory names one owner per dot (per agent), not per responsibility or capability. Enterprise only. |
| C4. Finding where to send work | part | "It can keep you updated in ChatGPT, Slack, or Teams and delegate tasks to ChatGPT Work or Codex." | Meet | The dot routes work to Work, Codex and its background agents by its own logic. No lookup from a kind of work to a handler is described. People can pick an agent from a mention menu in Space ("Type @ in a page to open the mention menu and choose your dot", https://learn.chatgpt.com/docs/space/agents). |

Directory (derived): C3 = part and C4 = part, so **part**.

## 2. Supplied agents for an area of work

No ready-made dot for a named area of work is on offer today. What the pages do name:

- **Specialist dots** (preview, focused enterprise pilots, built with OpenAI's engineers, not ready-made): "We’re building on lessons from early testing inside OpenAI across procurement, invoice processing, email marketing, customer support, and commercial contracting." and "We’re starting with focused enterprise pilots." (Launch)
- **Codex** and **ChatGPT Work**, to which a dot delegates. Codex is the vendor's agent for software work: "When you want to build, debug, test, or review software and work directly with code and developer tools." (Meet)
- **Plugins built by OpenAI** in the plugin directory, some for a named area, for example software security: "Install the Codex Security plugin to scan authorized code and confirm plausible vulnerability findings." (Plugins). The pages do not say which plugins a dot supports.
- The role examples on the product page (finance lead, sales lead, engineer, developer, content creator; https://chatgpt.com/features/dots) are illustrations, not supplied agents or skills.

Searched: all pages listed below for "specialist", "role", "skill", "template", "department", "domain". Not opened: openai.com/business/plugins (403).

## 3. What fits nowhere

- **Self-started search for work to do** (proactive research): "When you aren’t actively working with it, your dot looks for ways to help in the background. We call this “proactive research”." (Launch). Scheduling decides when assigned work starts; this decides what work to propose.
- **Persona and appearance**: "Give your dot a name and choose its shape, color, eyes, glasses, and accessories." (Meet)
- **Usage metering and billing**: "Eligible Enterprise workspaces can pay a flat rate based on the type of work a dot does or pay based on consumption." and "Workspace analytics includes enabled-dot counts and total active users of dots." (Admin)
- **A person taking over the agent's computer**: "Select Take over to use its mouse and keyboard, then Return control when your dot can continue." (Computers). Close to Approvals and Environments, but it is shared control of the workspace, not an authorization.
- **Data residency and customer-managed keys**: "For eligible workspaces with EKM enabled, your workspace’s customer-managed key protects saved cloud computer snapshots and saved browser cookies at rest." (Security)
- **Control over the vendor's use of the data for model training**: "For personal ChatGPT plans, your “Improve the model for everyone” setting controls whether your dots’ conversations and work may be used to improve our models." (FAQ)
- **Product feedback to the vendor through the agent**: "To report a bug, suggest a feature, or give product feedback, tell your main dot in conversation." (https://learn.chatgpt.com/docs/whats-new/november-2-6-2026)

## 4. Where it runs and what the user supplies

- **Where it runs**: the vendor's cloud, and optionally the user's machine as well. "Your dot lives in the cloud and has its own computer and browser." (Meet). "Access to your local computer is optional and starts turned off." (Help start). With a connected computer, "the command that reads the file runs on your laptop" while "A dot coordinates work in the cloud." (Security)
- **Keeps running when the user is away**: yes. "You can reach it and it can keep working even when your computer is off." and "Your dot works between conversations." (Meet). Local work is the exception: "Your computer must be online with the ChatGPT app open for your dot to use it." (Meet)
- **What the user supplies**:
  - An eligible plan and region: "Dots are rolling out today in ChatGPT to Pro and Business Premium users in eligible markets" (Launch); in Enterprise, an admin grant ("grant Use dots on the group’s custom role", Security).
  - App connections: "Each plugin must be connected and permitted to perform the actions you request." (Meet)
  - The responsibility, sources and boundaries, in words: "Describe the responsibility and share the source material it needs, then review its work and explain what needs to change." (Meet)
  - For repository work, an environment made beforehand: "Create the environment in Codex before asking your dot to use it." (Help start)
  - Review: "Dots can still make mistakes, so always review consequential work." (Launch)
  - Nothing has to be built. Custom instructions, custom rules, a connected computer and extra channels are optional.

# Pages opened (all on 2026-11-12)

Live (fetched directly):

- https://learn.chatgpt.com/docs/dots (Meet dots; both nav variants)
- https://learn.chatgpt.com/docs/dots/getting-started
- https://learn.chatgpt.com/docs/dots/channels
- https://learn.chatgpt.com/docs/dots/computers-and-apps
- https://learn.chatgpt.com/docs/dots/controls
- https://learn.chatgpt.com/docs/dots/tasks-and-memory
- https://learn.chatgpt.com/docs/enterprise/dots-admin-guide
- https://learn.chatgpt.com/docs/enterprise/dots-security
- https://learn.chatgpt.com/docs/enterprise/cloud-local-access
- https://learn.chatgpt.com/docs/enterprise/agent-security (lines that mention dots)
- https://learn.chatgpt.com/docs/enterprise/plugin-management (lines on versions)
- https://learn.chatgpt.com/docs/enterprise/groups-and-provisioning (opening section)
- https://learn.chatgpt.com/docs/enterprise/roles-and-workspace-permissions (lines that mention dots)
- https://learn.chatgpt.com/docs/space/agents
- https://learn.chatgpt.com/docs/space/pages (searched for versions; none found)
- https://learn.chatgpt.com/docs/sandboxing/auto-review
- https://learn.chatgpt.com/docs/plugins
- https://learn.chatgpt.com/docs/skills-and-plugins
- https://learn.chatgpt.com/docs/feature-maturity
- https://learn.chatgpt.com/docs/working-with-agents (lines that mention dots)
- https://learn.chatgpt.com/docs/whats-new (newest week: November 9-13, 2026)
- https://learn.chatgpt.com/docs/whats-new/november-2-6-2026
- https://learn.chatgpt.com/docs/whats-new/dots-october-28-2026
- https://learn.chatgpt.com/docs/whats-new/dots-october-9-2026
- https://learn.chatgpt.com/docs/whats-new/devday-2026
- https://learn.chatgpt.com/docs/changelog (newest entry 2026-11-11; searched for dots)
- https://learn.chatgpt.com/training/walkthroughs/personalize-your-dot
- https://chatgpt.com/features/dots
- Fetched and searched for "dot", no mention found, not otherwise read: /docs/automations, /docs/enterprise/compliance-api, /docs/enterprise/teams, /docs/enterprise/service-accounts, /docs/enterprise/skills, /docs/models, /docs/long-running-work, /docs/customization/memories, /docs/enterprise/workspace-model-availability, /docs/notifications (all on learn.chatgpt.com)

Internet Archive snapshots of vendor pages (direct access returned 403):

- https://openai.com/index/introducing-dots/ (snapshot 2026-11-06; post dated September 29, 2026, updated November 3, 2026)
- https://openai.com/index/how-we-build-safety-security-and-privacy-into-dots/ (snapshot 2026-10-27; post dated September 29, 2026)
- https://help.openai.com/en/articles/20001530-getting-started-with-your-dot (snapshot 2026-11-07, "Updated: 4 hours ago")
- https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs (snapshot 2026-10-30, "Updated: 2 days ago")
- https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces (snapshot 2026-10-06; it describes the earlier Enterprise beta, so no cell rests on it)
- https://help.openai.com/en/articles/6825453-chatgpt-release-notes (snapshot 2026-11-08; newest entry November 4, 2026; dots entries: "Meet your dot" and October 28, 2026 "Texting your dot")
- https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes (snapshot 2026-10-30; searched for dots, no entry found)

# Disclosures and what could not be opened

- **openai.com and help.openai.com refused every direct request today** (HTTP 403 to curl and WebFetch; a bot challenge in a signed-in browser, which I did not try to pass). The seven pages above were therefore read from Internet Archive snapshots 5 to 37 days old. The pages may have changed since. Cells that rest on a snapshot alone: none of the 25 (each has a live quote or a live page behind its value), but several reasons cite snapshot quotes (FAQ, Launch, Safety post, Help start), as do parts of questions 2 to 4.
- The Internet Archive index went offline during the session, so I could not look for newer snapshots, in particular of the "Manage dots in ChatGPT workspaces" article.
- **Not opened**: openai.com/business/plugins (403); chatgpt.com/dots (needs sign-in); status.openai.com; the system card at deploymentsafety.openai.com (reachable, not read); Help Center articles 20001495 (app permissions), 20001256 (plugins), 9261474 (compliance platform), 20001069 (HIPAA); the Help Center collection page (rate limited); the Admin API reference.
- **Product not used.** Nothing here was checked against a running dot. Every value is what the vendor's pages state.
- Web search was used only to find vendor pages. Its result summaries quoted press coverage; no cell uses them.
- Under  I read only protocol-v2.md and rerate-criteria-v2.md. I did not list the directory, and no search printed content from another file there.
- The shared plugin directory, Space, ChatGPT Work and Codex are separate ChatGPT features that a dot uses. Where a value depends on one of them (Registry, Artifacts, Releases), the row says so.
