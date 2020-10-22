matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
number_of_moves = 0
player = 0
player_id = ""
winner = False


def draw_grid(matrix):
    print("   " + "|" + "   " + "|" + "   ")
    print(" " + str(matrix[0][0]) + " |" + " " + str(matrix[0][1]) + " |" + " " + str(matrix[0][2]) + "  ")
    print("___" + "|" + "___" + "|" + "___")
    print("   " + "|" + "   " + "|" + "   ")
    print(" " + str(matrix[1][0]) + " |" + " " + str(matrix[1][1]) + " |" + " " + str(matrix[1][2]) + "  ")
    print("___" + "|" + "___" + "|" + "___")
    print(" " + str(matrix[2][0]) + " |" + " " + str(matrix[2][1]) + " |" + " " + str(matrix[2][2]) + "  ")
    print("   " + "|" + "   " + "|" + "   ")


def check_horizontal(matrix):
    if matrix[0][0] == matrix[0][1] and matrix[0][1] == matrix[0][2] and matrix[0][0] != " ":
        return True
    elif matrix[1][0] == matrix[1][1] and matrix[1][1] == matrix[1][2] and matrix[1][0] != " ":
        return True
    elif matrix[2][0] == matrix[2][1] and matrix[2][1] == matrix[2][2] and matrix[2][0] != " ":
        return True
    else:
        return False


def check_vertical(matrix):
    if matrix[0][0] == matrix[1][0] and matrix[1][0] == matrix[2][0] and matrix[0][0] != " ":
        return True
    elif matrix[0][1] == matrix[1][1] and matrix[1][1] == matrix[2][1] and matrix[0][1] != " ":
        return True
    elif matrix[0][2] == matrix[1][2] and matrix[1][2] == matrix[2][2] and matrix[0][2] != " ":
        return True
    else:
        return False


def check_diagonal(matrix):
    if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] and matrix[0][0] != " ":
        return True
    elif matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0] and matrix[0][2] != " ":
        return True
    else:
        return False


def check_all(matrix):
    if check_diagonal(matrix) or check_horizontal(matrix) or check_vertical(matrix):
        return True
    else:
        return False


def move(i, j, player, matrix_t):
    if player == 1:
        matrix_t[i][j] = "X"
    else:
        matrix_t[i][j] = "0"
    return matrix_t


while number_of_moves < 9:
    X_move = -1
    Y_move = -1

    if player % 2 == 0:
        player_id = "Player 1"
    else:
        player_id = "Player 2"

    while True:
        try:
            i = int(input(player_id + ", Give me an X coordinate!"))
        except:
            print("I need an integer!")
            continue
        if i > 2:
            print("The X coordinate has to be between 0 and 2!")
            continue
        else:
            X_move = i
            break

    while True:
        try:
            j = int(input(player_id + ", Give me an Y coordinate!"))
        except:
            print("I need an integer!")
            continue
        if j > 2:
            print("The Y coordinate has to be between 0 and 2!")
            continue
        else:
            Y_move = j
            break

    if matrix[X_move][Y_move] != " ":
        print("That slot is taken! Chose another one!")
        continue

    move(X_move, Y_move, player % 2, matrix)
    draw_grid(matrix)

    if check_all(matrix):
        print("The game is over!" + player_id + " won! Congratulations!")
        winner = True
        break

    player += 1
    number_of_moves += 1

if winner is not True:
    print("Seems like it is a draw! Good game!")