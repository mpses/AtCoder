#!/usr/bin/env python3
dist = lambda a, b, c, p, q, r: abs(p - a) + abs(q - b) + max(0, r - c)
(n,), *d = [[*map(int, o.split())] for o in open(0)]
INF = float("inf")
dp = [[INF] * n for _ in [None] * (1 << n)]
dp[0][0] = 0
for i in range(1 << n):
    for j, (a, b, c) in enumerate(d):
        for k, (p, q, r) in enumerate(d):
            dp[i | (1 << k)][k] = min(dp[i | (1 << k)][k], dp[i][j] + dist(a, b, c, p, q, r))
print(dp[-1][0])