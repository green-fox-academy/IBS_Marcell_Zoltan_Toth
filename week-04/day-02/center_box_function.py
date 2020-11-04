from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

Tk.update(root)

canvas_width = canvas.winfo_width()/2
canvas_height = canvas.winfo_height()/2


# Create a function that draws one square and takes 1 parameters:
# The square size
# and draws a square of that size to the center of the canvas.
# Draw 3 squares with that function.
# Avoid code duplication.


def center_box(size):
    canvas.create_rectangle(canvas_width - size /2, canvas_height - size/2, canvas_width + size /2, canvas_height + size/2 )


for i in range(3):
    center_box(10)
    center_box(30)
    center_box(50)


root.mainloop()