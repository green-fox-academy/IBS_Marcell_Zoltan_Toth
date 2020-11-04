from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

Tk.update(root)
mid_x = canvas.winfo_width()/2
mid_y = canvas.winfo_height()/2

def line_to_mid(start_x, start_y):
    canvas.create_line(start_x,start_y,mid_x,mid_y)


for i in range(0,300,20):
    line_to_mid(0,i)
    line_to_mid(i,0)
    line_to_mid(canvas.winfo_width(),i)
    line_to_mid(i, canvas.winfo_height())

# Create a function that draws a single line and takes 2 parameters:
# The x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# Fill the canvas with lines from the edges, every 20 px, to the center.

root.mainloop()