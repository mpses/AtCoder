#!/usr/bin/env python3
_, m, *a = map(int, open(0).read().split())
s = sum(a)
print("No" if m > sum(s <= 4*m*i for i in a) else "Yes")