from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a green 10x10 square to the center of the canvas.

Tk.update(root)
mid_x = canvas.winfo_width()/2
mid_y = canvas.winfo_height()/2

square_side = 10
canvas.create_rectangle(mid_x-square_side/2,mid_y-square_side/2,mid_x+square_side/2,mid_y+square_side/2, fill = "green")

root.mainloop()