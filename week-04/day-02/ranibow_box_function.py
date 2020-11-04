from tkinter import *
from random import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

Tk.update(root)

canvas_width = canvas.winfo_width()/2
canvas_height = canvas.winfo_height()/2



# Create a square drawing function that takes 2 parameters:
# The square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# Create a loop that fills the canvas with rainbow colored squares (red, orange, yellow, green, blue, indigo, violet).


def center_box(size, color):
    canvas.create_rectangle(canvas_width - size /2, canvas_height - size/2, canvas_width + size /2, canvas_height + size/2, fill = color )


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range(10,-1,-1):
    center_box(i*10, colors[randint(0,len(colors)-1)])


root.mainloop()