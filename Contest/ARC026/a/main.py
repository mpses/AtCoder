#!/usr/bin/env python3
n, a, b = map(int, input().split())
print(n * b if n <= 5 else 5 * b + (n - 5) * a)