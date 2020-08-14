#!/usr/bin/env python3
from itertools import*
n, *t = map(int, open(0))
m = INF = float("inf")
for i in product([0, 1], repeat=n):
    s = [0, 0]
    for j, k in enumerate(i):
        s[k] += t[j]
    m = min(m, max(s))
print(m)