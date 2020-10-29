map = {}

map["William A. Lathan"] = "405-709-1865"
map["John K. Miller"] = "402-247-8568"
map["Hortensia E. Foster"] = "606-481-6467"
map["Amanda D. Newland"] = "319-243-5613"
map["Brooke P. Askew"] = "307-687-2982"


print(map["John K. Miller"])

for k,v in map.items():
    if v == "307-687-2982":
        print(k)
        break

if "Chris E. Myer" in map:
    print("We have the phone number of Chris E. Myer")
else:
    print("We do not have the phone number of Chris E. Myer")