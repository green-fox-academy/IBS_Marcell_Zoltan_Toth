from cows_and_bulls_pckg.cab import CAB

ex = CAB()

while ex.game_state:
    tipp = str(input("Give me a guess!"))

    if tipp is str and len(tipp) == 4:
        print(ex.guess(tipp))
    else:
        print("Incorrect input")