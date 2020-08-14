#!/usr/bin/env python3
s = input()
l = int(input())
m = len(s) - l
print(0 if m<0 else len({s[i : i+l] for i in range(m + 1)}))