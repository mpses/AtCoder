#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())

l = lambda h, i, j: sum(a[min(i, j):max(i, j) + 1][h::2])

r = range(n)
x = t = -10**4

for i in r:
    y = t
    for j in r:
        if i == j: continue
        z = l(1, i, j)
        if z > y: y, k = z, j
    x = max(x, l(0, i, k))
print(x)