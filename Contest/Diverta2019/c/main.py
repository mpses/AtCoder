#!/usr/bin/env python3
t = open(0).read()
c1 = c2 = c3 = 0
for s in t.split():
    if s[-1] == "A" and s[0] == "B":
        c1 += 1
    elif s[-1] == "A":
        c2 += 1
    elif s[0] == "B":
        c3 += 1
if c1:
    a = c1 + min(c2, c3) if c2 + c3 > 0 else c1 - 1
else:
    a = min(c2, c3)

print(t.count("AB") + a)