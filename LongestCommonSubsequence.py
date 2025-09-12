# lcs.py

def lcs(X, Y):
    """Return length of LCS and the LCS string using Dynamic Programming."""
    m, n = len(X), len(Y)

    # Create DP table (m+1 x n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct LCS string from DP table
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], ''.join(reversed(lcs_str))


# Example usage
if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"

    length, sequence = lcs(X, Y)

    print("String 1:", X)
    print("String 2:", Y)
    print("Length of LCS:", length)
    print("LCS:", sequence)
