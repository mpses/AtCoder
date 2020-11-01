#!/usr/bin/env python3
from itertools import*
print(max(len([*l]) * k for k, l in groupby([len(set(o.split())) == 1 for o in open(0)][1:])) >= 3 and "Yes" or "No")
