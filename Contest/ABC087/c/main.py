#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
m = 0
for i in range(n): m = max(m, sum(a[:i+1] + a[n+i:]))
print(m)