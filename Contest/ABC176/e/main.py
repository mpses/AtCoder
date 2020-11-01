#!/usr/bin/env python3
from collections import*
d = defaultdict(bool)
(H, W, _), *C = [[*map(int, o.split())] for o in open(0)]
x, y = [0] * H, [0] * W
for h, w in C:
    h -= 1; w -= 1
    x[h] += 1
    y[w] += 1
    d[f"{h}-{w}"] = True
X, Y = max(x), max(y)
A = [h for h, i in enumerate(x) if i == X]
B = [w for w, j in enumerate(y) if j == Y]
flag = False
for a in A:
    for b in B:
        if not d[f"{a}-{b}"]:
            flag = True
            break
print(X + Y - 1 + flag)