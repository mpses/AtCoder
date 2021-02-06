#!/usr/bin/env python3
def T(L):
    return [[*x] for x in zip(*L)]
(h, w, n, m), *z = [[*map(int, o.split())] for o in open(0)]
R = [[0] * w for _ in [0] * h]
for a, b in z[:n]:
    R[a - 1][b - 1] = 1
for c, d in z[n:]:
    R[c - 1][d - 1] = 2
G1 = R[:]
G2 = T(R)
from itertools import*
def main(G, t):
    for i in range(t):
        g = []
        for k, l in groupby(G[i], key = lambda x: x < 2):
            l = list(l)
            if k:
                if 1 in l:
                    g += [1] * len(l)
                else:
                    g += l
            else:
                g += [0] * len(l)
        G[i] = g
    return G
G1 = main(G1, h)
G2 = main(G2, w)
ans = 0
for i in range(h):
    for j in range(w):
        if G1[i][j] or G2[j][i]:
            ans += 1
print(ans)