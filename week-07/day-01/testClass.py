class test:

    static_count = 0
    count = 0

    def __init__(self, count=1):
        self.count = count



t = test(1)

print(t.static_count)
print(test.static_count)

t.static_count = 1

print(t.static_count)
print(test.static_count)

t2 = test(1)

print(t2.static_count)