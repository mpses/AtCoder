#!/usr/bin/env python3.4.3
# AGC 040 A

# groupbyはいいぞ
from itertools import*
a = b = 0
for k, n in groupby(input()):
  n = len(list(n))
  a -= n*~n//2 + min(n, b)*(k==">")
  b = n
print(a)