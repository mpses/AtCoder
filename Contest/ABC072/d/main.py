#!/usr/bin/env python3
n, *p = map(int, open(0).read().split())
c = 0
for i in range(n):
    if p[i] == -~i:
        if i == ~-n:
            p[i], p[i-1] = p[i-1], p[i]
        else:
            p[i], p[i+1] = p[i+1], p[i]
        c += 1
print(c)