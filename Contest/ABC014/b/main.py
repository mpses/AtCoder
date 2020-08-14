#!/usr/bin/env python3
n, x, *a = map(int, open(0).read().split())
b = bin(x)[::-1]
s = 0
for i, k in enumerate(a):
  if b[i:i+1] == "1":
    s += k
print(s)