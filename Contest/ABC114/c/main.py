#!/usr/bin/env python3
from itertools import*
n = int(input())
c = 0
k = "357"

for i in range(3, -~len(str(n))):
    for j in product(k, repeat = i):
        if all(j.count(h) for h in k):
            if int("".join(j)) <= n:
                c += 1
print(c)