import sys
from pypdf import PdfReader, PdfWriter
src,out,a,b=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
r=PdfReader(src); w=PdfWriter()
for i in range(a-1,b): w.add_page(r.pages[i])
w.write(out); print(out,b-a+1)
