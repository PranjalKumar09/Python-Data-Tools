from PyPDF2 import PdfWriter 
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith("pdf")]
# to do in any order you must  in that order



for pdf in files:
    merger.append(pdf)
    
merger.write("Merged-pdf.pdf")
merger.close()



