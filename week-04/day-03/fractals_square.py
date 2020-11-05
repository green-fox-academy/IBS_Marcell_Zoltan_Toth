from tkinter import *

root = Tk()

canvas = Canvas(root, width="1000", height="1000")
canvas.pack()

center_x = canvas.winfo_width()
center_y = canvas.winfo_height()

init_square = [[0, 0], [300, 300]]


def square_parameters(points):
    out = []
    pos_x = (abs(points[0][0] - points[1][0]) /2 + points[0][0])
    pos_y = (abs(points[0][1] - points[1][1]) /2 + points[0][1])
    size = abs(points[0][0] - points[1][0]) /6
    out.append(pos_x)
    out.append(pos_y)
    out.append(size)
    return out


def square_fractal(topl_botr, depth):
    param = square_parameters(topl_botr)
    canvas.create_rectangle(param[0] - param[2], param[1] - param[2], param[0] + param[2], param[1] + param[2], fill="black")
    if depth < 4:

        sq_1 = [[param[0] - param[2]*3, param[1] - param[2]*3],[param[0] - param[2], param[1] - param[2]]]
        square_fractal(sq_1, depth + 1)

        sq_2 = [[param[0] - param[2], param[1] - param[2]*3],[param[0] + param[2], param[1] - param[2]]]
        square_fractal(sq_2, depth + 1)

        sq_3 = [[param[0]+param[2], param[1]-param[2]*3],[param[0]+param[2]*3, param[1]-param[2]]]
        square_fractal(sq_3, depth + 1)

        sq_4 = [[param[0]-param[2]*3, param[1]-param[2]],[param[0]-param[2], param[1]+param[2]]]
        square_fractal(sq_4, depth + 1)

        sq_5 = [[param[0]+param[2], param[1]-param[2]],[param[0]+param[2]*3, param[1]+param[2]]]
        square_fractal(sq_5, depth + 1)

        sq_6 = [[param[0]-param[2]*3, param[1]+param[2]],[param[0]-param[2], param[1]+param[2]*3]]
        square_fractal(sq_6, depth + 1)

        sq_7 = [[param[0]-param[2], param[1]+param[2]],[param[0]+param[2], param[1]+param[2]*3]]
        square_fractal(sq_7, depth + 1)

        sq_8 = [[param[0]+param[2], param[1]+param[2]],[param[0]+param[2]*3, param[1]+param[2]*3]]
        square_fractal(sq_8, depth + 1)

        '''
        sq_1 = [topl_botr[0], [param[0] - param[2], param[1] - param[2]]]
        square_fractal(sq_1, depth+1)
        
        sq_2 = [[topl_botr[0][0] + param[2]*2, topl_botr[0][1] ],[param[0] - param[2], param[1] - param[2]]]
        square_fractal(sq_2, depth + 1)
        
        sq_3 = [[topl_botr[0][0] + param[2]*4, topl_botr[0][1] ],[param[0] + param[2], param[1] - param[2]]]
        square_fractal(sq_3, depth + 1)
        
        sq_4 = [[topl_botr[0][0], topl_botr[0][1] + param[2]*2],[param[0] - param[2], param[1] + param[2]]]
        square_fractal(sq_4, depth + 1)
        
        sq_5 = [[param[0] - param[2], param[1] - param[2]],[param[0] - param[2] , param[1] - param[2]]]
        '''


square_fractal([[0,0],[1000,1000]], 0)

root.mainloop()
