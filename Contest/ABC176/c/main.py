#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
a = [0] + a
c = 0
for i in range(n):
    t = a[i] - a[i + 1]
    if t > 0:
        a[i + 1] += t
        c += t
print(c)