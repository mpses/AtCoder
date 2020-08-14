#!/usr/bin/env python3
n, *h = map(int, open(0).read().split())
dp = [0] * n
dp[0] = 0
a = abs

for i in range(1, n):
    dp[i] = min(dp[i], dp[i-1] + a(h[i] - h[i-1]))
    dp[i+1] = min(dp[i+1], dp[i-1] + a(h[i] - h[i-2]))
print(dp[n-1])
