#!/usr/bin/env python3
K, n, *a = map(int, open(0).read().split())
s = 0
for i in range(n):
    s = max(s, a[i] - a[i-1])
print(K - max(s, a[0]+K-a[-1]))
