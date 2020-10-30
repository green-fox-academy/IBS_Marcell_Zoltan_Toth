students = [
        {'name': 'Mark', 'age': 9.5, 'candies': 2},
        {'name': 'Sean', 'age': 10, 'candies': 1},
        {'name': 'Clark', 'age': 7, 'candies': 3},
        {'name': 'Paul', 'age': 12, 'candies': 5}
]

test = ["Paul", "Mark", "Sean"]

def more_than_4(list_of_students):
    for i in list_of_students:
        for k in students:
            if k.get("name") == i and k.get("candies") > 4:
                print(k.get("name") + " has more than 4 candies")


more_than_4(test)

def candies_on_average(list_of_students):
    numbeer_of_candies = 0
    for i in list_of_students:
        for k in students:
            if k.get("name") == i:
                numbeer_of_candies += k.get("candies")

    return numbeer_of_candies / len(list_of_students)


print(candies_on_average(test))