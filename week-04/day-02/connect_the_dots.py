from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that takes 1 parameter:
# A list of [x, y] points
# and connects them with green lines.
# Connect these to get a box:
points = [[10, 10], [290,  10], [290, 290], [10, 290]]
# Connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]
points2 = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],[120, 100], [85, 130], [50, 100]]

def connect(list_of_points):
    for i in range(0,len(list_of_points)-1):
        canvas.create_line(list_of_points[i][0], list_of_points[i][1], list_of_points[i+1][0], list_of_points[i+1][1])

    canvas.create_line(list_of_points[len(list_of_points)-1][0], list_of_points[len(list_of_points)-1][1],list_of_points[0][0], list_of_points[0][1] )


connect(points2)
root.mainloop()