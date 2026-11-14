import sys
from pypdf import PdfReader
r=PdfReader(sys.argv[1]); out=[]
for i,p in enumerate(r.pages,1): out.append(f"\n===== PDF p.{i} =====\n"+(p.extract_text() or ''))
open(sys.argv[2],'w').write(''.join(out)); print(len(r.pages),'pages',sum(len(x.split()) for x in out),'words')
