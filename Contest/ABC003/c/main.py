#!/usr/bin/env python3
_, k, *r = map(int, open(0).read().split())
R = 0
for C in sorted(r)[-k:]:
    R = (R + C) / 2
print(R)