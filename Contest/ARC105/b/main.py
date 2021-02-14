#!/usr/bin/env python3
# gcd(x, X) = gcd(x, X - x) より全体の gcd は変化しない
n, *a = map(int, open(0).read().split())
from functools import reduce
from math import gcd
print(reduce(gcd, a))