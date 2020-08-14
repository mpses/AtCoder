#!/usr/bin/env python3
from itertools import*
from bisect import*
(n, m, k), a, b = [list(map(int, o.split())) for o in open(0)]
*a, = accumulate([0] + a)
*b, = accumulate([0] + b)
c = 0
for i in range(n + 1):
    if a[i] > k:
        break
    c = max(c, i + bisect(b, k - a[i]) - 1)
print(c)