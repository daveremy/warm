---
title: "Gemini Spark (now Tasks in Gemini) mapped to the 25 WARM platform services"
date: 2026-11-12
author: claude (reader for sagan, protocol-v2)
product: "Google Gemini Spark, renamed Tasks in Gemini (task mode in the Gemini app)"
version: "No version number is published. Newest entry on gemini.google/release-notes: 2026.10.13. Newest entry that names Spark: 2026.06.30. Help center pages carry no date; read 2026-11-12."
status: not yet checked by sagan
---

# What was rated

Google has renamed the product. The help center says: "Since May, we've been testing Spark in beta with our subscribers. As people used it, they really wanted Gemini to just help them finish "tasks." That's the word that kept coming up, so we renamed it Task to make it easier to understand." (https://support.google.com/gemini/answer/17094507). The Privacy Hub calls it "Tasks in Gemini (formerly known as Spark)" (https://support.google.com/gemini/answer/13594961). The rename has no date on the pages I opened. I rated the product as the current help center describes it, and used the Spark launch posts (May and June 2026) only where marked.

**Availability (written "TA" in the table).** Tasks in Gemini is offered to people who are "18 or over", signed in "with a personal Google Account", with "a Google AI Pro or Ultra subscription" and "Keep Activity on"; "Available wherever Gemini Apps are supported, except in the European Economic Area, Nigeria, Switzerland, and the United Kingdom"; "Only available in the Gemini mobile app, the Gemini app on Mac, and the Gemini web app at gemini.google.com." The vendor does not call it generally available: "Gemini’s ability to handle tasks is experimental." (all from answer/17094507).

Short URLs in the table: `H/<id>` means `https://support.google.com/gemini/answer/<id>`.

# The 25 services

| Service | Value | Quote | URL | Availability |
|---|---|---|---|---|
| Harness | yes | "Planning info: Gemini is designed to show you what it’s planning to do after you submit a prompt, its progress as it works on your task, and any relevant Skills, Connected Apps, and files used or created." Launch post: "Gemini Spark runs on Gemini 3.5 and uses the Antigravity harness." | H/17094507; https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/ (May 19, 2026) | TA |
| Sessions | yes | "To change Gemini’s approach while the task is running, just enter additional instructions in the text box. Gemini updates its work without losing progress." "If you turn task mode back on: Gemini will automatically resume paused tasks and schedules." "your task activity is manageable in Gemini Apps Activity" | H/17094507; H/13594961 | TA |
| Tasks | part. DISPUTABLE (yes) | "Next to your task threads, check the icon for the progress of your tasks. Ready / Needs attention / In progress". "If you want to completely cancel a task yourself, in the Gemini text box, click Stop." Reason for part: tracking, cancellation and the kept thread are described; retry of a failed task is not. A reader who counts the fallback ("Gemini tries to figure out the next steps to continue your task") as recovery rates yes. | H/17094196; H/17094507 | TA |
| Environments | yes | "To interact with websites, Gemini can connect to the local Chrome browser on your desktop or use a separate remote browser in the cloud." "Gemini can use a remote browser with automatically saved info and remote computer with code execution data for your tasks." On Mac: "Gemini can only view files or directories that you specifically add to the Connected folders toolbar." | H/17094507; H/17208717 | TA. Local Chrome only on desktop |
| Scheduling | yes | "Gemini currently supports three types of schedules. Time-based: schedule tasks to run once, hourly, daily, weekly, monthly, or yearly. ... Gmail monitors: schedule tasks to run when you receive an email that satisfies a Gmail filter. ... Topic monitors". "You can have at most 15 tasks running at a given time. A schedule will not run if there are already 15 tasks currently running." | H/17094710 | TA |
| Lifecycle | part | "If you turn off task mode: ... Your schedules and tasks are paused and not deleted." "If you turn task mode back on: Gemini will automatically resume paused tasks and schedules." Reason: the one agent can be suspended and resumed; there is no creating or ending of agents and no list of agents. | H/13594961 | TA |
| Memory | part. DISPUTABLE (yes) | "Gemini can use Personal Intelligence for your tasks, which includes: Memory of your past Gemini chats; Instructions for Gemini". "You can review a chronological record of the updates made to your Memory summary." Reason for part: the pages describe retaining and correcting facts and when each changed, not where each entry came from. | H/17094507; H/18617127; H/16598625 | Memory needs a personal account, 18+, Keep Activity on; "remember" requests US only; memory summary not on Mac |
| Retrieval | yes | "To add files to your task, click Upload & tools, then one of the following options: Upload files / Add from Drive / Add Notebook". "Search & manage your Google Drive files: Search for files, read file contents, rename or delete files, check metadata, and view recent documents." | H/17094507 | TA |
| Artifacts | part. DISPUTABLE (yes) | "When Gemini creates files as part of your task, you can access them directly in the task thread." Versions are described only for Canvas documents: "To view your saved versions, at the top, click Previous Version or Next Version." Reason for part: no versions are described for the other file types a task creates. | H/17094507; H/16047321 | TA |
| Models | part. DISPUTABLE (yes) | "To change the Gemini model or thinking level, click the model menu at the top." The models table lists, under "Available Models (Tasks)", Hydrogen and Argon for the Pro plan and Hydrogen, Argon and Carbon for the Ultra plan. Reason for part: several models of one vendor, chosen by the user per thread; automatic routing ("your prompts are automatically routed to the most efficient model and thinking level") is not stated for tasks. | H/17094507; H/18648722 | TA |
| Tools | yes | "Gemini can use some Connected Apps and certain Google services for your tasks, including: Custom apps. ... Several third-party apps." "add a custom app with its Model Context Protocol (MCP) server URL in the Gemini web app" | H/17094507; H/17209137 | TA. Custom apps: US, English, not in the Mac app |
| Registry | part | "Check if a skill is relevant. Gemini only checks the skill’s name and description to determine if a skill is relevant for your task." "The Connected Apps page lists apps that are available to you". Reason: skills and apps are held, found and loaded on need, but no versions: "To update files in a skill, you need to upload the entire skill with its reference files again." | H/17102773; H/13695044; H/17094296 | Skills: all signed-in users 18+ |
| Directory | no (derived). DISPUTABLE (part) | Derived from C3 = no and C4 = no. It becomes part if either C3 or C4 is read as part (see question 1). | n/a | n/a |
| Messaging | no. DISPUTABLE (part) | Searched the eight task help pages, the release notes and the Privacy Hub for "sub-agent", "subagent", "agents", "message" between agents: nothing. The only event delivery is to a schedule ("schedule tasks to run in response to specific events"), which I counted under Scheduling; a reader who counts it here rates part. | H/17094710 | n/a |
| Orchestration | part | "For certain steps, like signing in to a website, the task pauses until you take over and complete that step." "Mix and match skills: Use multiple skills for a single task ... You can even use skills with other skills." Sub-agents were announced and are not in the current help pages: "We'll also be adding new abilities, including texting and emailing Spark, creating custom sub-agents and operating your local browser." | H/17094507; H/17094296; https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/ | TA; sub-agents announced May 19, 2026, not found as available |
| Channels | part. DISPUTABLE (yes) | "Only available in the Gemini mobile app, the Gemini app on Mac, and the Gemini web app at gemini.google.com." "You can ask the Gemini app to take action on your Mac from another device, like your phone." Reason for part: every channel is a Gemini app. Reaching the agent by email or chat was announced ("in the Gemini app or soon, through email and chat") and is not in the current help pages. | H/17094507; H/17208717; https://blog.google/innovation-and-ai/sundar-pichai-io-2026/ | TA |
| Identity | part | "Sign in to the Gemini app with a personal Google Account." "When acting on your behalf, Gemini will share necessary info with third parties." "You can unlink an MCP server from your Google Account and revoke its permissions". Reason: the agent acts under the user's Google Account; no separate agent identity or accountable-person record is described. | H/17094507; H/17209137 | TA |
| Secrets | part. DISPUTABLE (yes) | "With your permission, Gemini in Chrome can get help from Google Password Manager and Sign in with Google to sign in to sites for you. Google doesn’t share your passwords with Gemini in Chrome or other sites." Reason for part: this covers website passwords in local Chrome on desktop only; in the remote browser "it’ll ask you to take over and sign in manually", and no store for other values is described. | H/16821166; H/17094507 | Chrome auto browse, desktop only |
| Policy | part. DISPUTABLE (yes) | "Under “App actions,” next to the action, click the dropdown and select your permission preference: Always allow: Gemini runs this action without asking. Always ask: Gemini asks before running this action." "Site and action restrictions: Gemini restricts its browsing activity to the websites and actions relevant to your task." "By default, your Gemini Apps activity older than 18 months is auto-deleted." Reason for part: rules are the vendor's fixed safeguards plus an allow/ask setting per action; no user-written rules and no grant are described. | H/18766567; H/17094507; H/13278892 | TA |
| Approvals | yes | "Always allow: Approves the action for the current thread and all future task threads. Selecting this automatically updates your preference to “Always allow” in your settings." "Even if you update your permission preferences, very sensitive actions require your permission each time." | H/18766567; H/17094507 | TA |
| Observability | yes | "To show this task thread’s work panel, at the top of the thread, click the progress chip. Here you can find the steps and progress of tasks in a thread." "In the task thread’s work panel, under “Files,” you can review the files that Gemini read or updated for tasks in the thread." | H/17094507 | TA |
| Evaluation | no | Searched the task, skills, schedules and auto browse help pages for "evaluat", "verify", "criteria", "quality", "unknown": no feature. The auto browse page lists as a risk "Confirming a task is done when it’s not or could have done more". | H/16821166 | n/a |
| Improvement | no. DISPUTABLE (part) | No feature turns traces or evaluations into proposed changes. A reader may count "Gemini can now help you build custom skills from your chats" (release notes 2026.09.30) as part. | https://gemini.google/release-notes/ | n/a |
| Releases | no | Searched skills and task pages for "version", "roll back", "release", "restore". Found only "If you delete a skill, it can’t be undone." and "Copies don’t automatically sync when the original skill is updated." | H/17094296 | n/a |
| Reliability | no. DISPUTABLE (part) | Searched for "outage", "restore", "recover", "availab", "retry": no feature that keeps the service available. A reader may count the browser fallback as part: "If you close or turn off your device before the task is finished, or the device isn’t available, Gemini might use a remote browser to complete the task." | H/17094507 | n/a |

# Four further questions

## 1. Areas of work (C1 to C4)

- **C1: no. DISPUTABLE (part).** The task model has tasks, schedules and skills ("A task is your high-level goal", "A skill is a set of reusable instructions", "Each skill is built for a single job"), none of which is an area of work. The nearest unit is the notebook: "you can use notebooks to organize your projects in a dedicated, focused space" and task threads can be added to one (H/16972047, H/17094196). I rated no because the examples are projects ("Plan a trip or vacation", "Apply for a job"), which the version 2 ruling treats as activities, and no agent or role belongs to a notebook. A reader who takes a notebook as a unit that divides the user's work rates part (a user can have several; the unit is defined but holds no agents or roles).
- **C2: no. DISPUTABLE (part).** No unit found under C1. If the notebook is the unit, it has properties at the unit level, "Notebooks provide a continuous chat experience that remembers your sources, instructions, and ongoing discussions" and "Give instructions for your notebook" (H/16972047), but no statement of what it is responsible for and no roles: part.
- **C3: no. DISPUTABLE (part).** Searched for "owner", "accountab", "responsib" on the task, skills and Connected Apps pages. No record of accountability. Two records name an owner or a provider and could be read as part: a shared skill has one owner ("A skill can only be shared by its owner and individuals with Editor access"; "Transfer ownership of a shared skill", H/17094296), and the Connected Apps page lists each app with its "supported and unsupported actions" (H/13695044). I rated no because the skill owner is an access role for sharing a file, not a statement of who answers for a responsibility.
- **C4: no. DISPUTABLE (part).** There is one agent and no other agent or role to find. The agent matches a kind of work to a skill or app inside its own logic: "Gemini automatically uses skills: Gemini can automatically use activated skills based on the context and intent of your task." (H/17094296). A reader who counts that as routing inside one orchestrator rates part.
- **Directory (derived): no.** Part under either disputed reading.

## 2. Supplied agents for an area of work

No ready-made agents or roles for a named area of work were found in the task product. What the vendor supplies:

- Two premade skills: "Get ready for your next call using the premade /prep-for-meetings skill." and "Use the premade /match-my-writing-style skill to write faster while maintaining your unique voice and tone." (https://gemini.google/overview/productivity/)
- Skill templates, not named in the help page: "On the Skills page under “Recommended,” click the skill template you want to use." (H/17094296)
- Two notebook types for an area: "Study notebooks let you upload notes or study materials to create personalized, interactive lessons." and "you can create a business notebook to help you manage and grow your business." (H/16972047). The small-business hub: "From this central hub, they can build their brand, analyze finances, understand customer insights, and more." (https://blog.google/innovation-and-ai/products/gemini-app/new-tools-small-business-owners/, Oct 20, 2026). These are spaces and pages, not agents.
- Coding agents, in a separate product inside the same Mac app: "Antigravity gives you a dedicated space to build with coding agents in the Gemini app for Mac." (H/18755601). Not part of Tasks in Gemini.

Searched: the eight task help pages, the skills pages, gemini.google/overview/productivity, the release notes, and the Gemini app blog feed back to September 2026.

## 3. What fits nowhere

- **Usage metering and quotas.** "Gemini Apps have compute-based usage limits that determine how much you can interact with Gemini tools and features. ... If you’re close to your limit, Gemini lets you know." (H/17094507). Scheduling covers how much may run at once, not how much compute a user may spend.
- **Undo for the agent's changes to the user's own data.** "When Gemini works with your computer files, it will create temporary backup files. You can choose to recover these backup files before moving on to your next task. Backup files are deleted when you start a new query or task, or after 24 hours." (H/17208717). "To undo Gemini’s action, click the link in Gemini’s confirmation and make your changes in the Workspace service." (H/17094507)
- **Live takeover of the agent's environment by the person.** "Click Take over task and then Take over task. Complete your steps. To give back control to Gemini, at the top, click Go back to Gemini." (H/17094507). Approvals covers a yes or no on a held action; here the person does the step.
- **Onboarding by interview.** "You can get help with setting up your first skills and tasks conversationally. Just enter “set up,” “get started,” or “interview me” in a task." (H/17094507)
- **Sharing a skill with other people.** "Select their access level: Viewer or Editor." (H/17094296)

## 4. Where it runs and what the user supplies

- **Where.** Both, with the vendor's cloud as the base. "Gemini runs in the cloud instead of on your phone or computer. This means it keeps working even if your device is turned off." (H/17094710). "To interact with websites, Gemini can connect to the local Chrome browser on your desktop or use a separate remote browser in the cloud." (H/17094507). On a Mac it also acts on local files: "You can use Gemini as a partner to manage and modify files directly on your Mac desktop." (H/17208717). At launch Google said: "It runs on dedicated virtual machines on Google Cloud. And it’s 24/7 so you don’t need to keep your laptop open." (https://blog.google/innovation-and-ai/sundar-pichai-io-2026/, May 2026)
- **Running while the user is away.** Yes for cloud work: "If you use the remote browser: Gemini continues to work on your task even if you close your device". Not for local work: "For Gemini to work on a task using your local browser, you’ll need to keep your device and Google Chrome awake and running." (H/17094507); "The Gemini app must be set up and running on your Mac." (H/17208717). Some steps wait for the person: "For certain steps, like signing in to a website, the task pauses until you take over and complete that step."
- **What the user supplies.** A paid plan and settings: "Have a Google AI Pro or Ultra subscription." "Have Keep Activity on." (H/17094507). The work definition: "you define the task (what you want), set the schedules (when it should happen), and provide the skills (how to do it) to complete the work." (H/17094507). Connections: apps the user connects, and for a custom app "the MCP server URL for the custom app" (H/17209137). Supervision: "Your active supervision is the most important way to protect against risk when you assign tasks to Gemini." (H/17094507). The user builds no infrastructure.

# Pages opened (all read 2026-11-12)

Google help center (support.google.com/gemini/answer/<id>):

- 17094507 Manage your tasks & workflows in Gemini Apps (Computer and Android views)
- 17094196 Find & manage your tasks in Gemini Apps
- 17094710 Create & manage schedules for tasks in Gemini (Computer and Android views)
- 17094296 Create & manage skills for Gemini Apps
- 17102773 Write effective skills for Gemini Apps
- 17208717 Assign tasks in the Gemini app on Mac
- 17209137 Connect & manage custom apps for Gemini Apps
- 18766567 Manage browser & app permissions for tasks in Gemini
- 18648722 About Gemini models
- 16821166 Ask Gemini in Chrome to complete tasks for you with auto browse
- 13695044 Use & manage Connected Apps in Gemini; table/17434654 availability of Connected Apps
- 16598406, 16598469, 16598623, 16598625, 18617127 Personal Intelligence, Memory, instructions, memory summary
- 13278892 Manage & delete your activity in Gemini Apps
- 13594961 Gemini Apps Privacy Hub (section "Tasks in Gemini")
- 16972047 Organize your projects with notebooks in Gemini Apps
- 16047321 Canvas; 16275805 limits & feature availability; 17077455 daily brief; 17011627 Gemini app on Mac; 18755601 Antigravity in the Gemini app on Mac; 14620100 work or school accounts
- Downloaded and only skimmed or searched by keyword: 18116629 (Google Photos workflows), 16316416 (schedules in chats), 14959807, 13278668, 14286560, 14517446, 17216260

gemini.google:

- https://gemini.google/release-notes/ (newest entry 2026.10.13; Spark entries 2026.05.19 and 2026.06.30)
- https://gemini.google/about/ and https://gemini.google/overview/productivity/ (also downloaded, not used: /overview/apps/, /overview/personal-intelligence/)

blog.google:

- https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/ (May 19, 2026)
- https://blog.google/innovation-and-ai/sundar-pichai-io-2026/ (May 2026)
- https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/
- https://blog.google/products-and-platforms/products/workspace/workspace-updates/
- https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/ (Jun 30, 2026)
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/
- https://blog.google/innovation-and-ai/products/gemini-app/new-tools-small-business-owners/ (Oct 20, 2026)
- https://blog.google/innovation-and-ai/technology/developers-tools/connected-apps-one-place/ (Oct 28, 2026)
- Gemini app blog RSS feed (newest item Nov 12, 2026), and the monthly AI roundups for August, September and October 2026, searched for "Spark" and "task mode". Also downloaded and searched, nothing used: edit-files-directly, gemini-4-argon-availability, new-connected-apps-gemini.

# Disclosures and what could not be opened

- **Rename.** The product named in the assignment no longer exists under that name. The rating is of Tasks in Gemini. The October 2026 pages do not say "Spark"; the September 2026 roundup still does.
- **Spark overview page.** https://gemini.google/overview/agent/spark/ now redirects to https://gemini.google/about/, which has no Spark or tasks section. Not readable.
- **"What's new for Gemini Spark"** (support.google.com/gemini/answer/17171264) now redirects to the general Gemini release notes. The Spark-specific changelog is not readable. The release notes list nothing about tasks after 2026.06.30, although the help pages describe later changes (Pro plan access, remote control of the Mac app, the rename), so the release notes are not a complete changelog for this product.
- **The product itself.** I did not sign in to gemini.google.com. Every value rests on help and blog text, not on use.
- **Not opened.** The Connected Apps Platform developer documentation; Gemini Developer Mode; the help pages on Gems-to-skills migration and on importing memory from other AI platforms; Workspace (business) documentation for the preview announced in May ("Gemini Spark in Google Workspace will be available soon in preview for business customers"). The current help says tasks are not available "with a work or school Google Account".
- **Old statements used.** Three rows quote May 2026 launch posts (the Antigravity harness, sub-agents, email and chat). I used them only to show what was announced; the values rest on the current help pages.
- **Search.** Two web searches located the vendor pages. Their result lists showed titles from news sites (Decrypt, Tom's Guide, The Next Web, Engadget, DataCamp and others). I opened none of them and no cell rests on them.
- **Other files.** Under `` I opened only `prior-work/vendors/protocol-v2.md` and `prior-work/rerate-criteria-v2.md`.
- **Method.** Pages were fetched with curl and converted to text with lynx; quotes were copied from that text. Ellipses mark omitted words; a slash inside a quote marks a list item break.
