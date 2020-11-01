#!/usr/bin/env python3
n = int(input())
c = 0
for i in range(1, int(n ** .5) + 1):
    for j in range(i, 0--n // i):
        if i < j:
            c += 2
        if i == j:
            c += 1
print(c)