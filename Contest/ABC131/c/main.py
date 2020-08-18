#!/usr/bin/env python3
from fractions import gcd
a, b, c, d = map(int, input().split())
a = a-1
C, D = b // c - a // c, b // d - a // d
l = c*d // gcd(c, d)
CD = b // l - a // l
print(b - a - C - D + CD)