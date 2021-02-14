#!/usr/bin/env python3
from math import gcd
from functools import reduce
lcm = lambda a, b: a * b // gcd(a, b)
print(reduce(lcm, range(2, int(input()) + 1)) + 1)