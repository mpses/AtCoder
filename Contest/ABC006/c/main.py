#!/usr/bin/env python3
n, m = map(int, input().split())
b = m%2
if not 2*n <= m <= 4*n:
    print(-1, -1, -1)
    exit()
m -= 2*n
c = m // 2
a = n - b - c
print(a, b, c)