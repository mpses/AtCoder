#!/usr/bin/env python3
n, x, *a = map(int, open(0).read().split())
print(*[b for b in a if b != x])