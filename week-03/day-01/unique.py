def unique(arr):
    sol = []
    for i in arr:

        if len(sol) == 0:
            sol.append(i)
            continue

        for k in range(len(sol)):
            if sol[k] == i:
                break
            elif sol[k] == sol[-1] and sol[k] != i:
                sol.append(i)
    return sol

print(unique([1, 11, 34, 11, 52, 61, 1, 34]))