line_even = "% % % % "
line_odd = " % % % %"

for i in range(8):
    if(i % 2 == 0):
        print(line_even)
    else:
        print(line_odd)