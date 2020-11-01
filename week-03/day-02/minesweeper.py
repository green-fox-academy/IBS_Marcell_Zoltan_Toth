import random

discovered_field_count = 1


def front_display_field(arr):
    out = []
    temp_row = []
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr) - 1):
            temp_row.append(arr[i][j])
        out.append(temp_row[:])
        temp_row.clear()

    for i in out:
        print(i)
        print()


def back_display_field(arr):
    for i in arr:
        print(i)
        print()


def generate_back_field_size(num, fill):
    temp = []
    sol = []
    for i in range(num):
        temp.append(fill)
    for i in range(num):
        sol.append(temp[:])
    return sol


def generate_front_field_size(num, fill):
    temp = []
    sol = []
    for i in range(num):
        temp.append(fill)
    for i in range(num):
        sol.append(temp[:])

    for i in range(1, len(sol) - 1):
        for j in range(1, len(sol) - 1):
            sol[i][j] = "X"

    return sol


def generate_mines(arr):
    number_of_mines = ((len(arr) - 2) ** 2) // 10
    if number_of_mines == 0:
        number_of_mines = 1
    # number_of_mines = 5
    goal = 0
    mine_locations = []

    while goal != number_of_mines:
        i_rand = random.randint(1, len(arr) - 2)
        j_rand = random.randint(1, len(arr) - 2)

        if arr[i_rand][j_rand] != "*":
            arr[i_rand][j_rand] = "*"
            mine_locations.append([i_rand, j_rand])
            goal += 1

    return mine_locations


def generate_clues(field):
    count_of_surrounding_mines = 0
    for i in range(1, len(field) - 1):
        for j in range(1, len(field) - 1):
            if i == 0 or j == 0 or i == len(field) - 1 or j == len(field) - 1:
                field[i][j] = 0
            elif field[i][j] == "*":
                continue
            else:
                if field[i - 1][j - 1] == "*":
                    count_of_surrounding_mines += 1
                if field[i - 1][j] == "*":
                    count_of_surrounding_mines += 1
                if field[i - 1][j + 1] == "*":
                    count_of_surrounding_mines += 1
                if field[i][j - 1] == "*":
                    count_of_surrounding_mines += 1
                if field[i][j + 1] == "*":
                    count_of_surrounding_mines += 1
                if field[i + 1][j - 1] == "*":
                    count_of_surrounding_mines += 1
                if field[i + 1][j] == "*":
                    count_of_surrounding_mines += 1
                if field[i + 1][j + 1] == "*":
                    count_of_surrounding_mines += 1

                field[i][j] = str(count_of_surrounding_mines)
                count_of_surrounding_mines = 0


def move(i, j, front, back):
    front[i][j] = back[i][j]
    return back[i][j]


def moves_left(front):
    moves = 0
    for i in range(1, len(front) - 1):
        for j in range(1, len(front) - 1):
            if front[i][j] == "X":
                moves += 1

    return moves


def zero_flood_fill(i, j, front, back):
    if front[i - 1][j] == "X" and back[i - 1][j] == "0":    #up
        front[i - 1][j] = back[i - 1][j]
        zero_flood_fill(i - 1, j, front, back)       #left
    if front[i][j - 1] == "X" and back[i][j - 1] == "0":
        front[i][j - 1] = back[i][j - 1]
        zero_flood_fill(i, j - 1, front, back)       #right
    if front[i][j + 1] == "X" and back[i][j + 1] == "0":
        front[i][j + 1] = back[i][j + 1]
        zero_flood_fill(i, j + 1, front, back)       #down
    if front[i + 1][j] == "X" and back[i + 1][j] == "0":
        front[i + 1][j] = back[i + 1][j]
        zero_flood_fill(i + 1, j, front, back)


size = int(input("What size do you want your filed to be?"))

front_field = generate_front_field_size(size + 2, "0")
back_filed = generate_back_field_size(size + 2, "0")
mines = generate_mines(back_filed)
generate_clues(back_filed)

back_display_field(back_filed)
print()
print()
front_display_field(front_field)
condition = moves_left(front_field)

while condition > len(mines):
    i_move = int(input("Give me an X coordinate!")) + 1
    j_move = int(input("Give me a Y coordinate!")) + 1

    symbol = move(i_move, j_move, front_field, back_filed)
    if symbol == "*":
        front_display_field(front_field)
        print("BOOOM, youve just stepped on a bomb! Game over.")
        break
    elif symbol == "0":
        zero_flood_fill(i_move, j_move, front_field, back_filed)

    front_display_field(front_field)
    condition = moves_left(front_field)
print("CONGRATULATIONS! YOU WON!")

#The code below shows how i got to the final solution, not deleted so I can review the thought process later.

'''
def compare_fields(locations, neighbours):
    matches = 0
    for i in neighbours:
        for k in locations:
            if i == k:
                matches += 1
                continue
    return matches


def generate_clues(arr, locations):
    neighbours = []
    for i in range(1:len(arr)-1):
        for j in range(1:len(arr)-1):
            if arr[i][j] != "*":
                neighbours.append([i + 1, j])
                neighbours.append([i - 1, j])
                neighbours.append([i, j + 1])
                neighbours.append([i, j - 1])
                arr[i][j] = compare_fields(locations, neighbours)
                neighbours.clear()





def explore_field(i, j, front, back):
    front[i][j] = back[i][j]


def case_zero(i, j, back):
    checked_fields = []
    checked_fields.append([i, j])



size = int(input("How big do you want the filed to be?"))
field_back = generate_field_size(size, 0)
field_front = generate_field_size(size, "X")
mine_locations = generate_mines(field_back)
generate_clues(field_back, mine_locations)
display_list(field_front)

discovered_field_count = size ** 2 - len(mine_locations)

while discovered_field_count != 0:
    coordinates_j = int(input("Give me an X coordinate to explore!"))
    coordinates_i = int(input("Give me an Y coordinate to explore!"))
    explore_field(coordinates_i, coordinates_j, field_front, field_back)

    if field_back[coordinates_i][coordinates_j] == "*":
        print("BOOOM!")
        break
    elif field_back[coordinates_i][coordinates_j] == 0:
        print("Special case")
    else:
        display_list(field_front)
        discovered_field_count -= 1


test = generate_field_size(5)
loc = generate_mines(test)
display_list(test)
print("-------------")
generate_clues(test, loc)
print(loc)
print("-------------")
display_list(test)


'''
