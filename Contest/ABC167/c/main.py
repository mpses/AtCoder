#!/usr/bin/env python3
from itertools import*
n, m, x = map(int, input().split())
d = [list(map(int, input().split())) for k in range(n)]
INF = float("inf")
mi = INF
for i in range(1, n+1):
    for j in combinations(range(n), i):
        if all(sum(d[p][q] for p in j) >= x for q in range(1, m+1)):
            mi = min(mi, sum(d[c][0] for c in j))
print(mi if mi != INF else -1)
