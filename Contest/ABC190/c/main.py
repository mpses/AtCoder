#!/usr/bin/env python3
(n, m), *d = [[*map(int, o.split())] for o in open(0)]
(k,), *s = d[m:]
ans = 0
from itertools import*
for i in product([0, 1], repeat = k):
    p = [0] * n
    for e, j in enumerate(i):
        p[s[e][j] - 1] = 1
    ans = max(ans, sum(p[a - 1] * p[b - 1] for a, b in d[:m]))
print(ans)