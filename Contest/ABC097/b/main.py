#!/usr/bin/env python3
r = range(1,32)
x = int(input())
print(max(b**p for p in r[1:] for b in r if b**p <= x))