from pikepdf import Pdf 
from glob import glob

new_pdf = Pdf.new()

for file in glob("*.pdf"):
    new_pdf.pages.extend(Pdf.open(file).pages)
    
new_pdf.save("sample.pdf")
