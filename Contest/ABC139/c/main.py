#!/usr/bin/env python3
d = {}
c = 0
for i in open(0):
    i = str(sorted(i))
    t = d.get(i, 0)
    c += t
    d[i] = t + 1
print(c)