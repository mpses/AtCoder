#!/usr/bin/env python3
_, s = open(0)
c = 0
for i in range(1000):
    p = 0
    F = 1
    for j in str(i).zfill(3):
        q = s[p:].find(j)
        if q < 0:
            F = 0
            break
        p += q + 1
    c += F
print(c)