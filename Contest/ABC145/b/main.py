#!/usr/bin/env python3
m = int(input()) // 2
s = input()
print("Yes" if s[:m] == s[m:] else "No")