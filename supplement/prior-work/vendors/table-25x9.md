---
title: "Nine vendor products against the 25 WARM platform services: first-reader values"
date: 2026-11-12
author: sagan (table built by prior-work/tools/vendor_table.py from the nine reader files)
status: "first readers only; second-reader sample in progress; no cell checked by sagan"
---

Values are each product's own reader file in this folder, protocol version 2, pages read 2026-11-12. `*` marks a cell the reader called DISPUTABLE (the lower value is shown). The last three columns count products per service.

| Service | claude-code | codex | grok-build | antigravity | claude-duet | openai-dots | grok-bot | gemini-spark | meta-muse | yes | part | no |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harness | yes | yes | yes | yes | yes | yes | yes | yes | yes | 9 | 0 | 0 |
| Sessions | yes | yes | yes | yes | yes | yes | yes | yes | part* | 8 | 1 | 0 |
| Tasks | yes | part* | part* | part* | part* | yes | part | part* | part* | 2 | 7 | 0 |
| Environments | yes | yes | yes | yes | yes | yes | part* | yes | yes | 8 | 1 | 0 |
| Scheduling | yes | part* | part* | part | part* | yes | yes | yes | part* | 4 | 5 | 0 |
| Lifecycle | yes | yes | yes | yes | no | yes | part* | part | part | 5 | 3 | 1 |
| Memory | part* | yes | part* | part | part* | part* | part* | part* | part* | 1 | 8 | 0 |
| Retrieval | yes | yes | yes | yes | yes | yes | yes | yes | yes | 9 | 0 | 0 |
| Artifacts | yes | part* | part | part | part | part* | part | part* | part* | 1 | 8 | 0 |
| Models | yes | yes | yes | yes | no* | yes | yes | part* | part* | 6 | 2 | 1 |
| Tools | yes | yes | yes | yes | yes | yes | yes | yes | yes | 9 | 0 | 0 |
| Registry | yes | part* | yes | yes | part* | part* | part | part | part | 3 | 6 | 0 |
| Directory | part | part | part | part | no | part | part | no* | part | 0 | 7 | 2 |
| Messaging | yes | part* | part* | yes | no | part* | yes | no* | part | 3 | 4 | 2 |
| Orchestration | yes | part* | yes | yes | no* | yes | part* | part | part* | 4 | 4 | 1 |
| Channels | yes | yes | yes | yes | yes | yes | yes | part* | yes | 8 | 1 | 0 |
| Identity | part* | yes | part | part | part | yes | part* | part | part | 2 | 7 | 0 |
| Secrets | yes | yes | part | part* | yes | yes | yes | part* | yes | 6 | 3 | 0 |
| Policy | yes | yes | yes | part* | part* | yes | part* | part* | part* | 4 | 5 | 0 |
| Approvals | yes | yes | yes | yes | yes | yes | yes | yes | yes | 9 | 0 | 0 |
| Observability | yes | yes | yes | yes | part* | yes | yes | yes | yes | 8 | 1 | 0 |
| Evaluation | part* | part* | part | part | no* | no* | no | no | no* | 0 | 4 | 5 |
| Improvement | part* | part | part | part* | no* | part | part* | no* | part | 0 | 7 | 2 |
| Releases | part* | part | part | part | no* | no* | part | no | part | 0 | 6 | 3 |
| Reliability | yes | part | part | part* | no* | part | yes | no* | part | 2 | 5 | 2 |
| **yes** | 19 | 14 | 13 | 13 | 8 | 16 | 12 | 8 | 8 | | | |
| **part** | 6 | 11 | 12 | 12 | 8 | 7 | 12 | 11 | 16 | | | |
| **no** | 0 | 0 | 0 | 0 | 9 | 2 | 1 | 6 | 1 | | | |
| **?** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | | | |

## Notes

- **Directory** is derived from C3 and C4 for every product. Claude Code's reader rated it "no" from the definition (pilot, protocol version 1); the table shows the derived value, part.
- **gemini-spark** is now "Tasks in Gemini (formerly known as Spark)"; the reader rated the product as the current help center describes it.
- **openai-dots**: openai.com and help.openai.com refused the requests; seven pages were read from Internet Archive snapshots (2026-10-06 to 2026-11-08). One table cell (Releases) rests on a snapshot.
- **meta-muse**: muse.ai's robots.txt disallows ClaudeBot and carries a notice against automated collection; the reader read its public sitemap pages once each with curl under a browser user agent. CORRECTED 14:50: 19 of the 24 rated rows cite a muse.ai page and 12 cite only muse.ai pages (Harness, Sessions, Tools, Orchestration, Channels, Identity, Secrets, Policy, Approvals, Evaluation, Improvement, Reliability); an earlier version of this note said one cell. The author ruled at 15:18: keep the column, with the disclosure (PROGRESS.md).
- **grok-bot**: the reader used Cursor pages (teams, groups, organization) as vendor material; not yet confirmed that they describe Grok Bot.
- **claude-duet**: no documentation section exists; twelve cells are disputable.
- C1 to C4, first readers: Claude Code part*, part*, part, part*; Codex part*, part, part, part; Grok Build part*, part, part, part; Antigravity part*, part*, part, part*; Claude Duet no*, no, no*, no*; Dots part*, part, part, part; Grok Bot part*, part, part, part*; Tasks in Gemini no*, no*, no*, no*; Muse no*, no*, part, part.
