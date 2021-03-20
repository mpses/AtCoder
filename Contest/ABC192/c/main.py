#!/usr/bin/env python3
n, k = input().split()
for _ in [None] * int(k):
    n = str(int("".join(sorted(n, reverse = True))) - int("".join(sorted(n))))
print(n)