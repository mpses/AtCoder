#!/usr/bin/env python3
n = int(input())
s = input()
x = m = 0
for i in range(n): x += [-1,1][s[i] == "I"]; m = max(m,x)
print(m)