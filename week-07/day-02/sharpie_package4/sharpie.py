class Sharpie:

    color = ""
    width = 0.0
    ink_amount = 0.0

    def __init__(self, color, width, ink_amount=100):
        self.color = color
        self.width = float(width)
        self.ink_amount = ink_amount

    def use(self):
        self.ink_amount -= 2

    def print_stats(self):
        print("color = " + self.color)
        print("width = " + str(self.width))
        print("ink_amount = " + str(self.ink_amount))
