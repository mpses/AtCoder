#!/usr/bin/env python3
t = 0
for i, j in sorted([list(map(int, input().split())) for _ in [0]*int(input())], key = lambda x:x[1]):
  t += i
  if t > j:
    print("No")
    exit()
print("Yes")