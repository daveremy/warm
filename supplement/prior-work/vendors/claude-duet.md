---
title: "Claude Duet mapped to the 25 WARM platform services (protocol version 2)"
date: 2026-11-12
author: "vendor reader (Claude subagent, model claude-fable-5-2), one reader, no second rating yet"
product: "Claude Duet (Anthropic), research preview"
product_version: "iOS app 1.261111.19, released 2026-11-12 (App Store listing). Newest entry in Anthropic's release notes: 2026-11-12 (Claude Meetings, not Duet). Newest release-note entry about Duet: 2026-10-21 (launch). Safety article dated 2026-10-23. Help article 'Get started with Claude Duet' shows 'Updated this week'."
status: "not yet checked by sagan"
---

# How to read this file

All pages were opened on 2026-11-12 (13:25 to 13:35 MST). Every quote is copied from the page named in the same cell. Availability is the same for every row unless the cell says otherwise: **research preview**, by waitlist, for Pro, Max and Ultra plans in the US ("Claude Duet is available as a research preview to users on Pro, Max, and Ultra plans in the US, through a waitlist.").

Page keys used in the table:

- **GS** = https://support.claude.com/en/articles/17631495-get-started-with-claude-duet
- **INTRO** = https://claude.com/resources/articles/claude-duet
- **SAFE** = https://claude.com/resources/articles/claude-duet-safety-privacy-and-security
- **PROD** = https://claude.com/product/claude-duet
- **MEM** = https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
- **APP** = https://apps.apple.com/us/app/claude-duet-by-anthropic/id6803276000
- **BROWSER** = https://support.claude.com/en/articles/18234133-how-do-anthropic-hosted-browsers-identify-themselves-when-they-browse-the-web-on-a-user-s-behalf
- **LINK** = https://support.claude.com/en/articles/17666484-how-to-use-link-by-stripe-with-claude-duet
- **PLUGIN** = https://claude.com/marketplace/plugins/small-business
- **PLUGIN-README** = https://github.com/anthropics/knowledge-work-plugins/tree/e605d8ddbfb688da57dfaaceebd93f12a64ef1d3/small-business (README.md)

"Searched" in a **no** cell means a text search of the body of GS, INTRO, SAFE, PROD, LINK, the Shop Pay article, BROWSER and the App Store description for the listed terms, plus a search for "duet" in the full text of the claude.com documentation site (https://claude.com/docs/llms-full.txt, 4.4 MB, zero matches).

# The 25 services

| Service | Value | Quote and reason | URL | Availability |
|---|---|---|---|---|
| Harness | **yes** | "Describe a task in a short message, and it works out which apps to use and what steps to take in the background." Also: "larger tasks, like building a financial model or a deck, require more model turns and background work." The vendor runs the loop; the pages do not describe how the context is assembled. | INTRO | research preview |
| Sessions | **yes** | "Claude Duet keeps your conversation history and its memory so it can carry context between tasks, until you delete your history or reset it." (SAFE) and "Your main thread stays in one place, so Claude Duet picks up where you left off." (GS). Hand-off to another agent is not described. | SAFE, GS | research preview |
| Tasks | **part** DISPUTABLE (yes) | "The Tasks tab shows what Claude Duet is working on and highlights tasks that need your input." and "It may suggest that a task looks finished, but only you can mark a task as completed." (GS); "each task has its own page" (SAFE). Tracking from start to finish is stated. Retry, recovery, cancellation and keeping the original request are not (searched: retry, cancel, stop, recover, fail). Yes is defensible because a per-task record with a completion rule exists. | GS, SAFE | research preview |
| Environments | **yes** | "Your browser in Claude Duet runs in its own dedicated virtual machine in the cloud, separate from the model and from the cloud computers the agent works on." Also GS: "It works on its own computer in the cloud". | SAFE | research preview |
| Scheduling | **part** DISPUTABLE (yes) | "Claude Duet checks your connected accounts every few hours, because checking nonstop would use up your plan’s limits much faster." and "Each morning, it sends you a short brief" (INTRO); "It can read your inbox, draft replies, book things, and run routines while you are away." (SAFE). Starting work at a time is stated. Events are found by polling ("It checks your accounts at set intervals, so something urgent can arrive between checks.", GS), and no limit on how much runs at once is stated; the pages do not say how a user defines a routine. Yes is defensible because timed and recurring work runs today. | INTRO, SAFE, GS | research preview |
| Lifecycle | **no** | One agent per Claude account. Searched: agents, subagent, create, pause, suspend, list. Found only account-level deletion ("Deleting your account wipes everything Claude Duet has stored.", SAFE). No way to create, suspend or list agents. | (searched) | n/a |
| Memory | **part** DISPUTABLE (yes) | "Claude Duet, a research preview for Pro, Max, and Ultra plans, also uses and adds to your memory, so what Claude knows about you is there from your first message." and "Claude updates memory as you chat." (MEM). Retention across sessions and updating are stated; the memory article lists entries as topics the user can edit or delete, but does not say each entry records where it came from. Yes is defensible if editable, updated topics count as kept current and provenance is treated as secondary. | MEM | research preview (memory itself is generally available in Claude) |
| Retrieval | **yes** | "Claude Duet can search your past chats to pick up context from earlier work, so you don't have to repeat yourself." and "When it gives you a number or a summary, it tells you which email, file, or spreadsheet it came from." Connectors named on the same page include Gmail and Google Drive. | GS | research preview |
| Artifacts | **part** | "Bigger results come back as files you can review and edit, such as a research brief, a financial model, a slide deck, or a dashboard. Finished work appears in the Make tab." Storage of work products is stated; versions are not (searched: version, history, revert). | GS | research preview |
| Models | **no** DISPUTABLE (part) | "You can't choose a model. Claude Duet runs on Claude Opus 5.5 and decides how much effort a job needs." One model from one vendor; no choice among models was found. Part is defensible because the product chooses the effort for each job. | GS | n/a |
| Tools | **yes** | "Claude Duet can use the over 6,000 connectors and plugins in the Claude Marketplace" (INTRO); "The agent drives the browser only through a fixed set of commands: open this page, click here, type this." (SAFE). | INTRO, SAFE | research preview |
| Registry | **part** DISPUTABLE (yes) | "Claude Duet supports plugins, such as the small business plugin, and can suggest ones that fit your work." (GS); "Claude Duet runs on your Claude account, so the memory, skills, and connectors you've set up in Claude are there from your first message." (GS). Finding and loading tools and skills is stated. The Duet pages do not state versioning or definitions of agents. Yes is defensible because the plugin Duet names carries a version in its repository ("Current version: 1.35.1 — 2026-09-15", PLUGIN-README). | GS | research preview |
| Directory | **no** (derived) | Derived from C3 = no and C4 = no. Both of those cells are DISPUTABLE (part); if either is read as part, this row becomes part. | derived | n/a |
| Messaging | **no** | Searched: agents, subagent, event, subscribe, webhook, trigger. Found no delivery of messages between agents and no event subscription. Notifications to the person are rated under Channels. | (searched) | n/a |
| Orchestration | **no** DISPUTABLE (part) | Searched: assign, delegate, depends, team, role, steps. Found no coordination among several agents or people. Part is defensible because the product divides work between itself and the one user and returns results: "The Tasks tab shows what Claude Duet is working on and highlights tasks that need your input." (GS) and "If you can’t approve right away, Claude Duet finishes the rest of the task and brings the approval back to you later." (GS). | GS | n/a |
| Channels | **yes** | "It’s available as a standalone app on iOS and Android, and on claude.ai." and "you can message it through typing or voice in one ongoing thread" and "You’ll receive a notification when the task is complete or needs your review." Limit: the person must come to Duet's own app; "It doesn't make phone calls or send text messages to other people." (GS). | INTRO | research preview |
| Identity | **part** | "Today, requests that its web browser sends include a distinct User-Agent header, and we publish the public IP addresses it browses from, so sites can recognize it and decide how to treat it." (SAFE); "Open Claude Duet and sign in with your Claude account." (GS). The pages establish that a hosted Claude agent is acting and tie it to one Claude account. They describe no record of the accountable person for each agent identity and no revocation of an agent identity (only "you can disconnect any app at any time"). | SAFE, GS, BROWSER | research preview |
| Secrets | **yes** | "Credentials that the agent uses on your behalf, such as a sign-in token for a connected service, never enter the machine where the agent works. A placeholder for the credential sits there instead and a proxy outside that machine puts in the real value only as a request is made." | SAFE | research preview (1Password sign-in is "Soon") |
| Policy | **part** DISPUTABLE (yes) | "Some actions stay off-limits even with your approval, like trading securities, banking actions such as moving money between accounts, and accessing someone else's account." and "we built a new safety classifier that runs separately from the main model and checks whether each message Claude Duet is about to send contains potentially sensitive information". Rules on actions and on content that leaves are stated, and a purchase gets a scoped grant ("a one-time card from a wallet like Link from Stripe, limited to that merchant and amount"). The rules are fixed by the vendor, the per-action check is a classifier, and no rule on what stored data is kept is stated beyond deletion by the user. Yes is defensible because each part of the definition has some stated mechanism. | SAFE | research preview |
| Approvals | **yes** | Single held actions: "But before it sends a message, makes a payment, signs a document, or deletes anything, it shows you exactly what it’s about to do and waits for your approval." (INTRO). Approvals in advance for a class: "Some other steps aren’t covered by a "don't ask me again" rule, however often you have approved them, like paying or sending money, deleting an order, or creating an account." (SAFE). A separate record of approvals is not described. | INTRO, SAFE | research preview |
| Observability | **part** DISPUTABLE (yes) | "You can see what Claude Duet has done and is doing in its task list, where each task has its own page, and steer it mid-task." (SAFE). A record for each task is stated. No log, trace or audit record was found (searched: log, audit, trace, export), and "You can't watch Claude Duet work in its browser or take over the browser." (GS). Yes is defensible because the task pages are evidence of what the agent did. | SAFE, GS | research preview |
| Evaluation | **no** DISPUTABLE (part) | Searched: evaluat, test, check, criteria, unknown. Found only the vendor's own testing before launch ("Our Safeguards team built evaluations from routine-shaped tasks", SAFE), which is not a feature a user can use. Part is defensible because an automated check judges each action against a criterion: "It assesses whether the action matches your intent." (SAFE); this reader counted that check under Policy. | SAFE | n/a |
| Improvement | **no** DISPUTABLE (part) | Searched: improve, learn, feedback, suggest, tune. Found no feature that turns traces or evaluations into proposed changes. Part is defensible on two statements: "Claude Duet supports plugins, such as the small business plugin, and can suggest ones that fit your work." (GS) and "You can send feedback or report any issues directly from the chat by telling Claude Duet in plain words what happened, and it will pass your report to our team." (GS). | GS | n/a |
| Releases | **no** DISPUTABLE (part) | Searched: version, release, undo, revert, roll back, rollback. Found nothing that versions or rolls back the agent, its skills or its rules for the user. Part is defensible because the vendor ships numbered app versions (APP: version 1.261111.19, release note "Squashed some bugs and made Claude Duet better.") and the named plugin carries a version (PLUGIN-README); no way back is described. | APP | n/a |
| Reliability | **no** DISPUTABLE (part) | Searched: uptime, outage, restore, recover, fail, backup, status. Found no statement on availability targets or on restoring the service after a failure; https://status.claude.com lists no Claude Duet component (it lists claude.ai, where Duet's web version is opened). Part is defensible on "it runs continuously even after you close the app" (SAFE) and "While it’s always on" (PROD), which state that the vendor keeps the agent running. | SAFE, PROD | n/a |

Count: yes 8, part 8, no 9 (of which Directory is derived). DISPUTABLE cells: 12, plus the derived Directory row.

# Four further questions

## 1. Areas of work (C1 to C4 of rerate-criteria-v2.md)

**C1. An area of work exists in the model: no. DISPUTABLE (part).**
The only unit that stands for part of the user's work is the channel: "You can also start separate channels for different topics, and they share the same memory." (GS) and "Keep each part of your work in its own channel, like one for finance and one for hiring. Claude Duet can read across all of them, so it keeps the whole picture." (APP). A channel is a message thread, and the version 2 ruling says a unit that models a conversation is not an area of work, so the lower value is no. Part is defensible because the App Store text presents a channel as a named unit for a part of the work (finance, hiring) and a user can have several; the unit is used but not defined, and one agent serves all of them. The small business plugin that Duet names groups its skills by area ("44 skills spanning finance, sales, marketing, operations, and hiring", PLUGIN-README), but those are headings in an optional plugin's README, not an element of Duet.

**C2. The area is specified apart from who does the work: no.**
Rated on the channel. The pages state no responsibility for a channel as a whole and no roles. The only stated properties are a topic and shared memory ("they share the same memory", GS). Searched: role, responsib, owner, scope, team.

**C3. A record of accountability: no. DISPUTABLE (part).**
Searched: owner, accountab, responsib, registry, assign. No record names an accountable area or owner for a responsibility or capability. Part is defensible under the version 2 ruling that a record of commitments an agent takes on while the system runs counts as a record: "The Tasks tab shows what Claude Duet is working on and highlights tasks that need your input." (GS). That record shows, per task, whether the agent or the person must act; it does not state accountability per responsibility.

**C4. Finding where to send work: no. DISPUTABLE (part).**
There is one agent, and no page describes a lookup from a kind of work to an agent or role. Searched: route, delegate, assign, directory, agents. Part is defensible because routing exists inside the one agent's own logic: "Describe what you need, and it works out which apps to use and how much effort the job takes." (GS), and the named plugin has "a router that understands plain English" that "picks the right skill" (PLUGIN-README). Those route to apps and skills, not to an agent or role with a way to reach it.

**Directory (derived): no.** C3 and C4 are both no. If either disputed cell is read as part, Directory is part.

## 2. Supplied agents for an area of work

- **Small Business plugin (skills, by Anthropic).** "Claude Duet supports plugins, such as the small business plugin, and can suggest ones that fit your work." (GS). The plugin page: "Claude for Small Business gives owners 43 ready-to-run workflows for running and growing the business, inside the tools you already use." (PLUGIN). Its repository README: "44 skills spanning finance, sales, marketing, operations, and hiring, plus a router that understands plain English." and lists them by area: Finance (12), Sales & leads (8), Marketing (8), Customers & proposals (4), Operations & hiring (5), Briefings (2), Setup & building (5) (PLUGIN-README). The two pages give different counts (43 and 44). The plugin page's install button reads "Install in Cowork"; only GS says Duet supports it.
- **Marketplace plugins in general.** "Claude Duet can use the over 6,000 connectors and plugins in the Claude Marketplace" (INTRO). The pages do not say which other plugins for a named area work in Duet.
- **Built-in behavior for one area (not a separate agent).** "Each morning, it looks across your email and calendar, picks what most needs your attention, and can start the first steps, like drafting replies for you to review." (GS). The vendor states the intended users: "We built Claude Duet for professionals and small business owners" and "We built its core functionality around work, so personal errands, such as booking tickets, aren’t quite as strong" (INTRO).
- **Ready-made agents or roles: none found.** Searched the pages above for agents, roles, persona, assistant for; the plugin's contents are skills (its folder holds `skills/`, `shared/`, `.mcp.json`, no agents folder).

## 3. What fits nowhere

- **Metering work against a usage budget.** "Claude Duet uses your plan's usage limits, including any five-hour session limit and your weekly limits, at the same rate as chats in Claude. Work it does in the background, like the morning brief and check-ins, also counts, so you may reach your limits sooner than with chat alone." (GS). Scheduling covers how much may run at once, not what the work costs against an allowance.
- **Deciding what deserves the person's attention.** "built it to be resourceful and to decide what needs you, what can wait, and when to check with you first" (INTRO); "messages you only when something needs your attention" (INTRO); "You can also tell it what you want to hear about and how often." (INTRO). This is a judgment about interrupting a person, separate from carrying the message (Channels) or starting the work (Scheduling).
- **Letting third parties recognize and refuse the agent.** "we publish the public IP addresses it browses from, so sites can recognize it and decide how to treat it. Before launch, we also contacted several large websites and gave them the option to prevent Claude Duet from visiting their sites, and some chose to." (SAFE). Identity covers the first half; no service covers consent by an outside party that the agent acts on. Borderline.
- **Paying on the user's behalf and routing a purchase dispute.** "For purchases, Claude Duet pays with a one-time card from a wallet like Link from Stripe, limited to that merchant and amount." (SAFE); "Where to get help with a purchase depends on the problem" (GS). The card is a grant (Policy) and the wallet is a tool (Tools); what is left over is responsibility for a financial transaction after it is made. Borderline.
- **Saying where a figure in the output came from.** "When it gives you a number or a summary, it tells you which email, file, or spreadsheet it came from." (GS). Close to Retrieval and Observability; listed because neither definition mentions the source of a statement in a work product. Borderline.

## 4. Where it runs and what the user supplies

- **Where the agent runs: the vendor's cloud.** "It works on its own computer in the cloud, so it can keep working after you close the app." (GS). "Claude Duet has a virtual machine with its own browser, so it doesn’t require your laptop or phone to be on." (INTRO). The user's devices hold only the app: "Claude Duet is a standalone app for iOS and Android. On a computer, you can open it on the web at claude.ai." (PROD). It cannot reach the user's machine: "It can't see all of your projects or the files on your computer" (GS).
- **Does it keep running when the user is away: yes.** "It can use all the apps and services you've chosen to connect to Claude, and it runs continuously even after you close the app. It can read your inbox, draft replies, book things, and run routines while you are away." (SAFE). It checks at intervals, not constantly: "Claude Duet checks your connected accounts every few hours" (INTRO). Held actions wait for the user: "If you can’t approve right away, Claude Duet finishes the rest of the task and brings the approval back to you later." (GS).
- **What the user must supply.** A paid plan, a US account and an invitation: "A Pro, Max, or Ultra plan / A Claude account in the US / An invitation from the waitlist or from a Claude Duet user" (GS, three list items). Connections to the user's apps: "You start every connection yourself, and you can disconnect any app at any time." (GS). Approvals for consequential actions (INTRO, quoted in the Approvals row). For purchases, a Link or Shop Pay account: "Sign in to your Link account and approve access." (LINK). Usage allowance from the plan (GS, quoted under question 3).
- **What the user must build: nothing is required.** "Message Claude Duet in the app like a teammate you trust, through text or voice with no prompts or setup." (PROD). "Claude Duet carries over your memory, skills, and connected apps from your Claude account, so setting it up requires minimal work." (INTRO). Optional: skills and plugins from the user's Claude account.

# Pages opened (all on 2026-11-12)

| Page | URL | Note |
|---|---|---|
| Get started with Claude Duet (help center) | https://support.claude.com/en/articles/17631495-get-started-with-claude-duet | "Updated this week" |
| Introducing Claude Duet (launch article) | https://claude.com/resources/articles/claude-duet | dated October 21, 2026 |
| Claude Duet Safety, Privacy, and Security | https://claude.com/resources/articles/claude-duet-safety-privacy-and-security | dated October 23, 2026; figures not read (images) |
| Claude Duet product page | https://claude.com/product/claude-duet | includes a scripted demo conversation; demo text was not used as evidence of a feature |
| How to use Link by Stripe with Claude Duet | https://support.claude.com/en/articles/17666484-how-to-use-link-by-stripe-with-claude-duet | |
| How to use Shop Pay with Claude Duet | https://support.claude.com/en/articles/17666489-how-to-use-shop-pay-with-claude-duet | |
| Release notes | https://support.claude.com/en/articles/12138966-release-notes | newest entry November 12, 2026; one Duet entry, October 21, 2026 |
| Use Claude's chat search and memory to build on previous context | https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context | two Duet sentences; the rest describes Claude's memory, which Duet "uses and adds to" |
| How do Anthropic-hosted browsers identify themselves | https://support.claude.com/en/articles/18234133-how-do-anthropic-hosted-browsers-identify-themselves-when-they-browse-the-web-on-a-user-s-behalf | "Updated over a week ago" |
| Use Personal Finance in Claude | https://support.claude.com/en/articles/18185620-use-personal-finance-in-claude | only the line "Personal Finance isn’t available in Claude Duet." |
| Features and capabilities (help collection) | https://support.claude.com/en/collections/18031719-features-and-capabilities | used to list Duet articles: three |
| Help center search for "claude duet" | https://support.claude.com/en/?q=claude+duet | used to find pages |
| Help center sitemap | https://support.claude.com/sitemap.xml | three Duet articles per language |
| App Store listing, Claude Duet by Anthropic | https://apps.apple.com/us/app/claude-duet-by-anthropic/id6803276000 | read through https://itunes.apple.com/search?term=claude+duet&entity=software&country=us ; version 1.261111.19, 2026-11-12 |
| Small Business plugin (marketplace) | https://claude.com/marketplace/plugins/small-business | |
| Small Business plugin source (README, plugin.json, folder list) | https://github.com/anthropics/knowledge-work-plugins/tree/e605d8ddbfb688da57dfaaceebd93f12a64ef1d3/small-business | version 1.35.1, 2026-09-15 |
| claude.com documentation index and full text | https://claude.com/docs/llms.txt , https://claude.com/docs/llms-full.txt | zero matches for "duet" |
| claude.com documentation pages | https://claude.com/docs/plugins/platform-support.md , /plugins/overview.md , /extend/overview.md , /skills/overview.md | zero matches for "duet" |
| claude.com sitemap | https://claude.com/sitemap.xml | three Duet URLs: product page and the two articles |
| Claude for small business (solutions page) | https://claude.com/solutions/small-business | Duet appears only in navigation |
| Anthropic news index and sitemap | https://www.anthropic.com/news , https://www.anthropic.com/sitemap.xml | no Duet article; one link to the product page |
| Privacy center sitemap and search | https://privacy.claude.com/sitemap.xml , https://privacy.claude.com/en/?q=duet | no Duet article; one crawler article mentions Duet (also on the help center), not opened |
| Status page components | https://status.claude.com/api/v2/components.json | no Duet component |

Web searches used only to find vendor pages (2026-11-12): "Claude Duet Anthropic personal agent research preview"; "Claude Duet" restricted to Anthropic domains (two queries). The first returned news coverage; no cell rests on it.

# Disclosures and what could not be opened

- **The product itself was not used.** Nothing in this file comes from the app, its settings screens or its in-app help. Features that exist only in the app and not on a public page are not counted.
- **Not opened:** the pages the Duet articles link to about other products (the trustworthy-agents framework, the Claude Managed Agents engineering post, the Claude Code auto mode post, the prompt-injection research post); the Link and Shop support sites; the Claude Academy tutorial for the small business plugin; the Google Play listing; the IP list at https://claude.com/.well-known/sail; the usage-limit and limit-reset help articles. A reader who opens the Managed Agents and auto mode posts may find detail that bears on Secrets, Policy and Environments, but those posts describe other products.
- **Returned 404:** https://claude.com/docs/claude-duet and https://claude.com/docs/duet (guessed addresses; the documentation site has no Duet section).
- **Figures** 1 to 4 of the safety article are images and were not read; only their captions were.
- **Reader's prior knowledge:** the reader's training data ends before this product was announced, so no value rests on memory.
- **Files under the warm folder:** only `prior-work/vendors/protocol-v2.md` and `prior-work/rerate-criteria-v2.md` were opened. No search printed content from any other file there.
- **Rule applied to two-sided cells:** the lower value is given and the cell is marked DISPUTABLE, as the protocol requires. In this reader's judgment the other value is the more natural reading for C1 (part), Tasks (yes), Scheduling (yes) and Policy (yes).
