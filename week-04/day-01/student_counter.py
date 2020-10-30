students = [
        {'name': 'Theodor', 'age': 3, 'candies': 2},
        {'name': 'Paul', 'age': 9.5, 'candies': 2},
        {'name': 'Mark', 'age': 12, 'candies': 5},
        {'name': 'Peter', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'George', 'age': 10, 'candies': 1}
]

def candies_together(list_of_students):
    candies = 0
    for i in list_of_students:
        for k in students:
            if k.get("name") == i:
                candies += k.get("candies")
    return candies

print(candies_together(["Theodor", "Paul", "Olaf"]))



def sum_of_age(list_of_students):
    age = 0
    for i in list_of_students:
        for k in students:
            if k.get("candies") < 5 and k.get("name") == i:
                age += k.get("age")

    return age

print(sum_of_age(["Theodor", "Paul", "Olaf"]))

