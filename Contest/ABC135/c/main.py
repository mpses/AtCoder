#!/usr/bin/env python3
n, p, *a = map(int, open(0).read().split())
c = 0
for a, b in zip(a, a[n:]):
    c += min(p+a, b)
    p = a - max(min(b-p, a), 0)
print(c)