#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
c = 0
for i in range(2, 1001):
    s = sum(b % i == 0 for b in a)
    if s > c:
        c = s
        k = i
print(k)