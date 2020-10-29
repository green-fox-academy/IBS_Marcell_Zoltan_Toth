shop = {}

shop["Milk"] = 1.07
shop["Rice"] = 1.59
shop["Eggs"] = 3.14
shop["Cheese"] = 12.60
shop["Chicken Breasts"] = 9.40
shop["Apples"] = 2.31
shop["Tomato"] = 2.58
shop["Potato"] = 1.75
shop["Onion"] = 1.10

bob = {}

bob["Milk"] = 3
bob["Rice"] = 2
bob["Eggs"] = 2
bob["Cheese"] = 1
bob["Chicken Breasts"] = 4
bob["Apples"] = 1
bob["Tomato"] = 2
bob["Potato"] = 1

alice = {}

alice["Rice"] = 1
alice["Eggs"] = 5
alice["Chicken Breasts"] = 2
alice["Apples"] = 1
alice["Tomato"] = 10

bob_pays = 0

for b in bob.items():
    if b[0] in shop.keys():
        bob_pays += b[1] * shop.get(b[0])
print(bob_pays)

alice_pays = 0

for k,v in alice.items():
    if k in shop.keys():
        alice_pays += v * shop.get(k)
print(alice_pays)

if alice.get("Rice") > bob.get("Rice"):
    print("Alice buys more rice")
else:
    print("Bob buys more rice")

if "Potato" in alice.keys() and "Potato" in bob.keys():
    if alice.get("Potato") > bob.get("Potato"):
        print("Alice buys more potatoes")
    else:
        print("Bob buys more potatoes")
elif "Potato" not in alice.keys() and "Potato" in bob.keys():
    print("Bob buys more potatoes")
elif "Potato" in alice.keys() and "Potato" not in bob.keys():
    print("Alice buys more potatoes")
else:
    print("Noone bought any potatoes")


if sum(alice.values()) > sum(bob.values()):
    print("Alice buys more items")
elif sum(alice.values()) == sum(bob.values()):
    print("They buy the same amount of items")
else:
    print("Alice buys more items")

