#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
x = 0
for l in range(n):
    m = float("inf")
    for r in range(l, n):
        m = min(m, a[r])
        x = max(x, (r - l + 1) * m)
print(x)