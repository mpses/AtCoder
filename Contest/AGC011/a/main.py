#!/usr/bin/env python3
n, c, k, *t = map(int, open(0).read().split())
t.sort()
m = l = s = 0
for t in t:
    m += 1
    if m > c or t > l:
        s += 1
        m = 1
        l = t + k
print(s)