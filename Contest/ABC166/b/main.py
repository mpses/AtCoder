#!/usr/bin/env python3
n, k = map(int, input().split())
a = []
for i in range(k):
    d = int(input())
    a += list(map(int, input().split()))
print(n - len(set(a)))