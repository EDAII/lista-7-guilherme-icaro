def unbounded_knapsack(w, n, V, W):

    dp = [0 for i in range(w + 1)]

    ans = 0

    for i in range(w + 1):
        for j in range(n):
            if (W[j] <= i):
                dp[i] = max(dp[i], dp[i - W[j]] + V[j])

    return dp[w]
