from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

canvas.create_line(100,100,200,100, fill ="green")
canvas.create_line(200,100,200,200, fill ="red")
canvas.create_line(200,200,100,200, fill ="blue")
canvas.create_line(100,200,100,100, fill ="yellow")

root.mainloop()