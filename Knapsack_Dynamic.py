# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 08:40:15 2025

@author: DUCLAS MATSINHE
"""

# Returns the maximum value that
# can be put in a knapsack of capacity W
def knapsackRec(W, val, wt, n, memo):

    # Base Case
    if n == 0 or W == 0:
        return 0

    if memo[n][W] != -1:
        return memo[n][W]

    pick = 0

   
    if wt[n - 1] <= W:
        pick = val[n - 1] + knapsackRec(W - wt[n - 1], val, wt, n - 1, memo)

    # Don't pick the nth item
    notPick = knapsackRec(W, val, wt, n - 1, memo)

    # Store the result in memo[n][W] and return it
    memo[n][W] = max(pick, notPick)
    return memo[n][W]

def knapsack(W, val, wt):
    n = len(val)

    # Memoization table to store the results
    memo = [[-1] * (W + 1) for _ in range(n + 1)]

    return knapsackRec(W, val, wt, n, memo)

if __name__ == "__main__":
    val = [1, 2, 3]
    wt = [4, 5, 1]
    W = 4

    print(knapsack(W, val, wt))