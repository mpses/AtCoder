#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
b = a[0]
for i in range(n):
    if b == 2:
        print(i+1)
        exit()
    b = a[b - 1]
print(-1)