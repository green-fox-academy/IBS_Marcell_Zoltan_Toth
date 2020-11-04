from tkinter import *
from random import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


# Create a function that draws a single line and takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# Draw at least 3 lines with that function using a loop.

Tk.update(root)
center_x = canvas.winfo_width()/2
center_y = canvas.winfo_height()/2

def line_to_the_middle(starting_x, starting_y):
    canvas.create_line(starting_x, starting_y, center_x,center_y)


for i in range(3):
    line_to_the_middle(randint(0,canvas.winfo_width()), randint(0,canvas.winfo_height()))



root.mainloop()