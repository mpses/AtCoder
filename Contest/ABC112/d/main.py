#!/usr/bin/env python3
n, m = map(int, input().split())
print(next(v for v in range(m // n, -1, -1) if m % v == 0))