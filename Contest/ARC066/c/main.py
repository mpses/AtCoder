#!/usr/bin/env python3
from collections import*
n, *a = map(int, open(0).read().split())
c = Counter(a)
MOD = 10**9+7
if n%2:
    if c.get(0, 0) != 1 or any(c.get(i, 0) != 2 for i in range(2, n, 2)):
        exit(print(0))
    print(2 ** (n // 2) % MOD)
else:
    if any(c.get(i, 0) != 2 for i in range(1, n, 2)):
        exit(print(0))
    print(2 ** (n // 2) % MOD)