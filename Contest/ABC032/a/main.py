#!/usr/bin/env python3
from fractions import gcd
a, b, n = map(int, open(0).read().split())
f = g = a * b // gcd(a,b) 
while True:
  if f >= n:
    print(f)
    exit()
  f += g