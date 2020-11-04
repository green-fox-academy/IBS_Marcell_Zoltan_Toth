from tkinter import *
from random import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that draws one square and takes 2 parameters:
# The x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# Draw 3 squares with that function.
# Avoid code duplication.

def draw_square(sq_x, sq_y):
    canvas.create_rectangle(sq_x,sq_y,sq_x+50,sq_y+50)

for i in range(3):
    draw_square(randint(0,300),randint(0,300))

root.mainloop()