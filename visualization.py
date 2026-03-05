import matplotlib.pyplot as plt


def plot_results(noise_levels, pfa_results, pomdp_results):

    pfa_success = [r["success_rate"] for r in pfa_results]
    pomdp_success = [r["success_rate"] for r in pomdp_results]

    plt.figure()

    plt.plot(noise_levels, pfa_success, marker="o", label="PFA")
    plt.plot(noise_levels, pomdp_success, marker="s", label="POMDP")

    plt.xlabel("Noise Level")
    plt.ylabel("Success Rate")
    plt.title("PFA vs POMDP Performance")

    plt.legend()
    plt.grid(True)

    plt.show()