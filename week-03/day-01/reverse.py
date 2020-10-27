numbers = [3, 4, 5, 6, 7]
ans = []

for i in range(len(numbers)-1, -1, -1):
    ans.append(numbers[i])

numbers = ans[:]
print(numbers)
