#!/usr/bin/env python3
"""Recompute the counts in the paper's tables and figures from the files in this folder.
Usage (from this folder):  python3 recompute.py
Python 3.9 or later, standard library only. Exit status 0 means that every check passed.

What it does:
 1. runs the two generators that built the paper's tables (paper/build/gen.py, gen_vendors.py) on the files here
    and checks that each generated table or figure is, character for character, the one in the draft;
 2. counts again, without the generators, the numbers that the generators carry as constants:
    Table A2 and Figure 3 from the four assignment tables, the reference implementation's row of Figure 4 and
    Table 6 from its list of services, Table A1 from the search record, and the rows of Table 5 that are not
    read from rerate-four-columns.md from the two files that hold them."""
import json, re, runpy, subprocess, sys, collections, html, contextlib, io, os
sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
from pathlib import Path
H = Path(__file__).resolve().parent
PAPER = H / 'paper' / 'warm-paper-d10.html'
paper = PAPER.read_text()
fails = []
def check(name, ok, detail=''):
    print(('PASS  ' if ok else 'FAIL  ') + name + (('  ' + detail) if detail else ''))
    if not ok: fails.append(name)
def md_rows(path, start=None, stop=None):
    """Rows of the markdown tables of a file, as lists of cells, between two heading prefixes."""
    on = start is None; out = []
    for ln in (H / path).read_text().split('\n'):
        if start and ln.startswith(start): on = True; continue
        if on and stop and ln.startswith(stop): break
        if on and ln.startswith('|') and not re.match(r'\|\s*-', ln): out.append([c.strip() for c in ln.strip().strip('|').split('|')])
    return out
def paper_table(caption):
    """Rows of the HTML table that stands just above a caption in the draft, as lists of plain-text cells."""
    i = paper.index(caption); a = paper.rindex('<table', 0, i); b = paper.index('</table>', a)
    rows = re.findall(r'<tr>(.*?)</tr>', paper[a:b], re.S)
    return [[html.unescape(re.sub(r'<[^>]+>', '', c)).strip() for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S)] for r in rows]
num = lambda s: int(s.replace(',', ''))

# ---- 1. the generators
(H / 'paper' / 'src').mkdir(exist_ok=True)
os.chdir(H / 'paper')
buf = io.StringIO()
with contextlib.redirect_stdout(buf): G = runpy.run_path('build/gen.py')
gen_out = buf.getvalue()
v = subprocess.run([sys.executable, 'build/gen_vendors.py'], capture_output=True, text=True)
check('generators ran', v.returncode == 0, v.stderr.strip()[-200:])
for label, f in (('Figure 3', 'fig-fit.svg'), ('Figure 4', 'fig-grid.svg'), ('Table 5', 'tab-groups.html'), ('Table 7', 'tab-vendors.html'), ('Table 8', 'tab-vendors-c.html'), ('Table 7a', 'tab-ruled.html')):
    check(f'{label}: the generated {f} is in the draft unchanged', (H / 'paper' / 'src' / f).read_text() in paper)
T = json.loads((H / 'paper' / 'build' / 'vendor-totals.json').read_text())
print('\nTable 7 (ten products by 25 services, %d cells)' % T['cells'])
print('  shown:   yes %d, part %d, no %d' % (T['yes_total'], T['part_total'], T['no_total']))
print('  as read: yes %d, part %d, no %d' % tuple(T['as_read_totals']))
print('  yes per product:', {k: x[0] for k, x in T['per_product'].items()})
print('  harnesses %s, personal agents %s, platform %s' % (T['harness_yes'], T['personal_yes'], T['platform_yes']))
print('  services with a yes from every product:', T['all_yes'])
print('  services with no yes:', T['zero_yes'])
print('  Approvals yes in', T['per_service']['Approvals'][0], 'of', T['products'])
print('  marks: dagger %d, double dagger %d, section sign %d; criteria dagger %d, double dagger %d' % (T['marks']['dagger'], T['marks']['double_dagger_services'], T['marks']['section'], T['marks']['dagger_C'], T['marks']['double_dagger_C']))
print('  asterisks kept: %d service cells, %d criterion cells; marked disputable by a reader: %d of %d and %d of %d' % (T['disputable_service_cells'], T['disputable_C_cells'], T['reader_flagged_service_cells'], T['disputable_nonderived_of'], T['reader_flagged_C_cells'], T['second_read_C_cells']))
print('Table 8:', {c: {x: len(s) for x, s in d.items()} for c, d in T['C'].items()})
print('Table 5, from gen.py:'); print('  ' + '\n  '.join(l for l in gen_out.split('\n') if l.startswith(('seventeen', 'all', 'eight'))))
t7 = paper_table('Table 7. Ten vendor products')
tot = [sum(int(r[-3 + k]) for r in t7 if len(r) == 14 and r[-1].isdigit()) for k in range(3)]
check('Table 7: the yes, part and no columns of the draft sum to the generator totals', tot == [T['yes_total'], T['part_total'], T['no_total']], str(tot))
check('Table 7a: thirteen changed cells', len(paper_table('Table 7a.')) - 1 == len(T['ruled']) == 13)

# ---- 2. Table A2 and Figure 3, counted from the assignment tables
print('\nTable A2 and Figure 3 (inventory entries by assignment)')
ORDER = ['service', 'layer', 'builder', 'span', 'misfit']
def klass(s):
    s = s.lower()
    for key, k in (('(a)', 'service'), ('(b)', 'layer'), ('(c)', 'builder'), ('(d)', 'span'), ('(e)', 'misfit')):
        if s.startswith(key): return k
    if s.startswith('builder'): return 'builder'
    if s.startswith('span'): return 'span'
    if s.startswith('misfit'): return 'misfit'
    if '(layer)' in s or s.startswith(('providers', 'domains', 'infrastructure', 'people')): return 'layer'
    return 'service'
def count(rows): c = collections.Counter(rows); return [c[k] for k in ORDER]
ac = count(klass(r[2]) for r in md_rows('platform-mapping/mapping-agentcore.md', '## Full assignment table', '## The 22 services') if re.match(r'C\d+$', r[0]))
lg = count(klass(r[2]) for r in md_rows('platform-mapping/mapping-langgraph.md', '## Full assignment table', '## The 22 services') if re.match(r'\d+$', r[0]))
oc = collections.Counter()
for r in md_rows('platform-mapping/mapping-openclaw.md', '### 1.1 Individual rows', '### 1.2 Class rows'):
    if len(r) == 4 and r[0] != 'Component': oc[klass(r[1])] += 1
for r in md_rows('platform-mapping/mapping-openclaw.md', '### 1.2 Class rows', '## 2.'):
    if len(r) == 6 and r[2].isdigit(): oc[klass(r[3])] += int(r[2])
oc = [oc[k] for k in ORDER]
lo = collections.Counter(l.split('\t')[2] for l in (H / 'platform-mapping' / 'lifeos-assignments.tsv').read_text().split('\n')[1:] if l)
lo = [lo[k] for k in ('one service', 'other layer', 'builder tooling', 'span', 'misfit')]
recount = {'AgentCore': ac, 'LangGraph': lg, 'OpenClaw': oc, 'LifeOS': lo}
a2 = {r[0]: [num(x) for x in r[1:7]] for r in paper_table('Table A2. Inventory entries') if len(r) == 8 and r[1].replace(',', '').isdigit()}
fig3 = {name: (n, v) for name, n, v in G['data']}
for name, c in recount.items():
    row = next(vv for k, vv in a2.items() if name in k); f3 = next(vv for k, vv in fig3.items() if name in k)
    print('  %-26s %4d components: %s' % (name, sum(c), c))
    check(f'Table A2, {name}: the assignment table gives the draft\'s row', [sum(c)] + c == row, 'draft ' + str(row))
    check(f'Figure 3, {name}: the generator draws the same numbers', (sum(c), c) == f3)
    share = round(100 * (c[0] + c[1]) / sum(c)); drow = next(r for r in paper_table('Table A2. Inventory entries') if name in r[0])
    check(f'Table A2, {name}: single category {share}%', drow[7] == f'{share}%', 'draft ' + drow[7])

# ---- 3. the reference implementation: the first row of Figure 4, and Table 6
sv = [l.split('\t') for l in (H / 'platform-mapping' / 'lifeos-services.tsv').read_text().split('\n')[1:] if l]
status = [{'present': 'yes', 'partial': 'part', 'absent': 'no'}[s[2]] for s in sv]
check('Figure 4, first row: the 25 service cells equal the list of services (%d present, %d partial)' % (status.count('yes'), status.count('part')), status == G['life'][:25])
partial = [s[1] for s in sv if s[2] == 'partial']
t6 = [r[0].replace(' (disputed)', '') for r in paper_table('Table 6. The services that the mapper judged partial') if len(r) == 2 and r[0] != 'Service']
check('Table 6: its rows are the %d services rated partial' % len(partial), sorted(t6) == sorted(partial), str(sorted(set(t6) ^ set(partial))))

# ---- 3b. Table 2 and Table A3, from the model's list of services
mt = [r for r in md_rows('model/warm-model-v0.14.md') if len(r) == 4 and r[1].startswith('**')][:25]
model = {r[1].strip('*'): (r[0], r[2], r[3]) for r in mt}
flat = lambda s: re.sub(r'\W+', ' ', html.unescape(s)).strip().lower()
t2 = [r for r in paper_table('Table 2. The 25 platform services') if len(r) == 3 and r[0] != 'Group']
a3 = [r for r in paper_table('Table A3. Industry terms') if len(r) == 2 and r[0] != 'Service']
check('Table 2: the 25 services and their groups are those of the model, version 0.14', len(t2) == 25 and [s[1] for s in sv] == [r[1] for r in t2] and all(model[s][0] == g for g, s, resp in t2))
check('Table A3: one row for each of the 25 services', [r[0] for r in a3] == [r[1] for r in t2])
diff = [f'Table 2, {s}: draft "{resp}" / model "{model[s][1]}"' for g, s, resp in t2 if flat(model[s][1]) != flat(resp)]
diff += [f'Table A3, {s}: draft "{terms}" / model "{model[s][2]}"' for s, terms in a3 if flat(model[s][2]) != flat(terms)]
for d in diff: print('NOTE  wording differs. ' + d)
check('Tables 2 and A3: the wording equals the model file except in the %d rows noted' % len(diff), len(diff) <= 2)

# ---- 4. Table A1, from the search record
flow = {r[0]: r[-1] for r in md_rows('prior-work/search.md', '## 9. Flow count', '## 10.') if len(r) == 6}
a1 = {r[0]: num(r[1]) for r in paper_table('Table A1. The documented search') if len(r) == 2 and r[1].replace(',', '').isdigit()}
pairs = (('Screened, within the page caps', 'Records screened (within the caps)'), ('After removing duplicates (approximate)', 'After de-duplication across all databases'), ('Passed title screening', 'Passed title screening'),
         ('Met the inclusion rule (a general model of an agent system)', 'Included'), ('Already known from the earlier reading', 'of which already known'), ('New', 'of which new'))
check('Table A1: six stages equal the flow count of the search record', all(a1[a] == num(flow[b]) for a, b in pairs), str([a1[a] for a, b in pairs]))
mapped = sum(1 for f in ('mapping-round2-charters.md', 'mapping-round2-platforms.md') for l in (H / 'prior-work' / f).read_text().split('\n') if re.match(r'## (?:Source )?[A-D]\. ', l))
check('Table A1: new sources mapped (sections A to D of the two second-round mapping files)', a1['New sources mapped to WARM'] == mapped, f'draft {a1["New sources mapped to WARM"]}, files {mapped}')

# ---- 5. Table 5: the rows that gen.py holds as constants
print('\nTable 5, rows not read from rerate-four-columns.md')
def val(s):
    m = re.match(r'\**(yes|part|no)\**(?:[ ,(]*(?:DISPUTABLE|D:?)[ (]*(yes|part|no))?', s.strip()); return (m.group(1), m.group(2))
RANK = {'no': 0, 'part': 1, 'yes': 2}
def gv(s): m = re.match(r'(yes|part|no)(?: D: (yes|part|no))?', s); return (m.group(1), m.group(2))
om = {}; cur = None
for ln in (H / 'prior-work' / 'organizational-mas.md').read_text().split('\n'):
    m = re.match(r'#{2,3} (?:[A-H]\.|Addition \d\.) (.*)', ln)
    if m: cur = m.group(1); om[cur] = []
    m = re.match(r'\| C([1-4]) \| ([^|]+)\|', ln)
    if m and cur and len(om[cur]) < 4: om[cur].append(val(m.group(2)))
KEY = {'AGR': 'AGR', 'Gaia': 'Gaia', 'MOISE+': 'MOISE', 'Microsoft adoption guidance': 'Microsoft Cloud Adoption', 'Beyond the Agent Harness': 'Beyond the Agent Harness', 'WorkMate': 'WorkMate', 'Kandogan': 'Kandogan', 'EDDOps': 'EDDOps'}
for r in G['extra']:
    if r[0].endswith('†'): continue
    k = next(v for n, v in KEY.items() if r[0].startswith(n)); src = next(v for n, v in om.items() if k in n)
    check(f'Table 5, {r[0]}: four cells equal organizational-mas.md', [gv(x) for x in r[1:]] == src, str(src))
cmp_rows = {r[0]: r[1:] for r in md_rows('prior-work/rerate-v2-comparison.md') if len(r) == 9 and r[0] != 'Source'}
two = {'AAM/5C': G['rr2'][3], 'Microsoft reference architecture': G['rr2'][4], 'ASOC': G['rr2'][13]}
two.update({'OperA': G['V2X']['OperA (2004)'], 'Horling and Lesser': G['V2X']['Horling and Lesser (2004)']})
two.update({'FIPA SC00023K': G['infra'][0][1:], 'ISLANDER and AMELI': G['infra'][1][1:], 'JaCaMo': G['infra'][2][1:]})
for name, cells in two.items():
    ok = True; shown = []
    for c in range(4):
        a, b = val(cmp_rows[name][2*c]), val(cmp_rows[name][2*c+1]); lowv = min(a[0], b[0], key=RANK.get); g = gv(cells[c]); shown.append(g[0])
        ok = ok and g[0] == lowv
        if a[0] != b[0]: ok = ok and g[1] == max(a[0], b[0], key=RANK.get)
    check(f'Table 5, {name} (two readers): each cell is the lower of the two readers\' values', ok, ' '.join(shown))

print('\n%d checks failed' % len(fails) if fails else '\nAll checks passed.')
sys.exit(1 if fails else 0)
