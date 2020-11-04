from tkinter import *
from random import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

Tk.update(root)
# Create a function that draws a single line and takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# Draw at least 3 lines with that function using a loop.

def fifty_from(line_x, line_y):
    canvas.create_line(line_x,line_y, line_x+50, line_y)


for i in range(3):
    fifty_from(randint(0, canvas.winfo_width()), randint(0, canvas.winfo_height()) )

root.mainloop()