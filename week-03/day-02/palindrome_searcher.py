def is_palindrome(word):
    if len(word) % 2 == 0:
        first = word[:len(word) // 2]
        second = word[len(word) // 2:]
        reverse_second = ""
        for i in range(len(second) - 1, -1, -1):
            reverse_second += second[i]
        if first == reverse_second:
            return True
        else:
            return False
    else:
        first = word[0:len(word) // 2]
        second = word[(len(word) + 1) // 2:]
        reverse_second = ""
        for i in range(len(second) - 1, -1, -1):
            reverse_second += second[i]
        if first == reverse_second:
            return True
        else:
            return False


#print(is_palindrome("dogod"))


def search_palindrome(input):
    output = []
    for i in range(0, len(input) - 3):
        for k in range(i + 3, len(input) +1):
            if is_palindrome(input[i:k]):
                output.append(input[i:k])
    return output



print(search_palindrome("dog goat dad duck doodle never"))


'''
word1 = "doggod"
print(len(word1)//2-1)
word1 = "Hello"
print(word1[0:2])
'''
