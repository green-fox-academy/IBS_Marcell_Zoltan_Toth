result = []
temp = [0, 0, 0, 0]

for i in range(4):
    temp[i] = 1
    result.append(temp[:])
    temp[i] = 0

print(result)
