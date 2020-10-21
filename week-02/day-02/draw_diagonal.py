num = int(input("Give me a number!"))

for i in range(1, num+1):
    if i == 1 or i == num:
        print("%" * num)
    else:
        l = list(("%") + (" " * (num-2)) + ("%"))
        l[i-1] = "%"
        print("".join(l))

#Solving this without using a list was just toooo painful. 