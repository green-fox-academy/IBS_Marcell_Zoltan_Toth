map = {}

map["978-1-60309-452-8"] = "A Letter to Jo"
map["978-1-60309-459-7"] = "Lupus"
map["978-1-60309-444-3"] = "Red Panda and Moon Bear"
map["978-1-60309-461-0"] = "The Lab"

for k,v in map.items():
    print(v + " (ISBN: " + k + ")")


del map["978-1-60309-444-3"]



for k,v in map.items():
    if v == "The Lab":
        del map[k]
        break


map["978-1-60309-450-4"] = "They Called Us Enemy"
map["978-1-60309-453-5"] = "Why Did We Trust Him?"

if "478-0-61159-424-8" in map.keys():
    print("There is a 478-0-61159-424-8 in map")
else:
    print("No 478-0-61159-424-8 in map")


print(map.get("978-1-60309-453-5"))
