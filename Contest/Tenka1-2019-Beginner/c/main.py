#!/usr/bin/env python3
from itertools import*
n = int(input())
s = input()
b, w = [list(accumulate([0] + list(map(int, s.translate(str.maketrans("#.","10"[::p]))))[::p]))[::p] for p in [1,-1]]
m = float("inf")
for i in zip(b, w):
    m = min(m, sum(i))
print(m)