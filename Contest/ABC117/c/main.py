#!/usr/bin/env python3
n, m, *x = map(int, open(0).read().split())
x.sort()
print(sum(sorted(j - i for i, j in zip(x, x[1:]))[-n::-1]))