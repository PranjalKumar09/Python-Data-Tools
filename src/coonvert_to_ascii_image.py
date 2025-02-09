import pywhatkit as kit 

from tkinter.filedialog import askopenfilename

file= askopenfilename()

# new_filename = input("Enter new filename  : ")
# kit.image_to_ascii_art(file,f"Image/{new_filename}.txt" )
 
 
 
# method 2  
from ascii_magic import AsciiArt

my_art = AsciiArt.from_image(file)
my_art.to_terminal()





