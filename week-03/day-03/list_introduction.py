names = []

print(len(names))

names.append("William")

if names:
    print("the list is not empty")
else:
    print("the list is empty")

names.append("John")
names.append("Amanda")

print(len(names))

print(names[2])


for i in names:
    print(i)

for i in range(len(names)-1):
    print(str(i) + "." + names[i])

names.remove(names[1])

for i in range(len(names)-1, -1,-1):
    print(names[i])

while names:
    names.remove(names[0])







