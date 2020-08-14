#!/usr/bin/env python3.4.3
# AGC 027 A
_, x, *a = map(int, open(0).read().split())
c = 0
for i in sorted(a):
  x -= i
  if x<0:
    break
  c += 1
print(c - (x>0))