def write_multiple_lines(filename, word, count):
    try:
        with open(filename, "w") as file:
            for i in range(count):
                file.write(word + "\n")
    except:
        print("Something went wrong! You might want to double check that !")

write_multiple_lines("example2.txt", "apple", 5)