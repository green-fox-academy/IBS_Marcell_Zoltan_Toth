class Sum:

    def sum(self, input):

        sol = 0

        if input is None:
            return sol
        else:
            for i in input:
                sol += i

            return sol



