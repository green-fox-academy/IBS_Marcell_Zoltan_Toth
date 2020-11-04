from tkinter import *

root = Tk()

canvas = Canvas(root, width="300", height="300")
canvas.pack()

Tk.update(root)
vertical_midpoint = canvas.winfo_width() /2
horizontal_midpoint = canvas.winfo_height() /2

canvas.create_line(0,vertical_midpoint,300,vertical_midpoint, fill="red")
canvas.create_line(horizontal_midpoint,0,horizontal_midpoint,300, fill="green")

canvas.pack()

root.mainloop()