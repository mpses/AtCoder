#!/usr/bin/env python3
s, _, *i = open(0).read().replace(" ", "").split()
for j in sorted(i, key = lambda a: int(a.translate(str.maketrans(s, "0123456789")))):
    print(j)