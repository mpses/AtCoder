#!/usr/bin/env python3
from itertools import accumulate
def erat(m):
    p = [1] * m
    p[0] = p[1] = 0
    for x in range(2, int((~-m)**.5) + 1):
        if p[x]:
            for y in range(x*x, m, x):
                p[y] = 0
    return p

INF = 10**5 + 1
p = erat(INF)
q = [0] * INF
for n in range(INF):
    q[n] = n%2 * p[n] * p[-~n//2]
*a, = accumulate([0] + q)
for _ in [None] * int(input()):
    l, r = map(int, input().split())
    print(a[r + 1] - a[l])