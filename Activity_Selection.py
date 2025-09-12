def activity_selection(start, finish):
    """Solve Activity Selection Problem using Greedy approach."""

    n = len(start)
    activities = list(zip(start, finish))
    activities.sort(key=lambda x: x[1])  # Sort by finish time

    selected = []
    last_finish = 0

    for i in range(n):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]

    return selected


# Example usage
if __name__ == "__main__":
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]

    selected_activities = activity_selection(start, finish)

    print("Selected Activities (start, finish):")
    for act in selected_activities:
        print(act)
