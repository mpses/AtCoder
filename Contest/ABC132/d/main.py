#!/usr/bin/env python3
from math import factorial as f
n, k = map(int, input().split())
mod = 10**9+7
for i in range(k):
    try:
        print(f(n - k + 1) * f(k - 1) // f(i + 1) // f(n - k - i) // f(i) // f(k - i - 1) % mod)
    except ValueError:
        print(0)