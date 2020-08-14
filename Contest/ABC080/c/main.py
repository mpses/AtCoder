#!/usr/bin/env python3
import numpy as np
n = int(input())
f = [list(map(int, input().split())) for _ in [0]*n]
p = [list(map(int, input().split())) for _ in [0]*n]
INF = float("inf")
m = -INF
from itertools import*
for j in product([0, 1], repeat=10):
    if sum(j) == 0:
        continue
    t = 0
    for i, k in enumerate(f):
        t += p[i][sum(np.array(j) & np.array(k))]
    m = max(t, m)
print(m)