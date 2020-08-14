#!/usr/bin/env python3
n = int(input())
t = input()
*c, = map(int, t.replace(*"W1").replace(*"R0"))

"""
1100 -> 0101 -> 0011
00
10110100 -> 00111100 -> 00011110 -> 00001111
"""

a = 0
i, j = 0, 1
while i + j < n:
    if c[i] == 1 and c[-j] == 0:
        a += 1
        i += 1
        j += 1
    elif c[i] == c[-j] == 0:
        i += 1
    elif c[i] == c[-j] == 1:
        j += 1
    else:
        i += 1
        j += 1
print(a)