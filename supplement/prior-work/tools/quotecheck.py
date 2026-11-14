import sys,re,html,glob,os,unicodedata
from pypdf import PdfReader
B=sys.argv[1]; W=sys.argv[2]
def norm(s):
    s=unicodedata.normalize('NFKD',s)
    s=s.replace('ﬁ','fi').replace('ﬂ','fl')
    return re.sub(r'[^a-z0-9]','',s.lower())
def pdf(p):
    try: return ' '.join((pg.extract_text() or '') for pg in PdfReader(p).pages)
    except Exception as e: return ''
def htm(p):
    t=open(p,encoding='utf-8',errors='replace').read()
    t=re.sub(r'<(script|style)[\s\S]*?</\1>','',t); return html.unescape(re.sub(r'<[^>]+>',' ',t))
def txt(p): return open(p,encoding='utf-8',errors='replace').read()
mara=' '.join(txt(f) for f in glob.glob(B+'/corpus/mara/**/*.md',recursive=True))
corp={
 1:pdf(B+'/corpus/aam.pdf'), 2:pdf(B+'/corpus/opera.pdf'), 3:htm(B+'/corpus/asoc.html'), 4:mara, 5:pdf(B+'/corpus/hl.pdf'),
 6:txt(B+'/src/fipa-SC00023K-text.txt'),
 7:pdf(B+'/src/ameli.pdf')+' '+pdf(B+'/src/huget-model-checking-EI.pdf')+' '+txt(B+'/islander-article/islander-decoded.txt'),
 8:txt(B+'/jacamo-article/jacamo-scp-2013.txt')+' '+txt(B+'/corpus/moise-extra.txt') if os.path.exists(B+'/corpus/moise-extra.txt') else txt(B+'/jacamo-article/jacamo-scp-2013.txt'),
}
ncorp={k:norm(v) for k,v in corp.items()}
print('corpus sizes',{k:len(v) for k,v in ncorp.items()})
for r in ['a','b']:
    t=open(f'{W}/prior-work/rerate-v2-reader-{r}.md').read()
    parts=re.split(r'\n# (\d)\. ',t)
    tot=hit=0; miss=[]
    for i in range(1,len(parts),2):
        n=int(parts[i]); body=parts[i+1].split('\n# ')[0]
        extra=''
        # addenda belong to 8 and 7
        for q in re.findall(r'["“]([^"”]{30,})["”]',body):
            for frag in re.split(r'\[\.\.\.\]|\[…\]|\.\.\.|…',q):
                f=norm(frag)
                if len(f)<25: continue
                tot+=1
                if f in ncorp[n]: hit+=1
                else: miss.append((n,frag.strip()[:150]))
    print(f'reader {r}: {hit}/{tot} fragments found'); 
    from collections import Counter
    print('  misses by source',dict(Counter(m[0] for m in miss)))
    for m in miss[:40]: print('   ',m[0],'|',m[1])
