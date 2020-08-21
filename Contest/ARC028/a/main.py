#!/usr/bin/env python3
n, a, b = map(int, input().split())
while 1:
  n -= a
  if n <= 0:print("Ant");exit()
  n -= b
  if n <= 0:print("Bug");exit()
