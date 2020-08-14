#!/usr/bin/env python3
n, a, b, c, d = map(int, input().split())
s = input()
p = "##" not in s[a:max(c, d)]
if c > d:
    p *= "..." in s[b-2:d+1]
print(p and "Yes" or "No")