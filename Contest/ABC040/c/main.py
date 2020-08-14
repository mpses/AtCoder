#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
INF = float("inf")
dp = [INF] * n
dp[0] = 0
for i in range(1, n):
    dp[i] = min(dp[i - p] + abs(a[i - p] - a[i]) for p in [1, 2])
print(dp[n - 1])