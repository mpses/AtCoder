#!/usr/bin/env python3
from itertools import*
n = int(input())
p = []
for i in combinations(range(1, n + 1), 2):
    if sum(i) != n + 1 - n % 2:
        p += i,
print(len(p))
for i in p:
    print(*i)