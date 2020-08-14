#!/usr/bin/env python3
from itertools import*
I = input
n = int(I())
c = 0;z = []
for i in range(n):
    for j in range(int(I())):
        z += [[i] + list(map(int, I().split()))]
for j in product([0,1], repeat=n):
    if all(j[i] == 0 or j[x-1] - y == 0 for i, x, y in z):
        c = max(c, sum(j))
print(c)