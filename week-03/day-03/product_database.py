map = {}

map["Eggs"] = 200
map["Milk"] = 200
map["Fish"] = 400
map["Apples"] = 150
map["Bread"] = 50
map["Chicken"] = 550


print(map["Fish"])

for k,v in map.items():
    if v == max(map.values()):
        print("Most expensive item: " + k)
        break

print(sum(map.values()) / len(map))

items_under_300 = 0
for i in map.values():
    if i < 300:
        items_under_300 += 1

if 125 in map.values():
    print("There is sth to buy for 125")
else:
    print("There is nothing to buy for 125")

for k,v in map.items():
    if v == min(map.values()):
        print("Cheapest item: " + k)
        break
