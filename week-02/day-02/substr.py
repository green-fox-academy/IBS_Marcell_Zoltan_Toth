str = "this is what I'm searching in"
keyword = "sss"

def substr(str, keyword):
    index = 0
    temp = ""
    key_length = len(keyword)
    str_length = len(str)
    match = False

    for i in range(0, str_length-key_length):
        index = i
        for k in range(key_length):
            if str[i+k] != keyword[k]:
                break
            elif k == key_length-1:
                match = True
        if match:
            return index

    return -1

sol = substr(str, keyword)
print(sol)