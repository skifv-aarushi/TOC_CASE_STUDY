import random


class POMDP:

    def __init__(self, env):
        self.env = env
        self.actions = list(env.actions.keys())

    def belief_update(self, belief, action, observation):

        new_belief = {}

        for state, prob in belief.items():

            dx, dy = self.env.actions[action]
            next_state = (state[0] + dx, state[1] + dy)

            if not self.env.valid(next_state):
                next_state = state

            # transition model (same as environment)
            transition_prob = 1 - self.env.noise

            predicted_prob = prob * transition_prob

            # observation likelihood
            if next_state == observation:
                likelihood = 0.8
            else:
                likelihood = 0.2

            new_belief[next_state] = new_belief.get(next_state, 0) + predicted_prob * likelihood

        total = sum(new_belief.values())

        if total == 0:
            return {self.env.start: 1.0}

        for s in new_belief:
            new_belief[s] /= total

        return new_belief

    def choose_action(self, belief):

        goal = self.env.goal
        best_action = None
        best_score = float("-inf")

        for action in self.actions:

            dx, dy = self.env.actions[action]
            score = 0

            for state, prob in belief.items():

                next_state = (state[0] + dx, state[1] + dy)

                if not self.env.valid(next_state):
                    next_state = state

                distance = abs(next_state[0] - goal[0]) + abs(next_state[1] - goal[1])

                score -= prob * distance

            if score > best_score:
                best_score = score
                best_action = action

        if best_action is None:
            return random.choice(self.actions)

        return best_action