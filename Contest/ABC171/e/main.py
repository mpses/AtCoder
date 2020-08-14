#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
s = 0
for A in a:s^=A
print(*[s^B for B in a])