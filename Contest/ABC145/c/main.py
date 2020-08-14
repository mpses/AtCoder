#!/usr/bin/env python3
from itertools import permutations as p
n, *d = map(int, open(0).read().split())
h = []
k = 0
for i in list(p(range(n))):
    for j in range(n - 1): # i[j], i[j+1]
        k += ((d[i[j] * 2] - d[i[j+1] * 2])**2 + (d[i[j] * 2 + 1] - d[i[j+1] * 2 + 1])**2)**.5
    h += [k]
    k = 0
print(sum(h) / len(h))