#!/usr/bin/env python3
"""Generate the paper's grid figure, fit figure and Table 6 from the working notes.
Sources: ../prior-work/source-by-part-grid.md (Grid A), ../prior-work/directory-column-rule.md
(Dir and DirC re-derived under one rule), ../platform-mapping/mapping-lifeos.md sections 2-5 (LifeOS row)."""
import re, json, pathlib
W = pathlib.Path(__file__).resolve().parents[2]
OUT = pathlib.Path(__file__).resolve().parents[1] / 'src'
grid = (W/'prior-work/source-by-part-grid.md').read_text().splitlines()
rows = {}
cols = None
for ln in grid:
    if ln.startswith('| # | Source | Har'):
        cols = [c.strip() for c in ln.strip('|').split('|')][2:]
    m = re.match(r'\| (\d+) \| ([^|]+) \|(.*)\|\s*$', ln)
    if m and cols and len(m.group(3).split('|')) == 32:
        rows[int(m.group(1))] = (m.group(2).strip(), [c.strip() for c in m.group(3).split('|')])
assert len(rows) == 17 and len(cols) == 32, (len(rows), cols)
ci = {c: i for i, c in enumerate(cols)}
# one rule for the Directory columns (directory-column-rule.md, sections 2 and 3)
for r in (1, 3, 4, 10, 13, 15, 16, 17):
    assert rows[r][1][ci['Dir']] == 'no'; rows[r][1][ci['Dir']] = 'part'
for r in (4, 5, 11):
    assert rows[r][1][ci['DirC']] == 'no'; rows[r][1][ci['DirC']] = 'part'
# ---- independent re-rating on four frozen criteria (prior-work/rerate-four-columns.md)
rr = {}
for ln in (W/'prior-work/rerate-four-columns.md').read_text().splitlines():
    m = re.match(r'\| (\d+) \| ([^|]+) \|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|\s*$', ln)
    if m: rr[int(m.group(1))] = [c.strip() for c in m.groups()[2:]]
assert len(rr) == 17, len(rr)
for i in rr:
    d = rr[i][4].split()[0]; assert d in ('yes','part','no'), d
    rows[i][1][ci['Dir']] = d
present = 'Har Ses Sch Mem Ret Mod Too Reg Msg Obs Eva Imp Rel Rlb'.split()
life = ['yes' if c in present else 'part' for c in cols[:25]] + ['yes', 'part', 'part', 'yes', 'yes', 'n.a.', 'part']
short = {1:'Yu et al.',2:'Zhu',3:'AAM/5C (Goujon)',4:'Microsoft MARA',5:'AWS guidance',6:'Google Cloud',7:'Charterion',8:'AEON',9:'CEAD',10:'Salesforce',11:'AOS',12:'Steinder and Franke',13:'ASOC',14:'EAAF',15:'Bedrock AgentCore',16:'LangGraph, LangSmith',17:'OpenClaw'}
order = [('LifeOS', life)] + [(short[i], rows[i][1]) for i in (15,16,17)] + [(short[i], rows[i][1]) for i in range(1,15)]
# totals over the 17 sources
tot = {c: {'yes':0,'part':0,'no':0,'n.a.':0} for c in cols}
for i in rows:
    for c, v in zip(cols, rows[i][1]): tot[c][v] += 1
allc = {k: sum(tot[c][k] for c in cols) for k in ('yes','part','no','n.a.')}
json.dump({'cols': cols, 'tot': tot, 'all': allc}, open(OUT.parent/'build/totals.json','w'), indent=1)
groups = [('Runtime',6),('Knowledge',3),('Capabilities',3),('Interaction',4),('Governance',4),('Operations',5),('Agents and decisions',4)]
DROP = ('Dom','Cht','DirC')
keep = [i for i,c in enumerate(cols) if c not in DROP]
fcols = [cols[i] for i in keep]
order = [(n,[v[i] for i in keep]) for n,v in order]
full = {'Har':'Harness','Ses':'Sessions','Tsk':'Tasks','Env':'Environments','Sch':'Scheduling','Lif':'Lifecycle','Mem':'Memory','Ret':'Retrieval','Art':'Artifacts','Mod':'Models','Too':'Tools','Reg':'Registry','Dir':'Directory','Msg':'Messaging','Orc':'Orchestration','Chn':'Channels','Idn':'Identity','Sec':'Secrets','Pol':'Policy','App':'Approvals','Obs':'Observability','Eva':'Evaluation','Imp':'Improvement','Rel':'Releases','Rlb':'Reliability','Dom':'Domains layer','Cht':'Charter','DirC':'Accountability record','Pers':'Persistent agents','TaskA':'Task agents','AgId':'Agent identity','PreA':'Pre-approval'}
# ---- grid figure
X0, Y0, CW, CH = 150, 132, 17, 17
gap = 15
xs = []; x = X0
gi = 0; n = 0
gx = []
for g, k in groups:
    gx.append((g, x, x + k*CW))
    for _ in range(k): xs.append(x); x += CW
    x += gap
Wd = x + 44
bands = [1, 3, 14]
ys = []; y = Y0
for b in bands:
    for _ in range(b): ys.append(y); y += CH
    y += 8
Ht = y + 34
o = [f'<svg viewBox="0 0 {Wd} {Ht}" role="img" aria-label="Grid of 18 systems and models by 29 parts of WARM; each cell is full, partial, absent or not assessed.">']
for g, a, b in gx:
    o.append(f'<line class="ln" x1="{a}" y1="14" x2="{b-2}" y2="14"/><text class="sm hd" x="{a}" y="10">{g}</text>')
for c, xx in zip(fcols, xs):
    o.append(f'<text class="sm" transform="translate({xx+11},{Y0-8}) rotate(-58)">{full[c]}</text>')
labels = ['Reference implementation', 'Platforms', 'Published models']
yi = 0
for b, lab in zip(bands, labels):
    o.append(f'<text class="dim" x="4" y="{ys[yi]-3 if b>1 else ys[yi]-3}">{lab}</text>') if False else None
    yi += b
for (name, cells), yy in zip(order, ys):
    o.append(f'<text class="sm" x="{X0-8}" y="{yy+12}" text-anchor="end">{name}</text>')
    for v, xx in zip(cells, xs):
        s = 12; cx = xx + 2; cy = yy + 2
        if v == 'yes': o.append(f'<rect class="cy" x="{cx}" y="{cy}" width="{s}" height="{s}" rx="2"/>')
        elif v == 'part': o.append(f'<rect class="cn" x="{cx}" y="{cy}" width="{s}" height="{s}" rx="2"/><rect class="cp" x="{cx}" y="{cy}" width="{s/2}" height="{s}"/>')
        elif v == 'no': o.append(f'<rect class="cn" x="{cx}" y="{cy}" width="{s}" height="{s}" rx="2"/>')
        else: o.append(f'<circle class="arrow" cx="{cx+s/2}" cy="{cy+s/2}" r="1.6"/>')
ly = Ht - 14; lx = X0
for v, lab in (('yes','counterpart in full'),('part','in part'),('no','absent'),('n.a.','not assessed')):
    s = 12
    if v == 'yes': o.append(f'<rect class="cy" x="{lx}" y="{ly-10}" width="{s}" height="{s}" rx="2"/>')
    elif v == 'part': o.append(f'<rect class="cn" x="{lx}" y="{ly-10}" width="{s}" height="{s}" rx="2"/><rect class="cp" x="{lx}" y="{ly-10}" width="{s/2}" height="{s}"/>')
    elif v == 'no': o.append(f'<rect class="cn" x="{lx}" y="{ly-10}" width="{s}" height="{s}" rx="2"/>')
    else: o.append(f'<circle class="arrow" cx="{lx+6}" cy="{ly-4}" r="1.6"/>')
    o.append(f'<text class="sm" x="{lx+18}" y="{ly}">{lab}</text>'); lx += 40 + 7*len(lab)
o.append('</svg>')
(OUT/'fig-grid.svg').write_text('\n'.join(x for x in o if x))
# ---- fit figure
data = [('Bedrock AgentCore', 146, [92,5,10,28,11]), ('LangGraph, LangSmith', 307, [183,22,55,30,17]), ('OpenClaw', 848, [329,212,256,38,13]), ('LifeOS (reference implementation)', 849, [400,288,93,61,7])]
cats = ['One service','Another layer','Builder tooling','Span of services','Misfit']
BW = 470; BX = 214
o = ['<svg viewBox="0 0 720 236" role="img" aria-label="Stacked bars: share of components by assignment category for four systems.">']
for i, (name, n, v) in enumerate(data):
    assert sum(v) == n
    yy = 22 + i*40
    o.append(f'<text x="{BX-10}" y="{yy+14}" text-anchor="end">{name}</text><text class="dim" x="{BX-10}" y="{yy+28}" text-anchor="end">n = {n:,}</text>')
    xx = BX
    for j, k in enumerate(v):
        w = BW * k / n
        o.append(f'<rect class="b{j+1}" x="{xx:.1f}" y="{yy}" width="{max(w-1,0.5):.1f}" height="22"/>')
        if w > 26: o.append(f'<text class="sm" x="{xx+w/2:.1f}" y="{yy+36}" text-anchor="middle">{100*k/n:.0f}%</text>')
        xx += w
lx = 96
for j, c in enumerate(cats):
    o.append(f'<rect class="b{j+1}" x="{lx}" y="196" width="12" height="12"/><text class="sm" x="{lx+17}" y="206">{c}</text>'); lx += 34 + 6.6*len(c)
o.append('</svg>')
(OUT/'fig-fit.svg').write_text('\n'.join(o))
# ---- Table 9: four frozen criteria, independent rating (17 sources) and the ten sources read afterward
def cc(v):
    v = v.strip(); m = re.match(r'(yes|part|no)(?: \(?D:? ?\(?(yes|part|no)\)?\)?)?', v.replace('D(', 'D: ').replace('))', ')'))
    base = m.group(1); alt = m.group(2)
    cls = {'yes':'y','part':'p','no':'n'}[base]
    return f'<td class="{cls}">{base}' + (f' <span class="alt">({alt}?)</span>' if alt else '') + '</td>'
extra = [('AGR (2004)','yes','part D: yes','no','no'),('Gaia (2003)','yes','yes','no D: part','no'),('MOISE+ (2002)','yes','part D: yes','part','no'),('OperA (2004)','yes','yes','part','part D: yes'),('Horling and Lesser (2004)','yes','part D: yes','part','yes'),("Microsoft adoption guidance",'part','part','part','part'),('Beyond the Agent Harness (2026)','part','part','no','no'),('WorkMate (2026)','part','part','part','part'),('Kandogan et al. (2025)','no','no','no D: part','yes'),('EDDOps (2025)','no','no','no','no')]
# ---- draft 5: eight sources re-rated by two readers under rerate-criteria-v2.md (prior-work/rerate-v2-comparison.md).
# Where the readers differ the lower value is kept and the higher is the alternative.
V2X = {'OperA (2004)': ('part','part D: yes','part','part'), 'Horling and Lesser (2004)': ('part D: yes','part','part','yes')}
extra = [((r[0] + ' \u2020',) + V2X[r[0]]) if r[0] in V2X else r for r in extra]
V2R = {3: ('part D: yes','part D: yes','part D: yes','part'), 4: ('part','no D: part','part','part D: yes'), 13: ('no D: part','no D: part','part','part')}
rr2 = {i: (list(V2R[i]) if i in V2R else list(rr[i][:4])) for i in rr}
for i in V2R: assert rr[i][4].split()[0] == 'part'   # derived Directory unchanged, so the grid figure is unchanged
dag = {i: (' \u2020' if i in V2R else '') for i in rr}
infra = [('FIPA agent management (2004) \u2020','no D: part','no','part','yes'), ('ISLANDER and AMELI (2002, 2004) \u2020','part','part','part','part'), ('JaCaMo (2013) \u2020','yes','part D: yes','part','part D: yes')]
def bv(v):
    m = re.match(r'(yes|part|no)(?: D: (yes|part|no))?', v.strip().replace('(D: ', 'D: ').replace('D(', 'D: ').replace(')', '')); return m.group(1), m.group(2)
def stats(name, rowsets):
    out = {}
    for c in range(4):
        vals = [bv(r[c]) for r in rowsets]
        out['C%d' % (c+1)] = dict(yes=sum(b=='yes' for b,a in vals), part=sum(b=='part' for b,a in vals), no=sum(b=='no' for b,a in vals), disp=sum(a is not None for b,a in vals), alt_yes=sum(a=='yes' for b,a in vals))
    print(name, len(rowsets), json.dumps(out))
stats('seventeen', [rr2[i] for i in rr2])
stats('all', [rr2[i] for i in rr2] + [r[1:] for r in extra] + [r[1:] for r in infra])
stats('eight', [rr2[i] for i in V2R] + [r[1:] for r in extra if r[0].endswith('\u2020')] + [r[1:] for r in infra])
t = ['<div class="tw"><table class="wide"><tr><th>Source</th><th>C1. An area of work exists</th><th>C2. The area is specified apart from who does the work</th><th>C3. A record of accountability</th><th>C4. Finding where to send work</th></tr>']
t.append('<tr><td colspan="5"><strong>Platforms</strong></td></tr>')
for i in (15,16,17): t.append(f'<tr><td>{short[i]}{dag[i]}</td>' + ''.join(cc(v) for v in rr2[i]) + '</tr>')
t.append('<tr><td colspan="5"><strong>Published models of LLM-agent systems</strong></td></tr>')
for i in range(1,15): t.append(f'<tr><td>{short[i]}{dag[i]}</td>' + ''.join(cc(v) for v in rr2[i]) + '</tr>')
t.append('<tr><td colspan="5"><strong>Organizational multi-agent literature, 2002 to 2004</strong></td></tr>')
for r in extra[:5]: t.append(f'<tr><td>{r[0]}</td>' + ''.join(cc(v) for v in r[1:]) + '</tr>')
t.append('<tr><td colspan="5"><strong>Agent platforms and organization infrastructure, 2002 to 2013</strong></td></tr>')
for r in infra: t.append(f'<tr><td>{r[0]}</td>' + ''.join(cc(v) for v in r[1:]) + '</tr>')
t.append('<tr><td colspan="5"><strong>Further recent sources</strong></td></tr>')
for r in extra[5:]: t.append(f'<tr><td>{r[0]}</td>' + ''.join(cc(v) for v in r[1:]) + '</tr>')
t.append('</table></div>')
(OUT/'tab-groups.html').write_text('\n'.join(t))
def base(v): return re.match(r'(yes|part|no)', v.strip()).group(1)
for k in range(4):
    a = [base(rr[i][k]) for i in rr]; b = [base(r[k+1]) for r in extra]
    print('C%d'%(k+1), {x: a.count(x) for x in ('yes','part','no')}, 'extra', {x: b.count(x) for x in ('yes','part','no')}, 'all27 yes', (a+b).count('yes'))
print('Dir derived', {x: [rows[i][1][ci['Dir']] for i in rows].count(x) for x in ('yes','part','no')})
tot = {c: {'yes':0,'part':0,'no':0,'n.a.':0} for c in cols}
for i in rows:
    for c, v in zip(cols, rows[i][1]): tot[c][v] += 1
f29 = {k: sum(tot[c][k] for c in fcols) for k in ('yes','part','no','n.a.')}; print('29 cols', f29, sum(f29.values()))
print(json.dumps(allc)); print({c: tot[c] for c in ('Dir','DirC','Dom','Cht','Pers','TaskA','AgId','PreA','Art','Lif','Imp')})
print('min yes+part over services:', min((tot[c]['yes']+tot[c]['part'], c) for c in cols[:25]))
print('services yes in all 17:', [c for c in cols[:25] if tot[c]['yes']==17], 'yes+part==17:', [c for c in cols[:25] if tot[c]['yes']+tot[c]['part']==17])
