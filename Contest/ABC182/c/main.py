#!/usr/bin/env python3
n = input()
l = len(n)
from itertools import*
for r in range(l):
    for k in combinations(n, l - r):
        if int("".join(k)) % 3 == 0:
            print(r)
            exit()
print(-1)