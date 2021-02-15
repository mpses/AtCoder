#!/usr/bin/env python3
n = int(input())
for i in range(101):
    ans = i ** 2 - n
    if ans >= 0:
        print(ans)
        exit()