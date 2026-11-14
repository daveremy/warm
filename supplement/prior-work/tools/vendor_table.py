"""Print the 25-by-9 vendor table (base value per cell, * = DISPUTABLE) and per-product counts.
Usage: python vendor_table.py <vendors-dir>"""
import re, sys
from pathlib import Path
from second_reader_compare import SERVICES, table
SLUGS = ["claude-code","codex","grok-build","antigravity","claude-duet","openai-dots","grok-bot","gemini-spark","meta-muse"]
def base(cell):
    m = re.match(r"\s*(not assessed|yes|part|no)\b", cell, re.I)
    return (m.group(1).lower() if m else "?") + ("*" if "DISPUTABLE" in cell.upper() else "")
def main():
    v = Path(sys.argv[1])
    tabs = {s: table(v / f"{s}.md") for s in SLUGS}
    tabs["claude-code"]["Directory"] = "part (derived by sagan from C3 part, C4 part; the reader rated no from the definition)"
    print("| Service | " + " | ".join(SLUGS) + " | yes | part | no |"); print("|---" * (len(SLUGS) + 4) + "|")
    for svc in SERVICES:
        row = [base(tabs[s].get(svc, "")) for s in SLUGS]
        b = [r.rstrip("*") for r in row]
        print(f"| {svc} | " + " | ".join(row) + f" | {b.count('yes')} | {b.count('part')} | {b.count('no')} |")
    for k in ("yes", "part", "no", "?"):
        print(f"| **{k}** | " + " | ".join(str(sum(base(tabs[s].get(x, '')).rstrip('*') == k for x in SERVICES)) for s in SLUGS) + " | | | |")

if __name__ == "__main__":
    main()
