import pikepdf 
from tkinter.filedialog  import * 

file= askopenfilename()

pdf_my = pikepdf.Pdf.open(file)
for i in  pdf_my.pages:
    i.Rotate = 180
    pdf_my.save("Media/sample.pdf")
    
    
