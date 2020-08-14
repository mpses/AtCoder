#!/usr/bin/env python3
s, t = open(0)
l, r, u, d, Q = map(s.count, "LRUD?")
d = abs(l - r) + abs(u - d)
print([0, d + Q, max((d - Q) % 2, d - Q)][int(t)])