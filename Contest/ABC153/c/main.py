#!/usr/bin/env python3
n, k, *h = map(int, open(0).read().split())
print(sum(sorted(h)[:n - min(n, k)]))