#!/usr/bin/env python3
_, _, _, *d = open(0).read().split()
s = ""
for c in d:s += c
from collections import*
for i in range(10):
    l = Counter(s).most_common()
    k = s.index(l[0][0])
    a, b = divmod(k, 10)
    print(f"{a+1} {b+1} {l[1][0]}")