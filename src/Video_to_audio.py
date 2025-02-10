import moviepy.editor
from tkinter.filedialog import *

file= askopenfilename()
video = moviepy.editor.VideoFileClip(file)

aud = video.audio 

aud.write_audiofile("Media/Conveted.mp3")

print("END")



