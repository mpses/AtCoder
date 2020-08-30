#!/usr/bin/env python3
s = input()
t = input()
a, b = len(s), len(t)
c = INF = float("inf")
for i in range(a - b + 1):
    c = min(c, sum(d != e for d, e in zip(s[i:i+b], t)))
print(c)