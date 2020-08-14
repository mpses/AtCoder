#!/usr/bin/env python3
from collections import*
c = Counter([input() for _ in [None]*int(input())])
for i in ["AC", "WA", "TLE", "RE"]:
    print(i, "x", c.get(i, 0))