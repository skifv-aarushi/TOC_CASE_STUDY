# pomdp_model.py

import random


class POMDP:

    def __init__(self, env):

        self.env = env
        self.actions = list(env.actions.keys())

    def choose_action(self, state):

        goal = self.env.goal

        best_action = None
        best_score = float("-inf")

        for action in self.actions:

            dx, dy = self.env.actions[action]
            next_state = (state[0] + dx, state[1] + dy)

            distance = abs(next_state[0] - goal[0]) + abs(next_state[1] - goal[1])

            score = -distance

            if score > best_score:
                best_score = score
                best_action = action

        return best_action