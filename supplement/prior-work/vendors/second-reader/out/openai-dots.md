Dots — newest changelog date seen: **November 12, 2026** ([Enterprise/Edu release notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes)); newest Dots-specific dated update opened: **November 4, 2026**.

Availability below: gradual rollout to eligible Pro and Business Premium accounts; generally available to eligible Enterprise, Edu, and Healthcare workspaces, with admin-enabled preview through November 18. [Current availability](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)

| Service | Value | Quote | URL | Availability and reason |
|---|---|---|---|---|
| Harness | **yes** | “carries it out using the appropriate computer or app tool, then uses the result to continue your task.” | [Safety design, “A separate check before dots act”](https://openai.com/index/how-we-build-safety-security-and-privacy-into-dots/); [Task context](https://learn.chatgpt.com/docs/dots/tasks-and-memory) | Available under the rollout above. The hosted loop uses context, executes model-directed tools, and continues from results; delegated tasks receive selected instructions and context. |
| Environments | **part — DISPUTABLE: yes** | “their own cloud computer, their own browser”; “separate task boundary, not an isolation guarantee.” | [Introduction, “Dots can work on their own”](https://openai.com/index/introducing-dots/); [Security architecture](https://learn.chatgpt.com/docs/enterprise/dots-security) | Available. Each dot has a cloud environment, but isolation between every delegated agent is not established. **Yes** is defensible for the personal dot’s own environment. |
| Lifecycle | **yes** | “view personal dots and their connections, pause or resume them”; “Workspace owners can also delete personal dots.” | [Enterprise release notes, November 4](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes); [Creation](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot) | Enterprise admin preview. Creation, inventory, pause, resume, and deletion are documented. Separate delegated work may require separate stopping. |
| Artifacts | **part** | “Files, Codex threads, and ChatGPT conversations your dot created are stored separately.” | [Privacy FAQ, deletion](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs) | Available. Outputs persist in their storage locations. Searches for Dots file versions and version history found no documented product-wide artifact versioning. |
| Identity | **part — DISPUTABLE: yes** | “its creator”; “service account identity or dot ID” | [Workspace management, “Managing personal dots”](https://help.openai.com/en/articles/20001554-managing-dots-in-chatgpt-workspaces) | Enterprise admin preview. Inventory associates a dot with its creator and identity; access can be revoked. Complete identity revocation across connected accounts and delegated agents requires separate handling. **Yes** is defensible for the primary personal dot alone. |
| Secrets | **yes** | “dots can use saved passwords without exposing them to the model.” | [Introduction, “Built-in safeguards”](https://openai.com/index/introducing-dots/); [Credential-service details](https://openai.com/index/how-we-build-safety-security-and-privacy-into-dots/) | Available for supported sign-ins, subject to password-manager permission. An encrypted service supplies credentials at sign-in outside model context. This protection does not cover secrets pasted into readable content. |
| Policy | **part — DISPUTABLE: yes** | “The review determines whether the action can proceed, needs your approval, or includes a step you must do yourself.”; “Coverage across browser, desktop, and delegated actions remains under review.” | [Action review](https://learn.chatgpt.com/docs/dots/controls); [Coverage limits](https://learn.chatgpt.com/docs/enterprise/dots-security) | Available, with workspace restrictions. Rules, allow/block decisions, information-sharing checks, and retention controls cover substantial portions. **Yes** is defensible for supported paths; complete coverage is not established. |
| Evaluation | **part** | “Your dot can check results and send follow-up instructions to tasks it created.” | [Meet dots, “Tasks and conversations”](https://learn.chatgpt.com/docs/dots); [Safety checks](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs) | Available. Result checking and behavior checks against instructions are documented. Searches found no general criteria-based evaluation facility with an explicit unknown outcome when a check cannot run. |

**C1 — part.** “ongoing responsibility”; “Each member can create one personal dot.” The responsibility-bearing unit is a single agent, which C1 explicitly limits to **part**. No independently defined collection of work areas was found in the Dots guides. [Getting started, overview and availability](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)

**C2 — part.** “Describe the responsibility and share the source material it needs”. Responsibilities and instructions attach to the dot; no area-level specification combining a mission with independently defined positions was found. [Meet dots, “Work with your dot”](https://learn.chatgpt.com/docs/dots)

**C3 — part.** “Use the inventory to find a dot and review its owner and status”. This is a kept ownership record per agent, not a unique accountable-area mapping per responsibility or capability. [Admin guide, “Manage dots in your workspace”](https://learn.chatgpt.com/docs/enterprise/dots-admin-guide)

**C4 — part.** “Your dot can divide work among background agents that run in parallel and report back to it.” Routing is documented within the dot’s own coordination. Searches for directories, registered capabilities, and handler lookup found no runtime capability lookup available to arbitrary agents. [Tasks and memory, “Assigned work”](https://learn.chatgpt.com/docs/dots/tasks-and-memory)

Pages opened, all read **November 12, 2026**; repeated opens and redirected aliases consolidated:

1. [Getting started with your dot](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)
2. [Introducing dots](https://openai.com/index/introducing-dots/)
3. [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
4. [ChatGPT Enterprise and Edu release notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes)
5. [Managing dots in ChatGPT workspaces](https://help.openai.com/en/articles/20001554-managing-dots-in-chatgpt-workspaces)
6. [How we build safety, security, and privacy into dots](https://openai.com/index/how-we-build-safety-security-and-privacy-into-dots/)
7. [GPT-6 Astra System Card, including Dots appendix](https://deploymentsafety.openai.com/gpt-6-astra/change-log)
8. [Auto-review](https://learn.chatgpt.com/docs/sandboxing/auto-review)
9. [Dots privacy, security, and safety FAQs](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs)
10. [Meet dots](https://learn.chatgpt.com/docs/dots)
11. [Manage dots permissions and capabilities](https://learn.chatgpt.com/docs/enterprise/dots-admin-guide)
12. [November 2–6, 2026 updates](https://learn.chatgpt.com/docs/whats-new/november-2-6-2026)
13. [Tasks and memory](https://learn.chatgpt.com/docs/dots/tasks-and-memory)
14. [Safety and security in dots](https://learn.chatgpt.com/docs/enterprise/dots-security)
15. [ChatGPT & Codex changelog](https://learn.chatgpt.com/docs/changelog)
16. [Control your dot](https://learn.chatgpt.com/docs/dots/controls)

Could not open: **none of the pages attempted**.

Disclosure: Besides the two specified protocol files, higher-priority operating instructions required reading the [OpenAI Docs skill](~/.codex/skills/.system/openai-docs/SKILL.md). It supplied workflow instructions and was not used as rating evidence. No earlier notes, ratings, paper, or model files were opened or printed. No files were written.