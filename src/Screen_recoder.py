""" NOT WORKING
"""

import cv2
import pyautogui 
import numpy as np
import time
from Xlib import display


def get_screen__resolution():
# Open the display
    d = display.Display()

    # Get the default screen
    screen = d.screen()

    # Get the root window
    root = screen.root

    # Get the width and height of the root window
    width = root.get_geometry().width
    height = root.get_geometry().height

    return width, height

# Get and print the screen resolution
width, height = get_screen__resolution()
dim = (width, height)
# Change the VideoWriter_fourcc line to use H.264 codec
f = cv2.VideoWriter_fourcc(*"H264")
output = cv2.VideoWriter("test.mp4v", f, 30.0, dim)


time_now = time.time()
dur = 10 
time_end = time_now + dur 

while 1:
    image = pyautogui.screenshot()
    frame_1 =np.array(image)
    frame = cv2.cvtColor(frame_1 , cv2.COLOR_BGR2RGB)
    
    output.write(frame)

    c_time = time.time()
    if c_time > time_end:
        break
output.release()
print("VIdeo maded ")




