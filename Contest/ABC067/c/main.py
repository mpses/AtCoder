#!/usr/bin/env python3
from itertools import*
_, *d = map(int, open(0).read().split())
*a, s = accumulate(d)
print(min(abs(s - x*2) for x in a))