from environment import GridWorld
from pfa_model import PFA
from pomdp_model import POMDP
from experiments import evaluate
from visualization import plot_results


noise_levels = [0.02, 0.05, 0.07,0.1]

pfa_results = []
pomdp_results = []

base_env = GridWorld(noise=0.05)
fixed_obstacles = base_env.obstacles


for noise in noise_levels:

    env = GridWorld(noise=noise)
    env.obstacles = fixed_obstacles

    # ----- PFA -----
    pfa = PFA(env)
    pfa.value_iteration()

    pfa_result = evaluate("PFA", env, pfa)
    pfa_results.append(pfa_result)

    # ----- POMDP -----
    pomdp = POMDP(env)
    pomdp_result = evaluate("POMDP", env, pomdp)
    pomdp_results.append(pomdp_result)

    print("Noise:", noise)
    print("PFA:", pfa_result)
    print("POMDP:", pomdp_result)
    print()


plot_results(noise_levels, pfa_results, pomdp_results)