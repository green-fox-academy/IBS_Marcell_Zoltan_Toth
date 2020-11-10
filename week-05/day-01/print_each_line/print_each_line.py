try:
    with open("example.txt", "r") as file:
        buffer = file.readlines()
        for line in buffer:
            print(line)
except:
    print("There was an error / no such file")
