#!/usr/bin/env python3
_, *h = map(int, open(0).read().split())
s = p = 0
for i in h:
    s += max(i - p, 0)
    p = i
print(s)