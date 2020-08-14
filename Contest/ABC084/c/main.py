#!/usr/bin/env python3
(n,), *d = [list(map(int, c.split())) for c in open(0)]
n -= 1
for i in range(n):
    t = 0
    for j in range(i, n):
        c, s, f = d[j]
        t = (s if t < s else t if t % f == 0 else t + f - t%f) + c
    print(t)
print(0)