class Counter:
    initial = 0
    count = 0

    def __init__(self, count=0):
        self.count = count
        self.initial = count


    def add(self, num=None):
        if num != None:
            self.count += num
        else:
            self.count += 1



    def get(self):
        return self.count

    def reset(self):
        self.count = self.initial

