def fib(k, r):
    dp = [1, 1, 0]
    for i in range(k - 1):
        dp[2] = (dp[0] + dp[1]) % r
        dp[0], dp[1] = dp[1], dp[2]
    return dp[2]

print(fib(14, 600))