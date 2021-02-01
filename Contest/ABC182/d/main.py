#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
from itertools import*
*S, = accumulate(a)
*M, = accumulate(S, max)
Z = ans = 0
for s, m in zip(S, M):
    ans = max(ans, Z + m)
    Z += s
print(ans)