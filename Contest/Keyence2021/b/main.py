#!/usr/bin/env python3
n, k, *a = map(int, open(0).read().split())
from collections import*
ans = 0
c = Counter(a)
for i in range(max(a) + 2):
    ans += i * max(k - c[i], 0)
    k = min(k, c[i])
print(ans)