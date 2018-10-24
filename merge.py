from PyPDF2 import PdfFileMerger

pdfs = []
#replace 57 with number of lectures
for i in range(1,57):
  pdfs.append(str(i)+'.pdf')
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('result.pdf', 'wb') as fout:
    merger.write(fout)
