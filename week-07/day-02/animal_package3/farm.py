from animal_package3.animal import Animal


class Farm:
    animals = []
    slots = 0

    def __init__(self, slots):
        self.slots = slots

    def breed(self):
        if self.slots > len(self.animals):
            self.animals.append(Animal())
        else:
            print("no free slots")

    def slaughter(self):

        die = Animal(100, 100)

        if len(self.animals) > 0:
            for i in self.animals:
                if i.hunger < die.hunger:
                    die = i

            self.animals.remove(die)

    def add(self,animal):
        self.animals.append(animal)