def create_palindrome(word):
    reverse = ""
    for i in range(len(word)-1, -1, -1):
        reverse += word[i]
    print(word + reverse)



create_palindrome("greenfox")