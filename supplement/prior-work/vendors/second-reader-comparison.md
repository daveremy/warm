---
title: "Vendor mappings: first reader against a blind second reader, on a sample"
date: 2026-11-12
author: sagan (numbers from prior-work/tools/second_reader_agreement.py)
status: "computed 2026-11-12 14:36; the 19 differing cells are adjudicated in adjudication-19.md (14:44)"
---

## Design

- First reader: one Claude subagent per product (claude-fable-5-2, high effort), all 25 services and C1 to C4, protocol version 2.
- Second reader: gpt-6-astra through `codex --search exec -s read-only`, one run per product, given only protocol-v2.md and rerate-criteria-v2.md and told to open no other local file. A different model family from the first reader.
- Sample: 8 of the 24 non-derived services per product, drawn with seed "20261112-<slug>" (second_reader_briefs.py), plus all four of C1 to C4. 72 service cells and 36 criterion cells.
- Compared: the base value (yes, part, no). A DISPUTABLE mark does not count as a difference.
- Own-vendor readings: Codex CLI and Dots were second-read by an OpenAI model; Claude Code and Claude Duet were first-read by an Anthropic model.

## Result

```
claude-code   services 8/8  C 4/4   C1:part*/part* C2:part*/part C3:part/part C4:part*/part
codex         services 6/8  C 4/4   C1:part*/part* C2:part/part C3:part/part C4:part/part
grok-build    services 6/8  C 4/4   C1:part*/part C2:part/part C3:part/part C4:part/part
antigravity   services 8/8  C 3/4   C1:part*/part* C2:part*/yes C3:part/part C4:part*/part*
claude-duet   services 6/8  C 3/4   C1:no*/no* C2:no/no* C3:no*/part C4:no*/no*
openai-dots   services 4/8  C 4/4   C1:part*/part C2:part/part C3:part/part C4:part/part
grok-bot      services 7/8  C 2/4   C1:part*/yes C2:part/part C3:part/part C4:part*/yes
gemini-spark  services 7/8  C 3/4   C1:no*/no C2:no*/no C3:no*/part C4:no*/no
meta-muse     services 7/8  C 3/4   C1:no*/no* C2:no*/no* C3:part/no* C4:part/part
TOTAL services [59, 72] criteria [30, 36]
DIFF codex Tasks part* yes
DIFF codex Policy yes part*
DIFF grok-build Scheduling part* yes
DIFF grok-build Improvement part yes
DIFF antigravity C2 part* yes
DIFF claude-duet Sessions yes part*
DIFF claude-duet Observability part* yes
DIFF claude-duet C3 no* part
DIFF openai-dots Environments yes part*
DIFF openai-dots Identity yes part*
DIFF openai-dots Policy yes part*
DIFF openai-dots Evaluation no* part
DIFF grok-bot Orchestration part* yes
DIFF grok-bot C1 part* yes
DIFF grok-bot C4 part* yes
DIFF gemini-spark Models part* yes
DIFF gemini-spark C3 no* part
DIFF meta-muse Policy part* yes
DIFF meta-muse C3 part no*
```

Each C cell reads first/second; `*` is a DISPUTABLE mark.

- Services: 59 of 72 agree (82%). Criteria: 30 of 36 (83%). Together 89 of 108 (82%).
- All 19 differences are one step apart (yes against part, or part against no). No cell has yes against no.
- In 18 of the 19, one of the two readers had marked the cell DISPUTABLE. The exception is Grok Build, Improvement (first part, second yes, from `/skillify`).
- Direction: the second reader is higher in 13 and lower in 6. The protocol tells a reader to give the lower of two defensible values.
- Own vendor: the OpenAI model rated Dots lower than the first reader on three cells (Environments, Identity, Policy) and higher on one (Evaluation); on Codex CLI one higher (Tasks), one lower (Policy).
- Weakest product: Dots, 4 of 8. Its first reader could not open openai.com or help.openai.com and used archive snapshots for seven pages.

## What this does to the first-reader patterns

- "No product rates yes on any of C1 to C4" holds for the first readers only. The second reader gives yes on Antigravity C2 (a Teamwork team's request artifact and defined roles), Grok Bot C1 (organizations and teams) and Grok Bot C4 (a Team Bot suggests other Team Bots that fit a request).
- "No product rates yes on Improvement" holds for the first readers only: the second reader gives Grok Build yes.
- Directory was not sampled (it is derived). Evaluation and Releases keep zero yes values in the sample.
- C3 is the least stable criterion: three of nine differ (Claude Duet, Tasks in Gemini, Muse), all between no and part.

## Not done

- DONE 14:44: the 19 cells are adjudicated in `adjudication-19.md`. After adjudication one cell on C1 to C4 rates yes (Grok Bot, C4), and no product rates yes on Improvement.
- A second reading of the 16 unsampled services per product.
- A quote check of the first-reader files other than Antigravity, whose reader checked its own.
