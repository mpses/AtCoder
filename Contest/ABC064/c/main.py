#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
l = [i//400 for i in a if i<3200]
k = len(set(l))
print(k or 1, n - len(l) + k)