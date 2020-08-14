#!/usr/bin/env python3
n, m = map(int, input().split())
from itertools import product
S = [{i} for i in range(n + 1)]
for _ in [0] * m:
    x, y = map(int, input().split())
    S[x] |= {y}
    S[y] |= {x}
M = 0
for i in product((0, 1), repeat = n):
    l = {k for k, j in enumerate(i, 1) if j}
    if all(S[p] >= l for p in l):
        M = max(M, len(l))
print(M)