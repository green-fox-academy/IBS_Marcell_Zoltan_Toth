def decode(filename):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index = -1
    shift = index - 4
    buffer = ""
    buffer_raw = ""
    buffer_raw_list = []
    sol = ""

    with open(filename, "r") as file:
        buffer = file.read().replace("\n", "")


    with open(filename, "r") as file:
        buffer_raw = file.read()
        buffer_raw_list = list(buffer_raw)

    for i in range(len(alphabet)):
        if alphabet[i] == most_common_letter(buffer):
            index = i

    shift = abs(index - 4)

    for i in range(len(buffer_raw_list)):
        if alphabet.find(buffer_raw_list[i].lower()) != -1:
            sol += alphabet[alphabet.find(buffer_raw_list[i].lower()) - shift]
        elif buffer_raw_list[i] == "\n":
            sol += "\n"
        elif buffer_raw_list[i] == " ":
            sol += " "
        else:
            sol += "!"
    print(sol)
'''
    with open("decoded_lines.txt", "w") as file:
        file.write(buffer_raw)
'''






def most_common_letter(message):
    dict = {}
    max = 0
    letter = ""

    for ch in message:
        if ch != " ":
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1

    for i in dict.keys():
        if dict[i] > max:
            max = dict[i]
            letter = i

    return letter

decode("encoded_lines.txt")