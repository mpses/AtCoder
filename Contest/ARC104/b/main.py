#!/usr/bin/env python3
from collections import*
n, s = input().split()
import numpy as np
from itertools import*
info = {s: np.array(l) for s, l in zip("ATGC", [[1, 0], [-1, 0], [0, 1], [0, -1]])}
C = Counter([tuple(a) for a in accumulate(info[m] for m in s)])
C[(0, 0)] += 1
print(sum(v * (v - 1) // 2 for v in C.values()))