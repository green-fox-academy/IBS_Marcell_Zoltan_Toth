class Fibo:

    def num_fibonacci(self, index):

        if index == 1:
            return 1

        if index == 2:
            return 1

        numbers = [1,1]

        while len(numbers) != index:
            numbers.append(numbers[-1] + numbers[-2])

        return numbers[-1]
