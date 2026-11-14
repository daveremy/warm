# WARM: evidence supplement

This folder holds the evidence behind the tables and figures of "WARM, the Working Agents Reference Model", draft 10 of 13 November 2026 (model version 0.14). It contains the frozen criteria, the readers' files with their quotations and rating reasons, the search record, the second readings and the decisions on the cells where two readers differed, and the two scripts that built the paper's tables.

Every reader, mapper and second rater was an AI agent working for the author (Section 7 of the paper). The files are their working notes as written, with local file paths and machine names removed. They were not edited for style, and they keep their dates, their stated limits and their errors.

## Recompute the counts

```
python3 recompute.py
```

Python 3.9 or later; no packages. The script ends with `All checks passed.` and exit status 0. It does two things.

1. It runs the two generators that built the paper's tables (`paper/build/gen.py` and `paper/build/gen_vendors.py`, unchanged) on the files in this folder, and checks that each table or figure they write is, character for character, the one in the draft (`paper/warm-paper-d10.html`). This covers every cell of Tables 5, 7, 7a and 8 and of Figures 3 and 4.
2. It counts again, without the generators, the numbers that the generators hold as constants: Table A2 and Figure 3 from the four assignment tables, the first row of Figure 4 and the rows of Table 6 from the reference implementation's list of services, Table A1 from the search record, and the sixteen rows of Table 5 whose values the generator holds as constants.

The script prints these counts, which are the ones in the draft:

| Count | Value | Where in the draft |
|---|---|---|
| Table 7, cells as shown | 106 yes, 127 part, 17 no, of 250 | Section 5.5 |
| Table 7, cells as read | 116 yes, 116 part, 18 no | Section 5.5 |
| Services rated yes, four harnesses | 18, 12, 11, 12 | Section 5.5 |
| Services rated yes, five personal agents | 6, 10, 12, 6, 8 | Section 5.5 |
| Services rated yes, the platform product | 11 | Section 5.5 |
| Approvals rated yes | 5 of 10 products | Section 5.5 |
| Services with no yes rating | 6 (Directory, Identity, Policy, Evaluation, Improvement, Releases) | Section 5.5 |
| Marks in Table 7 | 61 dagger, 16 double dagger, 13 section sign | Table 7 |
| Cells a reader marked disputable | 83 of 240 service cells, 23 of 40 criterion cells | Section 5.5 |
| Asterisks kept in Tables 7 and 8 | 81 and 18 | Tables 7 and 8 |
| Table 5, seventeen sources, yes on C1 to C4 | 2, 0, 0, 3 | Section 5.3 |
| Table A2, components | 146, 307, 848, 849 | Appendix A.3 |
| Table A1, records | 1,634 screened; 1,314; 258; 61; 13; 48; 8 mapped | Appendix A.1 |

The script writes `paper/src/` and two files of totals under `paper/build/`. They can be deleted.

Two differences of wording between the draft and the model file are printed as notes and are not counts: Table 2 omits "(a task or run)" from the Tasks row, and Table A3 omits "TTL" from the Policy row.

## Where the evidence for each table and figure is

Paths are relative to this folder.

| In the draft | Files |
|---|---|
| Table 1 (two kinds of agent), Figure 1 (layers), Figure 2 (review of stops), Table 3 (charter), Table 4 (one request, traced) | `model/warm-model-v0.14.md`. These state the model and hold no counts. Earlier versions that a mapping used as its yardstick: `model/warm-model-v0.10.md` to `v0.13.md` |
| Table 2 (25 services), Table A3 (industry terms) | `model/warm-model-v0.14.md`, the table of services |
| Figure 3, Table A2 (inventory entries by assignment) | `platform-mapping/inventory-agentcore.md`, `inventory-langgraph.md`, `inventory-openclaw.md` (the inventories); `mapping-agentcore.md`, `mapping-langgraph.md`, `mapping-openclaw.md` (every assignment with its reason); `mapping.md` (synthesis); `predictions.md` (written before the inventories); `spot-check.md` (second rater). Reference implementation: `lifeos-assignments.tsv`, `lifeos-spot-check.md` |
| Figure 4 (eighteen rows by 29 parts) | `prior-work/source-by-part-grid.md` (each cell cites a line of a note); `prior-work/directory-column-rule.md`; `prior-work/rerate-four-columns.md`; the notes it cites: `prior-work/mapping-yu-zhu.md`, `mapping-aam5c.md`, `mapping-vendors.md`, `mapping-round2-charters.md`, `mapping-round2-platforms.md`, `charterion-full.md`. First row: `platform-mapping/lifeos-services.tsv` |
| Table 5 (four criteria, 30 sources) | Criteria: `prior-work/rerate-criteria.md` and `rerate-criteria-v2.md`. Seventeen sources: `prior-work/rerate-four-columns.md`. Eight sources read by two readers: `prior-work/rerate-v2-reader-a.md`, `rerate-v2-reader-b.md`, `rerate-v2-comparison.md`, `rerate-v2-sources.md`, `platform-joined-sources.md`. Ten further sources: `prior-work/organizational-mas.md` |
| Table 6 (services partial in the reference implementation) | `platform-mapping/lifeos-services.tsv` gives the status of each service. The gaps are stated in the table itself; the mapper's reasons are withheld (see below) |
| Tables 7, 7a and 8 (ten vendor products) | Protocol: `prior-work/vendors/protocol.md`, `protocol-v2.md`, `reader-brief.md`. First readers, one file for each product with the quotation, page and reason for every cell: `prior-work/vendors/<product>.md`. Second readers: `prior-work/vendors/second-reader/` (`sample.txt` is the seeded sample, `briefs/` the instructions, `out/` the readings). Cells where the readers differed: `prior-work/vendors/second-reader-comparison.md`, `adjudication-19.md`, `second-reader/comparison-claude-managed-agents.md`. The thirteen changed cells: `prior-work/vendors/consistency-check.md`, `consistency-check-tenth.md`, `consistency-check-d9.md`, and the `RULED` and `WHY` tables in `paper/build/gen_vendors.py` |
| Table A1 (the documented search) | `prior-work/search.md` (protocol, deviations, every query, the screening results and the flow count in its Section 9); `prior-work/synthesis-round2.md` |
| Section 5.6 (what sources and products do with people's decisions; no table) | `prior-work/decision-review/protocol.md`, `protocol-v2.md`, `readers.md`, `references.txt`, `out/` (six readers), `synthesis.md` |
| Appendix A.2 (second rater of the comparison, the reading on autonomy) | `prior-work/second-rater.md`, `prior-work/autonomy-check.md` |
| Section 2.5 (domains and platforms in human organizations) | `prior-work/ddd-teamtopologies-datamesh.md` |

Other files: `prior-work/synthesis.md` and `prior-work/predictions.md` (the first round and its predictions), `prior-work/vendor-products-inventory.md` (how the products were chosen), `prior-work/vendors/table-25x9.md` (the first table, nine products, before the second readings), and `prior-work/tools/` (the scripts that drew the second readers' samples, compared readings and checked quotations).

## What is frozen

- `prior-work/rerate-criteria.md`: the four criteria C1 to C4, written before the separate rating.
- `prior-work/rerate-criteria-v2.md`: the clarified criteria, frozen before the two further readers started.
- `prior-work/vendors/protocol.md` and `protocol-v2.md`: the vendor protocol. Version 1 was frozen before any reader started and was used for a pilot of two products. Version 2 was frozen before the other readers started and makes one change, the rule for the Directory row.
- `prior-work/decision-review/protocol-v2.md`: the five questions H1 to H5, frozen before any reader started.
- `prior-work/directory-column-rule.md`: the one rule for the Directory column of the grid.
- `model/warm-model-v0.13.md`: the definitions of the 25 services that the vendor products and the reference implementation were rated against.

## What is withheld

- **Source texts.** No paper, specification or vendor page is reproduced. The notes quote short passages (none longer than 750 characters) with the page or URL. The copies the readers used (the Charterion specification, FIPA SC00023K, the ISLANDER, AMELI and JaCaMo articles and two others) are not in this folder; the paper's reference list cites the ones it uses. `prior-work/tools/quotecheck.py` needs those copies and cannot be run from this folder.
- **Quotations from muse.ai pages.** That site carries a notice against automated collection. The Muse reader files keep each value, its reason and the address of the page, and 78 quoted passages are replaced by `[quotation withheld: muse.ai page]`. Where a line cites a muse.ai page and another page, every quotation on the line is withheld.
- **The reference implementation's inventory.** LifeOS is a private system. For it this folder gives, for each of the 849 inventory rows, its kind, its assignment, whether the fit was clean or strained, and the rule that assigned it where a rule did (`platform-mapping/lifeos-assignments.tsv`), the status of each of the 25 services (`lifeos-services.tsv`), and the second rater's agreement counts (`lifeos-spot-check.md`). Component names, descriptions and the mapper's and second rater's reasons are withheld, so a reader can recompute the counts for this row and cannot check the judgments behind them. Some notes cite lines of the withheld files; the citations are kept.
- **Session logs** of the second readers, the drafts and reviews of the paper, and an earlier coverage matrix that no table rests on.
- **The author's words.** The working notes recorded the author's decisions by name and often in his words. Here his name is replaced by "the author" and each quotation by a paraphrase; no decision, date or value is changed. One comment line in `paper/build/gen_vendors.py` was changed the same way, and the tables it writes are identical.

## Limits

This folder makes the counts reproducible and the reasons readable. It does not make the ratings independent: one model family did most of the reading, most cells have one reader, and the mappers knew the model. Section 7 of the paper states these limits.
