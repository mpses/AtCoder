#!/usr/bin/env python3
n, k, m, *a = map(int, open(0).read().split())
p = n*m - sum(a)
print(-1 if p>k else p if p>0 else 0)