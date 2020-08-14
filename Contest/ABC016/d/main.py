#!/usr/bin/env python3
from numpy import*
cr = cross
ar = array
Ax, Ay, Bx, By, n, *z = map(int, open(0).read().split())
pos = list(zip(z[::2], z[1::2]))
pos += [pos[0]]

def inter(a1, a2, b1, b2):
    return cr(a2-a1, b1-a1) * cr(a2-a1, b2-a1) < 0 > cr(b2-b1, a1-b1) * cr(b2-b1, a2-b1)

a1, a2 = ar([Ax, Ay]), ar([Bx, By])
c = 0
for i in range(n):
    b1 = ar(pos[ i ])
    b2 = ar(pos[i+1])

    c += inter(a1, a2, b1, b2)

print(c // 2 + 1)