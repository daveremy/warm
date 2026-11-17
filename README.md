# WARM: the Working Agents Reference Model

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24238372.svg)](https://doi.org/10.5281/zenodo.24238372)

Part of **Working Agents**, a living series of working papers on operating AI agents and agent software development: [the plan and index](https://daveremy.github.io/working-agents/) · [all papers on Zenodo](https://zenodo.org/communities/working-agents).

The parts of a system in which agents finish work end to end, and a rule for reviewing every stop
for a person. Derived from one implementation, three agent platforms and fourteen published
models, and mapped to ten vendor products.

**Read the paper:** [web](https://daveremy.github.io/warm/) · [PDF](docs/warm.pdf) · [source](docs/index.html)

**Short on time?** [The short article](https://daveremy.github.io/warm/article.html) · [the narrated talk, 15 minutes](https://daveremy.github.io/warm/warm-talk.mp4) · [the deck, 44 slides (PDF)](docs/warm-deck.pdf)

**Check the evidence:** [the supplement](supplement/), with its own [README](supplement/README.md)

## In one paragraph

WARM names the parts of a system of AI agents and how they relate. People direct the work, domains
define it, agents carry it out, and a platform of 25 services in six groups provides what agents in
every domain share. The model was drawn first from a working system and took its vocabulary from a
survey of 34 sources; mappings of three agent platforms and comparisons with fourteen published models
corrected it in more than twenty places. Every platform service has at least a partial counterpart in
nine or more of the seventeen platforms and models. Two of the seventeen define an area of work in
their model, an idea the organizational multi-agent literature of 2002 to 2004 already specified. Ten
vendor products, read from their vendors' documentation from 12 November 2026, all rate in full on the
agent loop, retrieval and tools; no reading established a full rating on a directory, identity, policy,
evaluation, improvement or releases. The model also proposes that every stop for a person is recorded
and reviewed. WARM is a working model drawn largely from one system, and no evidence yet shows that
organizing a system this way improves it.

## The evidence supplement

The folder `supplement/` holds the evidence behind the paper's tables and figures: the frozen
criteria, the readers' files with their quotations and rating reasons, the search record, the second
readings and the decisions on cells where readers differed, the model versions 0.10 to 0.14, and the
two scripts that generate the tables. `python3 recompute.py`, run in that folder, rebuilds every
table and count and compares them with the paper. The supplement's README lists what the folder
leaves out and why.

The supplement was assembled against draft 10 of 13 November 2026 and names it throughout. Version
0.1 is that draft: the title block, the page metadata and the print style sheet changed, and no
other text did.

## Versions

- **0.1.1**, 17 November 2026: the subtitle and abstract lead with what was mapped and what was found; the review of stops for a person is presented as one proposal; the conclusion and Section 7 say the refactoring has begun and its measures are not yet set. No count, rating or table changed.
- **0.1**, 14 November 2026: first version (model version 0.14).

## What this is, and is not

This is a working model and a dated map, offered so others can use the vocabulary, repeat the
mappings, criticize them and improve them. It is not a standard, a product, a framework to install
or a commercial offering. The reference implementation is a personal project; its code is not part
of this repository.

## Feedback

Open an issue for questions, corrections to a rating, or a mapping of your own system or product.
A vendor's correction to how its product is represented is especially welcome.

## License

The paper, the supplement and this README are licensed under
[Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) (see `LICENSE`).
Reuse, adapt and share them, with attribution. Quotations from third-party sources in the supplement
remain their authors'.

## Citation

Remy, D. *WARM: the Working Agents Reference Model.* Working paper, version 0.1.1, November 2026.
https://doi.org/10.5281/zenodo.24238372

*Created in collaboration with AI.*
