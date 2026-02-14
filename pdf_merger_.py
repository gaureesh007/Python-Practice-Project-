import PyPDF2
pdf_1_src = "240310690827_1701351193.pdf"
pdf_2_src = "240310690827_1701351167.pdf"
pdf_file = [pdf_1_src,pdf_2_src]
merger = PyPDF2.PdfMerger()
for filename in pdf_file:
    pdf_file = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(pdf_file)
    merger.append(pdfReader)
pdf_file.close()
merger.write(f"merged_{pdf_1_src}_{pdf_2_src}")
