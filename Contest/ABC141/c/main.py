#!/usr/bin/env python3
n, k, q = map(int, input().split())
l = [k - q]*n
for _ in range(q):
    l[int(input()) - 1] += 1
for i in range(n):
    print("Yes" if l[i] > 0 else "No")