#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
A = 1
for i in a:
    A *= 2 - i%2
print(3**n - A)