def reverse_order(filename):
    buffer_in = []

    with open(filename, "r") as file:
        buffer_in = file.readlines()


    with open(filename, "w") as file:
        for i in range(len(buffer_in)-1, -1, -1):
            file.write(buffer_in[i])


reverse_order("reversed_order_zen.txt")