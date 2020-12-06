class Count:

    def count_letters(self, input):

        dict = {}

        if input == "":
            return dict

        for i in range(len(input)):
            if input[i] not in dict.keys():
                dict[input[i]] = 1
            else:
                dict[input[i]] += 1


        return dict

