#!/usr/bin/env python3
import sys
sys.setrecursionlimit(500000)

n, q, *d = map(int, open(0).read().split())
res = [0] * n
edge = [[] for _ in res]

for a, b in zip(d[:2*n-2:2],d[1:2*n-2:2]):
    a -= 1;b -= 1
    edge[a] += b,
    edge[b] += a,

def dfs(v, p):
    for j in edge[v]:
        if j != p:  # 親は弾く
            res[j] += res[v]
            dfs(j, v)

for p, x in zip(d[2*n-2::2],d[2*n-1::2]):
    p -= 1
    res[p] += x

dfs(0, -1)

print(*res)