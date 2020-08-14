#!/usr/bin/env python3
n, m = map(int, input().split())
s = [list(map(int, input().split()[1:])) for _ in range(m)]
p = list(map(int, input().split()))
c = 0

from itertools import product
for i in product([0,1], repeat=n):
    if all(
        len([None for t in t if i[t-1]]) % 2 == p[j] for j, t in enumerate(s)
    ):
        c += 1
print(c)