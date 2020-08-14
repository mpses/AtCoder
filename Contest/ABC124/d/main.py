#!/usr/bin/env python3
from itertools import*
n, k = map(int, input().split())
s = input()
l = [len(list(t)) for _ in t in groupby(s)]
if s[0] == 0:
    l = [0] + l
a = [0] + accumulate(l)
k 