num = int(input("How many numbers?"))

sum = 0

for i in range(num):
    num2 = int(input("Give me number" + str(i+1) + "! "))
    sum += num2

print("Sum: " + str(sum) + ", Average: " + str(sum/num))