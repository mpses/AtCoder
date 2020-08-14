#!/usr/bin/env python3
k, s = map(int, input().split())
c = 0
for x in range(min(s, k)+1):
    for y in range(min(s-x, k)+1):
        if s-x-y <= k:
            c += 1
print(c)