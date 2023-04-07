# python project to merge pdfs
from PyPDF2 import PdfWriter
import os
merger=PdfWriter()
files=[file for file in os.listdir("C:/Users/Yash Habib/.vscode") if file.endswith(".pdf")] #here give your path where the pdf you want to merge is saved
for pdf in files:
    merger.append(pdf)
merger.write("merged_pdf.pdf")
merger.close()