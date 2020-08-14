#!/usr/bin/env python3
n, m, q = map(int, input().split())
from itertools import*
t = 0
l = [list(map(int, input().split())) for _ in range(q)]
for i in combinations_with_replacement(range(1, m+1), n):
    s = 0
    for a, b, c, d, in l:
        if i[b-1] - i[a-1] == c: s += d
    t = max(t, s)
print(t)