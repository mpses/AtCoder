#!/usr/bin/env python3
n, k = map(int, input().split())

t = []
n = n%k

while n != 0:
    n = abs(n-k)
    if n in t or n == 0:
        print(min(t))
        exit()
    t.append(abs(n))
print(0)
