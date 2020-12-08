import random

class CAB:

    goal = 0
    game_state = False
    num_of_guesses = 0

    def __init__(self):
        self.goal = random.randint(1000,9999)
        self.game_state = True
        self.num_of_guesses = 0

    def guess(self, g):
        gss_str = []
        goal_str = []
        goal = [0,0,0,0]
        gues = [0,0,0,0]
        cows = 0
        bulls = 0


        for i in range(len(str(self.goal))):
            gss_str.append(g[i])
            goal_str.append(str(self.goal)[i])


        for i in range(len(goal_str)):
            for k in range(len(gss_str)):
                if goal[i] == 0:
                    if goal_str[i] == gss_str[k] and i == k:
                        goal[i] = 2
                        gues[k] = 2
                    elif goal_str[i] == gss_str[k] and i != k and gues[k] == 0:
                        goal[i] = 1
                        gues[k] = 1


        for i in gues:
            if i == 1:
                bulls += 1
            if i == 2:
                cows += 1

        if cows == 4:
            self.game_state = False


        return ("%s cows and %s bulls" % (cows, bulls))
