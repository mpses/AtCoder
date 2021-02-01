#!/usr/bin/env python3
from itertools import*
from bisect import*

def ac(l):
    return [*accumulate([0] + l)]

(n, m), h, w = [[*map(int, o.split())] for o in open(0)]
h.sort()
w.sort()

def take_closest_sub(w, m, x):
    pos = bisect_left(w, x)
    if pos == 0:
        return abs(x - w[0])
    if pos == m:
        return abs(w[-1] - x)
    before = w[pos - 1]
    after = w[pos]
    return min(after - x, x - before)

a = [j - i for i, j in zip(h, h[1:])]
b, c = ac(a[::2]), ac(a[1::2])
INF = float("inf")
ans = INF
for i in range(n // 2 + 1):
    j = i * 2
    p, q, r, s, v = b[i], b[0], c[n // 2], c[i], h[j]
    g = take_closest_sub(w, m, v)
    ans = min(ans, p - q + r - s + g)
print(ans)