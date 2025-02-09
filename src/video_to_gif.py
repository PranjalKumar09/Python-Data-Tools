from moviepy.editor import VideoFileClip
from tkinter import Tk, Label, Button, Entry, filedialog, StringVar, OptionMenu
import os

class VideoToGIFConverter:
    def __init__(self, master):
        self.master = master
        master.title("Kumar Video to GIF Converter")

        # Set the geometry to 500x500
        master.geometry("500x500+710+310")

        # Define a variable for font size
        font_size = 14

        # Set the font for labels
        label_font = ("Arial", font_size)

        self.label = Label(master, text="Select a video file:", font=label_font)
        self.label.pack()

        self.select_button = Button(master, text="Browse", command=self.select_file, font=label_font)
        self.select_button.pack()

        self.start_label = Label(master, text="Enter starting time (in seconds):", font=label_font)
        self.start_label.pack()
        self.start_entry = Entry(master, width=30, font=label_font)
        self.start_entry.pack()

        self.end_label = Label(master, text="Enter ending time (in seconds):", font=label_font)
        self.end_label.pack()
        self.end_entry = Entry(master, width=30, font=label_font)
        self.end_entry.pack()

        self.filename_label = Label(master, text="Enter new filename:", font=label_font)
        self.filename_label.pack()
        self.filename_entry = Entry(master, width=30, font=label_font)
        self.filename_entry.pack()

        self.rotate_label = Label(master, text="Rotate GIF:", font=label_font)
        self.rotate_label.pack()

        # Provide predefined rotation options in a dropdown menu
        self.rotation_var = StringVar(master)
        self.rotation_var.set("0")  # Default to 0 degree rotation
        self.rotation_options = ["0", "90", "180", "270"]
        self.rotation_menu = OptionMenu(master, self.rotation_var, *self.rotation_options)
        self.rotation_menu.pack()

        self.convert_button = Button(master, text="Convert to GIF", command=self.convert_to_gif, font=label_font)
        self.convert_button.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename()
        self.label.config(text=f"Selected file: {file_path}")
        self.file_path = file_path

    def convert_to_gif(self):
        try:
            start_second = int(self.start_entry.get())
            end_second = int(self.end_entry.get())
            new_file = self.filename_entry.get()
            rotation_degree = float(self.rotation_var.get())

            video = VideoFileClip(self.file_path).subclip(start_second, end_second)

            media_directory = "Media"
            if not os.path.exists(media_directory):
                os.makedirs(media_directory)

            # Check if the user wants to rotate the GIF
            if rotation_degree != 0:
                video = video.rotate(rotation_degree)

            video.write_gif(os.path.join(media_directory, f"{new_file}.gif"))
            print(f"GIF created successfully: {os.path.join(media_directory, new_file + '.gif')}")

        except Exception as e:
            print(f"Error converting to GIF: {e}")

if __name__ == "__main__":
    root = Tk()
    app = VideoToGIFConverter(root)
    root.mainloop()
