#!/usr/bin/env python3
# 2次元累積和 S の [x1, x2) × [y1, y2) 総和
def ac2(s, x1, x2, y1, y2):
    return s[x2][y2] - s[x1][y2] - s[x2][y1] + s[x1][y1]

import numpy as np
from itertools import*
n = int(input())
D = np.array([[0]*-~n] + [[0]+[*map(int, input().split())] for _ in [None]*n])
D = np.cumsum(D, axis = 0)
D = np.cumsum(D, axis = 1)
dp = [0] * (n * n + 1)
for x1 in range(n):
    for i in range(1, n - x1 + 1):
        x2 = x1 + i
        for y1 in range(n):
            for j in range(1, n - y1 + 1):
                y2 = y1 + j
                dp[i*j] = max(dp[i*j], ac2(D, x1, x2, y1, y2))
*dp, = accumulate(dp, max)
for _ in [None] * int(input()):
    print(dp[int(input())])