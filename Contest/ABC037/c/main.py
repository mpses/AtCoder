#!/usr/bin/env python3
from itertools import*
n, k, *a = map(int, open(0).read().split())
c = [0] + list(accumulate(a))
print(sum(c[i+k]-c[i] for i in range(n-k+1)))