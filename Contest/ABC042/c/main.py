#!/usr/bin/env python3
n, k, *d = open(0).read().split()
n, d = int(n), set(d)
while True:
  if not d & set(str(n)):
    exit(print(n))
  n += 1