from tkinter import *
from random import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg = "black")
canvas.pack()

for i in range(40):
    x_pos = randint(0,300)
    y_pos = randint(0,300)
    color = "gray" + str(randint(50,90))
    canvas.create_rectangle(x_pos, y_pos, x_pos+5,y_pos+5, fill =  color)

# Draw the night sky:
#  - The background should be black
#  - The stars should be small squares
#  - The stars should have random positions on the canvas
#  - The stars should have random color (some shade of grey)

root.mainloop()