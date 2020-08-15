#!/usr/bin/env python3
from itertools import*
d = [len(list(l)) for k, l in groupby(input()) if k == "R"]
print(max(d) if d else 0)