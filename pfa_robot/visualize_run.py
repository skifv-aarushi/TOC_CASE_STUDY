# visualize_run.py

import time
import matplotlib.pyplot as plt
import numpy as np

from environment import GridWorld
from pfa_model import PFA


def draw_grid(env, robot_pos):

    grid = np.zeros((env.size, env.size))

    # obstacles
    for o in env.obstacles:
        grid[o] = -1

    # goal
    grid[env.goal] = 2

    # robot
    grid[robot_pos] = 1

    plt.clf()

    plt.imshow(grid, cmap="coolwarm", origin="upper")

    plt.title("Robot Navigation Simulation")

    plt.xticks(range(env.size))
    plt.yticks(range(env.size))

    plt.grid(True)

    plt.pause(0.3)


def simulate():

    env = GridWorld(size=10, noise=0.05, obstacle_count=7)

    pfa = PFA(env)
    pfa.value_iteration()

    state = env.start

    plt.figure(figsize=(6,6))

    for step in range(200):

        draw_grid(env, state)

        if state == env.goal:
            print("Goal reached in", step, "steps")
            break

        action = pfa.best_action(state)

        state = env.move(state, action)

    plt.show()


if __name__ == "__main__":
    simulate()