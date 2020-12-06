
class Anagram:

    def is_anagram(self, word1, word2):

        if word1 == "" or word2 == "":
            return False

        if len(word1) != len(word2):
            return False

        dict1 = {}
        dict2 = {}

        for i in range(len(word1)):

            if word1[i] not in dict1:
                dict1[word1[i]] = 1
            else:
                dict1[word1[i]] += 1

            if word2[i] not in dict2:
                dict2[word2[i]] = 1
            else:
                dict2[word2[i]] += 1

        for k, v in dict1.items():
            if k not in dict2.keys():
                return False
            else:
                if v != dict2[k]:
                    return False


        return True


