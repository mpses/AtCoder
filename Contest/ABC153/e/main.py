#!/usr/bin/env python3
def chmin(dp, i, *x):
    dp[i] = min(dp[i], *x)
INF = float("inf")

# dp[i] := min 消耗する魔力 to H -= i
h, n = map(int, input().split())
dp = [0] + [INF] * h
for _ in [None] * n:
    a, b = map(int, input().split())
    for j in range(h + 1):
        chmin(dp, min(j + a, h), dp[j] + b)
print(dp[h])
