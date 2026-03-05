def compute_metrics(results):

    total_trials = len(results)

    if total_trials == 0:
        return {
            "success_rate": 0,
            "average_steps": 0
        }

    successes = sum(1 for r in results if r["success"])
    total_steps = sum(r["steps"] for r in results)

    success_rate = successes / total_trials
    average_steps = total_steps / total_trials

    return {
        "success_rate": round(success_rate, 3),
        "average_steps": round(average_steps, 2)
    }