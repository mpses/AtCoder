#!/usr/bin/env python3
# 2次元累積和 S の [x1, x2) × [y1, y2) 総和
def ac2(s, x1, x2, y1, y2):
    return s[x2][y2] - s[x1][y2] - s[x2][y1] + s[x1][y1]

import numpy as np
_, *d = open(0)
n, k = map(int, _.split())
B = np.zeros((2*k, 2*k))
for e in d:
    *z, c = e.split()
    x, y = map(int, z)
    B[x % (2*k)][(y + k * (z == "W")) % (2*k)] += 1
B.cumsum(axis = 0)
B.cumsum(axis = 1)
B = np.tile(B, (2,2))
print(B)
# 書きかけ