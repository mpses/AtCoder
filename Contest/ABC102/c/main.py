#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
s = [a - i - 1 for i, a in enumerate(a)]
b = sorted(s)[n // 2]
print(sum(abs(s - b) for s in s))