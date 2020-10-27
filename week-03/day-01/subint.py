def subint(number, array):
    ans = []
    div = 10
    for i in range(len(array)):
        digits = len(str(array[i]))
        if digits == 1 and number == array[i]:
            ans.append(i)
            continue
        else:
            for k in range(1, digits+1):
                if array[i] % div == number:
                    ans.append(i)
                    break
                else:
                    div *= 10
            div = 1
    return ans


t_num = 9
t_array = [1, 11, 34, 52, 61]
print(subint(t_num, t_array))