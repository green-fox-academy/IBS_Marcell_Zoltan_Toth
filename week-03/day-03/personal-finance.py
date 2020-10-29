expenses = [500, 1000, 1250, 175, 800, 120]

def calculator(command, spending):

    ret = 0

    if command == "sum":
        for i in spending:
            ret += i
        return ret

    elif command == "avg":
        for i in spending:
            ret += i
        return ret / len(spending)

    elif command == "min":
        ret = spending[0]
        for i in spending:
            if ret < i:
                ret = i
        return ret

    elif command == "max":
        ret = spending[0]
        for i in spending:
            if ret > i:
                ret = i
        return ret
    else:
        print("Invalid command! Only: sum ,avg, min, max")


print(sum(expenses))
print(max(expenses))
print(min(expenses))
print(sum(expenses) / len(expenses))
