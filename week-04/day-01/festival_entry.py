watchlist = []

security_alcohol_loot = 0

queue = [
    {'name': 'Amanda', 'alcohol': 10, 'guns': 1},
    {'name': 'Mark', 'alcohol': 0, 'guns': 0},
    {'name': 'Dolores', 'alcohol': 0, 'guns': 1},
    {'name': 'Wade', 'alcohol': 1, 'guns': 1},
    {'name': 'Anna', 'alcohol': 10, 'guns': 0},
    {'name': 'Rob', 'alcohol': 2, 'guns': 0},
    {'name': 'Joerg', 'alcohol': 20, 'guns': 0}
]

def security_check(people):
    global security_alcohol_loot
    got_in = []
    for i in people:
        if i.get("alcohol") != 0:
            security_alcohol_loot += i.get("alcohol")
        if i.get("guns") != 0:
            watchlist.append(i.get("name"))
            continue
        got_in.append(i.get("name"))
    return got_in



print(security_check(queue))
print(security_alcohol_loot)
print(watchlist)

            

'''
apples = 0

def increment_apples():
    apples += 1
'''
