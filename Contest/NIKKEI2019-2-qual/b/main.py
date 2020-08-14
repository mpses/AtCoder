#!/usr/bin/env python3
from collections import*
n, *d = map(int, open(0).read().split())
c = Counter(d)
if d[0] or c[0] > 1:
    exit(print(0))
MOD = 998244353
m = 1
for i in range(1, max(d)):
    m *= pow(c[i], c[i + 1], MOD)
    m %= MOD
print(m)