map = {}

map["Eggs"] = 200
map["Milk"] = 200
map["Fish"] = 400
map["Apples"] = 150
map["Bread"] = 50
map["Chicken"] = 550

less_than_201 = []
more_than_150 = []

for k,v in map.items():
    if v < 201:
        less_than_201.append(k)

print(less_than_201)

for i in map.items():
    if i[1] > 150:
        more_than_150.append(i)

print(more_than_150)