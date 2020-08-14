#!/usr/bin/env python3
from itertools import*
s = list(input())
l = len(s)
p = list(chain.from_iterable(zip(s, " "*l)))[:-1]
S = 0
for i in product([0,1], repeat=~-l):
    q = p[:]
    for k, j in enumerate(i):
        if j:
            q[k*2 + 1] = "+"
    S += eval("".join(q).replace(" ", ""))
print(S)