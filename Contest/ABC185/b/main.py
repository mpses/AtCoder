#!/usr/bin/env python3
(n, _, t), *q = [[*map(int, o.split())] for o in open(0)]
M, d = n, 0
for a, b in q:
    n -= a - d
    if n <= 0:
        print("No")
        exit()
    n = min(M, n + b - a)
    d = b
print("Yes" if n > t - b else "No")