verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"

def create_new_verbs(verbs, preverbs):
    for i in verbs:
        print(preverbs + i)

create_new_verbs(verbs, preverb)