#!/usr/bin/env python3
l, r = map(int,input().split())
s = range(l, r+1)[:673]
print(min(i*j % 2019 for i in s for j in s if i<j))