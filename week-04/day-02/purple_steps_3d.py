from tkinter import *

root = Tk()

canvas = Canvas(root, width = "1000", height = "1000")
canvas.pack()


increment = 0
start_x = 0
start_y = 0
end_x = 0
enx_y = 0
for i in range(10,200,10):
    end_x = start_x + i + increment
    end_y = start_x + i + increment
    canvas.create_rectangle(start_x,start_y,end_x,end_y, fill = "purple")
    increment += 10
    start_x = end_x
    start_y = end_y



root.mainloop()