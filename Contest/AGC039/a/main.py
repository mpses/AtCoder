#!/usr/bin/env python3
from itertools import*
s = input()
k = int(input())
t = [len(list(e)) for _, e in groupby(s)]
if len(set(s)) == 1:
    a = len(s) * k // 2
elif k > 1 and s[0] == s[-1]:
    p = sum(e // 2 for e in t[1:-1]) * k
    l, r = t[0], t[-1]
    q = (l + r) // 2 * ~-k + l // 2 + r // 2
    a = p + q
else:
    a = sum(e // 2 for e in t) * k
print(a)