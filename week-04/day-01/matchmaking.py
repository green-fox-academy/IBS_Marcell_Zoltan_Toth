girls = ["Eve", "Ashley", "Claire", "Kat", "Jane"]
boys = ["Joe", "Fred", "Tom", "Todd", "Neef", "Jeff", "Kyle", "Stan", "Cartman"]

def mix(first, second):
    sol = []
    index = 0
    while len(first)  > index and len(second)  > index:
        sol.append(first[index])
        sol.append(second[index])
        index += 1

    if len(first) -1 > index:
        sol += first[index:]

    if len(second) -1 > index:
        sol += second[index:]

    return sol

mixed_list = mix(girls, boys)
print(mixed_list)