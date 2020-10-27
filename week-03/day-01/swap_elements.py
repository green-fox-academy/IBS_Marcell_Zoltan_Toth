orders = ["first", "second", "third"]

temp = orders[0]
orders[0] = orders[2]
orders[2] = temp

print(orders)
