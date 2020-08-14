#!/usr/bin/env python3
from collections import Counter
(n, m), *d = [list(map(int, o.split())) for o in open(0)]
a = n
for _ in [0] * m:
    k = []
    for i in range(n):
        k += d[i][0],
    ind, w = Counter(k).most_common()[0]
    a = min(a, w)
    for j in range(n):
        d[j].remove(ind)
print(a)