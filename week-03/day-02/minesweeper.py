import random

discovered_field_count = 1


def generate_field_size(num, fill):
    temp = []
    sol = []
    for i in range(num):
        temp.append(fill)
    for i in range(num):
        sol.append(temp[:])
    return sol


def generate_mines(arr):
    number_of_mines = (len(arr) ** 2) // 10
    # number_of_mines = 5
    goal = 0
    mine_locations = []

    while goal != number_of_mines:
        i_rand = random.randint(0, len(arr) - 1)
        j_rand = random.randint(0, len(arr) - 1)

        if arr[i_rand][j_rand] != "*":
            arr[i_rand][j_rand] = "*"
            mine_locations.append([i_rand, j_rand])
            goal += 1

    return mine_locations


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
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != "*":
                neighbours.append([i + 1, j])
                neighbours.append([i - 1, j])
                neighbours.append([i, j + 1])
                neighbours.append([i, j - 1])
                arr[i][j] = compare_fields(locations, neighbours)
                neighbours.clear()


def display_list(arr):
    for i in arr:
        print(str(i) + " ")
        print()


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

'''
test = generate_field_size(5)
loc = generate_mines(test)
display_list(test)
print("-------------")
generate_clues(test, loc)
print(loc)
print("-------------")
display_list(test)
'''
