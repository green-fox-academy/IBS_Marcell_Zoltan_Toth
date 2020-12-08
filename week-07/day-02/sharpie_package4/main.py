from sharpie import Sharpie
from sharpie_set import SharpieSet

first = Sharpie("Blue", 1, 200)
second = Sharpie("Red", 3.45, 30)
third = Sharpie("Green", 5, 0)
fourth = Sharpie("Yellow", 2, 21)

set = SharpieSet()
set.add(first)
set.add(second)
set.add(third)
set.add(fourth)

set.print()
print("usable: " + str(set.count_usable()))
set.remove_trash()
set.print()





