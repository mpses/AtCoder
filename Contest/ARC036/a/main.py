#!/usr/bin/env python3
from itertools import*
n, k, *t = map(int, open(0).read().split())
p = [0] + list(accumulate(t))
for i in range(n-2):
    if p[i+3] - p[i] < k:
        print(i+3)
        exit()
print(-1)