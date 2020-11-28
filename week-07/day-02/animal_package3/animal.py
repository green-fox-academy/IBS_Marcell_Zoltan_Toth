class Animal:

    hunger = 0
    thirst = 0

    def __init__(self, hunger=50, thirst=50):
        self.hunger = hunger
        self.thirst = thirst

    def eat(self):
        self.hunger -= 1

    def drink(self):
        self.thirst -= 1

    def play(self):
        self.hunger += 1
        self.thirst += 1

    def print_stats(self):
        print("hunger = " + str(self.hunger))
        print("thirst = " + str(self.thirst))


