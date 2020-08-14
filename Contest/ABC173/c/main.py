#!/usr/bin/env python3
import numpy as np
from itertools import combinations as comb
h, w, k = map(int, input().split())
a = np.array([list(input()) for _ in [None]*h])
cnt = 0
for j1 in range(h):
    for i1 in comb(range(h), j1):
        for j2 in range(w):
            for i2 in comb(range(w), j2):
                c = np.copy(a)
                c = np.delete(c, list(i1), 0)
                c = np.delete(c, list(i2), 1)
                cnt += np.count_nonzero(c == '#') == k
print(cnt)