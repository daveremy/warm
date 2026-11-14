"""Write one blind second-reader brief per vendor product: a seeded sample of 8 of the
24 non-derived services plus C1 to C4. Usage: python second_reader_briefs.py <run-dir> <slug>..."""
import datetime, random, sys
from pathlib import Path

SERVICES = ["Harness","Sessions","Tasks","Environments","Scheduling","Lifecycle","Memory","Retrieval",
  "Artifacts","Models","Tools","Registry","Messaging","Orchestration","Channels","Identity","Secrets",
  "Policy","Approvals","Observability","Evaluation","Improvement","Releases","Reliability"]
PRODUCTS = {
 "claude-code": ("Claude Code", "Anthropic's agent harness: the claude CLI and the surfaces that share it", "code.claude.com/docs, docs.claude.com, github.com/anthropics/claude-code (CHANGELOG.md)", "claude"),
 "codex": ("Codex CLI", "OpenAI's agent harness: the codex CLI and the surfaces that share it", "developers.openai.com/codex, github.com/openai/codex (releases)", "codex"),
 "grok-build": ("Grok Build", "xAI's agent harness: the grok CLI and the surfaces that share it", "docs.x.ai, x.ai/news, github.com/xai-org/grok-build", "grok"),
 "antigravity": ("Google Antigravity", "Google's agent harness: the Antigravity app, CLI and SDK", "antigravity.google and its docs and changelog, blog.google", "agy"),
 "claude-duet": ("Claude Duet", "Anthropic's personal agent, research preview", "anthropic.com/news, support.claude.com, claude.com", None),
 "openai-dots": ("Dots", "OpenAI's personal agent in ChatGPT", "openai.com (DevDay 2026 posts), help.openai.com", None),
 "grok-bot": ("Grok Bot", "xAI's always-on personal agents", "x.ai/news/introducing-grok-bot, docs.x.ai", None),
 "gemini-spark": ("Gemini Spark", "Google's personal agent", "blog.google, support.google.com/gemini, gemini.google", None),
 "claude-managed-agents": ("Claude Managed Agents, self-hosted", "Anthropic's agent platform, in the form a customer runs on its own infrastructure", "platform.claude.com/docs (Managed Agents, self-hosted, and release notes)", None),
 "meta-muse": ("Muse", "Meta's personal agent", "about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/, Meta help center", None),
}
SEED = "20261112"
run = Path(sys.argv[1])
for slug in sys.argv[2:]:
    name, desc, starts, cli = PRODUCTS[slug]
    sample = sorted(random.Random(f"{SEED}-{slug}").sample(SERVICES, 8), key=SERVICES.index)
    cli_s = (f" The product is installed on this machine: you may run `{cli} --version`, `{cli} --help` and help for its subcommands as a primary source, always with stdin closed (append `</dev/null`). Do not start an agent session with it, send it prompts, or change any configuration." if cli else "")
    brief = f"""You are a second reader re-rating a sample of one vendor product's mapping to a fixed list of platform services, from the vendor's own current pages. A first reader has already rated this product; you must not see that work. Product: **{name}** ({desc}).

Read first, in full, and follow exactly the two files in the current directory: protocol-v2.md and rerate-criteria-v2.md (the second is for the protocol's question 1). Open no other local file anywhere on this machine: earlier notes, ratings, the paper and the model would contaminate your reading. If a search prints content from one, disclose it and do not use it.

Today is {datetime.date.today().isoformat()}. This product changes every few weeks, so do not rate from memory: every value must rest on a vendor page you open today with web search. Find the current official documentation and changelog yourself; likely starting points, which may have moved, are {starts}.{cli_s}

Rate ONLY these eight services, by the protocol's definitions and value rules: {", ".join(sample)}. Then answer the protocol's question 1 (C1 to C4), with a quote for each value. Do not rate the other services, do not rate or derive the Directory row, and skip questions 2 to 4. For each service look for the feature in the documentation before deciding, and quote exactly. Keep the reasons short. Do not spawn subagents.

You cannot write files. Your final message is the deliverable, in markdown: a first line with the product version or the newest changelog date you saw; a table with the columns Service, Value, Quote, URL, Availability and reason (mark DISPUTABLE cells with the other value); the four C1 to C4 values, each with a quote and URL; the list of pages you opened; and what you could not open. American English spelling outside quotations. Nothing else.
"""
    (run / "briefs" / f"{slug}.txt").write_text(brief)
    print(slug, ",".join(sample))
