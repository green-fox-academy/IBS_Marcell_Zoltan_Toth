words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]

def quote_swap(words):
    temp = words[2]
    words[2] = words[5]
    words[5] = temp
    out = ""

    for i in words:
        out += i + " "

    print(out)

quote_swap(words)