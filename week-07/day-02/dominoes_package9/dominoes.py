from dominoes_package9.domino import Domino

def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes

dominoes = initialize_dominoes()
# You have the list of Dominoes
# Order them into one snake where the adjacent dominoes have the same numbers on their adjacent sides
# eg: [2, 4], [4, 3], [3, 5], [5, 2],

ordered_dominoes = []
size = len(dominoes)
ordered_dominoes.append(dominoes[0])
dominoes.pop(0)


while len(ordered_dominoes) != size:


    for i in dominoes:
        if ordered_dominoes[-1].values[1] == i.values[0]:
            ordered_dominoes.append(i)
            dominoes.remove(i)


dominoes[:] = ordered_dominoes
print(dominoes)
print(ordered_dominoes)