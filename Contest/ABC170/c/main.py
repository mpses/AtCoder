#!/usr/bin/env python3
x, n, *p = map(int, open(0).read().split())
r = [i for i in range(102) if i not in p]
print(sorted(r, key = lambda y: abs(x - y))[0])