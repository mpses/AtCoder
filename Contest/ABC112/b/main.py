#!/usr/bin/env python3
n, T = map(int, input().split())
l = []
for i in range(n):
    c, t = map(int, input().split())
    if not t > T:
        l.append(c)
print("TLE" if len(l) == 0 else sorted(l)[0])