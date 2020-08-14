#!/usr/bin/env python3
n, m = map(int, input().split())
*h, = map(int, input().split())
h = [0] + h
i = [0] + [1] * n

for j in range(m):
    a, b = map(int, input().split())
    if h[a] >= h[b]:
        i[b] = 0
    if h[a] <= h[b]:
        i[a] = 0
print(sum(i))

