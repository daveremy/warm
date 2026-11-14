"""Draft 9 (RULED has thirteen cells, Table 7a lists them, reader-flag counts added; draft 8 copy: gen_vendors.d8.py).
Draft 8: build Table 7 (ten vendor products by 25 services) and Table 8 (C1 to C4) from the
reader files in prior-work/vendors, with the 22 adjudicated cells applied: 19 from adjudication-19.md and
3 for the tenth product from second-reader/comparison-claude-managed-agents.md.
Writes src/tab-vendors.html, src/tab-vendors-c.html and build/vendor-totals.json.
Usage: python3 build/gen_vendors.py   (run from paper/)"""
import json, re, sys
from pathlib import Path
V = Path("../prior-work/vendors"); sys.path.insert(0, "../prior-work/tools")
sys.argv = [sys.argv[0], str(V)]   # second_reader_compare reads argv at import; with no slug it prints nothing
from second_reader_compare import SERVICES, table
SLUGS = ["claude-code","codex","grok-build","antigravity","claude-duet","openai-dots","grok-bot","gemini-spark","meta-muse","claude-managed-agents"]
NAMES = ["Claude Code","Codex CLI","Grok Build","Anti&shy;gravity","Claude Duet","Dots","Grok Bot","Tasks in Gemini","Muse","Claude Managed Agents"]
HARNESS = SLUGS[:4]; PERSONAL = SLUGS[4:9]; PLATFORM = SLUGS[9:]   # the tenth product is a platform: neither a harness nor a personal agent
VAL = re.compile(r"\b(not assessed|yes|part|no)\b", re.I)
def base(cell):
    m = re.match(r"\s*(not assessed|yes|part|no)\b", cell, re.I)
    return (m.group(1).lower() if m else "?") + ("*" if "DISPUTABLE" in cell.upper() else "")
def crit(path):
    out = {}
    for line in path.read_text().splitlines():
        if re.match(r"\|?\s*\**\s*(Interaction \| )?Directory", line) or "erived" in line: continue
        for n in "1234":
            m = re.search(rf"\bC{n}\b(?! to)", line)
            if m and f"C{n}" not in out:
                v = VAL.search(line[m.end():])
                if v: out[f"C{n}"] = v.group(1).lower() + ("*" if "DISPUTABLE" in line.upper() else "")
    return out
# (slug, cell): (first reader, second reader, adjudicated). Source: prior-work/vendors/adjudication-19.md
ADJ = {
 ("codex","Tasks"):("part*","yes","part*"), ("codex","Policy"):("yes","part*","part*"),
 ("grok-build","Scheduling"):("part*","yes","part*"), ("grok-build","Improvement"):("part","yes","part*"),
 ("antigravity","C2"):("part*","yes","part*"),
 ("claude-duet","Sessions"):("yes","part*","part*"), ("claude-duet","Observability"):("part*","yes","part*"), ("claude-duet","C3"):("no*","part","part"),
 ("openai-dots","Environments"):("yes","part*","part*"), ("openai-dots","Identity"):("yes","part*","part*"),
 ("openai-dots","Policy"):("yes","part*","part*"), ("openai-dots","Evaluation"):("no*","part","no*"),
 ("grok-bot","Orchestration"):("part*","yes","part*"), ("grok-bot","C1"):("part*","yes","part*"), ("grok-bot","C4"):("part*","yes","yes"),
 ("gemini-spark","Models"):("part*","yes","part*"), ("gemini-spark","C3"):("no*","part","part"),
 ("meta-muse","Policy"):("part*","yes","part*"), ("meta-muse","C3"):("part","no*","part"),
 # Source: prior-work/vendors/second-reader/comparison-claude-managed-agents.md (2026-11-13)
 ("claude-managed-agents","Environments"):("yes","part*","part*"), ("claude-managed-agents","Channels"):("part*","yes","part*"),
 ("claude-managed-agents","C3"):("part","no*","part"),
 # second-read by choice, not in the seeded sample (comparison file, addendum, ruling 23)
 ("claude-managed-agents","Approvals"):("part*","yes","yes"),
}
assert len(ADJ) == 23
sample = {l.split()[0]: l.split()[1].split(",") for l in (V/"second-reader"/"sample.txt").read_text().splitlines() if l.strip()}
adjtext = (V/"adjudication-19.md").read_text()
first, C = {}, {}
for s in SLUGS:
    t = table(V/f"{s}.md"); first[s] = {k: base(t.get(k, "")) for k in SERVICES}; C[s] = crit(V/f"{s}.md")
    assert all(k in C[s] for k in ("C1","C2","C3","C4")), (s, C[s])
    assert all(first[s][k] != "?" for k in SERVICES if k != "Directory"), s
final = {s: dict(first[s]) for s in SLUGS}; Cf = {s: dict(C[s]) for s in SLUGS}
for (s, k), (a, b, adj) in ADJ.items():
    src = C[s] if k in ("C1","C2","C3","C4") else first[s]
    assert src[k] == a, (s, k, src[k], a)          # the override must start from what the reader file says
    (Cf[s] if k in ("C1","C2","C3","C4") else final[s])[k] = adj
def derive(c3, c4):
    c3, c4 = c3.rstrip("*"), c4.rstrip("*")
    return "yes" if c3 == c4 == "yes" else ("no" if c3 == c4 == "no" else "part")
for s in SLUGS: final[s]["Directory"] = derive(Cf[s]["C3"], Cf[s]["C4"])
# Cells changed after the readings so that they follow the rulings behind the adjudicated cells (the author's decision, 2026-11-13).
# (slug, service): (value as read, value under the ruling). Source: prior-work/vendors/consistency-check.md Section 2, the five "clear" rows.
RULED = {
 ("openai-dots","Tasks"):("yes","part"), ("claude-code","Policy"):("yes","part"), ("grok-build","Policy"):("yes","part"),
 ("openai-dots","Orchestration"):("yes","part"), ("gemini-spark","Improvement"):("no*","part*"),
 # prior-work/vendors/consistency-check-tenth.md, Section A: the one "clearly does not follow" cell of the tenth column (ruling R14)
 ("claude-managed-agents","Models"):("part*","yes"),
 # Draft 9 (final review, finding 1): the Approvals definition asks the service to obtain AND RECORD decisions on single held actions.
 # Five yes cells whose reader rows and H1 readings state no such record. Source: prior-work/vendors/consistency-check-d9.md
 ("openai-dots","Approvals"):("yes","part"), ("claude-duet","Approvals"):("yes","part"), ("grok-build","Approvals"):("yes","part"),
 ("antigravity","Approvals"):("yes","part"), ("gemini-spark","Approvals"):("yes","part"),
 # Draft 9 (final review, finding 3): two of the seven cells left unclear, which the reviewer judged against rulings 20 and 9
 ("gemini-spark","Environments"):("yes","part"), ("codex","Identity"):("yes","part"),
}
WHY = {
 ("openai-dots","Tasks"):"Retry and recovery of the tracked unit are not described (as decided for Codex CLI).",
 ("claude-code","Policy"):"The only content rule is on files and network addresses (as decided for Codex CLI).",
 ("grok-build","Policy"):"The only content rule is on files and network addresses (as decided for Codex CLI).",
 ("openai-dots","Orchestration"):"Dependencies between tasks are not described (as decided for Grok Bot).",
 ("gemini-spark","Improvement"):"A skill built from chats on request is the feature rated part for Grok Build.",
 ("claude-managed-agents","Models"):"A model set for each agent in its configuration is the feature rated yes for Codex CLI.",
 ("openai-dots","Approvals"):"No record of a decision on a single held action is stated.",
 ("claude-duet","Approvals"):"No record of a decision on a single held action is stated.",
 ("grok-build","Approvals"):"No record of a decision on a single held action is stated.",
 ("antigravity","Approvals"):"No record of a decision on a single held action is stated.",
 ("gemini-spark","Approvals"):"No record of a decision on a single held action is stated.",
 ("gemini-spark","Environments"):"Isolation of an agent from others is not stated (as decided for Dots and Claude Managed Agents).",
 ("codex","Identity"):"Subagents have no identity of their own (the reading by agent decided for Dots).",
}
assert set(WHY) == set(RULED) and len(RULED) == 13
as_read = {s: dict(final[s]) for s in SLUGS}
flag_s = {(s, k) for s in SLUGS for k in SERVICES if k != "Directory" and first[s][k].endswith("*")}
flag_c = {(s, c) for s in SLUGS for c in ("C1","C2","C3","C4") if C[s][c].endswith("*")}
for (s, k), (a, b, adj) in ADJ.items():
    if a.endswith("*") or b.endswith("*"): (flag_c if k in ("C1","C2","C3","C4") else flag_s).add((s, k))
# A cell both readers rated alike is disputable if either reader marked it so (draft 7; draft 6 kept only the first reader's mark).
second_only = []
for s in SLUGS:
    t2 = table(V/"second-reader"/"out"/f"{s}.md"); c2 = crit(V/"second-reader"/"out"/f"{s}.md")
    for k in list(sample[s]) + ["C1","C2","C3","C4"]:
        if (s, k) in ADJ: continue
        tgt = Cf[s] if k in ("C1","C2","C3","C4") else final[s]
        b2 = c2.get(k, "?") if k in ("C1","C2","C3","C4") else base(t2.get(k, ""))
        assert b2.rstrip("*") == tgt[k].rstrip("*"), (s, k, tgt[k], b2)   # agreed cells only; differences are all in ADJ
        if b2.endswith("*"): (flag_c if k in ("C1","C2","C3","C4") else flag_s).add((s, k))
        if b2.endswith("*") and not tgt[k].endswith("*"): tgt[k] += "*"; second_only.append((s, k))
for (s, k), (a, b) in RULED.items():
    assert (s, k) not in ADJ and final[s][k] == a, (s, k, final[s][k], a)   # must start from the value as read (after the second-reader pass)
    final[s][k] = b.rstrip("*")   # draft 9: a changed cell carries the section sign and no asterisk; Table 7a gives its value as read
def mark(s, k):
    if (s, k) in RULED: return "&sect;"
    if (s, k) in ADJ: return "&Dagger;"
    if k in ("C1","C2","C3","C4") or k in sample[s]: return "&dagger;"
    return ""
def td(val, s, k):
    b = val.rstrip("*"); cls = {"yes":"y","part":"p","no":"n"}[b]
    return f'<td class="{cls}">{b}{"*" if val.endswith("*") else ""}{mark(s, k)}</td>'
GROUP = {"Harness":"Runtime","Memory":"Knowledge","Models":"Capabilities","Directory":"Interaction","Identity":"Governance","Observability":"Operations"}
rows = ['<div class="tw"><table class="wide"><tr><th>Service</th>' + "".join(f"<th>{n}</th>" for n in NAMES) + '<th class="num">yes</th><th class="num">part</th><th class="num">no</th></tr>']
per_service = {}
for k in SERVICES:
    vals = [final[s][k].rstrip("*") for s in SLUGS]; per_service[k] = [vals.count(x) for x in ("yes","part","no")]
    if k in GROUP: rows.append(f'<tr><td colspan="14" class="grp"><strong>{GROUP[k]}</strong></td></tr>')
    rows.append(f"<tr><td>{k}</td>" + "".join(td(final[s][k], s, k) for s in SLUGS) + "".join(f'<td class="num">{n}</td>' for n in per_service[k]) + "</tr>")
per_product = {s: [sum(final[s][k].rstrip("*") == x for k in SERVICES) for x in ("yes","part","no")] for s in SLUGS}
for i, lab in enumerate(("yes","part","no")):
    rows.append(f"<tr><td><strong>{lab}</strong></td>" + "".join(f'<td class="num">{per_product[s][i]}</td>' for s in SLUGS) + '<td></td><td></td><td></td></tr>')
rows.append("</table></div>")
Path("src/tab-vendors.html").write_text("\n".join(rows) + "\n")
CN = {"C1":"C1. An area of work exists","C2":"C2. The area is specified apart from who does the work","C3":"C3. A record of accountability","C4":"C4. Finding where to send work"}
rc = ['<div class="tw"><table class="wide"><tr><th>Criterion</th>' + "".join(f"<th>{n}</th>" for n in NAMES) + "</tr>"]
for c in ("C1","C2","C3","C4"): rc.append(f"<tr><td>{CN[c]}</td>" + "".join(td(Cf[s][c], s, c) for s in SLUGS) + "</tr>")
rc.append("</table></div>"); Path("src/tab-vendors-c.html").write_text("\n".join(rc) + "\n")
NM = dict(zip(SLUGS, [n.replace("&shy;", "") for n in NAMES]))
rr = ['<div class="tw"><table><tr><th>Product</th><th>Service</th><th>As read</th><th>Shown</th><th>Readers</th><th>Reason</th></tr>']
for (s, k), (a, b) in RULED.items():
    rr.append(f"<tr><td>{NM[s]}</td><td>{k}</td><td>{a}</td><td>{b.rstrip('*')}</td><td>{'two' if k in sample[s] else 'one'}</td><td>{WHY[(s, k)]}</td></tr>")
rr.append("</table></div>"); Path("src/tab-ruled.html").write_text("\n".join(rr) + "\n")
dis = sum(v.endswith("*") for s in SLUGS for k, v in final[s].items()) 
tot = {
 "per_product": dict(zip(SLUGS, [per_product[s] for s in SLUGS])), "per_service": per_service,
 "all_yes": [k for k in SERVICES if per_service[k][0] == len(SLUGS)], "zero_yes": [k for k in SERVICES if per_service[k][0] == 0],
 "one_yes": {k: [s for s in SLUGS if final[s][k].rstrip('*') == "yes"] for k in SERVICES if per_service[k][0] == 1},
 "harness_yes": [per_product[s][0] for s in HARNESS], "personal_yes": [per_product[s][0] for s in PERSONAL], "platform_yes": [per_product[s][0] for s in PLATFORM],
 "C": {c: {x: [s for s in SLUGS if Cf[s][c].rstrip('*') == x] for x in ("yes","part","no")} for c in ("C1","C2","C3","C4")},
 "second_reader_only_disputable": second_only,
 "ruled": {f"{s}/{k}": list(v) for (s, k), v in RULED.items()},
 "as_read_totals": [sum(as_read[s][k].rstrip("*") == x for s in SLUGS for k in SERVICES) for x in ("yes","part","no")],
 "as_read_per_product": {s: [sum(as_read[s][k].rstrip("*") == x for k in SERVICES) for x in ("yes","part","no")] for s in SLUGS},
 "reader_flagged_service_cells": len(flag_s), "reader_flagged_C_cells": len(flag_c),
 "ruled_two_readers": [f"{s}/{k}" for (s, k) in RULED if k in sample[s]],
 "disputable_service_cells": dis, "disputable_C_cells": sum(v.endswith("*") for s in SLUGS for v in Cf[s].values()),
 "cells": 25 * len(SLUGS), "products": len(SLUGS), "second_read_service_cells": sum(len(sample[s]) for s in SLUGS) + 1, "sampled_service_cells": sum(len(sample[s]) for s in SLUGS), "second_read_C_cells": 4 * len(SLUGS),
 "marks": {"section": len(RULED), "dagger": sum(1 for s in SLUGS for k in list(sample[s]) if (s, k) not in ADJ and (s, k) not in RULED), "double_dagger_services": sum(1 for (s, k) in ADJ if not k.startswith("C") or k == "Channels"), "dagger_C": sum(1 for s in SLUGS for k in ("C1","C2","C3","C4") if (s, k) not in ADJ), "double_dagger_C": sum(1 for (s, k) in ADJ if k in ("C1","C2","C3","C4"))},
 "disputable_nonderived_of": 24 * len(SLUGS), "no_total": sum(per_product[s][2] for s in SLUGS), "yes_total": sum(per_product[s][0] for s in SLUGS), "part_total": sum(per_product[s][1] for s in SLUGS),
 "first_reader_per_product": {s: [sum((("part" if (s=="claude-code" and k=="Directory") else first[s][k].rstrip("*")) == x) for k in SERVICES) for x in ("yes","part","no")] for s in SLUGS},
}
Path("build/vendor-totals.json").write_text(json.dumps(tot, indent=1))
print(json.dumps(tot))
