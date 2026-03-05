# pfa_model.py

class PFA:

    def __init__(self, env):

        self.env = env

        self.states = [
            (i, j)
            for i in range(env.size)
            for j in range(env.size)
            if env.valid((i, j))
        ]

        self.actions = list(env.actions.keys())

        self.transition_prob = {}

        self.build_model()

    def build_model(self):

        for s in self.states:

            self.transition_prob[s] = {}

            for a in self.actions:

                probs = {}

                dx, dy = self.env.actions[a]
                intended = (s[0] + dx, s[1] + dy)

                if not self.env.valid(intended):
                    intended = s

                probs[intended] = 1 - self.env.noise

                other_actions = [x for x in self.actions if x != a]
                slip_prob = self.env.noise / len(other_actions)

                for oa in other_actions:

                    odx, ody = self.env.actions[oa]
                    alt = (s[0] + odx, s[1] + ody)

                    if not self.env.valid(alt):
                        alt = s

                    probs[alt] = probs.get(alt, 0) + slip_prob

                self.transition_prob[s][a] = probs

    def value_iteration(self, gamma=0.9, threshold=1e-5):

        V = {s: 0 for s in self.states}

        V[self.env.goal] = 1

        while True:

            delta = 0
            newV = V.copy()

            for s in self.states:

                if s == self.env.goal:
                    continue

                values = []

                for a in self.actions:

                    val = sum(
                        prob * V[s2]
                        for s2, prob in self.transition_prob[s][a].items()
                    )

                    values.append(val)

                newV[s] = max(values)

                delta = max(delta, abs(newV[s] - V[s]))

            V = newV

            if delta < threshold:
                break

        self.V = V

    def best_action(self, state):

        best_a = None
        best_val = -1

        for a in self.actions:

            val = sum(
                prob * self.V[s2]
                for s2, prob in self.transition_prob[state][a].items()
            )

            if val > best_val:
                best_val = val
                best_a = a

        return best_a