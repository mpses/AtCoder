#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
a.sort()
from itertools import*
*s, = accumulate(a)
print(sum(s[n - 1] - s[i] - (n - 1 - i) * a[i] for i in range(n - 1)))