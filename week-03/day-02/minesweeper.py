import random

discovered_field_count = 1


def display_field(arr):
    for i in arr:
        print(i)
        print()


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
        i_rand = random.randint(1, len(arr) - 2)
        j_rand = random.randint(1, len(arr) - 2)

        if arr[i_rand][j_rand] != "*":
            arr[i_rand][j_rand] = "*"
            mine_locations.append([i_rand, j_rand])
            goal += 1

    return mine_locations



def generate_clues(field):
    count_of_surrounding_mines = 0
    for i in range(1, len(field)-1):
        for j in range(1, len(field)-1):
            if i == 0 or j == 0 or i == len(field) -1 or j == len(field) -1:
                field[i][j] = 0
            elif field[i][j] == "*":
                continue
            else:
                if field[i-1][j-1] == "*":
                    count_of_surrounding_mines += 1
                if field[i-1][j] == "*":
                    count_of_surrounding_mines += 1
                if field[i-1][j+1] == "*":
                    count_of_surrounding_mines += 1
                if field[i][j-1] == "*":
                    count_of_surrounding_mines += 1
                if field[i][j+1] == "*":
                    count_of_surrounding_mines += 1
                if field[i+1][j-1] == "*":
                    count_of_surrounding_mines += 1
                if field[i+1][j] == "*":
                    count_of_surrounding_mines += 1
                if field[i+1][j+1] == "*":
                    count_of_surrounding_mines += 1

                field[i][j] = str(count_of_surrounding_mines)
                count_of_surrounding_mines = 0







front_field = generate_field_size(5, "0")
back_filed = generate_field_size(7, "0")
loc = generate_mines(back_filed)
generate_clues(back_filed)
display_field(front_field)
print()
print()
display_field(back_filed)

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
