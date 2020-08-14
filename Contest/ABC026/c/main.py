#!/usr/bin/env python3
n, *b = map(int, open(0))
b = [1] + b
c = [[] for _ in [0]*55]
for i in range(~-n, -1, -1):
    p = 1
    if c[i]:
        l = c[i]
        p += min(l) + max(l)
    if i:
        c[~-b[i]] += p,
    else:
        print(p)