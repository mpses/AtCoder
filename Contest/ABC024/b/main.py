#!/usr/bin/env python3
n, t, *a = map(int, open(0).read().split())
INF = float("inf")
print(sum(min(t, j - i) for i, j in zip(a, a[1:] + [INF])))