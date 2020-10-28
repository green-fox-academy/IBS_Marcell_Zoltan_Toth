def find_max(arr):
    maximum = arr[0]
    for i in arr:
        if i > maximum:
            maximum = i
    return maximum


def remove_element(num, arr):
    ref = arr[:]
    for i in range(len(arr) - 1):
        if num == arr[i]:
            ref[i] = []
    return ref


def bubble(arr):
    ref = arr[:]
    sol = []
    while len(ref) != 0:
        max_arr = find_max(ref)
        sol.append(max_arr)
        ref.remove(max_arr)

    return sol

def advanced_bubble(arr, is_desc):
    if is_desc == False:
        return bubble(arr)
    else:
        temp = bubble(arr)
        sol = []
        for i in range(len(temp) -1 , -1 , -1):
            sol.append(temp[i])
        return sol

#ex = [43, 12, 24, 9, 5]
#print(remove_element(12,ex))

print(advanced_bubble([43, 12, 24, 9, 5], False))
