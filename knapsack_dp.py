# knapsack_dp.py

def knapsack(W, wt, val, n):


    # Create DP table (n+1) x (W+1)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:  # If item can fit in knapsack
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # The maximum value is stored in dp[n][W]
    max_value = dp[n][W]

    # Trace back selected items
    selected_items = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # Item i was included
            selected_items.append(i - 1)  # Store index of item
            w -= wt[i - 1]

    selected_items.reverse()
    return max_value, selected_items


# Example usage
if __name__ == "__main__":
    val = [60, 100, 120]   # values
    wt = [10, 20, 30]      # weights
    W = 50                 # capacity
    n = len(val)

    max_value, items = knapsack(W, wt, val, n)

    print("Maximum value in Knapsack =", max_value)
    print("Selected item indices:", items)
    print("Selected items (value, weight):")
    for i in items:
        print(f"Value={val[i]}, Weight={wt[i]}")
