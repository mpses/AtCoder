#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
offset = 0
for i in range(n):
    offset = a[i] * 2 - offset
offset //= 2
for i in range(n):
    print(offset, end = " ")
    offset = a[i] * 2 - offset