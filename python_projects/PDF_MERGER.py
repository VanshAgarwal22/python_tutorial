import PyPDF2

pdffiles = ["Resume_job (1).pdf", "vansh_resume.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdffiles:
    pdffile= open(filename ,'rb')
    pdfReader = PyPDF2.PdfReader(pdffile)
    merger.append(pdfReader)
pdffile.close()
merger.write('merge.pdf')

    
