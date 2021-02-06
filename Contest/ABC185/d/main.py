#!/usr/bin/env python3
n, m, *a = map(int, open(0).read().split())
if n == m:
    print(0)
    exit()
a.sort()
a = [0] + a + [n + 1]
L = [t - s - 1 for s, t in zip(a, a[1:]) if s + 1 != t]
k = min(L)
print(sum(0--l // k for l in L))