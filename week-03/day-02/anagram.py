def is_anagram(word1, word2):
    if len(word1) == len(word2):
        list1 = []
        list2 = []
        for i in word1:
            list1.append(i)
        for i in word2:
            list2.append(i)
        for i in range(len(list1)-1, -1, -1):
            for k in range(len(list2)-1, -1, -1):
                if list1[i] == list2[k]:
                    list1.remove(list1[i])
                    list2.remove(list2[k])

        if len(list2) == 0 and len(list1) == 0:
            return True
        else:
            return False
    else:
        return False


print(is_anagram("dog", "god"))
