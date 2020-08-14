#!/usr/bin/env python3
x = int(input())
p, q = divmod(x, 11)
s = max(q - 6, 0)
print(p*2 + ([1,2][s>0] if q else 0))