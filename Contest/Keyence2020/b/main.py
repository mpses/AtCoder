#!/usr/bin/env python3
INF = float("inf")
n, *d = map(int, open(0).read().split())
p = sorted(zip(*[iter(d)]*2), key=sum)
M, a = -INF, 0
for X, L in p:
    l, r = X-L, X+L
    if M <= l:
        a += 1
        M = r
print(a)