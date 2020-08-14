#!/usr/bin/env python3
a, b, c = map(int, input().split())
if a + b == c:
  if b:
    print("+")
  else:
    print("?")
elif a - b == c:
  print("-")
else:
  print("!")
