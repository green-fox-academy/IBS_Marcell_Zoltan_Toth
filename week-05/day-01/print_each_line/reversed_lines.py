def reverse_lines(filename):
    buffer_in = []
    buffer_out = []
    with open(filename, "r") as file:
        buffer_in = file.readlines()


    for i in buffer_in:
        i.rstrip()
        i = i[::-1]
        #i += "\n"
        buffer_out.append(i)


    with open(filename, "w") as file:
        for i in buffer_out:
            file.write(i)


reverse_lines("reversed_zen")