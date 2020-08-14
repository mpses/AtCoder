#!/usr/bin/env python3
n, m = map(int, input().split())
a = set([int(input()) for _ in range(m)])

mod = 10**9+7

dp = [0] * -~n
dp[0] = 1
dp[1] = 0 + (1 not in a)

for i in range(2, -~n):
    if i in a:
        continue
    dp[i] = (dp[i - 1] + dp[i - 2]) % mod

print(dp[n])