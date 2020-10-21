num = int(input("Give me a number!"))

for i in range(1, num+1):
    if i == 1 or i == num:
        print("%" * num)
    else:
        print("%" + (" " * (num - 2)) + "%")