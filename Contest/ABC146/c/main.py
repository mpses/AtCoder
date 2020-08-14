#!/usr/bin/env python3
a, b, x = map(int, input().split())
l, r = 0, 10**9+1
while l　< r+1:
    m = (r + l) // 2
    if m*a + b*len(str(m)) > x: r = m
    else: l = m
print(l)