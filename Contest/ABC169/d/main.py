#!/usr/bin/env python3
from collections import Counter
def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct+=b,
        b = b + 1
    if n > 1:
        fct+=n,
    return Counter(fct).values()
a = 0
n = int(input())
if n == 1:exit(print(0))
for i in factorize(n):
  c = s = 0
  while s <= i:
    c += 1
    s = (c+1)*c//2
  a += c - 1
print(a)