from tkinter import *
from random import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

Tk.update(root)
# Draw four different size and color rectangles.
# Avoid code duplication.

width = canvas.winfo_width()
height = canvas.winfo_height()

def draw_rectangle(nw_x, nw_y, se_x, se_y, color):
    canvas.create_rectangle(nw_x, nw_y, se_x, se_y, fill=color)


colors = ["red", "green", "blue", "yellow", "brown", "white", "cyan", "orange", "pink"]

for i in range(4):
    draw_rectangle(randint(0,width), randint(0,height), randint(0,width), randint(0,height), colors[randint(0,len(colors)-1)] )

root.mainloop()
