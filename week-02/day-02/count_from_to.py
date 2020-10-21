first = int(input("Give me the first number"))
second = int(input("Give me the second number"))

if second <= first:
    print("The second number should be bigger!")
else:
    for i in range(first, second):
        print(i)