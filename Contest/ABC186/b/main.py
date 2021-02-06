#!/usr/bin/env python3
_, __, *a = map(int, open(0).read().split())
m = min(a)
print(sum(b - m for b in a))