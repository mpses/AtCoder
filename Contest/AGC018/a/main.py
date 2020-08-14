#!/usr/bin/env python3
n, k, *a = map(int, open(0).read().split())
from functools import*
import math
print("IM" * (k % reduce(math.gcd, a) > 0 or k > max(a)) + "POSSIBLE")