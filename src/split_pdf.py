import pikepdf 
from tkinter.filedialog  import *

file= askopenfilename()

pdf_my = pikepdf.Pdf.open(file)

for n, page in enumerate(pdf_my.pages):
    new_page = pikepdf.Pdf.new()
    
    new_page.pages.append(page)
    name = f"test {str(n)}.pdf"
    new_page.save(name)
