#!/usr/bin/env python3
from itertools import*
from fractions import*
ac = lambda l: list(accumulate([0] + l, gcd))
n, *a = map(int, open(0).read().split())
print(max(gcd(s, t) for s, t in zip(ac(a), ac(a[::-1])[-1::-1])))