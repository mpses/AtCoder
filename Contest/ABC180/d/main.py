#!/usr/bin/env python3
x, y, a, b = map(int, input().split())
c = 0
while y > a * x <= x + b:
    x *= a
    c += 1
print(c + (y - x - 1) // b)