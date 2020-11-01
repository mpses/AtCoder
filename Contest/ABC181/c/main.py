#!/usr/bin/env python3
from itertools import*
(n,), *d = [[*map(int, o.split())] for o in open(0)]
for (a, b), (c, d), (e, f) in combinations(d, 3):
    if (e - a) * (d - b) == (c - a) * (f - b):
        print("Yes")
        exit()
print("No")