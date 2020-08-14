#!/usr/bin/env python3
n, k = map(int, input().split())
s = 0
for i in range(1, n+1):
    c = 0
    while i < k:i*=2;c+=1
    s += 1 / 2**c
print(s/n)