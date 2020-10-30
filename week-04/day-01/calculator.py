exp = str(input("please type in the expression"))

def calculate(exp):
    words = exp.split()
    if words[0] == "+":
        return int(words[1]) + int(words[2])
    elif words[0] == "-":
        return int(words[1]) - int(words[2])
    elif words[0] == "*":
        return int(words[1]) * int(words[2])
    elif words[0] == "/":
        return int(words[1]) / int(words[2])
    elif words[0] == "%":
        return int(words[1]) % int(words[2])
    else:
        print("invalid operation")
        return 0

print(calculate(exp))




