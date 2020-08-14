#!/usr/bin/env python3
a, v, b, w, t = map(int, open(0).read().split())
if v <= w:
    exit(print("NO"))
if abs(b - a) <= (v - w) * t:
    print("YES")
else:
    print("NO")