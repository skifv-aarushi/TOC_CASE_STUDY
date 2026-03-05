# run_experiments.py

import time
import random
import pandas as pd

from dataset import benchmark_dataset
from environment import GridWorld
from pfa_model import PFA
from pomdp_model import POMDP
from experiments import evaluate


# Make experiments reproducible
random.seed(42)

results = []

# store one fixed obstacle layout for each grid size
fixed_maps = {}

for config in benchmark_dataset:

    print("Running:", config["scenario"])

    grid_size = config["grid"]

    # -------------------------------------------------
    # Create ONE obstacle map per grid size
    # -------------------------------------------------
    if grid_size not in fixed_maps:

        base_env = GridWorld(
            size=grid_size,
            noise=config["noise"],
            obstacle_count=config["obstacles"]
        )

        fixed_maps[grid_size] = base_env.obstacles

    # -------------------------------------------------
    # Use the SAME obstacle layout for all noise levels
    # -------------------------------------------------
    env = GridWorld(
        size=grid_size,
        noise=config["noise"],
        obstacle_count=config["obstacles"],
        obstacles=fixed_maps[grid_size]
    )

    # ---------------------
    # PFA model
    # ---------------------
    pfa = PFA(env)

    start = time.time()
    pfa.value_iteration()
    pfa_time = time.time() - start

    pfa_result = evaluate(
        "PFA",
        env,
        pfa,
        trials=300,
        max_steps=config["steps"]
    )

    # ---------------------
    # POMDP model
    # ---------------------
    pomdp = POMDP(env)

    start = time.time()
    pomdp_result = evaluate(
        "POMDP",
        env,
        pomdp,
        trials=300,
        max_steps=config["steps"]
    )
    pomdp_time = time.time() - start

    # ---------------------
    # Store results
    # ---------------------
    results.append({
        "Scenario": config["scenario"],
        "Grid": grid_size,
        "Noise": config["noise"],

        "PFA Success": pfa_result["success_rate"],
        "PFA Steps": pfa_result["average_steps"],
        "PFA Runtime": round(pfa_time, 4),

        "POMDP Success": pomdp_result["success_rate"],
        "POMDP Steps": pomdp_result["average_steps"],
        "POMDP Runtime": round(pomdp_time, 4)
    })


# Convert results to table
df = pd.DataFrame(results)

print("\nResults\n")
print(df)

# Save dataset
df.to_csv("benchmark_results.csv", index=False)

print("\nSaved benchmark_results.csv")