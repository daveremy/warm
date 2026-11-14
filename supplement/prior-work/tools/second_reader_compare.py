"""Print first-reader and second-reader values side by side for the sampled services.
Usage: python second_reader_compare.py <vendors-dir> <slug>..."""
import re, sys
from pathlib import Path
SERVICES = ["Harness","Sessions","Tasks","Environments","Scheduling","Lifecycle","Memory","Retrieval","Artifacts","Models","Tools","Registry","Directory","Messaging","Orchestration","Channels","Identity","Secrets","Policy","Approvals","Observability","Evaluation","Improvement","Releases","Reliability"]
def table(path):
    out = {}
    for line in path.read_text().splitlines():
        if not line.startswith("|"): continue
        cells = [c.strip().strip("*").strip() for c in line.strip().strip("|").split("|")]
        for i, c in enumerate(cells[:-1]):
            if c in SERVICES:  # first service name in the row only: later cells may name a page called "Tasks"
                out.setdefault(c, re.sub(r"\s+", " ", cells[i + 1].replace("*", ""))[:60])
                break
    return out
def crit(path):
    return [re.sub(r"\s+", " ", l)[:230] for l in path.read_text().splitlines() if re.search(r"\bC[1-4]\b", l) and re.search(r"\b(yes|part|no)\b", l, re.I)][:10]
v = Path(sys.argv[1])
for slug in sys.argv[2:]:
    a, b = table(v / f"{slug}.md"), table(v / "second-reader" / "out" / f"{slug}.md")
    print(f"\n## {slug}")
    for s in SERVICES:
        if s in b: print(f"{s:14} first: {a.get(s,'?'):45} second: {b[s]}")
    print("-- first C lines");  [print("  ", l) for l in crit(v / f"{slug}.md")]
    print("-- second C lines"); [print("  ", l) for l in crit(v / "second-reader" / "out" / f"{slug}.md")]
