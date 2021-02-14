#!/usr/bin/env python3
*p, = map(int, input().split())
s = sum(p)
from itertools import*
for i in range(1, 4):
    for j in combinations(p, i):
        if sum(j) * 2 == s:
            print("Yes")
            exit()
print("No")