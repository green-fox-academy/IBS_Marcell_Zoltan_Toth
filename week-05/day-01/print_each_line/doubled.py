def undouble(filename):
    buffer_out = []
    buffer_in = []
    temp = ""
    with open(filename, "r") as file:
        buffer_in = file.readlines()

    for line in buffer_in:
        line.rstrip()
        for i in range(0,len(line),2):
            temp += line[i]
        #temp += "\n"
        buffer_out.append(temp)
        temp = ""

    with open (filename, "w") as file:
        for i in buffer_out:
            file.write(i)


undouble("zen_of_python.txt")

