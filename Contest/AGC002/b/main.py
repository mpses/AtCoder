#!/usr/bin/env python3
n, m = map(int, input().split())
L = [1]*n
R = [1] + [0]*~-n
for _ in range(m):
  x, y = map(int, input().split())
  x -= 1;y -= 1
  if R[x]:R[y] = 1
  L[x] -= 1;L[y] += 1
  R[x] *= (L[x] > 0)
print(sum(R))