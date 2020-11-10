def write_single_line(file_name):
    try:
        with open(file_name, "a+") as file:
            file.write("Marcell Zoltan Toth\n")
    except:
        print("Unable to write file: " + file_name)




write_single_line("example.txt")