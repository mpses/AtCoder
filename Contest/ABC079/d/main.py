#!/usr/bin/env python3.4.3
import numpy as np
from scipy.sparse.csgraph import floyd_warshall, csgraph_from_dense
from itertools import*
from collections import*

h, w = map(int, input().split())
G = [list(map(int, input().split())) for _ in [0]*10]

m = floyd_warshall(csgraph_from_dense(G))

d = list(chain.from_iterable(list(map(int, input().split())) for _ in [0]*h))
C = Counter(d)
s = 0
for i in range(10):
    s += m[i][1] * C.get(i, 0)
print(int(s))