#!/usr/bin/env python3
n, k, *p = map(int, open(0).read().split())
print(sum(sorted(p)[:k]))