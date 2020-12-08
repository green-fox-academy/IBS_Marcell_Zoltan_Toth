def add(a, b):
    return a + b

def max_of_three(a, b, c):
    return max(a,b,c)

def median(pool):
    pool.sort()
    return pool[int((len(pool) - 1) / 2)]

def is_vovel(char):
    if char in ['a', 'u', 'o', 'e', 'i']:
        return True
    else:
        return False

def translate(hungarian):

    if hungarian == "":
        return ""

    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve

# Check out the folder. There's a work file and a test file.

#  -  Run the tests, all 10 should be green (passing).
#  -  The implementations though are not quite good.
#  -  Create tests that'll fail, and will show how the implementations are wrong(You can assume that the implementation of join and split are good)
#  -  After creating the tests, fix the implementations
#  -  Check again, if you can create failing tests
#  -  Implement if needed