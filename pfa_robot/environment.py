# environment.py

import random


class GridWorld:

    def __init__(self, size=10, noise=0.1, obstacle_count=7, obstacles=None):

        self.size = size
        self.noise = noise

        self.start = (0, 0)
        self.goal = (size - 1, size - 1)

        # movement actions
        self.actions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

        # if obstacles provided, reuse them
        if obstacles is not None:
            self.obstacles = obstacles
        else:
            self.obstacles = self.generate_obstacles(obstacle_count)

    def generate_obstacles(self, count):

        obstacles = set()

        while len(obstacles) < count:

            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)

            cell = (x, y)

            if cell != self.start and cell != self.goal:
                obstacles.add(cell)

        return obstacles

    def valid(self, state):

        return (
            0 <= state[0] < self.size
            and 0 <= state[1] < self.size
            and state not in self.obstacles
        )

    def move(self, state, action):

        # stochastic slip
        if random.random() < self.noise:
            return state

        dx, dy = self.actions[action]
        next_state = (state[0] + dx, state[1] + dy)

        if self.valid(next_state):
            return next_state

        return state