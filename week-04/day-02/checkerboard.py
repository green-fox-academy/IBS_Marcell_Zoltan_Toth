from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Fill the canvas with a checkerboard pattern.
for k in range(-300,300,20):
    for i in range(0,300,10):
        canvas.create_rectangle(i+k, i, i+10+k, i+10, fill = "black")


root.mainloop()