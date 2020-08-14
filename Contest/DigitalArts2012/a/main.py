#!/usr/bin/env python3
import re
s, n, *t = open(0)
s = s.split()
for i, j in enumerate(s):
    for k in t:
        if re.fullmatch(k.strip().replace("*","."), j):
            s[i] = "*" * len(j)
print(*s)