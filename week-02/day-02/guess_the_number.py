num = 8

while True:
    guess = int(input("What is your guess?"))

    if(guess < num):
        print("The stored number is higher!")
    elif(guess > num):
        print("The stored number is lower!")
    else:
        break

print("You found the number: " + str(guess))