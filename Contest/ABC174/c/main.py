#!/usr/bin/env python3
k, R, a = int(input()), 7, -1
for i in range(1, k+10):
    if not R%k:
        a = i
        break
    R = (R * 10 + 7) % k
print(a)