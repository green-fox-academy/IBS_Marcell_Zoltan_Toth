list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def check_nums(input):
    if 4 in input and 8 in input and 12 in input and 16 in input:
        return True
    else:
        return False


print(check_nums(list_of_numbers))