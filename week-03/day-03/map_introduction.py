map = {}

if map:
    print("the map is not empty")
else:
    print("the map is empty")

map[97] = "a"
map[98] = "b"
map[99] = "c"
map[65] = "A"
map[66] = "B"
map[67] = "C"


print(map.keys())   # prints the keys in a custom made list --> strange !

for k,v in map.items():
    print(str(k) + "-->" + v)


map[68]  = "D"

print(len(map))

print(map[99])

del map[97]

if 100 in map:
    print("There is a key with 100")
else:
    print("no key with 100")

map.clear()


