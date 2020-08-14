#!/usr/bin/env python3
from itertools import*
n, *a = map(int, open(0).read().split())
a = [i < j for i, j in zip(a, a[1:])]
H = lambda x: -~x*x//2
l = [H(len(list(p))) for k, p in groupby(a) if k]
print(n + sum(l))