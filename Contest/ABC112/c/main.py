#!/usr/bin/env python3
a = abs
z = [list(map(int, input().split())) for _ in range(int(input()))]
z.sort(key = lambda x: x[2])
x, y, h = z[-1]
r = range(101)
for c in r:
    for d in r:
        H = h + a(c-x) + a(d-y)
        if all(u == max(H - a(s-c) - a(t-d), 0) for s, t, u in z):
            print(c, d, H)
            exit()