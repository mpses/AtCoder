#!/usr/bin/env python3
n, *x = map(abs, map(int, open(0).read().split()))
print(sum(x))
print(sum(y**2 for y in x) ** .5)
print(max(x))