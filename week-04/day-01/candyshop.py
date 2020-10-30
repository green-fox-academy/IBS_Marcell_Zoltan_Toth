shop_items = ["Cupcake", 2, "Brownie", False]
shop_items[1] = "Croissant"
shop_items[3] = "Ice Cream"

def sweets(input):
    for i in input:
        print(i)

sweets(shop_items)