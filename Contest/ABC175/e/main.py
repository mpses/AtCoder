#!/usr/bin/env python3
(R, C, K), *D = [[*map(int,o.split())] for o in open(0)]
V = [[0] * C for _ in [None] * R]
for r, c, v in D:
    V[r - 1][c - 1] = v

dp = [[[-1] * C for _ in [None] * R] for _ in [None] * 4]

dp[0][0][0] = 0
for r in range(R):
    for c in range(C):
        v = V[r][c]
        for i in range(4):
            if dp[i][r][c] > -1:
                if r < R - 1:
                    dp[0][r + 1][c] = max(dp[0][r + 1][c], dp[i][r][c])
                if c < C - 1:
                    dp[i][r][c + 1] = max(dp[i][r][c + 1], dp[i][r][c])
                if i < 3 and v:
                    if r < R - 1:
                        dp[0][r + 1][c] = max(dp[0][r + 1][c], dp[i][r][c] + v)
                    if c < C - 1:
                        dp[i + 1][r][c + 1] = max(dp[i + 1][r][c + 1], dp[i][r][c] + v)

v = V[R - 1][C - 1]
ans = dp[3][R - 1][C - 1]
for i in range(3):
    ans = max(ans, dp[i][R - 1][C - 1] + v)
print(ans)