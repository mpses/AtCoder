#!/usr/bin/env python3
_, *s = open(0)
c = 0
for t in s[::-1]:
    a, b = map(int, t.split())
    c += (-a-c) % b
print(c)