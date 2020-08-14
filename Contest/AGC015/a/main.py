#!/usr/bin/env python3
n, a, b = map(int, input().split())
def p(a):print(a);exit()
if a > b:p(0)
elif n < 2:p(0+(a == b))
else: p((b-a) * (n-2) + 1)