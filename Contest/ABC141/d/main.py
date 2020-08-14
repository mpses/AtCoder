#!/usr/bin/env python3
from heapq import*
n, m, *a = eval(",-".join(open(0).read().split()))
a.sort()
for _ in [0]*-m:heappush(a, 0--heappop(a)//2)
print(-sum(a))