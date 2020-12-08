class SharpieSet:
    sharpies = []

    def __init__(self):
        self.sharpies = []


    def add(self, sharpie):
        self.sharpies.append(sharpie)

    def count_usable(self):
        count = 0
        for i in self.sharpies:
            if i.ink_amount != 0:
                count += 1

        return count

    def remove_trash(self):

        for i in range(len(self.sharpies)-1, -1, -1):
            if self.sharpies[i].ink_amount == 0.0:
                self.sharpies.pop(i)

    def print(self):
        for i in self.sharpies:
            i.print_stats()
