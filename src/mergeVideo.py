from moviepy.editor import *

clip1 = VideoFileClip("Media/Duniya Bananewale_new.mp4").subclip(1,4)
clip2 = VideoFileClip("Media/Duniya Bananewale.mp4").subclip(10,25)

# now lets set postion of  clip1
clip2 = clip2.set_position((45,150))

final_video = concatenate_videoclips([clip1, clip2])



final_video.write_videofile("static/file.mp4")


