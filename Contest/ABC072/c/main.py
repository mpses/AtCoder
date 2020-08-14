#!/usr/bin/env python3
c = [0]*100002
input()
for x in map(int, input().split()):
  c[x] += 1
  c[x+1] += 1
  c[x+2] += 1
print(max(c))