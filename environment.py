import random
from collections import deque


class GridWorld:

    def __init__(self, size=10, noise=0.1, obstacle_count=7):

        self.size = size
        self.noise = noise

        self.start = (0, 0)
        self.goal = (size - 1, size - 1)

        self.actions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

        # Generate obstacles until a valid path exists
        self.obstacles = self.generate_valid_obstacles(obstacle_count)

    def generate_valid_obstacles(self, count):

        while True:

            obstacles = set()

            while len(obstacles) < count:

                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)

                cell = (x, y)

                if cell != self.start and cell != self.goal:
                    obstacles.add(cell)

            if self.path_exists(obstacles):
                return obstacles

    def path_exists(self, obstacles):

        visited = set()
        queue = deque([self.start])

        while queue:

            x, y = queue.popleft()

            if (x, y) == self.goal:
                return True

            if (x, y) in visited:
                continue

            visited.add((x, y))

            for dx, dy in self.actions.values():

                nx, ny = x + dx, y + dy

                if (
                    0 <= nx < self.size
                    and 0 <= ny < self.size
                    and (nx, ny) not in obstacles
                ):
                    queue.append((nx, ny))

        return False

    def valid(self, state):

        return (
            0 <= state[0] < self.size
            and 0 <= state[1] < self.size
            and state not in self.obstacles
        )

    def move(self, state, action):

        if random.random() < self.noise:
            return state

        dx, dy = self.actions[action]
        next_state = (state[0] + dx, state[1] + dy)

        if self.valid(next_state):
            return next_state

        return state