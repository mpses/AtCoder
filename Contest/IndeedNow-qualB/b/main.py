#!/usr/bin/env python3
s, t = input(), input()
for i in range(len(s) + 1):
  if s == t:
    print(i)
    exit()
  s = s[-1] + s[:-1]
print(-1)