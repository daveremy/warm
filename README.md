# WARM: the Working Agents Reference Model

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24238372.svg)](https://doi.org/10.5281/zenodo.24238372)

Part of **Working Agents**, a living series of working papers on operating AI agents and agent software development: [the plan and index](https://daveremy.github.io/working-agents/) · [all papers on Zenodo](https://zenodo.org/communities/working-agents).

The parts of a system in which agents finish work end to end, and a rule for reviewing every stop
for a person. Derived from one implementation, three agent platforms and fourteen published
models, and mapped to ten vendor products.

**Read the paper:** [web](https://daveremy.github.io/warm/) · [PDF](docs/warm.pdf) · [source](docs/index.html)

**Check the evidence:** [the supplement](supplement/), with its own [README](supplement/README.md)

## In one paragraph

WARM names the parts of a system of AI agents and how they relate. People direct the work, domains
define it, agents carry it out, and a platform of 25 services in six groups provides what agents in
every domain share. The model is written for systems in which agents finish work without a person
approving each action, and its central rule follows from that aim: every stop for a person is
recorded and reviewed. The review asks whether the stop needed a person, whether a decision could
have been made in advance, and what change would remove the stop next time. The rule is a proposal
that the source system does not yet carry out. The paper maps the model to three agent platforms,
compares it with fourteen published models, and reads ten vendor products against it from their
vendors' documentation (first readings 12 November 2026). WARM is a working model drawn largely from
one system, and no evidence yet shows that organizing a system this way improves it.

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

Remy, D. *WARM: the Working Agents Reference Model.* Working paper, version 0.1, November 2026.
https://doi.org/10.5281/zenodo.24238372

*Created in collaboration with AI.*
