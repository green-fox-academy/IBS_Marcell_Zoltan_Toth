from fot_package7.fleet import Fleet
from fot_package7.thing import Thing

fleet = Fleet()
# - You have the `Thing` class
# - You have the `Fleet` class
# - You have the `fleet_of_things.py` file
# - Download those, use those
# - In the `fleet_of_things` file create a fleet
# - Achieve this output:
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

one = Thing("Get milk")
two = Thing("Remove the obstacles")
three = Thing("Stand up")
three.complete()
four = Thing("Eat lunch")
four.complete()

fleet.add(one)
fleet.add(two)
fleet.add(three)
fleet.add(four)

print(fleet)