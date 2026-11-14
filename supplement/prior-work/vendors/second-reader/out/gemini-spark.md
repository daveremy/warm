Newest changelog seen: **2026-10-13** — [Gemini release notes](https://gemini.google/release-notes/). Gemini Spark is now named Task in the [current documentation](https://support.google.com/gemini/answer/17094507?hl=en). Read date: **2026-11-12**.

| Service | Value | Quote | URL | Availability and reason |
|---|---|---|---|---|
| Lifecycle | **part** | “Your schedules and tasks are paused and not deleted.”; “creating custom sub-agents” | [Task controls](https://support.google.com/gemini/answer/17094507?hl=en); [Launch roadmap](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/) | Experimental, Pro/Ultra. Enable/disable controls exist; custom subagents were announced. Searched current task, skill, and release documentation; no agent inventory or complete agent lifecycle found. |
| Retrieval | **yes** | “Search for files, read file contents” | [Workspace actions](https://support.google.com/gemini/answer/17094507?hl=en) | Experimental, Pro/Ultra; requires connected Workspace. Retrieves named Drive files, email, and Keep notes. |
| Models | **yes** | “If you have a Google AI plan you can manually switch models in both Chat Mode and Task Mode.” | [Models](https://support.google.com/gemini/answer/18648722) | Available in experimental task mode. Pro supports Hydrogen and Argon; Ultra also supports Carbon. Multiple models satisfy the definition without multiple vendors. |
| Tools | **yes** | “After it’s connected, you can use the custom connected app” | [Custom apps](https://support.google.com/gemini/answer/17209137) | Available; custom apps require US, English, age 18+, and web/mobile. Gemini invokes connected MCP apps in tasks; users need not implement call mediation. |
| Secrets | **part — DISPUTABLE: yes** | “Google doesn’t share your passwords with Gemini in Chrome or other sites.” | [Password handling](https://support.google.com/chrome/answer/95606?co=GENIE.Platform%3DDesktop&hl=en); [Browser integration](https://support.google.com/chrome/answer/16821166) | Experimental Chrome integration. Password Manager supplies protected sign-in. **yes** is defensible for this integrated path; broader task and MCP secret isolation was not established. |
| Approvals | **yes** | “Allow or Allow once: Approves the action for this specific step only.”; “Always allow: Gemini runs this action without asking.” | [Permissions](https://support.google.com/gemini/answer/18766567?hl=en&ref_topic=17122162) | Available in experimental tasks. Supports individual decisions and saved preferences per app action; sensitive actions retain confirmation requirements. |
| Improvement | **no — DISPUTABLE: part** | “You can also ask Gemini to update a skill and its files.” | [Skill editing](https://support.google.com/gemini/answer/17094296) | Conversational editing is available. Searched skill creation, writing guidance, and releases for evidence-to-change proposals; none found. **part** is defensible if user-directed editing counts as the supporting mechanism. |
| Reliability | **no — DISPUTABLE: part** | “Gemini might use a remote browser to complete the task.” | [Browser fallback](https://support.google.com/chrome/answer/16821166); [Schedule troubleshooting](https://support.google.com/gemini/answer/17094710?hl=en) | Experimental fallback exists. Searched task, browser, schedule, and release documentation for service failover, restoration, and retries; no service recovery mechanism found. **part** is defensible for browser substitution when a device becomes unavailable. |

- **C1: no.** “a 24/7 personal AI agent” — [Launch description, Spark section](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/). Searched task, skill, and launch definitions for organizational or work-area units. Found an individual agent, tasks, and reusable instructions; no qualifying area.
- **C2: no.** “instructions that teach Gemini how to handle a type of task.” — [Skill-writing guidance, Optimize your instructions](https://support.google.com/gemini/answer/17102773?hl=en&ref_topic=17122162). Searched for area-level responsibilities and independently defined positions; neither was found.
- **C3: part.** “As the owner of a skill, you can transfer ownership” — [Skills, Transfer ownership of a shared skill](https://support.google.com/gemini/answer/17094296). Shared-skill records maintain ownership and access. This is ownership per asset, without stated accountability per responsibility.
- **C4: no.** “Gemini only checks the skill’s name and description” — [Skill-writing guidance, How skills work](https://support.google.com/gemini/answer/17102773?hl=en&ref_topic=17122162). Searched skill selection, connected apps, and subagent documentation for runtime agent discovery or capability-to-handler lookup. Skill loading does not identify an agent or role and how to reach it.

Pages opened successfully, all on **2026-11-12**:

1. [Manage your tasks & workflows](https://support.google.com/gemini/answer/17094507?hl=en)
2. [Gemini Spark launch announcement](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/)
3. [Gemini release notes](https://gemini.google/release-notes/)
4. [Connect & manage custom apps](https://support.google.com/gemini/answer/17209137)
5. [Create & manage skills](https://support.google.com/gemini/answer/17094296)
6. [About Gemini models](https://support.google.com/gemini/answer/18648722)
7. [Manage browser & app permissions](https://support.google.com/gemini/answer/18766567?hl=en&ref_topic=17122162)
8. [Write effective skills](https://support.google.com/gemini/answer/17102773?hl=en&ref_topic=17122162)
9. [Find & manage tasks](https://support.google.com/gemini/answer/17094196)
10. [Manage passwords in Chrome](https://support.google.com/chrome/answer/95606?co=GENIE.Platform%3DDesktop&hl=en)
11. [Chrome auto browse](https://support.google.com/chrome/answer/16821166)
12. [Create & manage schedules](https://support.google.com/gemini/answer/17094710?hl=en)

Could not open:

- [Former Spark changelog](https://support.google.com/gemini/answer/17171264?hl=en): redirect fetch failed; its destination, Gemini release notes, opened directly.
- [Custom apps with language parameter](https://support.google.com/gemini/answer/17209137?hl=en): inaccessible; parameter-free URL opened.
- [Schedules without language parameter](https://support.google.com/gemini/answer/17094710): timed out twice; English URL opened.
- [Chrome auto browse with language parameter](https://support.google.com/chrome/answer/16821166?hl=en): timed out; parameter-free URL opened.