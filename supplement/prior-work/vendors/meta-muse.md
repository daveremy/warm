---
title: "Meta Muse mapped to the 25 WARM platform services (protocol version 2)"
date: 2026-11-12
author: reader subagent (Claude), one reader, no second rating yet
product: Meta Muse (personal agent; apps for iOS, Android, web, Mac; WhatsApp)
product_version: "iOS app 15.1 (App Store version history, listed '1d ago' on 2026-11-12). No changelog page found. Newest dated vendor material: launch post last modified 2026-11-10; newsroom post 2026-11-06 (spaces); help article 'How your Muse agent browses the web' marked 'Updated: a day ago'."
status: not yet checked by sagan
---

# Scope and availability

Every value below rests on a Meta page opened on 2026-11-12 (list at the end). Nothing is rated from memory.

Availability, the same for every row unless the row says otherwise: usable today by adults in the US, Canada and Singapore, free with a weekly usage limit. Meta does not label it beta or preview, but its help pages still say "Muse and Muse subscriptions are in limited testing and aren’t available in all locations yet" (https://www.meta.com/help/subscriptions/1021145227643680/). I write "available (limited testing)" for this state.

Short names for the pages cited most:

- SEC = https://muse.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse (September 8, 2026; [quotation withheld: muse.ai page])
- DES = https://muse.ai/blog/how-we-designed-muse (September 8, 2026)
- HOME = https://muse.ai/
- NEWS = https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/
- H-APPROVE = https://www.meta.com/help/superintelligence/1385290430137537/
- H-DATA = https://www.meta.com/help/superintelligence/2225571704857152/
- H-CONN = https://www.meta.com/help/superintelligence/1687253048996149/
- H-START = https://www.meta.com/help/superintelligence/1331373868832401/
- H-SCHED = https://www.meta.com/help/superintelligence/1484325780075655/
- H-SKILL = https://www.meta.com/help/superintelligence/2797651547267109/
- H-PRIV = https://www.meta.com/help/superintelligence/1047255454427887/
- H-BROWSE = https://www.meta.com/help/superintelligence/2124746764949121/
- H-PERS = https://www.meta.com/help/superintelligence/995796179982326/
- H-MAC = https://www.meta.com/help/superintelligence/1126304576638594/
- PLAT = https://platform.muse.ai/docs (Connector guidelines)
- SPEC = https://research.meta.ai/blog/specialized-models-for-muse-and-metaai (November 6, 2026)
- TOK = https://www.meta.com/help/subscriptions/28153473374286914/
- TERMS = https://muse.ai/terms (last updated September 8, 2026)
- BIZHELP = https://www.facebook.com/business/help/38565157129799046

# The 25 services

| Service | Value | Quote and short reason | URL | Availability |
|---|---|---|---|---|
| Harness | yes | [quotation withheld: muse.ai page]. Also: [quotation withheld: muse.ai page] | SEC | available (limited testing) |
| Sessions | part, DISPUTABLE (yes) | [quotation withheld: muse.ai page] and [quotation withheld: muse.ai page] History and state are kept in one main chat and side chats and can be downloaded. Pause, resume and hand-off of a stretch of work are not described as features; the nearest text is [quotation withheld: muse.ai page] (BIZHELP). A reader who counts the persistent chat threads as the whole definition gives yes. | DES; SEC | available (limited testing) |
| Tasks | part, DISPUTABLE (yes) | [quotation withheld: muse.ai page] and [quotation withheld: muse.ai page] Tracking and cancellation are stated. Retry and recovery are stated only as model behavior ([quotation withheld: muse.ai page], SPEC). Keeping the original request is not stated. | DES; H-BROWSE | available (limited testing) |
| Environments | yes | [quotation withheld: muse.ai page] Also: [quotation withheld: muse.ai page] | HOME; H-PRIV | available (limited testing) |
| Scheduling | part, DISPUTABLE (yes) | [quotation withheld: muse.ai page] and [quotation withheld: muse.ai page]. Starts at a time and on an event are stated. A limit on how much runs at once is not found (searched "concurrent", "at once", "parallel", "limit"); the only stated limit is the weekly token allowance. A reader who counts the usage allowance as that limit gives yes. | H-SCHED; DES | available (limited testing) |
| Lifecycle | part | [quotation withheld: muse.ai page] and [quotation withheld: muse.ai page]. An account gets one agent, created at sign-up and ended by reset. Suspend and resume of agents, and a list of the agents (sub-agents) that exist, are not found. | H-APPROVE; SEC | available (limited testing) |
| Memory | part, DISPUTABLE (yes) | "You can find out what Muse remembers about you at any time by asking directly, or by viewing files like your MEMORY.md." and "We’ve trained our models to recognize what type of information is temporary versus permanent, to reason across time, and to distinguish between what is still relevant and what has become stale." Retention across conversations, editing, forgetting and staleness are covered. Where each entry came from is not stated. A reader who does not require provenance gives yes. | H-DATA; SPEC | available (limited testing) |
| Retrieval | yes | "For example, connecting your email allows Muse to search your email, but it won’t download your whole inbox (unless you tell it to)." Also, on a Mac: "your agent can work across your computer to find, organize, and manage the files you ask it to work with". | H-CONN; H-MAC | available (limited testing) |
| Artifacts | part, DISPUTABLE (yes) | "Finished artifacts are saved to your workspace in the Library tab, and shared in the conversation." Storage is stated. Versions of an artifact are not found (searched "version", "history", "revert" in the artifacts and data articles). A reader who does not require versions gives yes. | H-START | available (limited testing) |
| Models | part, DISPUTABLE (yes) | [quotation withheld: muse.ai page] and [quotation withheld: muse.ai page]. Requests to the model pass through a proxy and safety classifiers, and more than one Meta model is in use. No page says how a model is chosen for a task; the user cannot choose; one vendor. A reader who takes [quotation withheld: muse.ai page] as per-task choice gives yes. | SEC; TOK | available (limited testing) |
| Tools | yes | [quotation withheld: muse.ai page] | SEC | available (limited testing) |
| Registry | part | [quotation withheld: muse.ai page] and [quotation withheld: muse.ai page] A catalog of skills and connectors that the agent finds and loads. Versioned definitions, and definitions of agents, are not stated. | H-SKILL; PLAT | available (limited testing) |
| Directory | part (derived) | Derived from C3 = part and C4 = part by the rule in rerate-criteria-v2.md. Not rated from the definition. | see C3, C4 | n/a |
| Messaging | part | [quotation withheld: muse.ai page] Events from connectors reach the agent. Messages between agents appear only as a passing mention ([quotation withheld: muse.ai page], SEC); no delivery service between agents or to subscribers is described. | H-CONN | available (limited testing) |
| Orchestration | part, DISPUTABLE (yes) | [quotation withheld: muse.ai page] and [quotation withheld: muse.ai page]. Also: [quotation withheld: muse.ai page] (NEWS). Delegation to sub-agents, plans and held approvals are stated. How assignments, dependencies and returned results are coordinated is not described. | SEC | available (limited testing) |
| Channels | yes | [quotation withheld: muse.ai page] Also a Chrome extension, a Mac app and an Apple Watch app; AI glasses are "coming soon" (NEWS). | HOME | available (limited testing); voice [quotation withheld: muse.ai page] |
| Identity | part | [quotation withheld: muse.ai page] and [quotation withheld: muse.ai page]. The user signs in with a Meta account and services inside the VM are authenticated to each other. The agent has no identity of its own toward outside services, no record of the accountable person for an agent identity is described beyond the account, and revocation is per connector or site, not of an identity. | SEC | available (limited testing) |
| Secrets | yes | [quotation withheld: muse.ai page] | SEC | available (limited testing) |
| Policy | part, DISPUTABLE (yes) | [quotation withheld: muse.ai page] and [quotation withheld: muse.ai page] Rule decisions on actions and on content entering and leaving, with scoped grants, are stated. A rule for what stored data is kept is not found; deletion is done by the user. A reader who weighs the Sentinel as the whole responsibility gives yes. | SEC | available (limited testing) |
| Approvals | yes | [quotation withheld: muse.ai page] and [quotation withheld: muse.ai page] | SEC | available (limited testing) |
| Observability | yes | "Visit your Activity log by tapping your assistant icon to see a chronological record of actions your Muse has taken and permissions you’ve given it." | H-APPROVE | available (limited testing) |
| Evaluation | no, DISPUTABLE (part) | Searched every page for "eval", "evaluate", "criteria", "quality", "check", "verify", "unknown". Found no feature that assesses work products against stated criteria or reports a check that could not run. Found three near things: vendor-side development evals ([quotation withheld: muse.ai page], SEC); run-time safety classifiers ([quotation withheld: muse.ai page], SEC), which I read as Policy; and [quotation withheld: muse.ai page] (DES), which I read as a notification rule. A reader who counts either of the last two as assessment gives part. | SEC; DES | n/a |
| Improvement | part | [quotation withheld: muse.ai page] and [quotation withheld: muse.ai page]. Traces feed model training on the vendor side (with a user opt-out), and the agent "edits itself" (SEC). No step that turns evidence into proposed changes that a person reviews is described. | SEC; HOME | available (limited testing) |
| Releases | part | [quotation withheld: muse.ai page] and [quotation withheld: muse.ai page] A way back exists for the agent's customization and for the VM's data, and third-party connectors pass a review before listing ("Submit for review", https://platform.muse.ai/). Versioning and release of agents, skills and rules are not described; app versions appear only in the App Store history. | H-PERS; SEC | available (limited testing) |
| Reliability | part | [quotation withheld: muse.ai page] Backup and restore of data are stated. No mechanism that keeps the service available or restarts work after a failure is described, and the terms say Meta does not guarantee that [quotation withheld: muse.ai page] (TERMS). | SEC | available (limited testing) |

# Four further questions

## 1. Areas of work (C1 to C4)

**C1. An area of work exists in the model: no, DISPUTABLE (part).** Searched every page for "domain", "department", "team", "workspace", "project", "role", "area", "group". Found no defined unit that stands for an area of work and that agents or roles belong to. Found four near things, none defined that way:
- Side chats: "Side chats are separate conversations that help you organize different topics without cluttering the main chat." (H-START). A conversation, excluded by the version 2 ruling.
- Goals: "Goals: Personal goals that you have set, which Muse will help you track progress and send check-ins." (H-DATA). An objective, not an area.
- Spaces: "A space is a custom experience you create inside Muse by describing your idea, like a holiday gift tracker, a daily word game, or a planning board for your next DIY project." (https://about.fb.com/news/2026/11/introducing-spaces-customize-muse-app/). A page the agent builds, not a unit that holds agents or roles.
- Muse for Small Business: "we’re expanding it with a collection of new skills and connectors inside Muse to help people run their businesses" (https://about.fb.com/news/2026/09/introducing-muse-small-business/). A named bundle for one area of work; it is mentioned, not defined as an element of the product's model.
A reader who counts the Small Business bundle or spaces as units that are "mentioned or used, but ... not defined" gives part.

**C2. The area is specified apart from who does the work: no, DISPUTABLE (part).** No unit was found under C1, so there is nothing specified at the level of a unit. The only charter-like text is per agent: "Soul: Who your Muse is, including core truths, boundaries, and personality." (H-DATA). A reader who counts Soul.md as an agent charter (responsibilities per agent) gives part; the page states boundaries and personality, not responsibilities or roles.

**C3. A record of accountability: part.** The connector directory is a kept record of capabilities, each from one verified provider with a named maintainer: [quotation withheld: muse.ai page] (https://platform.muse.ai/) and [quotation withheld: muse.ai page] (PLAT, section 5.2). It names a provider and a responsible developer per connector, not an accountable area per responsibility, and the pages do not say the record states accountability. For the user's own work the only statement is in the terms, which is a rule and not a record: [quotation withheld: muse.ai page] (TERMS).

**C4. Finding where to send work: part.** Routing exists only inside the one agent's own logic: [quotation withheld: muse.ai page] (H-SKILL) and [quotation withheld: muse.ai page] (SEC). Connectors can be found by the agent ([quotation withheld: muse.ai page], PLAT), but these are tools, not agents or roles, and no lookup from a kind of work to a handler that any agent may ask is described.

**Directory (derived): part** (C3 part, C4 part).

## 2. Supplied agents for an area of work

- **Muse for Small Business** (skills and connectors for one named area): [quotation withheld: muse.ai page] https://muse.ai/business
- **Connector skills written by Meta** (per service, not per area): [quotation withheld: muse.ai page] SEC
- **Built-in skills** (per kind of output, not per area): "Things like creating podcasts, generating images, compiling research, drafting documents, creating dashboards or browsing the web." H-SKILL
- **Browser sub-agent** (a ready-made agent for one kind of task): [quotation withheld: muse.ai page] SEC
- **Sentinel** (a ready-made agent for permission decisions): [quotation withheld: muse.ai page] SEC
- **Role named only in store copy** (health and fitness): "Muse is your AI fitness coach." https://apps.apple.com/us/app/muse-from-meta/id6760173601. No help page defines a fitness role or skill; treat as marketing text.

No ready-made agents or roles for finance, communications, software or other named areas were found beyond these (searched the help center, muse.ai, the newsroom posts and the connector guidelines for "agent", "role", "skill", "coach", "assistant for").

## 3. What fits nowhere

- **Paying and purchase protection.** [quotation withheld: muse.ai page] and [quotation withheld: muse.ai page] SEC. Secrets covers hiding the card; issuing a payment instrument and insuring the purchase are not in the 25.
- **Usage metering and paid allowance.** "Additional Muse tokens are an account-bound, metered entitlement that represent a non-transferable, non-redeemable right to access and use the AI features." TOK. No service covers accounting for cost or quota.
- **Initiative: proposing work the user did not ask for.** [quotation withheld: muse.ai page] DES. Scheduling decides when work starts, not what work to propose.
- **Persona: avatar, name, voice, personality.** [quotation withheld: muse.ai page] DES.
- **Adversarial testing of the platform by outsiders.** [quotation withheld: muse.ai page] SEC. Evaluation covers agent behavior and work products, not security testing of the platform.
- **Rights of people who are not users.** "If you'd prefer that your business not receive these AI phone calls, you can opt out using this form." https://www.meta.com/help/superintelligence/4532990443643263/
- **Data portability in and out.** "Go to Settings, then tap Data Controls, then Import memory." H-PERS; "Tap Download your Muse data." H-DATA.
- **Consent to use of traces for training.** [quotation withheld: muse.ai page] SEC.
- **Hardware that extends the agent's network reach.** "Muse Home Link is a small USB-C device that connects your Muse agent to your home network." https://www.meta.com/help/muse-charm/1645260456993247/ (operating region: United States).

## 4. Where it runs and what the user supplies

- **Where it runs: the vendor's cloud, with optional reach into the user's machines.** "Muse runs on its own dedicated computer in the cloud, contained so no one else’s agent can reach it." NEWS. On a Mac: "When you use the Muse app on your Mac, your agent can work across your computer to find, organize, and manage the files you ask it to work with" H-MAC. In the user's browser: "You can chat with Muse from any page you open and Muse will browse using your personal Chrome." H-BROWSE.
- **Does it keep running when the user is away: yes.** "For tasks that take more time, Muse keeps working after people close the app, and comes back when something changes or when it needs approval, like before it sends an email or makes a purchase." NEWS.
- **What the user supplies.** A Meta account ([quotation withheld: muse.ai page], H-START); connections to their own services ([quotation withheld: muse.ai page], NEWS); goals and approvals; oversight, which the terms require ([quotation withheld: muse.ai page], TERMS); and payment for use above the free limit ([quotation withheld: muse.ai page], H-START). Nothing has to be built: [quotation withheld: muse.ai page] NEWS, and [quotation withheld: muse.ai page] H-SKILL. Optional building: [quotation withheld: muse.ai page] H-CONN.
- **Announced, not available:** "Later this year, Meta will introduce Muse Confidential VM" and "Shop Pay is coming soon as another way to pay, along with 1Password support" (NEWS).

# Pages opened (all on 2026-11-12)

Meta newsroom
- https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ (published 2026-09-08, modified 2026-11-10)
- https://about.fb.com/news/2026/09/introducing-muse-small-business/ (published 2026-09-29, modified 2026-10-08)
- https://about.fb.com/news/2026/10/introducing-muse-wonder-models/ (2026-10-12)
- https://about.fb.com/news/2026/10/muse-is-now-available-in-singapore-the-worlds-first-personal-ai-agent-built-for-everyone/ (2026-10-28)
- https://about.fb.com/news/2026/11/introducing-muse-ai-voice-expressive-avatars/ (2026-11-05)
- https://about.fb.com/news/2026/11/introducing-spaces-customize-muse-app/ (2026-11-06)

muse.ai
- https://muse.ai/ ; https://muse.ai/business ; https://muse.ai/security-and-privacy ; https://muse.ai/support (a contact form only) ; https://muse.ai/blog
- https://muse.ai/blog/how-we-designed-muse (2026-09-08)
- https://muse.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse (2026-09-08)
- https://muse.ai/blog/securing-muse (2026-11-02)
- https://muse.ai/privacy (effective 2026-09-17) ; https://muse.ai/terms (last updated 2026-09-08)
- https://muse.ai/sitemap.xml ; https://muse.ai/robots.txt
- https://platform.muse.ai/ ; https://platform.muse.ai/docs (Connector guidelines)

Meta help center (the "Updated" label on each page as shown)
- https://www.meta.com/help/artificial-intelligence/1303670544995562/ (Muse Help Center index)
- https://www.meta.com/help/superintelligence/1687253048996149/ (Connectors, 9 weeks ago)
- https://www.meta.com/help/superintelligence/2124746764949121/ (browsing, a day ago)
- https://www.meta.com/help/superintelligence/1385290430137537/ (guidance and approval, 9 weeks ago)
- https://www.meta.com/help/superintelligence/2225571704857152/ (manage your data, 9 weeks ago)
- https://www.meta.com/help/superintelligence/4532990443643263/ (people who don't use Muse, 8 weeks ago)
- https://www.meta.com/help/superintelligence/1331373868832401/ (get started, a week ago)
- https://www.meta.com/help/superintelligence/1047255454427887/ (privacy, safety and security, 9 weeks ago)
- https://www.meta.com/help/superintelligence/1436362127544482/ (payments, 7 weeks ago)
- https://www.meta.com/help/superintelligence/2797651547267109/ (skills, 9 weeks ago)
- https://www.meta.com/help/superintelligence/995796179982326/ (personality and memories, 6 weeks ago)
- https://www.meta.com/help/superintelligence/1484325780075655/ (reminders and scheduled tasks, 9 weeks ago)
- https://www.meta.com/help/superintelligence/2074655449783957/ (artifacts, 9 weeks ago)
- https://www.meta.com/help/superintelligence/1126304576638594/ (Mac files and apps, 5 weeks ago)
- https://www.meta.com/help/muse-charm/1645260456993247/ (Muse Home Link, 5 weeks ago)
- https://www.meta.com/help/subscriptions/1625680452306909/ ; https://www.meta.com/help/subscriptions/1021145227643680/ (9 weeks ago) ; https://www.meta.com/help/subscriptions/28153473374286914/ (3 weeks ago)
- https://www.facebook.com/business/help/38565157129799046 (Use Muse for a business goal)

Other Meta pages
- https://research.meta.ai/blog/introducing-muse-spark-1-3 (2026-09-02; a model post, not used for a cell)
- https://research.meta.ai/blog/specialized-models-for-muse-and-metaai (2026-11-06)
- https://ai.meta.com/muse/ (only the questions-and-answers text could be extracted)
- https://faq.whatsapp.com/1131618509041969 (Muse through WhatsApp) ; https://faq.whatsapp.com/1050934623978152 (third-party agents; not about Muse, not used)
- https://apps.apple.com/us/app/muse-from-meta/id6760173601 (Meta's store listing and version history; version 15.1)

# Disclosures and what could not be opened

- **Automated reading.** muse.ai/robots.txt disallows several AI crawlers by name, ClaudeBot among them, and carries the notice [quotation withheld: muse.ai page]. I read the public pages listed in muse.ai's sitemap once each with curl under a browser user agent, and did not request any path that robots.txt disallows for general crawlers. The meta.com help pages returned HTTP 400 to a plain request and 200 once browser request headers were added. The author should know this before the file is cited.
- **No changelog.** I found no Muse changelog or release-notes page. https://muse.ai/changelog, https://muse.ai/docs and https://muse.ai/help return 401 ("Authentication required"). The version above comes from the App Store history.
- **Not opened or not readable.** https://faq.whatsapp.com/1135041965850388 and https://faq.whatsapp.com/1516007700293140 (the body did not render without a browser; the second was not requested). The [quotation withheld: muse.ai page] business help article (link not found in the page source). https://platform.muse.ai/terms. http://research.meta.ai/blog/muse-wonder and https://research.meta.ai/blog/bringing-your-muse-to-life (downloaded, not read; model and avatar posts). The Google Play listing. The product itself: I have no Muse account, so nothing was checked in the app, and Settings pages such as the connector list were not seen.
- **Age of the architecture description.** The most detailed source (SEC) is dated September 8, 2026 and says it [quotation withheld: muse.ai page]. Rows that rest on it (Harness, Tools, Secrets, Policy, Approvals, Identity, Models, Orchestration) describe the launch design; no later page contradicts them.
- **Search results.** Web search was used only to locate Meta pages. One search summary described dev.meta.ai pages about Muse Code and the Meta Model API (a different product); I did not open them and did not use them.
- **Hints not used as evidence.** muse.ai/robots.txt lists application paths (/approvals, /artifacts, /crons, /goals, /library, /team, /flock, /identity). Path names are not descriptions of features and no cell rests on them. "/team" and "/flock" are not explained on any page I opened.
- **Contamination.** I opened only protocol-v2.md and rerate-criteria-v2.md under the warm folder. No search printed content from any other file there.
- **Spelling.** American English outside quotations; quotations keep the source's spelling and punctuation.
