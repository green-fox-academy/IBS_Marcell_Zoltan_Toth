num = int(input("Give me a number!"))

stars = 1
spaces = num - 1

while num != 0:
    print((" " * spaces) + ("*" * stars) + (" " * spaces))
    stars += 2
    spaces -= 1
    num -= 1
