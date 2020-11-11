



def check_rows(field):
    for i in range(len(field)-1):
        if field[i][0] == field[i][1] and field[i][0] == field[i][2]:
            if field[i][0] == "O":
                return 0
            else:
                return 1

    return 2

def check_cols(field):
    for i in range(len(field)):
        if field[0][i] == field[1][i] and field[0][i] == field[2][i]:
            if field[0][i] == "O":
                return 0
            else:
                return 1
    return 2


def check_diag(field):
    if field[0][0] == field[1][1] and field[1][1] == field[2][2]:
        if field[0][0] == "O":
            return 0
        else:
            return 1

    if field[0][2] == field[1][1] and field[1][1] == field[2][0]:
        if field[1][1] == "O":
            return 0
        else:
            return 1

    return 2

def winner(filename):
    buffer = ""
    field = []
    temp = []
    with open(filename, "r") as file:
        buffer = file.read().replace("\n", "")

    for i in range(len(buffer)):
        temp.append(buffer[i])
        if len(temp) == 3:
            field.append(temp)
            temp = []

    if check_rows(field) == 0:
        print("Winner O")
        return
    if check_rows(field) == 1:
        print("Winner X")
        return
    if check_cols(field) == 0:
        print("Winner O")
        return
    if check_cols(field) == 1:
        print("Winner X")
        return
    if check_diag(field) == 0:
        print("Winner O")
        return
    if check_diag(field) == 1:
        print("Winner X")
        return
    print("its a draw!")

winner("win_o.txt")
winner("win_x.txt")
winner("draw.txt")



