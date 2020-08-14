#!/usr/bin/env python3
s, _, *q = open(0)
g = ""
s = s.strip()
for q in q:
  q = q.strip().split()
  if q[0] == "1":
    g, s = s, g
  else:
    if q[1] == "1":
      g += q[2]
    else:
      s += q[2]
print(g[::-1] + s)