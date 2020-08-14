#!/usr/bin/env python3.4.3
# AGC 019 A
q, h, s, d, n = map(int, open(0).read().split())
m = min(q*4, h*2, s)
print(min(n*m, n//2*d + n%2*m))