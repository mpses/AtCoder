#!/usr/bin/env python3
import numpy as np
from scipy.sparse.csgraph import floyd_warshall, csgraph_from_dense
 
n, m = map(int, input().split())
G = [[0]*n for _ in [0]*n]
for _ in [0]*m:
    a, b = map(int, input().split())
    a -= 1;b -= 1
    G[a][b] = 1

m = floyd_warshall(csgraph_from_dense(G), directed = False)
for i in m:
  print(np.count_nonzero(i == 2))
