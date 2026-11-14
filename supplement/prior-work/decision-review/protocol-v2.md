---
title: "Protocol, version 2: what a source defines about decisions made by people and tasks handed to people (five questions)"
date: 2026-11-12
author: sagan
status: "version 2, frozen 2026-11-12 15:38, before any reader started. One change from protocol.md: question H5 (tasks handed to a person), added after the author widened the measure at 15:36. Do not edit; a change is a new file."
---

# Purpose

Record, for each source or product, what it defines about the decisions that people make on the actions of AI agents, and what it does with those decisions afterward. The reader decides from what the source states and does not infer what it "probably" has.

# The five questions

Each gets **yes**, **part**, **no** or **not assessed**, with one exact quotation and its location (page, section or URL), or, for **no**, the terms searched and not found. When two values are both defensible, give the lower and mark the cell DISPUTABLE with the other value and the reason.

**H1. A record of each decision.** When an agent's action waits for a person, or a person approves, changes or declines it, the source keeps a record of that decision.
- **yes**: a record per decision that includes why a person was needed (the rule, threshold or condition that sent it to a person) and what the person decided.
- **part**: decisions are logged, without the reason a person was needed or without the outcome.
- **no**: no such record.

**H2. A measure of how often people are required.** The source defines a quantity that counts or rates decisions by people (for example an escalation rate, an approval rate, an intervention rate, interruptions per task).
- **yes**: a defined measure, named, with what it counts.
- **part**: such a quantity is mentioned without a definition, or only as an example.
- **no**: none.

**H3. A review of past decisions that changes the rules.** The source defines a process, role or mechanism that examines past decisions by people in order to change what is asked of people in the future: for example, turning an action that people keep approving into a standing approval, a policy or an allow rule; or removing a step that did not need a person.
- **yes**: a defined process or mechanism with that purpose, covering decisions in general.
- **part**: a mechanism for one narrow kind of decision (for example, suggesting an allow rule for a repeated tool call), or a stated goal with no mechanism, or a manual option the user may take ("always allow") with no review.
- **no**: none.

**H4. Authority that changes with the record.** The source defines that an agent's authority (what it may do without a person) widens or narrows according to its past performance.
- **yes**: a defined mechanism or rule.
- **part**: stated as a principle or future work.
- **no**: none.

**H5. Tasks handed to a person because an agent could not do them.** The source treats a step that an agent passes to a person for lack of capability (a login, a document it cannot reach, an action in an application it cannot operate), as distinct from a step that waits for a person's authority.
- **yes**: such hand-offs are recorded or counted, and the source defines a way to reduce them (new tools, access, computer use) from that record.
- **part**: the source describes handing a step to a person (a takeover, a manual step) with no record or count, or it counts them with no way to reduce them.
- **no**: none.

# Also record

- Any other passage in which the source treats reducing the need for people's decisions as a goal, with the quotation. Any passage in which it says the opposite (that people's decisions should not be reduced), with the quotation.
- For each source: what you opened (URL or file), the date, and what you could not open. A source you could not open is **not assessed** on all five; do not rate from memory or from a summary of the source.

# Output

One Markdown file: a table (source, H1, H2, H3, H4, H5, each with value, quotation and location), then the further passages, then what was opened and what was not, then disclosures. American English outside quotations.
