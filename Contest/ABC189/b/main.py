#!/usr/bin/env python3
(n, x), *d = [[*map(int, o.split())] for o in open(0)]
x *= 100
for e, (v, p) in enumerate(d, 1):
    x -= v * p
    if x < 0:
        print(e)
        exit()
print(-1)