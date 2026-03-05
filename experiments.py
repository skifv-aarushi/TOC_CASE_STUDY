from metrics import compute_metrics


def evaluate(model_type, env, model, trials=300, max_steps=70):

    results = []

    for _ in range(trials):

        state = env.start
        belief = {env.start: 1.0}
        steps = 0

        while steps < max_steps and state != env.goal:

            if model_type == "PFA":
                action = model.best_action(state)
            else:
                action = model.choose_action(belief)

            next_state = env.move(state, action)

            if model_type == "POMDP":
                observation = next_state
                belief = model.belief_update(belief, action, observation)

            state = next_state
            steps += 1

        results.append({
            "success": state == env.goal,
            "steps": steps
        })

    return compute_metrics(results)