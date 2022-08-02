from PyPDF2  import PdfReader

import os

merger = PyPDF2.PdfReader.Merger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combined.pdf")