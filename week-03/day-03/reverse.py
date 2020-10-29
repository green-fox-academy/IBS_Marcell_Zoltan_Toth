toBeReversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"

def reverse_string(input):
    output = ""
    for i in range(len(input)-1, -1, -1):
        output += input[i]

    return output


print(reverse_string(toBeReversed))
