

def count_lines(name):
    try:
        counter = 0
        with open(name, "r") as file:
            lines = file.readlines()
            for line in lines:
                counter += 1
        return counter

    except:
        return 0

out = count_lines("example.txt")
print(out)
