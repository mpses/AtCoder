#!/usr/bin/env python3
from itertools import*
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in [0]*n]
for i in product(range(k), repeat=n):
    w = 0
    for j in range(n):
        w ^= t[j][i[j]]
    if w == 0:
        print("Found")
        exit()
print("Nothing")
