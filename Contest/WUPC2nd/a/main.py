#!/usr/bin/env python3
n, m = map(int, input().split())
print(sum(i*i % m for i in range(1, n + 1)) % m)