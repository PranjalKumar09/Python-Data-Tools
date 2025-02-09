"""
window width/ height is section of program that will visible by us

and winfo_screenwidth / height tell us our system screen width/w=height

#screen width  ----------------------   
#screen witth/2-----------
#window_width  ------
#wind_width(3) ---
#x =           --------                     (screen_width / 2) - (window_width / 2)
#reult =>              ------                  window_width*
#and it is in middle

for better programming you can even create a function
def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

also in geomentey always x used for multplication not *
# tkinter window with dimensions XxY
root.geometry('XxY+A+B') 
  
(A shifted on X-axis and B shifted on Y-axis)

text_area.grid(sticky=N + E + S + W)
#the text_area widget will be placed in a grid cell and will stick to all four sides of the cell. This will make the widget expand or shrink with the cell when the window is resized. The sticky option takes a string of compass directions (N, E, S, W) that indicate which sides of the cell the widget should stick to. For example, sticky=‘NW’ means that the widget will stick to the top-left corner of the cell


ScrollBar Options
1	activebackground	The background color of the widget when it has the focus.
2	bg	The background color of the widget.
3	bd	The border width of the widget.
4	command	It can be set to the procedure associated with the list which can be called each time when the scrollbar is moved.
5	cursor	The mouse pointer is changed to the cursor type set to this option which can be an arrow, dot, etc.
6	elementborderwidth	It represents the border width around the arrow heads and slider. The default value is -1.
7	Highlightbackground	The focus highlighcolor when the widget doesn't have the focus.
8	highlighcolor	The focus highlighcolor when the widget has the focus.
9	highlightthickness	It represents the thickness of the focus highlight.
10	jump	It is used to control the behavior of the scroll jump. If it set to 1, then the callback is called when the user releases the mouse button.
11	orient	It can be set to HORIZONTAL or VERTICAL depending upon the orientation of the scrollbar.
12	repeatdelay	This option tells the duration up to which the button is to be pressed before the slider starts moving in that direction repeatedly. The default is 300 ms.
13	repeatinterval	The default value of the repeat interval is 100.
14	takefocus	We can tab the focus through this widget by default. We can set this option to 0 if we don't want this behavior.
15	troughcolor	It represents the color of the trough.
16	width	It represents the

ScrollBar Mehtods

SN	Method	Description
1	get()	It returns the two numbers a and b which represents the current position of the scrollbar.
2	set(first, last)	It is used to connect the scrollbar to the other widget w. The yscrollcommand or xscrollcommand of the other widget to this method.

Spinbox in which up arrow and down arrow (fram_object , from_ = -- , to = --, textvariable = -- ,command = --)
Optionbox in which we can select option its not radio button

tkinter.colorchooser.askcolor(title = "----")

The first value is the RGB representation.
The second value is a hexadecimal representation.

change_font(*args) -> multiple arguments

file = tkinter.filedialog.askopenfilename(defaultextension = "..." , file =[(string1,extension1), (string2 ,extension2), ...]) -> for showing opening a file
file = tkinter.filedialog.asksaveasfilename( . .. )
extension all -> *.*
file store here address_object of 

text_area.delete(1.0, END) form starting to end
text_area.insert(1.0, file.read())
text_area.event_generate("<<Cut>>")
text_area.event_generate("<<Ccopy>>")
text_area.event_generate("<<Paste>>")

showinfo is nothing but box

window.destroy() -> end the program


"""

import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor(title="pick a color")
    print(color)
    text_area.config(fg=color[1])


def change_font(*args):
    text_area.config(font=(font_name.get(), font_size.get()))


def open_file():
    file = askopenfile(
        defaultextension=".txt",
        file=[("All files", "*.*"), ("Text documents", "*.txt")],
    )
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END) 

        file = open(file, "r")
        text_area.insert(1.0, file.read())
    except Exception:
        print("Coudn't read files")
    finally:
        file.close()


def new_file():
    window.title("Untitled - Kumar Editor")
    text_area.delete(1.0, END)


def save_file():
    file = filedialog.asksaveasfilename(
        initialfile="unitiled.txt",
        defaultextension=".txt",
        filetypes=[("All files", "*.*"), ("Text documents", "*.txt")],
    )
    if file is None:
        return
    try:
        window.title()(os.path.basename(file))
        file = open(file, "w")

        file.write(text_area.get(1.0, END))
    except Exception:
        print("Coudn't save a file")
    finally:
        file.close()


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("About this Prpgram", "This is program BY Pranjal Kumar Shukla")


def quit():
    window.destroy()


window = Tk()
window.title("Kumar Text editor")
file = None
window_width = 500
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))   
y = int((screen_height / 2) - (window_height / 2)) 

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name, font_size.get()))

scrolbar = Scrollbar(text_area)


window.grid_rowconfigure( 0, weight=1)#at starting and 100% coverage
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)


scrolbar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scrolbar.set) #yscrollcommand

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font) #from_
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0) #default tearoff  = 1 
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()
