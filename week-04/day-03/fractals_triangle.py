from tkinter import *

root = Tk()

canvas = Canvas(root, width="350", height="350")
canvas.pack()

initial_list = [[10, 10], [310, 10], [160, 310]]


def middle_point(point1, point2):
    sol = []
    sol.append(abs(point2[0] + point1[0]) / 2)
    sol.append(abs(point2[1] + point1[1]) / 2)
    return sol


def draw_triangle(list_of_points, depth):
    next_points = []
    top_left = []
    top_right = []
    bottom = []
    canvas.create_line(list_of_points[0][0], list_of_points[0][1], list_of_points[1][0], list_of_points[1][1])
    canvas.create_line(list_of_points[1][0], list_of_points[1][1], list_of_points[2][0], list_of_points[2][1])
    canvas.create_line(list_of_points[2][0], list_of_points[2][1], list_of_points[0][0], list_of_points[0][1])
    if depth < 7:
        first = middle_point(list_of_points[0], list_of_points[1])
        second = middle_point(list_of_points[1], list_of_points[2])
        third = middle_point(list_of_points[2], list_of_points[0])

        top_left.append(list_of_points[0])
        top_left.append(first)
        top_left.append(third)
        draw_triangle(top_left, depth+1)

        top_right.append(list_of_points[1])
        top_right.append(first)
        top_right.append(second)
        draw_triangle(top_right, depth+1)

        bottom.append(list_of_points[2])
        bottom.append(second)
        bottom.append(third)
        draw_triangle(bottom, depth+1)

        '''
        next_points.append(first)
        next_points.append(second)
        next_points.append(third)
        draw_triangle(next_points, depth + 1)
        '''

'''
canvas.create_line(initial_list[0][0], initial_list[0][1], initial_list[1][0], initial_list[1][1])
canvas.create_line(initial_list[1][0], initial_list[1][1], initial_list[2][0], initial_list[2][1])
canvas.create_line(initial_list[2][0], initial_list[2][1], initial_list[0][0], initial_list[0][1])
'''

draw_triangle(initial_list, 0)

root.mainloop()


print(middle_point(initial_list[0],initial_list[1] ))
print(middle_point(initial_list[1],initial_list[2] ))
print(middle_point(initial_list[2],initial_list[0] ))
