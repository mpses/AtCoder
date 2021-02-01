#!/usr/bin/env python3
n, x = map(int, input().split())
for i in input():
    if i == "o":
        x += 1
    else:
        x = max(0, x - 1)
print(x)