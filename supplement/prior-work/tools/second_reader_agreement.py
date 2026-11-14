"""Agreement between first and second readers on the sampled services and C1 to C4 (base values).
Usage: python second_reader_agreement.py <vendors-dir>"""
import re, sys
from pathlib import Path
from second_reader_compare import SERVICES, table
from vendor_table import SLUGS, base
VAL = re.compile(r"\b(not assessed|yes|part|no)\b", re.I)
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
v = Path(sys.argv[1]); tot = {"svc": [0, 0], "crit": [0, 0]}; dis = []
for s in SLUGS:
    a, b = table(v / f"{s}.md"), table(v / "second-reader" / "out" / f"{s}.md")
    ca, cb = crit(v / f"{s}.md"), crit(v / "second-reader" / "out" / f"{s}.md")
    if s == "claude-code": a["Directory"] = "part"
    cells = [(k, base(a.get(k, "")), base(b[k])) for k in SERVICES if k in b and k != "Directory"]
    cc = [(k, ca.get(k, "?"), cb.get(k, "?")) for k in ("C1", "C2", "C3", "C4")]
    ok = sum(x.rstrip("*") == y.rstrip("*") for _, x, y in cells); okc = sum(x.rstrip("*") == y.rstrip("*") for _, x, y in cc)
    tot["svc"][0] += ok; tot["svc"][1] += len(cells); tot["crit"][0] += okc; tot["crit"][1] += len(cc)
    dis += [(s, k, x, y) for k, x, y in cells + cc if x.rstrip("*") != y.rstrip("*")]
    print(f"{s:13} services {ok}/{len(cells)}  C {okc}/4   " + " ".join(f"{k}:{x}/{y}" for k, x, y in cc))
print("TOTAL services", tot["svc"], "criteria", tot["crit"])
for d in dis: print("DIFF", *d)
