girls = int(input("How many girls at the party?"))
boys = int(input("How many boys at the party?"))

if boys == girls and (boys + girls) > 20:
    print("This party is excellent!")
elif boys != girls and (boys + girls) > 20:
    print("Quite cool party")
elif (boys + girls) < 20:
    print("Average party...")
elif girls == 0:
    print("Sausage party")
