#!/usr/bin/env python3
x, y, a, b = map(int, input().split())
c = 0
while x < y:
    x *= a
    c += 1
x //= a
c -= 1
while x < y:
    x += b
    c += 1
c -= 1
print(c)