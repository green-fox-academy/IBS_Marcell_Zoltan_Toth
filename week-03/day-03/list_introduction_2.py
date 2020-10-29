List_A = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]
List_B = List_A[:]

if "Durian" in List_A:
    print("There is Durian in List_A")
else:
    print("No Durian in List_A")

List_B.remove("Durian")

List_A.insert(4, "Kiwifruit")

if len(List_B) > len(List_A):
    print("List_B is longer")
else:
    print("List_A is longer")

index_Avocado = List_A.index("Avocado")

if "Durian" in List_B:
    index_Durian = List_B.index("Durian")

List_B += ["Passion Fruit", "Pomelo"]
print(List_B)

print(List_A[2])