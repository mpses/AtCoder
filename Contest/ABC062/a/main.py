#!/usr/bin/env python3
p = "_acababaababa"
x, y = map(int, input().split())
print("YNeos"[p[x]!=p[y]::2])