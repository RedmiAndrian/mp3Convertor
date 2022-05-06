#!/usr/bin/env python3

from tkinter import *
from tkinter.filedialog import askdirectory, askopenfilename
import os

root = Tk()
root.title("Convert to MP3")

def ask_dir():
    global file
    file = askopenfilename(title="Select a file to convert")
    
def convert():
    convert_button['state'] = DISABLED
    output_name = e.get()
    print("ffmpeg -i \"" + file + "\" input.wav -vn -ar 44100 -ac 2 -b:a 192k \"" + output_name + "\"")
    os.system("ffmpeg -i \"" + file + "\" -vn -ar 44100 -ac 2 -b:a 192k \"" + output_name + "\"")
    convert_button['state'] = NORMAL

e = Entry(root, width=35, borderwidth=5)
file_select = Button(root, text="Choose a file", command=ask_dir)
convert_button = Button(root, text="Convert", command=convert)


file_select.grid(row=0, column=0)
e.grid(row=1, column=0)
convert_button.grid(row=2, column=0)



root.mainloop()

