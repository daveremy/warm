---
title: "Brief used for each vendor-product reader (the two pilot readers got this text with protocol.md; the other seven get it with protocol-v2.md)"
date: 2026-11-12
author: sagan
---

Spawn: fresh `general-purpose` agent (not a fork, which would carry the session's expectations), `model: fable`, `effort: high` (The author, 12:57: research and planning on Fable 5.2 high). One agent per product. Output file `prior-work/vendors/<slug>.md`.

## Template

You are a reader mapping one vendor product to a fixed list of 25 platform services, from the vendor's own current pages. Product: **<PRODUCT>** (<ONE-LINE DESCRIPTION>).

Read first, in full, and follow exactly: prior-work/vendors/protocol-v2.md. For its question 1 also read prior-work/rerate-criteria-v2.md. Open no other file under  (earlier notes, ratings, the paper and the model would contaminate your reading); if a search prints content from one, disclose it and do not use it.

Today is <DATE>. This product changes every few weeks, so do not rate from memory: every value must rest on a vendor page you open today (WebFetch, WebSearch to locate pages, curl, gh). Find the current official documentation and changelog yourself; likely starting points, which may have moved, are <STARTING POINTS>. <INSTALLED-CLI SENTENCE, harnesses only: The product is installed on this machine: you may run `<cli> --version`, `<cli> --help` and help for its subcommands as a primary source, always with stdin closed (append `</dev/null`). Do not start an agent session with it, send it prompts, or change any configuration.>

Be thorough on the 25 rows: for each service, look for the feature in the documentation before deciding, and quote exactly. Keep the reasons short. Do not spawn subagents.

Write the result to prior-work/vendors/<slug>.md in the format the protocol specifies.

Your final message to me: the product version or newest changelog date you saw; a compact list of the 25 services with their values (mark DISPUTABLE cells); your four C1 to C4 values; and what you could not open. Nothing else.

## The seven products still to run

| Slug | Product and one-line description | Starting points | Installed CLI |
|---|---|---|---|
| grok-build | Grok Build (xAI's agent harness: the grok CLI and the surfaces that share it) | docs.x.ai, x.ai/news, github.com/xai-org/grok-build | `grok` (1.0.67) |
| antigravity | Google Antigravity (Google's agent harness: the Antigravity app, CLI and SDK) | antigravity.google and its docs and changelog, blog.google | `agy` (1.5.7) |
| claude-duet | Claude Duet (Anthropic's personal agent, research preview) | anthropic.com/news, support.claude.com, claude.com | none |
| openai-dots | Dots (OpenAI's personal agent in ChatGPT) | openai.com (DevDay 2026 posts), help.openai.com | none |
| grok-bot | Grok Bot (xAI's always-on personal agents) | x.ai/news/introducing-grok-bot, docs.x.ai | none |
| gemini-spark | Gemini Spark (Google's personal agent) | blog.google, support.google.com/gemini, gemini.google | none |
| meta-muse | Muse (Meta's personal agent) | about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/, Meta help center | none |

The personal agents are closed products with little documentation; "not assessed" is an expected value for them.
