#!/usr/bin/env python3
s, p = map(int, input().split())
for n in range(1, int(p ** .5) + 1):
    if p % n:
        continue
    if n + p // n == s:
        print("Yes")
        exit()
print("No")