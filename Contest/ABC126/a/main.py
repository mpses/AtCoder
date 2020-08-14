#!/usr/bin/env python3
k = int(input()[2:])
s = list(input())
s[k-1] = chr(ord(str(s[k-1])) + 32)
print("".join(s))