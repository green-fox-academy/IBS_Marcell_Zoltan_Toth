num = int(input("Give me a number!"))

stars = 1
spaces = int((num - 1) / 2)


if num % 2 == 0:
    print("For a diamond to be symmetrical the given number has to be odd!")
else:
    for i in range(1, num + 1):
        if i < int((num+1)/2):
            print((" " * spaces) + ("*" * stars) + (" " * spaces))
            stars += 2
            spaces -= 1
        else:
            print((" " * spaces) + ("*" * stars) + (" " * spaces))
            stars -= 2
            spaces += 1


