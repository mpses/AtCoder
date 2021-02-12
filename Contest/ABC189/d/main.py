#!/usr/bin/env python3
n = int(input())
dp = [[1, 1]] + [[0] * 2 for _ in [0] * 60]
# dp[i] := [y[i] を False にする x[i] までの場合の数, y[i] を True にする x[i] までの場合の数]
for i in range(n):
    s = input()
    if s == "AND":
        dp[i + 1][0] = dp[i][0] * 2 + dp[i][1]
        dp[i + 1][1] = dp[i][1]
    else:
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = dp[i][0] + dp[i][1] * 2
print(dp[n][1])