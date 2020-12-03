class Station:

    gas_amount = 0

    def __init__(self, gas_amount=100):
        self.gas_amount = gas_amount

    def refill(self, car):

        gas_needed = car.capacity - car.gas_amount

        if gas_needed <= self.gas_amount:
            self.gas_amount -= gas_needed
            car.gas_amount += gas_needed
        else:
            car.gas_amount += self.gas_amount
            self.gas_amount = 0
