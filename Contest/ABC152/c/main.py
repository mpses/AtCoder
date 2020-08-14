#!/usr/bin/env python3
_ = input()
p = list(map(int, input().split()))
m = float("inf")
c = 0
for i in p:
  c += i < m
  m = min(m, i)
print(c)