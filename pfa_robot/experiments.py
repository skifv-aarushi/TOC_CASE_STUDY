# experiments.py

def evaluate(model_type, env, model, trials=300, max_steps=200):

    successes = 0
    total_steps = 0

    for _ in range(trials):

        state = env.start

        for step in range(max_steps):

            if model_type == "PFA":
                action = model.best_action(state)
            else:
                action = model.choose_action(state)

            state = env.move(state, action)

            if state == env.goal:
                successes += 1
                total_steps += step + 1
                break

    success_rate = successes / trials

    # avoid dividing by zero
    if successes > 0:
        average_steps = total_steps / successes
    else:
        average_steps = max_steps

    return {
        "success_rate": round(success_rate, 3),
        "average_steps": round(average_steps, 2)
    }