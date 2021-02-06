#!/usr/bin/env python3
(n,), *z = [[*map(int, o.split())] for o in open(0)]
from itertools import*
ans = 0
for (x1, y1), (x2, y2) in combinations(z, 2):
    x, y = (x2 - x1), (y2 - y1)
    ans += -1 <= y/x <= 1
print(ans)