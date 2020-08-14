#!/usr/bin/env python3
n, m, a, b, *c = map(int, open(0).read().split())
for i in range(m):
    if n <= a:
        n += b
    n -= c[i]
    if n < 0:
        print(i+1)
        exit()
print("complete")