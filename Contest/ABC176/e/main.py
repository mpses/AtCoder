#!/usr/bin/env python3
from collections import*
(H, W, m), *d = [[*map(int, o.split())] for o in open(0)]
x, y = [0] * H, [0] * W
for h, w in d:
    x[h - 1] += 1
    y[w - 1] += 1
X, Y = max(x), max(y)
R = [h for h, i in enumerate(x) if i == X]
C = [w for w, j in enumerate(y) if j == Y]
# solving