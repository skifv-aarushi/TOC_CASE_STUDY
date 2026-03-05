# plot_graphs.py

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("benchmark_results.csv")


# ------------------------------------------------
# Success Rate vs Noise
# ------------------------------------------------

noise_group = df.groupby("Noise").mean(numeric_only=True)

plt.figure(figsize=(8,5))

plt.plot(
    noise_group.index,
    noise_group["PFA Success"],
    marker="o",
    linewidth=2,
    label="PFA"
)

plt.plot(
    noise_group.index,
    noise_group["POMDP Success"],
    marker="s",
    linewidth=2,
    label="POMDP"
)

plt.title("Success Rate vs Noise Level")
plt.xlabel("Noise Level")
plt.ylabel("Success Rate")

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

plt.tight_layout()
plt.savefig("success_vs_noise.png")
plt.show()



# ------------------------------------------------
# Average Steps vs Grid Size
# ------------------------------------------------

grid_group = df.groupby("Grid").mean(numeric_only=True)

plt.figure(figsize=(8,5))

plt.plot(
    grid_group.index,
    grid_group["PFA Steps"],
    marker="o",
    linewidth=2,
    label="PFA"
)

plt.plot(
    grid_group.index,
    grid_group["POMDP Steps"],
    marker="s",
    linewidth=2,
    label="POMDP"
)

plt.title("Average Steps vs Environment Size")
plt.xlabel("Grid Size")
plt.ylabel("Average Steps to Goal")

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

plt.tight_layout()
plt.savefig("steps_vs_grid.png")
plt.show()



# ------------------------------------------------
# Runtime Comparison
# ------------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    df["Scenario"],
    df["PFA Runtime"],
    label="PFA"
)

plt.bar(
    df["Scenario"],
    df["POMDP Runtime"],
    bottom=df["PFA Runtime"],
    label="POMDP"
)

plt.title("Runtime Comparison Across Scenarios")
plt.xlabel("Scenario")
plt.ylabel("Runtime (seconds)")

plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.legend()

plt.tight_layout()
plt.savefig("runtime_comparison.png")
plt.show()



# ------------------------------------------------
# Memory Usage Graph
# ------------------------------------------------

grid_sizes = [5,10,15]

states = [g*g for g in grid_sizes]

pfa_memory = states
pomdp_memory = [s*1.5 for s in states]

plt.figure(figsize=(8,5))

plt.plot(grid_sizes, pfa_memory, marker="o", linewidth=2, label="PFA")
plt.plot(grid_sizes, pomdp_memory, marker="s", linewidth=2, label="POMDP")

plt.title("Memory Usage vs Environment Size")
plt.xlabel("Grid Size")
plt.ylabel("Memory Units (Approximate)")

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

plt.tight_layout()
plt.savefig("memory_vs_grid.png")
plt.show()