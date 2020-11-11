def unique_ips(filename):
    buffer = []
    dict = {}
    with open(filename, "r") as file:
        buffer = file.readlines()
        buffer = [line.split() for line in buffer]

    for i in buffer:
        dict[i[5]] = 1

    print(len(dict))
    print(dict)
    return len(dict)

def ratio(filename):
    buffer = []
    get = 0
    post = 0
    with open(filename, "r") as file:
        buffer = file.readlines()
        buffer = [line.split() for line in buffer]

    for i in buffer:
        if i[6] == "GET":
            get += 1
        if i[6] == "POST":
            post += 1

    print(get/post)
    return get/post

unique_ips("logs.txt")
ratio("logs.txt")
