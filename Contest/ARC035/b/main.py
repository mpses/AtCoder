#!/usr/bin/env python3
from itertools import*
import math
MOD = 10**9+7
_, *t = map(int, open(0))
t.sort()
print(sum(accumulate(t)))
p = 1
for _, l in groupby(t):p *= math.factorial(len(list(l)))
print(p % MOD)