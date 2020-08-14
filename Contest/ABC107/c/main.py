#!/usr/bin/env python3
n, k, *a = map(int, open(0).read().split())
m = INF = float("inf")
for i in range(n - k + 1):
    l, r = a[i], a[i + k - 1]
    c = abs(r-l)
    m = min(m, min(abs(l) + c, abs(r) + c))
print(m)