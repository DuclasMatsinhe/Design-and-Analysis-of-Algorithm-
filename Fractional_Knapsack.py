class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # value-to-weight ratio


def fractional_knapsack(capacity, values, weights):
    """Solve the Fractional Knapsack Problem using Greedy approach."""

    # Step 1: Create items and sort them by value-to-weight ratio (descending)
    items = [Item(values[i], weights[i]) for i in range(len(values))]
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0
    fractions = []

    # Step 2: Pick items one by one
    for item in items:
        if capacity >= item.weight:
            # Take the whole item
            capacity -= item.weight
            total_value += item.value
            fractions.append((item.value, item.weight, 1))  # 100% taken
        else:
            # Take a fraction of the item
            fraction = capacity / item.weight
            total_value += item.value * fraction
            fractions.append((item.value, item.weight, fraction))  # fraction taken
            break  # Knapsack is full

    return total_value, fractions


# Example usage
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    max_value, chosen_items = fractional_knapsack(capacity, values, weights)

    print("Maximum value in Knapsack =", max_value)
    print("\nItems taken (value, weight, fraction):")
    for val, wt, frac in chosen_items:
        print(f"Value={val}, Weight={wt}, Fraction taken={frac:.2f}")
