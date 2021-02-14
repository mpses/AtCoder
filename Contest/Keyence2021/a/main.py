#!/usr/bin/env python3
(n,), a, b = [[*map(int, o.split())] for o in open(0)]
from itertools import*
*A, = accumulate(a, max)
print(ans := a[0] * b[0])
for i in range(1, n):
    ans = max(ans, A[i] * b[i])
    print(ans)