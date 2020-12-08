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
        g_str = str(g)
        goal_str = str(self.goal)

        


