#!/usr/bin/env python3
(n,), *d = [[*map(int, o.split())] for o in open(0)]
c = 0
for a, b in d:
    m = (b - a + 1)
    c += (a + b) * (m // 2)
    if m % 2:
        c += (a + b) // 2
print(c)