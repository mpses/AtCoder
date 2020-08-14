#!/usr/bin/env python3
_, __, *d = map(int, open(0).read().split())
print(max(min(d[1::2]) - max(d[::2]) + 1, 0))