def copy_file(from_file, to_file):
    buffer = []
    try:
        with open(from_file, "r") as FR_file:
            buffer = FR_file.readlines()

        with open(to_file, "a+") as TO_file:
            for line in buffer:
                TO_file.write(line)

        return 1
    except:
        return 0


copy_file("example.txt", "copy_to.txt")