#!/usr/bin/env python3
from itertools import*
n, *c = map(int, open(0).read().split())
imos = [0] * (10**7 + 1)
for start, end in zip(c[::2], c[1::2]):
    imos[start] += 1
    imos[end+1] -= 1
print(max(accumulate(imos)))