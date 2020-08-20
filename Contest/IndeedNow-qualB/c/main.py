#!/usr/bin/env python3
(n,), *e = [[*map(int, o.split())] for o in open(0)]
from collections import*
d = defaultdict(list)
V = defaultdict(lambda: False)
for a, b in e:
    d[a] += b,
    d[b] += a,
from heapq import*
c, ans = [1], []
for _ in [None] * n:
    p = heappop(c)
    ans += p,
    V[p] = True
    for i in d[p]:
        if not V[i]:
            heappush(c, i)
print(*ans)