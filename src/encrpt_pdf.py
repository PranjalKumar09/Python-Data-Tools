import pikepdf
from tkinter.filedialog import *

file= askopenfilename()

old_pdf = pikepdf.Pdf.open(file)

no_extr = pikepdf.Permissions(extract=False) 

old_pdf.save("static/sample.pdf", 
             encryption= pikepdf.Encryption(user = "123",owner="pranjal" , allow=no_extr))

# user is password here