#!/usr/bin/env python3
n = int(input())
a = n
for i in range(n + 1):
    j = n - i
    c = 0
    while i > 0:
        c += i % 6
        i //= 6
    while j > 0:
        c += j % 9
        j //= 9
    a = min(a, c)
print(a)