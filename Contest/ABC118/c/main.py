#!/usr/bin/env python3
from fractions import gcd
from functools import reduce
print(reduce(gcd, map(int, open(0).read().split()[1:])))