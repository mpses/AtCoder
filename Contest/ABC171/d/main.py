#!/usr/bin/env python3
from collections import*
(n,), a, q, *d = [list(map(int, o.split())) for o in open(0)]
C = Counter(a)
s = sum(a)
for b, c in d:
    bf = C[b]
    C[c] += bf
    C[b] = 0
    s += (c - b) * bf
    print(s)