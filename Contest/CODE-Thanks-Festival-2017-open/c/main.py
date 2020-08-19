#!/usr/bin/env python3
from heapq import*
(n, k), *d = [[*map(int, o.split())] for o in open(0)]
q = []
for a, b in d:
    heappush(q, (a, b))
ans = 0
for _ in [0] * k:
    a, b = heappop(q)
    ans += a
    heappush(q, (a + b, b))
print(ans)