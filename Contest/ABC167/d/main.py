#!/usr/bin/env python3
n, k, *a = map(int, open(0).read().split())
a = [0] + a
p = 1
while k:
    if k % 2:
        p = a[p]
    a = [a[b] for b in a]
    k //= 2
print(p)