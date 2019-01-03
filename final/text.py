# -*- coding:utf-8 -*-
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

image_frame = Frame(root)

image_file = im = image_label = None
def create_image_label():
    global image_file, im, image_label
    image_file = Image.open("plane.png")
    im = ImageTk.PhotoImage(image_file)
    image_label = Label(image_frame,image = im)
    image_label.grid(row = 3, column = 0, sticky = NW, pady = 8, padx = 20)

button = Button(image_frame,text='猛击这里',anchor = 'center',command = create_image_label)
button.grid(row = 2, column = 0, sticky = NW, pady = 8, padx = 20)

image_frame.pack()

root.mainloop()
