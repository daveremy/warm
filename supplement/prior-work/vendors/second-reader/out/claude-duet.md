Newest changelog seen: **2026-11-12**; newest Duet-specific entry: **2026-10-21**, research preview. [Release notes](https://support.claude.com/en/articles/12138966-release-notes).

| Service | Value | Quote | URL | Availability and reason |
|---|---|---|---|---|
| Sessions | **part — DISPUTABLE: yes** | “keeps your conversation history and its memory” | [Safety, “You have visibility into tasks and connected apps”](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security) | Research preview. Persistent history and continuity across tasks; explicit state handoff is undocumented. **Yes** is defensible if retained context satisfies handoff. |
| Tasks | **part** | “highlights tasks that need your input.” | [Get started, “Keep track of tasks”](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet) | Research preview. Task pages, progress, decisions, and user-marked completion are documented. Searches for retry, recovery, and cancellation found no coordinating mechanism. |
| Scheduling | **part** | “Claude Duet checks your connected accounts every few hours” | [Introduction, “How Claude Duet works”](https://claude.com/resources/articles/claude-duet) | Research preview. Morning briefs and periodic checks initiate work. No documented concurrency limits or general event-trigger configuration found. |
| Retrieval | **yes** | “Search, read, and upload files instantly” | [Google Drive connector](https://claude.com/marketplace/connectors/google-drive); [Duet connector support](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet) | Research preview; requires connecting the source. Duet explicitly supports Google Drive and retrieves material through its connector. |
| Artifacts | **part** | “Finished work appears in the Make tab.” | [Get started, “How Claude Duet works”](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet) | Research preview. Stores finished files for review and editing. No Duet-specific version history found; general Claude artifact documentation does not establish Duet coverage. |
| Models | **no — DISPUTABLE: part** | “Claude Duet runs on Claude Opus 5.5” | [Get started, “Limitations”](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet) | Research preview uses one fixed model. Searched model choice and routing; no selection across models found. **Part** is defensible for mediation and automatic effort selection alone. |
| Observability | **yes** | “what Claude Duet has done and is doing in its task list” | [Safety, “You have visibility into tasks and connected apps”](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security) | Research preview. Task history and individual task pages supply evidence of actions and progress. |
| Releases | **no** | “even ship code” | [Introduction, “How testers are using Claude Duet”](https://claude.com/resources/articles/claude-duet); [Release notes](https://support.claude.com/en/articles/12138966-release-notes) | Searched Duet documentation, release notes, and plugin documentation for versioning, deployment, and rollback. A shipping anecdote and vendor changelog do not describe a supplied release mechanism with a way back. |

All Duet features above are assessed for the US research preview on Pro, Max, and Ultra, with invitation-based access. [Current availability](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet).

- **C1: no — DISPUTABLE: part.** “Plugins customize how Claude works for your role, team, and company.” [Use plugins, introduction](https://support.claude.com/en/articles/13837440-use-plugins-in-claude). Searched Duet’s channels, tasks, and supported plugins for defined organizational or work-area units. Plugins package capabilities; no area with agent or role membership is defined. **Part** is defensible if function-specific plugins count as mentioned work-area units.
- **C2: no — DISPUTABLE: part.** “43 ready-to-run workflows for running and growing the business” [Small Business plugin, description](https://claude.com/marketplace/plugins/small-business). Searched for unit-level responsibilities and independently defined positions. Found workflow scope, but no qualifying C1 unit or positions. **Part** follows if the plugin is accepted as the area.
- **C3: part.** “Made by” — “Google” [Google Drive connector, provider field](https://claude.com/marketplace/connectors/google-drive). The maintained catalog records a provider per connector asset. It does not assign unique accountability per responsibility.
- **C4: no — DISPUTABLE: part.** “Claude picks the skill that fits.” [Small Business tutorial, “To run a skill”](https://academy.claude.com/tutorials/how-to-install-the-claude-for-small-business-plugin). Searched for agent discovery, capability-to-handler lookup, and routing. Found skill selection, not lookup of an agent or role and its address. **Part** is defensible if this selection counts as routing inside one orchestrator.

Pages opened, all on **2026-11-12**:

1. [Get started with Claude Duet](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)
2. [Introducing Claude Duet](https://claude.com/resources/articles/claude-duet)
3. [Claude Duet Safety, Privacy, and Security](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)
4. [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
5. [Claude Duet product page](https://claude.com/product/claude-duet)
6. [What are artifacts and how do I use them?](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)
7. [Marketplace plugins](https://claude.com/marketplace/plugins)
8. [Marketplace connectors and plugins](https://claude.com/marketplace/connectors-plugins)
9. [Google Drive connector](https://claude.com/marketplace/connectors/google-drive)
10. [Code Review plugin](https://claude.com/marketplace/plugins/code-review)
11. [Small Business plugin](https://claude.com/marketplace/plugins/small-business), reached through the redirected [older URL](https://claude.com/plugins/small-business)
12. [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
13. [How to install and use the Claude for Small Business plugin](https://academy.claude.com/tutorials/how-to-install-the-claude-for-small-business-plugin)

Could not open: **none of the attempted pages**. Only `protocol-v2.md` and `rerate-criteria-v2.md` were opened locally, both in full; no other local content was exposed.