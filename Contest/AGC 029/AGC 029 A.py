#!/usr/bin/env python3.4.3
# AGC 029 A
c = b = 0
for s in input():
  c += b*(s=="W")
  b += s=="B"
print(c)