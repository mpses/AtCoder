#!/usr/bin/env python3
from itertools import*
n, *l = map(int, open(0).read().split())
cnt = 0
for a, b, c in combinations(l, 3):
    if a != b != c != a and a + b > c and b + c > a and c + a > b:
        cnt += 1
print(cnt)