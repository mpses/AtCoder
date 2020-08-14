#!/usr/bin/env python3
s, m = input(), float("inf")
for i in range(len(s)-2):
    m = min(abs(int(s[i:i+3])-753), m)
print(m)