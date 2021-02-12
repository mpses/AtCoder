#!/usr/bin/env python3
T = lambda a: [*map(list, zip(*a))]   # 転置
from itertools import*

h, w = map(int, input().split())
s = [input() for _ in [0] * h]
print(sum(sum(sum(len([*l]) - 1 for k, l in groupby(t) if k == ".") for t in u) for u in (s, T(s))))