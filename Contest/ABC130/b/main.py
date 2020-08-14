#!/usr/bin/env python3
n, x, *l = map(int, open(0).read().split())
s, c = 0, 0
for i in l:
    s += i
    c += 1
    if s > x:
        print(c)
        exit()
print(n + 1)