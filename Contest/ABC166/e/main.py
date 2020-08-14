#!/usr/bin/env python3
from collections import*

n = int(input())
a = list(map(int, input().split()))

l = []
r = []
for i, j in enumerate(a):
    l += [i + j]
    r += [i - j]

c = 0
l = Counter(l)
for r in r:
    c += l.get(r, 0)
print(c)