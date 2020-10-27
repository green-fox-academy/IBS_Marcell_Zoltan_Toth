def factorio(num):
    ans = 1
    for i in range(1, num+1):
        ans *= i
    return ans


print(factorio(4))