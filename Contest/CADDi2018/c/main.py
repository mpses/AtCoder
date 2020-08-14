#!/usr/bin/env python3
# 未AC
n, p = map(int, input().split())
k = c = f = 1
while f <= p:
    if p % f == 0:
        k = c
    c += 1
    f = c**n
print(k)